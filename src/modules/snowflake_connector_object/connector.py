class SnowflakeConnector():
    def __init__(self):
        self.auto_install()

    def auto_install(self):
        """
        Setter method, which can be compared to: 
            pip install -r requirements.txt

        param -> file_path: Location of requirements.txt file
        param -> file_path: string      
        """
        import os
        location = os.path.join(os.path.dirname(__file__), 'config/requirements.txt')
        
    def credentials_log_in(self, username:str, hostname:str, account:str, warh:str, dbname:str, schema:str)->None:
        """
        Setter method, which can be compared to: 
            pip install -r requirements.txt

        param -> file_path: Location of requirements.txt file
        param -> file_path: string      
        """
        import snowflake.connector
        ctx = snowflake.connector.connect(
            user="<username>",
            host="<hostname>",
            account="<account_identifier>",
            warehouse="test_warehouse",
            database="test_db",
            schema="test_schema"
        )
    @property
    def con_cursor(self):
        """
        Getter method, which is used to define the config file path.
        """
        return self.requirements_location_

    @con_cursor.setter
    def con_cursor(self, renewal:bool=False)->None:
        """
        Setter method, which can be compared to: 
            pip install -r requirements.txt

        param -> file_path: Location of requirements.txt file
        param -> file_path: string      
        """
        print('Checking system...')


    def __del__(self):
        pass