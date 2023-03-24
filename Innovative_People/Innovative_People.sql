/*Диалект - MySQL*/

/*Для начала создаем соответственно три таблицы.*/
create table SELL_1
(
    Date       date,
    PKod       int,
    Pquantity  float,
    Sale_Price float
);

create table Category
(
    PKod   int,
    Pgroup text
);

create table Average_Buy_price
(
    P_Code    int,
    Buy_price float
);


/*1. В какой день продано больше всего товаров*/
with temp_table as (select count(1) as quantity_of_goods, SELL_1.Date as sell_date
                    from SELL_1
                    group by SELL_1.Date)
select sell_date
from temp_table
where quantity_of_goods in (select max(quantity_of_goods) from temp_table);

/*2. В какой месяц продавалось меньше всего сладостей (категория SWEETS)?*/
with temp_table as (select SELL_1.PKod, SELL_1.Date as sell_date, Category.Pgroup
                    from SELL_1
                             left join Category on SELL_1.PKod = Category.PKod
                    where Category.Pgroup = 'SWEETS')
select month_sell
from (select count(1) as quantity_of_goods, month(sell_date) as month_sell
      from temp_table
      group by month(sell_date)) as total
where quantity_of_goods in (select min(quantity_of_goods));

/*3. Какой товар (его ID) принес нам больше всего денег? (Сумма всех заработанных c товара денег - сумма закупки)*/
with profit as
         (select PKod, sum(total_price) as sum_price_goods
          from (select PKod, Pquantity * Sale_Price as total_price
                from SELL_1) as temp_table
          group by PKod),
     consumption as (select sell_pkod.PKod, sell_pkod.count_pkod * Average_Buy_price.Buy_price as total_cost
                     from ((select PKod, sum(Pquantity) as count_pkod
                            from SELL_1
                            group by PKod) as sell_pkod
                         left join Average_Buy_price on sell_pkod.PKod = Average_Buy_price.P_Code)),
     cost_difference as (select profit.PKod, profit.sum_price_goods - consumption.total_cost as cost_difference
                         from profit
                                  left join consumption on profit.PKod = consumption.PKod)
select PKod
from cost_difference
where cost_difference.cost_difference in (select max(cost_difference) from cost_difference);

/*4. Посчитать среднюю маржу (отношение цены продажи к цене закупки) по всем категориями.
  Если следовать этому определению - 'маржу (отношение цены продажи к цене закупки)', то код ниже.
  Но я не совсем уверен в корректности определения маржи таким образом.
  По крайней мере, гугл говорит другое, но готов обсудить этот момент.*/
with sell_price as (select PKod, Pquantity, Pquantity * Sale_Price as total_price
                    from SELL_1),
     avg_sell_price as (select PKod, sum(total_price) / sum(Pquantity) as avg_sell_price from sell_price group by PKod)
select avg_buy_price.P_Code,
       if(avg_sell_price.avg_sell_price / avg_buy_price.Buy_price is null, 'no_sales',
          avg_sell_price.avg_sell_price / avg_buy_price.Buy_price) as margin
from Average_Buy_price as avg_buy_price
         left join avg_sell_price on avg_buy_price.P_Code = avg_sell_price.PKod
order by avg_buy_price.P_Code;
