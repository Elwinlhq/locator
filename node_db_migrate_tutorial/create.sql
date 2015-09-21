-- CREATE ALL
USE liquitest;

CREATE TABLE category (
  id int(11) NOT NULL AUTO_INCREMENT,
  name varchar(255),
  PRIMARY KEY (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE project (
  id int(11) NOT NULL AUTO_INCREMENT,
  name varchar(255),
  category_id int(11) NOT NULL,
  PRIMARY KEY (id),
  KEY category_id (category_id),
  CONSTRAINT project_x_category FOREIGN KEY (category_id) REFERENCES category (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE project_data (
  id int(11) NOT NULL AUTO_INCREMENT,
  description varchar(500),
  project_id int(11) NOT NULL,
  PRIMARY KEY (id),
  KEY project_id (project_id),
  CONSTRAINT project_data_x_project FOREIGN KEY (project_id) REFERENCES project (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE VIEW complete_project AS (
    SELECT project.id, project.name, category.name AS category, project_data.description 
    FROM project 
         JOIN 
         project_data ON project_data.project_id = project.id
         JOIN 
         category ON project.category_id = category.id
);