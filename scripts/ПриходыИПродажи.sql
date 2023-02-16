// Собрали продажи по позициям которые пришли из 1С




SELECT * FROM CountSummAnalog 
inner JOIN (SELECT code , opcode ,  SUM(cquant)   FROM goodsitem  
Group by code) as st
ON st.code  = CountSummAnalog.inventcode 


UPDATE invent 
set remain  = sumItog.summItog 
FROM (
SELECT invent.inventcode, (SummIsParent.remain + invent.remain) as summItog FROM SummIsParent 
INNER JOIN
invent ON SummIsParent.isParent = invent.inventcode
) as sumItog
WHERE  invent.inventcode  = sumItog.inventcode