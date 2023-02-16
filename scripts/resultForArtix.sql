-- Новый скрипт в myDB.sqlite.
-- Дата: 2 дек. 2022 г.
-- Время: 15:58:10
WITH RECURSIVE parents AS (select * from invent
inner JOIN (SELECT *  FROM additionalprices) as st
ON st.additionalpricesid  = invent.inventcode
)
           SELECT *
           FROM parents
           
