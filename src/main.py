import threading
import os
from modules.snowflake_connector_object.connector import SnowflakeConnector

if __name__ == "__main__":
    print("\nWorking on the main thread...\n")
    buff = SnowflakeConnector()
    filename = r"C:\Users\migue\Projects\snowflake\snowflake-python-connector\src\config\credentials.yaml"
    buff.read_file_values(filename)
    buff.credentials_log_in()
    filename_2 = r"C:\Users\migue\Projects\snowflake\snowflake-python-connector\src\sql\scripts\snowflake_tutorial.sql"
    with open (filename_2, "r") as file:
        query = file.read()
    data = buff.execute_query(query)
    print(data)
