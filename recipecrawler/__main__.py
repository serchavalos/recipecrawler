import os, sys, yaml, json

import client
import crawler

"""
UPDATE:
- Recipe object created

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

    client = client.Client(config['username'], config['password'], config['domain'])
    crawler = crawler.Crawler(client)
    menuPaths = crawler.getMenuPaths()
    recipe = crawler.getSingleMenu(menuPaths[0])

    print(json.dumps(recipe.to_json(), indent=4, sort_keys=True))

