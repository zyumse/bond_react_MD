# import numpy as np
# import pandas as pd
import my_common as mc
import tools_lammps as tl
import pickle

####### product ########

file_lmp = './2DGEBA_MDA/post/tmp/UNL_64725F.lmp'
file_key = './2DGEBA_MDA/post/tmp/UNL_64725F.key'

lmp_new, mapping_dict = tl.compute_mappings(file_lmp,file_key)
tl.write_lammps_full('./product.dat',lmp_new)

with open('mapping.pkl', 'wb') as file:
    pickle.dump(mapping_dict, file)

###### reactant1 ######## 

file = './DGEBA_n1/tmp/UNL_0DE044.lmp'
file_key = './DGEBA_n1/tmp/UNL_0DE044.key'
lmp_react_new = tl.convert_lmp(file,file_key,mapping_dict)
tl.write_lammps_full('./DGEBA.dat',lmp_react_new)

###### reactant2 ######## 

file = './MDA_sim/tmp/UNL_A52E2E.lmp'
file_key = './MDA_sim/tmp/UNL_A52E2E.key'
lmp_react_new = tl.convert_lmp(file,file_key,mapping_dict)
tl.write_lammps_full('./MDA.dat',lmp_react_new)






