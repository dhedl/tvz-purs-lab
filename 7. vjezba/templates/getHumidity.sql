SELECT * FROM vlaga
JOIN korisnikove_vlage ON vlaga.id = korisnikove_vlage.id_vlage
WHERE korisnikove_vlage.id_korisnika = %s;
