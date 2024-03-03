import os
import pandas as pd
from diamondpredict.loggers import logger
from diamondpredict.utils.utils import load_obj
from dotenv import find_dotenv

class predict_pipeline:
    def __init__(self) -> None:
        pass
    
    @logger.catch()
    def predict(self,features):
        try:
            preprocessor_path=str(os.path.join(os.path.dirname(find_dotenv()),'Artifacts','preprocessor.pkl'))
            model_path=str(os.path.join(os.path.dirname(find_dotenv()),'Artifacts','model.pkl'))

            preprocessor=load_obj(preprocessor_path)
            model=load_obj(model_path)

            scaled_data=preprocessor.transform(features)

            pred = model.predict(scaled_data)

            return pred

        except Exception as e:
            logger.exception(e)