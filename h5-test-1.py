import h5py
from tabulate import tabulate

with h5py.File('data00000395.h5', 'r') as f:
    with open('output.txt', 'w') as out_file:
        def write_attrs(name, obj):
            if isinstance(obj, h5py.Dataset):
                data = obj[()]
                out_file.write(f"\nDataset: {name}\n")
                if data.ndim > 1:
                    out_file.write(tabulate(data, headers='keys', tablefmt='grid') + "\n")
                else:
                    out_file.write(str(data) + "\n")

        f.visititems(write_attrs)