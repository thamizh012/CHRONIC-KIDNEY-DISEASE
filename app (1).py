import flask
from flask import Flask, render_template, request
import pickle
import numpy as np



app = Flask(__name__)

model = pickle.load(open('CKD.pkl', 'rb'))


@app.route('/')
def home():
    return render_template('predictResult.html')


@app.route('/getdata', methods=['POST'])
def pred():
    rbc = request.form['red_blood_cell']
    print('rbc' + rbc)
    pus_cell = request.form['pus_cell']
    print('Pus' + pus_cell)
    blood_glucose = request.form['blood_glucose_random']
    print('glu' + blood_glucose)
    urea = request.form['blood_urea']
    print('urea' + urea)
    pedal_edema = request.form['pedal_edema']
    print('ede' + pedal_edema)
    anemia = request.form['anemia']
    print('anemia' + anemia)
    diabetesmellitus = request.form['diabetesmellitus']
    coronary_artery_disease = request.form['coronary_artery_disease']

    inp_features = [[int(rbc), int(pus_cell), np.log(float(blood_glucose)), np.log(float(urea)), int(pedal_edema), int(anemia),
         int(diabetesmellitus),
         int(coronary_artery_disease)]]

    prediction = model.predict(inp_features)
    print(type(prediction))
    t = prediction[0]
    print(t)
    if t > 0.5:
        prediction_text = 'OOPS! You have Chronic Kidney Disease. Consult the Specialist'
    else:
        prediction_text = 'Well! You are safe & healthy'
    print(prediction_text)
    return render_template('result.html', prediction_results=prediction_text)


if __name__ == "__main__":
    app.run()
