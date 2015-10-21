from activepapers.contents import data
import numpy as np

# Create groups for the input data
inputs = data.create_group('inputs')

# creating a numpy array
arr = np.arange(100)

# Adding the numpy array to the groups
inputs['dataset_1'] = arr
inputs['dataset_2'] = arr 
