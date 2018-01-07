import sqlite3
import os.path
import errno
#Timing
import datetime, time
from time import sleep
from random import randint
class database:   
    
    def __init__(self,name, location=None):
        
        if location != None:
            try: 
                os.makedirs(location)
            except OSError as e:
                if e.errno == errno.EEXIST:
                    print("Database exists")
                else:
                    raise
            self.location = location+'\\'+name+'.db'

        else:
            self.location = name+'.db'
        
        self.conn = sqlite3.connect(self.location)
        self.c = self.conn.cursor()
        
    def create_word_table(self,table_name):
        try:     
            self.c.execute('''CREATE Table '''+table_name+'''
                 (word TEXT) ''')
            self.conn.commit()
        except sqlite3.Error as e:
            print(str(e))
            
        self.close()
        
    def insert(self,table_name,data):
        self.connect()
        
        if type(data) is list:
            qmarks = ','.join(['%s']*len(data[0]))
            columns = ','.join(data[0].keys())
            search = ','.join(['?' for d in data[0].keys()])
            
        elif type(data) is dict:
            qmarks = ','.join(['%s']*len(data))
            columns = ','.join(data.keys())
            search = ','.join(['?' for d in data.keys()])
        
        if qmarks and columns and search:
            query = "INSERT INTO %s (%s) VALUES (%s)"%(table_name,columns,search)
            
            try:
                self.c.execute(query,list(data.values()))
                pass
            except sqlite3.Error as e:
                print('Database Insert Error: ',str(e))
                print('\n\nData: ',)
                
        self.conn.commit()
        
    def get_ranword(self):

        query1 = 'select count(*) from words;'
        self.c.execute(query1)
        count = self.c.fetchone()[0]
        
        random = randint(1,count)
        query2 = 'select * from words limit 1 offset '+str(random)+';'
        
        self.c.execute(query2)
        return self.c.fetchone()[0]
        
    
    def connect(self):
        self.conn = sqlite3.connect(self.location) 
        self.c = self.conn.cursor()

    def close(self):
        self.conn.commit()
        self.conn.close()






