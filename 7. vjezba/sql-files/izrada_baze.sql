-- izrada i odabir baze
DROP DATABASE IF EXISTS lvj6;
CREATE DATABASE IF NOT EXISTS lvj6;
USE lvj6;

DROP USER IF EXISTS app;
CREATE USER app@'%' IDENTIFIED BY '1234';
GRANT SELECT, INSERT, UPDATE, DELETE ON lvj6.* TO app@'%';

-- z2 izrada tablice temperatura/vlaga i upis
CREATE TABLE temperatura (
    id INT AUTO_INCREMENT PRIMARY KEY,
    datum DATETIME,
    vrijednost INT
);

INSERT INTO temperatura (datum, vrijednost)
VALUES
    ('2023-10-10 12:20:35', '23'),
    ('2023-10-11 11:20:35', '20'),
    ('2023-10-12 10:20:35', '22'),
    ('2023-10-13 09:20:35', '118');
    
CREATE TABLE vlaga (
    id INT AUTO_INCREMENT PRIMARY KEY,
    datum DATETIME,
    vrijednost INT
);

INSERT INTO vlaga (datum, vrijednost)
VALUES
    ('2023-10-10 13:20:35', '50'),
    ('2023-10-11 14:20:35', '32'),
    ('2023-10-12 10:20:35', '70'),
    ('2023-10-13 09:20:35', '94');

-- z4 izrada tablice ovlasti i upis 
CREATE TABLE ovlasti (
    id INT AUTO_INCREMENT PRIMARY KEY,
    naziv VARCHAR(100)
);

INSERT INTO ovlasti (naziv)
VALUES
    ('Administrator'),
    ('Korisnik');
    
-- z5 izrada tablice korisnik i upis
CREATE TABLE korisnik (
    id INT AUTO_INCREMENT PRIMARY KEY,
    ime CHAR(50),
    prezime CHAR(50),
    username VARCHAR(50),
    password VARBINARY(50),
    id_ovlasti INT,
    FOREIGN KEY (id_ovlasti) REFERENCES ovlasti(id) ON UPDATE CASCADE
);

INSERT INTO korisnik (ime, prezime, username, password, id_ovlasti)
VALUES
    ('Ladislav', 'Kovač', 'lkovac', UNHEX(SHA2('1234', 256)), 1),
    ('Valentina', 'Ilić', 'vilic', UNHEX(SHA2('abcd', 256)), 1),
    ('Danko', 'Kovac', 'dkovac', UNHEX(SHA2('ab12', 256)), 2),
    ('Katija', 'Kolar', 'kkolar', UNHEX(SHA2('12ab', 256)), 2);
    
-- z7 izrada tablice korisnikove_temperature i upis
CREATE TABLE korisnikove_temperature(
	id_korisnika INT NOT NULL,
    id_temperature INT NOT NULL,
    PRIMARY KEY (id_korisnika, id_temperature),
    FOREIGN KEY (id_korisnika) REFERENCES korisnik(id) ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (id_temperature) REFERENCES temperatura(id) ON UPDATE CASCADE ON DELETE CASCADE
);

INSERT INTO korisnikove_temperature (id_korisnika, id_temperature)
VALUES
    (1, 1),
    (2, 1),
    (1, 2),
    (2, 2),
    (1, 3);
    
CREATE TABLE korisnikove_vlage(
	id_korisnika INT NOT NULL,
    id_vlage INT NOT NULL,
    PRIMARY KEY (id_korisnika, id_vlage),
    FOREIGN KEY (id_korisnika) REFERENCES korisnik(id) ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (id_vlage) REFERENCES vlaga(id) ON UPDATE CASCADE ON DELETE CASCADE
);

INSERT INTO korisnikove_vlage (id_korisnika, id_vlage)
VALUES
    (1, 1),
    (2, 1),
    (1, 2),
    (2, 2),
    (3, 4),
    (1, 3);
    
    
    