from pymongo import MongoClient
from bson.code import Code
import pprint

client = MongoClient('mongodb://localhost:27017')
db = client['data']

mapper = Code("""
                function() {
                    emit(this.port_or_country_of_origin, this.value_of_goods_in_rupees);
                }
            """)

reducer = Code("""
                function (key, vals) {
                 var total = 0.0;
                 vals.forEach(function(val){
                    total = total + val
                 })
                 return total;
             }
            """)

result = db.imports.map_reduce(mapper, reducer, "import_port")
csv = ""
for doc in result.find():
    pprint.pprint(doc)
    csv += str(doc['_id']) + "," + str(doc['value']) + "\n"

print csv
text_file = open("import_origin_agg.csv", "w")
text_file.write(csv)
text_file.close()

print type(result.find)
