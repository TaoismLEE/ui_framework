# -*- coding:utf-8 -*-

import csv  # excel lib
import yaml  # yaml lib
from configparser import ConfigParser  # ini lib
from xml.etree.ElementTree import ElementTree  # xml lib
from lib.common.log import logger
from conf.global_var import PROJECT_PATH


class ParseIni(object):
    def __init__(self, file_name):
        """
        Constructor
        :param file_name: name of xxx.ini config file
        """
        self.cf = ConfigParser()
        self.file_path = PROJECT_PATH + u'/conf/' + file_name
        self.cf.read(self.file_path, encoding='UTF-8')

    def get_section_item(self, section_name):
        return dict(self.cf.items(section_name))

    def get_option_value(self, section_name, option_name):
        return self.cf.get(section_name, option_name)


class ParseYaml(object):
    def __init__(self, file_name):
        """
        Constructor
        :param file_name: name of xxx.yml config file
        """
        self.file_path = PROJECT_PATH + u'/conf/' + file_name

    def get_yaml_dict(self):
        f = open(self.file_path, 'r', encoding='utf-8')
        data_dict = yaml.load(f.read())
        return data_dict


class ParseXml:
    def __init__(self, file_name):
        """
        Constructor
        :param file_name: full path of xxx.xml file
        """
        self.file_name = file_name
        try:
            self.tree = ElementTree(file=self.file_name)
            self.root = self.tree.getroot()
        except Exception as e:
            logger.error(e)

    def get_attr_values(self, node_path, attr_name):
        """
        get the attribute value of target nodes
        :param node_path: node path where attribute locates
        :param attr_name:  attribute name
        :return: list of attribute values
        """
        try:
            attr_values = []
            nodes = self.root.findall(node_path)

            if len(nodes) > 0:
                for node in nodes:
                    attr_values.append(node.get(attr_name))

            return attr_values

        except Exception as e:
            logger.error(e)

    def get_node_text(self, parent_node, target_node):
        """
        get one or more child node text under the same parent node
        :param parent_node: parent node
        :param target_node: target node
        :return: dic of target node: key=tag name of parent node, value=text content of target node
        """
        try:
            dic_node_value = {}
            for nd in self.root.iter(parent_node):
                dic_node_value[nd.get('name')] = nd.find(target_node).text
            return dic_node_value
        except Exception as e:
            logger.error(e)

    def get_nodes_text_by_parent_name(self, parent_name, target_node):
        """
        get text list of target nodes
        :param parent_name: 'name' attribute value of parent node
        :param target_node: target node
        :return: text list of target nodes
        """
        try:
            list_text = []
            for nd in self.root.findall(".//*[@name='" + parent_name + "']//" + target_node):
                list_text.append(nd.text)
            return list_text
        except Exception as e:
            logger.error(e)

    def get_nodes(self, target_node):
        """
        get node obj
        :param target_node: target node
        :return: list of node obj
        """
        try:
            return self.root.findall(".//" + target_node)
        except Exception as e:
            logger.error(e)


class ParseExcel(object):
    def __init__(self, file_name):
        """
        Constructor
        :param file_name: string, full path of xxx.xls file
        """
        self.file_name = file_name

    def write_excel(self, header, data):
        """
        Write Excel with list of header and dict data
        :param header: list, header names, eg.['age', 'name']
        :param data: dict list, eg.[{'age':'20', 'name':'zhangsan'}, {'name':'lisi', 'age':'30'}]
        :return: N/A
        """
        with open(self.file_name, 'w',  newline="", encoding='utf-8') as f:
            writer = csv.DictWriter(f, header)
            writer.writeheader()
            writer.writerows(data)

    def read_excel(self):
        """
        Read Excel Data
        :return: ordered dict list
        """
        with open(self.file_name, 'r', newline='', encoding='utf-8') as f:
            return list(csv.DictReader(f))


class ParseCSV(object):
    def __init__(self, file_name):
        """
        Constructor
        :param file_name: string, name of xxx.csv file
        """
        self.file_name = PROJECT_PATH + u'/data/' + file_name

    def read_csv(self):
        """
        Read csv Data
        :return: ordered list of list
        """
        with open(self.file_name, 'r', newline='', encoding='utf-8') as f:
            return list(csv.reader(f))
