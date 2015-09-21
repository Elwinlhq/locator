USE liquitest;

INSERT INTO project 
(id, name, category_id) VALUES 
(1, 'project guitar', 2),
(2, 'mayhem', 5);

INSERT INTO project_data 
(id, description, project_id) VALUES 
(1, 'a very nice project', 1),
(2, 'dont talk about it', 2);