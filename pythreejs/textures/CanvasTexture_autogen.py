from ipywidgets import Widget, DOMWidget, widget_serialization, Color
from traitlets import Unicode, Int, CInt, Instance, This, Enum, Tuple, List, Dict, Float, CFloat, Bool, Union, Any

from ..enums import *
from ..traits import *

from .Texture_autogen import Texture


class CanvasTexture(Texture):
    """CanvasTexture
    
    Autogenerated by generate-wrappers.js 
    Date: Thu Oct 20 2016 15:52:38 GMT-0700 (PDT) 
    See http://threejs.org/docs/#Reference/Textures/CanvasTexture 
    """
    
    _view_name = Unicode('CanvasTextureView').tag(sync=True)
    _model_name = Unicode('CanvasTextureModel').tag(sync=True)


