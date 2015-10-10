import bs4

class Recipe:
    title = None
    image = None
    calories = None
    ingredients = []
    instructions = []
    rawHtml = None

    def to_json(self):
        return {
            'title': self.title,
            'image': self.image,
            'calories': self.calories,
            'ingredients': self.ingredients,
            'instructions': self.instructions
        }

class RecipeFactory:
    soup = None
    patterns = {
        'title': ('div.content h1', 'text'),
        'image': ('div#recipe_image img', 'src'),
        'calories': ('.content .cal-info', 'text'),
        'ingredients': ('#ingredients li', 'text'),
        'instructions': ('#instructions ol > li', 'text')
    }

    def from_html(self, html):
        self.soup = bs4.BeautifulSoup(html, 'html.parser')
        base_props = self.patterns.keys()
        recipe = Recipe()

        for prop in base_props:
            value = []
            selector, attribute = self.patterns[prop]
            value = self.get_value_from_selector(selector, attribute)

            if len(value) == 1:
                setattr(recipe, prop, value.pop())
            elif len(value) > 1:
                setattr(recipe, prop, value)
            else:
                return None

        return recipe

    def get_value_from_selector(self, css_selector, attribute):
        values = []
        selected = self.soup.select(css_selector)
        for elem in selected:
            value = self.get_elem_value(elem, attribute)
            values.append(value)
        return values

    def get_elem_value(self, dom_elem, attr):
        if attr != 'text':
            value = dom_elem.attrs[attr]
        else:
            value = dom_elem.text
        return value
