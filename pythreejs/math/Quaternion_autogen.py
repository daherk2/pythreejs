from ipywidgets import Widget, DOMWidget, widget_serialization, Color
from traitlets import Unicode, Int, CInt, Instance, This, Enum, Tuple, List, Dict, Float, CFloat, Bool, Union, Any

from ..enums import *
from ..traits import *

from .._base.Three import ThreeWidget


class Quaternion(ThreeWidget):
    """Quaternion
    
    Autogenerated by generate-wrappers.js 
    Date: Thu Oct 20 2016 15:52:38 GMT-0700 (PDT) 
    See http://threejs.org/docs/#Reference/Math/Quaternion 
    """
    
    _view_name = Unicode('QuaternionView').tag(sync=True)
    _model_name = Unicode('QuaternionModel').tag(sync=True)

    x = CFloat(0).tag(sync=True)
    y = CFloat(0).tag(sync=True)
    z = CFloat(0).tag(sync=True)
    w = CFloat(1).tag(sync=True)

