"""Initizalization point for the API"""

from flask import Flask, jsonify

app = Flask(__name__)

# 1st problem: Given a list of points, a central point, and an integer k,
# find the k closest points to the central point.

points = [(0, 0), (5, 4), (3, 1), (2, 2), (1, 3)]
central_point = (1, 2)
k = 3


@app.route("/ride", methods=["POST"])
def request_ride():
    """Simple Hello World API"""
    return jsonify({"message": "Hello World!"})
