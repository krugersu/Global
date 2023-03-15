PRAGMA foreign_keys = off;
BEGIN TRANSACTION;


DROP TABLE IF EXISTS additionalprices;

CREATE TABLE additionalprices (
    additionalpricesid TEXT (20),
    pricecode          INTEGER (11),
    price              REAL (13, 2),
    name               TEXT (40) 
);



DROP TABLE IF EXISTS barcodes;

CREATE TABLE barcodes (
    barcodesid               TEXT (20),
    additionalpricesid       INTEGER,
    aspectvaluesetcode       INTEGER (11),
    barcode                  TEXT (100),
    cquant                   REAL (13, 3),
    measurecode              INTEGER (11),
    minprice                 REAL (13, 3),
    name                     TEXT (200),
    packingmeasure           INTEGER (11),
    packingprice             REAL (15, 2),
    price                    REAL (15, 2),
    quantdefault             REAL (13, 3),
    minretailprice           REAL (13, 2),
    customsdeclarationnumber TEXT (32),
    tmctype                  INTEGER (11),
    ntin                     TEXT (255) 
);



DROP TABLE IF EXISTS invent;

CREATE TABLE invent (
    inventcode              TEXT (20),
--    inventgroup             TEXT (100),
    name                    TEXT (200),
--    barcode                 TEXT (100),
    barcodes                TEXT (20),
    price                   REAL (13, 2),
    minprice                REAL (13, 2),
    additionalprices        TEXT (20),
    options                 TEXT (20),
    sellrestrictperiods     TEXT (20),
    extendedoptions         TEXT,
    discautoscheme          INTEGER,
    deptcode                INTEGER,
    taxgroupcode            INTEGER,
    measurecode             INTEGER,
    remain                  REAL (13, 4),
    remaindate              DATETIME,
    articul                 TEXT (200),
    defaultquantity         REAL (13, 3),
    taramode                INTEGER (11),
    taracapacity            REAL (13, 3),
    aspectschemecode        INTEGER (11),
    aspectvaluesetcode      INTEGER (11),
    aspectusecase           INTEGER (11),
    aspectselectionrule     INTEGER (11),
    age                     INTEGER (11),
    alcoholpercent          REAL (4, 2),
    cquant                  REAL (13, 3),
    inn                     TEXT (20),
    kpp                     TEXT (20),
    alctypecode             INTEGER (11),
    paymentobject           INTEGER (11),
    manufacturercountrycode INTEGER (11),
    opmode                  INTEGER (11),
    loyaltymode             INTEGER (11),
    minretailprice          REAL (13, 2),
    Parent                  BOOLEAN,
    isParent                TEXT (20) 
);



DROP TABLE IF EXISTS inventitemoptions;

CREATE TABLE inventitemoptions (
    inventitemoptionsid     TEXT (20),
    disablebackinsale       INTEGER (1),
    disableinventshow       INTEGER (1),
    disableinventsale       INTEGER (1),
    disableinventback       INTEGER (1),
    requiredepartmentmanual INTEGER (1),
    enabledepartmentmanual  INTEGER (1),
    enablebarcodemanual     INTEGER (1),
    enablebarcodescanner    INTEGER (1),
    visualverify            INTEGER (1),
    ageverify               INTEGER (1),
    requiresalerestrict     INTEGER (1),
    egaisverify             INTEGER (1),
    prepackaged             INTEGER (1),
    nopdfegaisverify        INTEGER (1),
    alcoset                 INTEGER (1),
    freesale                INTEGER (1),
    rfidverify              INTEGER (1),
    lowweight               INTEGER (1),
    weightcontrolbypass     INTEGER (1),
    tobacco                 INTEGER (1),
    shoes                   INTEGER (1),
    fuzzyweight             INTEGER (1),
    ignoremarking           INTEGER (1),
    markdownverify          INTEGER (1) 
);



DROP TABLE IF EXISTS optionsa;

CREATE TABLE optionsa (
    optionsidid         TEXT (20),
    inventitemoptions   TEXT (20),
    priceoptions        TEXT (20),
    quantityoptions     TEXT (20),
    remainsoptions      TEXT (20)
);



DROP TABLE IF EXISTS priceoptions;

CREATE TABLE priceoptions (
    priceoptionsid        TEXT (20),
    enablepricemanual     INTEGER (1),
    requirepricemanual    INTEGER (1),
    requireselectprice    INTEGER (1),
    requiredeferredprice  INTEGER (1),
    enableexcisemarkprice INTEGER (1) 
);



DROP TABLE IF EXISTS quantityoptions;

CREATE TABLE quantityoptions (
    quantityoptionsid           TEXT (20),
    enabledefaultquantity       INTEGER (1),
    enablequantitylimit         INTEGER (1),
    quantitylimit               REAL (13, 3),
    enablequantityscales        INTEGER (1),
    enablequantitybarcode       INTEGER (1),
    enablequantitymanual        INTEGER (1),
    requirequantitymanual       INTEGER (1),
    requirequantitybarcode      INTEGER (1),
    requirequantityscales       INTEGER (1),
    enabledocumentquantitylimit INTEGER (1),
    autogetquantityfromscales   INTEGER (1),
    documentquantlimit          REAL (13, 3) 
);



DROP TABLE IF EXISTS remainsoptions;

CREATE TABLE remainsoptions (
    remainsoptionsid TEXT (20) 
);



DROP TABLE IF EXISTS sellrestrictperiods;

CREATE TABLE sellrestrictperiods (
    sellrestrictperiodsid TEXT (20),
    dateend               DATE,
    datestart             DATE,
    dayend                INTEGER (11),
    daystart              INTEGER (11),
    timeend               TIME,
    timestart             TIME
);


DROP TABLE IF EXISTS goodsitem;

CREATE TABLE goodsitem (
	code            	TEXT (100),
	opcode          	INTEGER,
	cquant          	REAL (13, 3) 
);




DROP VIEW IF EXISTS CountSummAnalog;
CREATE VIEW CountSummAnalog AS
SELECT * FROM invent WHERE isParent ='';



DROP VIEW IF EXISTS SummIsParent;
CREATE VIEW SummIsParent AS
    SELECT isParent,
           sum(remain) AS remain
      FROM invent
     WHERE isParent IN (
               SELECT inventcode
                 FROM invent
                WHERE Parent = 1
           )
     GROUP BY isParent;



DROP VIEW IF EXISTS SummProd;
CREATE VIEW SummProd AS

SELECT * FROM CountSummAnalog 
inner JOIN (SELECT code , opcode ,  SUM(cquant)   FROM goodsitem  
Group by code) as st
ON st.code  = CountSummAnalog.inventcode;




COMMIT TRANSACTION;
PRAGMA foreign_keys = on;
