# MicroSpotipy

A micropython wrapper for some of the Spotify Web API!

## Usage

Instantiate as follows

```
import MicroSpotipy
s = MicroSpotipy(client_id, client_secret)
```

The object `s` has the following methods with arguments.

* `albums(id)`
* `albums_tracks(id)`
* `artists(id)`
* `artists_albums(id)`
* `artists_top_tracks(id)`
* `artists_related(id)`
* `search(type,query)`
* `tracks(id)`
* `users(id)`

The following endpoints require Spotify app credentials, which you can create [here](https://developer.spotify.com/my-applications/)

* `audio_features(id)`
* `featured_playlists()`
* `new_releases()`
* `categories(id="")`
* `categories_playlists(id)`

Not quite yet tested on the Electromagnetic Field TiLDA MK3, but it should be fine. If it doesn't, expect updates. Either way, expect example usages coming to the TiLDA app store "soon".
