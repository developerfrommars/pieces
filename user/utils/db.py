import os
import sqlalchemy

def get_db_config() -> list:
    return [os.environ['DB_USER_DEV'], os.environ['DB_PASS_DEV'], os.environ['DB_HOST'], os.environ['DB_NAME_DEV']]


def get_engine() -> sqlalchemy.engine:
    return sqlalchemy.create_engine('postgresql://{}:{}@{}/{}'.format(*get_db_config()))