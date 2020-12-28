import requests
import json

token = 'e716d094ce581cdc684d02f8'

#Getters to fetch Data from the Anghami API using my user's token
def get_song(song_id):
    url = ' https://bus.anghami.com/public/song/data?song_id=' + str(song_id)
    r=requests.get(
        str(url),
        headers={'xat': 'interns','xath':token}
    )
    song = r.json()
    return song

def get_album(album_id):
    url =  'https://bus.anghami.com/public/album?album_id=' + str(album_id)
    r=requests.get(
        str(url),
        headers={'xat': 'interns','xath':token}
    )
    album = r.json()
    return album

def get_artist(artist_id):
    url = 'https://bus.anghami.com/public/artist?artist_id=' + str(artist_id)
    r=requests.get(
        str(url),
        headers={'xat': 'interns','xath':token}
    )
    artist = r.json()
    return artist

def my_liked_songs():
    r=requests.get(
        'https://bus.anghami.com/public/user/likes',
        headers={'xat': 'interns','xath':token}
    )
    liked_songs={}
    for elem in r.json():
        liked_songs[elem['id']]=elem['title']
    return liked_songs

def my_liked_artists():
    r=requests.get(
        'https://bus.anghami.com/public/user/artists',
        headers={'xat': 'interns','xath':token}
    )
    liked_artists={}
    for elem in r.json():
        liked_artists[elem['id']]=elem['name']
    return liked_artists

def my_liked_albums():
    r=requests.get(
        'https://bus.anghami.com/public/user/albums',
        headers={'xat': 'interns','xath':token}
    )
    liked_albums={}
    for elem in r.json():
        liked_albums[elem['id']]=elem['title']
    return liked_albums

def my_downloads():
    r=requests.get(
        'https://bus.anghami.com/public/user/downloads',
        headers={'xat': 'interns','xath':token}
    )
    downloads={}
    for elem in r.json():
        downloads[elem['id']]=elem['title']
    return downloads

def my_playlists():
    r=requests.get(
        'https://bus.anghami.com/public/user/playlists',
        headers={'xat': 'interns','xath':token}
    )
    playlists={}
    for elem in r.json()['playlists']:
        playlists[elem['id']]=elem['name']
    return playlists


#Funstion that displays my first 10 liked songs on the Anghami application with their artist and genre
def display_liked_songs():
    liked_songs = my_liked_songs()
    print("\nThese are my 10 first liked songs fetched from Anghami's api displayed with their artist and genre: \n")
    counter = 0
    for song_id in liked_songs:
        if counter < 10:
            print("Song: " + get_song(song_id).get('title') + " --- Artist: " + get_song(song_id).get('artist') + " --- Genre: " + get_song(song_id).get('genre'))
            counter += 1
        else:
            return 0

#Function that displays my first 10 liked artists on the Anghami application
def display_liked_artists():
    liked_artists = my_liked_artists()
    print("\nThese are my 10 first liked artists fetched from Anghami's api: \n")
    counter = 0
    for artist_id in liked_artists:
        if counter < 10:
            print("Artist's Name :" + get_artist(artist_id).get('name'))
            counter += 1
        else:
            return 0

#Function that displays my liked albums on the Anghami application
def display_albums():
    albums = my_liked_albums()
    print("\nThese are my albums fetched from Anghami's api: \n")
    counter = 0
    for album_id in albums:
        if counter < 10:
            print("Album's Name :" + get_album(album_id).get('title'))
            counter += 1
        else:
            return 0



#Running my functions
display_liked_songs()
display_liked_artists()
display_albums()

exit = input("\nPress enter to exit... ")

