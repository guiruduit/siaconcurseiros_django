# -*- coding: utf-8 -*-

"""
This file demonstrates two different styles of tests (one doctest and one
unittest). These will both pass when you run "manage.py test".

Replace these with more appropriate tests for your application.
"""

# Django
from django.test import TestCase

# AppQuestoes
from models import Banca, Concurso, Prova, Disciplina, Assunto, QuestaoDeMultiplaEscolha

class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.failUnlessEqual(1 + 1, 2)

__test__ = {"doctest": """
Another way to test that 1 + 1 is equal to 2.

>>> 1 + 1 == 2
True

>>> cespe = Banca.objects.create(nome="Cespe UNB")
>>> print cespe
Cespe UNB

>>> caixa2010 = Concurso.objects.create(instituicao="CEF", ano=2010, banca=cespe)
>>> print caixa2010
CEF (2010)

>>> tbn_caixa2010 = Prova.objects.create(cargo="TBN", concurso=caixa2010)
>>> print tbn_caixa2010
CEF (2010) - TBN

>>> portugues = Disciplina.objects.create(nome="Portugues")
>>> print portugues
Portugues

>>> crase = Assunto.objects.create(nome="Crase", disciplina=portugues)
>>> print crase
Crase

>>> questao1 = QuestaoDeMultiplaEscolha(
... prova=tbn_caixa2010,
... assunto=crase,
... enunciado="No que tange à concordância e ao emprego do sinal indicativo de crase no texto, assinale a opção correta.",
... alternativa_A="Em 'conjunto de normas que dá o norte ao sistema educacional brasileiro' (L.27-28), o verbo dar pode ser flexionado tanto no singular, concordando com 'conjunto', quanto no plural, concordando com 'normas'.",
... alternativa_B="A oração 'tal tarefa cabe a todos os níveis do ensino básico' (L.29) poderia ser corretamente reescrita da seguinte forma: a todos os níveis do ensino básico cabem tal tarefa.",
... alternativa_C="Caso fosse empregado o sinal indicativo de crase em 'as', no trecho 'ensinar as crianças a pensar' (L.18), seriam mantidos a correção gramatical do período e seu sentido original.",
... alternativa_D="Em 'abertas a novas tecnologias' (L.21), se o termo 'a' fosse flexionado no plural, o emprego do sinal indicativo de crase seria obrigatório.",
... alternativa_E="O uso do sinal indicativo de crase em 'com vistas à sua colocação' (L.25) é obrigatório.",
... gabarito="D")
"""}

