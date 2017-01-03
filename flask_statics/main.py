from flask import Flask
from flask import render_template


app = Flask(__name__)
app.debug = True

@app.route("/static/")
def static_index_route():
    return static_route("index.html")

@app.route("/static/<path:path>")
def static_route(path):
    return app.send_static_file(path)

@app.route("/")
def root():
    return render_template("index.html")

if __name__ == "__main__":
    app.run()

