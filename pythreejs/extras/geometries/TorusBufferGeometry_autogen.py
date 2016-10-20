from ipywidgets import Widget, DOMWidget, widget_serialization, Color
from traitlets import Unicode, Int, CInt, Instance, This, Enum, Tuple, List, Dict, Float, CFloat, Bool, Union, Any

from ...enums import *
from ...traits import *

from ...core.BufferGeometry_autogen import BufferGeometry


class TorusBufferGeometry(BufferGeometry):
    """TorusBufferGeometry
    
    Autogenerated by generate-wrappers.js 
    Date: Thu Oct 20 2016 15:52:38 GMT-0700 (PDT) 
    See http://threejs.org/docs/#Reference/Extras.Geometries/TorusBufferGeometry 
    """
    
    _view_name = Unicode('TorusBufferGeometryView').tag(sync=True)
    _model_name = Unicode('TorusBufferGeometryModel').tag(sync=True)

    radius = CFloat(100).tag(sync=True)
    tube = CFloat(40).tag(sync=True)
    radialSegments = CInt(8).tag(sync=True)
    tubularSegments = CInt(6).tag(sync=True)
    arc = CFloat(6.283185307179586).tag(sync=True)

