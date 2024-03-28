from diamondpredict.components import data_ingestion
from diamondpredict.components import data_transformation
from diamondpredict.components import model_trainer
from diamondpredict.components import model_evaluation


from diamondpredict.loggers import logger
import pandas as pd

for i in range(100):

    ingest = data_ingestion.DataIngestion()
    trainpath, testpath=ingest.initiate_data_ingestion()

    transform = data_transformation.DataTransformation()
    train_arr, test_arr=transform.initiate_data_transformation(trainpath, testpath)

<<<<<<< HEAD
    train=model_trainer.ModelTrainer()
    train.initiate_model_training(train_arr, test_arr)

    eval=model_evalutation.Model_Evaluation()
    eval.initiate_model_eval(train_arr, test_arr)
=======
eval=model_evaluation.Model_Evaluation()
eval.initiate_model_eval(train_arr, test_arr)
>>>>>>> a96c5650fd5b0140f5c2ff29110b46cd30aee007

