## -*- coding: utf-8 -*-

from collective.task.interfaces import ITaskMethods
from Products.Five import BrowserView
from Products.CMFPlone.utils import safe_unicode


def object_link(obj, view=''):
    href = view and "%s/%s" % (obj.absolute_url(), view) or obj.absolute_url()
    return u'<a href="%s">%s</a>' % (href, safe_unicode(obj.Title()))


class ProjectSoapClientView(BrowserView):
    """ Adapts an action or task to prepare data to exchange within imio.pm.wsclient """

    def motivation(self):
        return ("<p></p>")

    def common_detailed_description(self):
        out = []
        out.append(u"<p>OS: %s</p>" % object_link(self.os))
        out.append(u"<p>OO: %s</p>" % object_link(self.oo))
        out.append(u"<p>Action: %s</p>" % object_link(self.action))
        return out


class ProjectActionSoapClientView(ProjectSoapClientView):

    def __init__(self, context, request):
        super(ProjectActionSoapClientView, self).__init__(context, request)
        self.action = self.context
        self.oo = self.action.aq_parent
        self.os = self.oo.aq_parent

    def detailed_description(self):
        return u''.join(self.common_detailed_description())


class ProjectTaskSoapClientView(ProjectSoapClientView):

    def __init__(self, context, request):
        super(ProjectActionSoapClientView, self).__init__(context, request)
        self.adapted = ITaskMethods(self.context)
        self.action = self.adapted.get_highest_task_parent(task=False)
        self.oo = self.action.aq_parent
        self.os = self.oo.aq_parent

    def detailed_description(self):
        out = self.common_detailed_description()
        return u''.join(out)
