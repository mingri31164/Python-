# exts.py：这个文件存在的意义就是为了解决循环引用的问题（数据库连接时）

# flask-sqlalchemy
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
