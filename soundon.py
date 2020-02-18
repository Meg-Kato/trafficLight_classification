from mutagen.mp3 import MP3 as mp3
import pygame
import time
import sys

new_flag = int(sys.argv[1])
print(new_flag)

def soundon(new_flag:int):
    if new_flag != 3:
        filename = {0:'red2.mp3', 1:'green2.mp3', 2:'idk.mp3'}
        pygame.mixer.init()
        pygame.mixer.music.load(filename[new_flag])
        mp3_length = mp3(filename[new_flag]).info.length
        pygame.mixer.music.play(1)
        time.sleep(mp3_length+0.25)
        pygame.mixer.music.stop()
        sys.exit()
    else:
        pygame.mixer.music.stop()


soundon(new_flag)