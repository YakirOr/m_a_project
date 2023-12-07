#pip install flask & jsonify & requests

from flask import Flask , jsonify
import requests
app = Flask(__name__)

@app.route("/", methods=['GET',])
def home():
    url = "https://official-joke-api.appspot.com/random_joke"
    response = requests.get(url)
    response_json = response.json()
    ID_VALUE = response_json.get("id")
    PUNCHLINE_VALUE = response_json.get("punchline")
    return jsonify({"ID: ": ID_VALUE}, {"Punchline: ": PUNCHLINE_VALUE})
    
if __name__ == "__main__":
    app.run(debug=True, port=3001) 