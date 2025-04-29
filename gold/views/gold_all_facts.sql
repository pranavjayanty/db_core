CREATE OR REPLACE VIEW gold.all_facts AS
SELECT
    f.fact_id,
    u.name AS user_name,
    u.discord_id AS discord_id,
    f.fact_text,
    f.created_at
FROM silver.fact f
JOIN silver.user u ON f.user_id = u.id
ORDER BY f.created_at DESC;
