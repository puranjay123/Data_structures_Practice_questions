select user_id as buyer_id,join_date,count(buyer_id) as orders_in_2019
from users u 
left join orders o on u.user_id = o.buyer_id and year(order_date) = '2019'
group by user_id
order by user_id
