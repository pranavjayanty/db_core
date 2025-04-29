
# db_core – Collective Brain Memory Architecture

This repository defines the **PostgreSQL-based memory layer** for the Collective Brain system that supports a suite of AI bots used by a student club. It implements a structured data model using a **Medallion Architecture** with three layers:

- **Bronze**: Raw, unstructured data ingested from external sources (e.g., Notion, Discord).
- **Silver**: Cleaned, structured, and relational tables that form the core memory graph.
- **Gold**: Bot-facing views that extract relevant slices of memory for specific use cases.

The architecture emphasizes scalability, version control, and separation of concerns, with all schema and transformation logic defined via SQL and orchestrated through Python.

---

## Project Structure

```
db_core/
├── bronze/                  # Raw staging tables
│   └── ddl/                 # SQL DDL for bronze schema
├── silver/                  # Cleaned and modeled tables
│   ├── ddl/                 # SQL DDL for entities (user, fact, etc.)
│   └── transformations/     # SQL scripts to load from bronze to silver
├── gold/                    # Use-case specific views
│   └── views/               # CREATE VIEW statements

├── manifests/               # YAML manifests to define SQL execution order
├── data/                    # Raw CSVs to ingest
├── utils/                   # Script runner, manifest loader, etc.
├── scripts/                 # CLI scripts for deployment and ingestion

├── database/                # Python repository pattern interface for bots
│   └── database.py          # The core Database class

├── .env.example             # Environment variable template
├── requirements.txt         # Python dependencies
├── README.md                # Project documentation
```

---

## Setup and Deployment

### 1. Install dependencies

```bash
uv pip install -r requirements.txt
```

### 2. Configure environment

Copy the `.env.example` file and set the `DATABASE_URL` for your target RDS instance:

```bash
cp .env.example .env
```

Edit `.env`:

```
DATABASE_URL=postgresql://<user>:<password>@<host>:5432/<database>
```

### 3. Deploy all layers

This command will execute all SQL files (Bronze → Silver → Gold) in the correct order based on YAML manifests:

```bash
PYTHONPATH=. python scripts/deploy_all_layers.py
```

The runner:
- Creates schemas and tables
- Loads curated data
- Builds Gold views
- Performs basic post-load checks (`SELECT * LIMIT 5`)

### 4. Ingest CSVs into Bronze

For example, to ingest users from a CSV file:

```bash
PYTHONPATH=. python scripts/bronze_ingest_users.py
```

---

## Repository Pattern (for Bots)

Bots interact with the memory layer via a Python class that abstracts database access.

```python
from database.database import Database
db = Database()

# Get user info
db.get_user(discord_id="123456")

# Get facts related to a user in the last 30 days
db.get_user_fact(discord_id="123456", days_back=30)

# Store a new fact about a user
db.set_user_fact(discord_id="123456", fact_text="Is building an AI bot.")
```

This follows the Repository Pattern to isolate database logic and enable decoupling between memory logic and bot behavior.

---

## Medallion Layers

### Bronze Layer

Staging tables that mirror external data sources with minimal transformation. Loaded via CSVs or external pipelines.

Example: `bronze.user_raw`

### Silver Layer

Structured and cleaned relational tables that form the core of the memory graph. All entities (e.g., users, facts, events) live here.

Example: `silver.user`, `silver.fact`

### Gold Layer

Bot-facing SQL views created over Silver tables. These are curated to meet specific retrieval needs for bots.

Examples:
- `gold.users_base`: all user metadata
- `gold.committee_users`: users with a role containing "committee"
- `gold.all_facts`: joined view of user facts
- `gold.high_confidence_facts`: only trusted facts

---

## Example Workflow

1. Ingest new people data into `bronze.user_raw`
2. Run transformation to populate `silver.user`
3. Insert facts into `silver.fact`
4. Query from `gold.all_facts` via bot interfaces

---

## Future Plans

- Add additional entities: events, departments, messages
- Integrate embedding generation for semantic search
- Build automated ingestion pipelines from Notion/Discord
- Add validation and test harnesses for schema changes
- Optional: CI/CD deployment via GitHub Actions

---

