class SnowflakeConnector():
    username = ''
    password = ''
    account_id = ''
    warehouse = ''
    database = ''
    schema = ''
    def credentials_log_in(self, filepath:str)->None:
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

    def execute_query(self, query:str, once:bool=True)->list:
        try:
            print("Querying sql...")
            engine_results = self.conn.cursor().execute(query)
            rows = engine_results.fetchall()
            return rows
        except Exception as error:
            print("ERROR: {}".format(error))
            self.conn.rollback()
        finally:
            if once:
                print("Closing connection...")
                self.conn.close()