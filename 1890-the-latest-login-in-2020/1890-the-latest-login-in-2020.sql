# # Write your MySQL query statement below
# select distinct(user_id) ,time_stamp as last_stamp
# from logins
# where time_stamp>='2020-01-01 00:00:00' and time_stamp<='2020-12-31 23:59:59'
# order by user_id
select user_id,max(time_stamp) as last_stamp 
from logins where time_stamp like '2020%'
group by user_id