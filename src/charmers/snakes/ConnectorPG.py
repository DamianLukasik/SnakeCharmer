#-*- coding: utf8 -*-

class ConnectorPG:
  file = "conf.ini"
  def __init__(self, file=None):
    if file!=None:
      self.file = file
    self.loadFile()
    self.connectWithDatabase()
  def loadFile(self):
    try:
      with open(self.file) as f:
        import configparser
        config = configparser.ConfigParser()
        config.read(self.file)
        self.hostname = config['DATABASE']['host']
        self.username = config['DATABASE']['user']
        self.password = config['DATABASE']['passwd']
        self.database = config['DATABASE']['dbname']
        self.port = config['DATABASE']['port']
        f.close()
    except IOError:
      print("> File not accessible")
  def connectWithDatabase(self):
    try:
      if self.hostname is not None:
        import psycopg2
        print('> Connecting to the PostgreSQL database...')
        self.conn = psycopg2.connect( host=self.hostname, user=self.username, password=self.password, port=self.port, dbname=self.database )
        self.cur = self.conn.cursor()
    except (Exception, psycopg2.DatabaseError) as error:
      print(error)
  def ExecuteQuery(self, query):
    if self.cur is not None:
      self.cur.execute( query )
      return self.cur.fetchall()
  def ShowResultOfQuery(self,query):
    if self.cur is not None:
      result = self.ExecuteQuery(query)
      idx = 1
      for row in result:
        row_print = ""
        for elem in row:#polskie znaki!!!
          elem = str(elem).center(20)
          row_print += elem + "\t|\t"
        row_print = row_print.strip("\t|\t")
        print(""+str(idx).zfill(3) + " |\t" + row_print)
        idx +=1
  def __del__(self):
    if self.cur is not None:
      self.cur.close()
    if self.conn is not None:
      self.conn.close()
      print('> Database connection closed.')