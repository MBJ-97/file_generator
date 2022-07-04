from openpyxl import load_workbook 
import json

#open json file and change it to python dictionnary
file = open('./dist/output.json')
data = json.load(file)

#loop through and fill the infos in excel sheets        
for i in data['infos']:
    unite = i["unite"]
    ref = i["ref"]

    #Location of generated files
    fileName = "dist/"+str(ref)+".xlsx"

    #Sample excel sheet used to fill infos
    workbook = load_workbook(filename="src/fiche_type.xlsx")

    sheet = workbook.active

    sheet["A14"] = i['dar'] #name
    sheet["A16"] = i['marque'] #marque
    sheet["A21"] = 'وحدة (وحدات) : %s' %unite #unite de vente
    sheet["A12"] = i['GTIN'] #Code GTIN


    workbook.save(filename=fileName)




