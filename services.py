from apscheduler.schedulers.background import BackgroundScheduler
from mailing.views import send_mailings


def setup_scheduler_one_day():
    scheduler = BackgroundScheduler()
    scheduler.add_job(send_mailings, 'interval', days=1)
    scheduler.start()

def setup_scheduler_one_week():
    scheduler = BackgroundScheduler()
    scheduler.add_job(send_mailings, 'interval', days=7)
    scheduler.start()

def setup_scheduler_one_month():
    scheduler = BackgroundScheduler()
    scheduler.add_job(send_mailings, 'interval', days=30)
    scheduler.start()
