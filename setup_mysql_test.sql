#!/bin/bash

"""
a script that prepares a MySQL server for the project
"""

CREATE DATATBASE IF NOT EXIST hbnb_test_db;
CREATE USER if NOT EXIST 'hbnb_test'@'localhost' IDENTIFIED By hbnb_test_pwd;
USE hbnb_test_db;
CREATE ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
USE performance_schema;
CREATE SELECT PRIVILEGES ON performance_schema.* TO 'hbnb_test'@'localhost';
FLUSH PRIVILEGES;
SET FOREIGN_KEY_CHECKS=1;
