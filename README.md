# db_core
Core Database that stores information used by the suite of AI products built by the AI @ DSCubed team.

The database follows a Medallion Architecture, comprising of two layers:
- `bronze`: ingestion layer where data from sources like Notion/Discord are loaded.
- `silver`: processed/curated layer where `bronze` layer artefacts are conformed into a dimensonal data model.

The artefact definitions in the `gold` layer will reside in the usecase-specific repositories, like `darcy`, to decouple from the database and to leverage the repository design pattern.
