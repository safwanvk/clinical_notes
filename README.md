# Clinical Notes API

A FastAPI application using Strawberry GraphQL and SQLAlchemy (async) for managing clinical notes and patients.

---

## Features

- Async database access with SQLAlchemy
- GraphQL API with Strawberry
- Modular project structure
- Environment-based configuration

---

## Requirements

- Python 3.9+
- Or: [Docker](https://www.docker.com/) and [Docker Compose](https://docs.docker.com/compose/)
- PostgreSQL (or compatible database)
- [pip](https://pip.pypa.io/) or [Poetry](https://python-poetry.org/) for dependencies

---

## Setup Instructions without Docker

1. **Clone the repository:**

   ```bash
   git clone https://github.com/safwanvk/clinical_notes.git
   cd clinical_notes
   ```

2. **Create and activate a virtual environment:**

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables:**

   Create a `.env` file in the `app` directory with:

   ```
   DATABASE_URL=postgresql+asyncpg://user:password@localhost:5432/clinical_notes
   ENV=development
   ```

   Or set these variables in your shell.

5. **Run the application:**

   ```bash
   uvicorn app.main:clinical_app --reload
   ```

6. **Access the GraphQL Playground:**

   Open [http://localhost:8000/graphql](http://localhost:8000/graphql) in your browser.

---

## Running with Docker

1. **Copy and edit the `.env` file:**

   Create a `.env` file in your project root (or use the provided sample):

   ```
   POSTGRES_HOST=postgres
   POSTGRES_PORT=5432
   POSTGRES_DB=clinical_notes_db
   POSTGRES_USER=user
   POSTGRES_PASSWORD=password
   ENV=development
   ```

2. **Build and start all services:**

   ```bash
   docker-compose up --build
   ```

   This will start:
   - The FastAPI app (on [http://localhost:8000](http://localhost:8000))
   - PostgreSQL database (on port 5432)
   - Adminer DB UI (on [http://localhost:8080](http://localhost:8080))

## Database Initialization

- Tables are created automatically at startup via the `init_db` function in `app/db.py`.
- Ensure your database is running and accessible with the credentials in `DATABASE_URL`.

---

## Notes

- All models should inherit from `Base` in `app/base.py`.
- Avoid circular imports by only importing `Base` from `base.py` in both `models.py` and `db.py`.
- The `ENV` variable controls whether the GraphiQL interface is enabled.

---

## License

MIT