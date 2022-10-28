class SnowflakeConnector():
    username = ''
    password = ''
    account_id = ''
    warehouse = ''
    database = ''
    schema = ''
    def credentials_log_in(self)->None:
        import snowflake.connector
        print("Connecting to Snowflake")
        self.conn = snowflake.connector.connect(
            user=self.username,
            password=self.password,
            account=self.account_id,
            warehouse=self.warehouse,
        )

        self.cursor = self.conn.cursor()

    @property
    def execute_query(self):
        return self.cursor.fetchall()

    @execute_query.setter
    def execute_query(self, query:str)->None:
        try:
            self.cursor().execute(query)
        except Exception as error:
            self.conn.rollback()

    def read_file_values(self, filepath:str)->None:
        import yaml
        import boto3
        import yaml
        from yaml.loader import SafeLoader
        with open(filepath, 'r') as f:
            print("Reading credentials...")
            yaml_config = yaml.safe_load(f)
            self.username = yaml_config["defaults"]["snowflake"]["username"]
            self.password = yaml_config["defaults"]["snowflake"]["password"]
            self.warehouse = yaml_config["defaults"]["snowflake"]["warehouse"]
            self.database = yaml_config["defaults"]["snowflake"]["database"]
            self.schema = yaml_config["defaults"]["snowflake"]["schema"]
            self.account_id = yaml_config["defaults"]["snowflake"]["account_id"]