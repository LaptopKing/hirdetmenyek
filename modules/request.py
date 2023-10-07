import requests


def request(uri, params=None):

    try:
        baseUrl = "https://hirdetmenyek.gov.hu"
        url = baseUrl + uri

        if (params is None):

            response = requests.get(url, verify=False)
            checkResponseStatusCode(response)
            return response

        response = requests.get(url, verify=False, params=params)
        checkResponseStatusCode(response)
        return response

    except Exception:
        raise (Exception)


def checkResponseStatusCode(response):

    if (response.status_code != 200):
        errMsg = f"Status code is not 200, \
                instead it is {response.status_code}!"
        raise (errMsg)
