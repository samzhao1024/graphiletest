import psycopg2
import configparser

conf = configparser.ConfigParser()
conf.read('config.conf')
con = conf["pgsql"]

conn = psycopg2.connect(database=con["database"], user=con["user"], password=con["pwd"], host=con["host"], port=con["port"])
cursor = conn.cursor()