CREATE DATABASE FaceRec; 

USE FaceRec; 

CREATE TABLE EMPLOYEE (
	Id int NOT NULL AUTO_INCREMENT PRIMARY KEY,
    DNI int NOT NULL,
    FirstName varchar(15) NOT NULL,
    SecondName varchar(15),
    LastName varchar(20),
    LastArrival timestamp
);

