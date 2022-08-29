# Write your MySQL query statement below
# select(select author_id,viewer_id  from views
# where (distinct(author_id=viewer_id))
# order by author_id asc) as id
select distinct author_id as id from views where author_id= viewer_id order by id