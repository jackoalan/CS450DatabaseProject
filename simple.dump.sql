PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE simple (id INTEGER PRIMARY KEY AUTOINCREMENT, name);
INSERT INTO simple VALUES(1,'Jack');
INSERT INTO simple VALUES(2,'Nico');
DELETE FROM sqlite_sequence;
INSERT INTO sqlite_sequence VALUES('simple',2);
COMMIT;