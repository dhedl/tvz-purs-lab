SELECT * FROM temperatura
JOIN korisnikove_temperature ON temperatura.id = korisnikove_temperature.id_temperature
WHERE korisnikove_temperature.id_korisnika = %s;

