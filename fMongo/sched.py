from flask1_mongo.user import CurrentToken,BlacklistToken
from apscheduler.schedulers.blocking import BlockingScheduler
from flask import request
from werkzeug.wrappers import Request
from flask1_mongo import app
from flask1_mongo.middleware import Middleware
#global sched

def blacklisting(token):
    print("sched started")
    for curToken in CurrentToken.objects():
        if (curToken.created_on >= datetime.datetime.utcnow()-datetime.timedelta(seconds=500)):
            token = curToken.token
            b=BlacklistToken(token=token).save()
            CurrentToken.objects(token=token).first().delete()
    print("sched end")

sched = BlockingScheduler(timezone="UTC")
sched.add_job(blacklisting, 'interval', seconds=300)
sched.start()

#run_at = datetime.datetime.utcnow() + datetime.timedelta(seconds=500)