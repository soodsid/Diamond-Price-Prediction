import pandas as pd
import numpy as np
from diamondpredict.loggers import logger
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import os
from dotenv import find_dotenv
from diamondpredict.utils.utils import loadobject
import mlflow

class Model_Evaluation():
    def __init__(self) -> None:
        pass

    def evaluation_metrics(self, ytest, ypred):
        mse=mean_squared_error(ytest, ypred)
        rmse=np.sqrt(mse)
        mae=mean_absolute_error(ytest, ypred)
        r2=r2_score(ytest, ypred)
        return rmse, mse, mae, r2
    
    def initiate_model_eval(self, train_arr, test_arr):
        xtest=test_arr[:,:-1]
        ytest=test_arr[:,-1]

        model_path=str(os.path.join(os.path.dirname(find_dotenv()),'Artifacts','model.pkl'))

        model=loadobject(model_path)

        with mlflow.start_run():
            ypred=model.predict(xtest)
            rmse,mse,mae,r2=self.evaluation_metrics(ytest, ypred)

            mlflow.log_metrics({'rmse':rmse,'mse':mse,'mae':mae,'r2':r2})


