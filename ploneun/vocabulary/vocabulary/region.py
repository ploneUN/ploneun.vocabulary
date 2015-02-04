from five import grok
from zope.schema.interfaces import IContextSourceBinder
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm
from zope.schema.interfaces import IVocabularyFactory
from zope.component import getUtility
from z3c.formwidget.query.interfaces import IQuerySource

class UNGeographicalRegion(grok.GlobalUtility):

    # UN Data Codes and Categorization
    # http://unstats.un.org/unsd/methods/m49/m49regin.htm

    grok.name('ploneun.vocabulary.region')
    grok.implements(IVocabularyFactory)

    _terms = [
        {
        'value': '002',
        'title': 'Africa',
        },
        {
        'value': '142',
        'title': 'Asia',
        },
        {
        'value': '419',
        'title': 'Latin America and the Caribbean',
        },
        {
        'value': '021',
        'title': 'Northern America',
        },
        {
        'value': '150',
        'title': 'Europe',
        },
        {
        'value': '009',
        'title': 'Oceania',
        },
        ]

    def __call__(self, context):
        terms = []
        for i in self._terms:
            terms.append(SimpleTerm(**i))
        return SimpleVocabulary(terms)
