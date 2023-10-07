from modules.request import request

params = {
    'order': 'desc',
    'targy': '',
    'kategoria': '',
    'forrasIntezmenyNeve': '',
    'ugyiratSzamIktatasiSzam': '',
    'telepules': '',
    'nev': '',
    'idoszak': '',
    'adottNap': '',
    'szo': '',
    'pageIndex': '0',
    'pageSize': '1',
    'sort': 'kifuggesztesNapja'
}


def getAnnouncements():

    try:
        params['pageSize'] = getTotalAnnouncements('/api/hirdetmenyek')
        response = request('/api/hirdetmenyek', params=params)

        return response.json()['rows']

    except Exception:
        raise (Exception)


def getTotalAnnouncements(uri):

    try:
        params['pageSize'] = '1'
        response = request(uri, params=params)
        return str(response.json()['total'])

    except Exception:
        raise (Exception)
