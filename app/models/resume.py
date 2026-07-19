from datetime import datetime



from sqlalchemy import Column, Integer, String, DateTime,Text
from sqlalchemy.orm import Mapped, mapped_column

from app.database.base import Base


class Resume(Base):
    __tablename__ = "resumes"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    pdf_path: Mapped[str] = mapped_column(String(500), nullable=False)
    extracted_text: Mapped[str] = mapped_column(Text, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    