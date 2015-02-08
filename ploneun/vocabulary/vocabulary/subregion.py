from five import grok
from zope.schema.interfaces import IContextSourceBinder
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm
from zope.schema.interfaces import IVocabularyFactory
from zope.component import getUtility
from z3c.formwidget.query.interfaces import IQuerySource

class UNGeographicalSubRegion(grok.GlobalUtility):

    # UN Data Codes and Categorization
    # http://unstats.un.org/unsd/methods/m49/m49regin.htm

    grok.name('ploneun.vocabulary.subregion')
    grok.implements(IVocabularyFactory)

    #FIXME incomplete, and should be from lookup csv file
    _terms = [
        {
        'value': '029',
        'title': 'Caribbean',
        },
        ]

    def __call__(self, context):
        terms = []
        for i in self._terms:
            terms.append(SimpleTerm(**i))
        return SimpleVocabulary(terms)
