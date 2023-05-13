SELECT a.author_id, a.author_name, b.category, 
sum(s.sales*b.price) as total_sales FROM book_sales as s
JOIN book as b on b.book_id = s.book_id
join author as a on a.author_id = b.author_id

WHERE s.sales_date >= '2022-01-01' and s.sales_date <= '2022-01-31'

GROUP BY a.author_name, b.category

ORDER BY a.author_id ASC, b.category DESC