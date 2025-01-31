import logging
from fastapi import FastAPI, HTTPException, Depends,Request
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base
from textblob import TextBlob
import jwt
import datetime
from jwt.exceptions import ExpiredSignatureError, InvalidTokenError
from passlib.context import CryptContext

# Logging setup
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

app = FastAPI()

# Secret key for JWT
SECRET_KEY = "your_secret_key_here"
ALGORITHM = "HS256"

# Password hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Database Setup
DATABASE_URL = "sqlite:///./database.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Define Database Model
class Feedback(Base):
    __tablename__ = "feedback"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer)
    review_text = Column(String)
    sentiment = Column(String)
    confidence = Column(Integer)

# Create Tables
Base.metadata.create_all(bind=engine)
logger.info("Database setup complete")

# Pydantic Models
class Review(BaseModel):
    user_id: int
    review_text: str

class UserLogin(BaseModel):
    username: str
    password: str

# Function to create JWT token
def create_jwt_token(data: dict, expires_delta: int = 60):
    expire = datetime.datetime.utcnow() + datetime.timedelta(minutes=expires_delta)
    to_encode = data.copy()
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

# Function to verify JWT token
def verify_jwt_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token has expired")
    except InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")

# Login Route to Generate JWT Token
@app.post("/login")
def login(user: UserLogin):
    # Hardcoded example credentials (Replace with database validation)
    if user.username == "admin" and user.password == "password":
        token = create_jwt_token({"sub": user.username})
        return {"access_token": token, "token_type": "bearer"}
    raise HTTPException(status_code=401, detail="Invalid username or password")

# Protected Route - Requires Token
@app.post("/analyze/")
def analyze_sentiment(review: Review, request: Request):
    # Extract the token from the Authorization header
    authorization: str = request.headers.get("Authorization")
    if not authorization:
        raise HTTPException(status_code=401, detail="Authorization token is missing")
    
    token = authorization.split(" ")[1]  # Assuming the header is like "Bearer <token>"
    user_payload = verify_jwt_token(token)  # Verify the token and extract user data

    # Now, proceed with sentiment analysis
    analysis = TextBlob(review.review_text)
    sentiment = "positive" if analysis.sentiment.polarity > 0 else "negative" if analysis.sentiment.polarity < 0 else "neutral"
    confidence = abs(analysis.sentiment.polarity) * 100

    db = SessionLocal()
    feedback = Feedback(user_id=review.user_id, review_text=review.review_text, sentiment=sentiment, confidence=confidence)
    db.add(feedback)
    db.commit()
    db.refresh(feedback)
    db.close()

    logger.info(f"Sentiment Analysis: {review.review_text} -> {sentiment} ({confidence}%)")

    return {"user_id": review.user_id, "sentiment": sentiment, "confidence": confidence}

@app.get("/")
def read_root():
    return {"message": "Welcome to Sentiment Analysis API"}
