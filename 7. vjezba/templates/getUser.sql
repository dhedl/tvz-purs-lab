SELECT id, username FROM korisnik WHERE username = '{{username}}' AND password = UNHEX(SHA2('{{password}}', 256));
