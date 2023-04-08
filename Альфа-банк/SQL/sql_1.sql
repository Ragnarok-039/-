create table clients
(
    client_id   varchar(1),
    FIO         varchar(255),
    Region      varchar(50),
    account_num int
);
-- insert into #Клиенты values
-- ('A','Иванов','Москва',111),
-- ('A','Иванов','Москва',222),
-- ('B','Петров','Иваново',333),
-- ('C','Сидоров','Москва',444)

create table bills
(
    [Date]      date,
    Summa_USD   money,
    Account_num int
);
-- insert into #Cчета values
-- ('2012-01-01',15000,111),
-- ('2012-02-01',10000,111),
-- ('2012-02-01',5000,222),
-- ('2012-03-01',30000,333),
-- ('2012-04-01',20000,444)

with temp_bills as (select Date,
                           Summa_USD,
                           Account_num,
                           row_number() over (partition by Account_num, Date order by Date desc) as num
                    from bills
                    where Summa_USD >= 20000)

select *
from clients
where Region = 'Москва'
  and clients.account_num in (select account_num from temp_bills where temp_bills.num = 1);
