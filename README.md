# Analog-to-Digital and Digital-to-Analog Conversion Module

### Description:
This module implements analog-to-digital (A/D) and digital-to-analog (D/A) conversion processes for audio signals using a sound card. The A/D conversion transforms analog sound signals into digital form, facilitating their processing in digital devices and storage in digital data carriers. It involves three main stages: sampling, quantization, and encoding. Conversely, the D/A conversion reconstructs digital signals into analog form. The resolution of the converter, expressed in bits, determines the number of discrete values it can generate. For instance, an 8-bit converter can process a sample into one of 256 numerical values. The module utilizes sound card input for A/D conversion and output for D/A conversion. It allows for simplification of the conversion process and saving the sampled and quantized audio as WAV files.

### Implementation:

Use of sound card input/output for A/D and D/A conversion.
Sampling, quantization, and encoding processes for A/D conversion.
Reconstructing digital signals into analog form for D/A conversion.
Saving sampled and quantized audio as WAV files.
### Requirements:

Python environment with necessary libraries (NumPy, SciPy, Soundcard).
Sound card with microphone input and speaker output.
### Functionality:

A/D Conversion: Convert analog sound signals to digital form.
D/A Conversion: Reconstruct digital signals into analog form.
Save Audio: Save sampled and quantized audio as WAV files.
### Parameters:

Sampling frequency: Determines how often the signal is checked and converted into a number.
Quantization levels: Determine the resolution of the converter, expressed in bits.
### Notes:

Ensure sampling frequency is at least twice the highest signal frequency to avoid distortion (Nyquist-Shannon theorem).
Reliable signal reproduction is achievable when the sampling frequency exceeds double the highest signal frequency.

### License:
This project is licensed under the MIT License - see the LICENSE.md file for details.
