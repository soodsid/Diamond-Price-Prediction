from diamondpredict.pipelines.prediction_pipeline import predict_pipeline, customdata
from flask import Flask, request, render_template,jsonify
from diamondpredict.loggers import logger

app=Flask(__name__)

@logger.catch()
@app.route('/')
def home_page():
    return render_template('index.html')


@logger.catch()
@app.route('/predict', methods=["GET","POST"])
def predicts():
    if request.method=="GET":
        return render_template('predict.html')
    else:
        data=customdata (
            carat=float(request.form.get('carat')),
            depth=float(request.form.get('depth')),
            table=float(request.form.get('table')),
            x=float(request.form.get('x')),
            y=float(request.form.get('y')),
            z=float(request.form.get('z')),
            cut=request.form.get('cut'),
            color=request.form.get('color'),
            clarity=request.form.get('clarity')
        )

        finaldata=data.convert_to_dataframe()

        prediction=predict_pipeline()

        res=round(prediction.predict(finaldata)[0],3)

        return render_template('result.html', result=res)


if __name__=='__main__':
    app.run(host='0.0.0.0', port=8080)