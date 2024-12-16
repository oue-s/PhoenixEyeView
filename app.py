from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    # if request.method == "GET":
    return render_template("index.html")
    # return "Hello,World"


if __name__ == "__main__":
    # 使用するポートを明示
    app.run(port=8000, debug=True)
