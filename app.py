from flask import Flask, request, jsonify
import unittest

app = Flask(__name__)

@app.route("/plus", methods=["GET"])
def plus():
    try:
        num1 = float(request.args.get("num1"))
        num2 = float(request.args.get("num2"))
        result = num1 + num2
        return jsonify({"Slozhenie": "poluchilos", "Rezultat": result})
    except (TypeError, ValueError):
        return jsonify({"Oshibka": "Vvedite 2 chisla"}), 400

@app.route("/minus", methods=["GET"])
def minus():
    try:
        num1 = float(request.args.get("num1"))
        num2 = float(request.args.get("num2"))
        result = num1 - num2
        return jsonify({"Vychitanie": "poluchilos", "Rezultat": result})
    except (TypeError, ValueError):
        return jsonify({"Oshibka": "Vvedite 2 chisla"}), 400

@app.route("/umnozh", methods=["GET"])
def umnozh():
    try:
        num1 = float(request.args.get("num1"))
        num2 = float(request.args.get("num2"))
        result = num1 * num2
        return jsonify({"Umnozhenie": "poluchilos", "Rezultat": result})
    except (TypeError, ValueError):
        return jsonify({"Oshibka": "Vvedite 2 chisla"}), 400

@app.route("/delenie", methods=["GET"])
def delenie():
    try:
        num1 = float(request.args.get("num1"))
        num2 = float(request.args.get("num2"))
        if num2 == 0:
            return jsonify({"Oshibka": "Nelzya delit' na 0!"}), 400
        result = num1 / num2
        return jsonify({"Delenie": "poluchilos", "Rezultat": result})
    except (TypeError, ValueError):
        return jsonify({"Oshibka": "Vvedite 2 chisla"}), 400

class CalculatorTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
        self.client.testing = True

    def test_plus(self):
        response = self.client.get('/plus?num1=5&num2=3')
        self.assertEqual(response.status_code, 200)
        response_json = response.get_json()
        self.assertEqual(response_json["Slozhenie"], "poluchilos")
        self.assertEqual(response_json["Rezultat"], 8.0)

    def test_minus(self):
        response = self.client.get('/minus?num1=5&num2=3')
        self.assertEqual(response.status_code, 200)
        response_json = response.get_json()
        self.assertEqual(response_json["Vychitanie"], "poluchilos")
        self.assertEqual(response_json["Rezultat"], 2.0)

    def test_umnozh(self):
        response = self.client.get('/umnozh?num1=5&num2=3')
        self.assertEqual(response.status_code, 200)
        response_json = response.get_json()
        self.assertEqual(response_json["Umnozhenie"], "poluchilos")
        self.assertEqual(response_json["Rezultat"], 15.0)

    def test_delenie(self):
        response = self.client.get('/delenie?num1=10&num2=2')
        self.assertEqual(response.status_code, 200)
        response_json = response.get_json()
        self.assertEqual(response_json["Delenie"], "poluchilos")
        self.assertEqual(response_json["Rezultat"], 5.0)

    def test_delenie_zero(self):
        response = self.client.get('/delenie?num1=10&num2=0')
        self.assertEqual(response.status_code, 400)
        response_json = response.get_json()
        self.assertEqual(response_json["Oshibka"], "Nelzya delit' na 0!")

    def test_invalid_input(self):
        response = self.client.get('/plus?num1=abc&num2=3')
        self.assertEqual(response.status_code, 400)
        response_json = response.get_json()
        self.assertEqual(response_json["Oshibka"], "Vvedite 2 chisla")


if __name__ == "__main__":
    app.run(debug=True)

