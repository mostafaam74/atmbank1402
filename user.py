import sqlite3
class karbaran:
    def user6840():
        conn=sqlite3.connect('data_card.db')
        c=conn.cursor()
        c.execute("select* from user where sh_kart='6037997391690337' ")
        x=c.fetchall()
        for i in x:
            c=i[0],i[1],i[2],i[3],i[4]
            return(c)
        conn.commit()
        conn.close()
    def user1278():
        conn=sqlite3.connect('data_card.db')
        c=conn.cursor()
        c.execute("select* from user where sh_kart='6219861925027848' ")
        x=c.fetchall()
        for i in x:
            c=i[0],i[1],i[2],i[3],i[4]
            return(c)
        conn.commit()
        conn.close()
    def user1354():
        conn=sqlite3.connect('data_card.db')
        c=conn.cursor()
        c.execute("select* from user where sh_kart='6037697689563531' ")
        x=c.fetchall()
        for i in x:
            c=i[0],i[1],i[2],i[3],i[4]
            return(c)
        conn.commit()
        conn.close()