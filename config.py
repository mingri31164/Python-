# 数据库的配置信息
HOSTNAME = '139.9.51.109'
PORT     = '3306'
DATABASE = 'db_douban'
USERNAME = 'mingri'
PASSWORD = 'mingri1234'
DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(USERNAME,PASSWORD,HOSTNAME,PORT,DATABASE)
SQLALCHEMY_DATABASE_URI = DB_URI



# Redis配置信息
REDIS_HOST = '139.9.82.205' # Redis服务器的端口
REDIS_PORT = '6379' # redis端口号
REDIS_PASSWORD = '123456' #redis密码
# REDIS_DB = '1'
REDIS_DECODE = True # 如果为True，将返回的数据解码为字符串





