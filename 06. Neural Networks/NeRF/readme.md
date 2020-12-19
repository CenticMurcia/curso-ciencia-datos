<h1 align="center">Neural Representations (NeRF, SIREN,...)</h1>


> - 2D: [x,y]->[R,G,B]
> - 3D: [x,y,z]->[R,G,B,alpha]

- Input coordinates with sine & cos (positional encoding) [NeRF](https://arxiv.org/abs/2003.08934)
- Replacing the ReLU activations with sine functions [SIREN](https://arxiv.org/abs/2006.09661)
- Input coordinates into a Fourier feature space [Fourier](https://arxiv.org/abs/2006.10739)

<p align="center"><img width="66%" src="img/____.png" /></p>


### Mejoras sobre el NeRF

| Description                  | Website                                               | Video                                | Paper                                        |
|------------------------------|-------------------------------------------------------|--------------------------------------|----------------------------------------------|
| NeRF in the Wild             | [web](https://nerf-w.github.io)                       | [3:41](https://youtu.be/yPKIxoN2Vf0) | [Aug 2020](https://arxiv.org/abs/2008.02268) |
| NeRF++                       |                                                       |                                      | [Oct 2020](https://arxiv.org/abs/2010.07492) |
| Deformable NeRF (nerfies)    | [web](https://nerfies.github.io)                      | [7:26](https://youtu.be/MrKrnHhk8IA) | [Nov 2020](https://arxiv.org/abs/2011.12948) |
| NeRF with time dimension     | [web](https://www.albertpumarola.com/research/D-NeRF) | [2:21](https://youtu.be/lSgzmgi2JPw) | [Nov 2020](https://arxiv.org/abs/2011.13961) |
| NeRF with better weight init | [web](https://www.matthewtancik.com/learnit)          | [3:54](https://youtu.be/A-r9itCzcyo) | [Dec 2020](https://arxiv.org/abs/2012.02189) |

