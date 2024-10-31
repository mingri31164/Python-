import redis
import config


def get_redis_cli(db_idx):
    redis_client = redis.StrictRedis(
        host=config.REDIS_HOST,
        port=config.REDIS_PORT,
        db=db_idx,
        password=config.REDIS_PASSWORD,
        decode_responses=config.REDIS_DECODE
    )
    return redis_client



