# Write your MySQL query statement below

# select w1.id from weather w1,weather w2
# where w1.temperature > w2.temperature 
# and TO_DAYS(w1.DATE)-TO_DAYS(w2.DATE)=1;
SELECT wt1.Id 
FROM Weather wt1, Weather wt2
WHERE wt1.Temperature > wt2.Temperature AND 
TO_DAYS(wt1.recordDATE)-TO_DAYS(wt2.recordDATE)=1;

