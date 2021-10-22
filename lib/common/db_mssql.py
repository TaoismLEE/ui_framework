# -*- coding:utf-8 -*-
import pymssql  # SQL Server module
from lib.common.parse_file import ParseYaml

# default DB config of Project
config_obj = ParseYaml('project.yml')
project_config = config_obj.get_yaml_dict()
host = project_config['MSSQL_DB_HOST']
user = project_config['MSSQL_DB_USER_NAME']
pwd = project_config['MSSQL_DB_USER_PASSWORD']
db = project_config['MSSQL_DB_DBNAME']


class MSSQL:
    def __init__(self, host=host, user=user, pwd=pwd, db=db):
        self.host = host
        self.user = user
        self.pwd = pwd
        self.db = db

    def __GetConnect(self):
        """
        得到连接信息
        返回: conn.cursor()
        """
        if not self.db:
            raise(NameError, "没有设置数据库信息")
        self.conn = pymssql.connect(host=self.host, user=self.user, password=self.pwd, database=self.db, charset="utf8")
        cur = self.conn.cursor()
        if not cur:
            raise(NameError, "连接数据库失败")
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
