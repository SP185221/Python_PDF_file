from reportlab.platypus import SimpleDocTemplate
from reportlab.lib.pagesizes import A4
from reportlab.platypus import Table
from reportlab.platypus import TableStyle
from reportlab.lib import colors
import mysql.connector;

connection1 = mysql.connector.connect( host = "localhost", database = "mydb",  user= "root",  password="root" )

cursor = connection1.cursor()
cursor.execute('select * from Global Where Emp_id = "ID10102"')
#cursor.execute('select * from Global')
rows = cursor.fetchone()
#rows = cursor.fetchall()
#print(rows)
cursor.close()
connection1.close()

data = [
    ['EMP ID  ', 'EMP Name ', 'EMP Address', 'EMP Mobile' , 'EMP Country', 'EMP Status'],
    ]
#for row in rows:
data.append(rows)
    
print(data)
    
    
fileName = 'Employee Table.pdf'
pdf = SimpleDocTemplate( fileName, pagesize= A4 )
table = Table(data)
elems = []
elems.append(table)
ts = TableStyle(
    [
    ('BOX',(0,0),(-1,-1),2,colors.black),

    ('LINEBEFORE',(2,1),(2,-1),2,colors.red),
    ('LINEABOVE',(0,2),(-1,2),2,colors.green),

    ('GRID',(0,1),(-1,-1),2,colors.black),
    ]
)
table.setStyle(ts)
print("PDF Generated to file Location")
pdf.build(elems)
