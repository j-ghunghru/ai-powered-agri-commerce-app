# AI-Powered-Agri-Commerce Backend API (FastAPI + SQLite)

This backend is built using **FastAPI**, **SQLAlchemy**, and **SQLite** to support an AI-powered agri-commerce platform for farmers and buyers.

---

## Features Implemented

### User Module
- `POST /users/register` – Register new users (`farmer` or `buyer`)
- `POST /users/login` – Login with phone number & password (returns JWT)
- `GET /users/me` – Get currently logged-in user's profile (JWT-secured)
- `GET /users/{user_id}` – Get user by ID
- `GET /users/` – List all registered users

### Produce Module
- `POST /produce/` – Publish a produce listing (JWT-secured, farmers only)
- `GET /produce/` – List all published produce
- `GET /produce/{produce_id}` – Get produce by ID

---

## Authentication

- JWT-based login (`/users/login`)
- Protected routes use `OAuth2PasswordBearer`
- Tokens carry `user_id` and `role` in payload
- `create_access_token()` and `decode_access_token()` are in `services/auth.py`

---

## Environment Configuration

### `.env` file (at project root):
```env
SQLALCHEMY_DATABASE_URL=sqlite:///./agri_app.db
```

### `app/config.py`
Loads the `.env` file and sets:
```python
SQLALCHEMY_DATABASE_URL = os.getenv("SQLALCHEMY_DATABASE_URL", "sqlite:///./agri_app.db")
```

---

## Models

### User Model (`models/user.py`)
- `user_id`, `name`, `email`, `password_hash`, `role`, `location`, `phone_number`, `created_at`
- Role is constrained to `farmer` or `buyer`

### Produce Model (`models/produce.py`)
- `id`, `farmer_id`, `crop`, `category`, `price_per_unit`, `unit`, `quantity`, `grade`, `lat`, `lon`, `tags`, `listing_date`, `description`, `image_url`, `status`, `location`

---

## Mock Data for Testing

- Seeded automatically using `app/db/mockdata.py`
- Triggered from `init_db()` in `app/db/session.py`
- Inserts:
  - 10 Farmers
  - 10 Buyers
  - 20 Produce Listings

---

## Getting Started

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Run the app
```bash
uvicorn app.main:app --reload
```

### 3. Access the API docs
Visit: [http://localhost:8000/docs](http://localhost:8000/docs)

---

## Project Structure
```
backend/
├── .env
└── app/
    ├── main.py
    ├── config.py
    ├── models/
    ├── schemas/
    ├── routers/
    ├── services/
    ├── db/
    └── tests/
```

---

## Auto Database Setup
- On startup, `init_db()`:
  - Creates all tables using SQLAlchemy models
  - Seeds mock data if empty

---

## Notes
- SQLite used for local development (can be swapped for PostgreSQL)
- `.env`-based config with `python-dotenv` support
- Clean modular architecture: `models`, `schemas`, `routers`, `services`, `db`

---