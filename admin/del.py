#!"C:/Users/HARSH PRASAD/anaconda3/python.exe"
import cgi
import mysql.connector
print("Content-type:text/html\n\n")

db=mysql.connector.connect(host="localhost",user="root",passwd="",db="kph")
form=cgi.FieldStorage()
a=int(form.getvalue('orderid'))
cur=db.cursor()
cur.execute("delete from orders where orderid=%d"%(a))
db.commit()
print('<meta HTTP-EQUIV="REFRESH" content="0; url=http://localhost/www/admin/orders.py">')
cur.close()
db.close()