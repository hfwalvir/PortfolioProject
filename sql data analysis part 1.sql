
--  Basic queries -- 
select * from sales
where amount > 10000 and SaleDate >= '2022-01-01';

select SaleDate, Amount from sales
where amount>10000 and year(SaleDate) = 2022
order by amount desc ;

select * from sales
where boxes > 0 and boxes <= 50;

select * from sales 
where boxes between 0 and 50;

select SaleDate, Amount,Boxes, weekday(SaleDate) as 'Day of Week'
from sales 
where weekday(SaleDate)=4;

select * from people
where team = "Delish" or team = "Jucies" ;

select * from people
where team in ('Delish' , 'Jucies') ;

select * from people
where salesperson like '%B%';

select * from people
where salesperson like 'B%';

select * from sales;
select SaleDate , Amount,
	   case     when amount < 1000 THEN 'under 1K'
                when amount < 5000 THEN 'under 5K'
                when amount < 10000 THEN 'under 10K'
              else '10 k or more'
			end as 'Amount category'
from sales;
 

