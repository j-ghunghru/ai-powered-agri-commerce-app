from fastapi import APIRouter, Depends, HTTPException, Header
from jose import jwt, JWTError
from app.models.user import User
from app.db.session import get_db
from sqlalchemy.orm import Session

SECRET_KEY = "supersecretkey"
ALGORITHM = "HS256"

router = APIRouter()

@router.get("/me")
def get_current_user(authorization: str = Header(...), db: Session = Depends(get_db)):
    try:
        scheme, token = authorization.split()
        if scheme.lower() != "bearer":
            raise HTTPException(status_code=403, detail="Invalid authentication scheme")
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")
        if not username:
            raise HTTPException(status_code=403, detail="Invalid token payload")
    except (JWTError, ValueError):
        raise HTTPException(status_code=403, detail="Invalid or expired token")

    user = db.query(User).filter(User.username == username).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return {"id": user.id, "username": user.username, "role": user.role}