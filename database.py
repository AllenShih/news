import psycopg2

class Database:
    #" dbname='database1' user='postgres' password='postgres123' host='localhost' port='5432' "
    def __init__(self,dbname):
        self.conn=psycopg2.connect(dbname)
        self.cur=self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS news (newspaper text, title text, time text, category text, url text, city text, sector text, highway text, landmark text, road text,comb_add text,hw_num text,coor text, address_coor text)")
        self.cur.execute("CREATE TABLE IF NOT EXISTS locations (newspapaer text, title text, time text, location text, coordinate text)")
        self.conn.commit()
        # , city text, sector text, highway text, landmark text, road text,comb_add text,hw_num text,coor text, address_coor text

    def insert(self,newspaper,title,time,category,url,city,sector,highway,landmark,road,comb_add,hw_num,coor,address_coor):
        self.cur.execute("INSERT INTO news VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)" ,(newspaper,title,time,category,url,city,sector,highway,landmark,road,comb_add,hw_num,coor,address_coor))
        self.conn.commit()
        #,city,sector,highway,landmark,road,comb_add,hw_num,coor,address_coor
        #,city,sector,highway,landmark,road,comb_add,hw_num,coor,address_coor

    def insert_location(self, newspaper, title, time, location, coordinate):
        self.cur.execute("INSERT INTO locations VALUES (%s,%s,%s,%s,%s)", (newspaper,title,time,location,coordinate))
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

    def close(self):
        self.cur.close()
        self.conn.close()

class Database2:
    #" dbname='database1' user='postgres' password='postgres123' host='localhost' port='5432' "
    def __init__(self,dbname):
        self.conn=psycopg2.connect(dbname)
        self.cur=self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS news_1 (title text, highway text,comb_add text,hw_num text,coor text, address_coor text)")
        self.conn.commit()

    def insert(self,title,highway,comb_add,hw_num,coor,address_coor):
        self.cur.execute("INSERT INTO news_1 VALUES (%s,%s,%s,%s,%s,%s)" ,(title,highway,comb_add,hw_num,coor,address_coor))
        self.conn.commit()

class Database_test:
    #" dbname='database_test' user='postgres' password='postgres123' host='localhost' port='5432' "
    def __init__(self,dbname):
        self.conn=psycopg2.connect(dbname)
        self.cur=self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS blackout (newspaper text, title text, time text, category text, url text)")
        self.conn.commit()

    def insert(self,newspaper,title,time,category,url):
        self.cur.execute("INSERT INTO blackout VALUES (%s,%s,%s,%s,%s)" ,(newspaper,title,time,category,url))
        self.conn.commit()
    
    def search(self,newspaper="",title="",time="",category="",url=""):
        self.cur.execute("SELECT * FROM blackout WHERE newspaper=%s OR title=%s OR time=%s OR category=%s OR url=%s", (newspaper,title,time,category,url))
        rows=self.cur.fetchall()
        return rows