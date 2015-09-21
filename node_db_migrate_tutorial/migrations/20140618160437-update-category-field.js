var dbm = require('db-migrate');
var type = dbm.dataType;

exports.up = function(db, callback) {

    db.runSql(
        'UPDATE project JOIN category ON project.category_id = category.id SET project.category_name = category.name', 
        [],
        callback
    );
};

exports.down = function(db, callback) {
    callback();
};
