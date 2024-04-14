import soundcard as sc
import numpy as np
from scipy.io.wavfile import read, write

quantization = [8, 16, 32]

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
            
            sampling = int(input("Podaj czestotliwosc probkowania: "))
            duration = int(input("Podaj czas nagrania w sekundach: "))
            audio = sc.default_microphone()
            
            print("Zaczynam nagrywac dzwiek...")
            recorded_audio = audio.record(numframes=int(duration * sampling), samplerate=sampling)
            data = recorded_audio
            quantized_data = quantize(data, value)
            
            write("recorded_audio.wav", sampling, quantized_data)
            print("Nagranie zakonczone")
            
        if option == '2':
            data = read("recorded_audio.wav")
            sampling = data[0]
            print("Czestotliwosc probkowania: ", sampling)
            data = np.float64(data[1] / np.max(abs(data[1])))
            audio = sc.default_speaker()
            audio.play(data, sampling)
                
        if option == '3':
            break
        elif option not in ['1', '2', '3']:
            print("Podales niepoprawna opcje")
                    
main()