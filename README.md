# bond_react_MD

Purpose: to build large molecules from small molecules (monomer) based on reaction-like MD 

Approach: [fix bond/react in lammps](https://docs.lammps.org/fix_bond_react.html), which searches specific reactive patterns in molecules and force the reactive groups to react in a fixed manner when they are within certain distance range. We need to prepare the template files and mapping file, in addition to the standard lammps inputs, in order to clearly inform the algorithm about the reaction details.

This tutorial provides the basic steps and associated tools to prepare the input files for bond/react. 

- Step 1: Prepare initial structures with force field parameters  
    - One way is through the Ligpargen server 
    - This includes all reactants (small molecules) and products. Note that the basic chemical reactions need to be identified clearly. 
- Optional Step: Unify types of atoms, bonds, angles, dihedrals, and impropers
    - This is preferred because Ligpargen generates each atom and `bond' as a unique type
    - This is done by gen_template.py. 
        - It generates a mapping dictionary (based on products, because they  contain the most interaction types) for the type conversion.
        - At the end, it can output new lammps structure files 
    - Check the new structure files in MD simulations  
- Step 2: Merge reactant molecules into one system
    - This can be done with lammps, see example in.merge 
- Step 3: prepare pre_react template 
    - gen_template.py 
    - visualize and check 
- Step 4: prepare post_react template 
    - visualize and check 
- Step 5: prepare the map file 
    - I did it manually

if you find this useful, you could cite [Yu, Z., & Jackson, N. E. (2023). Machine learning quantum-chemical bond scission in thermosets under extreme deformation. Applied Physics Letters, 122(21), https://doi.org/10.1063/5.0150085](https://doi.org/10.1063/5.0150085). 

