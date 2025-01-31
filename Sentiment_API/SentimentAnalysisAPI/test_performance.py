import asyncio
import httpx
import time
import csv
import pytest

# Enable pytest-asyncio
pytest_plugins = "pytest_asyncio"

# API URL
API_URL = "http://127.0.0.1:8000/analyze/"

# Authorization token (replace with a valid token)
#<enter the token from postman as i have showed into the documentation>
HEADERS = {
    "Authorization": "Bearer <enter the token>"
}

# Function to read reviews from CSV
def read_reviews_from_csv(file_path):
    reviews = []
    with open(file_path, mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            reviews.append({"user_id": int(row["user_id"]), "review_text": row["review_text"]})
    return reviews

# Function to send a request with a review from CSV
async def send_request(review):
    async with httpx.AsyncClient() as client:
        response = await client.post(API_URL, json=review, headers=HEADERS, timeout=30)
        return response.status_code, response.json()

# Main test function using pytest
@pytest.mark.asyncio
async def test_performance():
    start_time = time.time()
    
    reviews = read_reviews_from_csv("reviews.csv")  # Load reviews from CSV
    
    # Simulating concurrent requests for all reviews in CSV
    tasks = [send_request(review) for review in reviews]
    results = await asyncio.gather(*tasks)

    end_time = time.time()
    
    # Test Assertions
    successful_responses = sum(1 for status, _ in results if status == 200)
    failed_responses = sum(1 for status, _ in results if status != 200)

    print(f"Total Execution Time: {end_time - start_time:.2f} seconds")
    print(f"Successful Responses: {successful_responses}")
    print(f"Failed Responses: {failed_responses}")

    # Ensure at least one response is successful
    assert successful_responses > 0, "No successful API responses!"
