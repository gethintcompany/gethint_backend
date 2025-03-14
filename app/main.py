from fastapi import FastAPI
from app.routes import auth, portfolio

app = FastAPI()

app.include_router(auth.router)
app.include_router(portfolio.router)

@app.get("/")
async def root():
    return {"message": "Asset Management System"}