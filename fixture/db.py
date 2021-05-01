import pymysql


class Dbfixture:

    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self. user = user
        self.password = password
        self.connection = pymysql.connect(host=host, database=name, user=user, passwd=password)


    def get_group_list(self):
        cursor = self.connection.cursor()
        try:
            cursor.execute("select * from group_list")
        finally:
            cursor.close()



    def destroy(self):
        self.connection.close()