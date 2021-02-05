CREATE DATABASE IF NOT EXISTS encar CHARACTER SET utf8mb4;

USE encar;

CREATE USER encar@localhost identified by 'iIJaOux40';
GRANT ALL ON *.* TO encar@localhost;

CREATE TABLE IF NOT EXISTS car (
  ID int NOT NULL,
  Name text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci,
  Detail text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci,
  Price text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci,
  Service text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci,
  Link text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci,
  CreatedDate datetime DEFAULT NULL,
  PRIMARY KEY (ID),
  UNIQUE KEY ID_UNIQUE (ID)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;