from sqlalchemy.orm import Session
from app.models.user import User


class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    async def get_user_by_email(self, email: str):
        return self.db.query(User).filter(User.email == email).first()