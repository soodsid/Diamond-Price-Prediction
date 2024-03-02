from diamondpredict.components import data_ingestion
from diamondpredict.components import data_transformation

from diamondpredict.loggers import logger
import os
import pandas as pd

obj = data_ingestion.DataIngestion()

trainpath, testpath=obj.initiate_data_ingestion()

newobj = data_transformation.DataTransformation()

newobj.initiate_data_transformation(trainpath, testpath)