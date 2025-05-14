-- Create the database
CREATE DATABASE SBI_Database;
GO

USE SBI_Database;
GO

-- Create Users table (for login)
CREATE TABLE Users (
	account_no BIGINT UNIQUE,
	phone_no BIGINT Unique,

    username NVARCHAR(50) UNIQUE NOT NULL,
    password NVARCHAR(255) NOT NULL
);
GO

-- Create Customers table
CREATE TABLE Customers (
    id INT PRIMARY KEY IDENTITY(1,1),
	account_no BIGINT UNIQUE,
	phone_no BIGINT Unique,
    name NVARCHAR(100),
	password NVARCHAR(100),
    email NVARCHAR(100),
	account_type varchar(100),
    balance DECIMAL(18, 2),
	card_no BIGINT UNIQUE,
	pin_no BIGINT UNIQUE
);
GO


