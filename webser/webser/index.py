import random
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Define the list of responses
response = ["Ferrari", "Porsche", "Lexus"]

# Shuffle the list to randomize the order
random.shuffle(response)

@app.route("/")
def index():
    # Get the next item from the shuffled list
    selected_response = response.pop(0) if response else "No more entries"
    top_headlines = [selected_response]
    print(top_headlines)
    
    return jsonify({"news": top_headlines})

if __name__ == "__main__":
    app.run()
