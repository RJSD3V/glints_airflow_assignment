GRANT ALL PRIVILEGES ON DATABASE GLINTS TO postgres;
CREATE TABLE IF NOT EXISTS Employee( ID INT PRIMARY KEY NOT NULL, NAME TEXT NOT NULL, EMAIL TEXT NOT NULL);
INSERT INTO Employee(ID,NAME,EMAIL) VALUES ( 0 , 'Raajas Sode' , 'raajas@gmail.com');
INSERT INTO Employee(ID,NAME,EMAIL) VALUES ( 1 , 'Tanya Mogul' , 'tanya@gmail.com');
INSERT INTO Employee(ID,NAME,EMAIL) VALUES ( 2 , 'Scott Tiger' , 'scott@gmail.com');