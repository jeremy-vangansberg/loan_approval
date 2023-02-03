import pickle
import pandas as pd
import numpy as np

model = pickle.load(open('app/xgb.pkl', 'rb'))


col = ['State', 'NAICS', 'Term', 'NoEmp', 'NewExist', 'CreateJob',
       'RetainedJob', 'UrbanRural', 'RevLineCr', 'LowDoc', 'GrAppv']


to_predict = np.array(['FL', '44', 2, 2, 'True', 1, 2, 1, 'Y', 'N', 70000], dtype=object)


labels = [
  'Risque élevé',
  'Risque faible'
 ]

def predict_pipeline(list_of_values=None):
    temp = dict(zip(col,list_of_values))
    to_predict = pd.DataFrame(temp, index=[0])
    index_class = model.predict(to_predict)[0]
    return labels[index_class]


# print(predict_pipeline(list_of_values=to_predict))