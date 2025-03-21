
# Get Hint ! -- Python Backend

A modern, scalable asset management platform and stock predictor built with FastAPI and SQLAlchemy. Features include portfolio tracking, stock market integration, user authentication, and subscription management. Designed with clean architecture principles


![CodeRabbit Pull Request Reviews](https://img.shields.io/coderabbit/prs/github/gethintcompany/gethint_backend?utm_source=oss&utm_medium=github&utm_campaign=gethintcompany%2Fgethint_backend&labelColor=171717&color=FF570A&link=https%3A%2F%2Fcoderabbit.ai&label=CodeRabbit+Reviews)

## Contributing

Contributions are always welcome!

See `contributing.md` for ways to get started.

Please adhere to this project's `code of conduct`.


## Project setup

### Prerequisites
- Python 3.9 or higher
- pip package manager

#### 1. Create Virtual Environment
```bash
python -m venv venv
```

#### 2. Activate Virtual Environment
```bash
venv\Scripts\activate
```
#### 3. Dectivate Virtual Environment
```bash
deactivate
```
#### 4. Install Required package
```bash
pip install -r requirements.txt
```

### Run the FastAPI app with Uvicorn:
```
uvicorn app:main --reload
```
#### Interactive API documentation:
Swagger UI: http://127.0.0.1:8000/docs

ReDoc: http://127.0.0.1:8000/redoc

-end