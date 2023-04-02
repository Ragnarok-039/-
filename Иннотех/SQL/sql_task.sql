/*Диалект - MySQL*/

/*Для начала создаем соответственно две таблицы.*/
create table table_1
(
    item_id     int,
    title       text,
    actual_date datetime
);

create table table_2
(
    item_id     int,
    price       int,
    actual_date datetime
);

/*Выполним необходимый запрос.*/
with temp_1 as (select item_id, title, actual_date
                from (select *, row_number() over (partition by item_id order by actual_date desc) as num
                      from table_1) as t_1
                where num = 1),
     temp_2 as (select item_id, price, actual_date
                from (select *, row_number() over (partition by item_id order by actual_date desc) as num
                      from table_2) as t_2
                where num = 1)
select temp_1.item_id, temp_2.item_id, temp_1.title, temp_2.price, temp_1.actual_date, temp_2.actual_date
from temp_1
         left join temp_2 on temp_1.item_id = temp_2.item_id
union
select temp_1.item_id, temp_2.item_id, temp_1.title, temp_2.price, temp_1.actual_date, temp_2.actual_date
from temp_2
         left join temp_1 on temp_2.item_id = temp_1.item_id;
