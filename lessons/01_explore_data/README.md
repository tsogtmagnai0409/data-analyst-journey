# 📘 Хичээл 1: Өгөгдөлтэй танилцах

**Төлөв:** 🟡 Явж байна  
**Гол санаа:** Шинжлэхээсээ өмнө өгөгдлөө тань: хэдэн мөр, ямар багана, ямар утгатай вэ.

---

## 1.1 Хүснэгт бүр хэдэн мөртэй вэ?

**Excel**
```
=COUNTA(orders!A:A)-1
```
- `COUNTA` → хоосон биш нүдийг тоолно
- `orders!A:A` → orders sheet-ийн A баганыг бүхэлд нь
- `-1` → гарчгийн мөрийг хасна

**SQL**
```sql
SELECT COUNT(*) FROM orders;
```

**Python**
```python
import pandas as pd
orders = pd.read_csv("orders.csv")
len(orders)      # эсвэл orders.shape → (мөр, багана)
```

✅ Хариу: orders = **7,117** · customers = 608 · products = 40 · order_items = 14,241

---

## 1.2 Эхний 10 мөрийг харах

**Excel:** `Ctrl+↓` / `Ctrl+↑` үсрэх, `Ctrl+T` → Table болгох

**SQL**
```sql
SELECT * FROM orders LIMIT 10;
```

**Python**
```python
orders.head(10)
```

---

## 1.3 Төлөв тус бүр хэдэн захиалга вэ?

**Excel**
```
=COUNTIF(orders!D:D, H2)
```
- `COUNTIF(хаана, юуг)` → D баганаас H2-тэй тэнцүү утгыг тоолно

**SQL**
```sql
SELECT status, COUNT(*) AS order_count
FROM orders
GROUP BY status
ORDER BY order_count DESC;
```
- `GROUP BY` → бүлэглэх · `AS` → нэр өгөх · `DESC` → ихээс бага руу

**Python**
```python
orders["status"].value_counts()
```

✅ Хариу: Хүргэгдсэн **6,259** · Цуцлагдсан **495** · Буцаагдсан **363**

---

## 🔁 Давтлагын дасгал

- [ ] `orders`: төлбөрийн хэлбэр (`payment_method`) тус бүр хэд вэ? (Excel / SQL / Python)
- [ ] `products`: ангилал (`category`) тус бүр хэдэн бүтээгдэхүүнтэй вэ? (Excel / SQL / Python)
- [ ] `customers`: аль сувгаар (`channel`) хамгийн олон хүн бүртгүүлсэн бэ? (Excel / SQL / Python)

**Миний хариу:**  

---

## 📝 Миний тэмдэглэл

**Юу сурсан бэ?**  

**Хаана гацсан бэ / ямар алдаа гаргасан бэ?**  

**Гурван хэрэгслийн ялгаа, адил тал юу байсан бэ?**  
