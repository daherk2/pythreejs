from ipywidgets import Widget, DOMWidget, widget_serialization, Color
from traitlets import Unicode, Int, CInt, Instance, This, Enum, Tuple, List, Dict, Float, CFloat, Bool, Union, Any

from ...enums import *
from ...traits import *

from ...core.Geometry_autogen import Geometry


class ParametricGeometry(Geometry):
    """ParametricGeometry
    
    Autogenerated by generate-wrappers.js 
    Date: Thu Oct 20 2016 15:52:38 GMT-0700 (PDT) 
    See http://threejs.org/docs/#Reference/Extras.Geometries/ParametricGeometry 
    """
    
    _view_name = Unicode('ParametricGeometryView').tag(sync=True)
    _model_name = Unicode('ParametricGeometryModel').tag(sync=True)

    func = Unicode('function (u,v) { return THREE.Vector3(); }').tag(sync=True)
    slices = CInt(3).tag(sync=True)
    stacks = CInt(3).tag(sync=True)

