#Run -  pip install -r requirements.txt Before 

from flask import Flask , jsonify
import requests

app = Flask(__name__)

@app.route("/", methods=['GET',])
def home():
    url = "https://official-joke-api.appspot.com/random_joke"
    try:
        response = requests.get(url, timeout=1)
        response.raise_for_status() 
    except requests.exceptions.HTTPError as http_err:
        print("HTTP Error") 
        print(http_err.args[0]) 
    except requests.exceptions.RequestException as req_err:  
        print("Exception request") 
    except requests.exceptions.ReadTimeout as time_err: 
        print("Time out") 
    
    response_json = response.json()
    ID_VALUE = response_json.get("id")
    PUNCHLINE_VALUE = response_json.get("punchline")

    return jsonify({"ID": ID_VALUE, "Punchline": PUNCHLINE_VALUE})
    
if __name__ == "__main__":
    app.run(debug=True, port=3001) 