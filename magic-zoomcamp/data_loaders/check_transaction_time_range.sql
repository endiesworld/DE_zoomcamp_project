-- Docs: https://docs.mage.ai/guides/sql-blocks
SELECT 
    FORMAT_TIMESTAMP('%y-%m-%d', MIN(block_timestamp)) AS min_timestamp,
    FORMAT_TIMESTAMP('%y-%m-%d', MAX(block_timestamp)) AS max_timestamp 
FROM `bigquery-public-data.goog_blockchain_ethereum_goerli_us.transactions` ;