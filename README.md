
# Base End API

Base End is a modular FastAPI-based application that supports different types of APIs, such as MyBaseWeb (a web system) and Financial (a financial data system). It uses separate databases for different parts of the system.

## Project Structure

```
base_end/
├── main.py                  # Main FastAPI entry point
├── config.py                # Configuration (database connections, settings)
├── routers/                 # API route definitions
│   ├── mybaseweb.py         # API routes for "mybaseweb"
│   ├── financial.py         # API routes for "financial"
├── services/                # Business logic and services
│   ├── mybaseweb_service.py # Business logic for "mybaseweb"
│   ├── financial_service.py # Business logic for "financial"
├── models/                  # SQLAlchemy models (different for each domain)
│   ├── mybaseweb_models.py  # Models for "mybaseweb"
│   ├── financial_models.py  # Models for "financial"
├── database/                # Database connection files
│   ├── mybaseweb_db.py      # Database connection for "mybaseweb"
│   ├── financial_db.py      # Database connection for "financial"
```

### Technologies

- **Python**: 3.9+
- **FastAPI**: Web framework
- **SQLAlchemy**: ORM (Object Relational Mapper)
- **MySQL**: Database for MyBaseWeb API
- **PostgreSQL**: Database for Financial API

## Setup and Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-repo/base_end.git
cd base_end
```

### 2. Create a Virtual Environment

It’s recommended to use a virtual environment to manage dependencies.

```bash
python3 -m venv env
source env/bin/activate  # On Linux/MacOS
env\Scripts\activate     # On Windows
```

### 3. Install Dependencies

Install the required dependencies from the `requirements.txt` file (if you have one) or install manually.

```bash
pip install fastapi uvicorn sqlalchemy mysql-connector-python psycopg2
```

### 4. Configure Your Databases

Open the `config.py` file and update the database connection strings for your MySQL (MyBaseWeb) and PostgreSQL (Financial) databases.

```python
# config.py
MYBASEWEB_DATABASE_URL = "mysql+mysqlconnector://user:password@localhost:3306/mybaseweb_db"
FINANCIAL_DATABASE_URL = "postgresql://user:password@localhost:5432/financial_db"
```

### 5. Create Databases and Tables

You will need to manually create the databases and run migrations (if necessary).

For **MySQL** (MyBaseWeb):

```sql
CREATE DATABASE mybaseweb_db;
```

For **PostgreSQL** (Financial):

```sql
CREATE DATABASE financial_db;
```

You can use SQLAlchemy’s `create_all()` if you want to auto-generate tables based on the models.

### 6. Run the Application

Start the FastAPI application with Uvicorn:

```bash
uvicorn base_end.main:app --reload
```

The API will be running at `http://127.0.0.1:8000`.

### 7. Access API Documentation

FastAPI provides interactive documentation for your APIs.

- **Swagger UI**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **ReDoc**: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## API Overview

### MyBaseWeb API

- **GET /posts/**: Fetch all blog posts
- **POST /posts/**: Create a new blog post

Example request for creating a new post:
```json
{
  "title": "My First Post",
  "content": "This is the content of my first post."
}
```

### Financial API

- **GET /financial-data/**: Fetch all financial data
- **POST /analyze/**: Analyze financial data

Example request for analyzing data:
```json
{
  "company": "ABC Corp",
  "revenue": 1000000,
  "expenses": 500000
}
```

## Future Improvements

- Add authentication and authorization (e.g., OAuth2, JWT)
- Implement background tasks for financial data processing
- Add unit and integration tests
