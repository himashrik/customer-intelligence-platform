USE customer_intelligence;

-- =====================================================
-- 1. OVERALL BUSINESS KPIs
-- =====================================================

SELECT
    COUNT(DISTINCT customer_id) AS total_customers,
    COUNT(*) AS total_orders,
    ROUND(SUM(total_amount), 2) AS total_revenue,
    ROUND(AVG(total_amount), 2) AS average_order_value
FROM orders;


-- =====================================================
-- 2. MONTHLY REVENUE
-- =====================================================

SELECT
    DATE_FORMAT(order_date, '%Y-%m') AS month,
    COUNT(*) AS orders,
    ROUND(SUM(total_amount), 2) AS revenue
FROM orders
GROUP BY DATE_FORMAT(order_date, '%Y-%m')
ORDER BY month;


-- =====================================================
-- 3. TOP 10 CUSTOMERS BY REVENUE
-- =====================================================

SELECT
    c.customer_id,
    c.name,
    c.country,
    COUNT(o.order_id) AS total_orders,
    ROUND(SUM(o.total_amount), 2) AS total_spent
FROM customers c
JOIN orders o
    ON c.customer_id = o.customer_id
GROUP BY
    c.customer_id,
    c.name,
    c.country
ORDER BY total_spent DESC
LIMIT 10;


-- =====================================================
-- 4. TOP 10 PRODUCTS
-- =====================================================

SELECT
    p.product_id,
    p.product_name,
    p.category,
    SUM(oi.quantity) AS units_sold,
    ROUND(
        SUM(oi.quantity * oi.unit_price),
        2
    ) AS revenue
FROM products p
JOIN order_items oi
    ON p.product_id = oi.product_id
GROUP BY
    p.product_id,
    p.product_name,
    p.category
ORDER BY revenue DESC
LIMIT 10;


-- =====================================================
-- 5. REVENUE BY CATEGORY
-- =====================================================

SELECT
    p.category,
    SUM(oi.quantity) AS units_sold,
    ROUND(
        SUM(oi.quantity * oi.unit_price),
        2
    ) AS revenue
FROM products p
JOIN order_items oi
    ON p.product_id = oi.product_id
GROUP BY p.category
ORDER BY revenue DESC;


-- =====================================================
-- 6. COUNTRY-WISE PERFORMANCE
-- =====================================================

SELECT
    c.country,
    COUNT(DISTINCT c.customer_id) AS customers,
    COUNT(o.order_id) AS orders,
    ROUND(SUM(o.total_amount), 2) AS revenue
FROM customers c
JOIN orders o
    ON c.customer_id = o.customer_id
GROUP BY c.country
ORDER BY revenue DESC;


-- =====================================================
-- 7. REPEAT CUSTOMERS
-- =====================================================

SELECT
    c.customer_id,
    c.name,
    COUNT(o.order_id) AS order_count,
    ROUND(SUM(o.total_amount), 2) AS total_spent
FROM customers c
JOIN orders o
    ON c.customer_id = o.customer_id
GROUP BY
    c.customer_id,
    c.name
HAVING COUNT(o.order_id) > 1
ORDER BY order_count DESC;


-- =====================================================
-- 8. NEW VS RETURNING CUSTOMERS
-- =====================================================

SELECT
    CASE
        WHEN order_count = 1 THEN 'One-Time Customer'
        ELSE 'Returning Customer'
    END AS customer_type,
    COUNT(*) AS customers
FROM (
    SELECT
        customer_id,
        COUNT(*) AS order_count
    FROM orders
    GROUP BY customer_id
) customer_orders
GROUP BY customer_type;


-- =====================================================
-- 9. ORDERS BY DAY OF WEEK
-- =====================================================

SELECT
    DAYNAME(order_date) AS day_of_week,
    COUNT(*) AS total_orders,
    ROUND(SUM(total_amount), 2) AS revenue
FROM orders
GROUP BY DAYOFWEEK(order_date), DAYNAME(order_date)
ORDER BY DAYOFWEEK(order_date);


-- =====================================================
-- 10. ORDERS BY HOUR
-- =====================================================

SELECT
    HOUR(order_date) AS order_hour,
    COUNT(*) AS total_orders,
    ROUND(SUM(total_amount), 2) AS revenue
FROM orders
GROUP BY HOUR(order_date)
ORDER BY order_hour;


-- =====================================================
-- 11. CUSTOMER PURCHASE FREQUENCY
-- =====================================================

SELECT
    customer_id,
    COUNT(order_id) AS total_orders,
    ROUND(AVG(total_amount), 2) AS average_order_value,
    ROUND(SUM(total_amount), 2) AS lifetime_value
FROM orders
GROUP BY customer_id
ORDER BY lifetime_value DESC;


-- =====================================================
-- 12. LOW-PERFORMING PRODUCTS
-- =====================================================

SELECT
    p.product_id,
    p.product_name,
    p.category,
    COALESCE(SUM(oi.quantity), 0) AS units_sold,
    COALESCE(
        ROUND(SUM(oi.quantity * oi.unit_price), 2),
        0
    ) AS revenue
FROM products p
LEFT JOIN order_items oi
    ON p.product_id = oi.product_id
GROUP BY
    p.product_id,
    p.product_name,
    p.category
ORDER BY units_sold ASC;