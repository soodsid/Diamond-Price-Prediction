from diamondpredict.components import data_ingestion
from diamondpredict.loggers import logger
import os
import pandas as pd

obj = data_ingestion()

obj.initiate_data_ingestion()