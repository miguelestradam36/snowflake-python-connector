import threading
from modules.snowflake_connector_object.connector import SnowflakeConnector
#-----------------------------------------------------------
class SnowflakeTask(threading.Thread, SnowflakeConnector):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        #Tasks to be done
        print("\nStarting AWS threaded execution...\n")
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
