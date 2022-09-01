# Write your MySQL query statement below
select s.product_id,product_name from sales s left join product p on p.product_id = s.product_id group by s.product_id 
HAVING MIN(sale_date) >= '2019-01-01' AND MAX(sale_date) <= '2019-03-31' 
