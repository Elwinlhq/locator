var dbm = require('db-migrate');
var type = dbm.dataType;

exports.up = function(db, callback) {
    db.runSql(
        'DROP VIEW IF EXISTS complete_project', 
        [],
        function(err) {
            if (err) { callback(err); return; }
            
            db.runSql(
                'CREATE VIEW complete_project AS ( \
                SELECT project.id, project.name, project_data.description \
                FROM project \
                     JOIN \
                     project_data ON project_data.project_id = project.id \
                 );', 
                [],
                callback
            );
        }
    );
};

exports.down = function(db, callback) {
    callback();
};
