import numpy as np
import pandas as pd
import my_common as mc
import tools_lammps as tl
import pickle

file_lmp = './2DGEBA_MDA/post/post_new0.dat'

with open('mapping.pkl', 'rb') as file:
    mapping_dict = pickle.load(file)

#### specify ####
# idx_select = np.concatenate((np.array([18,21,22,23,24,25,45,46,47,48,49]),
#                              np.array([50,51,52,53,54,55,64,65,66,67,68,77,78]))) 
idx_select = np.concatenate((np.arange(1,24+1),np.arange(63,69+1),np.arange(86,89+1)))

file_template = './test_new/rxn2_post_v2.data_template'
tl.write_template(file_lmp,file_template,idx_select,mapping_dict)

# generate a file that can be visualized 
# tl.visualize_template(file_template,'./test_new/tmp.data',mapping_dict['mass_new'][:,2])
