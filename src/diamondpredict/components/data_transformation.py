import os
import sys
import pandas as pd
import numpy as np
from dataclasses import dataclass
from diamondpredict.loggers import logger
from dotenv import find_dotenv

from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OrdinalEncoder, StandardScaler

#from diamondpredict.utils.utils import saveobject

@dataclass
class DataTransformationConfig:
    preprocessor_path=str(os.path.join(os.path.dirname(find_dotenv()),'Artifacts','preprocessor.pkl'))

class DataTransformation:
    def __init__(self):
        self.transformationconfig=DataTransformationConfig()
    
    @logger.catch()
    def get_data_transformation(self):
        try:
            logger.info('Data Transformation initiated')

            catcolnames=['cut', 'color', 'clarity']
            numcolnames=['carat', 'depth', 'table', 'x', 'y', 'z']

            cutrank = ['Fair', 'Good', 'Very Good', 'Premium', 'Ideal']
            colorrank = ['D','E','F','G','H','I','J']
            clarityrank = ['I1', 'SI2','SI1','VS2','VS1','VVS2', 'VVS1', 'IF']

            logger.info('pipepline initiated')

            catpipe=Pipeline(
                steps=[
                    ('imputer', SimpleImputer(strategy='most_frequent')),
                    ('encode', OrdinalEncoder(categories=[cutrank,colorrank,clarityrank])),
                    ('scalar', StandardScaler())
                ]
            )
            numpipe=Pipeline(
                steps=[
                    ('imputer', SimpleImputer(strategy='median')),
                    ('scalar', StandardScaler())
                ]
            )

            preprocessor=ColumnTransformer(
                transformers=[
                    ('cat', catpipe, catcolnames),
                    ('num', numpipe, numcolnames)
                ]
            )

            return preprocessor

        except Exception as e:
            logger.exception(e)

    def initiate_data_transformation(self, traindata_path, testdata_path):
        try:
            logger.info('reading train and test data')
            traindf=pd.read_csv(traindata_path)
            testdf=pd.read_csv(testdata_path)

            logger.success(f'data reading sucessfull \n')
            logger.success(f'Training data \n{traindf.head().to_string()}')
            logger.success(f'Testing data \n{testdf.head().to_string()}')

            preprocessing_obj=self.get_data_transformation()

            targetcol ='price'
            drop_col=[targetcol, 'Unnamed: 0']

            input_feature_train_df=traindf.drop(drop_col, axis=1)
            input_feature_test_df=testdf.drop(drop_col, axis=1)
            target_feature_train_df=traindf[targetcol]

            input_feature_train_turned=preprocessing_obj.fit_transform(input_feature_train_df)
            input_feature_test_turned=preprocessing_obj.transform(input_feature_test_df)

            logger.success(f'Training Features Transformed \n{input_feature_train_turned[0:5]}')
            logger.success(f'Testing Features Transformed \n{input_feature_test_turned[0:5]}')

#            saveobject(
#                filepath=DataTransformationConfig.preprocessor_path,
#                obj=preprocessing_obj
#            )

        except Exception as e:
            logger.exception(e)