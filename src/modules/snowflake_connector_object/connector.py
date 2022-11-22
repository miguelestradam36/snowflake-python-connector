class SnowflakeConnector():
    """
    Attributes
    ---
    """
    username = '' # Snowflake account username
    password = '' # Snowflake account password
    account_id = '' # Snowflake account id
    warehouse = '' # Snowflake warehouse to connect to
    database = '' # Snowflake database to connect to
    schema = '' # Snowflake schema to connect to
    """
    Methods
    ---
    """
    def credentials_log_in(self, filepath:str)->None:
        """
        Class method
        Params: filepath (string [Required])
        Objective: Read credentials from YAML file and load into class for python-snowflake connection.
        """
        try:
            import yaml
            with open(filepath, 'r') as f:
                print("Reading credentials...")
                yaml_config = yaml.safe_load(f)
                self.username = yaml_config["defaults"]["snowflake"]["username"]
                self.password = yaml_config["defaults"]["snowflake"]["password"]
                self.warehouse = yaml_config["defaults"]["snowflake"]["warehouse"]
                self.database = yaml_config["defaults"]["snowflake"]["database"]
                self.schema = yaml_config["defaults"]["snowflake"]["schema"]
                self.account_id = yaml_config["defaults"]["snowflake"]["account_id"]
        except Exception as error:
            print("ERROR: {}".format(error))
        try:
            import snowflake.connector
            print("Connecting to Snowflake")
            self.conn = snowflake.connector.connect(
                user=self.username,
                password=self.password,
                account=self.account_id,
                warehouse=self.warehouse,
                database=self.database,
                schema=self.schema,
            )
        except snowflake.connector.errors.ProgrammingError as e:
            # default error message
            print("SNOWFLAKE CONNECTION ERROR: {}".format(e))
        except snowflake.connector.errors.DatabaseError as e:
            if db_ex.errno == 250001:
                print(f"Invalid username/password, please re-enter username and password...")
                # code for user to re-enter username & pass
            else:
                print("ERROR: {}".format(e))
        except Exception as error:
            print("ERROR: {}".format(error))

    def execute_query(self, query:str, shut_connection_after:bool=True)->list:
        """
        Class Method
        Params: query (string [Required]), shut_connection_after (bool [Not Required], default = True)
        Objective: Execute query under previously stablished connection
        """
        try:
            print("Querying sql...")
            engine_results = self.conn.cursor().execute(query)
            self.rows = engine_results.fetchall()
            return self.rows
        except Exception as error:
            print("ERROR: {}".format(error))
            self.conn.rollback()
        finally:
            if shut_connection_after:
                print("Closing connection...")
                self.conn.close()

    def manual_log_in(self, user:str, password:str, account:str, warehouse:str, database:str, schema:str):
        """
        Class method
        Params: user (string [Required]), 
            password (string [Required]), 
            account (string [Required]), 
            warehouse (string [Required]), database (string [Required]), schema (string [Required])
        Objective: Establish python-snowflake connection.
        """
        try:
            import snowflake.connector
            print("Connecting to Snowflake")
            self.conn = snowflake.connector.connect(
                user=user,
                password=password,
                account=account,
                warehouse=warehouse,
                database=database,
                schema=schema,
            )
        except snowflake.connector.errors.ProgrammingError as e:
            # default error message
            print("SNOWFLAKE CONNECTION ERROR: {}".format(e))
        except snowflake.connector.errors.DatabaseError as e:
            if db_ex.errno == 250001:
                print(f"Invalid username/password, please re-enter username and password...")
                # code for user to re-enter username & pass
            else:
                print("ERROR: {}".format(e))
        except Exception as error:
            print("ERROR: {}".format(error))

    def __init__(self, pandas:bool=True):
        """
        Function that initializes class
        ---
        Params: pandas (string [Not Required], default = True)
        Objective: Load pandas module into class as attribute, option given to avoid this.
        """
        if pandas:
            print("Including pandas Dataframe for ETL/ELT")
            self.pandas = __import__("pandas")