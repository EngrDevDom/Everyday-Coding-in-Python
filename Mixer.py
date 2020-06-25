from pygame import mixer

mixer.init()    # Start the mixer

mixer.music.load("Ne-Yo-Together.mp3")    # Load the song
mixer.music.set_volume(0.7)     # Set the volume
mixer.music.play()              # Play the mixer

while True:
    print("Press 'p' to pause, 'r' to resume ")
    print("Press 'e' to exit the program")
    query = input(">>> ")

    if query == 'p':
        mixer.music.pause()     # Pause the music
    elif query == 'r':
        mixer.music.unpause()   # Resume music
    elif query == 'e':
        mixer.music.stop()      # Stop the mixer
        break