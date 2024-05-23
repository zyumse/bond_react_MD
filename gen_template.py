import numpy as np
import pandas as pd
import my_common as mc
import tools_lammps as tl
import pickle

with open('mapping.pkl', 'rb') as file:
    mapping_dict = pickle.load(file)

# reactants
file_lmp = './example/merge/pre_react.dat'
idx_select = np.concatenate((np.array([18,21,22,23,24,25,45,46,47,48,49]),
                             np.array([50,51,52,53,54,55,64,65,66,67,68,77,78]))) 

file_template = './example/react/rxn1_pre.data_template'
tl.write_template(file_lmp,file_template,idx_select,mapping_dict)

# generate a file that can be visualized 
element = mapping_dict['mass_new'][np.argsort([float(item) for item in mapping_dict['mass_new'][:,0]]),2]
tl.visualize_template(file_template,'./example/react/pre_tmp.dat',element)

# products
file_lmp = './example/product.dat'
idx_select = idx_select1 = np.concatenate((np.arange(1,21),np.array([37,38,39,40])))
file_template = './example/react/rxn1_post.data_template'
tl.write_template(file_lmp,file_template,idx_select,mapping_dict)
tl.visualize_template(file_template,'./example/react/post_tmp.dat',element)




