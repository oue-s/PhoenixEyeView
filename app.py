from flask import Flask, render_template, request
from current_disp import create_crrent_disp

app = Flask(__name__)


@app.route("/")
def index():
    # postメソッドでユーザーから指定される
    his_0_name = "earth_point"
    his_1_name = "human_point"
    # ここはloginユーザー名をつけたい
    disp_his_name = "disp_2"
    # postメソッド で時間軸変換を指定する
    # 現状 1 起点を揃える 2 起点と終点を揃える 3 起点を揃えて、傾きを変える
    calc_method = 1
    # 予備の変数 現状slopeに使う
    a = 7
    # 指定の加工が施されたCSVファイルが作成される
    create_crrent_disp(his_0_name, his_1_name, disp_his_name, calc_method, a)
    return render_template("index.html")


if __name__ == "__main__":
    # 使用するポートを明示
    app.run(port=8000, debug=True)
