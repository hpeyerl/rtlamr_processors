import sys
import json
import MySQLdb

u="rtluser"
p="rtlpass"

conn = MySQLdb.connect(host='localhost', user=u, passwd=p, db='rtlamr')
conn.autocommit(True)

db = conn.cursor()

while 1:
    try:
        line = sys.stdin.readline()
    except KeyboardInterrupt:
        break

    if not line:
        break

    rec = json.loads(line)
    print("Time: {0} Meter ID: {1} Consumption: {2}".format(rec["Time"], rec["Message"]["ID"], rec["Message"]["Consumption"]))
    # create table meters (t timestamp default current_timestamp, id varchar(20),type int, tamperphy int, tamperenc int, consumption int);
    v = rec["Message"]
    sql='insert into meters values (current_timestamp,{0},{1},{2},{3},{4})'.format(v["ID"],v["Type"],v["TamperPhy"],v["TamperEnc"],v["Consumption"])
    print(sql)
    db.execute(sql)
