from five import grok
from zope.schema.interfaces import IContextSourceBinder
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm
from zope.schema.interfaces import IVocabularyFactory
from zope.component import getUtility
from z3c.formwidget.query.interfaces import IQuerySource

class core_human_rights(grok.GlobalUtility):
    grok.name('ploneun.vocabulary.core_human_rights')
    grok.implements(IVocabularyFactory)

    _terms = [{
        'value': 'icerd',
        'title': 'International Convention on the Elimination of All Forms of Racial Discrimination',
    },
    {   'value': 'iccpr',
        'title': 'International Covenant on Civil and Political Rights',
        },
    {   'value': 'icescr',
        'title': 'International Covenant on Economic, Social and Cultural Rights',
        },
    {   'value': 'cedaw',
        'title': 'Convention on the Elimination of All Forms of Discrimination against Women',
        },
    {   'value': 'cat',
        'title': 'Convention against Torture and Other Cruel, Inhuman or Degrading Treatment or Punishment',
        },
    {   'value': 'crc',
        'title': 'Convention on the Rights of the Child',
        },
    {   'value': 'icmw',
        'title': 'International Convention on the Protection of the Rights of All Migrant Workers and Members of Their Families',
        },
    {   'value': 'cped',
        'title': 'International Convention for the Protection of All Persons from Enforced Disappearance',
        },
    {   'value': 'crpd',
        'title': 'Convention on the Rights of Persons with Disabilities',
        },
    {   'value': 'opcat',
        'title': 'Optional Protocol to the Convention against Torture and Other Cruel, Inhuman or Degrading Treatment or Punishment',
        }
        ]

    def __call__(self, context):
        terms = []
        for i in self._terms:
            terms.append(SimpleTerm(**i))
        return SimpleVocabulary(terms)
