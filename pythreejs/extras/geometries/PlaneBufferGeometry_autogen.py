from ipywidgets import Widget, DOMWidget, widget_serialization, Color
from traitlets import Unicode, Int, CInt, Instance, This, Enum, Tuple, List, Dict, Float, CFloat, Bool, Union, Any

from ...enums import *
from ...traits import *

from ...core.BufferGeometry_autogen import BufferGeometry


class PlaneBufferGeometry(BufferGeometry):
    """PlaneBufferGeometry
    
    Autogenerated by generate-wrappers.js 
    Date: Thu Oct 20 2016 15:52:38 GMT-0700 (PDT) 
    See http://threejs.org/docs/#Reference/Extras.Geometries/PlaneBufferGeometry 
    """
    
    _view_name = Unicode('PlaneBufferGeometryView').tag(sync=True)
    _model_name = Unicode('PlaneBufferGeometryModel').tag(sync=True)

    width = CFloat(10).tag(sync=True)
    height = CFloat(10).tag(sync=True)
    widthSegments = CInt(1).tag(sync=True)
    heightSegments = CInt(1).tag(sync=True)

