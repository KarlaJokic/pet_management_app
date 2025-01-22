# Pet Management App
aplikacija za vođenje evidencije o kućnim ljubimcima i veterinarskim uslugama

## Opis funkcionalnosti aplikacije
Ova aplikacija omogućava upravljanje ljubimcima i veterinarskim uslugama, uključujući:
- Registraciju korisnika i prijavu.
- Pregled, dodavanje, uređivanje i brisanje ljubimaca (CRUD operacije).
- Upravljanje veterinarskim uslugama (CRUD operacije).
- Implementaciju RESTful API endpointa za Pet model s podrškom za:
  - Dohvat svih ljubimaca.
  - Kreiranje novog ljubimca.
  - Dohvat pojedinačnog ljubimca prema ID-u.
  - Ažuriranje podataka ljubimca.
  - Brisanje ljubimca.
- Pretraživanje i filtriranje podataka unutar ListView prikaza.
- Autentifikaciju korisnika za pristup aplikaciji i API endpointima.

## Tehnologije
- Python
- Django
- Django REST Framework
- HTML, CSS (za predloške)
- SQLite (default baza podataka)

## API Endpointi
1. `GET /api/pets/`: Dohvat svih ljubimaca.
2. `POST /api/pets/`: Kreiranje novog ljubimca.
3. `GET /api/pets/{id}/`: Dohvat pojedinačnog ljubimca prema ID-u.
4. `PUT /api/pets/{id}/`: Ažuriranje podataka ljubimca.
5. `DELETE /api/pets/{id}/`: Brisanje ljubimca.

## Autor(i): Karla Jokić i Eli Lipovac (lab4 + završni)
