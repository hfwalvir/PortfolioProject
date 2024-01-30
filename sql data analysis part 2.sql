-- For JOINS --
select * from sales;

select * from people;

select s.saleDate, s.amount, p.Salesperson, s.SPID
from sales s
join people p on p.SPID = s.SPID ; 

select s.SaleDate, s.amount, pr.product 
from sales s 
left join products pr on pr.pid = s.pid ;

select s.SaleDate, s.amount, pr.product, p.Salesperson, p.team
from sales s 
join people p on p.SPID = s.SPID
left join products pr on pr.pid = s.pid ;

select s.SaleDate, s.amount, pr.product, p.Salesperson, p.team
from sales s 
join people p on p.SPID = s.SPID
join products pr on pr.pid = s.pid 
join geo g on g.geoid = s.geoid 
where s.amount < 500 
and p.Team = '' 
and g.Geo in ('New Zealand', 'India') 
order by SaleDate ;









