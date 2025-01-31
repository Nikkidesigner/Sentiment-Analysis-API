# Sentiment Analysis API

## Overview
This project is a **Sentiment Analysis API** built using **FastAPI**. It provides an endpoint to analyze the sentiment of given text data. The API leverages **TextBlob** for natural language processing and sentiment analysis. Authentication is implemented using **JWT tokens**, and **SQLAlchemy** is used for database interactions.

## Features
- **User Authentication**: Secure login and JWT-based authentication.
- **Sentiment Analysis**: Analyze the sentiment of text (Positive, Negative, Neutral) using TextBlob.
- **Database Integration**: Uses SQLAlchemy for managing user and text history.
- **Token-based Security**: Ensures secure API access with JWT tokens.

## Technologies Used
- **FastAPI**: For building the web framework.
- **SQLAlchemy**: For database management.
- **TextBlob**: For sentiment analysis.
- **PyJWT**: For handling authentication tokens.
- **Uvicorn**: ASGI server to run FastAPI.

## Installation
### Prerequisites
Ensure you have **Python 3.9+** installed.

### Steps
1. Clone the repository:
   ```sh
   git clone https://github.com/Nikkidesigner/Sentiment-Analysis-API.git
   cd Sentiment-Analysis-API
   ```

2. Create a virtual environment:
   ```sh
   python -m venv venv
   ```

3. Activate the virtual environment:
   - Windows:
     ```sh
     venv\Scripts\activate
     ```
   - Mac/Linux:
     ```sh
     source venv/bin/activate
     ```

4. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Usage
### Running the API
Start the server using:
```sh
uvicorn main:app --reload
```
The API will be available at: **http://127.0.0.1:8000**

### Endpoints
#### 1. **User Authentication**
- **Login**: `POST /login`
- **Register**: `POST /register`

#### 2. **Sentiment Analysis**
- **Analyze Sentiment**: `POST /analyze`
  - **Request Body:**
    ```json
    {
      "text": "I love FastAPI!"
    }
    ```
  - **Response:**
    ```json
    {
      "sentiment": "Positive",
      "polarity": 0.9
    }
    ```

## Deployment
To deploy the API, you can use **Docker**, **AWS**, or **Heroku**.

## Contributing
Feel free to fork this repository and submit pull requests for improvements.

## License
This project is open-source and available under the **MIT License**.

---
_Developed by [Nikkidesigner](https://github.com/Nikkidesigner)_

