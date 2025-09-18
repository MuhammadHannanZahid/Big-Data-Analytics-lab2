import os
from sqlalchemy import create_engine, text
from dotenv import load_dotenv

# Load variables from .env file
load_dotenv()

# Read variables
user = os.getenv("POSTGRES_USER")
password = os.getenv("POSTGRES_PASSWORD")
db = os.getenv("POSTGRES_DB")
port = os.getenv("POSTGRES_PORT", "5432")
host = os.getenv("POSTGRES_HOST", "localhost")

# Build SQLAlchemy connection string
DATABASE_URL = f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{db}"
print("Connecting to:", DATABASE_URL)

# Create engine
engine = create_engine(DATABASE_URL)

try:
    with engine.connect() as conn:
        result = conn.execute(text("SELECT 1"))
        print("✅ Connection successful! Result:", result.scalar())
except Exception as e:
    print("❌ Connection failed:", e)
