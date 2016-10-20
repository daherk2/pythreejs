from ipywidgets import Widget, DOMWidget, widget_serialization, Color
from traitlets import Unicode, Int, CInt, Instance, This, Enum, Tuple, List, Dict, Float, CFloat, Bool, Union, Any

from ..enums import *
from ..traits import *

from .Camera_autogen import Camera


class OrthographicCamera(Camera):
    """OrthographicCamera
    
    Autogenerated by generate-wrappers.js 
    Date: Thu Oct 20 2016 15:52:38 GMT-0700 (PDT) 
    See http://threejs.org/docs/#Reference/Cameras/OrthographicCamera 
    """
    
    _view_name = Unicode('OrthographicCameraView').tag(sync=True)
    _model_name = Unicode('OrthographicCameraModel').tag(sync=True)

    zoom = CFloat(1).tag(sync=True)
    left = CFloat(0).tag(sync=True)
    right = CFloat(0).tag(sync=True)
    top = CFloat(0).tag(sync=True)
    bottom = CFloat(0).tag(sync=True)
    near = CFloat(0.1).tag(sync=True)
    far = CFloat(2000).tag(sync=True)

