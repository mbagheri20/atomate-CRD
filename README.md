# <img alt="atomate" src="https://raw.githubusercontent.com/hackingmaterials/atomate/main/docs_rst/_static/atomate_logo_small.png" width="250">

This is a edited version of atomate which used for creating [Computational Raman Database](https://ramandb.oulu.fi/) using [Phonon Database](https://github.com/atztogo/phonondb)

## List of changed files:
* atomate.vasp.drones
* atomate.vasp.firetasks.parse_outputs
* atomate.vasp.firetasks.write_inputs
* atomate.vasp.workflows.base.raman

## List of added files:
* atomate.vasp.workflows.presets.mode_find
* atomate.vasp.workflows.presets.phonondb.db

Note: You may need to change one of the pymatgen files like following file:
* pymatgen_changes.io.sets

You can find the example for submitting job in main branch: Raman-CRD-WF.py

If you find atomate-CRD useful, please cite the following papers in your research output:

```txt
Mathew, K., Montoya, J. H., Faghaninia, A., Dwarakanath, S., Aykol,
M., Tang, H., Chu, I., Smidt, T., Bocklund, B., Horton, M., Dagdelen,
J., Wood, B., Liu, Z.-K., Neaton, J., Ong, S. P., Persson, K., Jain,
A., Atomate: A high-level interface to generate, execute, and analyze
computational materials science workflows. Comput. Mater. Sci. 139,
140-152 (2017).
```


```
@article{CRD,
   doi = {10.1038/s41597-023-01988-5},
   url = {https://doi.org/10.1038/s41597-023-01988-5},
   journal = {Scientific Data},
   year = {2023},
   title = {High-throughput computation of Raman spectra from first principles},
   author = {Mohammad Bagheri and Hannu-Pekka Komsa},
   pages = {80},
   issue = {14},
   volume = {10}
}
```
