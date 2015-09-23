import os, sys, yaml, json

import client
import crawler

"""
UPDATE:
- Finally it fetches menu from the first page

TODO:
- Unit tests (`python setup.py test`) are broken because it's doing real requests (yikes!)
- Create "a proper" menu object
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

