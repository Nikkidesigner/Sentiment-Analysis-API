# Sentiment Analysis API

Welcome to the **Sentiment Analysis API**! 🚀 This API allows you to analyze the sentiment of text using **FastAPI**, **TextBlob**, and **SQLAlchemy** for managing user authentication and database operations.

## What i have added into the task according to the requirements :
- **User Authentication**: Secure login using JWT tokens
- **Sentiment Analysis**: Analyze text sentiment (positive, neutral, negative)
- **FastAPI-based**: High-performance and easy-to-use REST API
- **Database Integration**: Uses **SQLAlchemy** for data management

## Installation
To set up and run this project, follow these steps:

### 1. Clone the Repository
```bash
$ git clone https://github.com/Nikkidesigner/Sentiment-Analysis-API.git
$ cd Sentiment-Analysis-API
```

### 2. Create and Activate a Virtual Environment
```bash
# Windows
$ python -m venv venv
$ venv\Scripts\activate

# macOS/Linux
$ python -m venv venv
$ source venv/bin/activate
```

### 3. Install Dependencies
```bash
$ pip install -r requirements.txt
```

### 4. Run the API Server
```bash
$ uvicorn main:app --reload
```
The API will be running at **http://127.0.0.1:8000**.

## API Endpoints

### 1. User Login (JWT Authentication)
**POST** `/login`
```json
{
  "username": "admin",
  "password": "password"
}
```
_Response:_
```json
{
  "access_token": "your_jwt_token",
  "token_type": "bearer"
}
```

### 2. Sentiment Analysis
**POST** `/analyze`
#### Headers:
```json
{
  "Authorization": "Bearer your_jwt_token"
}
```
#### Request Body:
```json
{
  "text": "I love this product!"
}
```
_Response:_
```json
{
  "sentiment": "positive"
}
```
#### Request Body:
```json
{
  "text": "I did not like the flavour!"
}
```
_Response:_
```json
{
  "sentiment": "negative"
}
```

## How to Use in Postman
1. **Login** using `/login` to get a JWT token.
2. **Copy the access token** from the response.
3. **Go to the `/analyze` endpoint**, click on **Authorization** in Postman.
4. Select **Bearer Token** and paste your copied token.
5. Send the request with a text input.


> Created by **Nikhil Pawar** ✨

