# 📊 Data Analyst Journey — Excel · SQL · Python

Нэг өгөгдөл дээр (Монгол онлайн дэлгүүр, 2024–2025) дата аналистын ур чадварыг **Excel, SQL, Python** гурвуулаар нь ижил даалгавар хийж сурч буй миний бүртгэл.

## Өгөгдөл (`data/`)
| Хүснэгт | Мөр | Агуулга |
|---|---|---|
| customers | 608 | Харилцагч |
| products | 40 | Бүтээгдэхүүн, үнэ, өртөг |
| orders | 7,117 | Захиалга, төлөв, төлбөр |
| order_items | 14,241 | Захиалгын мөр, тоо, хөнгөлөлт |

Нэг өгөгдөл гурван хэлбэртэй: `online_shop.xlsx` (Excel), `online_shop.db` (SQLite), `*.csv` (Python).

## Хичээлүүд
| # | Сэдэв | Excel | SQL | Python | Төлөв |
|---|---|---|---|---|---|
| 01 | [Өгөгдөлтэй танилцах](lessons/01_explore_data/) | COUNTA, COUNTIF | COUNT, GROUP BY | read_csv, value_counts | 🟡 |
| 02 | Шүүх ба эрэмбэлэх | Filter, IF | WHERE, ORDER BY | df[...], sort_values | ⚪ |
| 03 | Өгөгдөл цэвэрлэх | TRIM, Remove Duplicates | DISTINCT, TRIM | drop_duplicates | ⚪ |
| 04 | Нэгтгэх | SUMIFS, Pivot | SUM, AVG, HAVING | groupby, agg | ⚪ |
| 05 | Хүснэгт холбох | XLOOKUP | JOIN | merge | ⚪ |

## Бүтэц
```
data/                     — өгөгдөл
lessons/NN_topic/
    README.md             — хичээлийн тэмдэглэл
    excel/  sql/  python/ — хэрэгсэл бүрийн ажил
notes/                    — ерөнхий тэмдэглэл, логикийн толь
```
