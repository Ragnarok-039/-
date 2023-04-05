select bc.bID,
       bc.piID,
       bc.Cost,
       b.BDate,
       b.PayDate,
       pi.product,
       case
           when pi.product like '%Контур%'
               then 'Продукт Контура'
           else pi.product
           end as product_company
from BillsContent as bc
         left join Bills as b on bc.bID = b.bID
         left join PriceItems as pi on bc.piID = pi.piID;
