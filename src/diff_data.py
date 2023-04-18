
curVal = ''
addinvent = ''

# заполнить таблицу иначе она пустая и некоторые сложности при добавлении записи, поом переделать
qrAddOptions = '''insert into optionsa  (inventitemoptions,priceoptions,quantityoptions, remainsoptions)
                    SELECT inventcode,inventcode, inventcode, inventcode FROM invent'''

qrAddPriceoptions = '''INSERT INTO priceoptions (priceoptionsid, enablepricemanual, requirepricemanual, requireselectprice, requiredeferredprice,enableexcisemarkprice)
                    VALUES 
                    (:priceoptionsid, :enablepricemanual, :requirepricemanual, :requireselectprice, :requiredeferredprice, :enableexcisemarkprice);'''

qrAddinventitemoptions = '''INSERT INTO inventitemoptions (inventitemoptionsid, disablebackinsale, disableinventshow, disableinventsale, disableinventback, requiredepartmentmanual,
                                    enabledepartmentmanual, enablebarcodemanual, enablebarcodescanner, visualverify, ageverify, requiresalerestrict, egaisverify, 
                                    prepackaged, nopdfegaisverify, alcoset, freesale, rfidverify, lowweight, weightcontrolbypass, tobacco, shoes, fuzzyweight, 
                                    ignoremarking, markdownverify)
                                    VALUES 
                                    (:inventitemoptionsid,:disablebackinsale, :disableinventshow, :disableinventsale, :disableinventback, :requiredepartmentmanual, 
                                    :enabledepartmentmanual, :enablebarcodemanual, :enablebarcodescanner, :visualverify, :ageverify, :requiresalerestrict, :egaisverify, 
                                    :prepackaged, :nopdfegaisverify, :alcoset, :freesale, :rfidverify, :lowweight, :weightcontrolbypass, :tobacco, :shoes, :fuzzyweight, 
                                    :ignoremarking, :markdownverify);'''
                                    
qrAddquantityoptions = '''INSERT INTO quantityoptions (quantityoptionsid, enabledefaultquantity, enablequantitylimit, quantitylimit, enablequantityscales, enablequantitybarcode,
                                    enablequantitymanual, requirequantitymanual, requirequantitybarcode, requirequantityscales, enabledocumentquantitylimit, autogetquantityfromscales,
                                    documentquantlimit)
                                    VALUES (:quantityoptionsid, :enabledefaultquantity, :enablequantitylimit, :quantitylimit, :enablequantityscales, :enablequantitybarcode, 
                                    :enablequantitymanual, :requirequantitymanual, :requirequantitybarcode, :requirequantityscales, :enabledocumentquantitylimit, 
                                    :autogetquantityfromscales, :documentquantlimit) ;'''

qrAddadditionalprices = 'INSERT INTO additionalprices (additionalpricesid, pricecode, price, name) VALUES (:additionalpricesid, :pricecode, :price, :name);'

# qrAddBarcodes = '''INSERT INTO barcodes (barcodesid, additionalpricesid, aspectvaluesetcode, barcode, cquant, measurecode,
#                             minprice, name, packingmeasure, packingprice, price, quantdefault, minretailprice, customsdeclarationnumber, tmctype, ntin)
#                             VALUES
#                             (:barcodesid, :additionalprices, :aspectvaluesetcode, :barcode, :cquant, :measurecode,
#                             :minprice, :name, :packingmeasure, :packingprice, :price, :quantdefault, :minretailprice, :customsdeclarationnumber, :tmctype, :ntin );'''

qrAddBarcodes = '''INSERT INTO barcodes (barcodesid, additionalpricesid, aspectvaluesetcode, barcode, cquant, measurecode,
                                name, packingmeasure, packingprice, quantdefault, minretailprice, customsdeclarationnumber, tmctype, ntin)
                            VALUES
                            (:barcodesid, :additionalprices, :aspectvaluesetcode, :barcode, :cquant, :measurecode,
                                :name, :packingmeasure, :packingprice, :quantdefault, :minretailprice, :customsdeclarationnumber, :tmctype, :ntin );'''



qrAddSellrestrictperiods = '''INSERT INTO sellrestrictperiods (sellrestrictperiodsid, dateend, datestart, dayend, daystart, timeend,
                            timestart)
                            VALUES
                            (:sellrestrictperiodsid, :dateend, :datestart, :dayend, :daystart, :timeend,
                            :timestart);'''

qrAddPriceoptions = '''INSERT INTO priceoptions (priceoptionsid, enablepricemanual, requirepricemanual, requireselectprice, requiredeferredprice,enableexcisemarkprice)
                    VALUES 
                    (:priceoptionsid, :enablepricemanual, :requirepricemanual, :requireselectprice, :requiredeferredprice, :enableexcisemarkprice);'''




# qrAddinvent = '''INSERT INTO invent (inventcode, inventgroup, name, barcode, barcodes, price, minprice, additionalprices, options, 
#                                 sellrestrictperiods, extendedoptions, discautoscheme, deptcode, taxgroupcode, measurecode, remain, remaindate, articul,
#                                 defaultquantity, taramode, taracapacity, aspectschemecode, aspectvaluesetcode, aspectusecase, aspectselectionrule, age, 
#                                 alcoholpercent, cquant, inn, kpp, alctypecode, paymentobject, manufacturercountrycode, opmode, loyaltymode, minretailprice, 
#                                 isParent, Parent)
#                                 VALUES
#                                 (:inventcode,:inventgroup,:name,:barcode,:barcodes,:price,:minprice,:additionalprices,:options,:sellrestrictperiods,
#                                 :extendedoptions,:discautoscheme,:deptcode,:taxgroupcode,:measurecode,:remain,:remaindate,:articul,:defaultquantity,
#                                 :taramode,:taracapacity,:aspectschemecode,:aspectvaluesetcode,:aspectusecase,:aspectselectionrule,:age,:alcoholpercent,
#                                 :cquant,:inn,:kpp,:alctypecode,:paymentobject,:manufacturercountrycode,:opmode,:loyaltymode,:minretailprice,:isParent,:Parent);'''


qrAddinvent = '''INSERT INTO invent (inventcode,  name,  barcodes, price, minprice, additionalprices, options, 
                                sellrestrictperiods, extendedoptions, discautoscheme, deptcode, taxgroupcode, measurecode, remain, remaindate, articul,
                                defaultquantity, taramode, taracapacity,  aspectusecase, aspectselectionrule, age, 
                                alcoholpercent, cquant, inn, kpp, alctypecode, paymentobject, manufacturercountrycode, opmode, loyaltymode, minretailprice, 
                                isParent, Parent)
                                VALUES
                                (:inventcode,:name,:barcodes,:price,:minprice,:additionalprices,:options,:sellrestrictperiods,
                                :extendedoptions,:discautoscheme,:deptcode,:taxgroupcode,:measurecode,:remain,:remaindate,:articul,:defaultquantity,
                                :taramode,:taracapacity,:aspectusecase,:aspectselectionrule,:age,:alcoholpercent,
                                :cquant,:inn,:kpp,:alctypecode,:paymentobject,:manufacturercountrycode,:opmode,:loyaltymode,:minretailprice,:isParent,:Parent);'''


qrSelectSales = 'SELECT goodsitemid, documentid, ttime, opcode,  cquant, code From goodsitem'
#qrSimpleSelectSale =  'SELECT code, opcode,  CAST(cquant AS CHAR) AS cquant  From goodsitem'
# qrSimpleSelectSale =  '''select
# 	code,
# 	opcode,
# 	cast(cquant as char) as cquant
# from
# 	goodsitem
# where
# 	documentid in (
# 	select
# 		documentid
# 	from
# 		document
# 	where
# 		cashcode = %s
# 		and workshiftid > %s)'''

# qrSimpleSelectSale =  '''select
# 	code,
# 	opcode,
# 	cast(cquant as char) as cquant
# from
# 	goodsitem
# where
# 	documentid in (
# 	select
# 		documentid
# 	from
# 		document
# 	where
# 		cashcode = %s
# 		and workshiftid > (
# 		SELECT 
#           workshiftid 
# 		from
# 			workshift
# 		where
# 			shiftnum = %s
# 			AND time_beg > '2023-01-21 15:47:15') )'''

qrSimpleSelectSale =  '''select
	code,
	opcode,
	cast(cquant as char) as cquant
from
	goodsitem
where
	documentid in (
	select
		documentid
	from
		document
	where
		cashcode = %s
		and workshiftid > (
		SELECT MAX(workshiftid) 
		from
			workshift
		where
			shiftnum = %s
			AND time_beg > '2023-01-21 15:47:15') )'''


qrGetNumWorkshift = 'SELECT workshiftid  from workshift where shiftnum = %s AND time_beg > "2023-01-21 15:47:15"'
  
qrSelectBarcodes = 'SELECT * FROM barcodes where barcodesid = ?'


qrCalculatingTheAmount = '''UPDATE invent 
set remain  = sumItog.summItog 
FROM (
SELECT invent.inventcode, (SummIsParent.remain + invent.remain) as summItog FROM SummIsParent 
INNER JOIN
invent ON SummIsParent.isParent = invent.inventcode
) as sumItog
WHERE  invent.inventcode  = sumItog.inventcode'''


# Work file

header = "### data begin ###"
footer = "### data end ###"
separator = "---"
#addInventItem = str({"command": "addInventItem" }) # Команда addInventItem добавляет товар в справочник товаров. 
clearInventory = {"command":"clearInventory"} # Команда clearInventory очищает справочник товаров со всеми зависимыми записями. 
clearTmcScale = {"command":"clearTmcScale"}  # Команда clearTmcScale очищает справочник товаров для прогрузки на весы
addInventItem = {"command":"addInventItem"}  # Команда addInventItem добавляет товар в справочник товаров. Атрибуты товара задаются обязательным параметром invent.  
clearAspectValueSet  = {"command": "clearAspectValueSet"} #Команда clearAspectValueSet очищает справочник значений разрезов



# Запросы для формирования файла

qrAdditionalprices = '''SELECT pricecode, price, name FROM additionalprices where additionalpricesid = ?'''
qrBarcodes = '''SELECT aspectvaluesetcode, barcode, cquant, measurecode,
                            minprice, name, packingmeasure, packingprice, price, quantdefault, minretailprice, customsdeclarationnumber, tmctype, ntin 
                            FROM barcodes where barcodesid = ?'''
                            
qrsellrestrictperiods = '''SELECT dateend, datestart, dayend, daystart, timeend, timestart
                            FROM sellrestrictperiods where sellrestrictperiodsid = ?'''
qrinventitemoptions = '''SELECT disablebackinsale, disableinventshow, disableinventsale, disableinventback, requiredepartmentmanual,
                                    enabledepartmentmanual, enablebarcodemanual, enablebarcodescanner, visualverify, ageverify, requiresalerestrict, egaisverify, 
                                    prepackaged, nopdfegaisverify, alcoset, freesale, rfidverify, lowweight, weightcontrolbypass, tobacco, shoes, fuzzyweight, 
                                    ignoremarking, markdownverify
                                    FROM inventitemoptions where inventitemoptionsid = ?'''

qrpriceoptions =  '''SELECT enablepricemanual, requirepricemanual, requireselectprice, requiredeferredprice,enableexcisemarkprice
                        FROM priceoptions where priceoptionsid = ?'''                           

qrquantityoptions = '''SELECT enabledefaultquantity, enablequantitylimit, quantitylimit, enablequantityscales, enablequantitybarcode,
                                    enablequantitymanual, requirequantitymanual, requirequantitybarcode, requirequantityscales, enabledocumentquantitylimit, autogetquantityfromscales,
                                    documentquantlimit
                        FROM quantityoptions where quantityoptionsid = ?'''

qrremainsoptions = '''SELECT * FROM remainsoptions where remainsoptionsid = ?'''


# ************************************************* 

qrSelect_last_workshift_date = 'SELECT MAX(workshiftid) AS "MaxDate" FROM workshift Where time_end IS NOT NULL '

#qrSelect_workshift_open = 'SELECT shiftnum ,cashcode,CAST(time_beg AS char),shopcode  FROM workshift WHERE time_end IS NULL AND time_beg >%s  '
#qrSelect_last_workshift_date_open = 'SELECT MAX(time_beg) AS "MaxDate" FROM workshift Where time_end IS NULL'
qrSelect_last_workshift_date_open = 'SELECT MAX(workshiftid) AS "MaxDate" FROM workshift Where time_end IS NULL'

#qrSelect_workshift_open = 'SELECT shiftnum ,cashcode,CAST(time_beg AS char),shopcode, workshiftid  FROM workshift WHERE time_end IS NULL AND workshiftid >%s  '
# Нужно проверять не только открытые смены с последней, но и закрытые, которые умпели открыть и звкрыть между запусками программы
qrSelect_workshift_open = 'SELECT shiftnum ,cashcode,CAST(time_beg AS char),shopcode, workshiftid  FROM workshift WHERE  workshiftid >%s  '

qrSelect_workshift = '''SELECT shiftnum , shopcode, CAST(time_end AS char) , cashcode, CAST(time_beg AS char), workshiftid, storeId,cashId, scode,
                        checknum1, checknum2,  CAST(sumSale AS char), CAST(sumGain AS char), CAST(sumDrawer AS char),
                        CAST(firstchecktime AS char), CAST(sumsalecash AS char), CAST(sumsalenoncash AS char), CAST(sumsaleother AS char), CAST(sumgaincash AS char),
                        CAST(sumgainnoncash AS char), CAST(sumrefund AS char), CAST(sumrefundcash AS char), CAST(sumrefundnoncash AS char), countsale, countrefund
                        FROM  workshift WHERE time_end IS NOT NULL AND workshiftid >%s '''



qrSelect_workshiftnew = '''SELECT shiftnum , shopcode, CAST(time_end AS char) , cashcode, CAST(time_beg AS char), workshiftid, storeId,cashId, scode,
                        checknum1, checknum2,  CAST(sumSale AS char), CAST(sumGain AS char), CAST(sumDrawer AS char),
                        CAST(firstchecktime AS char), CAST(sumsalecash AS char), CAST(sumsalenoncash AS char), CAST(sumsaleother AS char), CAST(sumgaincash AS char),
                        CAST(sumgainnoncash AS char), CAST(sumrefund AS char), CAST(sumrefundcash AS char), CAST(sumrefundnoncash AS char), countsale, countrefund
                        FROM  workshift WHERE time_end IS NOT NULL AND workshiftid  IN ({}) '''


qrAdd_workshift_open = '''INSERT INTO wh (workshiftid) VALUES (?)'''

qrGet_saveworkshift_open = ''' SELECT * FROM wh'''

qrDel_workshift_close = ''' DELETE FROM wh WHERE workshiftid = ?'''
