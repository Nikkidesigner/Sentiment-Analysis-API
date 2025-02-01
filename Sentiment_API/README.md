# Sentiment Analysis API

Hello I'm Nikhil Pawar. I'm working on the  **Sentiment Analysis API**! 🚀 This API allows you to analyze the sentiment of text using **FastAPI**, **TextBlob**, and **SQLAlchemy** for managing user authentication and database operations.

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
$ cd SentimentAnalysisAPI
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


To ensure the API works correctly, I performed the following checks:
- Sent a **single API request** and verified the **correct sentiment analysis response**.
- Checked the **database entry** to confirm that the review was stored properly.
- Examined the **logs** to ensure they recorded API requests appropriately.



### 1. Generating Token in Postman (Functional Testing)
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


#  Running and Testing the Sentiment Analysis API

## 1️⃣ Starting the API Server
To begin, we need to start the **FastAPI server** from one terminal inside the virtual environment.

### **Step 1: Activate Virtual Environment**
```bash
# Windows
$ venv\Scripts\activate

# macOS/Linux
$ source venv/bin/activate
```

### **Step 2: Start the API Server**
```bash
$ uvicorn main:app --reload
```

This will start the API server at **http://127.0.0.1:8000**.

📌 **Screenshot: Running API Server**

![starting server](https://github.com/user-attachments/assets/cfa86806-98eb-4533-ac37-34fc39abf0d1)

---

## 2️⃣ Running the Performance Tests
After the server is running, we use a **separate terminal** to execute the performance tests.

### **Step 1: Open a New Terminal and Activate Virtual Environment**
```bash
# Windows
$ venv\Scripts\activate

# macOS/Linux
$ source venv/bin/activate
```
### **Step 2: Install pytest Inside the Virtual Environment**
Once the virtual environment is activated, run:
```bash
pip install pytest pytest-asyncio httpx
```


### **Step 3: Run the Performance Test**
```bash
$ pytest test_performance.py -v
```

📌 **Screenshot: Running Performance Tests**

![running test](https://github.com/user-attachments/assets/7bd19316-9e9a-49d6-b107-96597160a02c)

---

## 3️⃣ How I Implemented Performance Testing
To ensure the API can handle concurrent requests efficiently, I performed:
- **Functional Testing**: Sending a single request and verifying the response.
- **Performance Testing**: Sending multiple concurrent requests using `pytest` and `httpx`.
- **Metrics Tracking**: Storing execution time and response data in `metrics.csv`.

### **How I Used `metrics.csv`**
1. Each API request logs its response time, sentiment analysis result, and user ID into `metrics.csv`.
2. This helps track API performance and identify slow responses.


📌 **Screenshot: `metrics.csv` file from DB Browser for SQLite**


![sqllite database](https://github.com/user-attachments/assets/ec6bfa00-b815-42c4-8410-6d129ff2bbad)


---

## 4️⃣ How I Used `reviews.txt`
To automate testing, I created `reviews.txt`, which contains different test strings. This is used in `test_performance.py`:
- Reads each line as a test input.
- Sends the input to `/analyze` endpoint.
- Logs the results in `metrics.csv`.





## 5️⃣ Additional Package Requirements
To ensure smooth execution, I updated `requirements.txt` with all necessary dependencies:
```plaintext
fastapi
uvicorn
sqlalchemy
textblob
pyjwt
pydantic
httpx
pytest
pytest-asyncio
passlib
bcrypt
csv
asyncio
```
These dependencies ensure:
- FastAPI runs correctly.
- Authentication and encryption work.
- Performance tests execute without issues.

---
## Referenece tutorials I used :

- Working with JWTs in Python (https://youtu.be/VRn8cPc7B_w?si=i4QJOp-rvmJPWwf8)
- Exploring Sentiment Analysis using TextBlob (https://youtu.be/wfFTjQckbdA?si=KWZ8RZIqvNfG9z7S)
- FastAPI Creating Models using Pydantic (https://youtu.be/GkrDmUEEEtM?si=DLn8ulx6jNZ_UUtf)
- How to Work with CSV Files in Python (https://youtu.be/sfTUVXfC0X0?si=KBRwmfsrlsCxP7LS)
- Python : Adding/Appending Data to CSV Files (https://youtu.be/sHf0CJU8y7U?si=SvWuc56Tme9YGci5)
- FastAPI MySQL REST API in Python | CRUD Operations | SQLAlchemy (https://youtu.be/4Zy90rd0bkU?si=L1HfYQ8S44pfrL4Y)
- Testing Our Application with Pytest and Pytest-Asyncio (https://youtu.be/fsRE5xflofI?si=9HqZNIVtKqm92jYb)
- HTTPX Tutorial - A next-generation HTTP client for Python (https://youtu.be/qAh5dDODJ5k?si=W4Z7tyiNTmnlTQ3W)


## 🎯 Final Thoughts
By following these steps, I successfully tested API performance while ensuring correctness and efficiency. The setup allows for **scalable testing** and **real-time sentiment tracking**.



> Created by **Nikhil Pawar** ✨

