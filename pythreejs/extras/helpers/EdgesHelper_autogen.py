from ipywidgets import Widget, DOMWidget, widget_serialization, Color
from traitlets import Unicode, Int, CInt, Instance, This, Enum, Tuple, List, Dict, Float, CFloat, Bool, Union, Any

from ...enums import *
from ...traits import *

from ..._base.Three import ThreeWidget


class EdgesHelper(ThreeWidget):
    """EdgesHelper
    
    Autogenerated by generate-wrappers.js 
    Date: Thu Oct 20 2016 15:52:38 GMT-0700 (PDT) 
    See http://threejs.org/docs/#Reference/Extras.Helpers/EdgesHelper 
    """
    
    _view_name = Unicode('EdgesHelperView').tag(sync=True)
    _model_name = Unicode('EdgesHelperModel').tag(sync=True)


