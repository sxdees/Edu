from flask import Flask, request, jsonify
import unittest

app = Flask(__name__)

class Calculator:
    
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def subtract(a, b):
        return a - b

    @staticmethod
    def multiply(a, b):
        return a * b

    @staticmethod
    def divide(a, b):
        if b == 0:
            raise ZeroDivisionError("Нельзя делить на 0")
        return a / b

def get_numbers():
    try:
        num1 = float(request.args.get("num1"))
        num2 = float(request.args.get("num2"))
        return num1, num2
    except (TypeError, ValueError):
        return None, None

def handle_request(operation):
    num1, num2 = get_numbers()
    if num1 is None or num2 is None:
        return jsonify({"error": "Введите два числа"}), 400

    try:
        result = operation(num1, num2)
        return jsonify({"result": result})
    except ZeroDivisionError:
        return jsonify({"error": "Нельзя делить на 0"}), 400

@app.route("/add", methods=["GET"])
def add():
    return handle_request(Calculator.add)

@app.route("/subtract", methods=["GET"])
def subtract():
    return handle_request(Calculator.subtract)

@app.route("/multiply", methods=["GET"])
def multiply():
    return handle_request(Calculator.multiply)

@app.route("/divide", methods=["GET"])
def divide():
    return handle_request(Calculator.divide)

class CalculatorTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_add(self):
        response = self.client.get('/add?num1=5&num2=3')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()["result"], 8.0)

    def test_divide_by_zero(self):
        response = self.client.get('/divide?num1=10&num2=0')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.get_json()["error"], "Нельзя делить на 0")

if __name__ == "__main__":
    app.run(debug=True)
