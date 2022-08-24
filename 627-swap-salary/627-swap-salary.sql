# Write your MySQL query statement below
 update salary set sex = CHAR(ASCII('f')^ ASCII('m')^ ASCII(sex));
# update salary set sex = (CASE when sex = 'm' then 'f' else 'm' end)
# update salary set sex = if (sex = 'f','m','f');