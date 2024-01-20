#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: 刘涛
@time: 2024/1/15 11:11 
@file: ReadYaml.py
@project: ZS22A_UI
"""
import yaml, os
from Config.Config import Config


class ReadYaml(object):

    def __init__(self, filename):
        self.filename = filename

    def read(self):
        with open(file=self.filename, mode="r", encoding='utf8', ) as f:
            data = f.read()
        data_yaml = yaml.load(data, Loader=yaml.FullLoader)
        for value in data_yaml:
            # 拼接URL地址
            if value.get("url地址") is not None:
                value["url地址"] = Config.url + value["url地址"]

        return data_yaml


if __name__ == '__main__':
    pass
    yaml_data = ReadYaml(os.path.join(Config.test_datas_dir, "test_data_1_10.yaml")).read()
    print([yaml_data[3]])
