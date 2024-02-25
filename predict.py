from flask import Flask, request, render_template
import copy_of_final_project as cp
import numpy as np

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def check():
    if request.method == 'POST':
        data1 = request.form['field1']
        data2 = request.form['field2']
        data3 = request.form['field3']
        data4 = request.form['field4']
        data5 = request.form['field5']
        data6 = request.form['field6']
        data7 = request.form['field7']
        data8 = request.form['field8']
        data9 = request.form['field9']
        data10 = request.form['field10']
        data11 = request.form['field11']
        data12 = request.form['field12']
        arr = np.array([[data1, data2, data3, data4, data5, data6, data7, data8, data9, data10, data11, data12]])
        result = cp.predict_water_safety(arr)
        if result == 'Safe':
            return render_template('safe.html')
        else:
            return render_template('unsafe.html')
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
    