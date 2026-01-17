# Uncomment the imports below before you add the function code
import requests
import os
from dotenv import load_dotenv


load_dotenv()

backend_url = os.getenv(
    'backend_url', default="http://localhost:3030")
sentiment_analyzer_url = os.getenv(
    'sentiment_analyzer_url',
    default="http://localhost:5050/")


# def get_request(endpoint, **kwargs):
def get_request(endpoint, **kwargs):
    params = ""
    if (kwargs):
        for key, value in kwargs.items():
            params = params+key+"="+value+"&"

    request_url = backend_url+endpoint+"?"+params

    print("GET from {} ".format(request_url))
    try:
        # Call get method of requests library with URL and parameters
        response = requests.get(request_url, timeout=10)
        print(f"Response status: {response.status_code}")
        print(f"Response headers: {response.headers.get('content-type')}")
        
        if response.status_code == 200:
            data = response.json()
            print(f"Success: Got {len(data) if isinstance(data, list) else 'dict'} items")
            return data
        else:
            print(f"Error: Status {response.status_code}")
            return []
    except Exception as err:
        # If any error occurs
        print(f"Exception: {err}")
        return []


# def analyze_review_sentiments(text):
def analyze_review_sentiments(text):
    request_url = sentiment_analyzer_url+"analyze/"+text
    try:
        # Call get method of requests library with URL and parameters
        response = requests.get(request_url)
        return response.json()
    except Exception as err:
        print(f"Unexpected {err=}, {type(err)=}")
        print("Network exception occurred")


# def post_review(data_dict):
# Add code for posting review
def post_review(data_dict):
    request_url = backend_url+"/insert_review"
    try:
        response = requests.post(request_url, json=data_dict, timeout=10)
        print(f"Review posted: {response.status_code}")
        return response.json()
    except Exception as err:
        print(f"Error posting review: {err}")
        return {"error": str(err)}
    request_url = backend_url+"/insert_review"
    try:
        response = requests.post(request_url, json=data_dict)
        print(response.json())
        return response.json()
    except Exception as err:
        print(f"Unexpected {err=}, {type(err)=}")
        print("Network exception occurred")
