#!/bin/python3

# pip install --user sounddevice
# pip install --user scipy

import os
import sounddevice
from scipy.io.wavfile import write

try:
    # Tempo de gravação
    fs = 44100
    second = int(input('Quantos segundos deseja gravar?:\n\n '))
    print('\nGravando...')

    # Captura a gravação
    record_voice=sounddevice.rec(int(second * fs) , samplerate=fs , channels=2)
    sounddevice.wait()

    # Salva arquivo da gravação
    write('gravação.wav' , fs , record_voice)
    print('Gravação finalizada!')

except KeyboardInterrupt:
    os.system('clear')
    exit()

