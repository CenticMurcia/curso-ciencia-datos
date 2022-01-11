---
layout: home

parent_id: 3-apps
id: 3.6-img2img
title: 🎨 Image generation

img_icon: 3.6-img2img.png
---



## Tasks

|                       | Input image          | Output image           |
|-----------------------|----------------------|------------------------|
| Semantic segmetation  | Image                | Class Mask             |
| Binary seg. (Matting) | Image                | Class Mask             |
| Depth detector        | Image                | Depht mask             |
| Enhance colors        | Dark image           | Vivid image            |
| Style transfer        | Image                | Styled image           |
| Colourisation         | Black & White image  | RGB image              |
| Super-resolution      | Low resolution image | High resolution image  |
| Document unwarp       | Warped ugly document | clean legible document |
| Image inpainting      | Image with holes     | Reconstructed image    |
| Image Generation      | Random noise + (class or text) | AI-generated image |


## DL models

- U-net
- Autoencoders (AE)
- Denoising autoencoder (DAE)
- Variational autoencoder (VAE)
- Vector Quantisation Variational autoencoder (VQ-VAE)
- Denoising Diffusion Probabilistic Models (DDPM)
- GANs


## Metrics

- log likelihood


# 📉 Loss functions

- **Segmentation**: Usually Loss = **IoU** + **Dice** + 0.8***BCE**
  - **Pixel-wise cross entropy**: each pixel individually, comparing the class predictions (depth-wise pixel vector)
  - **IoU** (F0): `(Pred ∩ GT)/(Pred ∪ GT)` = `TP / TP + FP * FN`
  - **Dice** (F1): `2 * (Pred ∩ GT)/(Pred + GT)` = `2·TP / 2·TP + FP * FN`
    - Range from `0` (worst) to `1` (best)
    - In order to formulate a loss function which can be minimized, we'll simply use `1 − Dice`
- **Generation**
   - **Pixel MSE**: Flat the 2D images and compare them with regular MSE.
   - **Discriminator/Critic** The loss function is a binary classification pretrained resnet (real/fake).
   - **Feature losses** or perpetual losses.