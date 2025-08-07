import requests
import json

from queenList import queenList 
from spotifyAuth import accessToken

def getQueens():
    queenIds = map(lambda x: x[1], queenList)
    queenIdsFormatted = ','.join(queenIds)

    url = 'https://api.spotify.com/v1/artists'

    headers = {
        'Authorization': f'Bearer {accessToken}'
    }

    params = {
        'ids': queenIdsFormatted
    }

    response = requests.get(url, headers=headers, params=params)
    return response.json()['artists']