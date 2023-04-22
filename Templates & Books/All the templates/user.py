class User:
    
    def __init__(self,Id):
        self.Id = Id
     
    @staticmethod    
    def login(username,password):
        import sqlite3
        conn = sqlite3.connect("mydb.db")
        c = conn.cursor()
        c.execute(""" 
                  select Id,Name,Role from user
                  where UserName = :uName
                  and Password = :pass
                  """,{'uName':username , 'pass':password})
        result = c.fetchone()
        
        if not result:
            return {'IsExist' : False}
        else:
            return {'IsExist' : True , 'Id': result[0] , 'Name': result[1], 
                    'Role': result[2]}
        conn.commit()
        conn.close()
    
    def register():
        pass
    

