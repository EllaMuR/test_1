class JsTestTask:

    def __init__(self, name, image, price):
        self.name = name
        self.image = image
        self.price = price

    def __repr__(self):
        return "JsTestTask(%s, %s, %s)" % (self.name, self.image, self.price)

    def __lt__(self, other):
        return self.name < other.name

    def __gt__(self, other):
        return self.name > other.name

    def __eq__(self, other):
        return self.name == other.name