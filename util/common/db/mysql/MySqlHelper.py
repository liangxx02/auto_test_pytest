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

    def insert_batch(self, sql, params=[]):
        """
        批量插入数据
        :param sql:
        :param params:
        :return:
        """
        conn = self.POOL.connection()
        cursor = conn.cursor()
        cursor.executemany(sql, params)
        commit(conn)

    def insert(self, sql, param=[]):
        """
        单个插入
        :param sql:
        :param param:
        :return:
        """
        conn = self.POOL.connection()
        cursor = conn.cursor()
        cursor.execute(sql, param)
        commit(conn)
