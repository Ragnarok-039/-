create table segment
(
    [date]    date,
    ClientID  varchar(6),
    SegmentID int
);
-- insert into #segment values
-- ('2018-01-31' ,'A11111', 2),
-- ('2018-02-28' ,'A11111', 2),
-- ('2018-03-31' ,'A11111', 1),
-- ('2018-04-30' ,'A11111', 1),
-- ('2017-11-30' ,'B22222', 1),
-- ('2017-10-31' ,'B22222', 1),
-- ('2017-09-30' ,'B22222', 3),
-- ('2017-09-30' ,'C33333', 1),
-- ('2017-10-31' ,'C33333', 1)

select ClientID, SegmentID, max(date) - min(date) as duration
from segment
group by ClientID, SegmentID;
