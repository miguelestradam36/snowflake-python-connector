import threading
import os
from modules.snowflake_connector_object.connector import SnowflakeConnector

if __name__ == "__main__":
    print("\nWorking on the main thread...\n")
    buff = SnowflakeConnector()
    filename = r"C:\Users\migue\Projects\snowflake\snowflake-python-connector\src\config\credentials.yaml"
    buff.read_file_values(filename)
    query = """
    
    """
    buff.execute_query = query
    data = buff.execute_query
    buff.credentials_log_in()
