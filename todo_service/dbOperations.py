import psycopg2

class dbOperations():
    def insert(con,sql):
        cur = con.cursor()
        try:
            cur.execute(sql)
            con.commit()
            insertedData = cur.fetchone()[0]
            
        except (Exception, psycopg2.DatabaseError) as error:
            print("Error: %s" % error)
            con.rollback()
            cur.close()
            return " Error to insert data"
        cur.close()
        return insertedData
    
    def update(con,sql,id):
        cur = con.cursor()
        try:
            cur.execute(sql)
            con.commit()
            idUpdatedData = cur.fetchone()[0]
        except (Exception, psycopg2.DatabaseError) as error:
            print("Error: %s" % error)
            con.rollback()
            cur.close()
            return f"ID:{id} not found to update"
        cur.close()
        return f"ID:{idUpdatedData} updated"
    
    def select(con,sql):
        cur = con.cursor()
        try:
            cur.execute(sql)
            return cur.fetchall()
        except (Exception, psycopg2.DatabaseError) as error:
            print("Error: %s" % error)
            con.rollback()
            cur.close()
            return 1
        cur.close()
        
    def delete(con,sql,id):
        cur = con.cursor()
        try:
            cur.execute(sql)
            con.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print("Error: %s" % error)
            con.rollback()
            cur.close()
            return f"ID:{id} not found to delete"
        cur.close()
        return f"ID:{id} deleted"
    