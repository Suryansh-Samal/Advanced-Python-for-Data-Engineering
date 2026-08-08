import requests

def api_calls(url:str):
    import requests
    response = requests.get(url)
    return {"data" : response.json()}

