import requests
from datetime import datetime

from spotifyAuth import accessToken

timeWeight = 0.25
popWeight = 0.75

def lastAlbum(queen):
    url = f'https://api.spotify.com/v1/artists/{queen['id']}/albums'
    headers = {
        'Authorization': f'Bearer {accessToken}'
    }

    response = requests.get(url, headers=headers)
    albums = response.json()['items']

    return max(albums, key=lambda album: album['release_date'])

def queenScore(queen):
    popularity = queen['popularity']
    lastAlbumReleaseStr = lastAlbum(queen)['release_date']
    now = datetime.now()
    lastAlbumRelease = datetime.strptime(lastAlbumReleaseStr, "%Y-%m-%d")
    diff = now - lastAlbumRelease
    diffDays = diff.days
    #-.6945(months)^2 + 100
    timeliness = ((diffDays / 30) ** 2 * -0.6945) + 100
    return (timeWeight * timeliness + popWeight * popularity)