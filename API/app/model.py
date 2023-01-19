import pickle
import pandas as pd

model = pickle.load(open('app/rfc.sav', 'rb'))


col = ['Term', 'NoEmp', 'NewExist', 'CreateJob', 'RetainedJob', 'UrbanRural',
       'RevLineCr', 'LowDoc', 'DisbursementGross', 'BalanceGross', 'GrAppv']


to_predict = [84, 45, 1.0, 0, 0, 0, 'N', 'N', 170000, 0, 170000, 127500]

labels = [
  'Risque élevé',
  'Risque faible'
 ]

def predict_pipeline(list_of_values=None):
    temp = dict(zip(col,list_of_values))
    to_predict = pd.DataFrame(temp, index=[0])
    index_class = model.predict(to_predict)[0]
    return labels[index_class]
