import mysql.connector
#連線到資料庫
con=mysql.connector.connect(
    user="root",
    password="1234",
    host="localhost",
    database="mydb"
)

print("資料庫連線成功")
#建立cursor物件,來對資料庫下sql指令
cursor=con.cursor()
#取得多筆資料
cursor.execute("select * from product")
data=cursor.fetchall()

#逐一取得資料
for row in data:
    print(row)
#更新資料
# productName="美式"
# productId=1
# cursor.execute("update product set name=%s where id=%s",(productName,productId))
# con.commit()

con.close()

#git@github.com:JasperC61/python.git