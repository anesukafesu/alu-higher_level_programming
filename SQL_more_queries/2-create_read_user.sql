-- create user user_0d_2 with password user_0d_2_pwd
-- then create database hbtn_0d_2
-- grant select permission to user_0d_2 over hbtn_0d_2

CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
