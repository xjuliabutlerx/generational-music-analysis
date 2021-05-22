import spotipy
from spotipy.oauth2 import SpotifyOAuth
import cred
import json

def find_album_id(album_name):
    # find album by name
    results = sp.search(q = "album:" + album_name, type = "album")

    # get the first album uri
    album_id = results['albums']['items'][0]['uri']

    return album_id

def get_album_tracks(album_id, artist, track_names, track_list):
    # get album tracks
    tracks = sp.album_tracks(album_id)
    #print(type(tracks['items']))

    # add each track to the list
    for track in tracks['items']:
        #print(track['name'])
        track_names.append(track['name'])

    # find the track URI and add it to the IDs list
    for n in range(len(tracks['items'])):
        #print(tracks['items'][n]['uri'])
        track_list.append(tracks['items'][n]['uri'])

def get_attributes(track_names, track_ids, track_attr):
    # get the track attributes
    for n in range(len(track_ids)):
        #print(track_names[n])
        result = sp.audio_features(track_ids[n])
        # change the types of the attributes from int to str and store them in
        # separate variables
        duration = str(result[0]['duration_ms'])
        danceability = str(result[0]['danceability'])
        energy = str(result[0]['energy'])
        key = str(result[0]['key'])
        loudness = str(result[0]['loudness'])
        mode = str(result[0]['mode'])
        speechiness = str(result[0]['speechiness'])
        acousticness = str(result[0]['acousticness'])
        instrumentalness = str(result[0]['instrumentalness'])
        liveness = str(result[0]['liveness'])
        valence = str(result[0]['valence'])
        tempo = str(result[0]['tempo'])
        time_signature = str(result[0]['time_signature'])
        # concatenate all the strings into a single string and append it to the attributes list
        output = duration + "," + danceability + "," + energy + "," + key + "," + loudness + "," + mode + "," + speechiness + "," + acousticness + "," + instrumentalness + "," + liveness + "," + valence + "," + tempo + "," + time_signature
        track_attr.append(output)
        #print(track_attr[n])

def print_csv(album, artist, tracks, trackIDs, attr):
    for n in range(len(tracks)):
        print(album + "," + artist + "," + tracks[n] + "," + trackIDs[n] + "," + attr[n])

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id = cred.client_id, client_secret = cred.client_secret, redirect_uri = cred.redirect_url))
sp.trace = False

# Names of Baby Boomer Albums
BB_albums = ["Highway 61 Revisited", "Sgt. Pepper's Lonely Hearts Club Band (Remastered)", "What's Going On", "Tapestry", "Led Zeppelin IV", "Exile On Main Street (Deluxe Version)", "Innervisions", "Their Greatest Hits 1971–1975 (2013 Remaster)", "Exodus", "Saturday Night Fever (The Original Movie Soundtrack)"]
BB_artists = ["Bob Dylan", "The Beatles", "Marvin Gaye", "Carole King", "Led Zeppelin", "The Rolling Stones", "Stevie Wonder", "Eagles", "Bob Marley & the Wailers", "Various Artists"]
BB_tracks = []
BB_tracksIDs = []
BB_attributes = []

# Names of Generation X Albums
X_albums = ["Nevermind", "Ten", "The Chronic", "OK Computer", "The Battle Of Los Angeles", "Sublime", "Blood Sugar Sex Magik", "Tragic Kingdom", "Mellon Collie and The Infinite Sadness (Deluxe Edition)", "Out Of Time"]
X_artists = ["Nirvana", "Pearl Jam", "Dr. Dre", "Radiohead", "Rage Against the Machine", "Sublime", "Red Hot Chili Peppers", "No Doubt", "Smashing Pumpkins", "R.E.M."]
X_tracks = []
X_tracksIDs = []
X_attributes = []

# Names of Millennial Albums
M_albums = ["Oops!... I Did It Again", "Bleed American", "Under My Skin", "Enema Of The State", "Stripped", "Try This", "American Idiot", "The Eminem Show", "Backstreet Boys", "From Under The Cork Tree"]
M_artists = ["Britney Spears", "Jimmy Eat World", "Avril Lavigne", "blink-182", "Christina Aguilera", "P!nk", "Green Day", "Eminem", "Backstreet Boys", "Fall Out Boy"]
M_tracks = []
M_tracksIDs = []
M_attributes = []

# Names of Generation Z Albums
Z_albums = ["My Beautiful Dark Twisted Fantasy", "Lemonade", "To Pimp A Butterfly", "Red", "WHEN WE ALL FALL ASLEEP, WHERE DO WE GO?", "Scorpion", "Melodrama", "21", "thank u, next", "My World 2.0"]
Z_artists = ["Kanye West", "Beyoncé", "Kendrick Lamar", "Taylor Swift", "Billie Eilish", "Drake", "Lorde", "Adele", "Ariana Grande", "Justin Bieber"]
Z_tracks = []
Z_tracksIDs = []
Z_attributes = []

print("Printing the Tracks of all the Baby Boomer Albums")

print("")

# print the csv header
print("album,artist,track_name,track_id,duration_ms,danceability,energy,key,loudness,mode,speechiness,acousticness,instrumentalness,liveness,valence,temp,time_signature")

for x in range(0, len(BB_albums)):
    #print(BB_albums[x].upper())
    album_id = find_album_id(BB_albums[x])
    artist = BB_artists[x]
    #print("ID: " + album_id)
    get_album_tracks(album_id, artist, BB_tracks, BB_tracksIDs)
    #print(BB_tracks)
    #print(BB_tracksIDs)
    #print(str(len(BB_tracks)) + " " + str(len(BB_tracksIDs)))
    #print("")

    get_attributes(BB_tracks, BB_tracksIDs, BB_attributes)
    print_csv(BB_albums[x], artist, BB_tracks, BB_tracksIDs, BB_attributes)

    BB_tracks = []
    BB_tracksIDs = []

print("Printing the Tracks of all the Generation X Albums")

print("")

# print the csv header
print("album,artist,track_name,track_id,duration_ms,danceability,energy,key,loudness,mode,speechiness,acousticness,instrumentalness,liveness,valence,temp,time_signature")

for x in range(0, len(X_albums)):
    #print(X_albums[x].upper())
    album_id = find_album_id(X_albums[x])
    artist = X_artists[x]
    #print("ID: " + album_id)
    get_album_tracks(album_id, artist, X_tracks, X_tracksIDs)
    #print(X_tracks)
    #print(X_tracksIDs)
    #print("")

    get_attributes(X_tracks, X_tracksIDs, X_attributes)
    print_csv(X_albums[x], artist, X_tracks, X_tracksIDs, X_attributes)

    X_tracks = []
    X_tracksIDs = []

print("Printing the Tracks of all the Millennial Albums")

print("")

# print the csv header
print("album,artist,track_name,track_id,duration_ms,danceability,energy,key,loudness,mode,speechiness,acousticness,instrumentalness,liveness,valence,temp,time_signature")

for x in range(0, len(M_albums)):
    #print(M_albums[x].upper())
    album_id = find_album_id(M_albums[x])
    artist = M_artists[x]
    #print("ID: " + album_id)
    get_album_tracks(album_id, artist, M_tracks, M_tracksIDs)
    #print(M_tracks)
    #print(M_tracksIDs)
    print("")

    get_attributes(M_tracks, M_tracksIDs, M_attributes)
    print_csv(M_albums[x], artist, M_tracks, M_tracksIDs, M_attributes)

    M_tracks = []
    M_tracksIDs = []

print("Printing the Tracks of all the Generation Z Albums")

print("")

# print the csv header
print("album,artist,track_name,track_id,duration_ms,danceability,energy,key,loudness,mode,speechiness,acousticness,instrumentalness,liveness,valence,temp,time_signature")

for x in range(0, len(Z_albums)):
    #print(Z_albums[x].upper())
    album_id = find_album_id(Z_albums[x])
    artist = Z_artists[x]
    #print("ID: " + album_id)
    get_album_tracks(album_id, artist, Z_tracks, Z_tracksIDs)
    #print(Z_tracks)
    #print(Z_tracksIDs)
    #print("")

    get_attributes(Z_tracks, Z_tracksIDs, Z_attributes)
    print_csv(Z_albums[x], artist, Z_tracks, Z_tracksIDs, Z_attributes)

    Z_tracks = []
    Z_tracksIDs = []
