"""Хичээл 1: Өгөгдөлтэй танилцах
Ажиллуулах: repo-гийн үндсэн хавтаснаас `python lessons/01_explore_data/python/lesson01.py`
"""
import pandas as pd

DATA = "data/"
customers = pd.read_csv(DATA + "customers.csv")
products = pd.read_csv(DATA + "products.csv")
orders = pd.read_csv(DATA + "orders.csv")
order_items = pd.read_csv(DATA + "order_items.csv")

# 1.1 Хүснэгт бүр хэдэн мөртэй вэ?
for name, df in [("customers", customers), ("products", products),
                 ("orders", orders), ("order_items", order_items)]:
    print(name, df.shape)

# 1.2 Эхний 10 захиалга
print(orders.head(10))

# 1.3 Төлөв тус бүр хэдэн захиалга вэ?
print(orders["status"].value_counts())

# ===== Давтлагын дасгал (өөрөө бөглө) =====
# 1) payment_method тус бүр хэд вэ?

# 2) category тус бүр хэдэн бүтээгдэхүүнтэй вэ?

# 3) аль channel-аар хамгийн олон хүн бүртгүүлсэн бэ?
