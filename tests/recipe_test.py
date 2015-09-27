import os

from unittest import TestCase
from unittest.mock import Mock

from recipecrawler.recipe import Recipe
from recipecrawler.recipe import RecipeFactory

class RecipeFactoryTest(TestCase):
    recipe_factory = None

    def setUp(self):
        self.recipe_factory = RecipeFactory()

    def test_create_from_html(self):
        html = self.__get_fixture('recipe_chilaquiles')
        recipe_factory = RecipeFactory()
        recipe = self.recipe_factory.from_html(html)

        self.assertTrue(isinstance(recipe, Recipe))
        self.assertEqual(recipe.title, 'Chilaquiles')
        self.assertEqual(recipe.image, 'http://goo.gl/jYjcz6')
        self.assertEqual(recipe.calories, '500 kcal')
        self.assertEqual(len(recipe.ingredients), 4)

    def test_importWithWrongHtml(self):
        self.assertEqual(None, self.recipe_factory.from_html('<html></html>'))
        self.assertEqual(None, self.recipe_factory.from_html('<htm>'))
        self.assertEqual(None, self.recipe_factory.from_html('<h//tm>'))
        self.assertEqual(None, self.recipe_factory.from_html('hola'))

    def __get_fixture(self, name):
        basedir = os.path.dirname(os.path.realpath(__file__))
        path = '%s/fixtures/%s.html' % (basedir, name)
        fileHandler = open(path, 'r')
        content = fileHandler.read()
        fileHandler.close()

        return content