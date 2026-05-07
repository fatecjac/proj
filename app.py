from flask import Flask
app = Flask (__name__)

@app.route("/")
def home():
	return "<h1>server</h1><p>flask</p>"
if __name__ == "__main__":
	app.run()
