use database spellbandb;
create Table  customer(
     CustomerID int not null auto_increment,
     FirstName varchar(250),
     LastName varchar(250),
     Address varchar(250),
     County varchar(250),
     Email varchar(320),
     PhoneNumber varchar(15),
     PRIMARY KEY(CustomerID)
     );