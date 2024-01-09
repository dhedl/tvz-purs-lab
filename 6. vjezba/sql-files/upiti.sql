-- upiti

-- z3 dohvacanje svih podataka
SELECT * FROM temperatura;

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

-- z7 visestruki upit
SELECT ime, prezime, vrijednost AS vrijednost_temperature FROM korisnik
JOIN korisnikove_temperature ON korisnik.id = korisnikove_temperature.id_korisnika
JOIN temperatura ON korisnikove_temperature.id_temperature = temperatura.id;
