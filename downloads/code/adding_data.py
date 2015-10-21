from activepapers.contents import data
import numpy as np

# Create group for the output data
output = data.create_group('output')

input_data = data['inputs']

# Adding the 2 inputs array
arr_1 = input_data['dataset_1'][:].astype(np.int)
arr_2 = input_data['dataset_2'][...].astype(np.int)
sum = arr_1 + arr_2

# Writing the output 
output['sum'] = sum
