"""
Adapter / structural
"""

from abc import abstractmethod, ABCMeta
from lxml import html


class Json(object):
    __metaclass__ = ABCMeta

    def __init__(self, text):
        self.text = text

    @abstractmethod
    def get_currency(self):
        pass


class Html(object):
    __metaclass__ = ABCMeta

    def __init__(self, text):
        self.text = text

    @abstractmethod
    def get_currency(self):
        pass


class JsonAdapter(Json):
    def get_currency(self):
        return self.text['currency']


class HtmlAdapter(Html):
    def get_currency(self):
        return self.text.xpath('.//currency/text()')[0]


class Client(object):
    def __init__(self, sourse):
        self.source = sourse

    def get_currency(self):
        return self.source.get_currency()


j = JsonAdapter({'currency': 'CCC'})
x = HtmlAdapter(html.fromstring('<html><body><currency>CCC</currency></body></html>'))
json_currency = Client(j).get_currency()
xml_currency = Client(x).get_currency()

print [json_currency, xml_currency]
