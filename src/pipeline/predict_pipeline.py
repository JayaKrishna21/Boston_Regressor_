import sys
import pandas as pd

from src.exception import CustomException
from src.utils import load_object # to load pickle file

class PredictPipeline:
    def __init__(self):
        pass

    def predict(self,features):
        try:
            model_path = 'artifacts\model.pkl'
            preprocessor_path = 'artifacts\preprocessor.pkl'

            model = load_object(file_path = model_path)
            preprocessor = load_object(file_path = preprocessor_path)
            data_scaled = preprocessor.transform(features)

            preds = model.predict(data_scaled)
            return preds
        except Exception as e:
            raise CustomException(e,sys)



class CustomData:

    # responsible to map the input values to pickle file

    def __init__(self,
                CRIM : int,
                ZN : int,
                INDUS : int,
                CHAS : int,
                NOX : int,
                RM : int,
                AGE : int,
                DIS : int,
                RAD : int,
                TAX : int,
                PTRATIO : int,
                B : int,
                LSTAT : int):
        
        self.CRIM  = CRIM

        self.ZN = ZN

        self.INDUS = INDUS

        self.CHAS = CHAS

        self.NOX = NOX

        self.RM = RM

        self.AGE = AGE

        self.DIS = DIS

        self.RAD = RAD

        self.TAX = TAX

        self.PTRATIO = PTRATIO

        self.B = B

        self.LSTAT = LSTAT


    def get_data_as_df(self):
        #mapping data to respective keys

        try:
            custom_data_input_dict = {
                'CRIM' : [self.CRIM],
                'ZN' : [self.ZN],
                'INDUS' : [self.INDUS],
                'CHAS' : [self.CHAS],
                'NOX' : [self.NOX],
                'RM' : [self.RM],
                'AGE' : [self.AGE],
                'DIS' : [self.DIS],
                'RAD' : [self.RAD],
                'TAX' : [self.TAX],
                'PTRATIO' : [self.PTRATIO],
                'B' : [self.B],
                'LSTAT' : [self.LSTAT]
            }
            return pd.DataFrame(custom_data_input_dict)
         
        except Exception as e:
            raise CustomException(e,sys)

