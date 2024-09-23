import pandas as pd
import pyodbc as db
import configparser
import  json
class SQL:
    def __init__(self):
        conf=configparser.ConfigParser()
        conf.read("webconfig/webconfig.cs")
        driver=conf.get("Cadena","Driver")
        server=conf.get("Cadena","Server")
        database=conf.get("Cadena","Database")
        self.Cadena="Driver={0};server={1};database={2};Trusted_Connection=yes"\
            .format(driver,server,database)
    def listarHTML(self,consulta):
        cn= db.connect(self.Cadena)
        df=pd.read_sql_query(consulta,cn)
        data=df.to_html(index=False)
        return data
    def listarJSON(self,consulta):
        cn= db.connect(self.Cadena)
        df=pd.read_sql_query(consulta,cn)
        data=df.to_json(orient="records")
        return json.loads(data)

