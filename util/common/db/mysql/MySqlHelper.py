import pymysql
from DBUtils.PooledDB import PooledDB


def commit(conn):
    """
    提交事务
    :param conn:
    :return:
    """
    conn.commit()
    # 这里close不是真的close了，是还回去了
    conn.close()


class MysqlHelper(object):
    def __init__(self, user_name, password, database, host, port=3306):
        print('init user_name is ', user_name, ' password is ', password, ' database is ', database, ' host is ', host,
              ' port is ', port)
        self.POOL = PooledDB(
            creator=pymysql,  # 使用链接数据库的模块
            maxconnections=100,  # 连接池允许的最大连接数，0和None表示没有限制
            mincached=100,  # 初始化时，连接池至少创建的空闲的连接，0表示不创建
            maxcached=100,  # 连接池空闲的最多连接数，0和None表示没有限制
            maxshared=3,
            # 连接池中最多共享的连接数量，0和None表示全部共享，ps:其实并没有什么用，因为pymsql和MySQLDB等模块中的threadsafety都为1，所有值无论设置多少，_maxcahed永远为0，所以永远是所有链接共享
            blocking=True,  # 链接池中如果没有可用共享连接后，是否阻塞等待，True表示等待，False表示不等待然后报错
            setsession=[],  # 开始会话前执行的命令列表
            ping=0,  # ping Mysql 服务端，检查服务是否可用
            host=host,
            port=port,
            user=user_name,
            password=password,
            database=database,
            charset='utf8'
        )

    def insert_batch(self, sql, param=[]):
        """
        批量插入数据
        :param sql:
        :param param:
        :return:
        """
        return self.default_executemany(sql, param)

    def insert(self, sql, param=[]):
        """
        单个插入
        :param sql:
        :param param:
        :return:
        """
        return self.default_execute(sql, param)

    def delete(self, sql, param=[]):
        """
        删除数据
        :param sql:
        :param param:
        :return:
        """
        return self.default_execute(sql, param)

    def update(self, sql, param=[]):
        """
        更新
        :param sql:
        :param param:
        :return:
        """
        return self.default_execute(sql, param)

    def query(self, sql, param=[]):
        """
        查询数据
        :param sql:
        :param param:
        :return:
        """
        conn = self.POOL.connection()
        cursor = conn.cursor()
        cursor.execute(sql)
        results = cursor.fetchall()
        return results

    def default_execute(self, sql, param=[]):
        if param:
            result = self.execute_with_param(sql, param)
        else:
            result = self.execute(sql)
        return result

    def default_executemany(self, sql, param=[]):
        if param:
            result = self.executemany_with_param(sql, param)
        else:
            result = self.executemany(sql)
        return result

    def execute(self, sql):
        conn = self.POOL.connection()
        cursor = conn.cursor()
        result = cursor.execute(sql)
        commit(conn)
        return result

    def execute_with_param(self, sql, param=[]):
        conn = self.POOL.connection()
        cursor = conn.cursor()
        result = cursor.execute(sql, param)
        commit(conn)
        return result

    def executemany(self, sql):
        conn = self.POOL.connection()
        cursor = conn.cursor()
        result = cursor.executemany(sql)
        commit(conn)
        return result

    def executemany_with_param(self, sql, param=[]):
        conn = self.POOL.connection()
        cursor = conn.cursor()
        result = cursor.executemany(sql, param)
        commit(conn)
        return result


def get_single_insert_sql(table_name, table_columns):
    """
    获取插入单挑数据的sql语句
    :param table_name: 表名
    :param table_columns: 表字段数组
    :return:
    """
    return get_insert_sql(table_name, table_columns)


def get_multi_insert_sql(table_name, table_columns):
    """
    获取批量插入数据的sql
    :param table_name: 表名
    :param table_columns: 表字段数组
    :return:
    """
    return get_insert_sql(table_name, table_columns, False)


def get_insert_sql(table_name, table_columns, is_single=True):
    """
    根据表名和表的列属性，自动封装insert语句
    :param is_single: 是否是单挑数据插入
    :param table_name: 表名
    :param table_columns: 表的各列名数组，如：['id', 'name', 'age']
    :return:
    """
    column_marks = ",".join(["%s" for i in range(len(table_columns))])
    table_columns_marks = ",".join(table_columns)
    value_str = 'VALUES'
    if is_single:
        value_str = 'VALUE'
    sql = "INSERT IGNORE INTO %s (%s) %s (%s)" % \
          (table_name, table_columns_marks, value_str, column_marks)
    return sql
