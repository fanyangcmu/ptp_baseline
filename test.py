import h5py 
import numpy as np

def read_h5_dict(path, data_names=None, exclude_names=[]):
    hf = h5py.File(path, 'r')
    data = {}
    hf_names = hf.keys()
    data_names = hf_names if data_names is None else data_names
    for name in data_names:
        if name in exclude_names or name not in hf_names:
            continue
        d = np.array(hf.get(name))
        data[name] = d
    hf.close()
    breakpoint()
    return data


if __name__ == "__main__":
    read_h5_dict('data/rope/rope_rollout_v6.h5')