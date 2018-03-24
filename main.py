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
	
	dataSend = {
		"type":"text"
    }
 
	return jsonify(dataSend)

	

@app.route('/message', methods=['GET'])
def message():
	dataReceive = request.get_json()
	
	content = dataReceive['content']

	if u"안녕" in content:
		dataSend = {
			"message": {
			"text": "안녕~~ 반가워 ㅎㅎ"
			}
		}
	else:
		dataSend = {
			"message": {
			"text": "..."
			}
		}

	return jsonify(dataSend)
	

if __name__ == '__main__':
    app.run(debug=True)
