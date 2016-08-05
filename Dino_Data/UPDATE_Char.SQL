/*CREATE TABLE "Dinosaur" (
	`ID`	Integer,
	`Name`	Integer,
	`Teeth`	TEXT,
	`How_it_moved`	TEXT, 'Meters'INTEGER,
	PRIMARY KEY(ID)
);
*/

/*  Correct Syntax to Update Meters in Characteristic table  */
/*
UPDATE Characteristic
SET Meters = 
(SELECT Meters
FROM Length WHERE Characteristic.Length_ID = Length.ID);

*/


/*Syntax to get 10 rows from Characteristic and Dinosaur*/
/*SELECT * FROM Characteristic JOIN Dinosaur
ON (SELECT Characteristic_ID FROM ID_Info WHERE ID = Dinosaur.ID)LIMIT(10);*/

SELECT Name FROM Dinosaur JOIN Diet 
ON (SELECT ID FROM ID_Info WHERE Diet_ID)