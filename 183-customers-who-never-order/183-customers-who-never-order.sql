# Write your MySQL query statement below
select A.name as customers from customers A
where Not exists (select 1 from orders B where A.id = B.customerId)