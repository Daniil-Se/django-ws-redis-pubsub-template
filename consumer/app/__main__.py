import redis
import json
from time import sleep



r = redis.StrictRedis(
	host='localhost',
	port=6379,
	db=0
)


def send_message_from_channel(parameters: dict, redis_name_channel: str) -> None:
    """
    Функция отправки сообщения в канал редиса.
    """
    r.publish(redis_name_channel, json.dumps(parameters))





def main():
	while 1:
		send_message_from_channel(
			parameters={'test': 123},
			redis_name_channel='__test'
		)
		sleep(3)



if __name__ == '__main__':
	main()	