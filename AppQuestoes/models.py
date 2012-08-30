# -*- coding: utf-8 -*-

# Django:
from django.db import models
from django.contrib.auth.models import User

class Banca(models.Model):

    nome = models.CharField(max_length=100)

    def __unicode__(self):
        return self.nome

class Concurso(models.Model):

    instituicao = models.CharField(max_length=100)
    ano = models.IntegerField()
    banca = models.ForeignKey(Banca)

    def __unicode__(self):
        return u"%s (%d)" % (self.instituicao, self.ano)

class AreaDeAtuacao(models.Model):

    nome = models.CharField(max_length=100)

    class Meta:
        verbose_name = u"Área de Atuação"
        verbose_name_plural = u"Áreas de Atuação"

    def __unicode__(self):
        return self.nome

class Prova(models.Model):

    NIVEIS_DE_ENSINO = (
        (u'Fundamental', u'Fundamental'),
        (u"Médio", u"Médio"),
        (u'Superior', u'Superior'),
        (u"Técnico", u"Técnico"),
    )

    cargo = models.CharField(max_length=100)
    concurso = models.ForeignKey(Concurso)
    nivel_de_ensino = models.CharField(choices=NIVEIS_DE_ENSINO, max_length=50, default=u"Médio")
    area_de_atuacao = models.ForeignKey(AreaDeAtuacao)

    def __unicode__(self):
        return u"%s - %s" % (self.concurso, self.cargo)

class Disciplina(models.Model):
    
    nome = models.CharField(max_length=100)

    def __unicode__(self):
        return self.nome

class Assunto(models.Model):

    disciplina = models.ForeignKey(Disciplina, blank=False)
    nome = models.CharField(max_length=100)

    def __unicode__(self):
        return self.nome

class Questao(models.Model):

    prova = models.ForeignKey(Prova, blank=False)
    assunto = models.ManyToManyField(Assunto, blank=False)
    enunciado = models.TextField()
    nivel_de_dificuldade = models.IntegerField(default=5) #TAI

    def __unicode__(self):
        return u"%s - Id. %d. %s..." % (self.prova, self.id, self.enunciado[:75])

class QuestaoDeVerdadeiroOuFalso(Questao):

    gabarito = models.BooleanField()

    class Meta:
        ordering = ['id']
        verbose_name = u"Questão de Verdadeiro ou Falso"
        verbose_name_plural = u"Questões de Verdadeiro ou Falso"

class QuestaoDeMultiplaEscolha(Questao):

    GABARITOS = (
        (u'A', u'A'),
        (u'B', u'B'),
        (u'C', u'C'),
        (u'D', u'D'),
        (u'E', u'E'),
    )

    alternativa_A = models.TextField()
    alternativa_B = models.TextField()
    alternativa_C = models.TextField()
    alternativa_D = models.TextField(blank=True, default=None)
    alternativa_E = models.TextField(blank=True, default=None)

    gabarito = models.CharField(choices=GABARITOS, max_length=1)

    class Meta:
        ordering = ['id']
        verbose_name = u"Questão de Múltipla Escolha"
        verbose_name_plural = u"Questões de Múltipla Escolha"

class UserProfile(models.Model):

    user = models.ForeignKey(User, unique=True, blank=False)
    nivel_de_preparo = models.IntegerField(default=5) #TAI

    def __unicode__(self):
        return self.user.username

class QuestoesRespondidas(models.Model):

    user = models.ForeignKey(User, blank=False)
    questao = models.ForeignKey(Questao, blank=False)
    acertou = models.BooleanField()

    class Meta:
        unique_together = ("user", "questao")

class _QuestaoDeMultiplaEscolha():

    id = 0
    prova = ""
    assunto = ""
    enunciado = ""
    alternativa_A = ""
    alternativa_B = ""
    alternativa_C = ""
    alternativa_D = ""
    alternativa_E = ""
    gabarito = ""
    acertou = 0
    alternativa_selecionada = ""
    comentarios = []
    tipo = "AppQuestoes.questaodemultiplaescolha"

    def __init__(
        self,
        id,
        prova,
        assunto,
        enunciado,
        alternativa_A,
        alternativa_B,
        alternativa_C,
        alternativa_D,
        alternativa_E,
        gabarito,
        acertou,
        alternativa_selecionada,
        comentarios=[]):

        self.id = id
        self.prova = prova
        self.assunto = assunto
        self.enunciado = enunciado
        self.alternativa_A = alternativa_A
        self.alternativa_B = alternativa_B
        self.alternativa_C = alternativa_C
        self.alternativa_D = alternativa_D
        self.alternativa_E = alternativa_E
        self.gabarito = gabarito
        self.acertou = acertou
        self.alternativa_selecionada = alternativa_selecionada
        self.comentarios = comentarios

class _QuestaoDeVerdadeiroOuFalso():

    id = 0
    prova = ""
    assunto = ""
    enunciado = ""
    gabarito = ""
    acertou = 0
    alternativa_selecionada = ""
    tipo = "AppQuestoes.questaodeverdadeirooufalso"

    def __init__(
        self,
        id,
        prova,
        assunto,
        enunciado,
        gabarito,
        acertou,
        alternativa_selecionada,
        comentarios=[]):

        self.id = id
        self.prova = prova
        self.assunto = assunto
        self.enunciado = enunciado
        self.gabarito = gabarito
        self.acertou = acertou
        self.alternativa_selecionada = alternativa_selecionada
        self.comentarios = comentarios
