SELECT substr(sales_date, 1, 10) as sales_date, f.PRODUCT_ID, NULL as USER_ID, f.SALES_AMOUNT FROM offline_sale as f
-- # WHERE f.sales_date LIKE "2022-03%"
WHERE f.sales_date >= '2022-03-01' AND f.sales_date < '2022-04-01'
UNION 
SELECT substr(sales_date, 1, 10) as sales_date, o.PRODUCT_ID, o.USER_ID, o.SALES_AMOUNT FROM online_sale as o
-- # WHERE f.sales_date >= '2022-03-01' AND f.sales_date < '2022-04-01'
-- # WHERE o.sales_date LIKE "2022-03%"
WHERE o.sales_date >= '2022-03-01' AND o.sales_date < '2022-04-01'



-- # OUTER JOIN offline_sale AS f 


ORDER BY sales_date, product_id, user_id;