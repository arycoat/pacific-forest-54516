from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/keyboard', methods=['GET'])
def keyboard():
    return '{
  "message": {
    "text": "안녕!"
  }
}'

if __name__ == '__main__':
    app.run(debug=True)
