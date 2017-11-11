#!/usr/bin/python
import argparse
from signal import pause
from gpiozero import Button,LED
from song_player import song_player

parser = argparse.ArgumentParser()
parser.add_argument('--playlist',default='default',help='default_playlist')
args = parser.parse_args()
playlist = args.playlist
button = Button(2)
song=song_player(playlist)
button.when_pressed = song.play
button.when_released = song.stop

pause()
