from __future__ import print_function

import cx_Oracle

# Connect as user "hr" with password "welcome" to the "orclpdb1" service running on this computer.
#sys/password@//localhost:1521/XE as sysdba
dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='XE') # if needed, place an 'r' before any parameter in order to address special characters such as '\'.
conn = cx_Oracle.connect(user='hr', password='password', dsn=dsn_tns) # if needed, place an 'r' before any parameter in order to address special characters such as '\'. For example, if your user name contains '\', you'll need to place 'r' before the user name: user=r'User Name'

c = conn.cursor()
c.execute("select * from all_tables") # use triple quotes if you want to spread your query across multiple lines
for row in c:
    print (row[0], '-', row[1]) # this only shows the first two columns. To add an additional column you'll need to add , '-', row[2], etc.
conn.close()
