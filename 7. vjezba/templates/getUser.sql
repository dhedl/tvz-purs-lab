SELECT id, username FROM korisnik WHERE username = %s AND password = UNHEX(SHA2(%s, 256));
