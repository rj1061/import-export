conn = new Mongo();
db = conn.getDB("data");
db.imports.find().forEach(function(data) {
    db.imports.update({
        "_id": data._id,
    }, {
        "$set": {
            "value_of_goods_in_rupees": parseFloat(data.value_of_goods_in_rupees),
            "quantity": parseFloat(data.quantity)
        }
    });
})
