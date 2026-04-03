from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Tạo đối tượng SQLAlchemy để dùng chung toàn project
db = SQLAlchemy()


def create_app():
    app = Flask(__name__)

    # Chuỗi kết nối SQL Server
    # Bạn sửa lại đúng tên server, user, password của máy bạn
    app.config["SQLALCHEMY_DATABASE_URI"] = (
        "mssql+pyodbc://sa:123456@DESKTOP-ABC123/DatPhongKhachSan?driver=ODBC+Driver+17+for+SQL+Server"
    )

    # Tắt cảnh báo không cần thiết
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # Gắn db vào app
    db.init_app(app)

    return app