import pyodbc
import pandas as pd
import sqlite3

class SQLDB:

    def __init__(self, server="(local)",
                 integrated_security = True,
                 driver = "{ODBC Driver 13 for SQL Server}",
                 dbname = "AdventureWorksDW2017",
                 username = "dummy",
                 password = "dummy"):
        self.server = server
        self.integrated_security = integrated_security
        self.driver = driver
        self.dbname = dbname
        self.username = username
        self.password = password

        self.connstring = "Driver={0};Server={1}; Database={2}; Trusted_Connection=yes;".format(self.driver, self.server, self.dbname)

        if not integrated_security:
            self.connstring += "uid=" + self.username + ";" + \ 
            "pwd=" + self.password + ";"

    def get_db_data(self, sqlstatement):
        """run query and return results as a dataframe"""

        conn = pyodbc.connect(self.connstring)

        result = pd.read_sql(sqlstatement, conn)

        conn.close()

        return result