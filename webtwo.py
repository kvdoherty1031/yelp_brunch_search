from flask import Flask, render_template, request
from yelpAPITwo import *
import os
app = Flask(__name__)


@app.route("/")
def index():
	businesslist = []
	address = request.values.get('addresstorender')
	businesslist = make_params(address)
	return render_template ('indextwo.html', addresstorender=address, businesses=businesslist)

@app.route("/about")
def about():
	return render_template("abouttwo.html")

if __name__ == "__main__":
	port = int(os.environ.get("PORT", 5000))
	app.run(host="0.0.0.0", port=port)