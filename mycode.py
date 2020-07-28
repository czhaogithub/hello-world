import pymysql
from sqlalchemy import create_engine
import sqlalchemy
import pandas as pd

cnx = create_engine('mysql+pymysql://analyst:badsecuritykills@localhost:3306/items')

pd.io.sql.execute("""CREATE TABLE books( \
id                               VARCHAR(40) PRIMARY KEY NOT NULL \
,author                          VARCHAR(255) \
,copies                          INT)""", cnx)

df = pd.DataFrame({
    "author": ["Alice", "Bob", "Charlie"],
    "copies": [2, "", 7, ],},
    index = [1, 2, 3])
    #Notice that one of these has the wrong data type!

df.to_sql(name='books',con=cnx,if_exists='append',index=False)