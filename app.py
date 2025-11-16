from flask import Flask, request, jsonify
from google.colab import output
import threading
import time

app = Flask(__name__)

# In-memory database
books = []

@app.route("/books", methods=["GET"])
def get_books():
    return jsonify(books)

@app.route("/books", methods=["POST"])
def add_book():
    data = request.json
    books.append(data)
    return jsonify({"message": "Book added", "book": data})

@app.route("/_reset", methods=["POST"])
def reset_db():
    books.clear()
    return jsonify({"message": "Database reset"})

# Start Flask server in background
def run_app():
    app.run(host="0.0.0.0", port=5000)

thread = threading.Thread(target=run_app)
thread.start()

# Open Colab tunnel
output.serve_kernel_port_as_iframe(port=5000)
time.sleep(2)

print("Server is running! DO NOT STOP THIS CELL.")
