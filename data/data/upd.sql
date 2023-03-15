UPDATE invent 
set remain  = sumItog.summItog 
FROM (
SELECT invent.inventcode, (SummIsParent.remain + invent.remain) as summItog FROM SummIsParent 
INNER JOIN
invent ON SummIsParent.isParent = invent.inventcode
) as sumItog
WHERE  invent.inventcode  = sumItog.inventcode