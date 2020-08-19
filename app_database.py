import pymysql

#set connection
conn=pymysql.connect(database="classicmodels",user="root",password="abc123")
cursor=conn.cursor()


# fetch the results using fetchall and save the headers as  a list , to be used further when creating the GUI
def headers_list(db_name,table_name):
    #create the string query and execute it
    query_columns_names="SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = '{}' and table_schema = '{}'".format(table_name,db_name)
    cursor.execute(query_columns_names)
    lista_headers=[]
    for c in cursor.fetchall():
        lista_headers.append(c[0])
    print("Headers List: ",lista_headers)
    return lista_headers

headers_list("classicmodels","employees")


#check how many rows are in a table, helps in creating the GUI table
def n_rows(table_name):
    count_rows="select count(*) from {}".format(table_name)
    cursor.execute(count_rows)
    # print(cursor.fetchone()[0])
    return cursor.fetchone()[0]

def n_columns(table_name):
    print("columns: ",headers_list(table_name).__sizeof__())
    return headers_list(table_name).__sizeof__()

# n_columns("employees")

#Returns all the rows as List of list* where each list* is a row from the db
def rows(table_name):
    cursor.execute("select * from {}".format(table_name))
    # for c in cursor.fetchall():
        # print(list(c))
    list_rows=[list(c) for c in cursor.fetchall()]
    print(list_rows)
    return list_rows

# rows("employees")

# print("Len headers: ",len(headers_list("employees")))
# print("len riga: ",len(rows("employees")[0]))

