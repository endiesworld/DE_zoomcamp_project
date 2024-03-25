from mage_ai.settings.repo import get_repo_path
from mage_ai.io.bigquery import BigQuery
from mage_ai.io.config import ConfigFileLoader
from os import path
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data_from_big_query(*args, **kwargs):
    """
    Template for loading data from a BigQuery warehouse.
    Specify your configuration settings in 'io_config.yaml'.

    Docs: https://docs.mage.ai/design/data-loading#bigquery
    """
    query ="""
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
            AND EXTRACT(MONTH FROM t.block_timestamp) = 3;
    """
    config_path = path.join(get_repo_path(), 'io_config.yaml')
    config_profile = 'default'

    return BigQuery.with_config(ConfigFileLoader(config_path, config_profile)).load(query)


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
