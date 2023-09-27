
import psycopg2
conn.close()
breake

conn = psycopg2.connect(dbname='postgres',
                              user='postgres',
                              password='1705',
                              host='127.0.0.1',
                              port='5432')
conn.autocommit = True
cursor = conn.cursor()
sql = '''CREATE DATABASE hh''';
name = 'h'
cursor.execute('''DROP DATABASE IF EXISTS hh''');
cursor.execute(f'''CREATE DATABASE {name};''');
conn.close()
