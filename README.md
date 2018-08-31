# omxplayer-youtube-playlist
youtube playlist for omxplayer

Requirements
---
Python 2.7 or higher.

A recent version of [omxplayer](http://omxplayer.sconde.net/). 

A recent version of [youtube-dl](https://rg3.github.io/youtube-dl/).

Usage
-----
```
$ python playlist.py [playlist-id]
```

**example**
```
https://www.youtube.com/watch?v=RBumgq5yVrA&list=RDRBumgq5yVrA

$ python playlist.py RDRBumgq5yVrA
```
You'll also need an API key for V3 of the Youtube API - set one up at https://console.developers.google.com/apis/credentials. Create an environment variable YOUTUBE_API_KEY containing your key.
