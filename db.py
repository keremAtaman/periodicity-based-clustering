import psycopg2
import pandas as pd

def connect(host, port, user, password, database, schema):
   conn = psycopg2.connect(host = host,
        port = port,
        user=user,
        password=password,
        database = database,
        options=str("-c search_path="+schema)
        )
   return conn

def get_customer_data(conn, customer_id, sql_query):
   sql_query = sql_query.replace(r'$P{rqstr_party_id}',str(customer_id))
   result = pd.read_sql(sql_query,conn,parse_dates={'dates': '%y-%m-%d %H:%M:%S'})
   return result