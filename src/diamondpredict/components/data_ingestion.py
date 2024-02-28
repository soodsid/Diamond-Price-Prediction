import pandas as pd
import numpy as np
from diamondpredict.loggers import logger
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
import os
from dotenv import find_dotenv


class DataIngestionConfig:
    rawdata_path = str(os.path.join(os.path.dirname(find_dotenv()),'Artifacts','rawdata.csv'))
    traindata_path = str(os.path.join(os.path.dirname(find_dotenv()), 'Artifacts','traindata.csv'))
    testdata_path = str(os.path.join(os.path.dirname(find_dotenv()), 'Artifacts','testdata.csv'))

class DataIngestion:
    def __init__(self):
        self.ingestion_paths=DataIngestionConfig()
        
    @logger.catch()
    def initiate_data_ingestion(self):
        logger.info('data ingestion started')

        try:
            data=pd.read_csv(os.path.join(os.path.dirname(find_dotenv()), 'notebooks', 'data','diamonds.csv'))
            logger.success('data reading succesfull, stored in >> data')
            os.makedirs(os.path.dirname(self.ingestion_paths.rawdata_path), exist_ok=True)

            data.to_csv(self.ingestion_paths.rawdata_path, index=False)
            logger.success('rawdata saved in artifacts folder')

            logger.info('spliting data in train and test')
            traindata, testdata= train_test_split(data, test_size=0.2)
            logger.success('splitting succesfull')
            os.makedirs(os.path.dirname(self.ingestion_paths.traindata_path), exist_ok =True)

            traindata.to_csv(self.ingestion_paths.traindata_path, index=False)
            os.makedirs(os.path.dirname(self.ingestion_paths.testdata_path), exist_ok=True)

            testdata.to_csv(self.ingestion_paths.testdata_path, index=False)
            logger.success('train and test data successfuly saved in artifacts folder')

            logger.success("successfull data ingestion")

        except Exception as e:
            logger.exception(e)
