CREATE DATABASE chart_db;
USE chart_db;
CREATE TABLE sales(
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50),
    count INT
);

INSERT INTO sales(name,count)
VALUES
("苹果",100),
("香蕉",80),
("橙子",120);

SELECT * FROM sales;
