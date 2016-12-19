import csv
import json
from pymongo import MongoClient

exportFile = open('../data/exports/exports.csv', 'r')
client = MongoClient('mongodb://localhost:27017/')
db = client['data']
collection = db['exports']

fieldnames = ("quantity_desc",
              "description_of_goods",
              "location_code",
              "quantity_type",
              "date",
              "location_name",
              "type",
              "port_of_destination",
              "quantity",
              "unit_quantity_code",
              "location_state",
              "customs_tariff_heading",
              "value_of_goods_in_rupees",
              "serial_id")

reader = csv.DictReader(exportFile, fieldnames)
for row in reader:
    jsonString = json.dumps(row)
    result = collection.insert_one(row)
    print result.inserted_id