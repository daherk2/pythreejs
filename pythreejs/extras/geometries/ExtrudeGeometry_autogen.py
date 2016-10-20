from ipywidgets import Widget, DOMWidget, widget_serialization, Color
from traitlets import Unicode, Int, CInt, Instance, This, Enum, Tuple, List, Dict, Float, CFloat, Bool, Union, Any

from ...enums import *
from ...traits import *

from ...core.Geometry_autogen import Geometry


class ExtrudeGeometry(Geometry):
    """ExtrudeGeometry
    
    Autogenerated by generate-wrappers.js 
    Date: Thu Oct 20 2016 15:52:38 GMT-0700 (PDT) 
    See http://threejs.org/docs/#Reference/Extras.Geometries/ExtrudeGeometry 
    """
    
    _view_name = Unicode('ExtrudeGeometryView').tag(sync=True)
    _model_name = Unicode('ExtrudeGeometryModel').tag(sync=True)


