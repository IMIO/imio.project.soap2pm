## -*- coding: utf-8 -*-

import base64
from Products.Five import BrowserView
from Products.CMFCore.utils import getToolByName


class ProjectSoapClientView(BrowserView):
    """ Adapts an action or task to prepare data to exchange within imio.pm.wsclient """

    # def getMainFiles(self):
    #     pc = getToolByName(self.context, 'portal_catalog')
    #     res = []
    #     for brain in pc(portal_type='dmsmainfile', path='/'.join(self.context.getPhysicalPath())):
    #         obj = brain.getObject()
    #         res.append({'title': obj.title.encode('utf8'),
    #                     'filename': obj.file.filename.encode('utf8'),
    #                     'file': base64.b64encode(obj.file.data)})
    #     return res
    #
    # def exampleDecision(self):
    #     return ("<p>Le collège communal autorise la location de la salle par Mr Jean Menfout à la date du"
    #             "12/02/2015 de 11h à 18h pour l'organisation d'un anniversaire.</p>")
