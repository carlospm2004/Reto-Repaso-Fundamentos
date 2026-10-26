import os
from datetime import datetime, timezone

import psycopg

url = os.getenv("DATABASE_URL")
ahora = datetime.now(timezone.utc)

personajes = [
    ("Zara Kestrel", "Alive", "Human", "", "Female", "Valencia", "Hangar 7", None, None, ahora),
    ("Xul'Thar", "Alive", "Alien", "", "Genderless", "Nebula K-9", "Orbital Port", None, None, ahora),
    ("Unit R-17", "Alive", "Robot", "", "unknown", "Factory 3", "Workshop Delta", None, None, ahora),
    ("Bram Oakhollow", "Alive", "Human", "", "Male", "Bilbao", "Workshop Delta", None, None, ahora),
    ("Lia Moreau", "Unknown", "Human", "", "Female", "Marseille", "Orbital Port", None, None, ahora),
    ("Tobias Quell", "Dead", "Human", "", "Male", "Zurich", "Lab 42", None, None, ahora),
    ("Pip Vranx", "Alive", "Alien", "", "Male", "Kepler-22b", "Hangar 7", None, None, ahora),
    ("Ossa Lumen", "Unknown", "Alien", "", "Female", "Andromeda", "Unknown", None, None, ahora),
    ("Grelk", "Dead", "Alien", "", "Male", "Nebula K-9", "Scrapyard", None, None, ahora),
    ("Gearsworth", "Alive", "Robot", "", "Male", "Factory 3", "Valencia", None, None, ahora),
    ("NOVA-9", "Dead", "Robot", "", "unknown", "Lab 42", "Scrapyard", None, None, ahora),
    ("Bolt-7", "Alive", "Robot", "", "unknown", "Factory 3", "Hangar 7", None, None, ahora),
]


def cargar_personajes():
    try:
        with psycopg.connect(url) as connection:
            print("Conexión establecida")
            with connection.cursor() as cur:
                cur.executemany(
                    """INSERT INTO characters
                       (name, status, species, type, gender, origin_name, location_name, image, url, created)
                       VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""",
                    personajes,
                )
                print("Personajes insertados")

                cur.execute("SELECT id, name, species FROM characters ORDER BY id LIMIT 10")
                rows = cur.fetchall()

        return [
            {
                "id": row[0],
                "name": row[1],
                "species": row[2],
            }
            for row in rows
        ]


    except Exception as e:
        print("Error:", e)
        raise


if __name__ == "__main__":
    for personaje in cargar_personajes():
        print(personaje)