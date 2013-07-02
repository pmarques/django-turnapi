# from functools import update_wrapper
# from django.http import Http404, HttpResponseRedirect
# from django.contrib.admin import ModelAdmin, actions
# from django.contrib.admin.forms import AdminAuthenticationForm
# from django.contrib.auth import REDIRECT_FIELD_NAME
# from django.contrib.contenttypes import views as contenttype_views
# from django.views.decorators.csrf import csrf_protect
# from django.db.models.base import ModelBase
# from django.core.exceptions import ImproperlyConfigured
# from django.core.urlresolvers import reverse, NoReverseMatch
# from django.template.response import TemplateResponse
# from django.utils import six
# from django.utils.text import capfirst
# from django.utils.translation import ugettext as _
# from django.views.decorators.cache import never_cache
from django.conf import settings

from django.conf.urls import patterns, url, include

# LOGIN_FORM_KEY = 'this_is_the_login_form'

# class AlreadyRegistered(Exception):
#     pass
# 
# 
# class NotRegistered(Exception):
#     pass


def get_urls():
  # if settings.DEBUG:
  #  self.check_dependencies()

  # Admin-site-wide views.
  urlpatterns = patterns('',
    url(r'^$',
      'turnapi.api.turn', # wrap(self.index),
      name='turnapi')
  )

  # # Add in each model's views.
  # for model, model_admin in six.iteritems(self._registry):
  #   urlpatterns += patterns('',
  #     url(r'^%s/%s/' % (model._meta.app_label, model._meta.module_name),
  #       include(model_admin.urls))
  #   )
  return urlpatterns

def urls():
  return get_urls(), 'self.app_name', 'self.name'
