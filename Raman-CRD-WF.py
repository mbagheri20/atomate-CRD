# This is an example for submitting job in edited version of Raman workflow
# Calcualte Raman Tensor with Phonopy database

from pymatgen.core import Structure
from pymatgen.io.vasp.inputs import Incar
from pymatgen.io.vasp.inputs import Kpoints
from fireworks import LaunchPad
from atomate.vasp.workflows.presets.core import wf_raman_spectra
from atomate.vasp.powerups import add_modify_incar , add_modify_kpoints
from pymatgen.io.ase import AseAtomsAdaptor
import atomate
from ase import io,Atoms
import phonopy
import numpy as np
from atomate.vasp.workflows.presets.mode_find import data_active
from atomate.vasp.workflows.presets.mode_find import rk_select

mat_id = "mpid=mp-19921"
active_modess=data_active(matid=mat_id)
egap = rk_select(matid=mat_id)
# Load structure from file
ph = phonopy.load("phonon.yaml",primitive_matrix='auto')
pc = ph.get_primitive()
pca = Atoms(pc.get_chemical_symbols(),positions=pc.get_positions(), cell=pc.get_cell(), pbc=True)
io.write('POSCAR-pc',pca)


aa = AseAtomsAdaptor()
struct = aa.get_structure(pca)
#struct = Structure.from_file('POSCAR-unitcell')

# Load Phonopy INCAR
my_incar = Incar.from_file("INCAR-nac").as_dict()
item_remove = ['@module', '@class', 'LCHARG', 'LWAVE']
for key in item_remove:
 del my_incar[key]
 
my_incar.update({'LPEAD': False, 'LAECHG': False, 'ISIF': 2, 'LASPH': False, 'ISPIN': 1, 'LVHAR': False})

# Load phonopy KPOINT
Rk=40
N1 = int(max(1,Rk*struct.lattice.reciprocal_lattice.a/(2*np.pi)+0.5))
N2 = int(max(1,Rk*struct.lattice.reciprocal_lattice.b/(2*np.pi)+0.5))
N3 = int(max(1,Rk*struct.lattice.reciprocal_lattice.c/(2*np.pi)+0.5))
my_kpoints = {'nkpoints': 0,
          'generation_style': 'Gamma',
          'kpts': [[N1, N2, N3]],
          'kpts_shift': [0, 0, 0],
          'comment': 'Automatic mesh'}


ram_setting = {"MODES":active_modess}
# Create the Workflow
original_wf = wf_raman_spectra(struct, c=ram_setting)
modified_wf = add_modify_incar(original_wf, modify_incar_params={'incar_update':my_incar},fw_name_constraint='a')
final_wf = add_modify_kpoints(modified_wf, modify_kpoints_params={'kpoints_update':my_kpoints})
# Instatiate the LaunchPad and add the workflow to it
lpad = LaunchPad.auto_load()
lpad.add_wf(final_wf)
