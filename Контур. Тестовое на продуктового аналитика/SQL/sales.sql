select bc.bID, bc.piID, bc.Cost, b.BDate, b.PayDate, pi.product, pi.piName
from BillsContent as bc
         left join Bills as b on bc.bID = b.bID
         left join PriceItems as pi on bc.piID = pi.piID
where pi.product = 'Бухгалтерия.Контур';
