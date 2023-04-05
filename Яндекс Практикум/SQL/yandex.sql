with temp_table as (select flt.user_id, 
                    flt.lesson_id,
                    flt.id,
                    flt.date_created,
                    lit.profession_name,
                    lit.profession_id,
                    lit.lesson_name,
                    row_number() over(partition by flt.user_id order by flt.date_created) as num
                     from finished_lesson_test as flt 
                     left join lesson_index_test as lit 
                     on flt.lesson_id = lit.lesson_id 
                     where lit.profession_name = 'data-analyst'),
users as (select user_id from temp_table as tt
          where tt.num = 1 
          and extract (month from tt.date_created) = 4 
          and extract (year from tt.date_created) = 2020)

select total.diff as delta_seconds,
total.date_created as lesson_datetime,
total.lesson_id,
total.next_time as next_lesson_datetime,
total.profession_name,
total.user_id
from
(select *, extract(epoch from temp.next_time - temp.date_created) as diff from
(select *, lead(tt.date_created) over (partition by tt.user_id order by tt.date_created) as next_time
from temp_table as tt
where tt.user_id in (select user_id from users) 
and extract(year from tt.date_created) >= 2020 
and extract(month from tt.date_created) >= 4 
order by tt.user_id, tt.date_created) as temp) as total
where total.diff <= 5;
