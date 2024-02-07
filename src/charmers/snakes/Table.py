#-*- coding: utf8 -*-

def query(columns,table,orderby=None,where=None,conf=None):
    if conf!=None:
        from snakes.ConnectorPG import ConnectorPG
        from snakes import Load_Args
    else:
        from ConnectorPG import ConnectorPG
        import Load_Args
    import sys

    args = [0]
    args[0] = ["l:","-l","Limit=",10]

    if len(sys.argv)>1:
        args = Load_Args.load_args(sys.argv[1:],args)

    # limit of rows - args[0]
    if len(args[0])>1:
        limit = args[0][3]
    else:
        limit = args[0][0]

    if limit=='':
        limit=10

    if orderby!=None:
        orderby = ' ORDER BY '+str(orderby)+' '
    else:
        orderby = ' '
    
    if where!=None:
        where = ' WHERE '+str(where)+' '
    else:
        where = ' '

    #connect with database
    if conf!=None:
        con = ConnectorPG(conf)
    else:
        con = ConnectorPG()
    query = 'SELECT '+str(columns)+' FROM '+str(table)+str(where)+str(orderby)+' limit '+str(limit)
    con.ShowResultOfQuery(query)