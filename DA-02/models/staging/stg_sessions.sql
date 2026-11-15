-- Staging reference to the existing BigQuery sessions table.
select *
from {{ source('customer360', 'sessions') }}
