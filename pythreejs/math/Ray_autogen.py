from ipywidgets import Widget, DOMWidget, widget_serialization, Color
from traitlets import Unicode, Int, CInt, Instance, This, Enum, Tuple, List, Dict, Float, CFloat, Bool, Union, Any

from ..enums import *
from ..traits import *

from .._base.Three import ThreeWidget


class Ray(ThreeWidget):
    """Ray
    
    Autogenerated by generate-wrappers.js 
    Date: Thu Oct 20 2016 15:52:38 GMT-0700 (PDT) 
    See http://threejs.org/docs/#Reference/Math/Ray 
    """
    
    _view_name = Unicode('RayView').tag(sync=True)
    _model_name = Unicode('RayModel').tag(sync=True)

    origin = Vector3(default=[0,0,0]).tag(sync=True)
    direction = Vector3(default=[0,0,0]).tag(sync=True)

