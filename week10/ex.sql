-- Create the database
CREATE DATABASE IF NOT EXISTS python_db;

-- Switch to the newly created database
USE python_db;

-- Create the Hospital table
CREATE TABLE IF NOT EXISTS Hospital (
    Hospital_Id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    Hospital_Name VARCHAR(100) NOT NULL,
    Bed_Count INT
);

-- Insert data into the Hospital table
INSERT INTO Hospital (Hospital_Name, Bed_Count) 
VALUES 
('Mayo Clinic', 200), 
('Cleveland Clinic', 400), 
('Johns Hopkins', 1000), 
('UCLA Medical Center', 1500);

-- Create the Doctor table
CREATE TABLE IF NOT EXISTS Doctor (
    Doctor_Id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    Doctor_Name VARCHAR(100) NOT NULL,
    Hospital_Id INT NOT NULL,
    Joining_Date DATE NOT NULL,
    Speciality VARCHAR(100) NOT NULL,
    Salary INT NOT NULL,
    Experience SMALLINT
);

-- Insert data into the Doctor table
INSERT INTO Doctor (Doctor_Name, Hospital_Id, Joining_Date, Speciality, Salary, Experience) 
VALUES 
('David', '1', '2005-02-10', 'Pediatric', '40000', NULL), 
('Michael', '1', '2018-07-23', 'Oncologist', '20000', NULL), 
('Susan', '2', '2016-05-19', 'Garnacologist', '25000', NULL), 
('Robert', '2', '2017-12-28', 'Pediatric', '28000', NULL), 
('Linda', '3', '2004-06-04', 'Garnacologist', '42000', NULL), 
('William', '3', '2012-09-11', 'Dermatologist', '30000', NULL), 
('Richard', '4', '2014-08-21', 'Garnacologist', '32000', NULL), 
('Karen', '4', '2011-10-17', 'Radiologist', '30000', NULL);
