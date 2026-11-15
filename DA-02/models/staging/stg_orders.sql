-- Uses the deduplicated orders table created during DA-02 preparation.
select *
from {{ source('customer360', 'orders_clean') }}
