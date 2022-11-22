"""
Check modules folder
"""
from modules.snowflake_connector_object.connector import SnowflakeConnector

if __name__ == "__main__":
    print("\nWorking on the main thread...\n")
    buff = SnowflakeConnector() #Creating/Initiating class
    filename = r"C:\Users\migue\Projects\snowflake\snowflake-python-connector\src\config\credentials.yaml" #credentials location
    buff.credentials_log_in(filename) #log in credentials
    buff.execute_query('SELECT * FROM SNOWFLAKE_SAMPLE_DATA.TPCDS_SF100TCL.CALL_CENTER;') #execute_query class method
