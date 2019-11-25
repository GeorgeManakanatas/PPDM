# -*- coding: utf-8 -*-
import os
import json


def master():
    with open('config/defaultConfig.json', 'r') as json_data_file:
        default_config = json.load(json_data_file)

    file_cleanup_before_start()


def file_cleanup_before_start():
    if not os.path.isdir(default_config["temp_folder_location"]):
        print('temp dir does not exist')
        os.mkdir(default_config["temp_folder_location"])
    else:
        print('temp dir exists')
        # checking for files
        if not os.path.isfile():
            # create file


if __name__ == '__main__':
    master()