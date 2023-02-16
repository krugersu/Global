ЕК-00000002
ЦБ-00003451
КН000107

SELECT * FROM invent WHERE isParent IN ('КН000746','КН000107', 'ЦБ-00000526','ЕК-00000002','ЦБ-00003451','ЦБ-00004629','ЦБ-00005124') 


SELECT  FROM NewView 
INNER JOIN
invent ON NewView.isParent = invent.inventcode


SELECT NewView.isParent,NewView.remain, invent.inventcode, invent.remain FROM NewView 
INNER JOIN
invent ON NewView.isParent = invent.inventcode

SELECT NewView.isParent,NewView.remain, invent.inventcode, invent.remain, (NewView.remain + invent.remain) as summItog FROM NewView 
INNER JOIN
invent ON NewView.isParent = invent.inventcode


КН000746	222.5
КН000107	433.0
ЦБ-00003451	40.0


UPDATE invent 
set remain  = sumItog.summItog 
FROM (
SELECT invent.inventcode, (NewView.remain + invent.remain) as summItog FROM NewView 
INNER JOIN
invent ON NewView.isParent = invent.inventcode
) as sumItog
WHERE  invent.inventcode  = sumItog.inventcode