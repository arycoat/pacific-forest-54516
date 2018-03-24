from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return '''{
  "message": {
    "text": "home"
  }
}'''

@app.route('/keyboard', methods=['GET'])
def keyboard():
    return '''{
    "type" : "buttons",
    "buttons" : ["선택 1", "선택 2", "선택 3"]
}'''

if __name__ == '__main__':
    app.run(debug=True)
