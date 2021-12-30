
# Reproducible DL

```python
seed_everything(seed=42):
	os.environ['PYTHONHASHSEED'] = str(seed)
	random.seed(seed)
	np.random.seed(seed)

	# Pytorch
	torch.manual_seed(seed)
	torch.cuda.manual_seed_all(seed)
	torch.backends.cudnn.deterministic = True
	torch.backends.cudnn.benchmark = False

	# Tensorflow
	tf.random.set_seed(seed)
	tf.set_random_seed(seed)
	tf.experimental.numpy.random.seed(seed)
	os.environ['TF_DETERMINISTIC_OPS'] = '1'
	os.environ['TF_CUDNN_DETERMINISTIC'] = '1'
	from tfdeterminism import patch
	patch()
```


- https://github.com/NVIDIA/framework-determinism
- https://github.com/NVIDIA/framework-determinism/blob/master/pytorch.md
- https://pytorch.org/docs/stable/notes/randomness.html
- https://twitter.com/kastnerkyle/status/1473361479143460872
- https://twitter.com/rishabh16_/status/1473472759405551619
