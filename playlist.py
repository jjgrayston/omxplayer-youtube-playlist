import urllib, json,sys
import subprocess
import os

def play_url(url):
    yt_dl = subprocess.Popen(['youtube-dl', '--max-quality' , '18', '-g', url], stdout = subprocess.PIPE, stderr = subprocess.PIPE)
    (url, err) = yt_dl.communicate()
    if yt_dl.returncode != 0:
        sys.stderr.write(err)
        raise RuntimeError('Error getting URL.')
        print "Playing"
    mplayer = subprocess.Popen(
            ['omxplayer','-b', url.decode('UTF-8').strip()],
            stdout = subprocess.PIPE, stderr = subprocess.PIPE)
    mplayer.wait()


input = sys.argv
playlist = input[1]

key = os.environ['YOUTUBE_API_KEY']

print 'Play List:', str(input[1])

url = "https://www.googleapis.com/youtube/v3/playlistItems?playlistId="+playlist+"&maxResults=50&part=snippet%2CcontentDetails&key="+key

response = urllib.urlopen(url);
data = json.loads(response.read())
feed = data['items']

print 'Found ',len(feed),' Video'

for d in feed:
        jsonstring = json.dumps(d)
        title = d['snippet']['title']
        link = "https://www.youtube.com/watch?v=" + d['contentDetails']['videoId']
        print "Play : ",title
        play_url(link)
        print "DONE"

#if 'nextPageToken' in data:
#    print "Another page is available."
#else:
#    print "That was the last page."
print "############# Play All Done ################"
