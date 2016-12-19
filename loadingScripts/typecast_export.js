conn = new Mongo();
db = conn.getDB("data");
db.exports.find().forEach(function(data) {
    db.exports.update({
        "_id": data._id,
    }, {
        "$set": {
            "value_of_goods_in_rupees": parseFloat(data.value_of_goods_in_rupees),
            "quantity": parseFloat(data.quantity)
        }
    });
})
