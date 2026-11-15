-- Customer 360 mart sourced from the existing prototype table.
-- This is a dbt model wrapper; it does not rebuild identity resolution.
select *
from {{ source('customer360', 'customer_360') }}
