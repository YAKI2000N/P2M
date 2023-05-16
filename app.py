from flask import Flask, request, jsonify, render_template
import numpy as np 
import pickle
app = Flask(__name__)
#Load the pickle model
model=pickle.load(open("model.pkl","rb"))

@app.route("/")
def home():
        return render_template("index.html")

@app.route("/predict", methods =["POST"])
def predict():
        int_features = [int(x) for x in request.form.values()]
        final_features = [np.array(int_features)]
        prediction = model.predict(final_features)

        prediction_text = "The number of vues is {}, and the number of interessed is {}".format(prediction[0], prediction[1])
        return render_template("index.html", prediction_text=prediction_text)

if __name__ == "__main__" :
        app.run()

        
