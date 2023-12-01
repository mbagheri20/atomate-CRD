
This is a edited version of atomate which used for creating [Computational Raman Database](https://ramandb.oulu.fi/) using [Phonon Database](https://github.com/atztogo/phonondb).

* Note: This is an unofficial version of atomate and original source can be found [here](https://github.com/hackingmaterials/atomate) .

## Instalation
Original documentaion for configuring and installing atomate can be find here: https://hackingmaterials.github.io/atomate/
You have to follow same process for this edited version.


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

Original paper for atomate

```txt
Mathew, K., Montoya, J. H., Faghaninia, A., Dwarakanath, S., Aykol,
M., Tang, H., Chu, I., Smidt, T., Bocklund, B., Horton, M., Dagdelen,
J., Wood, B., Liu, Z.-K., Neaton, J., Ong, S. P., Persson, K., Jain,
A., Atomate: A high-level interface to generate, execute, and analyze
computational materials science workflows. Comput. Mater. Sci. 139,
140-152 (2017).
```

- "High-throughput computation of Raman spectra from first principles",

  Mohammad Bagheri & Hannu-Pekka Komsa, Sci. Data, **10**, 80 (2023)

  https://doi.org/10.1038/s41597-023-01988-5 (Open access)


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
