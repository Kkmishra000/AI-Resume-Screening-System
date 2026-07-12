from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os   

load_dotenv()  # Load environment variables from .env file

DATABASE_URL = os.getenv("DATABASE_URL")  # Get the database URL from environment variables

if DATABASE_URL is None:
    raise ValueError("DATABASE_URL environment variable is not set.")


engine = create_engine(DATABASE_URL , echo=True)  # Create the SQLAlchemy engine with the database URL

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


