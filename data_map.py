#!/usr/bin/python
import csv
from pprint import pprint

exist = csv.DictReader(file("exist.csv"))
exist_data={}
for e in exist:
    exist_data[e['id']]=e['move_id']

todo=[]
to_update={}
missing= csv.DictReader(file("missing.csv"))
for m in missing:
    move_id = exist_data.get(m['id'],False)
    if move_id:
        todo.append(move_id)
        to_update[m['id']]=move_id

print "SQL for delete"
sql="delete from account_move where id not in (%s) "  %  ','.join(todo)

print sql

print "Sql for update"
update = open("update.sql","w")
for k,v in to_update.items():
    update.write("update stock_picking set move_id=%s where id=%s;\n" %(v,k))
update.close()
