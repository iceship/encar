CREATE DATABASE IF NOT EXISTS encar CHARACTER SET utf8mb4;

USE encar;

CREATE USER encar@localhost identified by 'iIJaOux40!';
GRANT CREATE ROUTINE, ALTER ROUTINE, CREATE VIEW, CREATE TEMPORARY TABLES, EVENT, DROP, TRIGGER, REFERENCES, LOCK TABLES  ON `encar`.* TO 'encar'@'%' WITH GRANT OPTION;
FLUSH PRIVILEGES;

CREATE TABLE IF NOT EXISTS car (
  ID int NOT NULL,
  Name text CHARACTER SET utf8mb4,
  Detail text CHARACTER SET utf8mb4,
  Price text CHARACTER SET utf8mb4,
  Service text CHARACTER SET utf8mb4,
  Link text CHARACTER SET utf8mb4,
  CreatedDate datetime DEFAULT NULL,
  PRIMARY KEY (ID),
  UNIQUE KEY ID_UNIQUE (ID)
);