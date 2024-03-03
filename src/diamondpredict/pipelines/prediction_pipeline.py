import os
import pandas as pd
from diamondpredict.loggers import logger
from diamondpredict.utils.utils import loadobject
from dotenv import find_dotenv

class predict_pipeline:
    def __init__(self) -> None:
        pass
    
    @logger.catch()
    def predict(self, features):
        try:
            preprocessor_path=str(os.path.join(os.path.dirname(find_dotenv()),'Artifacts','preprocessor.pkl'))
            model_path=str(os.path.join(os.path.dirname(find_dotenv()),'Artifacts','model.pkl'))

            preprocessor=loadobject(preprocessor_path)
            model=loadobject(model_path)

            scaled_data=preprocessor.transform(features)

            pred = model.predict(scaled_data)

            logger.success(f'succesfull preduction\n {pred[0]}')

            return pred

        except Exception as e:
            logger.exception(e)

class customdata:
    @logger.catch()
    def __init__(self, carat, cut, color, clarity, depth, table, x, y, z):
        self.carat=carat
        self.cut=cut
        self.color=color
        self.clarity=clarity
        self.depth=depth
        self.table=table
        self.x=x
        self.y=y
        self.z=z

    @logger.catch()
    def convert_to_dataframe(self):
        try:
            customdict={
                'carat':[self.carat],
                'cut': [self.cut],
                'color': [self.color],
                'clarity' : [self.clarity],
                'depth' : [self.depth],
                'table' : [self.table],
                'x': [self.x],
                'y': [self.y],
                'z': [self.z] 
            }

            df= pd.DataFrame(customdict)
            logger.info(f'data gathered\n {df.to_string()}')

            return df
        except Exception as e:
            logger.exception(e)
