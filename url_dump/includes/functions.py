import requests

def validate_url(url):
    try:
        result = requests.get(url)
        if result.status_code == 200:
            return True
        else:
            return False
    except:
        return False