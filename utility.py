import requests


def fetch_api(api):
    """ Fetch the contents of an API """
    response = requests.get(api)
    if response.status_code < 200 or 299 < response.status_code:
        raise Exception("The following API is not available: " + api + ". Status code: " + response.status_code + ".")
    return response.json()
