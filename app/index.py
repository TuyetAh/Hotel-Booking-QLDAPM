from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/dang_nhap")
def dang_nhap():
    return render_template("DangNhap.html")

@app.route("/dang_ky")
def dang_ky():
    return render_template("DangKy.html")

if __name__ == '__main__':
    app.run(debug=True)