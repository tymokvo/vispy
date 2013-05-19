# -*- coding: utf-8 -*-
from __future__ import print_function, division, absolute_import

"""
Vispy - http://vispy.org

The vispy consists of multiple subpackages that need to be imported
separately before use. These are:

  * ... todo

"""

__version__ = '0.0.dev'

import vispy.util
from vispy.util.keys import keys

from vispy.event import EmitterGroup, EventEmitter, Event


class ConfigEvent(Event):
    """ Event indicating a configuration change. 
    
    This class has a 'changes' attribute which is a dict of all name:value 
    pairs that have changed in the configuration.
    """
    def __init__(self, changes):
        Event.__init__(self, type='config_change')
        self.changes = changes
        
        
class Config(object):
    """ Container for global settings used application-wide in vispy.
    
    Events:
    -------
    Config.events.changed - Emits ConfigEvent whenever the configuration changes.
    """
    def __init__(self):
        self.events = EmitterGroup(source=self)
        self.events['changed'] = EventEmitter(event_class=ConfigEvent, source=self)
        self._config = {}
    
    def __getitem__(self, item):
        return self._config[item]
    
    def __setitem__(self, item, val):
        self._config[item] = val
        ## inform any listeners that a configuration option has changed
        self.events.changed(changes={item:val})
        
    def update(self, **kwds):
        self._config.update(kwds)
        self.events.changed(changes=kwds)


config = Config()
config.update(
    default_backend='qt',
    qt_lib= 'any',  # options are 'pyqt', 'pyside', or 'any'
)
