import requests

def fetch_data(api_url, params=None):
    response = requests.get(api_url, params=params)
    if response.status_code == 200:
        return response.json()
    return {"error": "Failed to fetch data"}
