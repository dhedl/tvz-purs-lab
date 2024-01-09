DELETE FROM temperatura
WHERE id = (
    SELECT id_temperature
    FROM korisnikove_temperature
    WHERE id_korisnika = %s
    ORDER BY id_temperature DESC
    LIMIT 1
);