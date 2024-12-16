from flask import Flask, render_template, request
from current_disp import create_crrent_disp

app = Flask(__name__)


@app.route("/")
def index():
    # postメソッドでユーザーから指定される
    his_0_name = "data_earth"
    his_1_name = "data_human"
    # ここはloginユーザー名をつけたい
    disp_his_name = "disp_1"
    # 指定の加工が施されたCSVファイルが作成される
    create_crrent_disp(his_0_name, his_1_name, disp_his_name)
    return render_template("index.html")


if __name__ == "__main__":
    # 使用するポートを明示
    app.run(port=8000, debug=True)
