USE customer_intelligence;

WITH rfm AS (
    SELECT
        c.customer_id,
        c.name,

        DATEDIFF(
            (SELECT MAX(order_date) FROM orders),
            MAX(o.order_date)
        ) AS recency,

        COUNT(o.order_id) AS frequency,

        ROUND(SUM(o.total_amount), 2) AS monetary

    FROM customers c

    JOIN orders o
        ON c.customer_id = o.customer_id

    GROUP BY
        c.customer_id,
        c.name
),

rfm_scores AS (
    SELECT
        customer_id,
        name,
        recency,
        frequency,
        monetary,

        -- Lower recency is better
        NTILE(5) OVER (
            ORDER BY recency ASC
        ) AS r_score,

        -- Higher frequency is better
        NTILE(5) OVER (
            ORDER BY frequency ASC
        ) AS f_score,

        -- Higher monetary value is better
        NTILE(5) OVER (
            ORDER BY monetary ASC
        ) AS m_score

    FROM rfm
)

SELECT
    customer_id,
    name,
    recency,
    frequency,
    monetary,
    r_score,
    f_score,
    m_score,

    CONCAT(r_score, f_score, m_score) AS rfm_score,

    CASE

        WHEN r_score >= 4
             AND f_score >= 4
             AND m_score >= 4
            THEN 'Champions'

        WHEN r_score >= 3
             AND f_score >= 4
            THEN 'Loyal Customers'

        WHEN r_score >= 4
             AND f_score <= 2
            THEN 'New Customers'

        WHEN r_score <= 2
             AND f_score >= 3
            THEN 'At Risk'

        WHEN r_score <= 2
             AND f_score <= 2
            THEN 'Lost Customers'

        ELSE 'Potential Loyalists'

    END AS segment

FROM rfm_scores

ORDER BY monetary DESC;