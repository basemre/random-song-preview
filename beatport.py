import requests
import json
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from selenium import webdriver
from random import randint
import time

cid = "" # CLIENT ID, GET IT FROM SPOTIFY.
secret = "" #CLIENT SECRET, GET IT FROM SPOTIFY.

client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret) 
spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

req = requests.get("https://www.beatport.com/genre/electro-house/17/top-100")
soup = BeautifulSoup(req.text, "html.parser")
top_100_songs = soup.find_all("li", "bucket-item ec-item track") 

x = {}
for i in range(0, 100):
    x.update( {i:{top_100_songs[i].p.find('span', class_='buk-track-primary-title').text : top_100_songs[i].select_one(".buk-track-artists").get_text(strip=True)}} )

song_number = randint(0, 100)
results = spotify.search(q='artist:' + json.dumps(x[song_number]), type='track')

song_url = results['tracks']['items'][0]['preview_url']
driver = webdriver.Chrome()
driver.get(song_url)
time.sleep(30)
driver.quit()