import psycopg2

class Database:
    #" dbname='database1' user='postgres' password='postgres123' host='localhost' port='5432' "
    def __init__(self,dbname):
        self.conn=psycopg2.connect(dbname)
        self.cur=self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS news (newspaper text, title text, time text, category text, url text, city text, sector text, highway text, landmark text, road text,comb_add text,hw_num text,coor text)")
        self.conn.commit()
        

    def insert(self,newspaper,title,time,category,url,city,sector,highway,landmark,road,comb_add,hw_num,coor):
        self.cur.execute("INSERT INTO news VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)" ,(newspaper,title,time,category,url,city,sector,highway,landmark,road,comb_add,hw_num,coor))
        self.conn.commit()

    def view(self):
        self.cur.execute("SELECT * FROM news")
        rows=self.cur.fetchall()
        return rows

    def search(self,newspaper="",title="",time="",category="",url=""):
        self.cur.execute("SELECT * FROM news WHERE newspaper=%s OR title=%s OR time=%s OR category=%s OR url=%s", (newspaper,title,time,category,url))
        rows=self.cur.fetchall()
        return rows

    def delete(self,title):
        self.cur.execute("DELETE FROM news WHERE title=%s",(title,))
        self.conn.commit()

    def update(self,newspaper,title,time,category,url):
        self.cur.execute("UPDATE news SET newspaper=?, title=?, time=?, category=? WHERE url=?",(newspaper,title,time,category,url))
        self.conn.commit()

class Database2:
    #" dbname='database1' user='postgres' password='postgres123' host='localhost' port='5432' "
    def __init__(self,dbname):
        self.conn=psycopg2.connect(dbname)
        self.cur=self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS news_1 (title text, highway text,comb_add text,hw_num text,coor text)")
        self.conn.commit()

    def insert(self,title,highway,comb_add,hw_num,coor):
        self.cur.execute("INSERT INTO news_1 VALUES (%s,%s,%s,%s,%s)" ,(title,highway,comb_add,hw_num,coor))
        self.conn.commit()