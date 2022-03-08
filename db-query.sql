CREATE DATABASE training_project

--create table Student_Personal
CREATE TABLE Student_Personal(
Std_ID varchar(15) PRIMARY KEY,
Std_Name varchar(50) NOT NULL,
Std_DOB date NOT NULL,
Std_Age int NOT NULL,
Std_Street varchar(50) NOT NULL,
Std_State varchar(30) NOT NULL,
Std_Country varchar(30) DEFAULT 'Malaysia' NOT NULL,
Std_Postcode int NOT NULL,
Std_Phone varchar(15) NOT NULL UNIQUE,
Std_Email varchar(25) NOT NULL UNIQUE,
CHECK (Std_Age > 0)
)

--create table Student_Marks
CREATE TABLE Student_Marks(
Std_ID varchar(15) FOREIGN KEY REFERENCES Student_Personal(Std_ID) on delete cascade on update cascade,
Malay int NOT NULL,
English int NOT NULL,
Science int NOT NULL,
Maths int NOT NULL,
Arts int NOT NULL,
History int NOT NULL,
Geography int NOT NULL,
Total int NOT NULL,
Average float NOT NULL,
Result varchar(5) NOT NULL,
Grade varchar(2) NOT NULL,
CHECK(Malay > 0 AND Malay <= 100),
CHECK(English > 0 AND English <= 100),
CHECK(Science > 0 AND Science <= 100),
CHECK(Maths > 0 AND Maths <= 100),
CHECK(Arts > 0 AND Arts <= 100),
CHECK(History > 0 AND History <= 100),
CHECK(Geography > 0 AND Geography <= 100),
CHECK(Result = 'PASS' or Result = 'FAIL')
)

-- test values
insert Student_Personal values(101, 'amir', '2022-01-01', 21, 'jalan', 'perak', 'malaysia', 31350, '01251312617', 'amir1@gmail.com')
insert Student_Marks values(102, 98, 45, 12, 65, 44, 74, 45, 101, 45.5, 'PASS', 'C')


--delete selected rows
DELETE FROM Student_Personal WHERE Std_ID = 102;

select * from Student_Personal
Select * from Student_Marks

-- bulk import from csv
GO
 
BULK INSERT dbo.Student_Personal
FROM 'C:\Users\Amir Yusoff\Documents\GitHub\Python\python-training-miniproject\name-list.csv'
WITH
(
        FORMAT='CSV',
        FIRSTROW=2
)
GO
 
BULK INSERT dbo.Student_Marks
FROM 'C:\Users\Amir Yusoff\Documents\GitHub\Python\python-training-miniproject\marks-list.csv'
WITH
(
        FORMAT='CSV',
        FIRSTROW=2
)
GO

-- display joined tables
SELECT * 
FROM Student_Personal
LEFT JOIN Student_Marks ON Student_Personal.Std_ID = Student_Marks.Std_ID

SELECT * 
FROM Student_Marks
INNER JOIN Student_Personal ON Student_Marks.Std_ID =  Student_Personal.Std_ID

Go

-- update total, average, result, grade

UPDATE Student_Marks SET Total = (Malay + English + Science +  Maths + Arts + History + Geography)
UPDATE Student_Marks SET Average = Total / 7

UPDATE Student_Marks
SET Grade = (
    CASE
        WHEN Average >= 80 THEN 'A' 
        WHEN Average >= 70 THEN 'B' 
		WHEN Average >= 60 THEN 'C' 
		WHEN Average >= 50 THEN 'D' 
        ELSE 'F' 
    END
)

UPDATE Student_Marks
SET Result = (
    CASE
        WHEN Grade ='A' or Grade ='B' or Grade ='C' or Grade ='D' THEN 'PASS'
        ELSE 'FAIL' 
    END
)

SELECT * 
FROM Student_Personal
LEFT JOIN Student_Marks ON Student_Personal.Std_ID = Student_Marks.Std_ID