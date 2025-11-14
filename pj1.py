class admin:
    # def login(self):
        # import mysql.connector
        # x=mysql.connector.connect(host='localhost',user='root',password='naan dhaan',database='sk')
        # c=x.cursor()    
        # x=input(f'sign up/sign in:').lower()
        # if x=='sign up':
            # e=input('username:')
            # c.execute(f'select userid from users')             
            # if e in q=c.fetchone():
                # print('not available/already existed')
                
            # r=input('password:')
            
         # x=mysql.connector.connect(host='localhost',user='root',password='naan dhaan',database='sk')
            # c=x.cursor()
            # c.execute(f'')  
            # q=c.fetchone() 
    def add(self):
        import mysql.connector
        x=mysql.connector.connect(host='localhost',user='root',password='naan dhaan',database='sk')
        c=x.cursor()
        e=input('enter which db to access:')
        y=input('enter question')
        z=input('enter answer')
        c.execute(f"insert into {e}(Q,A) values('{y}','{z}')")  
        q=c.fetchone() 
        x.commit()
        

#s.admin()
    def delete(self):
        import mysql.connector
        x=mysql.connector.connect(host='localhost',user='root',password='naan dhaan',database='sk')
        c=x.cursor()
        e=input('enter which db to access:')
        z=input('enter Answer from particular question delete: ')
        c.execute(f"delete from {e} where A='{z}'")  
        q=c.fetchone() 
        x.commit()
 
        
        
 