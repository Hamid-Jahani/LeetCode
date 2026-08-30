-- 1693. Daily Leads and Partners (Easy)
-- https://leetcode.com/problems/daily-leads-and-partners/
--
-- Table: DailySales(date_id, make_name, lead_id, partner_id)
--
-- For each date_id and make_name, return the number of distinct lead_id and
-- distinct partner_id values.
--
-- Dialect: MySQL

SELECT
    date_id,
    make_name,
    COUNT(DISTINCT lead_id)    AS unique_leads,
    COUNT(DISTINCT partner_id) AS unique_partners
FROM DailySales
GROUP BY date_id, make_name;
