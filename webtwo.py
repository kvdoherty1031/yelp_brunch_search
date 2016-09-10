from flask import Flask, render_template, request
from yelpAPITwo import *
app = Flask(__name__)


@app.route("/")
def index():
	# businesslist = []
	address = request.values.get('addresstorender')
	make_params(address)
	return render_template ('indextwo.html', addresstorender=address, businesses=businesslist)

@app.route("/about")
def about():
	return render_template("abouttwo.html")

if __name__ == "__main__":
	app.run()