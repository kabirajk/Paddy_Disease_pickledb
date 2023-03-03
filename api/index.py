from flask import Flask, request, jsonify
import pickledb 

app = Flask(__name__)
db = pickledb.load('example.db', False)
db.set("Count",0)

@app.route('/')
def home():
    return 'Hello, paddydisease'


@app.route('/image/<id>')
def getimage(id):
    imageuri = db.get(""+str(id))
    return '<img src="' + imageuri + '">'


@app.route('/predict', methods=['POST'])
def predict():
    global globalImage
    input_json = request.get_json(force=True)
    uri = input_json['imguri']
    count = int(db.get("Count"))
    count += 1
    db.set("" + str(count),uri)
    return jsonify({"imageId": "image/" + str(count)})


@app.route('/flush')
def flush():
    pass


@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers',
                         'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
    return response


# if __name__ == '__main__':
# 	app.run(host="0.0.0.0", port=int("5000"), debug=True)
# if __name__ == "__main__":  # Makes sure this is the main process
# 	app.run( # Starts the site
# 		host='0.0.0.0',  # EStablishes the host, required for repl to detect the site
# 		port=5000  # Randomly select the port the machine hosts on.
# 	)