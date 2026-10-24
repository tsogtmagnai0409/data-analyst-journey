-- Хичээл 1: Өгөгдөлтэй танилцах
-- Өгөгдлийн сан: data/online_shop.db (SQLite)

-- 1.1 Хүснэгт бүр хэдэн мөртэй вэ?
SELECT COUNT(*) AS row_count FROM orders;       -- 7117
SELECT COUNT(*) AS row_count FROM customers;    -- 608
SELECT COUNT(*) AS row_count FROM products;     -- 40
SELECT COUNT(*) AS row_count FROM order_items;  -- 14241

-- 1.2 Эхний 10 захиалга
SELECT *
FROM orders
LIMIT 10;

-- 1.3 Төлөв тус бүр хэдэн захиалга вэ?
SELECT status, COUNT(*) AS order_count
FROM orders
GROUP BY status
ORDER BY order_count DESC;

-- ===== Давтлагын дасгал (өөрөө бөглө) =====
-- 1) payment_method тус бүр хэд вэ?

-- 2) category тус бүр хэдэн бүтээгдэхүүнтэй вэ?

-- 3) аль channel-аар хамгийн олон хүн бүртгүүлсэн бэ?

