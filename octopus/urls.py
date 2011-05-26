# -*- coding: utf-8 -*-
# octopus.urls
# 

# Following few lines is an example urlmapping with an older interface.
"""
from werkzeug.routing import EndpointPrefix, Rule

def make_rules():
  return [
    EndpointPrefix('octopus/', [
      Rule('/', endpoint='index'),
    ]),
  ]

all_views = {
  'octopus/index': 'octopus.views.index',
}
"""

from kay.routing import (
  ViewGroup, Rule
)

view_groups = [
  ViewGroup(
    Rule('/', endpoint='index', view='octopus.views.index'),
  )
]

