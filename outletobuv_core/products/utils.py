from .models import Product, Color, Size, Material, Category
from time import time
import csv
import os

def time_decor(function):
    def wrapper(*args, **kwargs):
        start_time = time()
        func = function(*args, **kwargs)
        end_time = time()
        print('Время выполнения функции : ', start_time - end_time)
        return func
    return wrapper


@time_decor
def test(file_path):
    with open(file_path, 'r', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f, delimiter=';')
        for row in reader:
            try:
                article = row['Articul']
                name = row['GoodName'].split()[0]
                category = row['GoodTypeFull']
                material_name = row['Material']
                season = row['Season']
                color_name = row['Color']
                price = row['RetailPrice']
                size_value = row['TheSize']
                quantity = row['WarehouseQuantity']

                this_color, _ = Color.objects.get_or_create(name=color_name)
                this_material, _ = Material.objects.get_or_create(name=material_name)
                this_size, _ = Size.objects.get_or_create(value=size_value)

                # print(f'Артикул {articul} Категория {category} Сезон {season} Материал {material} Цвет {color} Размер {size} Цена {price}')
                
                category, created = Category.objects.get_or_create(title=category)
                product, created = Product.objects.get_or_create(
                    article=article,
                    name=name,
                    category=category,
                    season=season,
                    price=price,
                    quantity=quantity
                )
                product.color.add(this_color)
                product.material.add(this_material)
                product.size.add(this_size)
                product.save()

                # existed_size = Size.objects.filter(
                #     product=product,
                #     value=size_value
                # )
                # if not existed_size.exists():
                #     this_size = Size.objects.create(
                #         product=product,
                #         value=size_value
                #     )

                # this_size.color.add(this_color)
                # this_size.material.add(this_material)
                # this_size.save()
            except Exception as e:
                print(f'Произошла ошибка:  {e}')



        # "Articul";"GoodTypeFull";"Category";
        # "WarehouseQuantity";"Material";"GoodName";
        # "PCName";"TheSize";"Season";
        # "PriceDiscountPercent";"Color";"RetailPrice"

# @time_decor
def hide_product(file_path):
    pass
#     counter = 0
#     products = Product.objects.all()
#     for product in products:
#         try:
#             # "(\d+)"\;"([^"]+)"\;(\d+)\;(\d+)\;"([^"]+)"\;"([^"]+)"\;"(\d+)"\;"([^"]*)"\;(\d+)\;"([^"]+)"\;(\d+)

#             product_row = f'"{product.article}";"{product.category}";"[\d];"{product.material}";"{product.name}";product.color, product.size)
#             # "Articul";"GoodTypeFull";"Category";"WarehouseQuantity";"Material";"GoodName";"PCName";"TheSize";"Season";"PriceDiscountPercent";"Color";"RetailPrice"
# #               "9142";"Обувь,БОСОНОЖКИ";72;5;"замш ";"БОСОНОЖКИ бордвые замш 9142 Пекин, Китай 35(р)";"Пекин, Китай";"35";"";50;"бордвые";3990

#             with open(file_path, 'r', encoding='utf-8-sig') as f:
#                 reader = csv.DictReader(f, delimiter=';')
#                 for row in reader:
#                     if product_row in row:
#                         product.is_hidden = True
#                         counter += 1
#                     else:
#                         continue
#         except Exception as e:
#             print(f'Произошла ошибка:  {e}')
#     print(f'Скрыто {counter} продуктов.')
