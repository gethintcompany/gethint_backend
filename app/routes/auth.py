from fastapi import APIRouter
from app.controllers.auth_controller import AuthController

router = APIRouter()
auth_controller = AuthController()

@router.post("/login")
async def login(email: str, password: str):
    return await auth_controller.login(email, password)