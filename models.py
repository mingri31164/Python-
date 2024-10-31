# 连接数据库模型
import json
from datetime import datetime

from exts import db

# 报名表
class EnrollModel(db.Model):
    __tablename__ = "enroll_table"

    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)  # 使用 BigInteger
    created_at = db.Column(db.DateTime, nullable=True)
    updated_at = db.Column(db.DateTime, nullable=True)
    deleted_at = db.Column(db.DateTime, nullable=True)
    student_number = db.Column(db.Text, nullable=False)
    name = db.Column(db.String(20), nullable=False)
    qq_number = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    reason = db.Column(db.String(50), nullable=False)
    grade = db.Column(db.SmallInteger, nullable=False)
    had_experience = db.Column(db.SmallInteger, nullable=False)
    orientation = db.Column(db.String(4), nullable=True)
    experience = db.Column(db.String(50), nullable=True)

    def __repr__(self):
        # 将对象转换为字典
        return json.dumps({
            "id": self.id,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
            "deleted_at": self.deleted_at.isoformat() if self.deleted_at else None,
            "student_number": self.student_number,
            "name": self.name,
            "qq_number": self.qq_number,
            "email": self.email,
            "reason": self.reason,
            "grade": self.grade,
            "had_experience": self.had_experience,
            "orientation": self.orientation,
            "experience": self.experience
        })



 # 考核成绩表
class ScoreModel(db.Model):
    __tablename__ = "score_table"

    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    exam_id = db.Column(db.SmallInteger, nullable=False)
    name = db.Column(db.String(20), nullable=False)
    student_id = db.Column(db.Text, nullable=False)
    account = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    score = db.Column(db.SmallInteger, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now(), nullable=True)

    def __repr__(self):
        # 将对象转换为字典
        return json.dumps({
            "id": self.id,
            "exam_id": self.exam_id,
            "name": self.name,
            "student_id": self.student_number,
            "account": self.account,
            "email": self.email,
            "score": self.score,
            "created_at": self.created_at.isoformat() if self.created_at else None,
        })





