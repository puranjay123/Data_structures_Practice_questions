# Write your MySQL query statement below
# Approach 1
# select A.name as customers from customers A
# where Not exists (select 1 from orders B where A.id = B.customerId)
# approach2

select A.name as customers from customers A
left join orders B  on A.id = B.customerId
where B.customerId is  NULL