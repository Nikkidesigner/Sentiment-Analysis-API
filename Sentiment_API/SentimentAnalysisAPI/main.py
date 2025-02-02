import logging
import time
import csv
import uuid
from fastapi import FastAPI, HTTPException, Depends, Request
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base
from textblob import TextBlob
import jwt
import datetime
from jwt.exceptions import ExpiredSignatureError, InvalidTokenError
from passlib.context import CryptContext
from fastapi.middleware.cors import CORSMiddleware


origins = [
    "http://localhost:3000/login",
    "http://localhost:3000/analyze",
    "http://localhost:3000",
    "https://sentiment-frontend-dun.vercel.app"
]

# Logging setup
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

app = FastAPI()


#middleware 
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Secret key for JWT
SECRET_KEY = "MYSerjnjdnfjfenvjernvjiernvjenrvjnervjnerjvnerjnv"

ALGORITHM = "HS256"

# Password hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Database Setup
DATABASE_URL = "sqlite:///./database.db"
engine = create_engine(DATABASE_URL, echo=True, connect_args={"check_same_thread": False})
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
def create_jwt_token(data: dict, expires_delta: int = 60*24):
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
    if user.username == "admin" and user.password == "password":
        token = create_jwt_token({"sub": user.username})
        return {"access_token": token, "token_type": "bearer"}
    raise HTTPException(status_code=401, detail="Invalid username or password")

# Function to log metrics
def log_metrics(request_id, user_id, review_text, sentiment, confidence, execution_time):
    with open("metrics.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([
            datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            request_id,
            user_id,
            review_text,
            sentiment,
            confidence,
            execution_time
        ])

# Protected Route - Requires Token
@app.post("/analyze/")
def analyze_sentiment(review: Review, request: Request):
    start_time = time.time()
    request_id = str(uuid.uuid4())

    authorization: str = request.headers.get("Authorization")
    if not authorization:
        raise HTTPException(status_code=401, detail="Authorization token is missing")
    
    token = authorization.split(" ")[1]  # Extract token from header
    user_payload = verify_jwt_token(token)  # Verify JWT
    
    analysis = TextBlob(review.review_text)
    sentiment = "positive" if analysis.sentiment.polarity > 0 else "negative" if analysis.sentiment.polarity < 0 else "neutral"
    confidence = abs(analysis.sentiment.polarity) * 100

    db = SessionLocal()
    feedback = Feedback(user_id=review.user_id, review_text=review.review_text, sentiment=sentiment, confidence=confidence)
    db.add(feedback)
    db.commit()
    db.refresh(feedback)
    db.close()

    execution_time = round(time.time() - start_time, 4)
    log_metrics(request_id, review.user_id, review.review_text, sentiment, confidence, execution_time)

    logger.info(f"Request ID: {request_id} | Sentiment Analysis: {review.review_text} -> {sentiment} ({confidence}%) | Execution Time: {execution_time}s")

    return {"request_id": request_id, "user_id": review.user_id, "sentiment": sentiment, "confidence": confidence, "execution_time": execution_time}

@app.get("/")
def read_root():
    return {"message": "Welcome to Sentiment Analysis API"}
