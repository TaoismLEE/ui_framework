# -*- coding:utf-8 -*-
import pymysql  # MySQL server module
from lib.common.log import logger
from lib.common.parse_file import ParseYaml

# default DB config of Project
config_obj = ParseYaml('project.yml')
project_config = config_obj.get_yaml_dict()
db_host = project_config['MYSQL_DB_HOST']
db_port = int(project_config['MYSQL_DB_PORT'])
db_user = project_config['MYSQL_DB_USER_NAME']
db_password = project_config['MYSQL_DB_USER_PASSWORD']
db_database_name = project_config['MYSQL_DB_DBNAME']


class MYSQL(object):
    def __init__(self, host=db_host, port=db_port, user=db_user, pwd=db_password, db=db_database_name):
        self.host = host
        self.port = port
        self.user = user
        self.pwd = pwd
        self.db = db

    def __GetConnect(self):
        """
        得到连接信息
        返回: conn.cursor()
        """
        if not self.db:
            raise (NameError, "没有设置数据库信息")
        self.conn = pymysql.connect(host=self.host,
                                    port=self.port,
                                    user=self.user,
                                    password=self.pwd,
                                    database=self.db,
                                    charset="utf8")
        cur = self.conn.cursor()
        if not cur:
            raise (NameError, "连接数据库失败")
        else:
            return cur

    def exec_query(self, sql):
        """
        执行查询语句
        返回的是一个包含tuple的list，list的元素是记录行，tuple的元素是每行记录的字段
        """
        cur = self.__GetConnect()
        cur.execute(sql)
        res_list = cur.fetchall()

        # 查询完毕后必须关闭连接
        self.conn.close()
        return res_list

    def exec_non_query(self, sql):
        """
        执行非查询语句
        """
        cur = self.__GetConnect()
        cur.execute(sql)
        self.conn.commit()
        self.conn.close()
