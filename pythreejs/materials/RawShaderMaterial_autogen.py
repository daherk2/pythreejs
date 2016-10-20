from ipywidgets import Widget, DOMWidget, widget_serialization, Color
from traitlets import Unicode, Int, CInt, Instance, This, Enum, Tuple, List, Dict, Float, CFloat, Bool, Union, Any

from ..enums import *
from ..traits import *

from .ShaderMaterial_autogen import ShaderMaterial


class RawShaderMaterial(ShaderMaterial):
    """RawShaderMaterial
    
    Autogenerated by generate-wrappers.js 
    Date: Thu Oct 20 2016 15:52:38 GMT-0700 (PDT) 
    See http://threejs.org/docs/#Reference/Materials/RawShaderMaterial 
    """
    
    _view_name = Unicode('RawShaderMaterialView').tag(sync=True)
    _model_name = Unicode('RawShaderMaterialModel').tag(sync=True)


