DELETE FROM vlaga
WHERE id = (
    SELECT id_vlage
    FROM korisnikove_vlage
    WHERE id_korisnika = %s
    ORDER BY id_vlage DESC
    LIMIT 1
);