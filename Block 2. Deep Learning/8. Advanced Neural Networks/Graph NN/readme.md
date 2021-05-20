<h1 align="center">Graph Neural Networks (GNN)</h1>


## Architectures

- **[Message Passing Neural Networks (MPNNs)](https://arxiv.org/pdf/1704.01212.pdf)**
- **[Transformer Encoder](https://arxiv.org/pdf/1706.03762.pdf)** (multi-head attention layers)

- Models
  - [GNN](https://persagen.com/files/misc/scarselli2009graph.pdf) Graph Neural Network, 2009
  - [DeepWalk](https://arxiv.org/abs/1403.6652): Online Learning of Social Representations, 2014
  - [GraphSage](https://cs.stanford.edu/people/jure/pubs/graphsage-nips17.pdf), 2017
  - [Relational inductive biases, DL, and graph networks](https://arxiv.org/abs/1806.01261), 2018
  - [KGCN](https://arxiv.org/abs/1904.12575): Knowledge Graph Convolutional Network, 2019

<p align="center"><img width="66%" src="img/____.png" /></p>



## Applications

- Graph Databases
- Knowledge Graphs (KG): Describes real-world entities and their interrelations
- Social Networks
- Transport Graphs
- Molecules (including proteins): Make predictions about their properties and reactions.
  - [Smell molecules](https://ai.googleblog.com/2019/10/learning-to-smell-using-deep-learning.html)
- [Newton vs the machine: Solving the 3-body problem using DL](https://arxiv.org/abs/1910.07291) (Not using graphs)


## Reference

- [University of Amsterdam DL course](https://uvadlc.github.io)
  - [Tutorial 7: Graph Neural Networks](https://uvadlc-notebooks.readthedocs.io/en/latest/tutorial_notebooks/tutorial7/GNN_overview.html)
- Kaggle competitions
  - [Predicting Molecular Properties](https://www.kaggle.com/c/champs-scalar-coupling)
     - [2nd: Atomic Transformer](https://www.kaggle.com/c/champs-scalar-coupling/discussion/106468) by Antor.
     - [6th: MPNN + Transformer](https://www.kaggle.com/c/champs-scalar-coupling/discussion/106407)
  - [NFL Big Data Bowl](https://www.kaggle.com/c/nfl-big-data-bowl-2020)
     - [18th: Graph Transformer With Minimal FE, with code](https://www.kaggle.com/c/nfl-big-data-bowl-2020/discussion/119430) by CPMP.
- Papers
  - [A Generalization of Transformer Networks to Graphs](https://arxiv.org/abs/2012.09699), Dec 2020
  - [A Gentle Introduction to GNN](https://towardsdatascience.com/a-gentle-introduction-to-graph-neural-network-basics-deepwalk-and-graphsage-db5d540d50b3) Medium, Feb 2019 
  - [GNN: A Review of Methods and Applications](https://arxiv.org/abs/1812.08434): Dic 2018, last revised Jul 2019
  - [A Comprehensive Survey on GNN](https://arxiv.org/abs/1901.00596): Jan 2019, last revised Aug 2019
