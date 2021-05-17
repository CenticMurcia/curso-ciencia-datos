<h1 align="center">Autoencoders</h1>

## Theory

> #### What is an autoencoder?
>  Same input and output shape neural network made for reconstruct the input.
>  
>  Applications:
>  - Compress information (Bottleneck Autoencoder)
>  - Unsupervised feature extractor (Bottleneck Autoencoder & Deepstack Autoencoder)

- Architectures:
  - **Bottleneck Autoencoder**: only the bottleneck layer (smaller middle hidden layer) is used as extracted features. The main issue is that the surrounding layers have to be very large so that enough information is beeing captures.
  - **Deepstack Autoencoder**: all hidden layers are being used extracted features. Dimension isn't beeing reduced, but enlarged.
- **Denoising Autoencoder (DAE)**: Adds noise to the input to learn how to reconstrut the original input.
  - images:
    - NOISE: Random normal noise to the pixels.
    - LOSS: Only have a recontruction loss (pixel MSE for example)
  - Tabular:
    - NOISE: "inputSwapNoise" probability: 0.15 means 15% of features replaced by values from another row OF SAME FEATS (NO cross feature noise).
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


## Practice (Kaggle competitions)
- Adult Dataset
  - [walkwithfastai tutorial](https://walkwithfastai.com/tab.ae)
  - [TabularVAE repo](https://github.com/EtienneT/TabularVAE)
- Porto Seguro: Winning solution
  - Unspervised training (Feat extractor): DAE with swap noise 
  - [discussion](https://www.kaggle.com/c/porto-seguro-safe-driver-prediction/discussion/44629)
- Tabular Playground Jan 2021: Winning solution
  - Feature extractor: DAE of 3 Linear layers
  - Model: Stacking of heavily_regularized_MLPs + LightGBM 
  - [discussion](https://www.kaggle.com/c/tabular-playground-series-jan-2021/discussion/216037)
  - [notebook](https://www.kaggle.com/springmanndaniel/1st-place-turn-your-data-into-daeta)
- Tabular Playground Feb 2021: Winning solution
  - Feature extractor: DAE of Transformer layers
  - [discussion](https://www.kaggle.com/c/tabular-playground-series-feb-2021/discussion/222745)
  - [github repo](https://github.com/ryancheunggit/Denoise-Transformer-AutoEncoder)

