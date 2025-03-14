from fastapi import Depends, HTTPException
from app.services.user_service import UserService


class AuthController:
    def __init__(self, user_service: UserService):
        self.user_service = user_service

    async def login(self, email: str, password: str):
        user = await self.user_service.get_user(email)
        # Add authentication logic
        return {"access_token": "..."}