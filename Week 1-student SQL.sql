CREATE TABLE Student (
FirstName VARCHAR(255), 
SurName VARCHAR(255), 
Height INT,
PRIMARY KEY (FirstName, SurName)
);

INSERT INTO Student
VALUES('Lily', 'Johnson', 159);

UPDATE Student
SET Height = 166
WHERE FirstName = 'Addison' 
AND Surname = 'Deng';

DELETE FROM Student
WHERE FirstName = 'Ava'
AND Surname = 'Liu';

SELECT Height
FROM Student
WHERE FirstName = 'Eric'
And Surname = 'Yan';

SELECT * 
FROM Student
WHERE Height > 160
AND Height < 170;

SELECT AVG(Height)
FROM Student;

SELECT COUNT(*)
FROM Student;