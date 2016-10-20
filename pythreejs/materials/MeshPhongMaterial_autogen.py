from ipywidgets import Widget, DOMWidget, widget_serialization, Color
from traitlets import Unicode, Int, CInt, Instance, This, Enum, Tuple, List, Dict, Float, CFloat, Bool, Union, Any

from ..enums import *
from ..traits import *

from .Material_autogen import Material

from ..textures.Texture_autogen import Texture

class MeshPhongMaterial(Material):
    """MeshPhongMaterial
    
    Autogenerated by generate-wrappers.js 
    Date: Thu Oct 20 2016 15:52:38 GMT-0700 (PDT) 
    See http://threejs.org/docs/#Reference/Materials/MeshPhongMaterial 
    """
    
    _view_name = Unicode('MeshPhongMaterialView').tag(sync=True)
    _model_name = Unicode('MeshPhongMaterialModel').tag(sync=True)

    color = Unicode("#ffffff").tag(sync=True)
    specular = Unicode("#111111").tag(sync=True)
    shininess = CFloat(30).tag(sync=True)
    map = Instance(Texture, allow_none=True).tag(sync=True, **widget_serialization)
    lightMap = Instance(Texture, allow_none=True).tag(sync=True, **widget_serialization)
    lightMapIntensity = CFloat(1).tag(sync=True)
    aoMap = Instance(Texture, allow_none=True).tag(sync=True, **widget_serialization)
    aoMapIntensity = CFloat(1).tag(sync=True)
    emissive = Unicode("#000000").tag(sync=True)
    emissiveMap = Instance(Texture, allow_none=True).tag(sync=True, **widget_serialization)
    emissiveIntensity = CFloat(1).tag(sync=True)
    bumpMap = Instance(Texture, allow_none=True).tag(sync=True, **widget_serialization)
    bumpScale = CFloat(1).tag(sync=True)
    normalMap = Instance(Texture, allow_none=True).tag(sync=True, **widget_serialization)
    normalScale = Vector2(default=[1,1]).tag(sync=True)
    displacementMap = Instance(Texture, allow_none=True).tag(sync=True, **widget_serialization)
    displacementScale = CFloat(1).tag(sync=True)
    displacementBias = CFloat(0).tag(sync=True)
    specularMap = Instance(Texture, allow_none=True).tag(sync=True, **widget_serialization)
    alphaMap = Instance(Texture, allow_none=True).tag(sync=True, **widget_serialization)
    envMap = Instance(Texture, allow_none=True).tag(sync=True, **widget_serialization)
    combine = Enum(Operations, "MultiplyOperation").tag(sync=True)
    reflectivity = CFloat(1).tag(sync=True)
    refractionRatio = CFloat(0.98).tag(sync=True)
    fog = Bool(False).tag(sync=True)
    shading = Enum(Shading, "SmoothShading").tag(sync=True)
    wireframe = Bool(False).tag(sync=True)
    wireframeLinewidth = CFloat(1).tag(sync=True)
    wireframeLinecap = Unicode("round").tag(sync=True)
    wireframeLinejoin = Unicode("round").tag(sync=True)
    vertexColors = Enum(Colors, "NoColors").tag(sync=True)
    skinning = Bool(False).tag(sync=True)
    morphTargets = Bool(False).tag(sync=True)
    morphNormals = Bool(False).tag(sync=True)

