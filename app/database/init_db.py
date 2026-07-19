from app.database.base import Base
from app.database.database import engine
from app.database.database import DATABASE_URL


print(DATABASE_URL)  # Print the database URL to verify it's being read correctly
#import all models here to ensure they are registered with SQLAlchemy
from app.models.resume import Resume

Base.metadata.create_all(bind=engine)  # Create all tables in the database


