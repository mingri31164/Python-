import json
from flask import jsonify
from utils.redisUtil import get_redis_cli


redis_cli = get_redis_cli(1)

# 考生账号及座位号变量前缀
EXAM_PRE = "CSD2024_"


# 考生成功签到信息
class RecordDTO:
    def __init__(self, time, account, password, seat, name, real_name, score):
        self.time = time
        self.account = account
        self.password = password
        self.seat = seat
        self.name = name
        self.real_name = real_name
        self.score = score


    def __repr__(self):
        return (f"RecordDTO(time={self.time}, account={self.account}, "
                f"password={self.password}, seat={self.seat}, name={self.name}, "
                f"real_name={self.real_name}, score={self.score})")

    @classmethod
    def from_json(cls, json_str):
        data = json.loads(json_str)
        return cls(**data)

    # 将json对象存入Redis
    def store_record_to_redis(record, exam_id, stu_id):
        print(1111111111111111111111111)
        try:
            # 将对象转换为字典
            record_dict = record.__dict__  # 或者使用 record.to_dict() 方法（如果定义了）
            # 将字典转换为 JSON 字符串
            record_json = json.dumps(record_dict, ensure_ascii=False)
            # 生成 Redis 键
            exam_key = f"{EXAM_PRE}{str(exam_id)}_{str(stu_id)}"
            print(exam_key)
            # 将 JSON 字符串存储到 Redis
            redis_cli.set(exam_key, record_json)

            return jsonify({"status": "success", "message": "存入redis成功！"})
        except Exception as e:
            return jsonify({"status": "error", "message": str(e)}), 500


    # 从Redis中取出
    def get_record_from_redis(exam_id, stu_id):
        # 生成 Redis 键
        exam_key = f"{EXAM_PRE}{str(exam_id)}_{str(stu_id)}"

        # 从 Redis 获取 JSON 字符串
        record_json_from_redis = redis_cli.get(exam_key)

        if record_json_from_redis:
            try:
                # 将 JSON 字符串转换回字典
                record = json.loads(record_json_from_redis)
                return record
            except json.JSONDecodeError:
                print("JSON 解码错误")
                return None
        else:
            print("未找到记录")
            return None
