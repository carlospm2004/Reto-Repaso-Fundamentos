# Reto de repaso: fundamentos

Aplicación desarrollada con **Python**, **PostgreSQL** y **Docker Compose**. El programa conecta con la base de datos, inserta un conjunto de personajes y muestra por consola los diez primeros registros guardados.

## Equipo

- **ADRIAN_LAZARO (MDIA)**
- **ANGEL_CARLOS_PEREZ (MDIA)**
- **CARLOS_GUTIERREZ (MDES)**

## Tecnologías utilizadas

- Python 3.12
- PostgreSQL 17
- Docker y Docker Compose
- `psycopg` 3.1.18 para la conexión con PostgreSQL

## Estructura del proyecto

```text
.
├── main.py
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .env.example
└── .gitignore
```

### Componentes principales

- **`main.py`**: define los personajes, establece la conexión con PostgreSQL, inserta los datos y consulta los diez primeros registros.
- **`docker-compose.yml`**: configura los servicios de PostgreSQL y de la aplicación.
- **`Dockerfile`**: crea la imagen de Python e instala las dependencias.
- **`requirements.txt`**: contiene las dependencias de Python.
- **`.env.example`**: plantilla de las variables de entorno necesarias.

## Requisitos previos

Antes de ejecutar el proyecto, instala:

- [Docker Desktop](https://www.docker.com/products/docker-desktop/)
- Git, si vas a clonar el repositorio

Comprueba que Docker está disponible:

```bash
docker --version
docker compose version
```

## Configuración

1. Crea el archivo `.env` a partir de la plantilla:

   ```bash
   copy .env.example .env
   ```

   En macOS o Linux:

   ```bash
   cp .env.example .env
   ```

2. Revisa las variables de entorno. Un ejemplo válido para la configuración incluida en `docker-compose.yml` es:

   ```env
   POSTGRES_USER=postgres
   POSTGRES_PASSWORD=cambia_esta_contrasena
   POSTGRES_DB=pruebadb
   DATABASE_URL=postgresql://<usuario>:<contraseña>@db:5432/pruebadb
   ```

   El host `db` funciona porque es el nombre del servicio de PostgreSQL dentro de la red de Docker Compose. No utilices `localhost` desde el contenedor de la aplicación.

## Ejecución

Desde la raíz del proyecto, inicia primero la base de datos:

```bash
docker compose up -d db
```

Después construye y ejecuta la aplicación:

```bash
docker compose up --build app
```

También se puede ejecutar la aplicación como una tarea puntual:

```bash
docker compose run --rm app
```

La aplicación mostrará mensajes de conexión e inserción y, a continuación, los registros consultados:

```text
Conexión establecida
Personajes insertados
{'id': 1, 'name': 'Zara Kestrel', 'species': 'Human'}
...
```

## Funcionamiento

1. Docker Compose inicia PostgreSQL en el servicio `db`.
2. El servicio `app` se conecta usando `DATABASE_URL`.
3. `main.py` inserta los personajes en la tabla `characters`.
4. Se consultan los diez primeros registros ordenados por `id`.
5. Los resultados se imprimen en la consola.

El proyecto utiliza el volumen `RetoDocker` para conservar los datos de PostgreSQL aunque se detengan los contenedores.


```
## Notas

- El servicio PostgreSQL se publica en el puerto `5435` del equipo anfitrión.
- La aplicación se ejecuta dentro de Docker y utiliza el puerto interno `5432` de PostgreSQL.
- Si se ejecuta `main.py` fuera de Docker, `DATABASE_URL` debe apuntar al host y puerto publicados, por ejemplo `localhost:5435`, y será necesario tener instaladas las dependencias de `requirements.txt`.
