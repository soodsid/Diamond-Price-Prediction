from diamondpredict.pipelines import prediction_pipeline

a=prediction_pipeline.customdata(0.23,'Ideal','J','VS1',62.8,56.0,3.93,3.9,2.46)

feature=a.convert_to_dataframe()

prediction=prediction_pipeline.predict_pipeline()

res=prediction.predict(feature)

print(res)
