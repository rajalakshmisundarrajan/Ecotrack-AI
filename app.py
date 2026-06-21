from flask import Flask, render_template, request
from carbon_calculator import calculate_carbon
from recommendation_engine import generate_recommendations

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/calculate", methods=["POST"])
def calculate():

    name = request.form["name"]
    transport = request.form["transport"]
    distance = float(request.form["distance"])
    electricity = float(request.form["electricity"])
    diet = request.form["diet"]

    carbon = calculate_carbon(
        transport,
        distance,
        electricity,
        diet
    )

    eco_score, category, recommendations = generate_recommendations(carbon)

    return render_template(
        "result.html",
        name=name,
        carbon=carbon,
        eco_score=eco_score,
        category=category,
        recommendations=recommendations
    )


if __name__ == "__main__":
    import webbrowser
    import threading

    def open_browser():
        webbrowser.open_new("http://127.0.0.1:5000/")

    threading.Timer(1.0, open_browser).start()
    app.run(debug=True)