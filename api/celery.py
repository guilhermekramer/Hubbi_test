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
    from products.models import Products
    from django.db.models import F


    low_stock_products = Products.objects.filter(product_quantity__lt=10)
    
    for stock in low_stock_products:
        stock.product_quantity = F('product_quantity') + 10
        stock.save()
        print(f"Product {stock} has low stock. Updating product quantity.")


