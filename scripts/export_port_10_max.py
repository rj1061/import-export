from pymongo import MongoClient
from bson.code import Code
import pprint

client = MongoClient('mongodb://localhost:27017')
db = client['data']

mapper = Code("""
                function() {
                    var value = {}
                    value.val = this.value_of_goods_in_rupees
                    value.desc = this.description_of_goods
                    emit(this.port_of_destination, value);
                }
            """)

reducer = Code("""
                function (key, vals) {
                 var max = 0.0;
                 var desc = "";
                 for(var i = 0; i < vals.length; i++ ){
                    if(vals[i] > max){
                        max =  vals[i].val;
                        desc = descs[i].desc;
                    }
                 }
                 return desc;
             }
            """)

result = db.exports.map_reduce(mapper, reducer, "import_port")
csv = ""
for doc in result.find():
    pprint.pprint(doc)
    csv += str(doc['_id']) + "," + str(doc['value']) + "\n"

text_file = open("export_10_port_max.csv", "w")
text_file.write(csv)
text_file.close()

print type(result.find)
