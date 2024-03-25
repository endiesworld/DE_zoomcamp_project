-- Docs: https://docs.mage.ai/guides/sql-blocks
SELECT 
    r.status, t.block_hash, t.block_timestamp, t.transaction_hash, t.from_address, t.to_address
FROM
    `bigquery-public-data.goog_blockchain_ethereum_goerli_us.transactions` AS t
JOIN
    `bigquery-public-data.goog_blockchain_ethereum_goerli_us.receipts` AS r
ON
    t.transaction_hash = r.transaction_hash
WHERE 
    EXTRACT(YEAR FROM t.block_timestamp) IN (2021)
    AND EXTRACT(MONTH FROM t.block_timestamp) = 3; ;
