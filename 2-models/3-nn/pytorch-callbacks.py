# Fast.ai           https://docs.fast.ai/callback.core.html
# Torch bearer      https://torchbearer.readthedocs.io/en/latest/code/callbacks.html
# Pytorch-Lightning https://pytorch-lightning.readthedocs.io/en/latest/#tutorials



before_fit()
for e in range(epochs):
	
	before_epoch()

	before_train()
	for x,y in train_dl:
		
		after_get_xy()
		#p = model(x)
		after_foward()
		# l = loss(p,y)
		after_loss()
		# loss.backward()
		after_backward()
		# optimizer_step 
		after_step()

	after_train()

	before_validate()
	for x,y in valid_dl:


    after_validate()
    
    after_epoch()

after_fit()




class SetSeedCallback(Callback):

	def before_fit(self, seed):
	    random.seed(seed)
	    os.environ['PYTHONHASHSEED'] = str(seed)
	    np.random.seed(seed)
	    torch.manual_seed(seed)
	    torch.cuda.manual_seed_all(seed)
	    torch.backends.cudnn.deterministic = True
	    torch.backends.cudnn.benchmark = False