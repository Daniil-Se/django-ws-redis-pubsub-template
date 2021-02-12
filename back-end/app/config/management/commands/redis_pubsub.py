from django.core.management.base import BaseCommand
import redis
from dashboard.models import TestModel
import json


class Command(BaseCommand):
    def handle(self, *args, **options):

        r = redis.StrictRedis(host='localhost', port=6379, db=1)
        pub_sub = r.pubsub()
        pub_sub.subscribe('__test')

        for msg in pub_sub.listen():
            if msg:
                if msg['data'] != 1:
                    msg_data = json.loads(msg['data'])
                    data = TestModel(test=msg_data['test'])
                    data.save()
                    query = TestModel.objects.all()
                    print(query)
