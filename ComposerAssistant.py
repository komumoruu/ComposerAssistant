import os
print("""© Bebra Software inc. 2020-2022
Добро пожаловать в Composer Assistant! Для генерации случайных аккордов введите gen
Для генерации весёлой песни введите gen_fun""")
from random import randint
import random
cords = ["C", "D", "E", "F", "G", "A", 'B',"C#", "D#", "E#", "F#", "G#", "A#", 'B#', "Cm", "Dm", "Em", "Fm", "Gm", "Am", 'Bm', "Cm#", "Dm#", "Em#", "Fm#", "Gm#", "Am#", 'Bm#', "Cmaj7", "Dmaj7", "Emaj7", "Fmaj7", "Gmaj7", "Amaj7", 'Bmaj7',"C#maj7", "D#maj7", "E#maj7", "F#maj7", "G#maj7", "A#maj7", 'B#maj7', "Cmmaj7", "Dmmaj7", "Emmaj7", "Fmmaj7", "Gmmaj7", "Ammaj7", 'Bmmaj7', "Cm#maj7", "Dm#maj7", "Em#maj7", "Fm#maj7", "Gm#maj7", "Am#maj7", 'Bm#maj7']
cords_fun = ["C", "D", "E", "F", "G", "A", 'B',"C#", "D#", "E#", "F#", "G#", "A#", 'B#']
cords_sad = ["Cm", "Dm", "Em", "Fm", "Gm", "Am", 'Bm', "Cm#", "Dm#", "Em#", "Fm#", "Gm#", "Am#", 'Bm#', "Cmaj7", "Dmaj7", "Emaj7", "Fmaj7", "Gmaj7", "Amaj7", 'Bmaj7',"C#maj7", "D#maj7", "E#maj7", "F#maj7", "G#maj7", "A#maj7", 'B#maj7', "Cmmaj7", "Dmmaj7", "Emmaj7", "Fmmaj7", "Gmmaj7", "Ammaj7", 'Bmmaj7', "Cm#maj7", "Dm#maj7", "Em#maj7", "Fm#maj7", "Gm#maj7", "Am#maj7", 'Bm#maj7']
run = True


while run:
 command = input()
 if command == "gen_sad":
     print("Chord =", random.choice(cords_sad))
     print("Chord =", random.choice(cords_sad))
     print("Chord =", random.choice(cords_sad))
     print("Chord =", random.choice(cords_sad))
     print("BPM =", randint(60,100))


 if command == "gen_fun":
     print("Chord =", random.choice(cords_fun))
     print("Chord =", random.choice(cords_fun))
     print("Chord =", random.choice(cords_fun))
     print("Chord =", random.choice(cords_fun))
     print("BPM =", randint(90,140))

 if command == "gen":
  print("Chord =", random.choice(cords))
  print("Chord =", random.choice(cords))
  print("Chord =", random.choice(cords))
  print("Chord =", random.choice(cords))
  print("BPM =", randint(60,140))
  