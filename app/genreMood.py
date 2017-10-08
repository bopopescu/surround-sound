from topicAlgo import determineGenreOrMood
from testmicrosoftazure import analyze_tone
from testmicrosoftazure import getToneWords

playlists = {"hiphop": "https://open.spotify.com/user/spotify/playlist/37i9dQZF1DX0XUsuxWHRQd",
"pop": "https://open.spotify.com/user/spotify/playlist/37i9dQZF1DXcBWIGoYBM5M",
"popculture": "https://open.spotify.com/user/spotify/playlist/37i9dQZF1DWWF3yivn1m3D",
"country": "https://open.spotify.com/user/spotify/playlist/37i9dQZF1DX1lVhptIYRda",
"workout": "https://open.spotify.com/user/spotify/playlist/37i9dQZF1DWSJHnPb1f0X3",
"chill": "https://open.spotify.com/user/spotify/playlist/37i9dQZF1DX4WYpdgoIcn6",
"electronic": "https://open.spotify.com/user/spotify/playlist/37i9dQZF1DX8tZsk68tuDw",
"rock": "https://open.spotify.com/user/spotify/playlist/37i9dQZF1DXcF6B6QPhFDv",
"focus": "https://open.spotify.com/user/spotify/playlist/37i9dQZF1DX4sWSpwq3LiO",
"religious": "https://open.spotify.com/user/spotify/playlist/37i9dQZF1DXcb6CQIjdqKy",
"indie": "https://open.spotify.com/user/spotify/playlist/37i9dQZF1DX2Nc3B70tvx0",
"outside": "https://open.spotify.com/user/spotify/playlist/37i9dQZF1DX9wC1KY45plY",
"happy": "https://open.spotify.com/user/spotify/playlist/37i9dQZF1DX7KNKjOK0o75"}

def determinePlaylist(toneWord):
    if toneWord in playlists:
        return playlists[toneWord]
    else:

        return "https://open.spotify.com/user/spotify/playlist/37i9dQZF1DXcBWIGoYBM5M"

def main(url):
    toneWords = getToneWords(url)
    #print(eval(toneWords)['description'])
    print(toneWords)
    toneWord = determineGenreOrMood(toneWords)
    print(toneWord)
    return determinePlaylist(toneWord)
