from flask import Flask, render_template, request, flash
import pickle
from flask_cors import CORS

app = Flask(__name__)
app.secret_key = "manbearpig_MUDMAN888"
# CORS(app)
# model = pickle.load(open('model.pkl', 'rb'))

@app.route("/")
def index():
	flash("what's your name?")
	return render_template("index.html")

@app.route("/greet", methods=['POST', 'GET'])
def greeter():
	flash("Hi " + str(request.form['name_input']) + ", great to see you!")
	return render_template("index.html")

@app.route('/predict',methods=['POST'])
def predict():  
    int_features = [float(x) for x in request.form.values()]
    
    print('Vehicle location = ',int_features)
    
    # final_features = [np.array(int_features)]
    
    # prediction = model.predict(final_features)
    
    # output = round(prediction[0])
    
    # print('Predict speed = ', output)

    return format(int_features)