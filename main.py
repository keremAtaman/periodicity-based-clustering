import db
import yaml
import statsmodels.api as sm
import pandas as pd
import P4J

stream = open("config.yaml", 'r')
config = yaml.safe_load(stream)

stream = open(config['database_config'],'r')
database_config = yaml.safe_load(stream)

conn = db.connect(
    database_config['host'],
    database_config['port'],
    database_config['user'],
    database_config['password'],
    database_config['database'],
    database_config['schema']
)

# TODO: get the list of customers

customer_list = [239]

# TODO: for each customer in customer_list, get data
for customer in customer_list:
    customer_data = db.get_customer_data(conn,customer,database_config['get_customer_data'])
    customer_data['dates'] = pd.to_datetime(customer_data['dates'])
    customer_data = customer_data.set_index('dates').asfreq('d')
    # TODO: split data into activity and trade
    activity_decomposition = sm.tsa.seasonal_decompose(customer_data[["activitied"]],model = 'additive')
    trade_decomposition = sm.tsa.seasonal_decompose(customer_data[["traded"]],model = 'additive')
    
    print("decomposed")
    

conn.close()