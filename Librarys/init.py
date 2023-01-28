#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Imports
import json
import os

# Setup class
class init_setup:
    def __init__(self, server_name, storage_folder="servers"):
        self.server_name = server_name
        self.to_base_storage_link = os.path.join(os.path.abspath(storage_folder), server_name)

    def init_server_space(self):
        os.mkdir(self.to_base_storage_link)

        path_templates = os.path.join(self.to_base_storage_link, "templates")
        path_static = os.path.join(self.to_base_storage_link, "static")
        path_backup = os.path.join(self.to_base_storage_link, "backups")
        path_plugins = os.path.join(self.to_base_storage_link, "plugins")

        os.mkdir(path_templates)
        os.mkdir(path_static)
        os.mkdir(path_backup)
        os.mkdir(path_plugins)

    def init_server_files(self):
        default_configuration = {"server_name": self.server_name, "pages": {}, "users": {}}
        config_json = open(os.path.join(self.to_base_storage_link, "config.yml"), 'a')
        config_json.write(json.dumps(default_configuration))
        config_json.close()
        
    def init_default_page(self):
        default_configuration = {"server_name": self.server_name, "pages": {"/": "default.html"}, "users": {}}
        config_json = open(os.path.join(self.to_base_storage_link, "config.yml"), 'w')
        config_json.write(json.dumps(default_configuration))
        config_json.close()

        default_page = "<h1>Welcome to IstaServ</h1>"
        # FINIR ÇA!!!!
        config_json = open(os.path.join(self.to_base_storage_link, "default.html"), 'w')
        config_json.write(json.dumps(default_configuration))
        config_json.close()