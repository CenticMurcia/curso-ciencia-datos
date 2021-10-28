---
layout: page

parent_id: 3.6-audio
id: 2 - Audio classification
title: "🔈 Audio classification (with data aug)"

notebook: Audio classification with Tensorflow.ipynb
nb_btn_name: Tensorflow
nb_btn_icon: tensorflow

notebook_2: Audio classification with Fastai & Fastaudio.ipynb
nb2_btn_name: Pytorch
nb2_btn_icon: pytorch
---


## Transormation pipeline for Train dataset

1. Read audio wave from filepath
   1. Read wav file (`tf.io.read_file`)
   2. Decode wav file (`tf.audio.decode_wav`)
2. Remove silence from the begining and the end ([`tfio.audio.trim`](https://www.tensorflow.org/io/api_docs/python/tfio/audio/trim)) (OPTIONAL)
3. Limit audio to a fixed number of seconds
   - Sorter audio --> Pad the end with zeros
   - Longer audio --> Random crop
4. Data augmentation over audio wave
   - Change Speed
   - Pink noise
   - Gaussian noise
   - Gaussian SNR
   - Gain (Volume Adjustment)
5. Convert audio to MelSpectogram
   1. Convert audio to spectogram (`tfio.audio.spectrogram`)
   2. Apply the Mel scale (`tfio.audio.melscale`)
   3. Apply the DB scale (`tfio.audio.dbscale`)
6. Data augmentation over MelSpectogram
   - Time Warping (`tfa.image.sparse_image_warp`) (from the [SpecAugment](https://arxiv.org/abs/1904.08779) paper)
   - Time Masking (`tfio.audio.time_mask`) (from the [SpecAugment](https://arxiv.org/abs/1904.08779) paper)
   - Frequency Masking (`tfio.audio.freq_mask`) (from the [SpecAugment](https://arxiv.org/abs/1904.08779) paper)
   - Mixup
   - Any other image transformation
7. Add the coordconv channel (OPTIONAL)
8. Normalize (standard scale)
   - Apply the correct mean and std if transfer learning


## [Past kaggle audio competitions](https://www.kaggle.com/competitions?searchQuery=audio)

- [BirdCLEF - Birdcall Identification](https://www.kaggle.com/c/birdclef-2021) (2021)
- [Rainforest Species Audio Detection](https://www.kaggle.com/c/rfcx-species-audio-detection) (2021)
- [Cornell - Birdcall Identification](https://www.kaggle.com/c/birdsong-recognition) (2020)
- [Freesound Audio Tagging](https://www.kaggle.com/c/freesound-audio-tagging-2019) (2019)