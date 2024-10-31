from flask import Blueprint, Response, jsonify
from utils.redisUtil import get_redis_cli
from domain.dto.recordDTO import RecordDTO

# 初始化Redis
redis_cli = get_redis_cli(0)

#蓝图启用
bp = Blueprint("student", __name__, url_prefix="/")


@bp.route("/test/redis", methods=["POST"])
def test_redis():
    # 将用户信息和座位号保存到Redis
    newrecord = RecordDTO(
        time="1111",
        account="3333",
        password="2222",
        seat="1",
        name="1",
        real_name="1",
        score=-1,
    )
    RecordDTO.store_record_to_redis(newrecord, 1, 1)
    return jsonify({"status": "success", "message": "存入redis成功！"})

@bp.route("/test/get", methods=["GET"])
def test_redis_get():
    record = RecordDTO.get_record_from_redis(2, 2)
    return record


# 登录
@app.route("/login", methods=["GET", "POST"])
def login():
    # 存入
    key = "这是一个redis键"
    redis_cli.set(key, "admin")
    # 取出
    username = redis_cli.get(key)
    print(username)


    if request.method == "POST":
        req_params = dict(request.form)
        # 判断用户名密码是否正确
        sql = "SELECT * FROM `tb_user` WHERE `username` = %s AND `password` = %s"
        params = (req_params["username"], req_params["password"])
        if len(db_query.query(sql, params)) > 0:
            # 存储session
            session["login_username"] = req_params["username"]
            return redirect(url_for("index"))
        else:
            return render_template(
                "error.html",
                error="用户名或密码错误",
            )
    elif request.method == "GET":
        return render_template("login.html")


# 退出
@app.route("/logout")
def logout():
    session.pop("login_username", None)
    return redirect(url_for("index"))


# 注册
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        req_params = dict(request.form)
        if req_params["password"] == req_params["password_confirm"]:
            # 判断是否已存在该用户名
            sql = "SELECT * FROM `tb_user` WHERE `username` = %s"
            params = (req_params["username"],)
            result = db_query.query(sql, params)
            if len(result) > 0:
                return render_template(
                    "error.html",
                    error="用户名已存在",
                )
            sql = "INSERT INTO `tb_user` (`username`, `password`) VALUES (%s, %s)"
            params = (
                req_params["username"],
                req_params["password"],
            )
            db_query.query(sql, params, db_query.QueryType.NO_SELECT)
            return redirect(url_for("login"))
        else:
            return render_template(
                "error.html",
                error="两次密码输入不一致",
            )
    elif request.method == "GET":
        return render_template("register.html")


@app.route("/list")
def movie_list():
    # 查询数据库获取电影列表
    movies = db_query.fetch_movie_list()  # 假设此函数返回一个包含电影信息的列表
    # 渲染并返回list.html，同时传递movies数据
    return render_template(
        "list.html", login_username=session.get("login_username"), movies=movies
    )


@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"), 404


@app.errorhandler(500)
def system_error(error):
    return render_template("500.html"), 500