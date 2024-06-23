import h5py
import os

file_path = os.path.join("Table_extract_robust", "conc_col.h5")
#file_path = os.path.join("Table_extract_robust", "valid_cells.h5")

# def print_hdf5_item(name, item):
#     if isinstance(item, h5py.Group):
#         print(f"Group: {name}")
#         for key in item.keys():
#             print_hdf5_item(f"{name}/{key}", item[key])
#     elif isinstance(item, h5py.Dataset):
#         print(f"Dataset: {name}")
#         print(f"Shape: {item.shape}")
#         print(f"Datatype: {item.dtype}")
#         print("Data:")
#         print(item[()])  # Print data (use item[()] for NumPy array)

# with h5py.File(file_path, "r") as file:
#     file.visititems(print_hdf5_item)

with h5py.File(file_path, "r") as file:
    print("Keys:", list(file.keys()))
