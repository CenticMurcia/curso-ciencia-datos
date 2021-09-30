from catalyst import utils



######################################### Reprocubility
utils.misc.set_global_seed(seed=42) 
utils.torch.prepare_cudnn(deterministic=True)


runner = SupervisedRunner()
runner.train(
	loaders=loaders,
	model=model,
    criterion=criterion,
    optimizer=optimizer,
    scheduler=scheduler,
    num_epochs=8,
    logdir="./logdir",
	main_metric="accuracy01",
	minimize_metric=True,
	apex=True, # If we want mixed precission training (16 bit Float) of NVIDIA APEX
	amp=True,  # If we want mixed precission training (16 bit Float) of Pytorch AMP
	callbacks=[
	    dl.EarlyStoppingCallback(patience=2, metric="loss", minimize=True),
	    dl.BatchOverfitCallback(train=10, valid=0.5) # Use this if we want to overfit for 10 batches in train loader and half of the valid loader
	    dl.CheckRunCallback(num_batch_steps=3, num_epoch_steps=3) # Check the pipeline (run only 3 batches per loader, and 3 epochs per stage) 
	]
)




criterion = {
    "dice": DiceLoss(),
    "iou": IoULoss(),
    "bce": nn.BCEWithLogitsLoss()
}

optimizer = RAdam(model.parameters(), lr=1e-3)

callbacks = [
    dl.CriterionCallback(input_key="mask", prefix="loss_dice", criterion_key="dice"),
    dl.CriterionCallback(input_key="mask", prefix="loss_iou", criterion_key="iou"),
    dl.CriterionCallback(input_key="mask", prefix="loss_bce", criterion_key="bce"),
    dl.MetricAggregationCallback(prefix="loss", mode="weighted_sum", metrics={"loss_dice": 1.0, "loss_iou": 1.0, "loss_bce": 0.8}),
    dl.DiceCallback(input_key="mask"),
    dl.IouCallback(input_key="mask"),
]