import numpy as np
from ase.db import connect

#Check Active mode mpid=19921

def data_active(matid, raman_active= []):
    db = connect('phonondb.db')
    rows = db.select(selection=matid)
    for row in rows:
        act = np.array(row.data.Ramanactive)
        act[0:3] = 0
        raman_active.append(list(np.nonzero(act)[0]))
    active_2 = raman_active[0]
    pyintmode = []
    for i in range(len(active_2)):
        pyintmode.append(int(active_2[i]))

    return pyintmode

def rk_select(matid):
    db = connect('phonondb.db')
    rows = db.select(selection='mpid='+matid)
    for row in rows:
        e_gap = row.bandgap_mp
    return e_gap
