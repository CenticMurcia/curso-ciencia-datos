<h1 align="center">Audio</h1>



# 1D wave signal


Sample rate: Points per second

Due to the [Nyquist–Shannon sampling theorem](https://en.wikipedia.org/wiki/Nyquist%E2%80%93Shannon_sampling_theorem) the highest frecuency that you can caputure is **Sampling_Rate_Freq/2**.


| Sample rate | Max freq  | Description                                               |        
|-------------|-----------|-----------------------------------------------------------|
| 8.000 Hz    | 4 kHz     | Used in **telephone** & walkie-talkie.                    |
| 11.025 Hz   | 5,5 kHz   | Used for lower-quality MPEG, PCM audio                    |
| 16.000 Hz   | 8 kHz     | Used in most VoIP and VVoIP, extension of telephone band. |
| 22.050 Hz   | 11 kHz    | Used for lower-quality PCM and MPEG audio.                |
| 44.100 Hz   | 22 kHz    | Used for music CDs (MP3, MPEG-1 VCD, SVCD).               |
| 48.000 Hz   | 24 kHz    | Used by digital video equipment and movies                |
| 88.200 Hz   | 44 kHz    | Used by some professional recording equipment             |
| 96.000 Hz   | 48 kHz    | Used by Blu-ray audio tracks, HD DVD audio tracks.        |
| 176.400 Hz  | 88,2 kHz  | Used in professional applications for CD and HDCD.        |
| 192.000 Hz  | 96 kHz    | Used on professional video LPCM DVD, Blu-ray, HD DVD      |
| 352.800 Hz  | 176,4 kHz | Used for Super Audio CDs. Digital eXtreme Definition.     |
| 384.000 Hz  | 192 kHz   | Highest sample rate available for common software.        |


[source](https://github.com/audiojs/sample-rate)



# Espectogram

### Time parameters (X axis):

|                   | Decription                                    | Librosa      | Usually     |
|:-----------------:|:----------------------------------------------|:------------:|-------------|
| **Sampling Rate** | Constant: Depends how the signal was recorded | `sr`         | 22kHz, 44.1kHz, 48kHz |
| **Window size**   | Number of 1D points to compute the FourTrans  | `n_fft`      | 2048 (93ms) |
| **Hop size**      | Window displacement. Usually win_size // 4    | `hop_length` | 512         |
| **Window shape**  | Uniform, Normal, hann                         | `window`     | 'hann'      |

### Frequencies parameters (Y axis):

|                   | Decription                                    | Librosa      | Usually       |
|:-----------------:|:----------------------------------------------|:------------:|---------------|
| **Min frequency** | Lowest frequency (in Hz)                      | `fmin`       | 0.0           |
| **Max frequency** | Highest frequency (in Hz). If None: sr / 2.0  | `fmax`       | None          |
| **Resolution**    | Number of freqs from minFreq to maxFreq       | `n_mels`     | 224, 256, 512 |
| **Y scale**       | linear, log, mel                              |              |               |


> Why log or mel scale instead of linear?
> - The difference between 500 and 1000 Hz is obvious
> - whereas the difference between 7500 and 8000 Hz is barely noticeable.


### Amplitude parameter (pixel intensity)
- scale: linear or Decibel


### Examnple

```python
filename = 'my_sound.wav'
y, sr = librosa.load(filename)
```