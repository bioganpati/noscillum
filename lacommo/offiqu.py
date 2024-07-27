import redis

r = redis.StrictRedis(host='localhost', port=6379, db=0)

user_id = 123


r.publish(f'user_channel:{user_id}')
