import pj1 
import pj2 
import mysql.connector
class main:
    def __init__(self):
        self.h=pj1.admin()
        self.n=pj2.user()
    def o(self):
        x=mysql.connector.connect(host='localhost',user='root',password='naan dhaan',database='sk')
        c=x.cursor()
        m=int(input('enter 1 or 2 for admin or user:'))
        match m:
            case 1:
                d=input('usercode:')
                c.execute('select admincode from admin where password="naan dhaan"')
                if d==c.fetchone()[0]:
                    f=input('password:') 
                    c.execute('select password from admin where admincode="santhoshk"')
                    if f==c.fetchone()[0]:
                        x=int(input('enter 1 or 2 for add or delete:'))
                        match x:
                            case 1:
                                self.h.add()
                            case 2:
                                self.h.delete()
                            case _:
                                print('nee avalothaan panna') 
                    else:
                        print('wrong password')
                else:
                    print('wrong usercode')
                       
            case 2:
                x=int(input('enter 1 or 2 or 3 or 4 for gk or arithmetic or tech or tamil:'))
                match x:
                    case 1:
                        self.n.gk()
                    case 2:
                        self.n.arithmetic()
                    case 3:
                        self.n.tech()
                    case 4:
                        self.n.tamil()
                    case _:
                        print('invalid')
            case _:
                print('onnum illa')
k=main()
k.o()
                