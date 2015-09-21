var dbm = require('db-migrate');
var type = dbm.dataType;

exports.up = function(db, callback) {
    db.addColumn(
      'project',
      'category_name',
      type.STRING,
      callback
    )
};

exports.down = function(db, callback) {
    db.removeColumn(
      'project',
      'category_name',
      callback      
    )
};
