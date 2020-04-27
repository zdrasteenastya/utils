"""
Factory method / creational
"""

from abc import ABCMeta, abstractmethod


class Text(object):
    def __init__(self, text):
        self.text = text

    def write(self):
        return self.text


class Article(Text):
    def write(self):
        return 'It\'s article, baby - {}'.format(self.text)


class News(Text):
    def write(self):
        return 'It\'s news, baby - {}'.format(self.text)


class TextFabric(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def make_text(self, text):
        pass


class ArticleFabric(TextFabric):

    def make_text(self, text):
        return Article(text)


class NewsFabric(TextFabric):

    def make_text(self, text):
        return News(text)


def choose_type(type1):
    if type1 == 'Article':
        return ArticleFabric()
    if type1 == 'News':
        return News
    else:
        return None


print choose_type('Article').make_text('dfdds').write()
