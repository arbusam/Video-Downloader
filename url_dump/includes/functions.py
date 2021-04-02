import requests

def validate_url(url):
    if "https://www.youtube.com/" in url or "https://youtu.be/" in url:
        try:
            result = requests.get(url)
            if result.status_code == 200:
                return True
            else:
                return False
        except:
            return False
    else:
        return False