# Write your MySQL query statement below
# rretunr th e na,em,population,area with big countires

# select name,population,area
# from world
# where area>3000000 OR population >25000000
SELECT name, population, area
FROM World
WHERE area >= 3000000 OR population >= 25000000