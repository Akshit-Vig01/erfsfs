import pymysql


def Connect():
    c = pymysql.connect(
        host='localhost',
        user='root',
        password='system',
        database='pythonproject2'


    )
    return c


def getCatName():
    conn = Connect()
    cr = conn.cursor()
    q = f'select name from category'
    cr.execute(q)
    result = cr.fetchall()
    lst = []
    for i in result:
        lst.append(i[0])
    return lst




