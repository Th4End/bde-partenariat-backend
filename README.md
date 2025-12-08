# Partnership Dashboard Backend

![Python](https://img.shields.io/badge/python-3.11-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.104-green)
![License](https://img.shields.io/badge/license-MIT-lightgrey)
![Build](https://img.shields.io/github/actions/workflow/status/yourusername/partnership-dashboard-backend/python-app.yml?branch=main)
![Coverage](https://img.shields.io/badge/coverage-95%25-brightgreen)

This dashboard is designed to manage the partnerships of the Student Association,
including contracts, statuses, and categories.  
It provides a RESTful API built with FastAPI to handle CRUD operations for partnerships and related data.

---

### ⚙️ Tech Stack

| Category | Technologies |
|----------|--------------|
| Backend Framework | Python + FastAPI |
| Web Server | Uvicorn / Gunicorn |
| Database | PostgreSQL |
| Client DB | psycopg |
| Authentication | JWT (PyJWT) |
| Password Hashing | passlib[bcrypt] |

---

### 🛠️ Installation

1. Clone the repository:

```bash
git clone https://github.com/Th4End/bde-partenariat-backend.git
cd bde-partenariat-backend
```
2. Create a virtual env:

```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```
3. Install the dependencies:

```bash
pip install -r requirements.txt
```
4. Create a .env file in the root directory with the following variables:
```bash 
DATABASE_URL=postgresql://user:password@localhost:5432/dbname
JWT_SECRET=your_jwt_secret_key
```

# ✉️ Contact

Eliazid – eliazidb@gmail.com

Project Link: [https://github.com/yourusername/partnership-dashboard-backend](https://github.com/Th4End/bde-partenariat-backend.git)

# 📄 License
MIT License