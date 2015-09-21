var dbm = require('db-migrate');
var type = dbm.dataType;

exports.up = function(db, callback) {
    db.runSql(
        'ALTER TABLE project DROP FOREIGN KEY project_x_category', 
        [],
        function(err) {
            if (err) { callback(err); return; }
            db.removeColumn('project', 'category_id', callback);
        }
    );
};


exports.down = function(db, callback) {
    callback();
};
