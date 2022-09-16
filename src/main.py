import threading
import yaml, os
from modules.snowflake_connector_object.connector import SnowflakeConnector
#-----------------------------------------------------------
#-------------  Variables                          ---------
#-----------------------------------------------------------

fullpath = os.path.join(os.path.dirname(__file__), "config\\credentials.yaml")

with open(fullpath, 'r') as file:
    global yaml_config
    yaml_config = yaml.safe_load(file)

username = yaml_config["defaults"]["snowflake"]["username"]
password = yaml_config["defaults"]["snowflake"]["password"]
warehouse = yaml_config["defaults"]["snowflake"]["warehouse"]
database = yaml_config["defaults"]["snowflake"]["database"]
schema = yaml_config["defaults"]["snowflake"]["schema"]
host = yaml_config["defaults"]["snowflake"]["host"]
account_id = yaml_config["defaults"]["snowflake"]["account_id"]

#-----------------------------------------------------------
class SnowflakeTask(threading.Thread, SnowflakeConnector):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        print("\nStarting Snowflake threaded execution...\n")
        try:
            # TODO: Insert your code here
            pass
        except Exception as error:
            pass

#-----------------------------------------------------------
if __name__ == "__main__":
    print("\nWorking on the main thread...\n")

    #Creating snowflake threaded execution, thread which will later join the main thread
    snowflake_services= SnowflakeTask()
    snowflake_services.start()
    snowflake_services.join()
    del snowflake_services
