def compose_fns(*funcs):
    # Create a function that composes all functions in `funcs`,
    # passing along remaining `*args` and `**kwargs` to all"
    # compose_fns(func1, func2)
    #
    # https://github.com/fastai/fastcore/blob/master/fastcore/basics.py#L669
    
    def run_functions(x, *args, **kwargs):
        for f in list(funcs):
            x = f(x, *args, **kwargs)
        return x
    return run_functions


def parallel_map(func, array):

    import multiprocessing
    from concurrent.futures import ProcessPoolExecutor
    from tqdm import tqdm
    
    cpu_cores = multiprocessing.cpu_count()
    array_len = len(array)
    chunksize = array_len // 100
    
    if cpu_cores<2:
        return list(tqdm(map(func, arr), total=array_len))
    else:
        with ProcessPoolExecutor(max_workers=cpu_cores) as ex:
            return list(tqdm(ex.map(func, array, chunksize=chunksize), total=array_len))