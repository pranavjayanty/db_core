CREATE SCHEMA IF NOT EXISTS gold;

CREATE OR REPLACE VIEW gold.users_base AS
SELECT
    id AS user_id,
    name,
    role,
    notion_id,
    discord_id,
    created_at,
    updated_at
FROM silver.user;
