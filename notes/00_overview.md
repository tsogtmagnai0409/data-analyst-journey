# 📊 Дата аналистын сурах бүртгэл

> Нэг өгөгдөл (Монгол онлайн дэлгүүр 2024–2025), гурван хэрэгсэл (Excel · SQL · Python). Хичээл бүрт ижил даалгаврыг гурван хэрэгслээр хийнэ.

## 🗂 Өгөгдлийн бүтэц

| Хүснэгт | Мөр | Агуулга |
|---|---|---|
| customers | 608 | Харилцагч: нэр, хүйс, төрсөн он, хот, бүртгүүлсэн огноо, суваг |
| products | 40 | Бүтээгдэхүүн: ангилал, зарах үнэ, өртөг, гарал |
| orders | 7,117 | Захиалга: огноо, төлөв, төлбөрийн хэлбэр, хүргэлт |
| order_items | 14,241 | Захиалгын мөр: бүтээгдэхүүн, тоо, үнэ, хөнгөлөлт |

```
customers.customer_id ──< orders.customer_id
orders.order_id       ──< order_items.order_id
products.product_id   ──< order_items.product_id
```

## 📅 Хичээлийн явц

| # | Хичээл | Excel | SQL | Python | Төлөв | Огноо |
|---|---|---|---|---|---|---|
| 1 | Өгөгдөлтэй танилцах | COUNTA, COUNTIF | COUNT, GROUP BY | read_csv, value_counts | 🟡 Явж байна | |
| 2 | Шүүх ба эрэмбэлэх | Filter, IF | WHERE, ORDER BY | df[...], sort_values | ⚪ Эхлээгүй | |
| 3 | Өгөгдөл цэвэрлэх | TRIM, Remove Duplicates | DISTINCT, TRIM | drop_duplicates, str.strip | ⚪ Эхлээгүй | |
| 4 | Нэгтгэх (aggregation) | SUMIFS, Pivot | SUM, AVG, HAVING | groupby, agg | ⚪ Эхлээгүй | |
| 5 | Хүснэгт холбох | XLOOKUP | JOIN | merge | ⚪ Эхлээгүй | |

## 🧠 Нийтлэг логикийн толь

| Үйлдэл | Excel | SQL | Python (pandas) |
|---|---|---|---|
| Мөр тоолох | `=COUNTA(A:A)-1` | `SELECT COUNT(*) FROM t;` | `len(df)` |
| Эхний мөрүүд харах | Шууд / `Ctrl+↓` | `SELECT * FROM t LIMIT 10;` | `df.head(10)` |
| Ангилал бүрээр тоолох | `=COUNTIF(D:D, H2)` | `SELECT col, COUNT(*) FROM t GROUP BY col;` | `df["col"].value_counts()` |
