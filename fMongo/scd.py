"""from apscheduler.schedulers.blocking import BlockingScheduler
import datetime
import time

def prok(a):
    print(a)
    sched.shutdown(wait=False)
    #sched.remove_job('my_job_id')

sched = BlockingScheduler(timezone="UTC")
run_at = datetime.datetime.utcnow() + datetime.timedelta(seconds=2)
#time.sleep(10)
sched.add_job(prok, 'date', run_date=run_at,args=[9])
sched.start()
print(5)"""

"""

from apscheduler.schedulers.background import BlockingScheduler

count = 0

def job_function():
    print ("job executing")
    global count, scheduler

    # Execute the job till the count of 5 
    count = count + 1
    if count == 5:
        #scheduler.remove_job('my_job_id')
        scheduler.shutdown(wait=False)



scheduler = BlockingScheduler()
scheduler.add_job(job_function, 'interval', seconds=1, id='my_job_id')


scheduler.start()"""

import asyncio

async def nested():
    return 42

async def main():
    # Schedule nested() to run soon concurrently
    # with "main()".
    task = asyncio.create_task(nested())

    # "task" can now be used to cancel "nested()", or
    # can simply be awaited to wait until it is complete:
    await task

asyncio.run(main())