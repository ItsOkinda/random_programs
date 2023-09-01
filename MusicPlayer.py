import vlc
import os
##on the play pause next prev and volume function are not working use ctrl-c to cancel the program

folder_path = "D:\\os\\music vid"  

song_files = [f for f in os.listdir(folder_path) if f.endswith((".mp3", ".mp4"))]

# Initialize VLC instance and media player
instance = vlc.Instance()
player = instance.media_player_new()

def play_song(song_path):
    media = instance.media_new_path(song_path)
    player.set_media(media)
    player.play()

current_song_index = 0
while True:
    if current_song_index < 0:
        current_song_index = len(song_files) - 1
    elif current_song_index >= len(song_files):
        current_song_index = 0

    song_path = os.path.join(folder_path, song_files[current_song_index])

    play_song(song_path)


    command = input("Enter command (pause/next/prev/exit): ").lower()

    if command == "pause":
        player.pause()
    elif command == "next":
        player.stop()
        current_song_index += 1
    elif command == "prev":
        player.stop()
        current_song_index -= 1
    elif command == "exit":
        player.stop()
        break

player.release()
instance.release()
