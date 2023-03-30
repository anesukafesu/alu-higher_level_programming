-- create database hbtn_0d_usa
-- create table states inside htbn_0d_usa

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_od_usa.states(id INT UNIQUE AUTO_INCREMENT, name VARCHAR(256) NOT NULL, PRIMARY KEY(id));
