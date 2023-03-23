-- a script that prepares a MySQL server for the project


CREATE DATATBASE IF NOT EXISTS hbnb_test_db;
CREATE USER if NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED By hbnb_test_pwd;
CREATE ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
CREATE SELECT PRIVILEGES ON performance_schema.* TO 'hbnb_test'@'localhost';
FLUSH PRIVILEGES;
