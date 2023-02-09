import celery
import os

app = celery.Celery('scalingo-sample')


app.conf.update(BROKER_URL=os.environ['live-stream-score-1973.redis.a.osc-fr1.scalingo-dbs.com'],
                CELERY_RESULT_BACKEND=os.environ['live-stream-score-1973.redis.a.osc-fr1.scalingo-dbs.com'])
@app.task
def hello(name):
    return "Hello "+name