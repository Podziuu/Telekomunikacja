import soundcard as sc
import numpy as np
from scipy.io.wavfile import read, write

quantization = [8, 16, 32]

"""
Mikrofon przyjmuje sygnal analogowy i zamienia go na
sygnal cyfrowy.
zmiennia sampling: jest to czestotliwosc probkowania
generalnie okresla ile probek pobieramy na sekunde
jest wyrazana w hercach. Jak chcemy miec sygnal cyfrowy
to musi on byc probkowany w ustalonych interwalach.
Kwantyzacja - jest to proces polegajacy na przypisaniu
wartosci liczbowej do sygnalu analogowego. W zaleznosci
od ilosci bitow przypisujemy wartosci do sygnalu analogowego
np. 8 bitow - 2^8 = 256 wartosci
16 bitow - 2^16 = 65536 wartosci
32 bitow - 2^32 = 4294967296 wartosci
Sygnal analogowy moze przyjmowac dowolne wartosci, ale
sygnal cyfrowy musi byc skwantyzowany, czyli musi miec
przypisane wartosci liczbowe w skonczonej liczbie wartosci
SNR - stosunek sygnalu do szumu
SNR = 10 * log10(energia sygnalu / energia szumu)
energia sygnalu - suma kwadratow sygnalu
energia szumu - suma kwadratow roznicy miedzy sygnalem a szumem
Twierdzenie Nyquista - aby uniknac znieksztalcen sygnalu
cyfrowego, czestotliwosc probkowania musi byc przynajmniej
dwukrotnie wieksza niz najwyzsza czestotliwosc sygnalu analogowego
"""

def quantize(data, quantization):
    print(data, quantization)
    max_value = 2 ** (quantization - 1) - 1
    quantized_data = np.round(data * max_value / np.max(abs(data)))
    if quantization <= 16:
        return np.int16(quantized_data)
    else:
        return np.int32(quantized_data)

def main():
    while True:
        option = input("Wybierz opcje:\n"
              "1. nagrywanie dzwieku\n"
              "2. odtwarzanie dzwieku\n"
              "3. koniec programu\n"
              )
        if option == '1':
            value = int(input("Podaj poziom kwantyzacji (8, 16, 32): "))
            while value not in quantization:
                value = int(input("Podaj poziom kwantyzacji (8, 16, 32): "))
            
            # typowe wartosci dla czestotliwosci probkowania to 44100, 48000, wiecej niz 192kHz to juz jest overkill
            sampling = int(input("Podaj czestotliwosc probkowania: "))
            duration = int(input("Podaj czas nagrania w sekundach: "))
            audio = sc.default_microphone()
            
            print("Zaczynam nagrywac dzwiek...")
            # pierwsza zmienna mnozy nam czas nagrywania przez czestotliwosc probkowania na sekunde, druga to po prostu czestotliwosc probkowania
            recorded_audio = audio.record(numframes=int(duration * sampling), samplerate=sampling)
            data = recorded_audio
            # zamiana na sygnal cyfrowy
            quantized_data = quantize(data, value)
            
            write("recorded_audio.wav", sampling, quantized_data)
            print("Nagranie zakonczone")
            
        if option == '2':
            data = read("recorded_audio.wav")
            sampling = data[0]
            print("Czestotliwosc probkowania: ", sampling)
            # zamiana na sygnal analogowy
            data = np.float64(data[1] / np.max(abs(data[1])))
            audio = sc.default_speaker()
            audio.play(data, sampling)
                
        if option == '3':
            break
        elif option not in ['1', '2', '3']:
            print("Podales niepoprawna opcje")
                    
main()