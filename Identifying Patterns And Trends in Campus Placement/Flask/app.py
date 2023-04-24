from flask import Flask,render_template,request
app=Flask(__name__)
import pickle
import joblib
file = open("./placement.pkl", 'rb')
model = pickle.load(file)
ct = joblib.load("placement.pkl")

@app.route("/")
def hello():
    return render_template("index1.html")

@app.route('/guest')
def Guest():
    return render_template("index.html")

@app.route('/y_predict', methods = ["POST"])
def y_predict():
    x_test = [[int(yo) for yo in request.form.values()]]
    prediction = model.predict(x_test)
    prediction = prediction[0]
    return render_template("secondpage.html",y=prediction)

if __name__ == "__main__":
    app.run(debug=True)