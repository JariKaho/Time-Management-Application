CREATE TABLE Employees (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100)
);

CREATE TABLE Customers (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100)
);

CREATE TABLE WorkingHours (
    workingHourID SERIAL PRIMARY KEY,
    customerID INT NOT NULL,
    employeeID INT NOT NULL,
    startTime TIMESTAMP NOT NULL,
    endTime TIMESTAMP NOT NULL,
    lunchBreak BOOLEAN NOT NULL,
    FOREIGN KEY (customerID) REFERENCES Customers(id),
    FOREIGN KEY (employeeID) REFERENCES Employees(id)
);
-- ALTER TABLE table_name
--ALTER COLUMN column_name datatype;
SELECT * FROM Employees;

DROP TABLE WorkingHours;

SELECT * FROM WorkingHours;

