# python-oracledb 라이브러리 connect 샘플
import pymysql
conn = None
def dbconnect():
    try:
        global conn
        conn = pymysql.connect(host='127.0.0.1', user='root', password='990809', port=55555, db='opotato', charset='utf8')
    except:
        print("can't connect db")
        return False

def searchdata():
    cur = conn.cursor()
    sql = 'select * from camera_table'
    cur.execute(sql)
    results = cur.fetchall()
    print(results)

def insertdata(data):
    try:
        cur = conn.cursor()
        sql = "INSERT INTO camera_table (camera_id, time) VALUES (%s, %s)"
        cur.execute(sql, data)
        conn.commit()
        cur.close()
    except:
        print("can't connect db")
        return False
def main():
    print(conn)
    searchdata()
    conn.close()


