create table dbo.events
(
    event_datetime datetime, /*время события , только 2020 год*/
    event_id       int, /*идентификатор события, первичный ключ*/
    user_id        int, /*идентификатор посетителя (один пользователь может несколько раз заходить на сайт, в том числе и в течение дня,*/
    /*в том числе с разных городов) Так же посещения могут быть уже после открытия счета*/
    event_name     varchar(100), /*название события (Посещение сайта или Открытие счета) Для упрощения - счет может открыться только после посещения сайта,*/
    /* и каждый посетитель мождет открыть только один счет*/
    city           varchar(100), /*город*/
    cost           numeric(10, 2) /*расчетная стоимость привлечения посетителя на сайт*/
)

/*1. Вывести количество уникальных посетителей, которые заходили на сайт из разных городов*/
select city, count(distinct user_id)
from dbo.events
group by city;

/*2. Найти город, с максимальным числом уникальных посетителей. Вывести в разрезе каждого месяца*/
with temp_table as (select city, max(num)
                    from (select city, count(distinct user_id) as num from dbo.events group by city) as temp)
select city, count(distinct user_id)
from dbo.events
where city in (select city from temp_table)
group by month(event_datetime);

/*3. Найти среднее количество посещений сайта , потребовавшееся посетителям,
  чтобы принять решение об открытии счета ( результат = одно число, только по посетителям, открывшим счет)*/
with temp_table as (select * from dbo.events where event_name = 'Открытие счета')
select avg(my_num) as avg_visit
from (select count(1), user_id as my_num
      from dbo.events
      where user_id in (select user_id from temp_table)
        and event_name = 'Посещение сайта'
      group by user_id) as my_query;

/*4. Найти среднее число дней , потребовавшееся посетителям, чтобы принять решение об открытии счета
  ( Результат = одно число, только по посетителям, открывшим счет, считаем с первого посещения сайта)*/
with temp_table as (select * from dbo.events where event_name = 'Открытие счета')
select avg(my_num) as avg_day
from (select datediff(max(event_datetime), min(event_datetime)), user_id as my_num
      from dbo.events
      where user_id in (select user_id from temp_table)
        and event_name = 'Посещение сайта'
      group by user_id) as my_query;

/*5. Вывести идентификаторы посетителей, которые открыли счет в день первого посещения сайта*/
with temp_table as (select user_id, min(event_datetime) as min_date from dbo.events)
select user_id
from dbo.events
where event_name = 'Открытие счета'
  and event_datetime in (select min_date from temp_table);
