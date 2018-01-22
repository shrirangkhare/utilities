
import pandas as pd
import numpy as np

endpoints = pd.read_csv('/Users/shrirangkhare/DeviceDiscoveryTestTools/cyclist_lastname.csv',usecols = ['devicetype','os','deviceclassification','loc'])
endpoints1 = pd.read_csv('/Users/shrirangkhare/DeviceDiscoveryTestTools/test_data.csv', usecols = ['devicetype','os','deviceclassification','loc'])



eppv  = pd.pivot_table(endpoints, index = ['os','devicetype','loc'], columns = ['deviceclassification'], aggfunc= np.count_nonzero)
eppv1 = pd.pivot_table(endpoints1,index = ['os','devicetype','loc'], columns = ['deviceclassification'], aggfunc= np.count_nonzero)

print(type(eppv))

# def process_first(mainpivot, dclass):
#     print (type(eppv[dclass]))
#     print (eppv[dclass]['Linux'].index.levels)
#
# v = eppv.columns.get_values()
# for el in v:
#     process_first(eppv, el)

