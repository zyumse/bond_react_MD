# import numpy as np
# import pandas as pd
from tools_lammps import compute_mappings,write_lammps_full,convert_lmp
# from .tools_lammps import compute_mappings,write_lammps_full,convert_lmp
import pickle

####### product ########

file_lmp = './example/post_tmp/UNL_BF7C89.lmp'
file_key = './example/post_tmp/UNL_BF7C89.key'

lmp_new, mapping_dict = compute_mappings(file_lmp,file_key)
write_lammps_full('./example/product.dat',lmp_new)

with open('mapping.pkl', 'wb') as file:
    pickle.dump(mapping_dict, file)

###### reactant1 ######## 

file = './example/DGEBA_tmp/UNL_FFFFAF.lmp'
file_key = './example/DGEBA_tmp/UNL_FFFFAF.key'
lmp_react_DGEBA = convert_lmp(file,file_key,mapping_dict)
write_lammps_full('./example/DGEBA.dat',lmp_react_DGEBA)

###### reactant2 ######## 

file = './example/MDA_tmp/UNL_A52E2E.lmp'
file_key = './example/MDA_tmp/UNL_A52E2E.key'
lmp_react_new = convert_lmp(file,file_key,mapping_dict)
write_lammps_full('./example/MDA.dat',lmp_react_new)






