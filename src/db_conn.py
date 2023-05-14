from sqlalchemy import create_engine
from dotenv import load_dotenv
import os
load_dotenv()

db_user = os.getenv('POSTGRES_USER')
db_password = os.getenv('POSTGRES_PASSWORD')
db_db = os.getenv('POSTGRES_DB')

db_url = f"postgresql://{db_user}:{db_password}@localhost:5432/{db_db}"

engine = create_engine(db_url)

conn = engine.connect()
