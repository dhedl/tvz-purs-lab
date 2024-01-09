-- izrada i odabir baze
CREATE DATABASE IF NOT EXISTS lvj6;
USE lvj6;

-- z2 izrada tablice temperatura i upis
CREATE TABLE temperatura (
    id INT AUTO_INCREMENT PRIMARY KEY,
    datum DATE,
    vrijednost INT
);

INSERT INTO temperatura (datum, vrijednost)
VALUES
    ('2023-10-10', 23),
    ('2023-10-11', 20),
    ('2023-10-12', 22),
    ('2023-10-13', 18);
    
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
    password VARCHAR(50),
    id_ovlasti INT,
    FOREIGN KEY (id_ovlasti) REFERENCES ovlasti(id) ON UPDATE CASCADE
);

INSERT INTO korisnik (ime, prezime, username, password, id_ovlasti)
VALUES
    ('Ladislav', 'Kovač', 'lkovac', '1234', 1),
    ('Valentina', 'Ilić', 'vilic', 'abcd', 1),
    ('Danko', 'Kovac', 'dkovac', 'ab12', 2),
    ('Katija', 'Kolar', 'kkolar', '12ab', 2);
    
-- z7 izrada tablice korisnikove_temperature i upis
CREATE TABLE korisnikove_temperature (
    id_korisnika INT,
    id_temperature INT,
    FOREIGN KEY (id_korisnika) REFERENCES korisnik(id),
    FOREIGN KEY (id_temperature) REFERENCES temperatura(id),
    PRIMARY KEY (id_korisnika, id_temperature)
);

INSERT INTO korisnikove_temperature (id_korisnika, id_temperature)
VALUES
    (1, 1),
    (2, 1),
    (1, 2),
    (2, 2),
    (1, 3);
    
    
    