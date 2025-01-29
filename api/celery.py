from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "api.settings")

app = Celery("api")

app.config_from_object("django.conf:settings", namespace="CELERY")

app.autodiscover_tasks()

app.conf.beat_schedule = {
    'check-product-stock-every-20-minutes': {
        'task': 'api.celery.check_product_stock',
        'schedule': crontab(minute='*/1'),
    },
}

@app.task
def check_product_stock():

    from stock.models import Stock

    print("rodando a task")
    low_stock_products = Stock.objects.filter(quantity__lt=10)
    for stock in low_stock_products:
        product_in_stock = stock.product.product_name
        print(f"Product {product_in_stock} is running low on stock")
