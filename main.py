from flask import Flask

test_op = {
	"data": [
		{
			"agents": "Trixie Mikes",
			"total_calls": 201
		},
		{
			"agents": "Shane Monilar",
			"total_calls": 191
		}
	]
}

app = Flask(__name__)

@app.route('/api/', methods=['GET'])
def get_notofications():
    return test_op

app.run(host='0.0.0.0')