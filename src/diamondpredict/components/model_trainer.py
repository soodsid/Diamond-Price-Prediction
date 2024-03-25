import pandas as pd
import numpy as np
import os
from diamondpredict.loggers import logger
from dataclasses import dataclass
from diamondpredict.utils.utils import evaluate_model
from dotenv import find_dotenv
from diamondpredict.utils.utils import saveobject

from sklearn.linear_model import LinearRegression, Ridge, ElasticNet, Lasso

@dataclass
class ModelTrainerConfig:
    trainedmodel_filepath = str(os.path.join(os.path.dirname(find_dotenv()),'Artifacts','model.pkl'))

class ModelTrainer:
    def __init__(self):
        self.model_trainer_config=ModelTrainerConfig()
        
    @logger.catch()
    def initiate_model_training(self, train_arr, test_arr):
        try:
            logger.info('Spliting the target feature')
            xtrain=train_arr[:,:-1]
            ytrain=train_arr[:,-1]
            xtest=test_arr[:,:-1]
            ytest=test_arr[:,-1]

            models = {
                'linear': LinearRegression(),
                'lasso' : Lasso(),
                'ridge' : Ridge(),
                'elastic':ElasticNet()
            }

            modelreport:dict=evaluate_model(xtrain,ytrain,xtest,ytest, models)
            print(modelreport)
            print('='*80)

            logger.info(f'Model Report : {modelreport}')

            best_model_score = max(sorted(modelreport.values()))
            best_model_name = list(modelreport.keys())[list(modelreport.values()).index(best_model_score)]

            best_model=modelreport[best_model_name]

            print(f'Best Model Found : {best_model_name} , R2 score : {best_model_score}')
            print ('='*80)

            logger.success(f'Best Model Found : {best_model_name} , R2 score : {best_model_score}')

            saveobject(
                filepath=ModelTrainerConfig.trainedmodel_filepath,
                obj=models[best_model_name]
            )

            logger.info('model saved into a pickle file')
            logger.success('Model successfully trained')

        except Exception as e:
            logger.exception(e)