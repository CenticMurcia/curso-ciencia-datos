---
layout: home

parent_id: 3-apps
id: 3.6-audio
title: 🔈 Audio

img_icon: 3.6-audio.svg
---




## Make all sounds the same

```bash
ffmpeg -i nombre_file_wav -n -acodec pcm_s16le -ac 1 -ar 16000 nombre_fichero_salida
```

- `-n`: No sobreescribir fichero audo original
- `-ac 1`: Mono


## 1D wave signal


Sample rate: Points per second

Due to the [Nyquist–Shannon sampling theorem](https://en.wikipedia.org/wiki/Nyquist%E2%80%93Shannon_sampling_theorem) the highest frecuency that you can caputure is **Sampling Rate / 2**.


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


> Source: [https://github.com/audiojs/sample-rate](https://github.com/audiojs/sample-rate)



## Create dataset

youtube-dl --extract-audio --audio-format mp3 https://www.youtube.com/watch?v=TCudWnNMr0s



## Amplitude parameter (pixel intensity)
- scale: linear or Decibel


## Example

```python
filename = 'my_sound.wav'
y, sr = librosa.load(filename)
```

## References

- https://fastaudio.github.io/
- https://www.youtube.com/c/ValerioVelardoTheSoundofAI/videos
