from app.repositories.user_repository import UserRepository


class UserService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    async def get_user(self, email: str):
        return await self.user_repository.get_user_by_email(email)