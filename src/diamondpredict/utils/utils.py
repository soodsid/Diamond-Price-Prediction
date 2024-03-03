import os
import pickle
import numpy as np
import pandas as pd
from diamondpredict.loggers import logger
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error


@logger.catch()
def saveobject(filepath, obj):
    try:
        dirpath=os.path.dirname(filepath)
        os.makedirs(dirpath, exist_ok=True)
        with open (filepath,'wb') as fileobj:
            pickle.dump(obj, fileobj)

    except Exception as e:
        logger.exception(e)

@logger.catch()
def evaluate_model(xtrain,ytrain,xtest,ytest, models):       
    try:
        report={}
        for i in range(len(models)):
            model=list(models.values())[i]
            model.fit(xtrain,ytrain)

            ypred=model.predict(xtest)

            testmodelscore=r2_score(ytest,ypred)

            report[list(models.keys())[i]] = testmodelscore

        return report        

    except Exception as e:
        logger.exception(e)

@logger.catch()
def loadobject(filepath, obj):
    try:
        with open (filepath,'rb') as fileobj:
            pickle.load(fileobj)

    except Exception as e:
        logger.exception(e)