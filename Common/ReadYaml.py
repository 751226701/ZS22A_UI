#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @author: 刘涛
# @time: 2024/1/15 11:11
# @file: ReadYaml.py
# @project: ZS22A_UI

import yaml, os
from Config.Config import Config


class ReadYaml(object):

    def __init__(self, filename):
        self.filename = filename

    def read(self, keys=None):
        """如果提供了用例编号列表keys，则返回这些用例的数据列表；否则返回所有用例的列表"""
        with open(file=self.filename, mode="r", encoding='utf8') as f:
            data = f.read()
        data_yaml = yaml.load(data, Loader=yaml.FullLoader)

        # 如果提供了keys列表，则筛选出对应的用例数据
        if keys:
            # 筛选出请求的用例数据
            filtered_data = [item for item in data_yaml if item.get('用例编号') in keys]
            # 拼接URL地址
            for item in filtered_data:
                if item.get("url地址") is not None:
                    item["url地址"] = Config.url + item["url地址"]
            return filtered_data
        else:
            # 如果没有提供keys，则返回所有用例数据，并拼接URL地址
            for value in data_yaml:
                if value.get("url地址") is not None:
                    value["url地址"] = Config.url + value["url地址"]
            return data_yaml

    def readEx(self, keys=None):
        """返回一个字典，键为用例编号；如果提供了keys，则只包含这些用例编号的数据"""
        with open(file=self.filename, mode="r", encoding='utf8') as f:
            data = f.read()
        data_yaml = yaml.load(data, Loader=yaml.FullLoader)

        # 首先，构建用例编号到用例数据的映射
        data_dict = {item['用例编号']: item for item in data_yaml}

        if keys:
            # 如果提供了keys，筛选出请求的用例编号对应的数据，并拼接URL地址
            filtered_data = []
            for key in keys:
                test_case = data_dict.get(key)
                if test_case:
                    # 如果用例存在，拼接URL地址
                    if test_case.get("url地址") is not None:
                        test_case["url地址"] = Config.url + test_case["url地址"]
                    filtered_data.append(test_case)
            return filtered_data
        else:
            # 如果没有提供keys，返回所有用例数据，并拼接URL地址
            for key in data_dict:
                if data_dict[key].get("url地址") is not None:
                    data_dict[key]["url地址"] = Config.url + data_dict[key]["url地址"]
            return data_dict

if __name__ == '__main__':
    # yaml_data = ReadYaml(os.path.join(Config.test_datas_dir, "test_data_01.yaml"))
    # print(yaml_data.readEx(["test_case_01", "test_case_02"]))

    # yaml_data = ReadYaml(os.path.join(Config.test_datas_dir, "test_data_01.yaml"))
    # print(yaml_data.read(["test_case_01", "test_case_02"]))

    yaml_data = ReadYaml(os.path.join(Config.test_datas_dir, "test_data_01.yaml")).read()
    print(yaml_data[54]['断言元素定位'][2])