import os, sys, yaml, json

import client
import crawler

"""
UPDATE:
- HTTPSConn finally replace with requests

TODO:
- Create "a proper" menu object
- Add logic for fetching more menus
"""

def get_config_values():
    currentDir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    configPath = '{0}{1}'.format(currentDir, '/config/main.yaml')
    configHandler = open(configPath, 'r')

    return yaml.load(configHandler)


if __name__ == '__main__':
    config = get_config_values()

    client = client.Client(config['username'], config['password'], config['domain'])
    crawler = crawler.Crawler(client)
    menuPaths = crawler.getMenuPaths()
    menuObj = crawler.getSingleMenu(menuPaths[0])

    print(json.dumps(menuObj, indent=4, sort_keys=True))

