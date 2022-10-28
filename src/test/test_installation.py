import pytest
def test_installation():
    import snowflake.connector
    assert type(snowflake.connector)