class user:
    def gk(self):
        import mysql.connector
        import msvcrt
        z=1
        h=0
        while z:
            if msvcrt.kbhit() and msvcrt.getch()==b'\x1b':
                return
            x=mysql.connector.connect(host='localhost',user='root',password='naan dhaan',database='sk')
            c=x.cursor()
            c.execute(f'select no,Q from quiz where no={z} ')  
            q=c.fetchone() 
            if not q:
                print("No more questions.")
                break
            print(q)
            c.execute(f'select A from quiz where no={z}')
            a=c.fetchone()[0]            
            while True:
                f=msvcrt.getch()
                if f==b'\x1b':
                   return
                if f==b'\r':
                    break
            x=input('answer:')
            if a.lower()==' '.join(x.split()).lower():
                print('you are right')
                h+=1
            else:
                print('not correct')
            z+=1  
        print('youre score in GK:',h)
    def arithmetic(self):   
        import mysql.connector
        import msvcrt
        z=1
        while z:
            if msvcrt.kbhit() and msvcrt.getch()==b'\x1b':
                return
            x=mysql.connector.connect(host='localhost',user='root',password='naan dhaan',database='sk')
            c=x.cursor()
            c.execute(f'select no,Q from arithmetic where no={z} ')  
            q=c.fetchone() 
            if not q:
                print("No more questions.")
                break
            print(q)
            c.execute(f'select A from arithmetic where no={z}')
            a=c.fetchone()[0]
            while True:
                f=msvcrt.getch()
                if f==b'\x1b':
                   return
                if f==b'\r':
                    break
            x=input('answer:')
            if a.lower()==' '.join(x.split()).lower():
                print('you are right')
                h+=1
            else:
                print('not correct')
            z+=1
        print('your score in Arithmetic:',h)
    def tech(self):
        import mysql.connector
        import msvcrt
        z=1
        h=0
        while z:
            if msvcrt.kbhit() and msvcrt.getch()==b'\x1b':
                return
            x=mysql.connector.connect(host='localhost',user='root',password='naan dhaan',database='sk')
            c=x.cursor()
            c.execute(f'select no,Q from tech where no={z} ')  
            q=c.fetchone() 
            if not q:
                print("No more questions.")
                break
            print(q)
            c.execute(f'select A from tech where no={z}')
            a=c.fetchone()[0]
            while True:
                f=msvcrt.getch()
                if f==b'\x1b':
                   return
                if f==b'\r':
                    break
            x=input('answer:')
            if a.lower()==' '.join(x.split()).lower():
                print('you are right')
                h+=1
            else:
                print('not correct')
                z+=1
        print('your score in Arithmetic:',h)
    def tamil(self):
        import mysql.connector
        import msvcrt
        z=1
        h=0
        while z:
            if msvcrt.kbhit() and msvcrt.getch()==b'\x1b':
                return
            x=mysql.connector.connect(host='localhost',user='root',password='naan dhaan',database='sk')
            c=x.cursor()
            c.execute(f'select no,Q from tamil where no={z} ')  
            q=c.fetchone() 
            if not q:
                print("No more questions.")
                break
            print(q)
            c.execute(f'select A from tamil where no={z}')
            a=c.fetchone()[0]
            while True:
                f=msvcrt.getch()
                if f==b'\x1b':
                   return
                if f==b'\r':
                    break
            x=input('answer:')
            if a.lower()==' '.join(x.split()).lower():
                print('you are right')
                h+=1
            else:
                print('not correct')
            z+=1
        print('your score in Tamil:',h)
