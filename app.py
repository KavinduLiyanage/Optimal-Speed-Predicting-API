import numpy as np
from flask import Flask, request, jsonify, render_template
# import pickle
from flask_cors import CORS

app = Flask(__name__)
@app.route('/', methods=['GET'])
def home():
    return "This is Optimal speed predicting app"
# CORS(app)
# model = pickle.load(open('model.pkl', 'rb'))

# @app.route('/', methods=['GET'])
# def home():
#     return jsonify({"response":"This is Optimal speed predicting app"})

# @app.route('/predict',methods=['POST'])
# def predict():  
#     int_features = [float(x) for x in request.form.values()]
    
#     print('Vehicle location = ',int_features)
    
#     final_features = [np.array(int_features)]
    
#     prediction = model.predict(final_features)
    
#     output = round(prediction[0])
    
#     print('Predict speed = ', output)

#     return format(output)

if __name__ == "__main__":
    # app.run(host="0.0.0.0", port=5000, debug=True)
    app.run()