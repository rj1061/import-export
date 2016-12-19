import csv
import json
from pymongo import MongoClient

importFile = open('../data/imports/imports.csv', 'r')
client = MongoClient('mongodb://localhost:27017/')
db = client['data']
collection = db['imports']

fieldnames = ("unit_quantity_code",
              "location_state",
              "customs_tariff_heading",
              "value_of_goods_in_rupees",
              "quantity_desc",
              "description_of_goods",
              "location_code",
              "quantity_type",
              "date",
              "location_name",
              "type",
              "port_or_country_of_origin",
              "quantity",
              "serial_id")

reader = csv.DictReader(importFile, fieldnames)
for row in reader:
    jsonString = json.dumps(row)
    result = collection.insert_one(row)
    print result.inserted_id