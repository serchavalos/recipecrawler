import os, sys, yaml, json

from optparse import OptionParser

from client import Client
from crawler import Crawler

"""
UPDATE:

TODO:
- Add logic for fetching more menus
- Add a pre-commit hook that runs unit tests
"""

def get_config_values():
    currentDir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    configPath = '{0}{1}'.format(currentDir, '/config/main.yaml')
    configHandler = open(configPath, 'r')

    return yaml.load(configHandler)


if __name__ == '__main__':
    config = get_config_values()

    totalMenus = 1
    stepSize = 5
    menus = []
    offset = 0

    client = Client(config['username'], config['password'], config['domain'])
    crawler = Crawler(client)

    while len(menus) < totalMenus:
        menuPaths = crawler.getMenuPaths(stepSize, offset)
        if len(menuPaths) < 1:
            break #something broken

        for path in menuPaths:
            recipe = crawler.getSingleMenu(path)
            menus.append(recipe)
            break

        offset += stepSize

    # print(json.dumps(recipe.__dict__, indent=4, sort_keys=True, ensure_ascii=False))
    print ('Menus processed: %s' % (len(menus)))

    print ('Writing on cache file...')
    cacheFile = open('recipes.json', '+w')
    for menu in menus:
        cacheFile.write(json.dumps(menu.__dict__, indent=4, sort_keys=True, ensure_ascii=False))

    cacheFile.close()

    print ('Completed')


