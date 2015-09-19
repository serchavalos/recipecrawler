import os, sys, yaml

import client
import crawler

def get_config_values():
    currentDir = os.path.dirname(os.path.abspath(__file__))
    configPath = '{0}{1}'.format(currentDir, '/config/main.yaml')
    configHandler = open(configPath, 'r')

    return yaml.load(configHandler)


if __name__ == '__main__':
    config = get_config_values()

    client = client.Client(config['username'], config['password'], config['domain'])
    crawler = crawler.Crawler(client)
    receiptHtml = crawler.fetchMenuPage()

    fileHandler = open('receipt.html', 'w')
    fileHandler.write(receiptHtml)
    fileHandler.close()
