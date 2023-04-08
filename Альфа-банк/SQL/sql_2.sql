create table oper
(
    date date,
    cnt  int
);
-- insert into #oper values
-- ('2019-06-02',     1985),
-- ('2019-06-03',     1577),
-- ('2019-06-04',     1597),
-- ('2019-06-05',     1468),
-- ('2019-07-06',     82),
-- ('2019-07-08',     1689),
-- ('2019-07-09',     1556),
-- ('2019-07-10',     1480),
-- ('2019-07-11',     1405),
-- ('2019-07-12',     1502)

select date, sum(cnt) over (order by date rows between unbounded preceding and current row) as current_sum
from oper;
