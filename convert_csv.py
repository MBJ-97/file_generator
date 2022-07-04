import json 
import csv

with open('src/fileCsv.csv', encoding='utf-8') as f:
    reader = csv.reader(f)
    next(reader)

    data ={"infos": []}
    for row in reader :
        [data["infos"].append({
            "ref": row[0],
            "dar": row[1],
            "marque": row[2],
            "unite": row[3],
            "GTIN": row[4],
        })]

    print(data)

with open('dist/output.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=4)
