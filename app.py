from flask import Flask, render_template, request
import backend

app = Flask(__name__)

@app.route("/", methods = ["GET", "POST"])
def home():
    if request.method == "GET":
        return render_template("index.html")


    if request.method == "POST":
        day = request.form.get('textbox')
        day = int(day)
        return render_template("index.html",
        output = backend.days_feet(day),
        user_text = day)

if __name__ == "__main__":
    app.run()
