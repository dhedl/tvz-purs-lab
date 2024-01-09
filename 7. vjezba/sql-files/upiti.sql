-- upiti

-- z3 dohvacanje svih podataka
SELECT * FROM temperatura;
SELECT * FROM vlaga;

-- z3 dohvacanje zadnjeg reda
SELECT * FROM temperatura
ORDER BY id DESC
LIMIT 1;

-- z6 spajanje korisnika i ovlasti
SELECT ime, prezime, naziv FROM korisnik
INNER JOIN ovlasti ON id_ovlasti = ovlasti.id;

-- z6 dohvacanje korisnika
SELECT * FROM korisnik
WHERE username = 'kkolar' AND password = '12ab';

-- z8 visestruki upit
SELECT ime, prezime, vrijednost AS vrijednost_temperature FROM korisnik
INNER JOIN korisnikove_temperature ON korisnik.id = id_korisnika
LEFT JOIN temperatura ON temperatura.id = id_temperature
WHERE id_korisnika = 1;

-- brisanje temperature
DELETE FROM temperatura
WHERE id = (
    SELECT id_temperature
    FROM korisnikove_temperature
    WHERE id_korisnika = 1
    ORDER BY id_temperature DESC
    LIMIT 1
);

-- brisanje kor_temp
DELETE FROM korisnikove_temperature
WHERE id_korisnika = %s
ORDER BY id_temperature DESC
LIMIT 1;



