from flask import*
app = Flask(__name__) 

@app.route("/")
@app.route("/index")
def table():
    return render_template("index.html")

def hello():
    return "Hello World!"

@app.route("/content")
def content():
    return "<h1>This is the content of the page</h1>"

if __name__ == "__main__":
    app.run(debug=True)
