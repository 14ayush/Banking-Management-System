CREATE TABLE transaction_table(
TIMESTAMP DATETIME DEFAULT GETDATE(),
account_no INT,
description varchar(20),
transaction_type varchar(25),
amount float
);


