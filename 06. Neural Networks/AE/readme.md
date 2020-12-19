<h1 align="center">Autoencoders</h1>


- Standard autoencoders: Made for reconstruct the input. No continuous latant space.
  - **Simple Autoencoder**: Same input and output net with a smaller middle hidden layer (botleneck layer, latent vector).
  - **Denoising Autoencoder (DAE)**: Adds noise to the input to learn how to remove noise.
  - Only have a recontruction loss (pixel mean squared error for example)
- **Variational Autoencoder (VAE)**: Initially trained as a reconstruction problem, but later we can play with the latent vector to generate new outputs. Latant space need to be continuous.
  - **Latent vector**: Is modified by adding gaussian noise (normal distribution, mean and std vectors) during training.
  - **Loss**: `loss = recontruction loss + latent loss`
    - Recontruction loss: Keeps the output similar to the input  (mean squared error)
    - Latent loss: Keeps the latent space continuous (KL divergence)
  - **Disentangled Variational Autoencoder (β-VAE)**: Improved version. Each parameter of the latent vector is devotod to tweak 1 characteristic. [*paper*](https://arxiv.org/abs/1709.05047).
    - **β** to small: Overfitting. Learn to reconstruct your training data, but i won't generalize
    - **β** to big: Loose high definition details. Worse performance.
- **Hierarchial VAE (HVAE)**:
  - Can be thought of as a series of VAEs stacked on top of each other
- **NVAE**: Hierarchial VAE to the extreme
  - [video paper explained](https://www.youtube.com/watch?v=x6T1zMSE4Ts)
  - [original paper](https://arxiv.org/pdf/2007.03898.pdf)
  - [other paper](https://openreview.net/forum?id=RLRXCV6DbEJ)


  <p align="center"><img width="66%" src="img/____.png" /></p>
