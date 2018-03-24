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

	

@app.route('/message', methods=['POST'])
def message():
	
	dataReceive = request.get_json(force=True)
	content = dataReceive["content"]

	if content == u"안녕":
		dataSend = jsonify({
			"message": {
			"text": "안녕~~ 반가워 ㅎㅎ"
			}
		})
	else:
		message = {}
		message["text"] = content
		data = {}
		data["message"] = message
		dataSend = jsonify(data)
	
	return dataSend
	

if __name__ == '__main__':
    app.run(debug=True)
