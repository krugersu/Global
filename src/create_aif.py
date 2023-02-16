import os
import json

header = "### data begin ###"
footer = "### data end ###"
separator = "---"

	

	
addInventItem = {"command": "addInventItem" } # Команда addInventItem добавляет товар в справочник товаров. 
 
clearInventory = {"command":"clearInventory"} # Команда clearInventory очищает справочник товаров со всеми зависимыми записями. 

clearTmcScale = {"command":"clearTmcScale"}  # Команда clearTmcScale очищает справочник товаров для прогрузки на весы

data = []
data.append(header)
data.append(clearInventory)
data.append(separator)
data.append(addInventItem)
data.append(separator)
data.append(footer)


def saveTestFile():
    with open(r"data.aif", "w") as file:
        file.writelines("%s\n" % line for line in data)
    ''' with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4) '''