import csv
import io
from celery import shared_task

from products.models import Products
from stock.models import Stock



@shared_task
def processar_csv(arquivo):
    csvfile = io.StringIO(arquivo)
    primeira_linha = csvfile.readline()
    delimitador = ';' if ';' in primeira_linha else ','

    reader = csv.DictReader(csvfile, delimiter=delimitador)
    
    products_to_create = []
    stock_to_create = []

    for row in reader:
        
        try:
            product = Products(
                product_name=row["Nome"],
                product_description=row["Descrição"],
                product_price=float(row["Preço"]),
                product_quantity=int(row["Quantidade Inicial"])
            )
            products_to_create.append(product)

        except KeyError as e:
            print(f"Erro: Coluna {e} não encontrada no CSV. Verifique o cabeçalho.")
            return

    created_products = Products.objects.bulk_create(products_to_create)

    for product in created_products:
        stock_to_create.append(Stock(product=product, quantity=product.product_quantity))

    Stock.objects.bulk_create(stock_to_create)
    
