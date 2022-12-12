/*Диалект - MySQL*/

create table Users
(
    userId int,
    age    int
);

create table Purchases
(
    purchaseId int,
    userId     int,
    itemId     int,
    date       date
);

create table Items
(
    itemId int,
    price  int
);


/*А*/
select avg(i.price)
from Items as i
         left join Purchases as p on i.itemid = p.itemid
         left join Users as u on u.userId = p.userId
where u.age between 18 and 25;

select avg(i.price)
from Items as i
         left join Purchases as p on i.itemid = p.itemid
         left join Users as u on u.userId = p.userId
where u.age between 26 and 35;

/*Б*/
select temp.my_month, max(temp.my_sum)
from (select sum(i.price) as my_sum, month(p.date) as my_month
      from Items as i
               left join Purchases as p on i.itemid = p.itemid
               left join Users as u on u.userId = p.userId
      where u.age >= 35
      group by month(p.date)) as temp;

/*В*/
select temp.product, max(temp.my_sum)
from (select p.purchaseId as product, sum(i.price) as my_sum
      from Items as i
               left join Purchases as p on i.itemid = p.itemid
      where year(p.date) = year(curdate())
      group by p.purchaseId) as temp;

/*Г*/
select temp.product, temp.my_sum / sum(temp.my_sum) * 100 as '%'
from (select p.purchaseId as product, sum(i.price) as my_sum
      from Items as i
               left join Purchases as p on i.itemid = p.itemid
      where year(p.date) = year(curdate())
      group by p.purchaseId
      order by my_sum desc) as temp
limit 3;
