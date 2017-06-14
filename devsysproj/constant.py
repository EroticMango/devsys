#-*- coding:utf8 -*-

__all__ = []

import ConfigParser
from django.conf import settings

# DBNAME = cfg.get('DB', 'DBNAME')
class SvrConfig(object):

    def __init__(self):
        self.conf_dict = {}
        self.init_conf()
        print "=======init finish======="

    @property
    def cfp(self):
        cfp = ConfigParser.ConfigParser()
        self.read_conf_file(cfp)
        return cfp

    def read_conf_file(self, cfp):
        # if settings.DEBUG: #开发环境配置
        #     self.cfp.read("dev_svr.ini")
        # else:
        #     self.cfp.read("svr.ini")
        cfp.read("svr.ini")

    def init_conf(self):

        sections = self.cfp.sections()
        print sections
        for section in self.cfp.sections():

            section_dict = {}
            self.__setitem__(section, section_dict)

            for item in self.cfp.items(section):
                section_dict = self.__getitem__(section)
                section_dict[item[0]] = item[1]

    def __getitem__(self, key):
        return self.conf_dict[key]

    def __setitem__(self, key, value):
        self.conf_dict[key] = value

svr_config = SvrConfig()
