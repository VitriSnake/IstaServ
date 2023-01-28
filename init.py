#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Imports
import json
import os

# Setup class
class init_setup:
    def __init__(self, server_name, storage_folder="servers"):
        self.server_name = server_name
        self.to_base_storage_link = os.path.abspath(storage_folder)

    def init_server_space(self):
        path_templates = os.path.join(self.to_base_storage_link, "templates")
        path_static = os.path.join(self.to_base_storage_link, "static")
        path_backup = os.path.join(self.to_base_storage_link, "backups")
        path_plugins = os.path.join(self.to_base_storage_link, "plugins")

        os.mkdir(path_templates)
        os.mkdir(path_static)
        os.mkdir(path_backup)
        os.mkdir(path_plugins)

    def init_server_files(self):
        default_configuration = {"server_name": self.server_name, "pages": [], "users": {}}
        config_json = open(os.path.join(self.to_base_storage_link, "config.yml"), 'a')
        config_json.write(json.dumps(default_configuration))
        config_json.close()
        
