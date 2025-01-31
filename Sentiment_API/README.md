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

## Postman API Testing

### 1. Generating Token in Postman
To generate a JWT token, send a `POST` request to `/login` with valid credentials.

![generate_token](https://github.com/user-attachments/assets/d9641fd1-65f4-485c-bbdf-7252c7521169)

---

### 2. Using the Token in `/analyze` Route
After receiving the token, include it in the `Authorization` header as `Bearer <your_token>`.


![token input](https://github.com/user-attachments/assets/00353177-7d89-40fd-988b-804e5680e5c9)

---

### 3. Sending a Post Request to `/analyze`
Now, send a `POST` request to `/analyze` with a review text. The response will contain the sentiment analysis result.


![post request](https://github.com/user-attachments/assets/ffd19ad9-180c-4147-9dcd-de16576c1f3b)



> Created by **Nikhil Pawar** ✨

