import http_client
from base64 import b64encode

endpoint = 'https://api.spotify.com/v1'

def encode(string):
    # base 64 encode this string
    return b64encode(bytes(string, "utf-8")).decode("utf-8")

class MicroSpotipy:
    def __init__(self, client_id, client_secret):
        self.client_id = client_id
        self.client_secret = client_secret

    def get(self, url, authToken=None):
        # pass auth header
        r = None
        if authToken != None:
            r = http_client.request("GET",
                                    url,
                                    "",
                                    None,
                                    {"Authorization": "Bearer "+authToken})

        else:
            r = http_client.get(url)

        if r.status_code >= 500:
            raise OSError("Server error")
        if r.status_code == 404:
            raise OSError("Resource not found")

        if authToken is None and r.status_code != 200:
            if authToken != None:
                raise OSError("Failed to authenticate")
            auth_token = self.client_auth()
            return self.get(url, auth_token)
        return r.json()

    def client_auth(self):
        code = self.client_id+":"+self.client_secret
        r = http_client.request("POST",
                                "https://accounts.spotify.com/api/token",
                                "grant_type=client_credentials",
                                None,
                                {"Authorization":"Basic "+encode(code)})
        return r.json()["access_token"]

    def albums(self, id):
        # if typeof id = 'list': format query properly
        return self.get(endpoint+'/albums/'+id)

    def albums_tracks(self, id):
        return self.get(endpoint+'/albums/'+id)

    def artists(self, id):
        # if typeof id = 'list': format query properly
        return self.get(endpoint+'/artists/'+id)

    def artists_albums(self, id):
        return self.get(endpoint+'/artists/'+id+'/albums')

    def artists_top_tracks(self, id):
        return self.get(endpoint+'/artists/'+id+'/top-tracks')

    def artists_related(self, id):
        return self.get(endpoint+'/artists/'+id+'/related')

    def search(self, type,query):
        return self.get(endpoint+'/search?type='+type+'&q='+query)

    def tracks(self, id):
        # if typeof id = 'list': format query properly
        return self.get(endpoint+'/tracks/'+id)

    def users(self, id):
        return self.get(endpoint+'/users/'+id)

    # Below here requires client creds

    def audio_features(self, id):
        return self.get(endpoint+'/audio-features/'+id)

    def featured_playlists(self):
        return self.get(endpoint+'/browse/featured-playlists')

    def new_releases(self):
        return self.get(endpoint+'/browse/new-releases/'+id)

    def categories(self, id=""):
        return self.get(endpoint+'/browse/categories/'+id)


    def categories_playlists(self, id):
        return self.get(endpoint+'/browse/categories'+id+'/playlists')

if __name__ == "__main__":
    print("See http://www.github.com/hughrawlinson/microspotipy")
