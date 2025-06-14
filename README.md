# AI Powered Agri Commerce App

- Frontend: React.js
- Backend: FastAPI
- DB: SQLite
- BEKN Workflow: YAML in `bekn/`

Start backend:
```bash
python -m venv venv
pip install -r backend\app\requirements.txt
cd backend
uvicorn app.main:app --reload
```