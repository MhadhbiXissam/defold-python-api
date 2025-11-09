from enum import Enum
from defoldsdk import sdk
from PyQt5.QtCore import QObject, pyqtSignal, pyqtProperty
from google.protobuf.text_format import MessageToString, Parse
from typing import List
# ------- AcquireCameraFocus ------- #
# ------- AcquireInputFocus ------- #
# ------- Animation ------- #
# ------- AnimationDone ------- #
# ------- ApplyForce ------- #
# ------- Atlas ------- #
# ------- AtlasAnimation ------- #
# ------- AtlasImage ------- #
# ------- BufferDesc ------- #
# ------- CameraDesc ------- #
# ------- ClearColor ------- #
# ------- CollectionDesc ------- #
# ------- CollectionFactoryDesc ------- #
# ------- CollectionInstanceDesc ------- #
# ------- CollectionProxyDesc ------- #
# ------- Collision ------- #
# ------- CollisionEvent ------- #
# ------- CollisionObjectDesc ------- #
# ------- CollisionResponse ------- #
# ------- CollisionShape ------- #
class Type(Enum):
	TYPE_SPHERE = 0
	TYPE_BOX = 1
	TYPE_CAPSULE = 2
	TYPE_HULL = 3
# ------- ComponenTypeDesc ------- #
# ------- ComponentDesc ------- #
# ------- ComponentPropertyDesc ------- #
# ------- ContactPoint ------- #
# ------- ContactPointEvent ------- #
# ------- ContactPointResponse ------- #
# ------- ConvexHull ------- #
# ------- ConvexShape ------- #
class Type(Enum):
	TYPE_SPHERE = 0
	TYPE_BOX = 1
	TYPE_CAPSULE = 2
	TYPE_HULL = 3
# ------- Create ------- #
# ------- Cubemap ------- #
# ------- Cue ------- #
# ------- Disable ------- #
# ------- DisplayProfile ------- #
# ------- DisplayProfileQualifier ------- #
# ------- DisplayProfiles ------- #
# ------- DrawDebugText ------- #
# ------- DrawLine ------- #
# ------- DrawText ------- #
# ------- EmbeddedComponentDesc ------- #
# ------- EmbeddedInstanceDesc ------- #
# ------- Enable ------- #
# ------- EnableGridShapeLayer ------- #
# ------- Exit ------- #
# ------- FactoryDesc ------- #
# ------- FontDesc ------- #
# ------- FontMap ------- #
# ------- GlyphBank ------- #
# ------- HashDigest ------- #
# ------- HideApp ------- #
# ------- InstanceDesc ------- #
# ------- InstancePropertyDesc ------- #
# ------- LabelDesc ------- #
class BlendMode(Enum):
	BLEND_MODE_ALPHA = 0
	BLEND_MODE_ADD = 1
	BLEND_MODE_MULT = 3
	BLEND_MODE_SCREEN = 4
class Pivot(Enum):
	PIVOT_CENTER = 0
	PIVOT_N = 1
	PIVOT_NE = 2
	PIVOT_E = 3
	PIVOT_SE = 4
	PIVOT_S = 5
	PIVOT_SW = 6
	PIVOT_W = 7
	PIVOT_NW = 8
# ------- LayoutChanged ------- #
# ------- LightDesc ------- #
# ------- LuaModule ------- #
# ------- LuaRef ------- #
# ------- LuaSource ------- #
# ------- ManifestData ------- #
# ------- ManifestFile ------- #
# ------- ManifestHeader ------- #
# ------- Material ------- #
# ------- MaterialDesc ------- #
class ConstantType(Enum):
	CONSTANT_TYPE_USER = 0
	CONSTANT_TYPE_VIEWPROJ = 1
	CONSTANT_TYPE_WORLD = 2
	CONSTANT_TYPE_TEXTURE = 3
	CONSTANT_TYPE_VIEW = 4
	CONSTANT_TYPE_PROJECTION = 5
	CONSTANT_TYPE_NORMAL = 6
	CONSTANT_TYPE_WORLDVIEW = 7
	CONSTANT_TYPE_WORLDVIEWPROJ = 8
	CONSTANT_TYPE_USER_MATRIX4 = 9
class VertexSpace(Enum):
	VERTEX_SPACE_WORLD = 0
	VERTEX_SPACE_LOCAL = 1
class WrapMode(Enum):
	WRAP_MODE_REPEAT = 0
	WRAP_MODE_MIRRORED_REPEAT = 1
	WRAP_MODE_CLAMP_TO_EDGE = 2
class FilterModeMin(Enum):
	FILTER_MODE_MIN_NEAREST = 0
	FILTER_MODE_MIN_LINEAR = 1
	FILTER_MODE_MIN_NEAREST_MIPMAP_NEAREST = 2
	FILTER_MODE_MIN_NEAREST_MIPMAP_LINEAR = 3
	FILTER_MODE_MIN_LINEAR_MIPMAP_NEAREST = 4
	FILTER_MODE_MIN_LINEAR_MIPMAP_LINEAR = 5
	FILTER_MODE_MIN_DEFAULT = 6
class FilterModeMag(Enum):
	FILTER_MODE_MAG_NEAREST = 0
	FILTER_MODE_MAG_LINEAR = 1
	FILTER_MODE_MAG_DEFAULT = 2
# ------- Matrix4 ------- #
# ------- MeshDesc ------- #
class PrimitiveType(Enum):
	PRIMITIVE_LINES = 1
	PRIMITIVE_TRIANGLES = 4
	PRIMITIVE_TRIANGLE_STRIP = 5
# ------- Model ------- #
# ------- ModelAnimationDone ------- #
# ------- ModelCancelAnimation ------- #
# ------- ModelDesc ------- #
# ------- ModelPlayAnimation ------- #
# ------- NodeDesc ------- #
class Type(Enum):
	TYPE_BOX = 0
	TYPE_TEXT = 1
	TYPE_PIE = 2
	TYPE_TEMPLATE = 3
	TYPE_SPINE = 4
	TYPE_PARTICLEFX = 5
	TYPE_CUSTOM = 6
class BlendMode(Enum):
	BLEND_MODE_ALPHA = 0
	BLEND_MODE_ADD = 1
	BLEND_MODE_ADD_ALPHA = 2
	BLEND_MODE_MULT = 3
	BLEND_MODE_SCREEN = 4
class ClippingMode(Enum):
	CLIPPING_MODE_NONE = 0
	CLIPPING_MODE_STENCIL = 2
class XAnchor(Enum):
	XANCHOR_NONE = 0
	XANCHOR_LEFT = 1
	XANCHOR_RIGHT = 2
class YAnchor(Enum):
	YANCHOR_NONE = 0
	YANCHOR_TOP = 1
	YANCHOR_BOTTOM = 2
class Pivot(Enum):
	PIVOT_CENTER = 0
	PIVOT_N = 1
	PIVOT_NE = 2
	PIVOT_E = 3
	PIVOT_SE = 4
	PIVOT_S = 5
	PIVOT_SW = 6
	PIVOT_W = 7
	PIVOT_NW = 8
class AdjustMode(Enum):
	ADJUST_MODE_FIT = 0
	ADJUST_MODE_ZOOM = 1
	ADJUST_MODE_STRETCH = 2
class SizeMode(Enum):
	SIZE_MODE_MANUAL = 0
	SIZE_MODE_AUTO = 1
class PieBounds(Enum):
	PIEBOUNDS_RECTANGLE = 0
	PIEBOUNDS_ELLIPSE = 1
# ------- PathSettings ------- #
# ------- PauseSound ------- #
# ------- PlatformProfile ------- #
class OS(Enum):
	OS_ID_GENERIC = 0
	OS_ID_WINDOWS = 1
	OS_ID_OSX = 2
	OS_ID_LINUX = 3
	OS_ID_IOS = 4
	OS_ID_ANDROID = 5
	OS_ID_WEB = 6
	OS_ID_SWITCH = 7
	OS_ID_PS4 = 8
	OS_ID_PS5 = 9
	OS_ID_XBOX = 10
# ------- PlayAnimation ------- #
# ------- PlayParticleFX ------- #
# ------- PlaySound ------- #
# ------- Point3 ------- #
# ------- PropertyDeclarationEntry ------- #
# ------- PropertyDeclarations ------- #
# ------- PropertyDesc ------- #
# ------- PrototypeDesc ------- #
# ------- Quat ------- #
# ------- RayCastMissed ------- #
# ------- RayCastResponse ------- #
# ------- Reboot ------- #
# ------- ReleaseCameraFocus ------- #
# ------- ReleaseInputFocus ------- #
# ------- Reload ------- #
# ------- RenderPrototypeDesc ------- #
# ------- RequestVelocity ------- #
# ------- ResetConstant ------- #
# ------- ResetConstantParticleFX ------- #
# ------- ResetConstantTileMap ------- #
# ------- Resize ------- #
# ------- ResourceEntry ------- #
# ------- ResumeRendering ------- #
# ------- RunScript ------- #
# ------- SceneDesc ------- #
class AdjustReference(Enum):
	ADJUST_REFERENCE_LEGACY = 0
	ADJUST_REFERENCE_PARENT = 1
	ADJUST_REFERENCE_DISABLED = 2
# ------- ScriptMessage ------- #
# ------- ScriptUnrefMessage ------- #
# ------- SetCamera ------- #
# ------- SetConstant ------- #
# ------- SetConstantParticleFX ------- #
# ------- SetConstantTileMap ------- #
# ------- SetFlipHorizontal ------- #
# ------- SetFlipVertical ------- #
# ------- SetGain ------- #
# ------- SetGridShapeHull ------- #
# ------- SetLight ------- #
# ------- SetPan ------- #
# ------- SetParent ------- #
# ------- SetScale ------- #
# ------- SetSpeed ------- #
# ------- SetText ------- #
# ------- SetTexture ------- #
# ------- SetTimeStep ------- #
# ------- SetUpdateFrequency ------- #
# ------- SetViewProjection ------- #
# ------- SetVsync ------- #
# ------- ShaderDesc ------- #
class Language(Enum):
	LANGUAGE_GLSL_SM120 = 1
	LANGUAGE_GLES_SM100 = 2
	LANGUAGE_GLES_SM300 = 3
	LANGUAGE_SPIRV = 4
	LANGUAGE_PSSL = 5
	LANGUAGE_GLSL_SM430 = 6
	LANGUAGE_GLSL_SM330 = 7
	LANGUAGE_WGSL = 8
	LANGUAGE_HLSL_50 = 9
	LANGUAGE_HLSL_51 = 10
class ShaderType(Enum):
	SHADER_TYPE_VERTEX = 0
	SHADER_TYPE_FRAGMENT = 1
	SHADER_TYPE_COMPUTE = 2
class ShaderDataType(Enum):
	SHADER_TYPE_UNKNOWN = 0
	SHADER_TYPE_INT = 1
	SHADER_TYPE_UINT = 2
	SHADER_TYPE_FLOAT = 3
	SHADER_TYPE_VEC2 = 4
	SHADER_TYPE_VEC3 = 5
	SHADER_TYPE_VEC4 = 6
	SHADER_TYPE_MAT2 = 7
	SHADER_TYPE_MAT3 = 8
	SHADER_TYPE_MAT4 = 9
	SHADER_TYPE_SAMPLER2D = 10
	SHADER_TYPE_SAMPLER3D = 11
	SHADER_TYPE_SAMPLER_CUBE = 12
	SHADER_TYPE_SAMPLER2D_ARRAY = 13
	SHADER_TYPE_UNIFORM_BUFFER = 14
	SHADER_TYPE_UVEC2 = 15
	SHADER_TYPE_UVEC3 = 16
	SHADER_TYPE_UVEC4 = 17
	SHADER_TYPE_TEXTURE2D = 18
	SHADER_TYPE_UTEXTURE2D = 19
	SHADER_TYPE_RENDER_PASS_INPUT = 20
	SHADER_TYPE_UIMAGE2D = 21
	SHADER_TYPE_IMAGE2D = 22
	SHADER_TYPE_SAMPLER = 23
	SHADER_TYPE_STORAGE_BUFFER = 24
	SHADER_TYPE_TEXTURE2D_ARRAY = 25
	SHADER_TYPE_TEXTURE_CUBE = 26
	SHADER_TYPE_TEXTURE3D = 27
	SHADER_TYPE_UTEXTURE3D = 28
	SHADER_TYPE_UIMAGE3D = 29
	SHADER_TYPE_IMAGE3D = 30
	SHADER_TYPE_SAMPLER3D_ARRAY = 31
	SHADER_TYPE_TEXTURE3D_ARRAY = 32
# ------- SoundDesc ------- #
# ------- SoundEvent ------- #
# ------- SpriteDesc ------- #
class BlendMode(Enum):
	BLEND_MODE_ALPHA = 0
	BLEND_MODE_ADD = 1
	BLEND_MODE_ADD_ALPHA = 2
	BLEND_MODE_MULT = 3
	BLEND_MODE_SCREEN = 4
class SizeMode(Enum):
	SIZE_MODE_MANUAL = 0
	SIZE_MODE_AUTO = 1
# ------- SpriteGeometry ------- #
# ------- SpriteTexture ------- #
# ------- StartRecord ------- #
# ------- StopParticleFX ------- #
# ------- StopRecord ------- #
# ------- StopSound ------- #
# ------- StreamDesc ------- #
# ------- Texture ------- #
# ------- TextureFormatAlternative ------- #
class CompressionLevel(Enum):
	FAST = 0
	NORMAL = 1
	HIGH = 2
	BEST = 3
# ------- TextureImage ------- #
class Type(Enum):
	TYPE_2D = 1
	TYPE_CUBEMAP = 2
	TYPE_2D_ARRAY = 3
	TYPE_2D_IMAGE = 4
	TYPE_3D = 5
	TYPE_3D_IMAGE = 6
class CompressionType(Enum):
	COMPRESSION_TYPE_DEFAULT = 0
	COMPRESSION_TYPE_WEBP = 1
	COMPRESSION_TYPE_WEBP_LOSSY = 2
	COMPRESSION_TYPE_BASIS_UASTC = 3
	COMPRESSION_TYPE_BASIS_ETC1S = 4
	COMPRESSION_TYPE_ASTC = 5
class CompressionFlags(Enum):
	COMPRESSION_FLAG_ALPHA_CLEAN = 1
class TextureFormat(Enum):
	TEXTURE_FORMAT_LUMINANCE = 0
	TEXTURE_FORMAT_RGB = 1
	TEXTURE_FORMAT_RGBA = 2
	TEXTURE_FORMAT_RGB_PVRTC_2BPPV1 = 3
	TEXTURE_FORMAT_RGB_PVRTC_4BPPV1 = 4
	TEXTURE_FORMAT_RGBA_PVRTC_2BPPV1 = 5
	TEXTURE_FORMAT_RGBA_PVRTC_4BPPV1 = 6
	TEXTURE_FORMAT_RGB_ETC1 = 7
	TEXTURE_FORMAT_RGB_16BPP = 8
	TEXTURE_FORMAT_RGBA_16BPP = 9
	TEXTURE_FORMAT_LUMINANCE_ALPHA = 10
	TEXTURE_FORMAT_RGBA_ETC2 = 11
	TEXTURE_FORMAT_RGBA_ASTC_4X4 = 12
	TEXTURE_FORMAT_RGBA_ASTC_4x4 = 12
	TEXTURE_FORMAT_RGB_BC1 = 13
	TEXTURE_FORMAT_RGBA_BC3 = 14
	TEXTURE_FORMAT_R_BC4 = 15
	TEXTURE_FORMAT_RG_BC5 = 16
	TEXTURE_FORMAT_RGBA_BC7 = 17
	TEXTURE_FORMAT_RGB16F = 18
	TEXTURE_FORMAT_RGB32F = 19
	TEXTURE_FORMAT_RGBA16F = 20
	TEXTURE_FORMAT_RGBA32F = 21
	TEXTURE_FORMAT_R16F = 22
	TEXTURE_FORMAT_RG16F = 23
	TEXTURE_FORMAT_R32F = 24
	TEXTURE_FORMAT_RG32F = 25
	TEXTURE_FORMAT_RGBA_ASTC_5X4 = 26
	TEXTURE_FORMAT_RGBA_ASTC_5X5 = 27
	TEXTURE_FORMAT_RGBA_ASTC_6X5 = 28
	TEXTURE_FORMAT_RGBA_ASTC_6X6 = 29
	TEXTURE_FORMAT_RGBA_ASTC_8X5 = 30
	TEXTURE_FORMAT_RGBA_ASTC_8X6 = 31
	TEXTURE_FORMAT_RGBA_ASTC_8X8 = 32
	TEXTURE_FORMAT_RGBA_ASTC_10X5 = 33
	TEXTURE_FORMAT_RGBA_ASTC_10X6 = 34
	TEXTURE_FORMAT_RGBA_ASTC_10X8 = 35
	TEXTURE_FORMAT_RGBA_ASTC_10X10 = 36
	TEXTURE_FORMAT_RGBA_ASTC_12X10 = 37
	TEXTURE_FORMAT_RGBA_ASTC_12X12 = 38
# ------- TextureProfile ------- #
# ------- TextureProfiles ------- #
# ------- TextureSet ------- #
# ------- TextureSetAnimation ------- #
# ------- TileCell ------- #
# ------- TileGrid ------- #
class BlendMode(Enum):
	BLEND_MODE_ALPHA = 0
	BLEND_MODE_ADD = 1
	BLEND_MODE_ADD_ALPHA = 2
	BLEND_MODE_MULT = 3
	BLEND_MODE_SCREEN = 4
# ------- TileLayer ------- #
# ------- TileSet ------- #
# ------- TogglePhysicsDebug ------- #
# ------- ToggleProfile ------- #
# ------- Transform ------- #
# ------- Trigger ------- #
# ------- TriggerEvent ------- #
# ------- TriggerResponse ------- #
# ------- Vector3 ------- #
# ------- Vector3One ------- #
# ------- Vector4 ------- #
# ------- Vector4One ------- #
# ------- Vector4WOne ------- #
# ------- VelocityResponse ------- #
# ------- VertexAttribute ------- #
class DataType(Enum):
	TYPE_BYTE = 1
	TYPE_UNSIGNED_BYTE = 2
	TYPE_SHORT = 3
	TYPE_UNSIGNED_SHORT = 4
	TYPE_INT = 5
	TYPE_UNSIGNED_INT = 6
	TYPE_FLOAT = 7
class VectorType(Enum):
	VECTOR_TYPE_SCALAR = 1
	VECTOR_TYPE_VEC2 = 2
	VECTOR_TYPE_VEC3 = 3
	VECTOR_TYPE_VEC4 = 4
	VECTOR_TYPE_MAT2 = 5
	VECTOR_TYPE_MAT3 = 6
	VECTOR_TYPE_MAT4 = 7
class SemanticType(Enum):
	SEMANTIC_TYPE_NONE = 1
	SEMANTIC_TYPE_POSITION = 2
	SEMANTIC_TYPE_TEXCOORD = 3
	SEMANTIC_TYPE_PAGE_INDEX = 4
	SEMANTIC_TYPE_COLOR = 5
	SEMANTIC_TYPE_NORMAL = 6
	SEMANTIC_TYPE_TANGENT = 7
	SEMANTIC_TYPE_WORLD_MATRIX = 8
	SEMANTIC_TYPE_NORMAL_MATRIX = 9
	SEMANTIC_TYPE_BONE_WEIGHTS = 10
	SEMANTIC_TYPE_BONE_INDICES = 11
# ------- WindowResized ------- ## ------- AcquireCameraFocus ------- #
class AcquireCameraFocus(QObject) :
	__PROTO__ = sdk.AcquireCameraFocus
	def __init__(self) -> AcquireCameraFocus :
		pass
# ------- AcquireInputFocus ------- #
class AcquireInputFocus(QObject) :
	__PROTO__ = sdk.AcquireInputFocus
	def __init__(self) -> AcquireInputFocus :
		pass
# ------- Animation ------- #
class Animation(QObject) :
	__PROTO__ = sdk.Animation
	def __init__(self,id :str = str() ,start_tile :int = int() ,end_tile :int = int() ,playback :int = int() ,fps :int = int() ,flip_horizontal :int = int() ,flip_vertical :int = int() ,cues :List[Cue] = []) -> Animation :
		self._id = id
		self._start_tile = start_tile
		self._end_tile = end_tile
		self._playback = playback
		self._fps = fps
		self._flip_horizontal = flip_horizontal
		self._flip_vertical = flip_vertical
		self._cues = cues
		pass
	def getid(self) -> str :
		return self._id

	def setid(self,value : str) :
		if self._id != value:
			self._id = value
			self.idChanged.emit(value)

	id = pyqtProperty(str, fget=getid, fset=setid, notify=idChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.id.extend(self._id)
		instance.start_tile.extend(self._start_tile)
		instance.end_tile.extend(self._end_tile)
		instance.playback.extend(self._playback)
		instance.fps.extend(self._fps)
		instance.flip_horizontal.extend(self._flip_horizontal)
		instance.flip_vertical.extend(self._flip_vertical)
		instance.cues.extend([i.proto() for i in self._cues])

	def getstart_tile(self) -> int :
		return self._start_tile

	def setstart_tile(self,value : int) :
		if self._start_tile != value:
			self._start_tile = value
			self.start_tileChanged.emit(value)

	start_tile = pyqtProperty(int, fget=getstart_tile, fset=setstart_tile, notify=start_tileChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.id.extend(self._id)
		instance.start_tile.extend(self._start_tile)
		instance.end_tile.extend(self._end_tile)
		instance.playback.extend(self._playback)
		instance.fps.extend(self._fps)
		instance.flip_horizontal.extend(self._flip_horizontal)
		instance.flip_vertical.extend(self._flip_vertical)
		instance.cues.extend([i.proto() for i in self._cues])

	def getend_tile(self) -> int :
		return self._end_tile

	def setend_tile(self,value : int) :
		if self._end_tile != value:
			self._end_tile = value
			self.end_tileChanged.emit(value)

	end_tile = pyqtProperty(int, fget=getend_tile, fset=setend_tile, notify=end_tileChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.id.extend(self._id)
		instance.start_tile.extend(self._start_tile)
		instance.end_tile.extend(self._end_tile)
		instance.playback.extend(self._playback)
		instance.fps.extend(self._fps)
		instance.flip_horizontal.extend(self._flip_horizontal)
		instance.flip_vertical.extend(self._flip_vertical)
		instance.cues.extend([i.proto() for i in self._cues])

	def getplayback(self) -> int :
		return self._playback

	def setplayback(self,value : int) :
		if self._playback != value:
			self._playback = value
			self.playbackChanged.emit(value)

	playback = pyqtProperty(int, fget=getplayback, fset=setplayback, notify=playbackChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.id.extend(self._id)
		instance.start_tile.extend(self._start_tile)
		instance.end_tile.extend(self._end_tile)
		instance.playback.extend(self._playback)
		instance.fps.extend(self._fps)
		instance.flip_horizontal.extend(self._flip_horizontal)
		instance.flip_vertical.extend(self._flip_vertical)
		instance.cues.extend([i.proto() for i in self._cues])

	def getfps(self) -> int :
		return self._fps

	def setfps(self,value : int) :
		if self._fps != value:
			self._fps = value
			self.fpsChanged.emit(value)

	fps = pyqtProperty(int, fget=getfps, fset=setfps, notify=fpsChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.id.extend(self._id)
		instance.start_tile.extend(self._start_tile)
		instance.end_tile.extend(self._end_tile)
		instance.playback.extend(self._playback)
		instance.fps.extend(self._fps)
		instance.flip_horizontal.extend(self._flip_horizontal)
		instance.flip_vertical.extend(self._flip_vertical)
		instance.cues.extend([i.proto() for i in self._cues])

	def getflip_horizontal(self) -> int :
		return self._flip_horizontal

	def setflip_horizontal(self,value : int) :
		if self._flip_horizontal != value:
			self._flip_horizontal = value
			self.flip_horizontalChanged.emit(value)

	flip_horizontal = pyqtProperty(int, fget=getflip_horizontal, fset=setflip_horizontal, notify=flip_horizontalChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.id.extend(self._id)
		instance.start_tile.extend(self._start_tile)
		instance.end_tile.extend(self._end_tile)
		instance.playback.extend(self._playback)
		instance.fps.extend(self._fps)
		instance.flip_horizontal.extend(self._flip_horizontal)
		instance.flip_vertical.extend(self._flip_vertical)
		instance.cues.extend([i.proto() for i in self._cues])

	def getflip_vertical(self) -> int :
		return self._flip_vertical

	def setflip_vertical(self,value : int) :
		if self._flip_vertical != value:
			self._flip_vertical = value
			self.flip_verticalChanged.emit(value)

	flip_vertical = pyqtProperty(int, fget=getflip_vertical, fset=setflip_vertical, notify=flip_verticalChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.id.extend(self._id)
		instance.start_tile.extend(self._start_tile)
		instance.end_tile.extend(self._end_tile)
		instance.playback.extend(self._playback)
		instance.fps.extend(self._fps)
		instance.flip_horizontal.extend(self._flip_horizontal)
		instance.flip_vertical.extend(self._flip_vertical)
		instance.cues.extend([i.proto() for i in self._cues])

	def getcues(self) -> Cue :
		return self._cues

	def setcues(self,value : List[Cue]) :
		if self._cues != value:
			self._cues = value
			self.cuesChanged.emit(value)

	cues = pyqtProperty(List, fget=getcues, fset=setcues, notify=cuesChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.id.extend(self._id)
		instance.start_tile.extend(self._start_tile)
		instance.end_tile.extend(self._end_tile)
		instance.playback.extend(self._playback)
		instance.fps.extend(self._fps)
		instance.flip_horizontal.extend(self._flip_horizontal)
		instance.flip_vertical.extend(self._flip_vertical)
		instance.cues.extend([i.proto() for i in self._cues])

# ------- AnimationDone ------- #
class AnimationDone(QObject) :
	__PROTO__ = sdk.AnimationDone
	def __init__(self,current_tile :int = int() ,id :int = int() ) -> AnimationDone :
		self._current_tile = current_tile
		self._id = id
		pass
	def getcurrent_tile(self) -> int :
		return self._current_tile

	def setcurrent_tile(self,value : int) :
		if self._current_tile != value:
			self._current_tile = value
			self.current_tileChanged.emit(value)

	current_tile = pyqtProperty(int, fget=getcurrent_tile, fset=setcurrent_tile, notify=current_tileChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.current_tile.extend(self._current_tile)
		instance.id.extend(self._id)

	def getid(self) -> int :
		return self._id

	def setid(self,value : int) :
		if self._id != value:
			self._id = value
			self.idChanged.emit(value)

	id = pyqtProperty(int, fget=getid, fset=setid, notify=idChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.current_tile.extend(self._current_tile)
		instance.id.extend(self._id)

# ------- ApplyForce ------- #
class ApplyForce(QObject) :
	__PROTO__ = sdk.ApplyForce
	def __init__(self,force :Vector3 = None ,position :Point3 = None ) -> ApplyForce :
		self._force = force
		self._position = position
		pass
	def getforce(self) -> Vector3 :
		return self._force

	def setforce(self,value : Vector3) :
		if self._force != value:
			self._force = value
			self.forceChanged.emit(value)

	force = pyqtProperty(QObject, fget=getforce, fset=setforce, notify=forceChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.force = self._force.proto()
		instance.position = self._position.proto()

	def getposition(self) -> Point3 :
		return self._position

	def setposition(self,value : Point3) :
		if self._position != value:
			self._position = value
			self.positionChanged.emit(value)

	position = pyqtProperty(QObject, fget=getposition, fset=setposition, notify=positionChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.force = self._force.proto()
		instance.position = self._position.proto()

# ------- Atlas ------- #
class Atlas(QObject) :
	__PROTO__ = sdk.Atlas
	def __init__(self,images :List[AtlasImage] = [],animations :List[AtlasAnimation] = [],margin :int = int() ,extrude_borders :int = int() ,inner_padding :int = int() ,max_page_width :int = int() ,max_page_height :int = int() ,rename_patterns :str = str() ) -> Atlas :
		self._images = images
		self._animations = animations
		self._margin = margin
		self._extrude_borders = extrude_borders
		self._inner_padding = inner_padding
		self._max_page_width = max_page_width
		self._max_page_height = max_page_height
		self._rename_patterns = rename_patterns
		pass
	def getimages(self) -> AtlasImage :
		return self._images

	def setimages(self,value : List[AtlasImage]) :
		if self._images != value:
			self._images = value
			self.imagesChanged.emit(value)

	images = pyqtProperty(List, fget=getimages, fset=setimages, notify=imagesChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.images.extend([i.proto() for i in self._images])
		instance.animations.extend([i.proto() for i in self._animations])
		instance.margin.extend(self._margin)
		instance.extrude_borders.extend(self._extrude_borders)
		instance.inner_padding.extend(self._inner_padding)
		instance.max_page_width.extend(self._max_page_width)
		instance.max_page_height.extend(self._max_page_height)
		instance.rename_patterns.extend(self._rename_patterns)

	def getanimations(self) -> AtlasAnimation :
		return self._animations

	def setanimations(self,value : List[AtlasAnimation]) :
		if self._animations != value:
			self._animations = value
			self.animationsChanged.emit(value)

	animations = pyqtProperty(List, fget=getanimations, fset=setanimations, notify=animationsChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.images.extend([i.proto() for i in self._images])
		instance.animations.extend([i.proto() for i in self._animations])
		instance.margin.extend(self._margin)
		instance.extrude_borders.extend(self._extrude_borders)
		instance.inner_padding.extend(self._inner_padding)
		instance.max_page_width.extend(self._max_page_width)
		instance.max_page_height.extend(self._max_page_height)
		instance.rename_patterns.extend(self._rename_patterns)

	def getmargin(self) -> int :
		return self._margin

	def setmargin(self,value : int) :
		if self._margin != value:
			self._margin = value
			self.marginChanged.emit(value)

	margin = pyqtProperty(int, fget=getmargin, fset=setmargin, notify=marginChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.images.extend([i.proto() for i in self._images])
		instance.animations.extend([i.proto() for i in self._animations])
		instance.margin.extend(self._margin)
		instance.extrude_borders.extend(self._extrude_borders)
		instance.inner_padding.extend(self._inner_padding)
		instance.max_page_width.extend(self._max_page_width)
		instance.max_page_height.extend(self._max_page_height)
		instance.rename_patterns.extend(self._rename_patterns)

	def getextrude_borders(self) -> int :
		return self._extrude_borders

	def setextrude_borders(self,value : int) :
		if self._extrude_borders != value:
			self._extrude_borders = value
			self.extrude_bordersChanged.emit(value)

	extrude_borders = pyqtProperty(int, fget=getextrude_borders, fset=setextrude_borders, notify=extrude_bordersChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.images.extend([i.proto() for i in self._images])
		instance.animations.extend([i.proto() for i in self._animations])
		instance.margin.extend(self._margin)
		instance.extrude_borders.extend(self._extrude_borders)
		instance.inner_padding.extend(self._inner_padding)
		instance.max_page_width.extend(self._max_page_width)
		instance.max_page_height.extend(self._max_page_height)
		instance.rename_patterns.extend(self._rename_patterns)

	def getinner_padding(self) -> int :
		return self._inner_padding

	def setinner_padding(self,value : int) :
		if self._inner_padding != value:
			self._inner_padding = value
			self.inner_paddingChanged.emit(value)

	inner_padding = pyqtProperty(int, fget=getinner_padding, fset=setinner_padding, notify=inner_paddingChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.images.extend([i.proto() for i in self._images])
		instance.animations.extend([i.proto() for i in self._animations])
		instance.margin.extend(self._margin)
		instance.extrude_borders.extend(self._extrude_borders)
		instance.inner_padding.extend(self._inner_padding)
		instance.max_page_width.extend(self._max_page_width)
		instance.max_page_height.extend(self._max_page_height)
		instance.rename_patterns.extend(self._rename_patterns)

	def getmax_page_width(self) -> int :
		return self._max_page_width

	def setmax_page_width(self,value : int) :
		if self._max_page_width != value:
			self._max_page_width = value
			self.max_page_widthChanged.emit(value)

	max_page_width = pyqtProperty(int, fget=getmax_page_width, fset=setmax_page_width, notify=max_page_widthChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.images.extend([i.proto() for i in self._images])
		instance.animations.extend([i.proto() for i in self._animations])
		instance.margin.extend(self._margin)
		instance.extrude_borders.extend(self._extrude_borders)
		instance.inner_padding.extend(self._inner_padding)
		instance.max_page_width.extend(self._max_page_width)
		instance.max_page_height.extend(self._max_page_height)
		instance.rename_patterns.extend(self._rename_patterns)

	def getmax_page_height(self) -> int :
		return self._max_page_height

	def setmax_page_height(self,value : int) :
		if self._max_page_height != value:
			self._max_page_height = value
			self.max_page_heightChanged.emit(value)

	max_page_height = pyqtProperty(int, fget=getmax_page_height, fset=setmax_page_height, notify=max_page_heightChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.images.extend([i.proto() for i in self._images])
		instance.animations.extend([i.proto() for i in self._animations])
		instance.margin.extend(self._margin)
		instance.extrude_borders.extend(self._extrude_borders)
		instance.inner_padding.extend(self._inner_padding)
		instance.max_page_width.extend(self._max_page_width)
		instance.max_page_height.extend(self._max_page_height)
		instance.rename_patterns.extend(self._rename_patterns)

	def getrename_patterns(self) -> str :
		return self._rename_patterns

	def setrename_patterns(self,value : str) :
		if self._rename_patterns != value:
			self._rename_patterns = value
			self.rename_patternsChanged.emit(value)

	rename_patterns = pyqtProperty(str, fget=getrename_patterns, fset=setrename_patterns, notify=rename_patternsChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.images.extend([i.proto() for i in self._images])
		instance.animations.extend([i.proto() for i in self._animations])
		instance.margin.extend(self._margin)
		instance.extrude_borders.extend(self._extrude_borders)
		instance.inner_padding.extend(self._inner_padding)
		instance.max_page_width.extend(self._max_page_width)
		instance.max_page_height.extend(self._max_page_height)
		instance.rename_patterns.extend(self._rename_patterns)

# ------- AtlasAnimation ------- #
class AtlasAnimation(QObject) :
	__PROTO__ = sdk.AtlasAnimation
	def __init__(self,id :str = str() ,images :List[AtlasImage] = [],playback :int = int() ,fps :int = int() ,flip_horizontal :int = int() ,flip_vertical :int = int() ) -> AtlasAnimation :
		self._id = id
		self._images = images
		self._playback = playback
		self._fps = fps
		self._flip_horizontal = flip_horizontal
		self._flip_vertical = flip_vertical
		pass
	def getid(self) -> str :
		return self._id

	def setid(self,value : str) :
		if self._id != value:
			self._id = value
			self.idChanged.emit(value)

	id = pyqtProperty(str, fget=getid, fset=setid, notify=idChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.id.extend(self._id)
		instance.images.extend([i.proto() for i in self._images])
		instance.playback.extend(self._playback)
		instance.fps.extend(self._fps)
		instance.flip_horizontal.extend(self._flip_horizontal)
		instance.flip_vertical.extend(self._flip_vertical)

	def getimages(self) -> AtlasImage :
		return self._images

	def setimages(self,value : List[AtlasImage]) :
		if self._images != value:
			self._images = value
			self.imagesChanged.emit(value)

	images = pyqtProperty(List, fget=getimages, fset=setimages, notify=imagesChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.id.extend(self._id)
		instance.images.extend([i.proto() for i in self._images])
		instance.playback.extend(self._playback)
		instance.fps.extend(self._fps)
		instance.flip_horizontal.extend(self._flip_horizontal)
		instance.flip_vertical.extend(self._flip_vertical)

	def getplayback(self) -> int :
		return self._playback

	def setplayback(self,value : int) :
		if self._playback != value:
			self._playback = value
			self.playbackChanged.emit(value)

	playback = pyqtProperty(int, fget=getplayback, fset=setplayback, notify=playbackChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.id.extend(self._id)
		instance.images.extend([i.proto() for i in self._images])
		instance.playback.extend(self._playback)
		instance.fps.extend(self._fps)
		instance.flip_horizontal.extend(self._flip_horizontal)
		instance.flip_vertical.extend(self._flip_vertical)

	def getfps(self) -> int :
		return self._fps

	def setfps(self,value : int) :
		if self._fps != value:
			self._fps = value
			self.fpsChanged.emit(value)

	fps = pyqtProperty(int, fget=getfps, fset=setfps, notify=fpsChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.id.extend(self._id)
		instance.images.extend([i.proto() for i in self._images])
		instance.playback.extend(self._playback)
		instance.fps.extend(self._fps)
		instance.flip_horizontal.extend(self._flip_horizontal)
		instance.flip_vertical.extend(self._flip_vertical)

	def getflip_horizontal(self) -> int :
		return self._flip_horizontal

	def setflip_horizontal(self,value : int) :
		if self._flip_horizontal != value:
			self._flip_horizontal = value
			self.flip_horizontalChanged.emit(value)

	flip_horizontal = pyqtProperty(int, fget=getflip_horizontal, fset=setflip_horizontal, notify=flip_horizontalChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.id.extend(self._id)
		instance.images.extend([i.proto() for i in self._images])
		instance.playback.extend(self._playback)
		instance.fps.extend(self._fps)
		instance.flip_horizontal.extend(self._flip_horizontal)
		instance.flip_vertical.extend(self._flip_vertical)

	def getflip_vertical(self) -> int :
		return self._flip_vertical

	def setflip_vertical(self,value : int) :
		if self._flip_vertical != value:
			self._flip_vertical = value
			self.flip_verticalChanged.emit(value)

	flip_vertical = pyqtProperty(int, fget=getflip_vertical, fset=setflip_vertical, notify=flip_verticalChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.id.extend(self._id)
		instance.images.extend([i.proto() for i in self._images])
		instance.playback.extend(self._playback)
		instance.fps.extend(self._fps)
		instance.flip_horizontal.extend(self._flip_horizontal)
		instance.flip_vertical.extend(self._flip_vertical)

# ------- AtlasImage ------- #
class AtlasImage(QObject) :
	__PROTO__ = sdk.AtlasImage
	def __init__(self,image :str = str() ,sprite_trim_mode :int = int() ,pivot_x :float = float() ,pivot_y :float = float() ) -> AtlasImage :
		self._image = image
		self._sprite_trim_mode = sprite_trim_mode
		self._pivot_x = pivot_x
		self._pivot_y = pivot_y
		pass
	def getimage(self) -> str :
		return self._image

	def setimage(self,value : str) :
		if self._image != value:
			self._image = value
			self.imageChanged.emit(value)

	image = pyqtProperty(str, fget=getimage, fset=setimage, notify=imageChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.image.extend(self._image)
		instance.sprite_trim_mode.extend(self._sprite_trim_mode)
		instance.pivot_x.extend(self._pivot_x)
		instance.pivot_y.extend(self._pivot_y)

	def getsprite_trim_mode(self) -> int :
		return self._sprite_trim_mode

	def setsprite_trim_mode(self,value : int) :
		if self._sprite_trim_mode != value:
			self._sprite_trim_mode = value
			self.sprite_trim_modeChanged.emit(value)

	sprite_trim_mode = pyqtProperty(int, fget=getsprite_trim_mode, fset=setsprite_trim_mode, notify=sprite_trim_modeChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.image.extend(self._image)
		instance.sprite_trim_mode.extend(self._sprite_trim_mode)
		instance.pivot_x.extend(self._pivot_x)
		instance.pivot_y.extend(self._pivot_y)

	def getpivot_x(self) -> float :
		return self._pivot_x

	def setpivot_x(self,value : float) :
		if self._pivot_x != value:
			self._pivot_x = value
			self.pivot_xChanged.emit(value)

	pivot_x = pyqtProperty(float, fget=getpivot_x, fset=setpivot_x, notify=pivot_xChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.image.extend(self._image)
		instance.sprite_trim_mode.extend(self._sprite_trim_mode)
		instance.pivot_x.extend(self._pivot_x)
		instance.pivot_y.extend(self._pivot_y)

	def getpivot_y(self) -> float :
		return self._pivot_y

	def setpivot_y(self,value : float) :
		if self._pivot_y != value:
			self._pivot_y = value
			self.pivot_yChanged.emit(value)

	pivot_y = pyqtProperty(float, fget=getpivot_y, fset=setpivot_y, notify=pivot_yChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.image.extend(self._image)
		instance.sprite_trim_mode.extend(self._sprite_trim_mode)
		instance.pivot_x.extend(self._pivot_x)
		instance.pivot_y.extend(self._pivot_y)

# ------- BufferDesc ------- #
class BufferDesc(QObject) :
	__PROTO__ = sdk.BufferDesc
	def __init__(self,streams :List[StreamDesc] = []) -> BufferDesc :
		self._streams = streams
		pass
	def getstreams(self) -> StreamDesc :
		return self._streams

	def setstreams(self,value : List[StreamDesc]) :
		if self._streams != value:
			self._streams = value
			self.streamsChanged.emit(value)

	streams = pyqtProperty(List, fget=getstreams, fset=setstreams, notify=streamsChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.streams.extend([i.proto() for i in self._streams])

# ------- CameraDesc ------- #
class CameraDesc(QObject) :
	__PROTO__ = sdk.CameraDesc
	def __init__(self,aspect_ratio :float = float() ,fov :float = float() ,near_z :float = float() ,far_z :float = float() ,auto_aspect_ratio :int = int() ,orthographic_projection :int = int() ,orthographic_zoom :float = float() ,orthographic_mode :int = int() ) -> CameraDesc :
		self._aspect_ratio = aspect_ratio
		self._fov = fov
		self._near_z = near_z
		self._far_z = far_z
		self._auto_aspect_ratio = auto_aspect_ratio
		self._orthographic_projection = orthographic_projection
		self._orthographic_zoom = orthographic_zoom
		self._orthographic_mode = orthographic_mode
		pass
	def getaspect_ratio(self) -> float :
		return self._aspect_ratio

	def setaspect_ratio(self,value : float) :
		if self._aspect_ratio != value:
			self._aspect_ratio = value
			self.aspect_ratioChanged.emit(value)

	aspect_ratio = pyqtProperty(float, fget=getaspect_ratio, fset=setaspect_ratio, notify=aspect_ratioChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.aspect_ratio.extend(self._aspect_ratio)
		instance.fov.extend(self._fov)
		instance.near_z.extend(self._near_z)
		instance.far_z.extend(self._far_z)
		instance.auto_aspect_ratio.extend(self._auto_aspect_ratio)
		instance.orthographic_projection.extend(self._orthographic_projection)
		instance.orthographic_zoom.extend(self._orthographic_zoom)
		instance.orthographic_mode.extend(self._orthographic_mode)

	def getfov(self) -> float :
		return self._fov

	def setfov(self,value : float) :
		if self._fov != value:
			self._fov = value
			self.fovChanged.emit(value)

	fov = pyqtProperty(float, fget=getfov, fset=setfov, notify=fovChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.aspect_ratio.extend(self._aspect_ratio)
		instance.fov.extend(self._fov)
		instance.near_z.extend(self._near_z)
		instance.far_z.extend(self._far_z)
		instance.auto_aspect_ratio.extend(self._auto_aspect_ratio)
		instance.orthographic_projection.extend(self._orthographic_projection)
		instance.orthographic_zoom.extend(self._orthographic_zoom)
		instance.orthographic_mode.extend(self._orthographic_mode)

	def getnear_z(self) -> float :
		return self._near_z

	def setnear_z(self,value : float) :
		if self._near_z != value:
			self._near_z = value
			self.near_zChanged.emit(value)

	near_z = pyqtProperty(float, fget=getnear_z, fset=setnear_z, notify=near_zChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.aspect_ratio.extend(self._aspect_ratio)
		instance.fov.extend(self._fov)
		instance.near_z.extend(self._near_z)
		instance.far_z.extend(self._far_z)
		instance.auto_aspect_ratio.extend(self._auto_aspect_ratio)
		instance.orthographic_projection.extend(self._orthographic_projection)
		instance.orthographic_zoom.extend(self._orthographic_zoom)
		instance.orthographic_mode.extend(self._orthographic_mode)

	def getfar_z(self) -> float :
		return self._far_z

	def setfar_z(self,value : float) :
		if self._far_z != value:
			self._far_z = value
			self.far_zChanged.emit(value)

	far_z = pyqtProperty(float, fget=getfar_z, fset=setfar_z, notify=far_zChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.aspect_ratio.extend(self._aspect_ratio)
		instance.fov.extend(self._fov)
		instance.near_z.extend(self._near_z)
		instance.far_z.extend(self._far_z)
		instance.auto_aspect_ratio.extend(self._auto_aspect_ratio)
		instance.orthographic_projection.extend(self._orthographic_projection)
		instance.orthographic_zoom.extend(self._orthographic_zoom)
		instance.orthographic_mode.extend(self._orthographic_mode)

	def getauto_aspect_ratio(self) -> int :
		return self._auto_aspect_ratio

	def setauto_aspect_ratio(self,value : int) :
		if self._auto_aspect_ratio != value:
			self._auto_aspect_ratio = value
			self.auto_aspect_ratioChanged.emit(value)

	auto_aspect_ratio = pyqtProperty(int, fget=getauto_aspect_ratio, fset=setauto_aspect_ratio, notify=auto_aspect_ratioChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.aspect_ratio.extend(self._aspect_ratio)
		instance.fov.extend(self._fov)
		instance.near_z.extend(self._near_z)
		instance.far_z.extend(self._far_z)
		instance.auto_aspect_ratio.extend(self._auto_aspect_ratio)
		instance.orthographic_projection.extend(self._orthographic_projection)
		instance.orthographic_zoom.extend(self._orthographic_zoom)
		instance.orthographic_mode.extend(self._orthographic_mode)

	def getorthographic_projection(self) -> int :
		return self._orthographic_projection

	def setorthographic_projection(self,value : int) :
		if self._orthographic_projection != value:
			self._orthographic_projection = value
			self.orthographic_projectionChanged.emit(value)

	orthographic_projection = pyqtProperty(int, fget=getorthographic_projection, fset=setorthographic_projection, notify=orthographic_projectionChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.aspect_ratio.extend(self._aspect_ratio)
		instance.fov.extend(self._fov)
		instance.near_z.extend(self._near_z)
		instance.far_z.extend(self._far_z)
		instance.auto_aspect_ratio.extend(self._auto_aspect_ratio)
		instance.orthographic_projection.extend(self._orthographic_projection)
		instance.orthographic_zoom.extend(self._orthographic_zoom)
		instance.orthographic_mode.extend(self._orthographic_mode)

	def getorthographic_zoom(self) -> float :
		return self._orthographic_zoom

	def setorthographic_zoom(self,value : float) :
		if self._orthographic_zoom != value:
			self._orthographic_zoom = value
			self.orthographic_zoomChanged.emit(value)

	orthographic_zoom = pyqtProperty(float, fget=getorthographic_zoom, fset=setorthographic_zoom, notify=orthographic_zoomChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.aspect_ratio.extend(self._aspect_ratio)
		instance.fov.extend(self._fov)
		instance.near_z.extend(self._near_z)
		instance.far_z.extend(self._far_z)
		instance.auto_aspect_ratio.extend(self._auto_aspect_ratio)
		instance.orthographic_projection.extend(self._orthographic_projection)
		instance.orthographic_zoom.extend(self._orthographic_zoom)
		instance.orthographic_mode.extend(self._orthographic_mode)

	def getorthographic_mode(self) -> int :
		return self._orthographic_mode

	def setorthographic_mode(self,value : int) :
		if self._orthographic_mode != value:
			self._orthographic_mode = value
			self.orthographic_modeChanged.emit(value)

	orthographic_mode = pyqtProperty(int, fget=getorthographic_mode, fset=setorthographic_mode, notify=orthographic_modeChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.aspect_ratio.extend(self._aspect_ratio)
		instance.fov.extend(self._fov)
		instance.near_z.extend(self._near_z)
		instance.far_z.extend(self._far_z)
		instance.auto_aspect_ratio.extend(self._auto_aspect_ratio)
		instance.orthographic_projection.extend(self._orthographic_projection)
		instance.orthographic_zoom.extend(self._orthographic_zoom)
		instance.orthographic_mode.extend(self._orthographic_mode)

# ------- ClearColor ------- #
class ClearColor(QObject) :
	__PROTO__ = sdk.ClearColor
	def __init__(self,color :Vector4 = None ) -> ClearColor :
		self._color = color
		pass
	def getcolor(self) -> Vector4 :
		return self._color

	def setcolor(self,value : Vector4) :
		if self._color != value:
			self._color = value
			self.colorChanged.emit(value)

	color = pyqtProperty(QObject, fget=getcolor, fset=setcolor, notify=colorChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.color = self._color.proto()

# ------- CollectionDesc ------- #
class CollectionDesc(QObject) :
	__PROTO__ = sdk.CollectionDesc
	def __init__(self,name :str = str() ,instances :List[InstanceDesc] = [],collection_instances :List[CollectionInstanceDesc] = [],scale_along_z :int = int() ,embedded_instances :List[EmbeddedInstanceDesc] = [],property_resources :List[str] = [] ,component_types :List[ComponenTypeDesc] = []) -> CollectionDesc :
		self._name = name
		self._instances = instances
		self._collection_instances = collection_instances
		self._scale_along_z = scale_along_z
		self._embedded_instances = embedded_instances
		self._property_resources = property_resources
		self._component_types = component_types
		pass
	def getname(self) -> str :
		return self._name

	def setname(self,value : str) :
		if self._name != value:
			self._name = value
			self.nameChanged.emit(value)

	name = pyqtProperty(str, fget=getname, fset=setname, notify=nameChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.name.extend(self._name)
		instance.instances.extend([i.proto() for i in self._instances])
		instance.collection_instances.extend([i.proto() for i in self._collection_instances])
		instance.scale_along_z.extend(self._scale_along_z)
		instance.embedded_instances.extend([i.proto() for i in self._embedded_instances])
		instance.property_resources = self._property_resources
		instance.component_types.extend([i.proto() for i in self._component_types])

	def getinstances(self) -> InstanceDesc :
		return self._instances

	def setinstances(self,value : List[InstanceDesc]) :
		if self._instances != value:
			self._instances = value
			self.instancesChanged.emit(value)

	instances = pyqtProperty(List, fget=getinstances, fset=setinstances, notify=instancesChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.name.extend(self._name)
		instance.instances.extend([i.proto() for i in self._instances])
		instance.collection_instances.extend([i.proto() for i in self._collection_instances])
		instance.scale_along_z.extend(self._scale_along_z)
		instance.embedded_instances.extend([i.proto() for i in self._embedded_instances])
		instance.property_resources = self._property_resources
		instance.component_types.extend([i.proto() for i in self._component_types])

	def getcollection_instances(self) -> CollectionInstanceDesc :
		return self._collection_instances

	def setcollection_instances(self,value : List[CollectionInstanceDesc]) :
		if self._collection_instances != value:
			self._collection_instances = value
			self.collection_instancesChanged.emit(value)

	collection_instances = pyqtProperty(List, fget=getcollection_instances, fset=setcollection_instances, notify=collection_instancesChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.name.extend(self._name)
		instance.instances.extend([i.proto() for i in self._instances])
		instance.collection_instances.extend([i.proto() for i in self._collection_instances])
		instance.scale_along_z.extend(self._scale_along_z)
		instance.embedded_instances.extend([i.proto() for i in self._embedded_instances])
		instance.property_resources = self._property_resources
		instance.component_types.extend([i.proto() for i in self._component_types])

	def getscale_along_z(self) -> int :
		return self._scale_along_z

	def setscale_along_z(self,value : int) :
		if self._scale_along_z != value:
			self._scale_along_z = value
			self.scale_along_zChanged.emit(value)

	scale_along_z = pyqtProperty(int, fget=getscale_along_z, fset=setscale_along_z, notify=scale_along_zChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.name.extend(self._name)
		instance.instances.extend([i.proto() for i in self._instances])
		instance.collection_instances.extend([i.proto() for i in self._collection_instances])
		instance.scale_along_z.extend(self._scale_along_z)
		instance.embedded_instances.extend([i.proto() for i in self._embedded_instances])
		instance.property_resources = self._property_resources
		instance.component_types.extend([i.proto() for i in self._component_types])

	def getembedded_instances(self) -> EmbeddedInstanceDesc :
		return self._embedded_instances

	def setembedded_instances(self,value : List[EmbeddedInstanceDesc]) :
		if self._embedded_instances != value:
			self._embedded_instances = value
			self.embedded_instancesChanged.emit(value)

	embedded_instances = pyqtProperty(List, fget=getembedded_instances, fset=setembedded_instances, notify=embedded_instancesChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.name.extend(self._name)
		instance.instances.extend([i.proto() for i in self._instances])
		instance.collection_instances.extend([i.proto() for i in self._collection_instances])
		instance.scale_along_z.extend(self._scale_along_z)
		instance.embedded_instances.extend([i.proto() for i in self._embedded_instances])
		instance.property_resources = self._property_resources
		instance.component_types.extend([i.proto() for i in self._component_types])

	def getproperty_resources(self) -> str :
		return self._property_resources

	def setproperty_resources(self,value : List[str]) :
		if self._property_resources != value:
			self._property_resources = value
			self.property_resourcesChanged.emit(value)

	property_resources = pyqtProperty(List, fget=getproperty_resources, fset=setproperty_resources, notify=property_resourcesChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.name.extend(self._name)
		instance.instances.extend([i.proto() for i in self._instances])
		instance.collection_instances.extend([i.proto() for i in self._collection_instances])
		instance.scale_along_z.extend(self._scale_along_z)
		instance.embedded_instances.extend([i.proto() for i in self._embedded_instances])
		instance.property_resources = self._property_resources
		instance.component_types.extend([i.proto() for i in self._component_types])

	def getcomponent_types(self) -> ComponenTypeDesc :
		return self._component_types

	def setcomponent_types(self,value : List[ComponenTypeDesc]) :
		if self._component_types != value:
			self._component_types = value
			self.component_typesChanged.emit(value)

	component_types = pyqtProperty(List, fget=getcomponent_types, fset=setcomponent_types, notify=component_typesChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.name.extend(self._name)
		instance.instances.extend([i.proto() for i in self._instances])
		instance.collection_instances.extend([i.proto() for i in self._collection_instances])
		instance.scale_along_z.extend(self._scale_along_z)
		instance.embedded_instances.extend([i.proto() for i in self._embedded_instances])
		instance.property_resources = self._property_resources
		instance.component_types.extend([i.proto() for i in self._component_types])

# ------- CollectionFactoryDesc ------- #
class CollectionFactoryDesc(QObject) :
	__PROTO__ = sdk.CollectionFactoryDesc
	def __init__(self,prototype :str = str() ,load_dynamically :bool = bool() ,dynamic_prototype :bool = bool() ) -> CollectionFactoryDesc :
		self._prototype = prototype
		self._load_dynamically = load_dynamically
		self._dynamic_prototype = dynamic_prototype
		pass
	def getprototype(self) -> str :
		return self._prototype

	def setprototype(self,value : str) :
		if self._prototype != value:
			self._prototype = value
			self.prototypeChanged.emit(value)

	prototype = pyqtProperty(str, fget=getprototype, fset=setprototype, notify=prototypeChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.prototype.extend(self._prototype)
		instance.load_dynamically.extend(self._load_dynamically)
		instance.dynamic_prototype.extend(self._dynamic_prototype)

	def getload_dynamically(self) -> bool :
		return self._load_dynamically

	def setload_dynamically(self,value : bool) :
		if self._load_dynamically != value:
			self._load_dynamically = value
			self.load_dynamicallyChanged.emit(value)

	load_dynamically = pyqtProperty(bool, fget=getload_dynamically, fset=setload_dynamically, notify=load_dynamicallyChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.prototype.extend(self._prototype)
		instance.load_dynamically.extend(self._load_dynamically)
		instance.dynamic_prototype.extend(self._dynamic_prototype)

	def getdynamic_prototype(self) -> bool :
		return self._dynamic_prototype

	def setdynamic_prototype(self,value : bool) :
		if self._dynamic_prototype != value:
			self._dynamic_prototype = value
			self.dynamic_prototypeChanged.emit(value)

	dynamic_prototype = pyqtProperty(bool, fget=getdynamic_prototype, fset=setdynamic_prototype, notify=dynamic_prototypeChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.prototype.extend(self._prototype)
		instance.load_dynamically.extend(self._load_dynamically)
		instance.dynamic_prototype.extend(self._dynamic_prototype)

# ------- CollectionInstanceDesc ------- #
class CollectionInstanceDesc(QObject) :
	__PROTO__ = sdk.CollectionInstanceDesc
	def __init__(self,id :str = str() ,collection :str = str() ,position :Point3 = None ,rotation :Quat = None ,scale :float = float() ,scale3 :Vector3One = None ,instance_properties :List[InstancePropertyDesc] = []) -> CollectionInstanceDesc :
		self._id = id
		self._collection = collection
		self._position = position
		self._rotation = rotation
		self._scale = scale
		self._scale3 = scale3
		self._instance_properties = instance_properties
		pass
	def getid(self) -> str :
		return self._id

	def setid(self,value : str) :
		if self._id != value:
			self._id = value
			self.idChanged.emit(value)

	id = pyqtProperty(str, fget=getid, fset=setid, notify=idChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.id.extend(self._id)
		instance.collection.extend(self._collection)
		instance.position = self._position.proto()
		instance.rotation = self._rotation.proto()
		instance.scale.extend(self._scale)
		instance.scale3 = self._scale3.proto()
		instance.instance_properties.extend([i.proto() for i in self._instance_properties])

	def getcollection(self) -> str :
		return self._collection

	def setcollection(self,value : str) :
		if self._collection != value:
			self._collection = value
			self.collectionChanged.emit(value)

	collection = pyqtProperty(str, fget=getcollection, fset=setcollection, notify=collectionChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.id.extend(self._id)
		instance.collection.extend(self._collection)
		instance.position = self._position.proto()
		instance.rotation = self._rotation.proto()
		instance.scale.extend(self._scale)
		instance.scale3 = self._scale3.proto()
		instance.instance_properties.extend([i.proto() for i in self._instance_properties])

	def getposition(self) -> Point3 :
		return self._position

	def setposition(self,value : Point3) :
		if self._position != value:
			self._position = value
			self.positionChanged.emit(value)

	position = pyqtProperty(QObject, fget=getposition, fset=setposition, notify=positionChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.id.extend(self._id)
		instance.collection.extend(self._collection)
		instance.position = self._position.proto()
		instance.rotation = self._rotation.proto()
		instance.scale.extend(self._scale)
		instance.scale3 = self._scale3.proto()
		instance.instance_properties.extend([i.proto() for i in self._instance_properties])

	def getrotation(self) -> Quat :
		return self._rotation

	def setrotation(self,value : Quat) :
		if self._rotation != value:
			self._rotation = value
			self.rotationChanged.emit(value)

	rotation = pyqtProperty(QObject, fget=getrotation, fset=setrotation, notify=rotationChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.id.extend(self._id)
		instance.collection.extend(self._collection)
		instance.position = self._position.proto()
		instance.rotation = self._rotation.proto()
		instance.scale.extend(self._scale)
		instance.scale3 = self._scale3.proto()
		instance.instance_properties.extend([i.proto() for i in self._instance_properties])

	def getscale(self) -> float :
		return self._scale

	def setscale(self,value : float) :
		if self._scale != value:
			self._scale = value
			self.scaleChanged.emit(value)

	scale = pyqtProperty(float, fget=getscale, fset=setscale, notify=scaleChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.id.extend(self._id)
		instance.collection.extend(self._collection)
		instance.position = self._position.proto()
		instance.rotation = self._rotation.proto()
		instance.scale.extend(self._scale)
		instance.scale3 = self._scale3.proto()
		instance.instance_properties.extend([i.proto() for i in self._instance_properties])

	def getscale3(self) -> Vector3One :
		return self._scale3

	def setscale3(self,value : Vector3One) :
		if self._scale3 != value:
			self._scale3 = value
			self.scale3Changed.emit(value)

	scale3 = pyqtProperty(QObject, fget=getscale3, fset=setscale3, notify=scale3Changed)

	def proto(self) :
		instance = self.__PROTO__()
		instance.id.extend(self._id)
		instance.collection.extend(self._collection)
		instance.position = self._position.proto()
		instance.rotation = self._rotation.proto()
		instance.scale.extend(self._scale)
		instance.scale3 = self._scale3.proto()
		instance.instance_properties.extend([i.proto() for i in self._instance_properties])

	def getinstance_properties(self) -> InstancePropertyDesc :
		return self._instance_properties

	def setinstance_properties(self,value : List[InstancePropertyDesc]) :
		if self._instance_properties != value:
			self._instance_properties = value
			self.instance_propertiesChanged.emit(value)

	instance_properties = pyqtProperty(List, fget=getinstance_properties, fset=setinstance_properties, notify=instance_propertiesChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.id.extend(self._id)
		instance.collection.extend(self._collection)
		instance.position = self._position.proto()
		instance.rotation = self._rotation.proto()
		instance.scale.extend(self._scale)
		instance.scale3 = self._scale3.proto()
		instance.instance_properties.extend([i.proto() for i in self._instance_properties])

# ------- CollectionProxyDesc ------- #
class CollectionProxyDesc(QObject) :
	__PROTO__ = sdk.CollectionProxyDesc
	def __init__(self,collection :str = str() ,exclude :bool = bool() ) -> CollectionProxyDesc :
		self._collection = collection
		self._exclude = exclude
		pass
	def getcollection(self) -> str :
		return self._collection

	def setcollection(self,value : str) :
		if self._collection != value:
			self._collection = value
			self.collectionChanged.emit(value)

	collection = pyqtProperty(str, fget=getcollection, fset=setcollection, notify=collectionChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.collection.extend(self._collection)
		instance.exclude.extend(self._exclude)

	def getexclude(self) -> bool :
		return self._exclude

	def setexclude(self,value : bool) :
		if self._exclude != value:
			self._exclude = value
			self.excludeChanged.emit(value)

	exclude = pyqtProperty(bool, fget=getexclude, fset=setexclude, notify=excludeChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.collection.extend(self._collection)
		instance.exclude.extend(self._exclude)

# ------- Collision ------- #
class Collision(QObject) :
	__PROTO__ = sdk.Collision
	def __init__(self,position :Point3 = None ,id :int = int() ,group :int = int() ) -> Collision :
		self._position = position
		self._id = id
		self._group = group
		pass
	def getposition(self) -> Point3 :
		return self._position

	def setposition(self,value : Point3) :
		if self._position != value:
			self._position = value
			self.positionChanged.emit(value)

	position = pyqtProperty(QObject, fget=getposition, fset=setposition, notify=positionChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.position = self._position.proto()
		instance.id.extend(self._id)
		instance.group.extend(self._group)

	def getid(self) -> int :
		return self._id

	def setid(self,value : int) :
		if self._id != value:
			self._id = value
			self.idChanged.emit(value)

	id = pyqtProperty(int, fget=getid, fset=setid, notify=idChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.position = self._position.proto()
		instance.id.extend(self._id)
		instance.group.extend(self._group)

	def getgroup(self) -> int :
		return self._group

	def setgroup(self,value : int) :
		if self._group != value:
			self._group = value
			self.groupChanged.emit(value)

	group = pyqtProperty(int, fget=getgroup, fset=setgroup, notify=groupChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.position = self._position.proto()
		instance.id.extend(self._id)
		instance.group.extend(self._group)

# ------- CollisionEvent ------- #
class CollisionEvent(QObject) :
	__PROTO__ = sdk.CollisionEvent
	def __init__(self,a :Collision = None ,b :Collision = None ) -> CollisionEvent :
		self._a = a
		self._b = b
		pass
	def geta(self) -> Collision :
		return self._a

	def seta(self,value : Collision) :
		if self._a != value:
			self._a = value
			self.aChanged.emit(value)

	a = pyqtProperty(QObject, fget=geta, fset=seta, notify=aChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.a = self._a.proto()
		instance.b = self._b.proto()

	def getb(self) -> Collision :
		return self._b

	def setb(self,value : Collision) :
		if self._b != value:
			self._b = value
			self.bChanged.emit(value)

	b = pyqtProperty(QObject, fget=getb, fset=setb, notify=bChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.a = self._a.proto()
		instance.b = self._b.proto()

# ------- CollisionObjectDesc ------- #
class CollisionObjectDesc(QObject) :
	__PROTO__ = sdk.CollisionObjectDesc
	def __init__(self,collision_shape :str = str() ,type :int = int() ,mass :float = float() ,friction :float = float() ,restitution :float = float() ,group :str = str() ,mask :List[str] = [] ,embedded_collision_shape :CollisionShape = None ,linear_damping :float = float() ,angular_damping :float = float() ,locked_rotation :bool = bool() ,bullet :bool = bool() ,event_collision :bool = bool() ,event_contact :bool = bool() ,event_trigger :bool = bool() ) -> CollisionObjectDesc :
		self._collision_shape = collision_shape
		self._type = type
		self._mass = mass
		self._friction = friction
		self._restitution = restitution
		self._group = group
		self._mask = mask
		self._embedded_collision_shape = embedded_collision_shape
		self._linear_damping = linear_damping
		self._angular_damping = angular_damping
		self._locked_rotation = locked_rotation
		self._bullet = bullet
		self._event_collision = event_collision
		self._event_contact = event_contact
		self._event_trigger = event_trigger
		pass
	def getcollision_shape(self) -> str :
		return self._collision_shape

	def setcollision_shape(self,value : str) :
		if self._collision_shape != value:
			self._collision_shape = value
			self.collision_shapeChanged.emit(value)

	collision_shape = pyqtProperty(str, fget=getcollision_shape, fset=setcollision_shape, notify=collision_shapeChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.collision_shape.extend(self._collision_shape)
		instance.type.extend(self._type)
		instance.mass.extend(self._mass)
		instance.friction.extend(self._friction)
		instance.restitution.extend(self._restitution)
		instance.group.extend(self._group)
		instance.mask = self._mask
		instance.embedded_collision_shape = self._embedded_collision_shape.proto()
		instance.linear_damping.extend(self._linear_damping)
		instance.angular_damping.extend(self._angular_damping)
		instance.locked_rotation.extend(self._locked_rotation)
		instance.bullet.extend(self._bullet)
		instance.event_collision.extend(self._event_collision)
		instance.event_contact.extend(self._event_contact)
		instance.event_trigger.extend(self._event_trigger)

	def gettype(self) -> int :
		return self._type

	def settype(self,value : int) :
		if self._type != value:
			self._type = value
			self.typeChanged.emit(value)

	type = pyqtProperty(int, fget=gettype, fset=settype, notify=typeChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.collision_shape.extend(self._collision_shape)
		instance.type.extend(self._type)
		instance.mass.extend(self._mass)
		instance.friction.extend(self._friction)
		instance.restitution.extend(self._restitution)
		instance.group.extend(self._group)
		instance.mask = self._mask
		instance.embedded_collision_shape = self._embedded_collision_shape.proto()
		instance.linear_damping.extend(self._linear_damping)
		instance.angular_damping.extend(self._angular_damping)
		instance.locked_rotation.extend(self._locked_rotation)
		instance.bullet.extend(self._bullet)
		instance.event_collision.extend(self._event_collision)
		instance.event_contact.extend(self._event_contact)
		instance.event_trigger.extend(self._event_trigger)

	def getmass(self) -> float :
		return self._mass

	def setmass(self,value : float) :
		if self._mass != value:
			self._mass = value
			self.massChanged.emit(value)

	mass = pyqtProperty(float, fget=getmass, fset=setmass, notify=massChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.collision_shape.extend(self._collision_shape)
		instance.type.extend(self._type)
		instance.mass.extend(self._mass)
		instance.friction.extend(self._friction)
		instance.restitution.extend(self._restitution)
		instance.group.extend(self._group)
		instance.mask = self._mask
		instance.embedded_collision_shape = self._embedded_collision_shape.proto()
		instance.linear_damping.extend(self._linear_damping)
		instance.angular_damping.extend(self._angular_damping)
		instance.locked_rotation.extend(self._locked_rotation)
		instance.bullet.extend(self._bullet)
		instance.event_collision.extend(self._event_collision)
		instance.event_contact.extend(self._event_contact)
		instance.event_trigger.extend(self._event_trigger)

	def getfriction(self) -> float :
		return self._friction

	def setfriction(self,value : float) :
		if self._friction != value:
			self._friction = value
			self.frictionChanged.emit(value)

	friction = pyqtProperty(float, fget=getfriction, fset=setfriction, notify=frictionChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.collision_shape.extend(self._collision_shape)
		instance.type.extend(self._type)
		instance.mass.extend(self._mass)
		instance.friction.extend(self._friction)
		instance.restitution.extend(self._restitution)
		instance.group.extend(self._group)
		instance.mask = self._mask
		instance.embedded_collision_shape = self._embedded_collision_shape.proto()
		instance.linear_damping.extend(self._linear_damping)
		instance.angular_damping.extend(self._angular_damping)
		instance.locked_rotation.extend(self._locked_rotation)
		instance.bullet.extend(self._bullet)
		instance.event_collision.extend(self._event_collision)
		instance.event_contact.extend(self._event_contact)
		instance.event_trigger.extend(self._event_trigger)

	def getrestitution(self) -> float :
		return self._restitution

	def setrestitution(self,value : float) :
		if self._restitution != value:
			self._restitution = value
			self.restitutionChanged.emit(value)

	restitution = pyqtProperty(float, fget=getrestitution, fset=setrestitution, notify=restitutionChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.collision_shape.extend(self._collision_shape)
		instance.type.extend(self._type)
		instance.mass.extend(self._mass)
		instance.friction.extend(self._friction)
		instance.restitution.extend(self._restitution)
		instance.group.extend(self._group)
		instance.mask = self._mask
		instance.embedded_collision_shape = self._embedded_collision_shape.proto()
		instance.linear_damping.extend(self._linear_damping)
		instance.angular_damping.extend(self._angular_damping)
		instance.locked_rotation.extend(self._locked_rotation)
		instance.bullet.extend(self._bullet)
		instance.event_collision.extend(self._event_collision)
		instance.event_contact.extend(self._event_contact)
		instance.event_trigger.extend(self._event_trigger)

	def getgroup(self) -> str :
		return self._group

	def setgroup(self,value : str) :
		if self._group != value:
			self._group = value
			self.groupChanged.emit(value)

	group = pyqtProperty(str, fget=getgroup, fset=setgroup, notify=groupChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.collision_shape.extend(self._collision_shape)
		instance.type.extend(self._type)
		instance.mass.extend(self._mass)
		instance.friction.extend(self._friction)
		instance.restitution.extend(self._restitution)
		instance.group.extend(self._group)
		instance.mask = self._mask
		instance.embedded_collision_shape = self._embedded_collision_shape.proto()
		instance.linear_damping.extend(self._linear_damping)
		instance.angular_damping.extend(self._angular_damping)
		instance.locked_rotation.extend(self._locked_rotation)
		instance.bullet.extend(self._bullet)
		instance.event_collision.extend(self._event_collision)
		instance.event_contact.extend(self._event_contact)
		instance.event_trigger.extend(self._event_trigger)

	def getmask(self) -> str :
		return self._mask

	def setmask(self,value : List[str]) :
		if self._mask != value:
			self._mask = value
			self.maskChanged.emit(value)

	mask = pyqtProperty(List, fget=getmask, fset=setmask, notify=maskChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.collision_shape.extend(self._collision_shape)
		instance.type.extend(self._type)
		instance.mass.extend(self._mass)
		instance.friction.extend(self._friction)
		instance.restitution.extend(self._restitution)
		instance.group.extend(self._group)
		instance.mask = self._mask
		instance.embedded_collision_shape = self._embedded_collision_shape.proto()
		instance.linear_damping.extend(self._linear_damping)
		instance.angular_damping.extend(self._angular_damping)
		instance.locked_rotation.extend(self._locked_rotation)
		instance.bullet.extend(self._bullet)
		instance.event_collision.extend(self._event_collision)
		instance.event_contact.extend(self._event_contact)
		instance.event_trigger.extend(self._event_trigger)

	def getembedded_collision_shape(self) -> CollisionShape :
		return self._embedded_collision_shape

	def setembedded_collision_shape(self,value : CollisionShape) :
		if self._embedded_collision_shape != value:
			self._embedded_collision_shape = value
			self.embedded_collision_shapeChanged.emit(value)

	embedded_collision_shape = pyqtProperty(QObject, fget=getembedded_collision_shape, fset=setembedded_collision_shape, notify=embedded_collision_shapeChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.collision_shape.extend(self._collision_shape)
		instance.type.extend(self._type)
		instance.mass.extend(self._mass)
		instance.friction.extend(self._friction)
		instance.restitution.extend(self._restitution)
		instance.group.extend(self._group)
		instance.mask = self._mask
		instance.embedded_collision_shape = self._embedded_collision_shape.proto()
		instance.linear_damping.extend(self._linear_damping)
		instance.angular_damping.extend(self._angular_damping)
		instance.locked_rotation.extend(self._locked_rotation)
		instance.bullet.extend(self._bullet)
		instance.event_collision.extend(self._event_collision)
		instance.event_contact.extend(self._event_contact)
		instance.event_trigger.extend(self._event_trigger)

	def getlinear_damping(self) -> float :
		return self._linear_damping

	def setlinear_damping(self,value : float) :
		if self._linear_damping != value:
			self._linear_damping = value
			self.linear_dampingChanged.emit(value)

	linear_damping = pyqtProperty(float, fget=getlinear_damping, fset=setlinear_damping, notify=linear_dampingChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.collision_shape.extend(self._collision_shape)
		instance.type.extend(self._type)
		instance.mass.extend(self._mass)
		instance.friction.extend(self._friction)
		instance.restitution.extend(self._restitution)
		instance.group.extend(self._group)
		instance.mask = self._mask
		instance.embedded_collision_shape = self._embedded_collision_shape.proto()
		instance.linear_damping.extend(self._linear_damping)
		instance.angular_damping.extend(self._angular_damping)
		instance.locked_rotation.extend(self._locked_rotation)
		instance.bullet.extend(self._bullet)
		instance.event_collision.extend(self._event_collision)
		instance.event_contact.extend(self._event_contact)
		instance.event_trigger.extend(self._event_trigger)

	def getangular_damping(self) -> float :
		return self._angular_damping

	def setangular_damping(self,value : float) :
		if self._angular_damping != value:
			self._angular_damping = value
			self.angular_dampingChanged.emit(value)

	angular_damping = pyqtProperty(float, fget=getangular_damping, fset=setangular_damping, notify=angular_dampingChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.collision_shape.extend(self._collision_shape)
		instance.type.extend(self._type)
		instance.mass.extend(self._mass)
		instance.friction.extend(self._friction)
		instance.restitution.extend(self._restitution)
		instance.group.extend(self._group)
		instance.mask = self._mask
		instance.embedded_collision_shape = self._embedded_collision_shape.proto()
		instance.linear_damping.extend(self._linear_damping)
		instance.angular_damping.extend(self._angular_damping)
		instance.locked_rotation.extend(self._locked_rotation)
		instance.bullet.extend(self._bullet)
		instance.event_collision.extend(self._event_collision)
		instance.event_contact.extend(self._event_contact)
		instance.event_trigger.extend(self._event_trigger)

	def getlocked_rotation(self) -> bool :
		return self._locked_rotation

	def setlocked_rotation(self,value : bool) :
		if self._locked_rotation != value:
			self._locked_rotation = value
			self.locked_rotationChanged.emit(value)

	locked_rotation = pyqtProperty(bool, fget=getlocked_rotation, fset=setlocked_rotation, notify=locked_rotationChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.collision_shape.extend(self._collision_shape)
		instance.type.extend(self._type)
		instance.mass.extend(self._mass)
		instance.friction.extend(self._friction)
		instance.restitution.extend(self._restitution)
		instance.group.extend(self._group)
		instance.mask = self._mask
		instance.embedded_collision_shape = self._embedded_collision_shape.proto()
		instance.linear_damping.extend(self._linear_damping)
		instance.angular_damping.extend(self._angular_damping)
		instance.locked_rotation.extend(self._locked_rotation)
		instance.bullet.extend(self._bullet)
		instance.event_collision.extend(self._event_collision)
		instance.event_contact.extend(self._event_contact)
		instance.event_trigger.extend(self._event_trigger)

	def getbullet(self) -> bool :
		return self._bullet

	def setbullet(self,value : bool) :
		if self._bullet != value:
			self._bullet = value
			self.bulletChanged.emit(value)

	bullet = pyqtProperty(bool, fget=getbullet, fset=setbullet, notify=bulletChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.collision_shape.extend(self._collision_shape)
		instance.type.extend(self._type)
		instance.mass.extend(self._mass)
		instance.friction.extend(self._friction)
		instance.restitution.extend(self._restitution)
		instance.group.extend(self._group)
		instance.mask = self._mask
		instance.embedded_collision_shape = self._embedded_collision_shape.proto()
		instance.linear_damping.extend(self._linear_damping)
		instance.angular_damping.extend(self._angular_damping)
		instance.locked_rotation.extend(self._locked_rotation)
		instance.bullet.extend(self._bullet)
		instance.event_collision.extend(self._event_collision)
		instance.event_contact.extend(self._event_contact)
		instance.event_trigger.extend(self._event_trigger)

	def getevent_collision(self) -> bool :
		return self._event_collision

	def setevent_collision(self,value : bool) :
		if self._event_collision != value:
			self._event_collision = value
			self.event_collisionChanged.emit(value)

	event_collision = pyqtProperty(bool, fget=getevent_collision, fset=setevent_collision, notify=event_collisionChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.collision_shape.extend(self._collision_shape)
		instance.type.extend(self._type)
		instance.mass.extend(self._mass)
		instance.friction.extend(self._friction)
		instance.restitution.extend(self._restitution)
		instance.group.extend(self._group)
		instance.mask = self._mask
		instance.embedded_collision_shape = self._embedded_collision_shape.proto()
		instance.linear_damping.extend(self._linear_damping)
		instance.angular_damping.extend(self._angular_damping)
		instance.locked_rotation.extend(self._locked_rotation)
		instance.bullet.extend(self._bullet)
		instance.event_collision.extend(self._event_collision)
		instance.event_contact.extend(self._event_contact)
		instance.event_trigger.extend(self._event_trigger)

	def getevent_contact(self) -> bool :
		return self._event_contact

	def setevent_contact(self,value : bool) :
		if self._event_contact != value:
			self._event_contact = value
			self.event_contactChanged.emit(value)

	event_contact = pyqtProperty(bool, fget=getevent_contact, fset=setevent_contact, notify=event_contactChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.collision_shape.extend(self._collision_shape)
		instance.type.extend(self._type)
		instance.mass.extend(self._mass)
		instance.friction.extend(self._friction)
		instance.restitution.extend(self._restitution)
		instance.group.extend(self._group)
		instance.mask = self._mask
		instance.embedded_collision_shape = self._embedded_collision_shape.proto()
		instance.linear_damping.extend(self._linear_damping)
		instance.angular_damping.extend(self._angular_damping)
		instance.locked_rotation.extend(self._locked_rotation)
		instance.bullet.extend(self._bullet)
		instance.event_collision.extend(self._event_collision)
		instance.event_contact.extend(self._event_contact)
		instance.event_trigger.extend(self._event_trigger)

	def getevent_trigger(self) -> bool :
		return self._event_trigger

	def setevent_trigger(self,value : bool) :
		if self._event_trigger != value:
			self._event_trigger = value
			self.event_triggerChanged.emit(value)

	event_trigger = pyqtProperty(bool, fget=getevent_trigger, fset=setevent_trigger, notify=event_triggerChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.collision_shape.extend(self._collision_shape)
		instance.type.extend(self._type)
		instance.mass.extend(self._mass)
		instance.friction.extend(self._friction)
		instance.restitution.extend(self._restitution)
		instance.group.extend(self._group)
		instance.mask = self._mask
		instance.embedded_collision_shape = self._embedded_collision_shape.proto()
		instance.linear_damping.extend(self._linear_damping)
		instance.angular_damping.extend(self._angular_damping)
		instance.locked_rotation.extend(self._locked_rotation)
		instance.bullet.extend(self._bullet)
		instance.event_collision.extend(self._event_collision)
		instance.event_contact.extend(self._event_contact)
		instance.event_trigger.extend(self._event_trigger)

# ------- CollisionResponse ------- #
class CollisionResponse(QObject) :
	__PROTO__ = sdk.CollisionResponse
	def __init__(self,other_id :int = int() ,group :int = int() ,other_position :Point3 = None ,other_group :int = int() ,own_group :int = int() ) -> CollisionResponse :
		self._other_id = other_id
		self._group = group
		self._other_position = other_position
		self._other_group = other_group
		self._own_group = own_group
		pass
	def getother_id(self) -> int :
		return self._other_id

	def setother_id(self,value : int) :
		if self._other_id != value:
			self._other_id = value
			self.other_idChanged.emit(value)

	other_id = pyqtProperty(int, fget=getother_id, fset=setother_id, notify=other_idChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.other_id.extend(self._other_id)
		instance.group.extend(self._group)
		instance.other_position = self._other_position.proto()
		instance.other_group.extend(self._other_group)
		instance.own_group.extend(self._own_group)

	def getgroup(self) -> int :
		return self._group

	def setgroup(self,value : int) :
		if self._group != value:
			self._group = value
			self.groupChanged.emit(value)

	group = pyqtProperty(int, fget=getgroup, fset=setgroup, notify=groupChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.other_id.extend(self._other_id)
		instance.group.extend(self._group)
		instance.other_position = self._other_position.proto()
		instance.other_group.extend(self._other_group)
		instance.own_group.extend(self._own_group)

	def getother_position(self) -> Point3 :
		return self._other_position

	def setother_position(self,value : Point3) :
		if self._other_position != value:
			self._other_position = value
			self.other_positionChanged.emit(value)

	other_position = pyqtProperty(QObject, fget=getother_position, fset=setother_position, notify=other_positionChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.other_id.extend(self._other_id)
		instance.group.extend(self._group)
		instance.other_position = self._other_position.proto()
		instance.other_group.extend(self._other_group)
		instance.own_group.extend(self._own_group)

	def getother_group(self) -> int :
		return self._other_group

	def setother_group(self,value : int) :
		if self._other_group != value:
			self._other_group = value
			self.other_groupChanged.emit(value)

	other_group = pyqtProperty(int, fget=getother_group, fset=setother_group, notify=other_groupChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.other_id.extend(self._other_id)
		instance.group.extend(self._group)
		instance.other_position = self._other_position.proto()
		instance.other_group.extend(self._other_group)
		instance.own_group.extend(self._own_group)

	def getown_group(self) -> int :
		return self._own_group

	def setown_group(self,value : int) :
		if self._own_group != value:
			self._own_group = value
			self.own_groupChanged.emit(value)

	own_group = pyqtProperty(int, fget=getown_group, fset=setown_group, notify=own_groupChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.other_id.extend(self._other_id)
		instance.group.extend(self._group)
		instance.other_position = self._other_position.proto()
		instance.other_group.extend(self._other_group)
		instance.own_group.extend(self._own_group)

# ------- CollisionShape ------- #
class Type(Enum):
	TYPE_SPHERE = 0
	TYPE_BOX = 1
	TYPE_CAPSULE = 2
	TYPE_HULL = 3
class CollisionShape(QObject) :
	__PROTO__ = sdk.CollisionShape
	def __init__(self,shapes :List[Shape] = [],data :List[float] = [] ) -> CollisionShape :
		self._shapes = shapes
		self._data = data
		pass
	def getshapes(self) -> Shape :
		return self._shapes

	def setshapes(self,value : List[Shape]) :
		if self._shapes != value:
			self._shapes = value
			self.shapesChanged.emit(value)

	shapes = pyqtProperty(List, fget=getshapes, fset=setshapes, notify=shapesChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.shapes.extend([i.proto() for i in self._shapes])
		instance.data = self._data

	def getdata(self) -> float :
		return self._data

	def setdata(self,value : List[float]) :
		if self._data != value:
			self._data = value
			self.dataChanged.emit(value)

	data = pyqtProperty(List, fget=getdata, fset=setdata, notify=dataChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.shapes.extend([i.proto() for i in self._shapes])
		instance.data = self._data

# ------- ComponenTypeDesc ------- #
class ComponenTypeDesc(QObject) :
	__PROTO__ = sdk.ComponenTypeDesc
	def __init__(self,name_hash :int = int() ,max_count :int = int() ) -> ComponenTypeDesc :
		self._name_hash = name_hash
		self._max_count = max_count
		pass
	def getname_hash(self) -> int :
		return self._name_hash

	def setname_hash(self,value : int) :
		if self._name_hash != value:
			self._name_hash = value
			self.name_hashChanged.emit(value)

	name_hash = pyqtProperty(int, fget=getname_hash, fset=setname_hash, notify=name_hashChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.name_hash.extend(self._name_hash)
		instance.max_count.extend(self._max_count)

	def getmax_count(self) -> int :
		return self._max_count

	def setmax_count(self,value : int) :
		if self._max_count != value:
			self._max_count = value
			self.max_countChanged.emit(value)

	max_count = pyqtProperty(int, fget=getmax_count, fset=setmax_count, notify=max_countChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.name_hash.extend(self._name_hash)
		instance.max_count.extend(self._max_count)

# ------- ComponentDesc ------- #
class ComponentDesc(QObject) :
	__PROTO__ = sdk.ComponentDesc
	def __init__(self,id :str = str() ,component :str = str() ,position :Point3 = None ,rotation :Quat = None ,properties :List[PropertyDesc] = [],property_decls :PropertyDeclarations = None ,scale :Vector3One = None ) -> ComponentDesc :
		self._id = id
		self._component = component
		self._position = position
		self._rotation = rotation
		self._properties = properties
		self._property_decls = property_decls
		self._scale = scale
		pass
	def getid(self) -> str :
		return self._id

	def setid(self,value : str) :
		if self._id != value:
			self._id = value
			self.idChanged.emit(value)

	id = pyqtProperty(str, fget=getid, fset=setid, notify=idChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.id.extend(self._id)
		instance.component.extend(self._component)
		instance.position = self._position.proto()
		instance.rotation = self._rotation.proto()
		instance.properties.extend([i.proto() for i in self._properties])
		instance.property_decls = self._property_decls.proto()
		instance.scale = self._scale.proto()

	def getcomponent(self) -> str :
		return self._component

	def setcomponent(self,value : str) :
		if self._component != value:
			self._component = value
			self.componentChanged.emit(value)

	component = pyqtProperty(str, fget=getcomponent, fset=setcomponent, notify=componentChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.id.extend(self._id)
		instance.component.extend(self._component)
		instance.position = self._position.proto()
		instance.rotation = self._rotation.proto()
		instance.properties.extend([i.proto() for i in self._properties])
		instance.property_decls = self._property_decls.proto()
		instance.scale = self._scale.proto()

	def getposition(self) -> Point3 :
		return self._position

	def setposition(self,value : Point3) :
		if self._position != value:
			self._position = value
			self.positionChanged.emit(value)

	position = pyqtProperty(QObject, fget=getposition, fset=setposition, notify=positionChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.id.extend(self._id)
		instance.component.extend(self._component)
		instance.position = self._position.proto()
		instance.rotation = self._rotation.proto()
		instance.properties.extend([i.proto() for i in self._properties])
		instance.property_decls = self._property_decls.proto()
		instance.scale = self._scale.proto()

	def getrotation(self) -> Quat :
		return self._rotation

	def setrotation(self,value : Quat) :
		if self._rotation != value:
			self._rotation = value
			self.rotationChanged.emit(value)

	rotation = pyqtProperty(QObject, fget=getrotation, fset=setrotation, notify=rotationChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.id.extend(self._id)
		instance.component.extend(self._component)
		instance.position = self._position.proto()
		instance.rotation = self._rotation.proto()
		instance.properties.extend([i.proto() for i in self._properties])
		instance.property_decls = self._property_decls.proto()
		instance.scale = self._scale.proto()

	def getproperties(self) -> PropertyDesc :
		return self._properties

	def setproperties(self,value : List[PropertyDesc]) :
		if self._properties != value:
			self._properties = value
			self.propertiesChanged.emit(value)

	properties = pyqtProperty(List, fget=getproperties, fset=setproperties, notify=propertiesChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.id.extend(self._id)
		instance.component.extend(self._component)
		instance.position = self._position.proto()
		instance.rotation = self._rotation.proto()
		instance.properties.extend([i.proto() for i in self._properties])
		instance.property_decls = self._property_decls.proto()
		instance.scale = self._scale.proto()

	def getproperty_decls(self) -> PropertyDeclarations :
		return self._property_decls

	def setproperty_decls(self,value : PropertyDeclarations) :
		if self._property_decls != value:
			self._property_decls = value
			self.property_declsChanged.emit(value)

	property_decls = pyqtProperty(QObject, fget=getproperty_decls, fset=setproperty_decls, notify=property_declsChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.id.extend(self._id)
		instance.component.extend(self._component)
		instance.position = self._position.proto()
		instance.rotation = self._rotation.proto()
		instance.properties.extend([i.proto() for i in self._properties])
		instance.property_decls = self._property_decls.proto()
		instance.scale = self._scale.proto()

	def getscale(self) -> Vector3One :
		return self._scale

	def setscale(self,value : Vector3One) :
		if self._scale != value:
			self._scale = value
			self.scaleChanged.emit(value)

	scale = pyqtProperty(QObject, fget=getscale, fset=setscale, notify=scaleChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.id.extend(self._id)
		instance.component.extend(self._component)
		instance.position = self._position.proto()
		instance.rotation = self._rotation.proto()
		instance.properties.extend([i.proto() for i in self._properties])
		instance.property_decls = self._property_decls.proto()
		instance.scale = self._scale.proto()

# ------- ComponentPropertyDesc ------- #
class ComponentPropertyDesc(QObject) :
	__PROTO__ = sdk.ComponentPropertyDesc
	def __init__(self,id :str = str() ,properties :List[PropertyDesc] = [],property_decls :PropertyDeclarations = None ) -> ComponentPropertyDesc :
		self._id = id
		self._properties = properties
		self._property_decls = property_decls
		pass
	def getid(self) -> str :
		return self._id

	def setid(self,value : str) :
		if self._id != value:
			self._id = value
			self.idChanged.emit(value)

	id = pyqtProperty(str, fget=getid, fset=setid, notify=idChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.id.extend(self._id)
		instance.properties.extend([i.proto() for i in self._properties])
		instance.property_decls = self._property_decls.proto()

	def getproperties(self) -> PropertyDesc :
		return self._properties

	def setproperties(self,value : List[PropertyDesc]) :
		if self._properties != value:
			self._properties = value
			self.propertiesChanged.emit(value)

	properties = pyqtProperty(List, fget=getproperties, fset=setproperties, notify=propertiesChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.id.extend(self._id)
		instance.properties.extend([i.proto() for i in self._properties])
		instance.property_decls = self._property_decls.proto()

	def getproperty_decls(self) -> PropertyDeclarations :
		return self._property_decls

	def setproperty_decls(self,value : PropertyDeclarations) :
		if self._property_decls != value:
			self._property_decls = value
			self.property_declsChanged.emit(value)

	property_decls = pyqtProperty(QObject, fget=getproperty_decls, fset=setproperty_decls, notify=property_declsChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.id.extend(self._id)
		instance.properties.extend([i.proto() for i in self._properties])
		instance.property_decls = self._property_decls.proto()

# ------- ContactPoint ------- #
class ContactPoint(QObject) :
	__PROTO__ = sdk.ContactPoint
	def __init__(self,position :Point3 = None ,instance_position :Point3 = None ,normal :Vector3 = None ,relative_velocity :Vector3 = None ,mass :float = float() ,id :int = int() ,group :int = int() ) -> ContactPoint :
		self._position = position
		self._instance_position = instance_position
		self._normal = normal
		self._relative_velocity = relative_velocity
		self._mass = mass
		self._id = id
		self._group = group
		pass
	def getposition(self) -> Point3 :
		return self._position

	def setposition(self,value : Point3) :
		if self._position != value:
			self._position = value
			self.positionChanged.emit(value)

	position = pyqtProperty(QObject, fget=getposition, fset=setposition, notify=positionChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.position = self._position.proto()
		instance.instance_position = self._instance_position.proto()
		instance.normal = self._normal.proto()
		instance.relative_velocity = self._relative_velocity.proto()
		instance.mass.extend(self._mass)
		instance.id.extend(self._id)
		instance.group.extend(self._group)

	def getinstance_position(self) -> Point3 :
		return self._instance_position

	def setinstance_position(self,value : Point3) :
		if self._instance_position != value:
			self._instance_position = value
			self.instance_positionChanged.emit(value)

	instance_position = pyqtProperty(QObject, fget=getinstance_position, fset=setinstance_position, notify=instance_positionChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.position = self._position.proto()
		instance.instance_position = self._instance_position.proto()
		instance.normal = self._normal.proto()
		instance.relative_velocity = self._relative_velocity.proto()
		instance.mass.extend(self._mass)
		instance.id.extend(self._id)
		instance.group.extend(self._group)

	def getnormal(self) -> Vector3 :
		return self._normal

	def setnormal(self,value : Vector3) :
		if self._normal != value:
			self._normal = value
			self.normalChanged.emit(value)

	normal = pyqtProperty(QObject, fget=getnormal, fset=setnormal, notify=normalChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.position = self._position.proto()
		instance.instance_position = self._instance_position.proto()
		instance.normal = self._normal.proto()
		instance.relative_velocity = self._relative_velocity.proto()
		instance.mass.extend(self._mass)
		instance.id.extend(self._id)
		instance.group.extend(self._group)

	def getrelative_velocity(self) -> Vector3 :
		return self._relative_velocity

	def setrelative_velocity(self,value : Vector3) :
		if self._relative_velocity != value:
			self._relative_velocity = value
			self.relative_velocityChanged.emit(value)

	relative_velocity = pyqtProperty(QObject, fget=getrelative_velocity, fset=setrelative_velocity, notify=relative_velocityChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.position = self._position.proto()
		instance.instance_position = self._instance_position.proto()
		instance.normal = self._normal.proto()
		instance.relative_velocity = self._relative_velocity.proto()
		instance.mass.extend(self._mass)
		instance.id.extend(self._id)
		instance.group.extend(self._group)

	def getmass(self) -> float :
		return self._mass

	def setmass(self,value : float) :
		if self._mass != value:
			self._mass = value
			self.massChanged.emit(value)

	mass = pyqtProperty(float, fget=getmass, fset=setmass, notify=massChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.position = self._position.proto()
		instance.instance_position = self._instance_position.proto()
		instance.normal = self._normal.proto()
		instance.relative_velocity = self._relative_velocity.proto()
		instance.mass.extend(self._mass)
		instance.id.extend(self._id)
		instance.group.extend(self._group)

	def getid(self) -> int :
		return self._id

	def setid(self,value : int) :
		if self._id != value:
			self._id = value
			self.idChanged.emit(value)

	id = pyqtProperty(int, fget=getid, fset=setid, notify=idChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.position = self._position.proto()
		instance.instance_position = self._instance_position.proto()
		instance.normal = self._normal.proto()
		instance.relative_velocity = self._relative_velocity.proto()
		instance.mass.extend(self._mass)
		instance.id.extend(self._id)
		instance.group.extend(self._group)

	def getgroup(self) -> int :
		return self._group

	def setgroup(self,value : int) :
		if self._group != value:
			self._group = value
			self.groupChanged.emit(value)

	group = pyqtProperty(int, fget=getgroup, fset=setgroup, notify=groupChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.position = self._position.proto()
		instance.instance_position = self._instance_position.proto()
		instance.normal = self._normal.proto()
		instance.relative_velocity = self._relative_velocity.proto()
		instance.mass.extend(self._mass)
		instance.id.extend(self._id)
		instance.group.extend(self._group)

# ------- ContactPointEvent ------- #
class ContactPointEvent(QObject) :
	__PROTO__ = sdk.ContactPointEvent
	def __init__(self,a :ContactPoint = None ,b :ContactPoint = None ,distance :float = float() ,applied_impulse :float = float() ) -> ContactPointEvent :
		self._a = a
		self._b = b
		self._distance = distance
		self._applied_impulse = applied_impulse
		pass
	def geta(self) -> ContactPoint :
		return self._a

	def seta(self,value : ContactPoint) :
		if self._a != value:
			self._a = value
			self.aChanged.emit(value)

	a = pyqtProperty(QObject, fget=geta, fset=seta, notify=aChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.a = self._a.proto()
		instance.b = self._b.proto()
		instance.distance.extend(self._distance)
		instance.applied_impulse.extend(self._applied_impulse)

	def getb(self) -> ContactPoint :
		return self._b

	def setb(self,value : ContactPoint) :
		if self._b != value:
			self._b = value
			self.bChanged.emit(value)

	b = pyqtProperty(QObject, fget=getb, fset=setb, notify=bChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.a = self._a.proto()
		instance.b = self._b.proto()
		instance.distance.extend(self._distance)
		instance.applied_impulse.extend(self._applied_impulse)

	def getdistance(self) -> float :
		return self._distance

	def setdistance(self,value : float) :
		if self._distance != value:
			self._distance = value
			self.distanceChanged.emit(value)

	distance = pyqtProperty(float, fget=getdistance, fset=setdistance, notify=distanceChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.a = self._a.proto()
		instance.b = self._b.proto()
		instance.distance.extend(self._distance)
		instance.applied_impulse.extend(self._applied_impulse)

	def getapplied_impulse(self) -> float :
		return self._applied_impulse

	def setapplied_impulse(self,value : float) :
		if self._applied_impulse != value:
			self._applied_impulse = value
			self.applied_impulseChanged.emit(value)

	applied_impulse = pyqtProperty(float, fget=getapplied_impulse, fset=setapplied_impulse, notify=applied_impulseChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.a = self._a.proto()
		instance.b = self._b.proto()
		instance.distance.extend(self._distance)
		instance.applied_impulse.extend(self._applied_impulse)

# ------- ContactPointResponse ------- #
class ContactPointResponse(QObject) :
	__PROTO__ = sdk.ContactPointResponse
	def __init__(self,position :Point3 = None ,normal :Vector3 = None ,relative_velocity :Vector3 = None ,distance :float = float() ,applied_impulse :float = float() ,life_time :float = float() ,mass :float = float() ,other_mass :float = float() ,other_id :int = int() ,other_position :Point3 = None ,group :int = int() ,other_group :int = int() ,own_group :int = int() ) -> ContactPointResponse :
		self._position = position
		self._normal = normal
		self._relative_velocity = relative_velocity
		self._distance = distance
		self._applied_impulse = applied_impulse
		self._life_time = life_time
		self._mass = mass
		self._other_mass = other_mass
		self._other_id = other_id
		self._other_position = other_position
		self._group = group
		self._other_group = other_group
		self._own_group = own_group
		pass
	def getposition(self) -> Point3 :
		return self._position

	def setposition(self,value : Point3) :
		if self._position != value:
			self._position = value
			self.positionChanged.emit(value)

	position = pyqtProperty(QObject, fget=getposition, fset=setposition, notify=positionChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.position = self._position.proto()
		instance.normal = self._normal.proto()
		instance.relative_velocity = self._relative_velocity.proto()
		instance.distance.extend(self._distance)
		instance.applied_impulse.extend(self._applied_impulse)
		instance.life_time.extend(self._life_time)
		instance.mass.extend(self._mass)
		instance.other_mass.extend(self._other_mass)
		instance.other_id.extend(self._other_id)
		instance.other_position = self._other_position.proto()
		instance.group.extend(self._group)
		instance.other_group.extend(self._other_group)
		instance.own_group.extend(self._own_group)

	def getnormal(self) -> Vector3 :
		return self._normal

	def setnormal(self,value : Vector3) :
		if self._normal != value:
			self._normal = value
			self.normalChanged.emit(value)

	normal = pyqtProperty(QObject, fget=getnormal, fset=setnormal, notify=normalChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.position = self._position.proto()
		instance.normal = self._normal.proto()
		instance.relative_velocity = self._relative_velocity.proto()
		instance.distance.extend(self._distance)
		instance.applied_impulse.extend(self._applied_impulse)
		instance.life_time.extend(self._life_time)
		instance.mass.extend(self._mass)
		instance.other_mass.extend(self._other_mass)
		instance.other_id.extend(self._other_id)
		instance.other_position = self._other_position.proto()
		instance.group.extend(self._group)
		instance.other_group.extend(self._other_group)
		instance.own_group.extend(self._own_group)

	def getrelative_velocity(self) -> Vector3 :
		return self._relative_velocity

	def setrelative_velocity(self,value : Vector3) :
		if self._relative_velocity != value:
			self._relative_velocity = value
			self.relative_velocityChanged.emit(value)

	relative_velocity = pyqtProperty(QObject, fget=getrelative_velocity, fset=setrelative_velocity, notify=relative_velocityChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.position = self._position.proto()
		instance.normal = self._normal.proto()
		instance.relative_velocity = self._relative_velocity.proto()
		instance.distance.extend(self._distance)
		instance.applied_impulse.extend(self._applied_impulse)
		instance.life_time.extend(self._life_time)
		instance.mass.extend(self._mass)
		instance.other_mass.extend(self._other_mass)
		instance.other_id.extend(self._other_id)
		instance.other_position = self._other_position.proto()
		instance.group.extend(self._group)
		instance.other_group.extend(self._other_group)
		instance.own_group.extend(self._own_group)

	def getdistance(self) -> float :
		return self._distance

	def setdistance(self,value : float) :
		if self._distance != value:
			self._distance = value
			self.distanceChanged.emit(value)

	distance = pyqtProperty(float, fget=getdistance, fset=setdistance, notify=distanceChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.position = self._position.proto()
		instance.normal = self._normal.proto()
		instance.relative_velocity = self._relative_velocity.proto()
		instance.distance.extend(self._distance)
		instance.applied_impulse.extend(self._applied_impulse)
		instance.life_time.extend(self._life_time)
		instance.mass.extend(self._mass)
		instance.other_mass.extend(self._other_mass)
		instance.other_id.extend(self._other_id)
		instance.other_position = self._other_position.proto()
		instance.group.extend(self._group)
		instance.other_group.extend(self._other_group)
		instance.own_group.extend(self._own_group)

	def getapplied_impulse(self) -> float :
		return self._applied_impulse

	def setapplied_impulse(self,value : float) :
		if self._applied_impulse != value:
			self._applied_impulse = value
			self.applied_impulseChanged.emit(value)

	applied_impulse = pyqtProperty(float, fget=getapplied_impulse, fset=setapplied_impulse, notify=applied_impulseChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.position = self._position.proto()
		instance.normal = self._normal.proto()
		instance.relative_velocity = self._relative_velocity.proto()
		instance.distance.extend(self._distance)
		instance.applied_impulse.extend(self._applied_impulse)
		instance.life_time.extend(self._life_time)
		instance.mass.extend(self._mass)
		instance.other_mass.extend(self._other_mass)
		instance.other_id.extend(self._other_id)
		instance.other_position = self._other_position.proto()
		instance.group.extend(self._group)
		instance.other_group.extend(self._other_group)
		instance.own_group.extend(self._own_group)

	def getlife_time(self) -> float :
		return self._life_time

	def setlife_time(self,value : float) :
		if self._life_time != value:
			self._life_time = value
			self.life_timeChanged.emit(value)

	life_time = pyqtProperty(float, fget=getlife_time, fset=setlife_time, notify=life_timeChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.position = self._position.proto()
		instance.normal = self._normal.proto()
		instance.relative_velocity = self._relative_velocity.proto()
		instance.distance.extend(self._distance)
		instance.applied_impulse.extend(self._applied_impulse)
		instance.life_time.extend(self._life_time)
		instance.mass.extend(self._mass)
		instance.other_mass.extend(self._other_mass)
		instance.other_id.extend(self._other_id)
		instance.other_position = self._other_position.proto()
		instance.group.extend(self._group)
		instance.other_group.extend(self._other_group)
		instance.own_group.extend(self._own_group)

	def getmass(self) -> float :
		return self._mass

	def setmass(self,value : float) :
		if self._mass != value:
			self._mass = value
			self.massChanged.emit(value)

	mass = pyqtProperty(float, fget=getmass, fset=setmass, notify=massChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.position = self._position.proto()
		instance.normal = self._normal.proto()
		instance.relative_velocity = self._relative_velocity.proto()
		instance.distance.extend(self._distance)
		instance.applied_impulse.extend(self._applied_impulse)
		instance.life_time.extend(self._life_time)
		instance.mass.extend(self._mass)
		instance.other_mass.extend(self._other_mass)
		instance.other_id.extend(self._other_id)
		instance.other_position = self._other_position.proto()
		instance.group.extend(self._group)
		instance.other_group.extend(self._other_group)
		instance.own_group.extend(self._own_group)

	def getother_mass(self) -> float :
		return self._other_mass

	def setother_mass(self,value : float) :
		if self._other_mass != value:
			self._other_mass = value
			self.other_massChanged.emit(value)

	other_mass = pyqtProperty(float, fget=getother_mass, fset=setother_mass, notify=other_massChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.position = self._position.proto()
		instance.normal = self._normal.proto()
		instance.relative_velocity = self._relative_velocity.proto()
		instance.distance.extend(self._distance)
		instance.applied_impulse.extend(self._applied_impulse)
		instance.life_time.extend(self._life_time)
		instance.mass.extend(self._mass)
		instance.other_mass.extend(self._other_mass)
		instance.other_id.extend(self._other_id)
		instance.other_position = self._other_position.proto()
		instance.group.extend(self._group)
		instance.other_group.extend(self._other_group)
		instance.own_group.extend(self._own_group)

	def getother_id(self) -> int :
		return self._other_id

	def setother_id(self,value : int) :
		if self._other_id != value:
			self._other_id = value
			self.other_idChanged.emit(value)

	other_id = pyqtProperty(int, fget=getother_id, fset=setother_id, notify=other_idChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.position = self._position.proto()
		instance.normal = self._normal.proto()
		instance.relative_velocity = self._relative_velocity.proto()
		instance.distance.extend(self._distance)
		instance.applied_impulse.extend(self._applied_impulse)
		instance.life_time.extend(self._life_time)
		instance.mass.extend(self._mass)
		instance.other_mass.extend(self._other_mass)
		instance.other_id.extend(self._other_id)
		instance.other_position = self._other_position.proto()
		instance.group.extend(self._group)
		instance.other_group.extend(self._other_group)
		instance.own_group.extend(self._own_group)

	def getother_position(self) -> Point3 :
		return self._other_position

	def setother_position(self,value : Point3) :
		if self._other_position != value:
			self._other_position = value
			self.other_positionChanged.emit(value)

	other_position = pyqtProperty(QObject, fget=getother_position, fset=setother_position, notify=other_positionChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.position = self._position.proto()
		instance.normal = self._normal.proto()
		instance.relative_velocity = self._relative_velocity.proto()
		instance.distance.extend(self._distance)
		instance.applied_impulse.extend(self._applied_impulse)
		instance.life_time.extend(self._life_time)
		instance.mass.extend(self._mass)
		instance.other_mass.extend(self._other_mass)
		instance.other_id.extend(self._other_id)
		instance.other_position = self._other_position.proto()
		instance.group.extend(self._group)
		instance.other_group.extend(self._other_group)
		instance.own_group.extend(self._own_group)

	def getgroup(self) -> int :
		return self._group

	def setgroup(self,value : int) :
		if self._group != value:
			self._group = value
			self.groupChanged.emit(value)

	group = pyqtProperty(int, fget=getgroup, fset=setgroup, notify=groupChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.position = self._position.proto()
		instance.normal = self._normal.proto()
		instance.relative_velocity = self._relative_velocity.proto()
		instance.distance.extend(self._distance)
		instance.applied_impulse.extend(self._applied_impulse)
		instance.life_time.extend(self._life_time)
		instance.mass.extend(self._mass)
		instance.other_mass.extend(self._other_mass)
		instance.other_id.extend(self._other_id)
		instance.other_position = self._other_position.proto()
		instance.group.extend(self._group)
		instance.other_group.extend(self._other_group)
		instance.own_group.extend(self._own_group)

	def getother_group(self) -> int :
		return self._other_group

	def setother_group(self,value : int) :
		if self._other_group != value:
			self._other_group = value
			self.other_groupChanged.emit(value)

	other_group = pyqtProperty(int, fget=getother_group, fset=setother_group, notify=other_groupChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.position = self._position.proto()
		instance.normal = self._normal.proto()
		instance.relative_velocity = self._relative_velocity.proto()
		instance.distance.extend(self._distance)
		instance.applied_impulse.extend(self._applied_impulse)
		instance.life_time.extend(self._life_time)
		instance.mass.extend(self._mass)
		instance.other_mass.extend(self._other_mass)
		instance.other_id.extend(self._other_id)
		instance.other_position = self._other_position.proto()
		instance.group.extend(self._group)
		instance.other_group.extend(self._other_group)
		instance.own_group.extend(self._own_group)

	def getown_group(self) -> int :
		return self._own_group

	def setown_group(self,value : int) :
		if self._own_group != value:
			self._own_group = value
			self.own_groupChanged.emit(value)

	own_group = pyqtProperty(int, fget=getown_group, fset=setown_group, notify=own_groupChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.position = self._position.proto()
		instance.normal = self._normal.proto()
		instance.relative_velocity = self._relative_velocity.proto()
		instance.distance.extend(self._distance)
		instance.applied_impulse.extend(self._applied_impulse)
		instance.life_time.extend(self._life_time)
		instance.mass.extend(self._mass)
		instance.other_mass.extend(self._other_mass)
		instance.other_id.extend(self._other_id)
		instance.other_position = self._other_position.proto()
		instance.group.extend(self._group)
		instance.other_group.extend(self._other_group)
		instance.own_group.extend(self._own_group)

# ------- ConvexHull ------- #
class ConvexHull(QObject) :
	__PROTO__ = sdk.ConvexHull
	def __init__(self,index :int = int() ,count :int = int() ,collision_group :str = str() ) -> ConvexHull :
		self._index = index
		self._count = count
		self._collision_group = collision_group
		pass
	def getindex(self) -> int :
		return self._index

	def setindex(self,value : int) :
		if self._index != value:
			self._index = value
			self.indexChanged.emit(value)

	index = pyqtProperty(int, fget=getindex, fset=setindex, notify=indexChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.index.extend(self._index)
		instance.count.extend(self._count)
		instance.collision_group.extend(self._collision_group)

	def getcount(self) -> int :
		return self._count

	def setcount(self,value : int) :
		if self._count != value:
			self._count = value
			self.countChanged.emit(value)

	count = pyqtProperty(int, fget=getcount, fset=setcount, notify=countChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.index.extend(self._index)
		instance.count.extend(self._count)
		instance.collision_group.extend(self._collision_group)

	def getcollision_group(self) -> str :
		return self._collision_group

	def setcollision_group(self,value : str) :
		if self._collision_group != value:
			self._collision_group = value
			self.collision_groupChanged.emit(value)

	collision_group = pyqtProperty(str, fget=getcollision_group, fset=setcollision_group, notify=collision_groupChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.index.extend(self._index)
		instance.count.extend(self._count)
		instance.collision_group.extend(self._collision_group)

# ------- ConvexShape ------- #
class Type(Enum):
	TYPE_SPHERE = 0
	TYPE_BOX = 1
	TYPE_CAPSULE = 2
	TYPE_HULL = 3
class ConvexShape(QObject) :
	__PROTO__ = sdk.ConvexShape
	def __init__(self,shape_type :int = int() ,data :List[float] = [] ) -> ConvexShape :
		self._shape_type = shape_type
		self._data = data
		pass
	def getshape_type(self) -> int :
		return self._shape_type

	def setshape_type(self,value : int) :
		if self._shape_type != value:
			self._shape_type = value
			self.shape_typeChanged.emit(value)

	shape_type = pyqtProperty(int, fget=getshape_type, fset=setshape_type, notify=shape_typeChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.shape_type.extend(self._shape_type)
		instance.data = self._data

	def getdata(self) -> float :
		return self._data

	def setdata(self,value : List[float]) :
		if self._data != value:
			self._data = value
			self.dataChanged.emit(value)

	data = pyqtProperty(List, fget=getdata, fset=setdata, notify=dataChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.shape_type.extend(self._shape_type)
		instance.data = self._data

# ------- Create ------- #
class Create(QObject) :
	__PROTO__ = sdk.Create
	def __init__(self,position :Point3 = None ,rotation :Quat = None ,id :int = int() ,scale :float = float() ,scale3 :Vector3 = None ) -> Create :
		self._position = position
		self._rotation = rotation
		self._id = id
		self._scale = scale
		self._scale3 = scale3
		pass
	def getposition(self) -> Point3 :
		return self._position

	def setposition(self,value : Point3) :
		if self._position != value:
			self._position = value
			self.positionChanged.emit(value)

	position = pyqtProperty(QObject, fget=getposition, fset=setposition, notify=positionChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.position = self._position.proto()
		instance.rotation = self._rotation.proto()
		instance.id.extend(self._id)
		instance.scale.extend(self._scale)
		instance.scale3 = self._scale3.proto()

	def getrotation(self) -> Quat :
		return self._rotation

	def setrotation(self,value : Quat) :
		if self._rotation != value:
			self._rotation = value
			self.rotationChanged.emit(value)

	rotation = pyqtProperty(QObject, fget=getrotation, fset=setrotation, notify=rotationChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.position = self._position.proto()
		instance.rotation = self._rotation.proto()
		instance.id.extend(self._id)
		instance.scale.extend(self._scale)
		instance.scale3 = self._scale3.proto()

	def getid(self) -> int :
		return self._id

	def setid(self,value : int) :
		if self._id != value:
			self._id = value
			self.idChanged.emit(value)

	id = pyqtProperty(int, fget=getid, fset=setid, notify=idChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.position = self._position.proto()
		instance.rotation = self._rotation.proto()
		instance.id.extend(self._id)
		instance.scale.extend(self._scale)
		instance.scale3 = self._scale3.proto()

	def getscale(self) -> float :
		return self._scale

	def setscale(self,value : float) :
		if self._scale != value:
			self._scale = value
			self.scaleChanged.emit(value)

	scale = pyqtProperty(float, fget=getscale, fset=setscale, notify=scaleChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.position = self._position.proto()
		instance.rotation = self._rotation.proto()
		instance.id.extend(self._id)
		instance.scale.extend(self._scale)
		instance.scale3 = self._scale3.proto()

	def getscale3(self) -> Vector3 :
		return self._scale3

	def setscale3(self,value : Vector3) :
		if self._scale3 != value:
			self._scale3 = value
			self.scale3Changed.emit(value)

	scale3 = pyqtProperty(QObject, fget=getscale3, fset=setscale3, notify=scale3Changed)

	def proto(self) :
		instance = self.__PROTO__()
		instance.position = self._position.proto()
		instance.rotation = self._rotation.proto()
		instance.id.extend(self._id)
		instance.scale.extend(self._scale)
		instance.scale3 = self._scale3.proto()

# ------- Cubemap ------- #
class Cubemap(QObject) :
	__PROTO__ = sdk.Cubemap
	def __init__(self,right :str = str() ,left :str = str() ,top :str = str() ,bottom :str = str() ,front :str = str() ,back :str = str() ) -> Cubemap :
		self._right = right
		self._left = left
		self._top = top
		self._bottom = bottom
		self._front = front
		self._back = back
		pass
	def getright(self) -> str :
		return self._right

	def setright(self,value : str) :
		if self._right != value:
			self._right = value
			self.rightChanged.emit(value)

	right = pyqtProperty(str, fget=getright, fset=setright, notify=rightChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.right.extend(self._right)
		instance.left.extend(self._left)
		instance.top.extend(self._top)
		instance.bottom.extend(self._bottom)
		instance.front.extend(self._front)
		instance.back.extend(self._back)

	def getleft(self) -> str :
		return self._left

	def setleft(self,value : str) :
		if self._left != value:
			self._left = value
			self.leftChanged.emit(value)

	left = pyqtProperty(str, fget=getleft, fset=setleft, notify=leftChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.right.extend(self._right)
		instance.left.extend(self._left)
		instance.top.extend(self._top)
		instance.bottom.extend(self._bottom)
		instance.front.extend(self._front)
		instance.back.extend(self._back)

	def gettop(self) -> str :
		return self._top

	def settop(self,value : str) :
		if self._top != value:
			self._top = value
			self.topChanged.emit(value)

	top = pyqtProperty(str, fget=gettop, fset=settop, notify=topChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.right.extend(self._right)
		instance.left.extend(self._left)
		instance.top.extend(self._top)
		instance.bottom.extend(self._bottom)
		instance.front.extend(self._front)
		instance.back.extend(self._back)

	def getbottom(self) -> str :
		return self._bottom

	def setbottom(self,value : str) :
		if self._bottom != value:
			self._bottom = value
			self.bottomChanged.emit(value)

	bottom = pyqtProperty(str, fget=getbottom, fset=setbottom, notify=bottomChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.right.extend(self._right)
		instance.left.extend(self._left)
		instance.top.extend(self._top)
		instance.bottom.extend(self._bottom)
		instance.front.extend(self._front)
		instance.back.extend(self._back)

	def getfront(self) -> str :
		return self._front

	def setfront(self,value : str) :
		if self._front != value:
			self._front = value
			self.frontChanged.emit(value)

	front = pyqtProperty(str, fget=getfront, fset=setfront, notify=frontChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.right.extend(self._right)
		instance.left.extend(self._left)
		instance.top.extend(self._top)
		instance.bottom.extend(self._bottom)
		instance.front.extend(self._front)
		instance.back.extend(self._back)

	def getback(self) -> str :
		return self._back

	def setback(self,value : str) :
		if self._back != value:
			self._back = value
			self.backChanged.emit(value)

	back = pyqtProperty(str, fget=getback, fset=setback, notify=backChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.right.extend(self._right)
		instance.left.extend(self._left)
		instance.top.extend(self._top)
		instance.bottom.extend(self._bottom)
		instance.front.extend(self._front)
		instance.back.extend(self._back)

# ------- Cue ------- #
class Cue(QObject) :
	__PROTO__ = sdk.Cue
	def __init__(self,id :str = str() ,frame :int = int() ,value :float = float() ) -> Cue :
		self._id = id
		self._frame = frame
		self._value = value
		pass
	def getid(self) -> str :
		return self._id

	def setid(self,value : str) :
		if self._id != value:
			self._id = value
			self.idChanged.emit(value)

	id = pyqtProperty(str, fget=getid, fset=setid, notify=idChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.id.extend(self._id)
		instance.frame.extend(self._frame)
		instance.value.extend(self._value)

	def getframe(self) -> int :
		return self._frame

	def setframe(self,value : int) :
		if self._frame != value:
			self._frame = value
			self.frameChanged.emit(value)

	frame = pyqtProperty(int, fget=getframe, fset=setframe, notify=frameChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.id.extend(self._id)
		instance.frame.extend(self._frame)
		instance.value.extend(self._value)

	def getvalue(self) -> float :
		return self._value

	def setvalue(self,value : float) :
		if self._value != value:
			self._value = value
			self.valueChanged.emit(value)

	value = pyqtProperty(float, fget=getvalue, fset=setvalue, notify=valueChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.id.extend(self._id)
		instance.frame.extend(self._frame)
		instance.value.extend(self._value)

# ------- Disable ------- #
class Disable(QObject) :
	__PROTO__ = sdk.Disable
	def __init__(self) -> Disable :
		pass
# ------- DisplayProfile ------- #
class DisplayProfile(QObject) :
	__PROTO__ = sdk.DisplayProfile
	def __init__(self,name :str = str() ,qualifiers :List[DisplayProfileQualifier] = []) -> DisplayProfile :
		self._name = name
		self._qualifiers = qualifiers
		pass
	def getname(self) -> str :
		return self._name

	def setname(self,value : str) :
		if self._name != value:
			self._name = value
			self.nameChanged.emit(value)

	name = pyqtProperty(str, fget=getname, fset=setname, notify=nameChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.name.extend(self._name)
		instance.qualifiers.extend([i.proto() for i in self._qualifiers])

	def getqualifiers(self) -> DisplayProfileQualifier :
		return self._qualifiers

	def setqualifiers(self,value : List[DisplayProfileQualifier]) :
		if self._qualifiers != value:
			self._qualifiers = value
			self.qualifiersChanged.emit(value)

	qualifiers = pyqtProperty(List, fget=getqualifiers, fset=setqualifiers, notify=qualifiersChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.name.extend(self._name)
		instance.qualifiers.extend([i.proto() for i in self._qualifiers])

# ------- DisplayProfileQualifier ------- #
class DisplayProfileQualifier(QObject) :
	__PROTO__ = sdk.DisplayProfileQualifier
	def __init__(self,width :int = int() ,height :int = int() ,device_models :List[str] = [] ) -> DisplayProfileQualifier :
		self._width = width
		self._height = height
		self._device_models = device_models
		pass
	def getwidth(self) -> int :
		return self._width

	def setwidth(self,value : int) :
		if self._width != value:
			self._width = value
			self.widthChanged.emit(value)

	width = pyqtProperty(int, fget=getwidth, fset=setwidth, notify=widthChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.width.extend(self._width)
		instance.height.extend(self._height)
		instance.device_models = self._device_models

	def getheight(self) -> int :
		return self._height

	def setheight(self,value : int) :
		if self._height != value:
			self._height = value
			self.heightChanged.emit(value)

	height = pyqtProperty(int, fget=getheight, fset=setheight, notify=heightChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.width.extend(self._width)
		instance.height.extend(self._height)
		instance.device_models = self._device_models

	def getdevice_models(self) -> str :
		return self._device_models

	def setdevice_models(self,value : List[str]) :
		if self._device_models != value:
			self._device_models = value
			self.device_modelsChanged.emit(value)

	device_models = pyqtProperty(List, fget=getdevice_models, fset=setdevice_models, notify=device_modelsChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.width.extend(self._width)
		instance.height.extend(self._height)
		instance.device_models = self._device_models

# ------- DisplayProfiles ------- #
class DisplayProfiles(QObject) :
	__PROTO__ = sdk.DisplayProfiles
	def __init__(self,profiles :List[DisplayProfile] = [],auto_layout_selection :bool = bool() ) -> DisplayProfiles :
		self._profiles = profiles
		self._auto_layout_selection = auto_layout_selection
		pass
	def getprofiles(self) -> DisplayProfile :
		return self._profiles

	def setprofiles(self,value : List[DisplayProfile]) :
		if self._profiles != value:
			self._profiles = value
			self.profilesChanged.emit(value)

	profiles = pyqtProperty(List, fget=getprofiles, fset=setprofiles, notify=profilesChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.profiles.extend([i.proto() for i in self._profiles])
		instance.auto_layout_selection.extend(self._auto_layout_selection)

	def getauto_layout_selection(self) -> bool :
		return self._auto_layout_selection

	def setauto_layout_selection(self,value : bool) :
		if self._auto_layout_selection != value:
			self._auto_layout_selection = value
			self.auto_layout_selectionChanged.emit(value)

	auto_layout_selection = pyqtProperty(bool, fget=getauto_layout_selection, fset=setauto_layout_selection, notify=auto_layout_selectionChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.profiles.extend([i.proto() for i in self._profiles])
		instance.auto_layout_selection.extend(self._auto_layout_selection)

# ------- DrawDebugText ------- #
class DrawDebugText(QObject) :
	__PROTO__ = sdk.DrawDebugText
	def __init__(self,position :Point3 = None ,text :str = str() ,color :Vector4 = None ) -> DrawDebugText :
		self._position = position
		self._text = text
		self._color = color
		pass
	def getposition(self) -> Point3 :
		return self._position

	def setposition(self,value : Point3) :
		if self._position != value:
			self._position = value
			self.positionChanged.emit(value)

	position = pyqtProperty(QObject, fget=getposition, fset=setposition, notify=positionChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.position = self._position.proto()
		instance.text.extend(self._text)
		instance.color = self._color.proto()

	def gettext(self) -> str :
		return self._text

	def settext(self,value : str) :
		if self._text != value:
			self._text = value
			self.textChanged.emit(value)

	text = pyqtProperty(str, fget=gettext, fset=settext, notify=textChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.position = self._position.proto()
		instance.text.extend(self._text)
		instance.color = self._color.proto()

	def getcolor(self) -> Vector4 :
		return self._color

	def setcolor(self,value : Vector4) :
		if self._color != value:
			self._color = value
			self.colorChanged.emit(value)

	color = pyqtProperty(QObject, fget=getcolor, fset=setcolor, notify=colorChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.position = self._position.proto()
		instance.text.extend(self._text)
		instance.color = self._color.proto()

# ------- DrawLine ------- #
class DrawLine(QObject) :
	__PROTO__ = sdk.DrawLine
	def __init__(self,start_point :Point3 = None ,end_point :Point3 = None ,color :Vector4 = None ) -> DrawLine :
		self._start_point = start_point
		self._end_point = end_point
		self._color = color
		pass
	def getstart_point(self) -> Point3 :
		return self._start_point

	def setstart_point(self,value : Point3) :
		if self._start_point != value:
			self._start_point = value
			self.start_pointChanged.emit(value)

	start_point = pyqtProperty(QObject, fget=getstart_point, fset=setstart_point, notify=start_pointChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.start_point = self._start_point.proto()
		instance.end_point = self._end_point.proto()
		instance.color = self._color.proto()

	def getend_point(self) -> Point3 :
		return self._end_point

	def setend_point(self,value : Point3) :
		if self._end_point != value:
			self._end_point = value
			self.end_pointChanged.emit(value)

	end_point = pyqtProperty(QObject, fget=getend_point, fset=setend_point, notify=end_pointChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.start_point = self._start_point.proto()
		instance.end_point = self._end_point.proto()
		instance.color = self._color.proto()

	def getcolor(self) -> Vector4 :
		return self._color

	def setcolor(self,value : Vector4) :
		if self._color != value:
			self._color = value
			self.colorChanged.emit(value)

	color = pyqtProperty(QObject, fget=getcolor, fset=setcolor, notify=colorChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.start_point = self._start_point.proto()
		instance.end_point = self._end_point.proto()
		instance.color = self._color.proto()

# ------- DrawText ------- #
class DrawText(QObject) :
	__PROTO__ = sdk.DrawText
	def __init__(self,position :Point3 = None ,text :str = str() ) -> DrawText :
		self._position = position
		self._text = text
		pass
	def getposition(self) -> Point3 :
		return self._position

	def setposition(self,value : Point3) :
		if self._position != value:
			self._position = value
			self.positionChanged.emit(value)

	position = pyqtProperty(QObject, fget=getposition, fset=setposition, notify=positionChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.position = self._position.proto()
		instance.text.extend(self._text)

	def gettext(self) -> str :
		return self._text

	def settext(self,value : str) :
		if self._text != value:
			self._text = value
			self.textChanged.emit(value)

	text = pyqtProperty(str, fget=gettext, fset=settext, notify=textChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.position = self._position.proto()
		instance.text.extend(self._text)

# ------- EmbeddedComponentDesc ------- #
class EmbeddedComponentDesc(QObject) :
	__PROTO__ = sdk.EmbeddedComponentDesc
	def __init__(self,id :str = str() ,type :str = str() ,data :str = str() ,position :Point3 = None ,rotation :Quat = None ,scale :Vector3One = None ) -> EmbeddedComponentDesc :
		self._id = id
		self._type = type
		self._data = data
		self._position = position
		self._rotation = rotation
		self._scale = scale
		pass
	def getid(self) -> str :
		return self._id

	def setid(self,value : str) :
		if self._id != value:
			self._id = value
			self.idChanged.emit(value)

	id = pyqtProperty(str, fget=getid, fset=setid, notify=idChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.id.extend(self._id)
		instance.type.extend(self._type)
		instance.data.extend(self._data)
		instance.position = self._position.proto()
		instance.rotation = self._rotation.proto()
		instance.scale = self._scale.proto()

	def gettype(self) -> str :
		return self._type

	def settype(self,value : str) :
		if self._type != value:
			self._type = value
			self.typeChanged.emit(value)

	type = pyqtProperty(str, fget=gettype, fset=settype, notify=typeChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.id.extend(self._id)
		instance.type.extend(self._type)
		instance.data.extend(self._data)
		instance.position = self._position.proto()
		instance.rotation = self._rotation.proto()
		instance.scale = self._scale.proto()

	def getdata(self) -> str :
		return self._data

	def setdata(self,value : str) :
		if self._data != value:
			self._data = value
			self.dataChanged.emit(value)

	data = pyqtProperty(str, fget=getdata, fset=setdata, notify=dataChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.id.extend(self._id)
		instance.type.extend(self._type)
		instance.data.extend(self._data)
		instance.position = self._position.proto()
		instance.rotation = self._rotation.proto()
		instance.scale = self._scale.proto()

	def getposition(self) -> Point3 :
		return self._position

	def setposition(self,value : Point3) :
		if self._position != value:
			self._position = value
			self.positionChanged.emit(value)

	position = pyqtProperty(QObject, fget=getposition, fset=setposition, notify=positionChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.id.extend(self._id)
		instance.type.extend(self._type)
		instance.data.extend(self._data)
		instance.position = self._position.proto()
		instance.rotation = self._rotation.proto()
		instance.scale = self._scale.proto()

	def getrotation(self) -> Quat :
		return self._rotation

	def setrotation(self,value : Quat) :
		if self._rotation != value:
			self._rotation = value
			self.rotationChanged.emit(value)

	rotation = pyqtProperty(QObject, fget=getrotation, fset=setrotation, notify=rotationChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.id.extend(self._id)
		instance.type.extend(self._type)
		instance.data.extend(self._data)
		instance.position = self._position.proto()
		instance.rotation = self._rotation.proto()
		instance.scale = self._scale.proto()

	def getscale(self) -> Vector3One :
		return self._scale

	def setscale(self,value : Vector3One) :
		if self._scale != value:
			self._scale = value
			self.scaleChanged.emit(value)

	scale = pyqtProperty(QObject, fget=getscale, fset=setscale, notify=scaleChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.id.extend(self._id)
		instance.type.extend(self._type)
		instance.data.extend(self._data)
		instance.position = self._position.proto()
		instance.rotation = self._rotation.proto()
		instance.scale = self._scale.proto()

# ------- EmbeddedInstanceDesc ------- #
class EmbeddedInstanceDesc(QObject) :
	__PROTO__ = sdk.EmbeddedInstanceDesc
	def __init__(self,id :str = str() ,children :List[str] = [] ,data :str = str() ,position :Point3 = None ,rotation :Quat = None ,component_properties :List[ComponentPropertyDesc] = [],scale :float = float() ,scale3 :Vector3One = None ) -> EmbeddedInstanceDesc :
		self._id = id
		self._children = children
		self._data = data
		self._position = position
		self._rotation = rotation
		self._component_properties = component_properties
		self._scale = scale
		self._scale3 = scale3
		pass
	def getid(self) -> str :
		return self._id

	def setid(self,value : str) :
		if self._id != value:
			self._id = value
			self.idChanged.emit(value)

	id = pyqtProperty(str, fget=getid, fset=setid, notify=idChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.id.extend(self._id)
		instance.children = self._children
		instance.data.extend(self._data)
		instance.position = self._position.proto()
		instance.rotation = self._rotation.proto()
		instance.component_properties.extend([i.proto() for i in self._component_properties])
		instance.scale.extend(self._scale)
		instance.scale3 = self._scale3.proto()

	def getchildren(self) -> str :
		return self._children

	def setchildren(self,value : List[str]) :
		if self._children != value:
			self._children = value
			self.childrenChanged.emit(value)

	children = pyqtProperty(List, fget=getchildren, fset=setchildren, notify=childrenChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.id.extend(self._id)
		instance.children = self._children
		instance.data.extend(self._data)
		instance.position = self._position.proto()
		instance.rotation = self._rotation.proto()
		instance.component_properties.extend([i.proto() for i in self._component_properties])
		instance.scale.extend(self._scale)
		instance.scale3 = self._scale3.proto()

	def getdata(self) -> str :
		return self._data

	def setdata(self,value : str) :
		if self._data != value:
			self._data = value
			self.dataChanged.emit(value)

	data = pyqtProperty(str, fget=getdata, fset=setdata, notify=dataChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.id.extend(self._id)
		instance.children = self._children
		instance.data.extend(self._data)
		instance.position = self._position.proto()
		instance.rotation = self._rotation.proto()
		instance.component_properties.extend([i.proto() for i in self._component_properties])
		instance.scale.extend(self._scale)
		instance.scale3 = self._scale3.proto()

	def getposition(self) -> Point3 :
		return self._position

	def setposition(self,value : Point3) :
		if self._position != value:
			self._position = value
			self.positionChanged.emit(value)

	position = pyqtProperty(QObject, fget=getposition, fset=setposition, notify=positionChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.id.extend(self._id)
		instance.children = self._children
		instance.data.extend(self._data)
		instance.position = self._position.proto()
		instance.rotation = self._rotation.proto()
		instance.component_properties.extend([i.proto() for i in self._component_properties])
		instance.scale.extend(self._scale)
		instance.scale3 = self._scale3.proto()

	def getrotation(self) -> Quat :
		return self._rotation

	def setrotation(self,value : Quat) :
		if self._rotation != value:
			self._rotation = value
			self.rotationChanged.emit(value)

	rotation = pyqtProperty(QObject, fget=getrotation, fset=setrotation, notify=rotationChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.id.extend(self._id)
		instance.children = self._children
		instance.data.extend(self._data)
		instance.position = self._position.proto()
		instance.rotation = self._rotation.proto()
		instance.component_properties.extend([i.proto() for i in self._component_properties])
		instance.scale.extend(self._scale)
		instance.scale3 = self._scale3.proto()

	def getcomponent_properties(self) -> ComponentPropertyDesc :
		return self._component_properties

	def setcomponent_properties(self,value : List[ComponentPropertyDesc]) :
		if self._component_properties != value:
			self._component_properties = value
			self.component_propertiesChanged.emit(value)

	component_properties = pyqtProperty(List, fget=getcomponent_properties, fset=setcomponent_properties, notify=component_propertiesChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.id.extend(self._id)
		instance.children = self._children
		instance.data.extend(self._data)
		instance.position = self._position.proto()
		instance.rotation = self._rotation.proto()
		instance.component_properties.extend([i.proto() for i in self._component_properties])
		instance.scale.extend(self._scale)
		instance.scale3 = self._scale3.proto()

	def getscale(self) -> float :
		return self._scale

	def setscale(self,value : float) :
		if self._scale != value:
			self._scale = value
			self.scaleChanged.emit(value)

	scale = pyqtProperty(float, fget=getscale, fset=setscale, notify=scaleChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.id.extend(self._id)
		instance.children = self._children
		instance.data.extend(self._data)
		instance.position = self._position.proto()
		instance.rotation = self._rotation.proto()
		instance.component_properties.extend([i.proto() for i in self._component_properties])
		instance.scale.extend(self._scale)
		instance.scale3 = self._scale3.proto()

	def getscale3(self) -> Vector3One :
		return self._scale3

	def setscale3(self,value : Vector3One) :
		if self._scale3 != value:
			self._scale3 = value
			self.scale3Changed.emit(value)

	scale3 = pyqtProperty(QObject, fget=getscale3, fset=setscale3, notify=scale3Changed)

	def proto(self) :
		instance = self.__PROTO__()
		instance.id.extend(self._id)
		instance.children = self._children
		instance.data.extend(self._data)
		instance.position = self._position.proto()
		instance.rotation = self._rotation.proto()
		instance.component_properties.extend([i.proto() for i in self._component_properties])
		instance.scale.extend(self._scale)
		instance.scale3 = self._scale3.proto()

# ------- Enable ------- #
class Enable(QObject) :
	__PROTO__ = sdk.Enable
	def __init__(self) -> Enable :
		pass
# ------- EnableGridShapeLayer ------- #
class EnableGridShapeLayer(QObject) :
	__PROTO__ = sdk.EnableGridShapeLayer
	def __init__(self,shape :int = int() ,enable :int = int() ) -> EnableGridShapeLayer :
		self._shape = shape
		self._enable = enable
		pass
	def getshape(self) -> int :
		return self._shape

	def setshape(self,value : int) :
		if self._shape != value:
			self._shape = value
			self.shapeChanged.emit(value)

	shape = pyqtProperty(int, fget=getshape, fset=setshape, notify=shapeChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.shape.extend(self._shape)
		instance.enable.extend(self._enable)

	def getenable(self) -> int :
		return self._enable

	def setenable(self,value : int) :
		if self._enable != value:
			self._enable = value
			self.enableChanged.emit(value)

	enable = pyqtProperty(int, fget=getenable, fset=setenable, notify=enableChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.shape.extend(self._shape)
		instance.enable.extend(self._enable)

# ------- Exit ------- #
class Exit(QObject) :
	__PROTO__ = sdk.Exit
	def __init__(self,code :int = int() ) -> Exit :
		self._code = code
		pass
	def getcode(self) -> int :
		return self._code

	def setcode(self,value : int) :
		if self._code != value:
			self._code = value
			self.codeChanged.emit(value)

	code = pyqtProperty(int, fget=getcode, fset=setcode, notify=codeChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.code.extend(self._code)

# ------- FactoryDesc ------- #
class FactoryDesc(QObject) :
	__PROTO__ = sdk.FactoryDesc
	def __init__(self,prototype :str = str() ,load_dynamically :bool = bool() ,dynamic_prototype :bool = bool() ) -> FactoryDesc :
		self._prototype = prototype
		self._load_dynamically = load_dynamically
		self._dynamic_prototype = dynamic_prototype
		pass
	def getprototype(self) -> str :
		return self._prototype

	def setprototype(self,value : str) :
		if self._prototype != value:
			self._prototype = value
			self.prototypeChanged.emit(value)

	prototype = pyqtProperty(str, fget=getprototype, fset=setprototype, notify=prototypeChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.prototype.extend(self._prototype)
		instance.load_dynamically.extend(self._load_dynamically)
		instance.dynamic_prototype.extend(self._dynamic_prototype)

	def getload_dynamically(self) -> bool :
		return self._load_dynamically

	def setload_dynamically(self,value : bool) :
		if self._load_dynamically != value:
			self._load_dynamically = value
			self.load_dynamicallyChanged.emit(value)

	load_dynamically = pyqtProperty(bool, fget=getload_dynamically, fset=setload_dynamically, notify=load_dynamicallyChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.prototype.extend(self._prototype)
		instance.load_dynamically.extend(self._load_dynamically)
		instance.dynamic_prototype.extend(self._dynamic_prototype)

	def getdynamic_prototype(self) -> bool :
		return self._dynamic_prototype

	def setdynamic_prototype(self,value : bool) :
		if self._dynamic_prototype != value:
			self._dynamic_prototype = value
			self.dynamic_prototypeChanged.emit(value)

	dynamic_prototype = pyqtProperty(bool, fget=getdynamic_prototype, fset=setdynamic_prototype, notify=dynamic_prototypeChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.prototype.extend(self._prototype)
		instance.load_dynamically.extend(self._load_dynamically)
		instance.dynamic_prototype.extend(self._dynamic_prototype)

# ------- FontDesc ------- #
class FontDesc(QObject) :
	__PROTO__ = sdk.FontDesc
	def __init__(self,font :str = str() ,material :str = str() ,size :int = int() ,antialias :int = int() ,alpha :float = float() ,outline_alpha :float = float() ,outline_width :float = float() ,shadow_alpha :float = float() ,shadow_blur :int = int() ,shadow_x :float = float() ,shadow_y :float = float() ,extra_characters :str = str() ,output_format :int = int() ,all_chars :bool = bool() ,cache_width :int = int() ,cache_height :int = int() ,render_mode :int = int() ,characters :str = str() ) -> FontDesc :
		self._font = font
		self._material = material
		self._size = size
		self._antialias = antialias
		self._alpha = alpha
		self._outline_alpha = outline_alpha
		self._outline_width = outline_width
		self._shadow_alpha = shadow_alpha
		self._shadow_blur = shadow_blur
		self._shadow_x = shadow_x
		self._shadow_y = shadow_y
		self._extra_characters = extra_characters
		self._output_format = output_format
		self._all_chars = all_chars
		self._cache_width = cache_width
		self._cache_height = cache_height
		self._render_mode = render_mode
		self._characters = characters
		pass
	def getfont(self) -> str :
		return self._font

	def setfont(self,value : str) :
		if self._font != value:
			self._font = value
			self.fontChanged.emit(value)

	font = pyqtProperty(str, fget=getfont, fset=setfont, notify=fontChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.font.extend(self._font)
		instance.material.extend(self._material)
		instance.size.extend(self._size)
		instance.antialias.extend(self._antialias)
		instance.alpha.extend(self._alpha)
		instance.outline_alpha.extend(self._outline_alpha)
		instance.outline_width.extend(self._outline_width)
		instance.shadow_alpha.extend(self._shadow_alpha)
		instance.shadow_blur.extend(self._shadow_blur)
		instance.shadow_x.extend(self._shadow_x)
		instance.shadow_y.extend(self._shadow_y)
		instance.extra_characters.extend(self._extra_characters)
		instance.output_format.extend(self._output_format)
		instance.all_chars.extend(self._all_chars)
		instance.cache_width.extend(self._cache_width)
		instance.cache_height.extend(self._cache_height)
		instance.render_mode.extend(self._render_mode)
		instance.characters.extend(self._characters)

	def getmaterial(self) -> str :
		return self._material

	def setmaterial(self,value : str) :
		if self._material != value:
			self._material = value
			self.materialChanged.emit(value)

	material = pyqtProperty(str, fget=getmaterial, fset=setmaterial, notify=materialChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.font.extend(self._font)
		instance.material.extend(self._material)
		instance.size.extend(self._size)
		instance.antialias.extend(self._antialias)
		instance.alpha.extend(self._alpha)
		instance.outline_alpha.extend(self._outline_alpha)
		instance.outline_width.extend(self._outline_width)
		instance.shadow_alpha.extend(self._shadow_alpha)
		instance.shadow_blur.extend(self._shadow_blur)
		instance.shadow_x.extend(self._shadow_x)
		instance.shadow_y.extend(self._shadow_y)
		instance.extra_characters.extend(self._extra_characters)
		instance.output_format.extend(self._output_format)
		instance.all_chars.extend(self._all_chars)
		instance.cache_width.extend(self._cache_width)
		instance.cache_height.extend(self._cache_height)
		instance.render_mode.extend(self._render_mode)
		instance.characters.extend(self._characters)

	def getsize(self) -> int :
		return self._size

	def setsize(self,value : int) :
		if self._size != value:
			self._size = value
			self.sizeChanged.emit(value)

	size = pyqtProperty(int, fget=getsize, fset=setsize, notify=sizeChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.font.extend(self._font)
		instance.material.extend(self._material)
		instance.size.extend(self._size)
		instance.antialias.extend(self._antialias)
		instance.alpha.extend(self._alpha)
		instance.outline_alpha.extend(self._outline_alpha)
		instance.outline_width.extend(self._outline_width)
		instance.shadow_alpha.extend(self._shadow_alpha)
		instance.shadow_blur.extend(self._shadow_blur)
		instance.shadow_x.extend(self._shadow_x)
		instance.shadow_y.extend(self._shadow_y)
		instance.extra_characters.extend(self._extra_characters)
		instance.output_format.extend(self._output_format)
		instance.all_chars.extend(self._all_chars)
		instance.cache_width.extend(self._cache_width)
		instance.cache_height.extend(self._cache_height)
		instance.render_mode.extend(self._render_mode)
		instance.characters.extend(self._characters)

	def getantialias(self) -> int :
		return self._antialias

	def setantialias(self,value : int) :
		if self._antialias != value:
			self._antialias = value
			self.antialiasChanged.emit(value)

	antialias = pyqtProperty(int, fget=getantialias, fset=setantialias, notify=antialiasChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.font.extend(self._font)
		instance.material.extend(self._material)
		instance.size.extend(self._size)
		instance.antialias.extend(self._antialias)
		instance.alpha.extend(self._alpha)
		instance.outline_alpha.extend(self._outline_alpha)
		instance.outline_width.extend(self._outline_width)
		instance.shadow_alpha.extend(self._shadow_alpha)
		instance.shadow_blur.extend(self._shadow_blur)
		instance.shadow_x.extend(self._shadow_x)
		instance.shadow_y.extend(self._shadow_y)
		instance.extra_characters.extend(self._extra_characters)
		instance.output_format.extend(self._output_format)
		instance.all_chars.extend(self._all_chars)
		instance.cache_width.extend(self._cache_width)
		instance.cache_height.extend(self._cache_height)
		instance.render_mode.extend(self._render_mode)
		instance.characters.extend(self._characters)

	def getalpha(self) -> float :
		return self._alpha

	def setalpha(self,value : float) :
		if self._alpha != value:
			self._alpha = value
			self.alphaChanged.emit(value)

	alpha = pyqtProperty(float, fget=getalpha, fset=setalpha, notify=alphaChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.font.extend(self._font)
		instance.material.extend(self._material)
		instance.size.extend(self._size)
		instance.antialias.extend(self._antialias)
		instance.alpha.extend(self._alpha)
		instance.outline_alpha.extend(self._outline_alpha)
		instance.outline_width.extend(self._outline_width)
		instance.shadow_alpha.extend(self._shadow_alpha)
		instance.shadow_blur.extend(self._shadow_blur)
		instance.shadow_x.extend(self._shadow_x)
		instance.shadow_y.extend(self._shadow_y)
		instance.extra_characters.extend(self._extra_characters)
		instance.output_format.extend(self._output_format)
		instance.all_chars.extend(self._all_chars)
		instance.cache_width.extend(self._cache_width)
		instance.cache_height.extend(self._cache_height)
		instance.render_mode.extend(self._render_mode)
		instance.characters.extend(self._characters)

	def getoutline_alpha(self) -> float :
		return self._outline_alpha

	def setoutline_alpha(self,value : float) :
		if self._outline_alpha != value:
			self._outline_alpha = value
			self.outline_alphaChanged.emit(value)

	outline_alpha = pyqtProperty(float, fget=getoutline_alpha, fset=setoutline_alpha, notify=outline_alphaChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.font.extend(self._font)
		instance.material.extend(self._material)
		instance.size.extend(self._size)
		instance.antialias.extend(self._antialias)
		instance.alpha.extend(self._alpha)
		instance.outline_alpha.extend(self._outline_alpha)
		instance.outline_width.extend(self._outline_width)
		instance.shadow_alpha.extend(self._shadow_alpha)
		instance.shadow_blur.extend(self._shadow_blur)
		instance.shadow_x.extend(self._shadow_x)
		instance.shadow_y.extend(self._shadow_y)
		instance.extra_characters.extend(self._extra_characters)
		instance.output_format.extend(self._output_format)
		instance.all_chars.extend(self._all_chars)
		instance.cache_width.extend(self._cache_width)
		instance.cache_height.extend(self._cache_height)
		instance.render_mode.extend(self._render_mode)
		instance.characters.extend(self._characters)

	def getoutline_width(self) -> float :
		return self._outline_width

	def setoutline_width(self,value : float) :
		if self._outline_width != value:
			self._outline_width = value
			self.outline_widthChanged.emit(value)

	outline_width = pyqtProperty(float, fget=getoutline_width, fset=setoutline_width, notify=outline_widthChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.font.extend(self._font)
		instance.material.extend(self._material)
		instance.size.extend(self._size)
		instance.antialias.extend(self._antialias)
		instance.alpha.extend(self._alpha)
		instance.outline_alpha.extend(self._outline_alpha)
		instance.outline_width.extend(self._outline_width)
		instance.shadow_alpha.extend(self._shadow_alpha)
		instance.shadow_blur.extend(self._shadow_blur)
		instance.shadow_x.extend(self._shadow_x)
		instance.shadow_y.extend(self._shadow_y)
		instance.extra_characters.extend(self._extra_characters)
		instance.output_format.extend(self._output_format)
		instance.all_chars.extend(self._all_chars)
		instance.cache_width.extend(self._cache_width)
		instance.cache_height.extend(self._cache_height)
		instance.render_mode.extend(self._render_mode)
		instance.characters.extend(self._characters)

	def getshadow_alpha(self) -> float :
		return self._shadow_alpha

	def setshadow_alpha(self,value : float) :
		if self._shadow_alpha != value:
			self._shadow_alpha = value
			self.shadow_alphaChanged.emit(value)

	shadow_alpha = pyqtProperty(float, fget=getshadow_alpha, fset=setshadow_alpha, notify=shadow_alphaChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.font.extend(self._font)
		instance.material.extend(self._material)
		instance.size.extend(self._size)
		instance.antialias.extend(self._antialias)
		instance.alpha.extend(self._alpha)
		instance.outline_alpha.extend(self._outline_alpha)
		instance.outline_width.extend(self._outline_width)
		instance.shadow_alpha.extend(self._shadow_alpha)
		instance.shadow_blur.extend(self._shadow_blur)
		instance.shadow_x.extend(self._shadow_x)
		instance.shadow_y.extend(self._shadow_y)
		instance.extra_characters.extend(self._extra_characters)
		instance.output_format.extend(self._output_format)
		instance.all_chars.extend(self._all_chars)
		instance.cache_width.extend(self._cache_width)
		instance.cache_height.extend(self._cache_height)
		instance.render_mode.extend(self._render_mode)
		instance.characters.extend(self._characters)

	def getshadow_blur(self) -> int :
		return self._shadow_blur

	def setshadow_blur(self,value : int) :
		if self._shadow_blur != value:
			self._shadow_blur = value
			self.shadow_blurChanged.emit(value)

	shadow_blur = pyqtProperty(int, fget=getshadow_blur, fset=setshadow_blur, notify=shadow_blurChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.font.extend(self._font)
		instance.material.extend(self._material)
		instance.size.extend(self._size)
		instance.antialias.extend(self._antialias)
		instance.alpha.extend(self._alpha)
		instance.outline_alpha.extend(self._outline_alpha)
		instance.outline_width.extend(self._outline_width)
		instance.shadow_alpha.extend(self._shadow_alpha)
		instance.shadow_blur.extend(self._shadow_blur)
		instance.shadow_x.extend(self._shadow_x)
		instance.shadow_y.extend(self._shadow_y)
		instance.extra_characters.extend(self._extra_characters)
		instance.output_format.extend(self._output_format)
		instance.all_chars.extend(self._all_chars)
		instance.cache_width.extend(self._cache_width)
		instance.cache_height.extend(self._cache_height)
		instance.render_mode.extend(self._render_mode)
		instance.characters.extend(self._characters)

	def getshadow_x(self) -> float :
		return self._shadow_x

	def setshadow_x(self,value : float) :
		if self._shadow_x != value:
			self._shadow_x = value
			self.shadow_xChanged.emit(value)

	shadow_x = pyqtProperty(float, fget=getshadow_x, fset=setshadow_x, notify=shadow_xChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.font.extend(self._font)
		instance.material.extend(self._material)
		instance.size.extend(self._size)
		instance.antialias.extend(self._antialias)
		instance.alpha.extend(self._alpha)
		instance.outline_alpha.extend(self._outline_alpha)
		instance.outline_width.extend(self._outline_width)
		instance.shadow_alpha.extend(self._shadow_alpha)
		instance.shadow_blur.extend(self._shadow_blur)
		instance.shadow_x.extend(self._shadow_x)
		instance.shadow_y.extend(self._shadow_y)
		instance.extra_characters.extend(self._extra_characters)
		instance.output_format.extend(self._output_format)
		instance.all_chars.extend(self._all_chars)
		instance.cache_width.extend(self._cache_width)
		instance.cache_height.extend(self._cache_height)
		instance.render_mode.extend(self._render_mode)
		instance.characters.extend(self._characters)

	def getshadow_y(self) -> float :
		return self._shadow_y

	def setshadow_y(self,value : float) :
		if self._shadow_y != value:
			self._shadow_y = value
			self.shadow_yChanged.emit(value)

	shadow_y = pyqtProperty(float, fget=getshadow_y, fset=setshadow_y, notify=shadow_yChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.font.extend(self._font)
		instance.material.extend(self._material)
		instance.size.extend(self._size)
		instance.antialias.extend(self._antialias)
		instance.alpha.extend(self._alpha)
		instance.outline_alpha.extend(self._outline_alpha)
		instance.outline_width.extend(self._outline_width)
		instance.shadow_alpha.extend(self._shadow_alpha)
		instance.shadow_blur.extend(self._shadow_blur)
		instance.shadow_x.extend(self._shadow_x)
		instance.shadow_y.extend(self._shadow_y)
		instance.extra_characters.extend(self._extra_characters)
		instance.output_format.extend(self._output_format)
		instance.all_chars.extend(self._all_chars)
		instance.cache_width.extend(self._cache_width)
		instance.cache_height.extend(self._cache_height)
		instance.render_mode.extend(self._render_mode)
		instance.characters.extend(self._characters)

	def getextra_characters(self) -> str :
		return self._extra_characters

	def setextra_characters(self,value : str) :
		if self._extra_characters != value:
			self._extra_characters = value
			self.extra_charactersChanged.emit(value)

	extra_characters = pyqtProperty(str, fget=getextra_characters, fset=setextra_characters, notify=extra_charactersChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.font.extend(self._font)
		instance.material.extend(self._material)
		instance.size.extend(self._size)
		instance.antialias.extend(self._antialias)
		instance.alpha.extend(self._alpha)
		instance.outline_alpha.extend(self._outline_alpha)
		instance.outline_width.extend(self._outline_width)
		instance.shadow_alpha.extend(self._shadow_alpha)
		instance.shadow_blur.extend(self._shadow_blur)
		instance.shadow_x.extend(self._shadow_x)
		instance.shadow_y.extend(self._shadow_y)
		instance.extra_characters.extend(self._extra_characters)
		instance.output_format.extend(self._output_format)
		instance.all_chars.extend(self._all_chars)
		instance.cache_width.extend(self._cache_width)
		instance.cache_height.extend(self._cache_height)
		instance.render_mode.extend(self._render_mode)
		instance.characters.extend(self._characters)

	def getoutput_format(self) -> int :
		return self._output_format

	def setoutput_format(self,value : int) :
		if self._output_format != value:
			self._output_format = value
			self.output_formatChanged.emit(value)

	output_format = pyqtProperty(int, fget=getoutput_format, fset=setoutput_format, notify=output_formatChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.font.extend(self._font)
		instance.material.extend(self._material)
		instance.size.extend(self._size)
		instance.antialias.extend(self._antialias)
		instance.alpha.extend(self._alpha)
		instance.outline_alpha.extend(self._outline_alpha)
		instance.outline_width.extend(self._outline_width)
		instance.shadow_alpha.extend(self._shadow_alpha)
		instance.shadow_blur.extend(self._shadow_blur)
		instance.shadow_x.extend(self._shadow_x)
		instance.shadow_y.extend(self._shadow_y)
		instance.extra_characters.extend(self._extra_characters)
		instance.output_format.extend(self._output_format)
		instance.all_chars.extend(self._all_chars)
		instance.cache_width.extend(self._cache_width)
		instance.cache_height.extend(self._cache_height)
		instance.render_mode.extend(self._render_mode)
		instance.characters.extend(self._characters)

	def getall_chars(self) -> bool :
		return self._all_chars

	def setall_chars(self,value : bool) :
		if self._all_chars != value:
			self._all_chars = value
			self.all_charsChanged.emit(value)

	all_chars = pyqtProperty(bool, fget=getall_chars, fset=setall_chars, notify=all_charsChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.font.extend(self._font)
		instance.material.extend(self._material)
		instance.size.extend(self._size)
		instance.antialias.extend(self._antialias)
		instance.alpha.extend(self._alpha)
		instance.outline_alpha.extend(self._outline_alpha)
		instance.outline_width.extend(self._outline_width)
		instance.shadow_alpha.extend(self._shadow_alpha)
		instance.shadow_blur.extend(self._shadow_blur)
		instance.shadow_x.extend(self._shadow_x)
		instance.shadow_y.extend(self._shadow_y)
		instance.extra_characters.extend(self._extra_characters)
		instance.output_format.extend(self._output_format)
		instance.all_chars.extend(self._all_chars)
		instance.cache_width.extend(self._cache_width)
		instance.cache_height.extend(self._cache_height)
		instance.render_mode.extend(self._render_mode)
		instance.characters.extend(self._characters)

	def getcache_width(self) -> int :
		return self._cache_width

	def setcache_width(self,value : int) :
		if self._cache_width != value:
			self._cache_width = value
			self.cache_widthChanged.emit(value)

	cache_width = pyqtProperty(int, fget=getcache_width, fset=setcache_width, notify=cache_widthChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.font.extend(self._font)
		instance.material.extend(self._material)
		instance.size.extend(self._size)
		instance.antialias.extend(self._antialias)
		instance.alpha.extend(self._alpha)
		instance.outline_alpha.extend(self._outline_alpha)
		instance.outline_width.extend(self._outline_width)
		instance.shadow_alpha.extend(self._shadow_alpha)
		instance.shadow_blur.extend(self._shadow_blur)
		instance.shadow_x.extend(self._shadow_x)
		instance.shadow_y.extend(self._shadow_y)
		instance.extra_characters.extend(self._extra_characters)
		instance.output_format.extend(self._output_format)
		instance.all_chars.extend(self._all_chars)
		instance.cache_width.extend(self._cache_width)
		instance.cache_height.extend(self._cache_height)
		instance.render_mode.extend(self._render_mode)
		instance.characters.extend(self._characters)

	def getcache_height(self) -> int :
		return self._cache_height

	def setcache_height(self,value : int) :
		if self._cache_height != value:
			self._cache_height = value
			self.cache_heightChanged.emit(value)

	cache_height = pyqtProperty(int, fget=getcache_height, fset=setcache_height, notify=cache_heightChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.font.extend(self._font)
		instance.material.extend(self._material)
		instance.size.extend(self._size)
		instance.antialias.extend(self._antialias)
		instance.alpha.extend(self._alpha)
		instance.outline_alpha.extend(self._outline_alpha)
		instance.outline_width.extend(self._outline_width)
		instance.shadow_alpha.extend(self._shadow_alpha)
		instance.shadow_blur.extend(self._shadow_blur)
		instance.shadow_x.extend(self._shadow_x)
		instance.shadow_y.extend(self._shadow_y)
		instance.extra_characters.extend(self._extra_characters)
		instance.output_format.extend(self._output_format)
		instance.all_chars.extend(self._all_chars)
		instance.cache_width.extend(self._cache_width)
		instance.cache_height.extend(self._cache_height)
		instance.render_mode.extend(self._render_mode)
		instance.characters.extend(self._characters)

	def getrender_mode(self) -> int :
		return self._render_mode

	def setrender_mode(self,value : int) :
		if self._render_mode != value:
			self._render_mode = value
			self.render_modeChanged.emit(value)

	render_mode = pyqtProperty(int, fget=getrender_mode, fset=setrender_mode, notify=render_modeChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.font.extend(self._font)
		instance.material.extend(self._material)
		instance.size.extend(self._size)
		instance.antialias.extend(self._antialias)
		instance.alpha.extend(self._alpha)
		instance.outline_alpha.extend(self._outline_alpha)
		instance.outline_width.extend(self._outline_width)
		instance.shadow_alpha.extend(self._shadow_alpha)
		instance.shadow_blur.extend(self._shadow_blur)
		instance.shadow_x.extend(self._shadow_x)
		instance.shadow_y.extend(self._shadow_y)
		instance.extra_characters.extend(self._extra_characters)
		instance.output_format.extend(self._output_format)
		instance.all_chars.extend(self._all_chars)
		instance.cache_width.extend(self._cache_width)
		instance.cache_height.extend(self._cache_height)
		instance.render_mode.extend(self._render_mode)
		instance.characters.extend(self._characters)

	def getcharacters(self) -> str :
		return self._characters

	def setcharacters(self,value : str) :
		if self._characters != value:
			self._characters = value
			self.charactersChanged.emit(value)

	characters = pyqtProperty(str, fget=getcharacters, fset=setcharacters, notify=charactersChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.font.extend(self._font)
		instance.material.extend(self._material)
		instance.size.extend(self._size)
		instance.antialias.extend(self._antialias)
		instance.alpha.extend(self._alpha)
		instance.outline_alpha.extend(self._outline_alpha)
		instance.outline_width.extend(self._outline_width)
		instance.shadow_alpha.extend(self._shadow_alpha)
		instance.shadow_blur.extend(self._shadow_blur)
		instance.shadow_x.extend(self._shadow_x)
		instance.shadow_y.extend(self._shadow_y)
		instance.extra_characters.extend(self._extra_characters)
		instance.output_format.extend(self._output_format)
		instance.all_chars.extend(self._all_chars)
		instance.cache_width.extend(self._cache_width)
		instance.cache_height.extend(self._cache_height)
		instance.render_mode.extend(self._render_mode)
		instance.characters.extend(self._characters)

# ------- FontMap ------- #
class FontMap(QObject) :
	__PROTO__ = sdk.FontMap
	def __init__(self,material :str = str() ,glyph_bank :str = str() ,font :str = str() ,size :int = int() ,antialias :int = int() ,shadow_x :float = float() ,shadow_y :float = float() ,shadow_blur :int = int() ,shadow_alpha :float = float() ,alpha :float = float() ,outline_alpha :float = float() ,outline_width :float = float() ,layer_mask :int = int() ,output_format :int = int() ,render_mode :int = int() ,all_chars :bool = bool() ,characters :str = str() ,cache_width :int = int() ,cache_height :int = int() ,sdf_spread :float = float() ,sdf_outline :float = float() ,sdf_shadow :float = float() ,padding :int = int() ) -> FontMap :
		self._material = material
		self._glyph_bank = glyph_bank
		self._font = font
		self._size = size
		self._antialias = antialias
		self._shadow_x = shadow_x
		self._shadow_y = shadow_y
		self._shadow_blur = shadow_blur
		self._shadow_alpha = shadow_alpha
		self._alpha = alpha
		self._outline_alpha = outline_alpha
		self._outline_width = outline_width
		self._layer_mask = layer_mask
		self._output_format = output_format
		self._render_mode = render_mode
		self._all_chars = all_chars
		self._characters = characters
		self._cache_width = cache_width
		self._cache_height = cache_height
		self._sdf_spread = sdf_spread
		self._sdf_outline = sdf_outline
		self._sdf_shadow = sdf_shadow
		self._padding = padding
		pass
	def getmaterial(self) -> str :
		return self._material

	def setmaterial(self,value : str) :
		if self._material != value:
			self._material = value
			self.materialChanged.emit(value)

	material = pyqtProperty(str, fget=getmaterial, fset=setmaterial, notify=materialChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.material.extend(self._material)
		instance.glyph_bank.extend(self._glyph_bank)
		instance.font.extend(self._font)
		instance.size.extend(self._size)
		instance.antialias.extend(self._antialias)
		instance.shadow_x.extend(self._shadow_x)
		instance.shadow_y.extend(self._shadow_y)
		instance.shadow_blur.extend(self._shadow_blur)
		instance.shadow_alpha.extend(self._shadow_alpha)
		instance.alpha.extend(self._alpha)
		instance.outline_alpha.extend(self._outline_alpha)
		instance.outline_width.extend(self._outline_width)
		instance.layer_mask.extend(self._layer_mask)
		instance.output_format.extend(self._output_format)
		instance.render_mode.extend(self._render_mode)
		instance.all_chars.extend(self._all_chars)
		instance.characters.extend(self._characters)
		instance.cache_width.extend(self._cache_width)
		instance.cache_height.extend(self._cache_height)
		instance.sdf_spread.extend(self._sdf_spread)
		instance.sdf_outline.extend(self._sdf_outline)
		instance.sdf_shadow.extend(self._sdf_shadow)
		instance.padding.extend(self._padding)

	def getglyph_bank(self) -> str :
		return self._glyph_bank

	def setglyph_bank(self,value : str) :
		if self._glyph_bank != value:
			self._glyph_bank = value
			self.glyph_bankChanged.emit(value)

	glyph_bank = pyqtProperty(str, fget=getglyph_bank, fset=setglyph_bank, notify=glyph_bankChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.material.extend(self._material)
		instance.glyph_bank.extend(self._glyph_bank)
		instance.font.extend(self._font)
		instance.size.extend(self._size)
		instance.antialias.extend(self._antialias)
		instance.shadow_x.extend(self._shadow_x)
		instance.shadow_y.extend(self._shadow_y)
		instance.shadow_blur.extend(self._shadow_blur)
		instance.shadow_alpha.extend(self._shadow_alpha)
		instance.alpha.extend(self._alpha)
		instance.outline_alpha.extend(self._outline_alpha)
		instance.outline_width.extend(self._outline_width)
		instance.layer_mask.extend(self._layer_mask)
		instance.output_format.extend(self._output_format)
		instance.render_mode.extend(self._render_mode)
		instance.all_chars.extend(self._all_chars)
		instance.characters.extend(self._characters)
		instance.cache_width.extend(self._cache_width)
		instance.cache_height.extend(self._cache_height)
		instance.sdf_spread.extend(self._sdf_spread)
		instance.sdf_outline.extend(self._sdf_outline)
		instance.sdf_shadow.extend(self._sdf_shadow)
		instance.padding.extend(self._padding)

	def getfont(self) -> str :
		return self._font

	def setfont(self,value : str) :
		if self._font != value:
			self._font = value
			self.fontChanged.emit(value)

	font = pyqtProperty(str, fget=getfont, fset=setfont, notify=fontChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.material.extend(self._material)
		instance.glyph_bank.extend(self._glyph_bank)
		instance.font.extend(self._font)
		instance.size.extend(self._size)
		instance.antialias.extend(self._antialias)
		instance.shadow_x.extend(self._shadow_x)
		instance.shadow_y.extend(self._shadow_y)
		instance.shadow_blur.extend(self._shadow_blur)
		instance.shadow_alpha.extend(self._shadow_alpha)
		instance.alpha.extend(self._alpha)
		instance.outline_alpha.extend(self._outline_alpha)
		instance.outline_width.extend(self._outline_width)
		instance.layer_mask.extend(self._layer_mask)
		instance.output_format.extend(self._output_format)
		instance.render_mode.extend(self._render_mode)
		instance.all_chars.extend(self._all_chars)
		instance.characters.extend(self._characters)
		instance.cache_width.extend(self._cache_width)
		instance.cache_height.extend(self._cache_height)
		instance.sdf_spread.extend(self._sdf_spread)
		instance.sdf_outline.extend(self._sdf_outline)
		instance.sdf_shadow.extend(self._sdf_shadow)
		instance.padding.extend(self._padding)

	def getsize(self) -> int :
		return self._size

	def setsize(self,value : int) :
		if self._size != value:
			self._size = value
			self.sizeChanged.emit(value)

	size = pyqtProperty(int, fget=getsize, fset=setsize, notify=sizeChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.material.extend(self._material)
		instance.glyph_bank.extend(self._glyph_bank)
		instance.font.extend(self._font)
		instance.size.extend(self._size)
		instance.antialias.extend(self._antialias)
		instance.shadow_x.extend(self._shadow_x)
		instance.shadow_y.extend(self._shadow_y)
		instance.shadow_blur.extend(self._shadow_blur)
		instance.shadow_alpha.extend(self._shadow_alpha)
		instance.alpha.extend(self._alpha)
		instance.outline_alpha.extend(self._outline_alpha)
		instance.outline_width.extend(self._outline_width)
		instance.layer_mask.extend(self._layer_mask)
		instance.output_format.extend(self._output_format)
		instance.render_mode.extend(self._render_mode)
		instance.all_chars.extend(self._all_chars)
		instance.characters.extend(self._characters)
		instance.cache_width.extend(self._cache_width)
		instance.cache_height.extend(self._cache_height)
		instance.sdf_spread.extend(self._sdf_spread)
		instance.sdf_outline.extend(self._sdf_outline)
		instance.sdf_shadow.extend(self._sdf_shadow)
		instance.padding.extend(self._padding)

	def getantialias(self) -> int :
		return self._antialias

	def setantialias(self,value : int) :
		if self._antialias != value:
			self._antialias = value
			self.antialiasChanged.emit(value)

	antialias = pyqtProperty(int, fget=getantialias, fset=setantialias, notify=antialiasChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.material.extend(self._material)
		instance.glyph_bank.extend(self._glyph_bank)
		instance.font.extend(self._font)
		instance.size.extend(self._size)
		instance.antialias.extend(self._antialias)
		instance.shadow_x.extend(self._shadow_x)
		instance.shadow_y.extend(self._shadow_y)
		instance.shadow_blur.extend(self._shadow_blur)
		instance.shadow_alpha.extend(self._shadow_alpha)
		instance.alpha.extend(self._alpha)
		instance.outline_alpha.extend(self._outline_alpha)
		instance.outline_width.extend(self._outline_width)
		instance.layer_mask.extend(self._layer_mask)
		instance.output_format.extend(self._output_format)
		instance.render_mode.extend(self._render_mode)
		instance.all_chars.extend(self._all_chars)
		instance.characters.extend(self._characters)
		instance.cache_width.extend(self._cache_width)
		instance.cache_height.extend(self._cache_height)
		instance.sdf_spread.extend(self._sdf_spread)
		instance.sdf_outline.extend(self._sdf_outline)
		instance.sdf_shadow.extend(self._sdf_shadow)
		instance.padding.extend(self._padding)

	def getshadow_x(self) -> float :
		return self._shadow_x

	def setshadow_x(self,value : float) :
		if self._shadow_x != value:
			self._shadow_x = value
			self.shadow_xChanged.emit(value)

	shadow_x = pyqtProperty(float, fget=getshadow_x, fset=setshadow_x, notify=shadow_xChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.material.extend(self._material)
		instance.glyph_bank.extend(self._glyph_bank)
		instance.font.extend(self._font)
		instance.size.extend(self._size)
		instance.antialias.extend(self._antialias)
		instance.shadow_x.extend(self._shadow_x)
		instance.shadow_y.extend(self._shadow_y)
		instance.shadow_blur.extend(self._shadow_blur)
		instance.shadow_alpha.extend(self._shadow_alpha)
		instance.alpha.extend(self._alpha)
		instance.outline_alpha.extend(self._outline_alpha)
		instance.outline_width.extend(self._outline_width)
		instance.layer_mask.extend(self._layer_mask)
		instance.output_format.extend(self._output_format)
		instance.render_mode.extend(self._render_mode)
		instance.all_chars.extend(self._all_chars)
		instance.characters.extend(self._characters)
		instance.cache_width.extend(self._cache_width)
		instance.cache_height.extend(self._cache_height)
		instance.sdf_spread.extend(self._sdf_spread)
		instance.sdf_outline.extend(self._sdf_outline)
		instance.sdf_shadow.extend(self._sdf_shadow)
		instance.padding.extend(self._padding)

	def getshadow_y(self) -> float :
		return self._shadow_y

	def setshadow_y(self,value : float) :
		if self._shadow_y != value:
			self._shadow_y = value
			self.shadow_yChanged.emit(value)

	shadow_y = pyqtProperty(float, fget=getshadow_y, fset=setshadow_y, notify=shadow_yChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.material.extend(self._material)
		instance.glyph_bank.extend(self._glyph_bank)
		instance.font.extend(self._font)
		instance.size.extend(self._size)
		instance.antialias.extend(self._antialias)
		instance.shadow_x.extend(self._shadow_x)
		instance.shadow_y.extend(self._shadow_y)
		instance.shadow_blur.extend(self._shadow_blur)
		instance.shadow_alpha.extend(self._shadow_alpha)
		instance.alpha.extend(self._alpha)
		instance.outline_alpha.extend(self._outline_alpha)
		instance.outline_width.extend(self._outline_width)
		instance.layer_mask.extend(self._layer_mask)
		instance.output_format.extend(self._output_format)
		instance.render_mode.extend(self._render_mode)
		instance.all_chars.extend(self._all_chars)
		instance.characters.extend(self._characters)
		instance.cache_width.extend(self._cache_width)
		instance.cache_height.extend(self._cache_height)
		instance.sdf_spread.extend(self._sdf_spread)
		instance.sdf_outline.extend(self._sdf_outline)
		instance.sdf_shadow.extend(self._sdf_shadow)
		instance.padding.extend(self._padding)

	def getshadow_blur(self) -> int :
		return self._shadow_blur

	def setshadow_blur(self,value : int) :
		if self._shadow_blur != value:
			self._shadow_blur = value
			self.shadow_blurChanged.emit(value)

	shadow_blur = pyqtProperty(int, fget=getshadow_blur, fset=setshadow_blur, notify=shadow_blurChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.material.extend(self._material)
		instance.glyph_bank.extend(self._glyph_bank)
		instance.font.extend(self._font)
		instance.size.extend(self._size)
		instance.antialias.extend(self._antialias)
		instance.shadow_x.extend(self._shadow_x)
		instance.shadow_y.extend(self._shadow_y)
		instance.shadow_blur.extend(self._shadow_blur)
		instance.shadow_alpha.extend(self._shadow_alpha)
		instance.alpha.extend(self._alpha)
		instance.outline_alpha.extend(self._outline_alpha)
		instance.outline_width.extend(self._outline_width)
		instance.layer_mask.extend(self._layer_mask)
		instance.output_format.extend(self._output_format)
		instance.render_mode.extend(self._render_mode)
		instance.all_chars.extend(self._all_chars)
		instance.characters.extend(self._characters)
		instance.cache_width.extend(self._cache_width)
		instance.cache_height.extend(self._cache_height)
		instance.sdf_spread.extend(self._sdf_spread)
		instance.sdf_outline.extend(self._sdf_outline)
		instance.sdf_shadow.extend(self._sdf_shadow)
		instance.padding.extend(self._padding)

	def getshadow_alpha(self) -> float :
		return self._shadow_alpha

	def setshadow_alpha(self,value : float) :
		if self._shadow_alpha != value:
			self._shadow_alpha = value
			self.shadow_alphaChanged.emit(value)

	shadow_alpha = pyqtProperty(float, fget=getshadow_alpha, fset=setshadow_alpha, notify=shadow_alphaChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.material.extend(self._material)
		instance.glyph_bank.extend(self._glyph_bank)
		instance.font.extend(self._font)
		instance.size.extend(self._size)
		instance.antialias.extend(self._antialias)
		instance.shadow_x.extend(self._shadow_x)
		instance.shadow_y.extend(self._shadow_y)
		instance.shadow_blur.extend(self._shadow_blur)
		instance.shadow_alpha.extend(self._shadow_alpha)
		instance.alpha.extend(self._alpha)
		instance.outline_alpha.extend(self._outline_alpha)
		instance.outline_width.extend(self._outline_width)
		instance.layer_mask.extend(self._layer_mask)
		instance.output_format.extend(self._output_format)
		instance.render_mode.extend(self._render_mode)
		instance.all_chars.extend(self._all_chars)
		instance.characters.extend(self._characters)
		instance.cache_width.extend(self._cache_width)
		instance.cache_height.extend(self._cache_height)
		instance.sdf_spread.extend(self._sdf_spread)
		instance.sdf_outline.extend(self._sdf_outline)
		instance.sdf_shadow.extend(self._sdf_shadow)
		instance.padding.extend(self._padding)

	def getalpha(self) -> float :
		return self._alpha

	def setalpha(self,value : float) :
		if self._alpha != value:
			self._alpha = value
			self.alphaChanged.emit(value)

	alpha = pyqtProperty(float, fget=getalpha, fset=setalpha, notify=alphaChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.material.extend(self._material)
		instance.glyph_bank.extend(self._glyph_bank)
		instance.font.extend(self._font)
		instance.size.extend(self._size)
		instance.antialias.extend(self._antialias)
		instance.shadow_x.extend(self._shadow_x)
		instance.shadow_y.extend(self._shadow_y)
		instance.shadow_blur.extend(self._shadow_blur)
		instance.shadow_alpha.extend(self._shadow_alpha)
		instance.alpha.extend(self._alpha)
		instance.outline_alpha.extend(self._outline_alpha)
		instance.outline_width.extend(self._outline_width)
		instance.layer_mask.extend(self._layer_mask)
		instance.output_format.extend(self._output_format)
		instance.render_mode.extend(self._render_mode)
		instance.all_chars.extend(self._all_chars)
		instance.characters.extend(self._characters)
		instance.cache_width.extend(self._cache_width)
		instance.cache_height.extend(self._cache_height)
		instance.sdf_spread.extend(self._sdf_spread)
		instance.sdf_outline.extend(self._sdf_outline)
		instance.sdf_shadow.extend(self._sdf_shadow)
		instance.padding.extend(self._padding)

	def getoutline_alpha(self) -> float :
		return self._outline_alpha

	def setoutline_alpha(self,value : float) :
		if self._outline_alpha != value:
			self._outline_alpha = value
			self.outline_alphaChanged.emit(value)

	outline_alpha = pyqtProperty(float, fget=getoutline_alpha, fset=setoutline_alpha, notify=outline_alphaChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.material.extend(self._material)
		instance.glyph_bank.extend(self._glyph_bank)
		instance.font.extend(self._font)
		instance.size.extend(self._size)
		instance.antialias.extend(self._antialias)
		instance.shadow_x.extend(self._shadow_x)
		instance.shadow_y.extend(self._shadow_y)
		instance.shadow_blur.extend(self._shadow_blur)
		instance.shadow_alpha.extend(self._shadow_alpha)
		instance.alpha.extend(self._alpha)
		instance.outline_alpha.extend(self._outline_alpha)
		instance.outline_width.extend(self._outline_width)
		instance.layer_mask.extend(self._layer_mask)
		instance.output_format.extend(self._output_format)
		instance.render_mode.extend(self._render_mode)
		instance.all_chars.extend(self._all_chars)
		instance.characters.extend(self._characters)
		instance.cache_width.extend(self._cache_width)
		instance.cache_height.extend(self._cache_height)
		instance.sdf_spread.extend(self._sdf_spread)
		instance.sdf_outline.extend(self._sdf_outline)
		instance.sdf_shadow.extend(self._sdf_shadow)
		instance.padding.extend(self._padding)

	def getoutline_width(self) -> float :
		return self._outline_width

	def setoutline_width(self,value : float) :
		if self._outline_width != value:
			self._outline_width = value
			self.outline_widthChanged.emit(value)

	outline_width = pyqtProperty(float, fget=getoutline_width, fset=setoutline_width, notify=outline_widthChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.material.extend(self._material)
		instance.glyph_bank.extend(self._glyph_bank)
		instance.font.extend(self._font)
		instance.size.extend(self._size)
		instance.antialias.extend(self._antialias)
		instance.shadow_x.extend(self._shadow_x)
		instance.shadow_y.extend(self._shadow_y)
		instance.shadow_blur.extend(self._shadow_blur)
		instance.shadow_alpha.extend(self._shadow_alpha)
		instance.alpha.extend(self._alpha)
		instance.outline_alpha.extend(self._outline_alpha)
		instance.outline_width.extend(self._outline_width)
		instance.layer_mask.extend(self._layer_mask)
		instance.output_format.extend(self._output_format)
		instance.render_mode.extend(self._render_mode)
		instance.all_chars.extend(self._all_chars)
		instance.characters.extend(self._characters)
		instance.cache_width.extend(self._cache_width)
		instance.cache_height.extend(self._cache_height)
		instance.sdf_spread.extend(self._sdf_spread)
		instance.sdf_outline.extend(self._sdf_outline)
		instance.sdf_shadow.extend(self._sdf_shadow)
		instance.padding.extend(self._padding)

	def getlayer_mask(self) -> int :
		return self._layer_mask

	def setlayer_mask(self,value : int) :
		if self._layer_mask != value:
			self._layer_mask = value
			self.layer_maskChanged.emit(value)

	layer_mask = pyqtProperty(int, fget=getlayer_mask, fset=setlayer_mask, notify=layer_maskChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.material.extend(self._material)
		instance.glyph_bank.extend(self._glyph_bank)
		instance.font.extend(self._font)
		instance.size.extend(self._size)
		instance.antialias.extend(self._antialias)
		instance.shadow_x.extend(self._shadow_x)
		instance.shadow_y.extend(self._shadow_y)
		instance.shadow_blur.extend(self._shadow_blur)
		instance.shadow_alpha.extend(self._shadow_alpha)
		instance.alpha.extend(self._alpha)
		instance.outline_alpha.extend(self._outline_alpha)
		instance.outline_width.extend(self._outline_width)
		instance.layer_mask.extend(self._layer_mask)
		instance.output_format.extend(self._output_format)
		instance.render_mode.extend(self._render_mode)
		instance.all_chars.extend(self._all_chars)
		instance.characters.extend(self._characters)
		instance.cache_width.extend(self._cache_width)
		instance.cache_height.extend(self._cache_height)
		instance.sdf_spread.extend(self._sdf_spread)
		instance.sdf_outline.extend(self._sdf_outline)
		instance.sdf_shadow.extend(self._sdf_shadow)
		instance.padding.extend(self._padding)

	def getoutput_format(self) -> int :
		return self._output_format

	def setoutput_format(self,value : int) :
		if self._output_format != value:
			self._output_format = value
			self.output_formatChanged.emit(value)

	output_format = pyqtProperty(int, fget=getoutput_format, fset=setoutput_format, notify=output_formatChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.material.extend(self._material)
		instance.glyph_bank.extend(self._glyph_bank)
		instance.font.extend(self._font)
		instance.size.extend(self._size)
		instance.antialias.extend(self._antialias)
		instance.shadow_x.extend(self._shadow_x)
		instance.shadow_y.extend(self._shadow_y)
		instance.shadow_blur.extend(self._shadow_blur)
		instance.shadow_alpha.extend(self._shadow_alpha)
		instance.alpha.extend(self._alpha)
		instance.outline_alpha.extend(self._outline_alpha)
		instance.outline_width.extend(self._outline_width)
		instance.layer_mask.extend(self._layer_mask)
		instance.output_format.extend(self._output_format)
		instance.render_mode.extend(self._render_mode)
		instance.all_chars.extend(self._all_chars)
		instance.characters.extend(self._characters)
		instance.cache_width.extend(self._cache_width)
		instance.cache_height.extend(self._cache_height)
		instance.sdf_spread.extend(self._sdf_spread)
		instance.sdf_outline.extend(self._sdf_outline)
		instance.sdf_shadow.extend(self._sdf_shadow)
		instance.padding.extend(self._padding)

	def getrender_mode(self) -> int :
		return self._render_mode

	def setrender_mode(self,value : int) :
		if self._render_mode != value:
			self._render_mode = value
			self.render_modeChanged.emit(value)

	render_mode = pyqtProperty(int, fget=getrender_mode, fset=setrender_mode, notify=render_modeChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.material.extend(self._material)
		instance.glyph_bank.extend(self._glyph_bank)
		instance.font.extend(self._font)
		instance.size.extend(self._size)
		instance.antialias.extend(self._antialias)
		instance.shadow_x.extend(self._shadow_x)
		instance.shadow_y.extend(self._shadow_y)
		instance.shadow_blur.extend(self._shadow_blur)
		instance.shadow_alpha.extend(self._shadow_alpha)
		instance.alpha.extend(self._alpha)
		instance.outline_alpha.extend(self._outline_alpha)
		instance.outline_width.extend(self._outline_width)
		instance.layer_mask.extend(self._layer_mask)
		instance.output_format.extend(self._output_format)
		instance.render_mode.extend(self._render_mode)
		instance.all_chars.extend(self._all_chars)
		instance.characters.extend(self._characters)
		instance.cache_width.extend(self._cache_width)
		instance.cache_height.extend(self._cache_height)
		instance.sdf_spread.extend(self._sdf_spread)
		instance.sdf_outline.extend(self._sdf_outline)
		instance.sdf_shadow.extend(self._sdf_shadow)
		instance.padding.extend(self._padding)

	def getall_chars(self) -> bool :
		return self._all_chars

	def setall_chars(self,value : bool) :
		if self._all_chars != value:
			self._all_chars = value
			self.all_charsChanged.emit(value)

	all_chars = pyqtProperty(bool, fget=getall_chars, fset=setall_chars, notify=all_charsChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.material.extend(self._material)
		instance.glyph_bank.extend(self._glyph_bank)
		instance.font.extend(self._font)
		instance.size.extend(self._size)
		instance.antialias.extend(self._antialias)
		instance.shadow_x.extend(self._shadow_x)
		instance.shadow_y.extend(self._shadow_y)
		instance.shadow_blur.extend(self._shadow_blur)
		instance.shadow_alpha.extend(self._shadow_alpha)
		instance.alpha.extend(self._alpha)
		instance.outline_alpha.extend(self._outline_alpha)
		instance.outline_width.extend(self._outline_width)
		instance.layer_mask.extend(self._layer_mask)
		instance.output_format.extend(self._output_format)
		instance.render_mode.extend(self._render_mode)
		instance.all_chars.extend(self._all_chars)
		instance.characters.extend(self._characters)
		instance.cache_width.extend(self._cache_width)
		instance.cache_height.extend(self._cache_height)
		instance.sdf_spread.extend(self._sdf_spread)
		instance.sdf_outline.extend(self._sdf_outline)
		instance.sdf_shadow.extend(self._sdf_shadow)
		instance.padding.extend(self._padding)

	def getcharacters(self) -> str :
		return self._characters

	def setcharacters(self,value : str) :
		if self._characters != value:
			self._characters = value
			self.charactersChanged.emit(value)

	characters = pyqtProperty(str, fget=getcharacters, fset=setcharacters, notify=charactersChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.material.extend(self._material)
		instance.glyph_bank.extend(self._glyph_bank)
		instance.font.extend(self._font)
		instance.size.extend(self._size)
		instance.antialias.extend(self._antialias)
		instance.shadow_x.extend(self._shadow_x)
		instance.shadow_y.extend(self._shadow_y)
		instance.shadow_blur.extend(self._shadow_blur)
		instance.shadow_alpha.extend(self._shadow_alpha)
		instance.alpha.extend(self._alpha)
		instance.outline_alpha.extend(self._outline_alpha)
		instance.outline_width.extend(self._outline_width)
		instance.layer_mask.extend(self._layer_mask)
		instance.output_format.extend(self._output_format)
		instance.render_mode.extend(self._render_mode)
		instance.all_chars.extend(self._all_chars)
		instance.characters.extend(self._characters)
		instance.cache_width.extend(self._cache_width)
		instance.cache_height.extend(self._cache_height)
		instance.sdf_spread.extend(self._sdf_spread)
		instance.sdf_outline.extend(self._sdf_outline)
		instance.sdf_shadow.extend(self._sdf_shadow)
		instance.padding.extend(self._padding)

	def getcache_width(self) -> int :
		return self._cache_width

	def setcache_width(self,value : int) :
		if self._cache_width != value:
			self._cache_width = value
			self.cache_widthChanged.emit(value)

	cache_width = pyqtProperty(int, fget=getcache_width, fset=setcache_width, notify=cache_widthChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.material.extend(self._material)
		instance.glyph_bank.extend(self._glyph_bank)
		instance.font.extend(self._font)
		instance.size.extend(self._size)
		instance.antialias.extend(self._antialias)
		instance.shadow_x.extend(self._shadow_x)
		instance.shadow_y.extend(self._shadow_y)
		instance.shadow_blur.extend(self._shadow_blur)
		instance.shadow_alpha.extend(self._shadow_alpha)
		instance.alpha.extend(self._alpha)
		instance.outline_alpha.extend(self._outline_alpha)
		instance.outline_width.extend(self._outline_width)
		instance.layer_mask.extend(self._layer_mask)
		instance.output_format.extend(self._output_format)
		instance.render_mode.extend(self._render_mode)
		instance.all_chars.extend(self._all_chars)
		instance.characters.extend(self._characters)
		instance.cache_width.extend(self._cache_width)
		instance.cache_height.extend(self._cache_height)
		instance.sdf_spread.extend(self._sdf_spread)
		instance.sdf_outline.extend(self._sdf_outline)
		instance.sdf_shadow.extend(self._sdf_shadow)
		instance.padding.extend(self._padding)

	def getcache_height(self) -> int :
		return self._cache_height

	def setcache_height(self,value : int) :
		if self._cache_height != value:
			self._cache_height = value
			self.cache_heightChanged.emit(value)

	cache_height = pyqtProperty(int, fget=getcache_height, fset=setcache_height, notify=cache_heightChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.material.extend(self._material)
		instance.glyph_bank.extend(self._glyph_bank)
		instance.font.extend(self._font)
		instance.size.extend(self._size)
		instance.antialias.extend(self._antialias)
		instance.shadow_x.extend(self._shadow_x)
		instance.shadow_y.extend(self._shadow_y)
		instance.shadow_blur.extend(self._shadow_blur)
		instance.shadow_alpha.extend(self._shadow_alpha)
		instance.alpha.extend(self._alpha)
		instance.outline_alpha.extend(self._outline_alpha)
		instance.outline_width.extend(self._outline_width)
		instance.layer_mask.extend(self._layer_mask)
		instance.output_format.extend(self._output_format)
		instance.render_mode.extend(self._render_mode)
		instance.all_chars.extend(self._all_chars)
		instance.characters.extend(self._characters)
		instance.cache_width.extend(self._cache_width)
		instance.cache_height.extend(self._cache_height)
		instance.sdf_spread.extend(self._sdf_spread)
		instance.sdf_outline.extend(self._sdf_outline)
		instance.sdf_shadow.extend(self._sdf_shadow)
		instance.padding.extend(self._padding)

	def getsdf_spread(self) -> float :
		return self._sdf_spread

	def setsdf_spread(self,value : float) :
		if self._sdf_spread != value:
			self._sdf_spread = value
			self.sdf_spreadChanged.emit(value)

	sdf_spread = pyqtProperty(float, fget=getsdf_spread, fset=setsdf_spread, notify=sdf_spreadChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.material.extend(self._material)
		instance.glyph_bank.extend(self._glyph_bank)
		instance.font.extend(self._font)
		instance.size.extend(self._size)
		instance.antialias.extend(self._antialias)
		instance.shadow_x.extend(self._shadow_x)
		instance.shadow_y.extend(self._shadow_y)
		instance.shadow_blur.extend(self._shadow_blur)
		instance.shadow_alpha.extend(self._shadow_alpha)
		instance.alpha.extend(self._alpha)
		instance.outline_alpha.extend(self._outline_alpha)
		instance.outline_width.extend(self._outline_width)
		instance.layer_mask.extend(self._layer_mask)
		instance.output_format.extend(self._output_format)
		instance.render_mode.extend(self._render_mode)
		instance.all_chars.extend(self._all_chars)
		instance.characters.extend(self._characters)
		instance.cache_width.extend(self._cache_width)
		instance.cache_height.extend(self._cache_height)
		instance.sdf_spread.extend(self._sdf_spread)
		instance.sdf_outline.extend(self._sdf_outline)
		instance.sdf_shadow.extend(self._sdf_shadow)
		instance.padding.extend(self._padding)

	def getsdf_outline(self) -> float :
		return self._sdf_outline

	def setsdf_outline(self,value : float) :
		if self._sdf_outline != value:
			self._sdf_outline = value
			self.sdf_outlineChanged.emit(value)

	sdf_outline = pyqtProperty(float, fget=getsdf_outline, fset=setsdf_outline, notify=sdf_outlineChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.material.extend(self._material)
		instance.glyph_bank.extend(self._glyph_bank)
		instance.font.extend(self._font)
		instance.size.extend(self._size)
		instance.antialias.extend(self._antialias)
		instance.shadow_x.extend(self._shadow_x)
		instance.shadow_y.extend(self._shadow_y)
		instance.shadow_blur.extend(self._shadow_blur)
		instance.shadow_alpha.extend(self._shadow_alpha)
		instance.alpha.extend(self._alpha)
		instance.outline_alpha.extend(self._outline_alpha)
		instance.outline_width.extend(self._outline_width)
		instance.layer_mask.extend(self._layer_mask)
		instance.output_format.extend(self._output_format)
		instance.render_mode.extend(self._render_mode)
		instance.all_chars.extend(self._all_chars)
		instance.characters.extend(self._characters)
		instance.cache_width.extend(self._cache_width)
		instance.cache_height.extend(self._cache_height)
		instance.sdf_spread.extend(self._sdf_spread)
		instance.sdf_outline.extend(self._sdf_outline)
		instance.sdf_shadow.extend(self._sdf_shadow)
		instance.padding.extend(self._padding)

	def getsdf_shadow(self) -> float :
		return self._sdf_shadow

	def setsdf_shadow(self,value : float) :
		if self._sdf_shadow != value:
			self._sdf_shadow = value
			self.sdf_shadowChanged.emit(value)

	sdf_shadow = pyqtProperty(float, fget=getsdf_shadow, fset=setsdf_shadow, notify=sdf_shadowChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.material.extend(self._material)
		instance.glyph_bank.extend(self._glyph_bank)
		instance.font.extend(self._font)
		instance.size.extend(self._size)
		instance.antialias.extend(self._antialias)
		instance.shadow_x.extend(self._shadow_x)
		instance.shadow_y.extend(self._shadow_y)
		instance.shadow_blur.extend(self._shadow_blur)
		instance.shadow_alpha.extend(self._shadow_alpha)
		instance.alpha.extend(self._alpha)
		instance.outline_alpha.extend(self._outline_alpha)
		instance.outline_width.extend(self._outline_width)
		instance.layer_mask.extend(self._layer_mask)
		instance.output_format.extend(self._output_format)
		instance.render_mode.extend(self._render_mode)
		instance.all_chars.extend(self._all_chars)
		instance.characters.extend(self._characters)
		instance.cache_width.extend(self._cache_width)
		instance.cache_height.extend(self._cache_height)
		instance.sdf_spread.extend(self._sdf_spread)
		instance.sdf_outline.extend(self._sdf_outline)
		instance.sdf_shadow.extend(self._sdf_shadow)
		instance.padding.extend(self._padding)

	def getpadding(self) -> int :
		return self._padding

	def setpadding(self,value : int) :
		if self._padding != value:
			self._padding = value
			self.paddingChanged.emit(value)

	padding = pyqtProperty(int, fget=getpadding, fset=setpadding, notify=paddingChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.material.extend(self._material)
		instance.glyph_bank.extend(self._glyph_bank)
		instance.font.extend(self._font)
		instance.size.extend(self._size)
		instance.antialias.extend(self._antialias)
		instance.shadow_x.extend(self._shadow_x)
		instance.shadow_y.extend(self._shadow_y)
		instance.shadow_blur.extend(self._shadow_blur)
		instance.shadow_alpha.extend(self._shadow_alpha)
		instance.alpha.extend(self._alpha)
		instance.outline_alpha.extend(self._outline_alpha)
		instance.outline_width.extend(self._outline_width)
		instance.layer_mask.extend(self._layer_mask)
		instance.output_format.extend(self._output_format)
		instance.render_mode.extend(self._render_mode)
		instance.all_chars.extend(self._all_chars)
		instance.characters.extend(self._characters)
		instance.cache_width.extend(self._cache_width)
		instance.cache_height.extend(self._cache_height)
		instance.sdf_spread.extend(self._sdf_spread)
		instance.sdf_outline.extend(self._sdf_outline)
		instance.sdf_shadow.extend(self._sdf_shadow)
		instance.padding.extend(self._padding)

# ------- GlyphBank ------- #
class GlyphBank(QObject) :
	__PROTO__ = sdk.GlyphBank
	def __init__(self,glyphs :List[Glyph] = [],glyph_padding :int = int() ,glyph_channels :int = int() ,glyph_data :bytes = bytes() ,max_ascent :float = float() ,max_descent :float = float() ,max_advance :float = float() ,max_width :float = float() ,max_height :float = float() ,image_format :int = int() ,sdf_spread :float = float() ,sdf_outline :float = float() ,sdf_shadow :float = float() ,cache_width :int = int() ,cache_height :int = int() ,cache_cell_width :int = int() ,cache_cell_height :int = int() ,cache_cell_max_ascent :int = int() ,padding :int = int() ,is_monospaced :bool = bool() ) -> GlyphBank :
		self._glyphs = glyphs
		self._glyph_padding = glyph_padding
		self._glyph_channels = glyph_channels
		self._glyph_data = glyph_data
		self._max_ascent = max_ascent
		self._max_descent = max_descent
		self._max_advance = max_advance
		self._max_width = max_width
		self._max_height = max_height
		self._image_format = image_format
		self._sdf_spread = sdf_spread
		self._sdf_outline = sdf_outline
		self._sdf_shadow = sdf_shadow
		self._cache_width = cache_width
		self._cache_height = cache_height
		self._cache_cell_width = cache_cell_width
		self._cache_cell_height = cache_cell_height
		self._cache_cell_max_ascent = cache_cell_max_ascent
		self._padding = padding
		self._is_monospaced = is_monospaced
		pass
	def getglyphs(self) -> Glyph :
		return self._glyphs

	def setglyphs(self,value : List[Glyph]) :
		if self._glyphs != value:
			self._glyphs = value
			self.glyphsChanged.emit(value)

	glyphs = pyqtProperty(List, fget=getglyphs, fset=setglyphs, notify=glyphsChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.glyphs.extend([i.proto() for i in self._glyphs])
		instance.glyph_padding.extend(self._glyph_padding)
		instance.glyph_channels.extend(self._glyph_channels)
		instance.glyph_data.extend(self._glyph_data)
		instance.max_ascent.extend(self._max_ascent)
		instance.max_descent.extend(self._max_descent)
		instance.max_advance.extend(self._max_advance)
		instance.max_width.extend(self._max_width)
		instance.max_height.extend(self._max_height)
		instance.image_format.extend(self._image_format)
		instance.sdf_spread.extend(self._sdf_spread)
		instance.sdf_outline.extend(self._sdf_outline)
		instance.sdf_shadow.extend(self._sdf_shadow)
		instance.cache_width.extend(self._cache_width)
		instance.cache_height.extend(self._cache_height)
		instance.cache_cell_width.extend(self._cache_cell_width)
		instance.cache_cell_height.extend(self._cache_cell_height)
		instance.cache_cell_max_ascent.extend(self._cache_cell_max_ascent)
		instance.padding.extend(self._padding)
		instance.is_monospaced.extend(self._is_monospaced)

	def getglyph_padding(self) -> int :
		return self._glyph_padding

	def setglyph_padding(self,value : int) :
		if self._glyph_padding != value:
			self._glyph_padding = value
			self.glyph_paddingChanged.emit(value)

	glyph_padding = pyqtProperty(int, fget=getglyph_padding, fset=setglyph_padding, notify=glyph_paddingChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.glyphs.extend([i.proto() for i in self._glyphs])
		instance.glyph_padding.extend(self._glyph_padding)
		instance.glyph_channels.extend(self._glyph_channels)
		instance.glyph_data.extend(self._glyph_data)
		instance.max_ascent.extend(self._max_ascent)
		instance.max_descent.extend(self._max_descent)
		instance.max_advance.extend(self._max_advance)
		instance.max_width.extend(self._max_width)
		instance.max_height.extend(self._max_height)
		instance.image_format.extend(self._image_format)
		instance.sdf_spread.extend(self._sdf_spread)
		instance.sdf_outline.extend(self._sdf_outline)
		instance.sdf_shadow.extend(self._sdf_shadow)
		instance.cache_width.extend(self._cache_width)
		instance.cache_height.extend(self._cache_height)
		instance.cache_cell_width.extend(self._cache_cell_width)
		instance.cache_cell_height.extend(self._cache_cell_height)
		instance.cache_cell_max_ascent.extend(self._cache_cell_max_ascent)
		instance.padding.extend(self._padding)
		instance.is_monospaced.extend(self._is_monospaced)

	def getglyph_channels(self) -> int :
		return self._glyph_channels

	def setglyph_channels(self,value : int) :
		if self._glyph_channels != value:
			self._glyph_channels = value
			self.glyph_channelsChanged.emit(value)

	glyph_channels = pyqtProperty(int, fget=getglyph_channels, fset=setglyph_channels, notify=glyph_channelsChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.glyphs.extend([i.proto() for i in self._glyphs])
		instance.glyph_padding.extend(self._glyph_padding)
		instance.glyph_channels.extend(self._glyph_channels)
		instance.glyph_data.extend(self._glyph_data)
		instance.max_ascent.extend(self._max_ascent)
		instance.max_descent.extend(self._max_descent)
		instance.max_advance.extend(self._max_advance)
		instance.max_width.extend(self._max_width)
		instance.max_height.extend(self._max_height)
		instance.image_format.extend(self._image_format)
		instance.sdf_spread.extend(self._sdf_spread)
		instance.sdf_outline.extend(self._sdf_outline)
		instance.sdf_shadow.extend(self._sdf_shadow)
		instance.cache_width.extend(self._cache_width)
		instance.cache_height.extend(self._cache_height)
		instance.cache_cell_width.extend(self._cache_cell_width)
		instance.cache_cell_height.extend(self._cache_cell_height)
		instance.cache_cell_max_ascent.extend(self._cache_cell_max_ascent)
		instance.padding.extend(self._padding)
		instance.is_monospaced.extend(self._is_monospaced)

	def getglyph_data(self) -> bytes :
		return self._glyph_data

	def setglyph_data(self,value : bytes) :
		if self._glyph_data != value:
			self._glyph_data = value
			self.glyph_dataChanged.emit(value)

	glyph_data = pyqtProperty(bytes, fget=getglyph_data, fset=setglyph_data, notify=glyph_dataChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.glyphs.extend([i.proto() for i in self._glyphs])
		instance.glyph_padding.extend(self._glyph_padding)
		instance.glyph_channels.extend(self._glyph_channels)
		instance.glyph_data.extend(self._glyph_data)
		instance.max_ascent.extend(self._max_ascent)
		instance.max_descent.extend(self._max_descent)
		instance.max_advance.extend(self._max_advance)
		instance.max_width.extend(self._max_width)
		instance.max_height.extend(self._max_height)
		instance.image_format.extend(self._image_format)
		instance.sdf_spread.extend(self._sdf_spread)
		instance.sdf_outline.extend(self._sdf_outline)
		instance.sdf_shadow.extend(self._sdf_shadow)
		instance.cache_width.extend(self._cache_width)
		instance.cache_height.extend(self._cache_height)
		instance.cache_cell_width.extend(self._cache_cell_width)
		instance.cache_cell_height.extend(self._cache_cell_height)
		instance.cache_cell_max_ascent.extend(self._cache_cell_max_ascent)
		instance.padding.extend(self._padding)
		instance.is_monospaced.extend(self._is_monospaced)

	def getmax_ascent(self) -> float :
		return self._max_ascent

	def setmax_ascent(self,value : float) :
		if self._max_ascent != value:
			self._max_ascent = value
			self.max_ascentChanged.emit(value)

	max_ascent = pyqtProperty(float, fget=getmax_ascent, fset=setmax_ascent, notify=max_ascentChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.glyphs.extend([i.proto() for i in self._glyphs])
		instance.glyph_padding.extend(self._glyph_padding)
		instance.glyph_channels.extend(self._glyph_channels)
		instance.glyph_data.extend(self._glyph_data)
		instance.max_ascent.extend(self._max_ascent)
		instance.max_descent.extend(self._max_descent)
		instance.max_advance.extend(self._max_advance)
		instance.max_width.extend(self._max_width)
		instance.max_height.extend(self._max_height)
		instance.image_format.extend(self._image_format)
		instance.sdf_spread.extend(self._sdf_spread)
		instance.sdf_outline.extend(self._sdf_outline)
		instance.sdf_shadow.extend(self._sdf_shadow)
		instance.cache_width.extend(self._cache_width)
		instance.cache_height.extend(self._cache_height)
		instance.cache_cell_width.extend(self._cache_cell_width)
		instance.cache_cell_height.extend(self._cache_cell_height)
		instance.cache_cell_max_ascent.extend(self._cache_cell_max_ascent)
		instance.padding.extend(self._padding)
		instance.is_monospaced.extend(self._is_monospaced)

	def getmax_descent(self) -> float :
		return self._max_descent

	def setmax_descent(self,value : float) :
		if self._max_descent != value:
			self._max_descent = value
			self.max_descentChanged.emit(value)

	max_descent = pyqtProperty(float, fget=getmax_descent, fset=setmax_descent, notify=max_descentChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.glyphs.extend([i.proto() for i in self._glyphs])
		instance.glyph_padding.extend(self._glyph_padding)
		instance.glyph_channels.extend(self._glyph_channels)
		instance.glyph_data.extend(self._glyph_data)
		instance.max_ascent.extend(self._max_ascent)
		instance.max_descent.extend(self._max_descent)
		instance.max_advance.extend(self._max_advance)
		instance.max_width.extend(self._max_width)
		instance.max_height.extend(self._max_height)
		instance.image_format.extend(self._image_format)
		instance.sdf_spread.extend(self._sdf_spread)
		instance.sdf_outline.extend(self._sdf_outline)
		instance.sdf_shadow.extend(self._sdf_shadow)
		instance.cache_width.extend(self._cache_width)
		instance.cache_height.extend(self._cache_height)
		instance.cache_cell_width.extend(self._cache_cell_width)
		instance.cache_cell_height.extend(self._cache_cell_height)
		instance.cache_cell_max_ascent.extend(self._cache_cell_max_ascent)
		instance.padding.extend(self._padding)
		instance.is_monospaced.extend(self._is_monospaced)

	def getmax_advance(self) -> float :
		return self._max_advance

	def setmax_advance(self,value : float) :
		if self._max_advance != value:
			self._max_advance = value
			self.max_advanceChanged.emit(value)

	max_advance = pyqtProperty(float, fget=getmax_advance, fset=setmax_advance, notify=max_advanceChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.glyphs.extend([i.proto() for i in self._glyphs])
		instance.glyph_padding.extend(self._glyph_padding)
		instance.glyph_channels.extend(self._glyph_channels)
		instance.glyph_data.extend(self._glyph_data)
		instance.max_ascent.extend(self._max_ascent)
		instance.max_descent.extend(self._max_descent)
		instance.max_advance.extend(self._max_advance)
		instance.max_width.extend(self._max_width)
		instance.max_height.extend(self._max_height)
		instance.image_format.extend(self._image_format)
		instance.sdf_spread.extend(self._sdf_spread)
		instance.sdf_outline.extend(self._sdf_outline)
		instance.sdf_shadow.extend(self._sdf_shadow)
		instance.cache_width.extend(self._cache_width)
		instance.cache_height.extend(self._cache_height)
		instance.cache_cell_width.extend(self._cache_cell_width)
		instance.cache_cell_height.extend(self._cache_cell_height)
		instance.cache_cell_max_ascent.extend(self._cache_cell_max_ascent)
		instance.padding.extend(self._padding)
		instance.is_monospaced.extend(self._is_monospaced)

	def getmax_width(self) -> float :
		return self._max_width

	def setmax_width(self,value : float) :
		if self._max_width != value:
			self._max_width = value
			self.max_widthChanged.emit(value)

	max_width = pyqtProperty(float, fget=getmax_width, fset=setmax_width, notify=max_widthChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.glyphs.extend([i.proto() for i in self._glyphs])
		instance.glyph_padding.extend(self._glyph_padding)
		instance.glyph_channels.extend(self._glyph_channels)
		instance.glyph_data.extend(self._glyph_data)
		instance.max_ascent.extend(self._max_ascent)
		instance.max_descent.extend(self._max_descent)
		instance.max_advance.extend(self._max_advance)
		instance.max_width.extend(self._max_width)
		instance.max_height.extend(self._max_height)
		instance.image_format.extend(self._image_format)
		instance.sdf_spread.extend(self._sdf_spread)
		instance.sdf_outline.extend(self._sdf_outline)
		instance.sdf_shadow.extend(self._sdf_shadow)
		instance.cache_width.extend(self._cache_width)
		instance.cache_height.extend(self._cache_height)
		instance.cache_cell_width.extend(self._cache_cell_width)
		instance.cache_cell_height.extend(self._cache_cell_height)
		instance.cache_cell_max_ascent.extend(self._cache_cell_max_ascent)
		instance.padding.extend(self._padding)
		instance.is_monospaced.extend(self._is_monospaced)

	def getmax_height(self) -> float :
		return self._max_height

	def setmax_height(self,value : float) :
		if self._max_height != value:
			self._max_height = value
			self.max_heightChanged.emit(value)

	max_height = pyqtProperty(float, fget=getmax_height, fset=setmax_height, notify=max_heightChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.glyphs.extend([i.proto() for i in self._glyphs])
		instance.glyph_padding.extend(self._glyph_padding)
		instance.glyph_channels.extend(self._glyph_channels)
		instance.glyph_data.extend(self._glyph_data)
		instance.max_ascent.extend(self._max_ascent)
		instance.max_descent.extend(self._max_descent)
		instance.max_advance.extend(self._max_advance)
		instance.max_width.extend(self._max_width)
		instance.max_height.extend(self._max_height)
		instance.image_format.extend(self._image_format)
		instance.sdf_spread.extend(self._sdf_spread)
		instance.sdf_outline.extend(self._sdf_outline)
		instance.sdf_shadow.extend(self._sdf_shadow)
		instance.cache_width.extend(self._cache_width)
		instance.cache_height.extend(self._cache_height)
		instance.cache_cell_width.extend(self._cache_cell_width)
		instance.cache_cell_height.extend(self._cache_cell_height)
		instance.cache_cell_max_ascent.extend(self._cache_cell_max_ascent)
		instance.padding.extend(self._padding)
		instance.is_monospaced.extend(self._is_monospaced)

	def getimage_format(self) -> int :
		return self._image_format

	def setimage_format(self,value : int) :
		if self._image_format != value:
			self._image_format = value
			self.image_formatChanged.emit(value)

	image_format = pyqtProperty(int, fget=getimage_format, fset=setimage_format, notify=image_formatChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.glyphs.extend([i.proto() for i in self._glyphs])
		instance.glyph_padding.extend(self._glyph_padding)
		instance.glyph_channels.extend(self._glyph_channels)
		instance.glyph_data.extend(self._glyph_data)
		instance.max_ascent.extend(self._max_ascent)
		instance.max_descent.extend(self._max_descent)
		instance.max_advance.extend(self._max_advance)
		instance.max_width.extend(self._max_width)
		instance.max_height.extend(self._max_height)
		instance.image_format.extend(self._image_format)
		instance.sdf_spread.extend(self._sdf_spread)
		instance.sdf_outline.extend(self._sdf_outline)
		instance.sdf_shadow.extend(self._sdf_shadow)
		instance.cache_width.extend(self._cache_width)
		instance.cache_height.extend(self._cache_height)
		instance.cache_cell_width.extend(self._cache_cell_width)
		instance.cache_cell_height.extend(self._cache_cell_height)
		instance.cache_cell_max_ascent.extend(self._cache_cell_max_ascent)
		instance.padding.extend(self._padding)
		instance.is_monospaced.extend(self._is_monospaced)

	def getsdf_spread(self) -> float :
		return self._sdf_spread

	def setsdf_spread(self,value : float) :
		if self._sdf_spread != value:
			self._sdf_spread = value
			self.sdf_spreadChanged.emit(value)

	sdf_spread = pyqtProperty(float, fget=getsdf_spread, fset=setsdf_spread, notify=sdf_spreadChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.glyphs.extend([i.proto() for i in self._glyphs])
		instance.glyph_padding.extend(self._glyph_padding)
		instance.glyph_channels.extend(self._glyph_channels)
		instance.glyph_data.extend(self._glyph_data)
		instance.max_ascent.extend(self._max_ascent)
		instance.max_descent.extend(self._max_descent)
		instance.max_advance.extend(self._max_advance)
		instance.max_width.extend(self._max_width)
		instance.max_height.extend(self._max_height)
		instance.image_format.extend(self._image_format)
		instance.sdf_spread.extend(self._sdf_spread)
		instance.sdf_outline.extend(self._sdf_outline)
		instance.sdf_shadow.extend(self._sdf_shadow)
		instance.cache_width.extend(self._cache_width)
		instance.cache_height.extend(self._cache_height)
		instance.cache_cell_width.extend(self._cache_cell_width)
		instance.cache_cell_height.extend(self._cache_cell_height)
		instance.cache_cell_max_ascent.extend(self._cache_cell_max_ascent)
		instance.padding.extend(self._padding)
		instance.is_monospaced.extend(self._is_monospaced)

	def getsdf_outline(self) -> float :
		return self._sdf_outline

	def setsdf_outline(self,value : float) :
		if self._sdf_outline != value:
			self._sdf_outline = value
			self.sdf_outlineChanged.emit(value)

	sdf_outline = pyqtProperty(float, fget=getsdf_outline, fset=setsdf_outline, notify=sdf_outlineChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.glyphs.extend([i.proto() for i in self._glyphs])
		instance.glyph_padding.extend(self._glyph_padding)
		instance.glyph_channels.extend(self._glyph_channels)
		instance.glyph_data.extend(self._glyph_data)
		instance.max_ascent.extend(self._max_ascent)
		instance.max_descent.extend(self._max_descent)
		instance.max_advance.extend(self._max_advance)
		instance.max_width.extend(self._max_width)
		instance.max_height.extend(self._max_height)
		instance.image_format.extend(self._image_format)
		instance.sdf_spread.extend(self._sdf_spread)
		instance.sdf_outline.extend(self._sdf_outline)
		instance.sdf_shadow.extend(self._sdf_shadow)
		instance.cache_width.extend(self._cache_width)
		instance.cache_height.extend(self._cache_height)
		instance.cache_cell_width.extend(self._cache_cell_width)
		instance.cache_cell_height.extend(self._cache_cell_height)
		instance.cache_cell_max_ascent.extend(self._cache_cell_max_ascent)
		instance.padding.extend(self._padding)
		instance.is_monospaced.extend(self._is_monospaced)

	def getsdf_shadow(self) -> float :
		return self._sdf_shadow

	def setsdf_shadow(self,value : float) :
		if self._sdf_shadow != value:
			self._sdf_shadow = value
			self.sdf_shadowChanged.emit(value)

	sdf_shadow = pyqtProperty(float, fget=getsdf_shadow, fset=setsdf_shadow, notify=sdf_shadowChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.glyphs.extend([i.proto() for i in self._glyphs])
		instance.glyph_padding.extend(self._glyph_padding)
		instance.glyph_channels.extend(self._glyph_channels)
		instance.glyph_data.extend(self._glyph_data)
		instance.max_ascent.extend(self._max_ascent)
		instance.max_descent.extend(self._max_descent)
		instance.max_advance.extend(self._max_advance)
		instance.max_width.extend(self._max_width)
		instance.max_height.extend(self._max_height)
		instance.image_format.extend(self._image_format)
		instance.sdf_spread.extend(self._sdf_spread)
		instance.sdf_outline.extend(self._sdf_outline)
		instance.sdf_shadow.extend(self._sdf_shadow)
		instance.cache_width.extend(self._cache_width)
		instance.cache_height.extend(self._cache_height)
		instance.cache_cell_width.extend(self._cache_cell_width)
		instance.cache_cell_height.extend(self._cache_cell_height)
		instance.cache_cell_max_ascent.extend(self._cache_cell_max_ascent)
		instance.padding.extend(self._padding)
		instance.is_monospaced.extend(self._is_monospaced)

	def getcache_width(self) -> int :
		return self._cache_width

	def setcache_width(self,value : int) :
		if self._cache_width != value:
			self._cache_width = value
			self.cache_widthChanged.emit(value)

	cache_width = pyqtProperty(int, fget=getcache_width, fset=setcache_width, notify=cache_widthChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.glyphs.extend([i.proto() for i in self._glyphs])
		instance.glyph_padding.extend(self._glyph_padding)
		instance.glyph_channels.extend(self._glyph_channels)
		instance.glyph_data.extend(self._glyph_data)
		instance.max_ascent.extend(self._max_ascent)
		instance.max_descent.extend(self._max_descent)
		instance.max_advance.extend(self._max_advance)
		instance.max_width.extend(self._max_width)
		instance.max_height.extend(self._max_height)
		instance.image_format.extend(self._image_format)
		instance.sdf_spread.extend(self._sdf_spread)
		instance.sdf_outline.extend(self._sdf_outline)
		instance.sdf_shadow.extend(self._sdf_shadow)
		instance.cache_width.extend(self._cache_width)
		instance.cache_height.extend(self._cache_height)
		instance.cache_cell_width.extend(self._cache_cell_width)
		instance.cache_cell_height.extend(self._cache_cell_height)
		instance.cache_cell_max_ascent.extend(self._cache_cell_max_ascent)
		instance.padding.extend(self._padding)
		instance.is_monospaced.extend(self._is_monospaced)

	def getcache_height(self) -> int :
		return self._cache_height

	def setcache_height(self,value : int) :
		if self._cache_height != value:
			self._cache_height = value
			self.cache_heightChanged.emit(value)

	cache_height = pyqtProperty(int, fget=getcache_height, fset=setcache_height, notify=cache_heightChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.glyphs.extend([i.proto() for i in self._glyphs])
		instance.glyph_padding.extend(self._glyph_padding)
		instance.glyph_channels.extend(self._glyph_channels)
		instance.glyph_data.extend(self._glyph_data)
		instance.max_ascent.extend(self._max_ascent)
		instance.max_descent.extend(self._max_descent)
		instance.max_advance.extend(self._max_advance)
		instance.max_width.extend(self._max_width)
		instance.max_height.extend(self._max_height)
		instance.image_format.extend(self._image_format)
		instance.sdf_spread.extend(self._sdf_spread)
		instance.sdf_outline.extend(self._sdf_outline)
		instance.sdf_shadow.extend(self._sdf_shadow)
		instance.cache_width.extend(self._cache_width)
		instance.cache_height.extend(self._cache_height)
		instance.cache_cell_width.extend(self._cache_cell_width)
		instance.cache_cell_height.extend(self._cache_cell_height)
		instance.cache_cell_max_ascent.extend(self._cache_cell_max_ascent)
		instance.padding.extend(self._padding)
		instance.is_monospaced.extend(self._is_monospaced)

	def getcache_cell_width(self) -> int :
		return self._cache_cell_width

	def setcache_cell_width(self,value : int) :
		if self._cache_cell_width != value:
			self._cache_cell_width = value
			self.cache_cell_widthChanged.emit(value)

	cache_cell_width = pyqtProperty(int, fget=getcache_cell_width, fset=setcache_cell_width, notify=cache_cell_widthChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.glyphs.extend([i.proto() for i in self._glyphs])
		instance.glyph_padding.extend(self._glyph_padding)
		instance.glyph_channels.extend(self._glyph_channels)
		instance.glyph_data.extend(self._glyph_data)
		instance.max_ascent.extend(self._max_ascent)
		instance.max_descent.extend(self._max_descent)
		instance.max_advance.extend(self._max_advance)
		instance.max_width.extend(self._max_width)
		instance.max_height.extend(self._max_height)
		instance.image_format.extend(self._image_format)
		instance.sdf_spread.extend(self._sdf_spread)
		instance.sdf_outline.extend(self._sdf_outline)
		instance.sdf_shadow.extend(self._sdf_shadow)
		instance.cache_width.extend(self._cache_width)
		instance.cache_height.extend(self._cache_height)
		instance.cache_cell_width.extend(self._cache_cell_width)
		instance.cache_cell_height.extend(self._cache_cell_height)
		instance.cache_cell_max_ascent.extend(self._cache_cell_max_ascent)
		instance.padding.extend(self._padding)
		instance.is_monospaced.extend(self._is_monospaced)

	def getcache_cell_height(self) -> int :
		return self._cache_cell_height

	def setcache_cell_height(self,value : int) :
		if self._cache_cell_height != value:
			self._cache_cell_height = value
			self.cache_cell_heightChanged.emit(value)

	cache_cell_height = pyqtProperty(int, fget=getcache_cell_height, fset=setcache_cell_height, notify=cache_cell_heightChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.glyphs.extend([i.proto() for i in self._glyphs])
		instance.glyph_padding.extend(self._glyph_padding)
		instance.glyph_channels.extend(self._glyph_channels)
		instance.glyph_data.extend(self._glyph_data)
		instance.max_ascent.extend(self._max_ascent)
		instance.max_descent.extend(self._max_descent)
		instance.max_advance.extend(self._max_advance)
		instance.max_width.extend(self._max_width)
		instance.max_height.extend(self._max_height)
		instance.image_format.extend(self._image_format)
		instance.sdf_spread.extend(self._sdf_spread)
		instance.sdf_outline.extend(self._sdf_outline)
		instance.sdf_shadow.extend(self._sdf_shadow)
		instance.cache_width.extend(self._cache_width)
		instance.cache_height.extend(self._cache_height)
		instance.cache_cell_width.extend(self._cache_cell_width)
		instance.cache_cell_height.extend(self._cache_cell_height)
		instance.cache_cell_max_ascent.extend(self._cache_cell_max_ascent)
		instance.padding.extend(self._padding)
		instance.is_monospaced.extend(self._is_monospaced)

	def getcache_cell_max_ascent(self) -> int :
		return self._cache_cell_max_ascent

	def setcache_cell_max_ascent(self,value : int) :
		if self._cache_cell_max_ascent != value:
			self._cache_cell_max_ascent = value
			self.cache_cell_max_ascentChanged.emit(value)

	cache_cell_max_ascent = pyqtProperty(int, fget=getcache_cell_max_ascent, fset=setcache_cell_max_ascent, notify=cache_cell_max_ascentChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.glyphs.extend([i.proto() for i in self._glyphs])
		instance.glyph_padding.extend(self._glyph_padding)
		instance.glyph_channels.extend(self._glyph_channels)
		instance.glyph_data.extend(self._glyph_data)
		instance.max_ascent.extend(self._max_ascent)
		instance.max_descent.extend(self._max_descent)
		instance.max_advance.extend(self._max_advance)
		instance.max_width.extend(self._max_width)
		instance.max_height.extend(self._max_height)
		instance.image_format.extend(self._image_format)
		instance.sdf_spread.extend(self._sdf_spread)
		instance.sdf_outline.extend(self._sdf_outline)
		instance.sdf_shadow.extend(self._sdf_shadow)
		instance.cache_width.extend(self._cache_width)
		instance.cache_height.extend(self._cache_height)
		instance.cache_cell_width.extend(self._cache_cell_width)
		instance.cache_cell_height.extend(self._cache_cell_height)
		instance.cache_cell_max_ascent.extend(self._cache_cell_max_ascent)
		instance.padding.extend(self._padding)
		instance.is_monospaced.extend(self._is_monospaced)

	def getpadding(self) -> int :
		return self._padding

	def setpadding(self,value : int) :
		if self._padding != value:
			self._padding = value
			self.paddingChanged.emit(value)

	padding = pyqtProperty(int, fget=getpadding, fset=setpadding, notify=paddingChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.glyphs.extend([i.proto() for i in self._glyphs])
		instance.glyph_padding.extend(self._glyph_padding)
		instance.glyph_channels.extend(self._glyph_channels)
		instance.glyph_data.extend(self._glyph_data)
		instance.max_ascent.extend(self._max_ascent)
		instance.max_descent.extend(self._max_descent)
		instance.max_advance.extend(self._max_advance)
		instance.max_width.extend(self._max_width)
		instance.max_height.extend(self._max_height)
		instance.image_format.extend(self._image_format)
		instance.sdf_spread.extend(self._sdf_spread)
		instance.sdf_outline.extend(self._sdf_outline)
		instance.sdf_shadow.extend(self._sdf_shadow)
		instance.cache_width.extend(self._cache_width)
		instance.cache_height.extend(self._cache_height)
		instance.cache_cell_width.extend(self._cache_cell_width)
		instance.cache_cell_height.extend(self._cache_cell_height)
		instance.cache_cell_max_ascent.extend(self._cache_cell_max_ascent)
		instance.padding.extend(self._padding)
		instance.is_monospaced.extend(self._is_monospaced)

	def getis_monospaced(self) -> bool :
		return self._is_monospaced

	def setis_monospaced(self,value : bool) :
		if self._is_monospaced != value:
			self._is_monospaced = value
			self.is_monospacedChanged.emit(value)

	is_monospaced = pyqtProperty(bool, fget=getis_monospaced, fset=setis_monospaced, notify=is_monospacedChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.glyphs.extend([i.proto() for i in self._glyphs])
		instance.glyph_padding.extend(self._glyph_padding)
		instance.glyph_channels.extend(self._glyph_channels)
		instance.glyph_data.extend(self._glyph_data)
		instance.max_ascent.extend(self._max_ascent)
		instance.max_descent.extend(self._max_descent)
		instance.max_advance.extend(self._max_advance)
		instance.max_width.extend(self._max_width)
		instance.max_height.extend(self._max_height)
		instance.image_format.extend(self._image_format)
		instance.sdf_spread.extend(self._sdf_spread)
		instance.sdf_outline.extend(self._sdf_outline)
		instance.sdf_shadow.extend(self._sdf_shadow)
		instance.cache_width.extend(self._cache_width)
		instance.cache_height.extend(self._cache_height)
		instance.cache_cell_width.extend(self._cache_cell_width)
		instance.cache_cell_height.extend(self._cache_cell_height)
		instance.cache_cell_max_ascent.extend(self._cache_cell_max_ascent)
		instance.padding.extend(self._padding)
		instance.is_monospaced.extend(self._is_monospaced)

# ------- HashDigest ------- #
class HashDigest(QObject) :
	__PROTO__ = sdk.HashDigest
	def __init__(self,data :bytes = bytes() ) -> HashDigest :
		self._data = data
		pass
	def getdata(self) -> bytes :
		return self._data

	def setdata(self,value : bytes) :
		if self._data != value:
			self._data = value
			self.dataChanged.emit(value)

	data = pyqtProperty(bytes, fget=getdata, fset=setdata, notify=dataChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.data.extend(self._data)

# ------- HideApp ------- #
class HideApp(QObject) :
	__PROTO__ = sdk.HideApp
	def __init__(self) -> HideApp :
		pass
# ------- InstanceDesc ------- #
class InstanceDesc(QObject) :
	__PROTO__ = sdk.InstanceDesc
	def __init__(self,id :str = str() ,prototype :str = str() ,children :List[str] = [] ,position :Point3 = None ,rotation :Quat = None ,component_properties :List[ComponentPropertyDesc] = [],scale :float = float() ,scale3 :Vector3One = None ) -> InstanceDesc :
		self._id = id
		self._prototype = prototype
		self._children = children
		self._position = position
		self._rotation = rotation
		self._component_properties = component_properties
		self._scale = scale
		self._scale3 = scale3
		pass
	def getid(self) -> str :
		return self._id

	def setid(self,value : str) :
		if self._id != value:
			self._id = value
			self.idChanged.emit(value)

	id = pyqtProperty(str, fget=getid, fset=setid, notify=idChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.id.extend(self._id)
		instance.prototype.extend(self._prototype)
		instance.children = self._children
		instance.position = self._position.proto()
		instance.rotation = self._rotation.proto()
		instance.component_properties.extend([i.proto() for i in self._component_properties])
		instance.scale.extend(self._scale)
		instance.scale3 = self._scale3.proto()

	def getprototype(self) -> str :
		return self._prototype

	def setprototype(self,value : str) :
		if self._prototype != value:
			self._prototype = value
			self.prototypeChanged.emit(value)

	prototype = pyqtProperty(str, fget=getprototype, fset=setprototype, notify=prototypeChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.id.extend(self._id)
		instance.prototype.extend(self._prototype)
		instance.children = self._children
		instance.position = self._position.proto()
		instance.rotation = self._rotation.proto()
		instance.component_properties.extend([i.proto() for i in self._component_properties])
		instance.scale.extend(self._scale)
		instance.scale3 = self._scale3.proto()

	def getchildren(self) -> str :
		return self._children

	def setchildren(self,value : List[str]) :
		if self._children != value:
			self._children = value
			self.childrenChanged.emit(value)

	children = pyqtProperty(List, fget=getchildren, fset=setchildren, notify=childrenChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.id.extend(self._id)
		instance.prototype.extend(self._prototype)
		instance.children = self._children
		instance.position = self._position.proto()
		instance.rotation = self._rotation.proto()
		instance.component_properties.extend([i.proto() for i in self._component_properties])
		instance.scale.extend(self._scale)
		instance.scale3 = self._scale3.proto()

	def getposition(self) -> Point3 :
		return self._position

	def setposition(self,value : Point3) :
		if self._position != value:
			self._position = value
			self.positionChanged.emit(value)

	position = pyqtProperty(QObject, fget=getposition, fset=setposition, notify=positionChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.id.extend(self._id)
		instance.prototype.extend(self._prototype)
		instance.children = self._children
		instance.position = self._position.proto()
		instance.rotation = self._rotation.proto()
		instance.component_properties.extend([i.proto() for i in self._component_properties])
		instance.scale.extend(self._scale)
		instance.scale3 = self._scale3.proto()

	def getrotation(self) -> Quat :
		return self._rotation

	def setrotation(self,value : Quat) :
		if self._rotation != value:
			self._rotation = value
			self.rotationChanged.emit(value)

	rotation = pyqtProperty(QObject, fget=getrotation, fset=setrotation, notify=rotationChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.id.extend(self._id)
		instance.prototype.extend(self._prototype)
		instance.children = self._children
		instance.position = self._position.proto()
		instance.rotation = self._rotation.proto()
		instance.component_properties.extend([i.proto() for i in self._component_properties])
		instance.scale.extend(self._scale)
		instance.scale3 = self._scale3.proto()

	def getcomponent_properties(self) -> ComponentPropertyDesc :
		return self._component_properties

	def setcomponent_properties(self,value : List[ComponentPropertyDesc]) :
		if self._component_properties != value:
			self._component_properties = value
			self.component_propertiesChanged.emit(value)

	component_properties = pyqtProperty(List, fget=getcomponent_properties, fset=setcomponent_properties, notify=component_propertiesChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.id.extend(self._id)
		instance.prototype.extend(self._prototype)
		instance.children = self._children
		instance.position = self._position.proto()
		instance.rotation = self._rotation.proto()
		instance.component_properties.extend([i.proto() for i in self._component_properties])
		instance.scale.extend(self._scale)
		instance.scale3 = self._scale3.proto()

	def getscale(self) -> float :
		return self._scale

	def setscale(self,value : float) :
		if self._scale != value:
			self._scale = value
			self.scaleChanged.emit(value)

	scale = pyqtProperty(float, fget=getscale, fset=setscale, notify=scaleChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.id.extend(self._id)
		instance.prototype.extend(self._prototype)
		instance.children = self._children
		instance.position = self._position.proto()
		instance.rotation = self._rotation.proto()
		instance.component_properties.extend([i.proto() for i in self._component_properties])
		instance.scale.extend(self._scale)
		instance.scale3 = self._scale3.proto()

	def getscale3(self) -> Vector3One :
		return self._scale3

	def setscale3(self,value : Vector3One) :
		if self._scale3 != value:
			self._scale3 = value
			self.scale3Changed.emit(value)

	scale3 = pyqtProperty(QObject, fget=getscale3, fset=setscale3, notify=scale3Changed)

	def proto(self) :
		instance = self.__PROTO__()
		instance.id.extend(self._id)
		instance.prototype.extend(self._prototype)
		instance.children = self._children
		instance.position = self._position.proto()
		instance.rotation = self._rotation.proto()
		instance.component_properties.extend([i.proto() for i in self._component_properties])
		instance.scale.extend(self._scale)
		instance.scale3 = self._scale3.proto()

# ------- InstancePropertyDesc ------- #
class InstancePropertyDesc(QObject) :
	__PROTO__ = sdk.InstancePropertyDesc
	def __init__(self,id :str = str() ,properties :List[ComponentPropertyDesc] = []) -> InstancePropertyDesc :
		self._id = id
		self._properties = properties
		pass
	def getid(self) -> str :
		return self._id

	def setid(self,value : str) :
		if self._id != value:
			self._id = value
			self.idChanged.emit(value)

	id = pyqtProperty(str, fget=getid, fset=setid, notify=idChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.id.extend(self._id)
		instance.properties.extend([i.proto() for i in self._properties])

	def getproperties(self) -> ComponentPropertyDesc :
		return self._properties

	def setproperties(self,value : List[ComponentPropertyDesc]) :
		if self._properties != value:
			self._properties = value
			self.propertiesChanged.emit(value)

	properties = pyqtProperty(List, fget=getproperties, fset=setproperties, notify=propertiesChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.id.extend(self._id)
		instance.properties.extend([i.proto() for i in self._properties])

# ------- LabelDesc ------- #
class BlendMode(Enum):
	BLEND_MODE_ALPHA = 0
	BLEND_MODE_ADD = 1
	BLEND_MODE_MULT = 3
	BLEND_MODE_SCREEN = 4
class Pivot(Enum):
	PIVOT_CENTER = 0
	PIVOT_N = 1
	PIVOT_NE = 2
	PIVOT_E = 3
	PIVOT_SE = 4
	PIVOT_S = 5
	PIVOT_SW = 6
	PIVOT_W = 7
	PIVOT_NW = 8
class LabelDesc(QObject) :
	__PROTO__ = sdk.LabelDesc
	def __init__(self,size :Vector4 = None ,scale :Vector4One = None ,color :Vector4One = None ,outline :Vector4WOne = None ,shadow :Vector4WOne = None ,leading :float = float() ,tracking :float = float() ,pivot :int = int() ,blend_mode :int = int() ,line_break :bool = bool() ,text :str = str() ,font :str = str() ,material :str = str() ) -> LabelDesc :
		self._size = size
		self._scale = scale
		self._color = color
		self._outline = outline
		self._shadow = shadow
		self._leading = leading
		self._tracking = tracking
		self._pivot = pivot
		self._blend_mode = blend_mode
		self._line_break = line_break
		self._text = text
		self._font = font
		self._material = material
		pass
	def getsize(self) -> Vector4 :
		return self._size

	def setsize(self,value : Vector4) :
		if self._size != value:
			self._size = value
			self.sizeChanged.emit(value)

	size = pyqtProperty(QObject, fget=getsize, fset=setsize, notify=sizeChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.size = self._size.proto()
		instance.scale = self._scale.proto()
		instance.color = self._color.proto()
		instance.outline = self._outline.proto()
		instance.shadow = self._shadow.proto()
		instance.leading.extend(self._leading)
		instance.tracking.extend(self._tracking)
		instance.pivot.extend(self._pivot)
		instance.blend_mode.extend(self._blend_mode)
		instance.line_break.extend(self._line_break)
		instance.text.extend(self._text)
		instance.font.extend(self._font)
		instance.material.extend(self._material)

	def getscale(self) -> Vector4One :
		return self._scale

	def setscale(self,value : Vector4One) :
		if self._scale != value:
			self._scale = value
			self.scaleChanged.emit(value)

	scale = pyqtProperty(QObject, fget=getscale, fset=setscale, notify=scaleChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.size = self._size.proto()
		instance.scale = self._scale.proto()
		instance.color = self._color.proto()
		instance.outline = self._outline.proto()
		instance.shadow = self._shadow.proto()
		instance.leading.extend(self._leading)
		instance.tracking.extend(self._tracking)
		instance.pivot.extend(self._pivot)
		instance.blend_mode.extend(self._blend_mode)
		instance.line_break.extend(self._line_break)
		instance.text.extend(self._text)
		instance.font.extend(self._font)
		instance.material.extend(self._material)

	def getcolor(self) -> Vector4One :
		return self._color

	def setcolor(self,value : Vector4One) :
		if self._color != value:
			self._color = value
			self.colorChanged.emit(value)

	color = pyqtProperty(QObject, fget=getcolor, fset=setcolor, notify=colorChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.size = self._size.proto()
		instance.scale = self._scale.proto()
		instance.color = self._color.proto()
		instance.outline = self._outline.proto()
		instance.shadow = self._shadow.proto()
		instance.leading.extend(self._leading)
		instance.tracking.extend(self._tracking)
		instance.pivot.extend(self._pivot)
		instance.blend_mode.extend(self._blend_mode)
		instance.line_break.extend(self._line_break)
		instance.text.extend(self._text)
		instance.font.extend(self._font)
		instance.material.extend(self._material)

	def getoutline(self) -> Vector4WOne :
		return self._outline

	def setoutline(self,value : Vector4WOne) :
		if self._outline != value:
			self._outline = value
			self.outlineChanged.emit(value)

	outline = pyqtProperty(QObject, fget=getoutline, fset=setoutline, notify=outlineChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.size = self._size.proto()
		instance.scale = self._scale.proto()
		instance.color = self._color.proto()
		instance.outline = self._outline.proto()
		instance.shadow = self._shadow.proto()
		instance.leading.extend(self._leading)
		instance.tracking.extend(self._tracking)
		instance.pivot.extend(self._pivot)
		instance.blend_mode.extend(self._blend_mode)
		instance.line_break.extend(self._line_break)
		instance.text.extend(self._text)
		instance.font.extend(self._font)
		instance.material.extend(self._material)

	def getshadow(self) -> Vector4WOne :
		return self._shadow

	def setshadow(self,value : Vector4WOne) :
		if self._shadow != value:
			self._shadow = value
			self.shadowChanged.emit(value)

	shadow = pyqtProperty(QObject, fget=getshadow, fset=setshadow, notify=shadowChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.size = self._size.proto()
		instance.scale = self._scale.proto()
		instance.color = self._color.proto()
		instance.outline = self._outline.proto()
		instance.shadow = self._shadow.proto()
		instance.leading.extend(self._leading)
		instance.tracking.extend(self._tracking)
		instance.pivot.extend(self._pivot)
		instance.blend_mode.extend(self._blend_mode)
		instance.line_break.extend(self._line_break)
		instance.text.extend(self._text)
		instance.font.extend(self._font)
		instance.material.extend(self._material)

	def getleading(self) -> float :
		return self._leading

	def setleading(self,value : float) :
		if self._leading != value:
			self._leading = value
			self.leadingChanged.emit(value)

	leading = pyqtProperty(float, fget=getleading, fset=setleading, notify=leadingChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.size = self._size.proto()
		instance.scale = self._scale.proto()
		instance.color = self._color.proto()
		instance.outline = self._outline.proto()
		instance.shadow = self._shadow.proto()
		instance.leading.extend(self._leading)
		instance.tracking.extend(self._tracking)
		instance.pivot.extend(self._pivot)
		instance.blend_mode.extend(self._blend_mode)
		instance.line_break.extend(self._line_break)
		instance.text.extend(self._text)
		instance.font.extend(self._font)
		instance.material.extend(self._material)

	def gettracking(self) -> float :
		return self._tracking

	def settracking(self,value : float) :
		if self._tracking != value:
			self._tracking = value
			self.trackingChanged.emit(value)

	tracking = pyqtProperty(float, fget=gettracking, fset=settracking, notify=trackingChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.size = self._size.proto()
		instance.scale = self._scale.proto()
		instance.color = self._color.proto()
		instance.outline = self._outline.proto()
		instance.shadow = self._shadow.proto()
		instance.leading.extend(self._leading)
		instance.tracking.extend(self._tracking)
		instance.pivot.extend(self._pivot)
		instance.blend_mode.extend(self._blend_mode)
		instance.line_break.extend(self._line_break)
		instance.text.extend(self._text)
		instance.font.extend(self._font)
		instance.material.extend(self._material)

	def getpivot(self) -> int :
		return self._pivot

	def setpivot(self,value : int) :
		if self._pivot != value:
			self._pivot = value
			self.pivotChanged.emit(value)

	pivot = pyqtProperty(int, fget=getpivot, fset=setpivot, notify=pivotChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.size = self._size.proto()
		instance.scale = self._scale.proto()
		instance.color = self._color.proto()
		instance.outline = self._outline.proto()
		instance.shadow = self._shadow.proto()
		instance.leading.extend(self._leading)
		instance.tracking.extend(self._tracking)
		instance.pivot.extend(self._pivot)
		instance.blend_mode.extend(self._blend_mode)
		instance.line_break.extend(self._line_break)
		instance.text.extend(self._text)
		instance.font.extend(self._font)
		instance.material.extend(self._material)

	def getblend_mode(self) -> int :
		return self._blend_mode

	def setblend_mode(self,value : int) :
		if self._blend_mode != value:
			self._blend_mode = value
			self.blend_modeChanged.emit(value)

	blend_mode = pyqtProperty(int, fget=getblend_mode, fset=setblend_mode, notify=blend_modeChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.size = self._size.proto()
		instance.scale = self._scale.proto()
		instance.color = self._color.proto()
		instance.outline = self._outline.proto()
		instance.shadow = self._shadow.proto()
		instance.leading.extend(self._leading)
		instance.tracking.extend(self._tracking)
		instance.pivot.extend(self._pivot)
		instance.blend_mode.extend(self._blend_mode)
		instance.line_break.extend(self._line_break)
		instance.text.extend(self._text)
		instance.font.extend(self._font)
		instance.material.extend(self._material)

	def getline_break(self) -> bool :
		return self._line_break

	def setline_break(self,value : bool) :
		if self._line_break != value:
			self._line_break = value
			self.line_breakChanged.emit(value)

	line_break = pyqtProperty(bool, fget=getline_break, fset=setline_break, notify=line_breakChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.size = self._size.proto()
		instance.scale = self._scale.proto()
		instance.color = self._color.proto()
		instance.outline = self._outline.proto()
		instance.shadow = self._shadow.proto()
		instance.leading.extend(self._leading)
		instance.tracking.extend(self._tracking)
		instance.pivot.extend(self._pivot)
		instance.blend_mode.extend(self._blend_mode)
		instance.line_break.extend(self._line_break)
		instance.text.extend(self._text)
		instance.font.extend(self._font)
		instance.material.extend(self._material)

	def gettext(self) -> str :
		return self._text

	def settext(self,value : str) :
		if self._text != value:
			self._text = value
			self.textChanged.emit(value)

	text = pyqtProperty(str, fget=gettext, fset=settext, notify=textChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.size = self._size.proto()
		instance.scale = self._scale.proto()
		instance.color = self._color.proto()
		instance.outline = self._outline.proto()
		instance.shadow = self._shadow.proto()
		instance.leading.extend(self._leading)
		instance.tracking.extend(self._tracking)
		instance.pivot.extend(self._pivot)
		instance.blend_mode.extend(self._blend_mode)
		instance.line_break.extend(self._line_break)
		instance.text.extend(self._text)
		instance.font.extend(self._font)
		instance.material.extend(self._material)

	def getfont(self) -> str :
		return self._font

	def setfont(self,value : str) :
		if self._font != value:
			self._font = value
			self.fontChanged.emit(value)

	font = pyqtProperty(str, fget=getfont, fset=setfont, notify=fontChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.size = self._size.proto()
		instance.scale = self._scale.proto()
		instance.color = self._color.proto()
		instance.outline = self._outline.proto()
		instance.shadow = self._shadow.proto()
		instance.leading.extend(self._leading)
		instance.tracking.extend(self._tracking)
		instance.pivot.extend(self._pivot)
		instance.blend_mode.extend(self._blend_mode)
		instance.line_break.extend(self._line_break)
		instance.text.extend(self._text)
		instance.font.extend(self._font)
		instance.material.extend(self._material)

	def getmaterial(self) -> str :
		return self._material

	def setmaterial(self,value : str) :
		if self._material != value:
			self._material = value
			self.materialChanged.emit(value)

	material = pyqtProperty(str, fget=getmaterial, fset=setmaterial, notify=materialChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.size = self._size.proto()
		instance.scale = self._scale.proto()
		instance.color = self._color.proto()
		instance.outline = self._outline.proto()
		instance.shadow = self._shadow.proto()
		instance.leading.extend(self._leading)
		instance.tracking.extend(self._tracking)
		instance.pivot.extend(self._pivot)
		instance.blend_mode.extend(self._blend_mode)
		instance.line_break.extend(self._line_break)
		instance.text.extend(self._text)
		instance.font.extend(self._font)
		instance.material.extend(self._material)

# ------- LayoutChanged ------- #
class LayoutChanged(QObject) :
	__PROTO__ = sdk.LayoutChanged
	def __init__(self,id :int = int() ,previous_id :int = int() ) -> LayoutChanged :
		self._id = id
		self._previous_id = previous_id
		pass
	def getid(self) -> int :
		return self._id

	def setid(self,value : int) :
		if self._id != value:
			self._id = value
			self.idChanged.emit(value)

	id = pyqtProperty(int, fget=getid, fset=setid, notify=idChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.id.extend(self._id)
		instance.previous_id.extend(self._previous_id)

	def getprevious_id(self) -> int :
		return self._previous_id

	def setprevious_id(self,value : int) :
		if self._previous_id != value:
			self._previous_id = value
			self.previous_idChanged.emit(value)

	previous_id = pyqtProperty(int, fget=getprevious_id, fset=setprevious_id, notify=previous_idChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.id.extend(self._id)
		instance.previous_id.extend(self._previous_id)

# ------- LightDesc ------- #
class LightDesc(QObject) :
	__PROTO__ = sdk.LightDesc
	def __init__(self,id :str = str() ,type :int = int() ,intensity :float = float() ,color :Vector3 = None ,range :float = float() ,decay :float = float() ,cone_angle :float = float() ,penumbra_angle :float = float() ,drop_off :float = float() ) -> LightDesc :
		self._id = id
		self._type = type
		self._intensity = intensity
		self._color = color
		self._range = range
		self._decay = decay
		self._cone_angle = cone_angle
		self._penumbra_angle = penumbra_angle
		self._drop_off = drop_off
		pass
	def getid(self) -> str :
		return self._id

	def setid(self,value : str) :
		if self._id != value:
			self._id = value
			self.idChanged.emit(value)

	id = pyqtProperty(str, fget=getid, fset=setid, notify=idChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.id.extend(self._id)
		instance.type.extend(self._type)
		instance.intensity.extend(self._intensity)
		instance.color = self._color.proto()
		instance.range.extend(self._range)
		instance.decay.extend(self._decay)
		instance.cone_angle.extend(self._cone_angle)
		instance.penumbra_angle.extend(self._penumbra_angle)
		instance.drop_off.extend(self._drop_off)

	def gettype(self) -> int :
		return self._type

	def settype(self,value : int) :
		if self._type != value:
			self._type = value
			self.typeChanged.emit(value)

	type = pyqtProperty(int, fget=gettype, fset=settype, notify=typeChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.id.extend(self._id)
		instance.type.extend(self._type)
		instance.intensity.extend(self._intensity)
		instance.color = self._color.proto()
		instance.range.extend(self._range)
		instance.decay.extend(self._decay)
		instance.cone_angle.extend(self._cone_angle)
		instance.penumbra_angle.extend(self._penumbra_angle)
		instance.drop_off.extend(self._drop_off)

	def getintensity(self) -> float :
		return self._intensity

	def setintensity(self,value : float) :
		if self._intensity != value:
			self._intensity = value
			self.intensityChanged.emit(value)

	intensity = pyqtProperty(float, fget=getintensity, fset=setintensity, notify=intensityChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.id.extend(self._id)
		instance.type.extend(self._type)
		instance.intensity.extend(self._intensity)
		instance.color = self._color.proto()
		instance.range.extend(self._range)
		instance.decay.extend(self._decay)
		instance.cone_angle.extend(self._cone_angle)
		instance.penumbra_angle.extend(self._penumbra_angle)
		instance.drop_off.extend(self._drop_off)

	def getcolor(self) -> Vector3 :
		return self._color

	def setcolor(self,value : Vector3) :
		if self._color != value:
			self._color = value
			self.colorChanged.emit(value)

	color = pyqtProperty(QObject, fget=getcolor, fset=setcolor, notify=colorChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.id.extend(self._id)
		instance.type.extend(self._type)
		instance.intensity.extend(self._intensity)
		instance.color = self._color.proto()
		instance.range.extend(self._range)
		instance.decay.extend(self._decay)
		instance.cone_angle.extend(self._cone_angle)
		instance.penumbra_angle.extend(self._penumbra_angle)
		instance.drop_off.extend(self._drop_off)

	def getrange(self) -> float :
		return self._range

	def setrange(self,value : float) :
		if self._range != value:
			self._range = value
			self.rangeChanged.emit(value)

	range = pyqtProperty(float, fget=getrange, fset=setrange, notify=rangeChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.id.extend(self._id)
		instance.type.extend(self._type)
		instance.intensity.extend(self._intensity)
		instance.color = self._color.proto()
		instance.range.extend(self._range)
		instance.decay.extend(self._decay)
		instance.cone_angle.extend(self._cone_angle)
		instance.penumbra_angle.extend(self._penumbra_angle)
		instance.drop_off.extend(self._drop_off)

	def getdecay(self) -> float :
		return self._decay

	def setdecay(self,value : float) :
		if self._decay != value:
			self._decay = value
			self.decayChanged.emit(value)

	decay = pyqtProperty(float, fget=getdecay, fset=setdecay, notify=decayChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.id.extend(self._id)
		instance.type.extend(self._type)
		instance.intensity.extend(self._intensity)
		instance.color = self._color.proto()
		instance.range.extend(self._range)
		instance.decay.extend(self._decay)
		instance.cone_angle.extend(self._cone_angle)
		instance.penumbra_angle.extend(self._penumbra_angle)
		instance.drop_off.extend(self._drop_off)

	def getcone_angle(self) -> float :
		return self._cone_angle

	def setcone_angle(self,value : float) :
		if self._cone_angle != value:
			self._cone_angle = value
			self.cone_angleChanged.emit(value)

	cone_angle = pyqtProperty(float, fget=getcone_angle, fset=setcone_angle, notify=cone_angleChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.id.extend(self._id)
		instance.type.extend(self._type)
		instance.intensity.extend(self._intensity)
		instance.color = self._color.proto()
		instance.range.extend(self._range)
		instance.decay.extend(self._decay)
		instance.cone_angle.extend(self._cone_angle)
		instance.penumbra_angle.extend(self._penumbra_angle)
		instance.drop_off.extend(self._drop_off)

	def getpenumbra_angle(self) -> float :
		return self._penumbra_angle

	def setpenumbra_angle(self,value : float) :
		if self._penumbra_angle != value:
			self._penumbra_angle = value
			self.penumbra_angleChanged.emit(value)

	penumbra_angle = pyqtProperty(float, fget=getpenumbra_angle, fset=setpenumbra_angle, notify=penumbra_angleChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.id.extend(self._id)
		instance.type.extend(self._type)
		instance.intensity.extend(self._intensity)
		instance.color = self._color.proto()
		instance.range.extend(self._range)
		instance.decay.extend(self._decay)
		instance.cone_angle.extend(self._cone_angle)
		instance.penumbra_angle.extend(self._penumbra_angle)
		instance.drop_off.extend(self._drop_off)

	def getdrop_off(self) -> float :
		return self._drop_off

	def setdrop_off(self,value : float) :
		if self._drop_off != value:
			self._drop_off = value
			self.drop_offChanged.emit(value)

	drop_off = pyqtProperty(float, fget=getdrop_off, fset=setdrop_off, notify=drop_offChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.id.extend(self._id)
		instance.type.extend(self._type)
		instance.intensity.extend(self._intensity)
		instance.color = self._color.proto()
		instance.range.extend(self._range)
		instance.decay.extend(self._decay)
		instance.cone_angle.extend(self._cone_angle)
		instance.penumbra_angle.extend(self._penumbra_angle)
		instance.drop_off.extend(self._drop_off)

# ------- LuaModule ------- #
class LuaModule(QObject) :
	__PROTO__ = sdk.LuaModule
	def __init__(self,source :LuaSource = None ,modules :List[str] = [] ,resources :List[str] = [] ,properties :PropertyDeclarations = None ,property_resources :List[str] = [] ) -> LuaModule :
		self._source = source
		self._modules = modules
		self._resources = resources
		self._properties = properties
		self._property_resources = property_resources
		pass
	def getsource(self) -> LuaSource :
		return self._source

	def setsource(self,value : LuaSource) :
		if self._source != value:
			self._source = value
			self.sourceChanged.emit(value)

	source = pyqtProperty(QObject, fget=getsource, fset=setsource, notify=sourceChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.source = self._source.proto()
		instance.modules = self._modules
		instance.resources = self._resources
		instance.properties = self._properties.proto()
		instance.property_resources = self._property_resources

	def getmodules(self) -> str :
		return self._modules

	def setmodules(self,value : List[str]) :
		if self._modules != value:
			self._modules = value
			self.modulesChanged.emit(value)

	modules = pyqtProperty(List, fget=getmodules, fset=setmodules, notify=modulesChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.source = self._source.proto()
		instance.modules = self._modules
		instance.resources = self._resources
		instance.properties = self._properties.proto()
		instance.property_resources = self._property_resources

	def getresources(self) -> str :
		return self._resources

	def setresources(self,value : List[str]) :
		if self._resources != value:
			self._resources = value
			self.resourcesChanged.emit(value)

	resources = pyqtProperty(List, fget=getresources, fset=setresources, notify=resourcesChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.source = self._source.proto()
		instance.modules = self._modules
		instance.resources = self._resources
		instance.properties = self._properties.proto()
		instance.property_resources = self._property_resources

	def getproperties(self) -> PropertyDeclarations :
		return self._properties

	def setproperties(self,value : PropertyDeclarations) :
		if self._properties != value:
			self._properties = value
			self.propertiesChanged.emit(value)

	properties = pyqtProperty(QObject, fget=getproperties, fset=setproperties, notify=propertiesChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.source = self._source.proto()
		instance.modules = self._modules
		instance.resources = self._resources
		instance.properties = self._properties.proto()
		instance.property_resources = self._property_resources

	def getproperty_resources(self) -> str :
		return self._property_resources

	def setproperty_resources(self,value : List[str]) :
		if self._property_resources != value:
			self._property_resources = value
			self.property_resourcesChanged.emit(value)

	property_resources = pyqtProperty(List, fget=getproperty_resources, fset=setproperty_resources, notify=property_resourcesChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.source = self._source.proto()
		instance.modules = self._modules
		instance.resources = self._resources
		instance.properties = self._properties.proto()
		instance.property_resources = self._property_resources

# ------- LuaRef ------- #
class LuaRef(QObject) :
	__PROTO__ = sdk.LuaRef
	def __init__(self,ref :int = int() ,context_table_ref :int = int() ) -> LuaRef :
		self._ref = ref
		self._context_table_ref = context_table_ref
		pass
	def getref(self) -> int :
		return self._ref

	def setref(self,value : int) :
		if self._ref != value:
			self._ref = value
			self.refChanged.emit(value)

	ref = pyqtProperty(int, fget=getref, fset=setref, notify=refChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.ref.extend(self._ref)
		instance.context_table_ref.extend(self._context_table_ref)

	def getcontext_table_ref(self) -> int :
		return self._context_table_ref

	def setcontext_table_ref(self,value : int) :
		if self._context_table_ref != value:
			self._context_table_ref = value
			self.context_table_refChanged.emit(value)

	context_table_ref = pyqtProperty(int, fget=getcontext_table_ref, fset=setcontext_table_ref, notify=context_table_refChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.ref.extend(self._ref)
		instance.context_table_ref.extend(self._context_table_ref)

# ------- LuaSource ------- #
class LuaSource(QObject) :
	__PROTO__ = sdk.LuaSource
	def __init__(self,script :bytes = bytes() ,filename :str = str() ,bytecode :bytes = bytes() ,delta :bytes = bytes() ,bytecode_32 :bytes = bytes() ,bytecode_64 :bytes = bytes() ) -> LuaSource :
		self._script = script
		self._filename = filename
		self._bytecode = bytecode
		self._delta = delta
		self._bytecode_32 = bytecode_32
		self._bytecode_64 = bytecode_64
		pass
	def getscript(self) -> bytes :
		return self._script

	def setscript(self,value : bytes) :
		if self._script != value:
			self._script = value
			self.scriptChanged.emit(value)

	script = pyqtProperty(bytes, fget=getscript, fset=setscript, notify=scriptChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.script.extend(self._script)
		instance.filename.extend(self._filename)
		instance.bytecode.extend(self._bytecode)
		instance.delta.extend(self._delta)
		instance.bytecode_32.extend(self._bytecode_32)
		instance.bytecode_64.extend(self._bytecode_64)

	def getfilename(self) -> str :
		return self._filename

	def setfilename(self,value : str) :
		if self._filename != value:
			self._filename = value
			self.filenameChanged.emit(value)

	filename = pyqtProperty(str, fget=getfilename, fset=setfilename, notify=filenameChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.script.extend(self._script)
		instance.filename.extend(self._filename)
		instance.bytecode.extend(self._bytecode)
		instance.delta.extend(self._delta)
		instance.bytecode_32.extend(self._bytecode_32)
		instance.bytecode_64.extend(self._bytecode_64)

	def getbytecode(self) -> bytes :
		return self._bytecode

	def setbytecode(self,value : bytes) :
		if self._bytecode != value:
			self._bytecode = value
			self.bytecodeChanged.emit(value)

	bytecode = pyqtProperty(bytes, fget=getbytecode, fset=setbytecode, notify=bytecodeChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.script.extend(self._script)
		instance.filename.extend(self._filename)
		instance.bytecode.extend(self._bytecode)
		instance.delta.extend(self._delta)
		instance.bytecode_32.extend(self._bytecode_32)
		instance.bytecode_64.extend(self._bytecode_64)

	def getdelta(self) -> bytes :
		return self._delta

	def setdelta(self,value : bytes) :
		if self._delta != value:
			self._delta = value
			self.deltaChanged.emit(value)

	delta = pyqtProperty(bytes, fget=getdelta, fset=setdelta, notify=deltaChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.script.extend(self._script)
		instance.filename.extend(self._filename)
		instance.bytecode.extend(self._bytecode)
		instance.delta.extend(self._delta)
		instance.bytecode_32.extend(self._bytecode_32)
		instance.bytecode_64.extend(self._bytecode_64)

	def getbytecode_32(self) -> bytes :
		return self._bytecode_32

	def setbytecode_32(self,value : bytes) :
		if self._bytecode_32 != value:
			self._bytecode_32 = value
			self.bytecode_32Changed.emit(value)

	bytecode_32 = pyqtProperty(bytes, fget=getbytecode_32, fset=setbytecode_32, notify=bytecode_32Changed)

	def proto(self) :
		instance = self.__PROTO__()
		instance.script.extend(self._script)
		instance.filename.extend(self._filename)
		instance.bytecode.extend(self._bytecode)
		instance.delta.extend(self._delta)
		instance.bytecode_32.extend(self._bytecode_32)
		instance.bytecode_64.extend(self._bytecode_64)

	def getbytecode_64(self) -> bytes :
		return self._bytecode_64

	def setbytecode_64(self,value : bytes) :
		if self._bytecode_64 != value:
			self._bytecode_64 = value
			self.bytecode_64Changed.emit(value)

	bytecode_64 = pyqtProperty(bytes, fget=getbytecode_64, fset=setbytecode_64, notify=bytecode_64Changed)

	def proto(self) :
		instance = self.__PROTO__()
		instance.script.extend(self._script)
		instance.filename.extend(self._filename)
		instance.bytecode.extend(self._bytecode)
		instance.delta.extend(self._delta)
		instance.bytecode_32.extend(self._bytecode_32)
		instance.bytecode_64.extend(self._bytecode_64)

# ------- ManifestData ------- #
class ManifestData(QObject) :
	__PROTO__ = sdk.ManifestData
	def __init__(self,header :ManifestHeader = None ,engine_versions :List[HashDigest] = [],resources :List[ResourceEntry] = []) -> ManifestData :
		self._header = header
		self._engine_versions = engine_versions
		self._resources = resources
		pass
	def getheader(self) -> ManifestHeader :
		return self._header

	def setheader(self,value : ManifestHeader) :
		if self._header != value:
			self._header = value
			self.headerChanged.emit(value)

	header = pyqtProperty(QObject, fget=getheader, fset=setheader, notify=headerChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.header = self._header.proto()
		instance.engine_versions.extend([i.proto() for i in self._engine_versions])
		instance.resources.extend([i.proto() for i in self._resources])

	def getengine_versions(self) -> HashDigest :
		return self._engine_versions

	def setengine_versions(self,value : List[HashDigest]) :
		if self._engine_versions != value:
			self._engine_versions = value
			self.engine_versionsChanged.emit(value)

	engine_versions = pyqtProperty(List, fget=getengine_versions, fset=setengine_versions, notify=engine_versionsChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.header = self._header.proto()
		instance.engine_versions.extend([i.proto() for i in self._engine_versions])
		instance.resources.extend([i.proto() for i in self._resources])

	def getresources(self) -> ResourceEntry :
		return self._resources

	def setresources(self,value : List[ResourceEntry]) :
		if self._resources != value:
			self._resources = value
			self.resourcesChanged.emit(value)

	resources = pyqtProperty(List, fget=getresources, fset=setresources, notify=resourcesChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.header = self._header.proto()
		instance.engine_versions.extend([i.proto() for i in self._engine_versions])
		instance.resources.extend([i.proto() for i in self._resources])

# ------- ManifestFile ------- #
class ManifestFile(QObject) :
	__PROTO__ = sdk.ManifestFile
	def __init__(self,data :bytes = bytes() ,signature :bytes = bytes() ,archive_identifier :bytes = bytes() ,version :int = int() ) -> ManifestFile :
		self._data = data
		self._signature = signature
		self._archive_identifier = archive_identifier
		self._version = version
		pass
	def getdata(self) -> bytes :
		return self._data

	def setdata(self,value : bytes) :
		if self._data != value:
			self._data = value
			self.dataChanged.emit(value)

	data = pyqtProperty(bytes, fget=getdata, fset=setdata, notify=dataChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.data.extend(self._data)
		instance.signature.extend(self._signature)
		instance.archive_identifier.extend(self._archive_identifier)
		instance.version.extend(self._version)

	def getsignature(self) -> bytes :
		return self._signature

	def setsignature(self,value : bytes) :
		if self._signature != value:
			self._signature = value
			self.signatureChanged.emit(value)

	signature = pyqtProperty(bytes, fget=getsignature, fset=setsignature, notify=signatureChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.data.extend(self._data)
		instance.signature.extend(self._signature)
		instance.archive_identifier.extend(self._archive_identifier)
		instance.version.extend(self._version)

	def getarchive_identifier(self) -> bytes :
		return self._archive_identifier

	def setarchive_identifier(self,value : bytes) :
		if self._archive_identifier != value:
			self._archive_identifier = value
			self.archive_identifierChanged.emit(value)

	archive_identifier = pyqtProperty(bytes, fget=getarchive_identifier, fset=setarchive_identifier, notify=archive_identifierChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.data.extend(self._data)
		instance.signature.extend(self._signature)
		instance.archive_identifier.extend(self._archive_identifier)
		instance.version.extend(self._version)

	def getversion(self) -> int :
		return self._version

	def setversion(self,value : int) :
		if self._version != value:
			self._version = value
			self.versionChanged.emit(value)

	version = pyqtProperty(int, fget=getversion, fset=setversion, notify=versionChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.data.extend(self._data)
		instance.signature.extend(self._signature)
		instance.archive_identifier.extend(self._archive_identifier)
		instance.version.extend(self._version)

# ------- ManifestHeader ------- #
class ManifestHeader(QObject) :
	__PROTO__ = sdk.ManifestHeader
	def __init__(self,resource_hash_algorithm :int = int() ,signature_hash_algorithm :int = int() ,signature_sign_algorithm :int = int() ,project_identifier :HashDigest = None ) -> ManifestHeader :
		self._resource_hash_algorithm = resource_hash_algorithm
		self._signature_hash_algorithm = signature_hash_algorithm
		self._signature_sign_algorithm = signature_sign_algorithm
		self._project_identifier = project_identifier
		pass
	def getresource_hash_algorithm(self) -> int :
		return self._resource_hash_algorithm

	def setresource_hash_algorithm(self,value : int) :
		if self._resource_hash_algorithm != value:
			self._resource_hash_algorithm = value
			self.resource_hash_algorithmChanged.emit(value)

	resource_hash_algorithm = pyqtProperty(int, fget=getresource_hash_algorithm, fset=setresource_hash_algorithm, notify=resource_hash_algorithmChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.resource_hash_algorithm.extend(self._resource_hash_algorithm)
		instance.signature_hash_algorithm.extend(self._signature_hash_algorithm)
		instance.signature_sign_algorithm.extend(self._signature_sign_algorithm)
		instance.project_identifier = self._project_identifier.proto()

	def getsignature_hash_algorithm(self) -> int :
		return self._signature_hash_algorithm

	def setsignature_hash_algorithm(self,value : int) :
		if self._signature_hash_algorithm != value:
			self._signature_hash_algorithm = value
			self.signature_hash_algorithmChanged.emit(value)

	signature_hash_algorithm = pyqtProperty(int, fget=getsignature_hash_algorithm, fset=setsignature_hash_algorithm, notify=signature_hash_algorithmChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.resource_hash_algorithm.extend(self._resource_hash_algorithm)
		instance.signature_hash_algorithm.extend(self._signature_hash_algorithm)
		instance.signature_sign_algorithm.extend(self._signature_sign_algorithm)
		instance.project_identifier = self._project_identifier.proto()

	def getsignature_sign_algorithm(self) -> int :
		return self._signature_sign_algorithm

	def setsignature_sign_algorithm(self,value : int) :
		if self._signature_sign_algorithm != value:
			self._signature_sign_algorithm = value
			self.signature_sign_algorithmChanged.emit(value)

	signature_sign_algorithm = pyqtProperty(int, fget=getsignature_sign_algorithm, fset=setsignature_sign_algorithm, notify=signature_sign_algorithmChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.resource_hash_algorithm.extend(self._resource_hash_algorithm)
		instance.signature_hash_algorithm.extend(self._signature_hash_algorithm)
		instance.signature_sign_algorithm.extend(self._signature_sign_algorithm)
		instance.project_identifier = self._project_identifier.proto()

	def getproject_identifier(self) -> HashDigest :
		return self._project_identifier

	def setproject_identifier(self,value : HashDigest) :
		if self._project_identifier != value:
			self._project_identifier = value
			self.project_identifierChanged.emit(value)

	project_identifier = pyqtProperty(QObject, fget=getproject_identifier, fset=setproject_identifier, notify=project_identifierChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.resource_hash_algorithm.extend(self._resource_hash_algorithm)
		instance.signature_hash_algorithm.extend(self._signature_hash_algorithm)
		instance.signature_sign_algorithm.extend(self._signature_sign_algorithm)
		instance.project_identifier = self._project_identifier.proto()

# ------- Material ------- #
class Material(QObject) :
	__PROTO__ = sdk.Material
	def __init__(self,name :str = str() ,material :str = str() ,textures :List[Texture] = [],attributes :List[VertexAttribute] = []) -> Material :
		self._name = name
		self._material = material
		self._textures = textures
		self._attributes = attributes
		pass
	def getname(self) -> str :
		return self._name

	def setname(self,value : str) :
		if self._name != value:
			self._name = value
			self.nameChanged.emit(value)

	name = pyqtProperty(str, fget=getname, fset=setname, notify=nameChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.name.extend(self._name)
		instance.material.extend(self._material)
		instance.textures.extend([i.proto() for i in self._textures])
		instance.attributes.extend([i.proto() for i in self._attributes])

	def getmaterial(self) -> str :
		return self._material

	def setmaterial(self,value : str) :
		if self._material != value:
			self._material = value
			self.materialChanged.emit(value)

	material = pyqtProperty(str, fget=getmaterial, fset=setmaterial, notify=materialChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.name.extend(self._name)
		instance.material.extend(self._material)
		instance.textures.extend([i.proto() for i in self._textures])
		instance.attributes.extend([i.proto() for i in self._attributes])

	def gettextures(self) -> Texture :
		return self._textures

	def settextures(self,value : List[Texture]) :
		if self._textures != value:
			self._textures = value
			self.texturesChanged.emit(value)

	textures = pyqtProperty(List, fget=gettextures, fset=settextures, notify=texturesChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.name.extend(self._name)
		instance.material.extend(self._material)
		instance.textures.extend([i.proto() for i in self._textures])
		instance.attributes.extend([i.proto() for i in self._attributes])

	def getattributes(self) -> VertexAttribute :
		return self._attributes

	def setattributes(self,value : List[VertexAttribute]) :
		if self._attributes != value:
			self._attributes = value
			self.attributesChanged.emit(value)

	attributes = pyqtProperty(List, fget=getattributes, fset=setattributes, notify=attributesChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.name.extend(self._name)
		instance.material.extend(self._material)
		instance.textures.extend([i.proto() for i in self._textures])
		instance.attributes.extend([i.proto() for i in self._attributes])

# ------- MaterialDesc ------- #
class ConstantType(Enum):
	CONSTANT_TYPE_USER = 0
	CONSTANT_TYPE_VIEWPROJ = 1
	CONSTANT_TYPE_WORLD = 2
	CONSTANT_TYPE_TEXTURE = 3
	CONSTANT_TYPE_VIEW = 4
	CONSTANT_TYPE_PROJECTION = 5
	CONSTANT_TYPE_NORMAL = 6
	CONSTANT_TYPE_WORLDVIEW = 7
	CONSTANT_TYPE_WORLDVIEWPROJ = 8
	CONSTANT_TYPE_USER_MATRIX4 = 9
class VertexSpace(Enum):
	VERTEX_SPACE_WORLD = 0
	VERTEX_SPACE_LOCAL = 1
class WrapMode(Enum):
	WRAP_MODE_REPEAT = 0
	WRAP_MODE_MIRRORED_REPEAT = 1
	WRAP_MODE_CLAMP_TO_EDGE = 2
class FilterModeMin(Enum):
	FILTER_MODE_MIN_NEAREST = 0
	FILTER_MODE_MIN_LINEAR = 1
	FILTER_MODE_MIN_NEAREST_MIPMAP_NEAREST = 2
	FILTER_MODE_MIN_NEAREST_MIPMAP_LINEAR = 3
	FILTER_MODE_MIN_LINEAR_MIPMAP_NEAREST = 4
	FILTER_MODE_MIN_LINEAR_MIPMAP_LINEAR = 5
	FILTER_MODE_MIN_DEFAULT = 6
class FilterModeMag(Enum):
	FILTER_MODE_MAG_NEAREST = 0
	FILTER_MODE_MAG_LINEAR = 1
	FILTER_MODE_MAG_DEFAULT = 2
class MaterialDesc(QObject) :
	__PROTO__ = sdk.MaterialDesc
	def __init__(self,name :str = str() ,tags :List[str] = [] ,vertex_program :str = str() ,fragment_program :str = str() ,vertex_space :int = int() ,vertex_constants :List[Constant] = [],fragment_constants :List[Constant] = [],textures :List[str] = [] ,samplers :List[Sampler] = [],max_page_count :int = int() ,attributes :List[VertexAttribute] = [],program :str = str() ,pbr_parameters :PbrParameters = None ) -> MaterialDesc :
		self._name = name
		self._tags = tags
		self._vertex_program = vertex_program
		self._fragment_program = fragment_program
		self._vertex_space = vertex_space
		self._vertex_constants = vertex_constants
		self._fragment_constants = fragment_constants
		self._textures = textures
		self._samplers = samplers
		self._max_page_count = max_page_count
		self._attributes = attributes
		self._program = program
		self._pbr_parameters = pbr_parameters
		pass
	def getname(self) -> str :
		return self._name

	def setname(self,value : str) :
		if self._name != value:
			self._name = value
			self.nameChanged.emit(value)

	name = pyqtProperty(str, fget=getname, fset=setname, notify=nameChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.name.extend(self._name)
		instance.tags = self._tags
		instance.vertex_program.extend(self._vertex_program)
		instance.fragment_program.extend(self._fragment_program)
		instance.vertex_space.extend(self._vertex_space)
		instance.vertex_constants.extend([i.proto() for i in self._vertex_constants])
		instance.fragment_constants.extend([i.proto() for i in self._fragment_constants])
		instance.textures = self._textures
		instance.samplers.extend([i.proto() for i in self._samplers])
		instance.max_page_count.extend(self._max_page_count)
		instance.attributes.extend([i.proto() for i in self._attributes])
		instance.program.extend(self._program)
		instance.pbr_parameters = self._pbr_parameters.proto()

	def gettags(self) -> str :
		return self._tags

	def settags(self,value : List[str]) :
		if self._tags != value:
			self._tags = value
			self.tagsChanged.emit(value)

	tags = pyqtProperty(List, fget=gettags, fset=settags, notify=tagsChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.name.extend(self._name)
		instance.tags = self._tags
		instance.vertex_program.extend(self._vertex_program)
		instance.fragment_program.extend(self._fragment_program)
		instance.vertex_space.extend(self._vertex_space)
		instance.vertex_constants.extend([i.proto() for i in self._vertex_constants])
		instance.fragment_constants.extend([i.proto() for i in self._fragment_constants])
		instance.textures = self._textures
		instance.samplers.extend([i.proto() for i in self._samplers])
		instance.max_page_count.extend(self._max_page_count)
		instance.attributes.extend([i.proto() for i in self._attributes])
		instance.program.extend(self._program)
		instance.pbr_parameters = self._pbr_parameters.proto()

	def getvertex_program(self) -> str :
		return self._vertex_program

	def setvertex_program(self,value : str) :
		if self._vertex_program != value:
			self._vertex_program = value
			self.vertex_programChanged.emit(value)

	vertex_program = pyqtProperty(str, fget=getvertex_program, fset=setvertex_program, notify=vertex_programChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.name.extend(self._name)
		instance.tags = self._tags
		instance.vertex_program.extend(self._vertex_program)
		instance.fragment_program.extend(self._fragment_program)
		instance.vertex_space.extend(self._vertex_space)
		instance.vertex_constants.extend([i.proto() for i in self._vertex_constants])
		instance.fragment_constants.extend([i.proto() for i in self._fragment_constants])
		instance.textures = self._textures
		instance.samplers.extend([i.proto() for i in self._samplers])
		instance.max_page_count.extend(self._max_page_count)
		instance.attributes.extend([i.proto() for i in self._attributes])
		instance.program.extend(self._program)
		instance.pbr_parameters = self._pbr_parameters.proto()

	def getfragment_program(self) -> str :
		return self._fragment_program

	def setfragment_program(self,value : str) :
		if self._fragment_program != value:
			self._fragment_program = value
			self.fragment_programChanged.emit(value)

	fragment_program = pyqtProperty(str, fget=getfragment_program, fset=setfragment_program, notify=fragment_programChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.name.extend(self._name)
		instance.tags = self._tags
		instance.vertex_program.extend(self._vertex_program)
		instance.fragment_program.extend(self._fragment_program)
		instance.vertex_space.extend(self._vertex_space)
		instance.vertex_constants.extend([i.proto() for i in self._vertex_constants])
		instance.fragment_constants.extend([i.proto() for i in self._fragment_constants])
		instance.textures = self._textures
		instance.samplers.extend([i.proto() for i in self._samplers])
		instance.max_page_count.extend(self._max_page_count)
		instance.attributes.extend([i.proto() for i in self._attributes])
		instance.program.extend(self._program)
		instance.pbr_parameters = self._pbr_parameters.proto()

	def getvertex_space(self) -> int :
		return self._vertex_space

	def setvertex_space(self,value : int) :
		if self._vertex_space != value:
			self._vertex_space = value
			self.vertex_spaceChanged.emit(value)

	vertex_space = pyqtProperty(int, fget=getvertex_space, fset=setvertex_space, notify=vertex_spaceChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.name.extend(self._name)
		instance.tags = self._tags
		instance.vertex_program.extend(self._vertex_program)
		instance.fragment_program.extend(self._fragment_program)
		instance.vertex_space.extend(self._vertex_space)
		instance.vertex_constants.extend([i.proto() for i in self._vertex_constants])
		instance.fragment_constants.extend([i.proto() for i in self._fragment_constants])
		instance.textures = self._textures
		instance.samplers.extend([i.proto() for i in self._samplers])
		instance.max_page_count.extend(self._max_page_count)
		instance.attributes.extend([i.proto() for i in self._attributes])
		instance.program.extend(self._program)
		instance.pbr_parameters = self._pbr_parameters.proto()

	def getvertex_constants(self) -> Constant :
		return self._vertex_constants

	def setvertex_constants(self,value : List[Constant]) :
		if self._vertex_constants != value:
			self._vertex_constants = value
			self.vertex_constantsChanged.emit(value)

	vertex_constants = pyqtProperty(List, fget=getvertex_constants, fset=setvertex_constants, notify=vertex_constantsChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.name.extend(self._name)
		instance.tags = self._tags
		instance.vertex_program.extend(self._vertex_program)
		instance.fragment_program.extend(self._fragment_program)
		instance.vertex_space.extend(self._vertex_space)
		instance.vertex_constants.extend([i.proto() for i in self._vertex_constants])
		instance.fragment_constants.extend([i.proto() for i in self._fragment_constants])
		instance.textures = self._textures
		instance.samplers.extend([i.proto() for i in self._samplers])
		instance.max_page_count.extend(self._max_page_count)
		instance.attributes.extend([i.proto() for i in self._attributes])
		instance.program.extend(self._program)
		instance.pbr_parameters = self._pbr_parameters.proto()

	def getfragment_constants(self) -> Constant :
		return self._fragment_constants

	def setfragment_constants(self,value : List[Constant]) :
		if self._fragment_constants != value:
			self._fragment_constants = value
			self.fragment_constantsChanged.emit(value)

	fragment_constants = pyqtProperty(List, fget=getfragment_constants, fset=setfragment_constants, notify=fragment_constantsChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.name.extend(self._name)
		instance.tags = self._tags
		instance.vertex_program.extend(self._vertex_program)
		instance.fragment_program.extend(self._fragment_program)
		instance.vertex_space.extend(self._vertex_space)
		instance.vertex_constants.extend([i.proto() for i in self._vertex_constants])
		instance.fragment_constants.extend([i.proto() for i in self._fragment_constants])
		instance.textures = self._textures
		instance.samplers.extend([i.proto() for i in self._samplers])
		instance.max_page_count.extend(self._max_page_count)
		instance.attributes.extend([i.proto() for i in self._attributes])
		instance.program.extend(self._program)
		instance.pbr_parameters = self._pbr_parameters.proto()

	def gettextures(self) -> str :
		return self._textures

	def settextures(self,value : List[str]) :
		if self._textures != value:
			self._textures = value
			self.texturesChanged.emit(value)

	textures = pyqtProperty(List, fget=gettextures, fset=settextures, notify=texturesChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.name.extend(self._name)
		instance.tags = self._tags
		instance.vertex_program.extend(self._vertex_program)
		instance.fragment_program.extend(self._fragment_program)
		instance.vertex_space.extend(self._vertex_space)
		instance.vertex_constants.extend([i.proto() for i in self._vertex_constants])
		instance.fragment_constants.extend([i.proto() for i in self._fragment_constants])
		instance.textures = self._textures
		instance.samplers.extend([i.proto() for i in self._samplers])
		instance.max_page_count.extend(self._max_page_count)
		instance.attributes.extend([i.proto() for i in self._attributes])
		instance.program.extend(self._program)
		instance.pbr_parameters = self._pbr_parameters.proto()

	def getsamplers(self) -> Sampler :
		return self._samplers

	def setsamplers(self,value : List[Sampler]) :
		if self._samplers != value:
			self._samplers = value
			self.samplersChanged.emit(value)

	samplers = pyqtProperty(List, fget=getsamplers, fset=setsamplers, notify=samplersChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.name.extend(self._name)
		instance.tags = self._tags
		instance.vertex_program.extend(self._vertex_program)
		instance.fragment_program.extend(self._fragment_program)
		instance.vertex_space.extend(self._vertex_space)
		instance.vertex_constants.extend([i.proto() for i in self._vertex_constants])
		instance.fragment_constants.extend([i.proto() for i in self._fragment_constants])
		instance.textures = self._textures
		instance.samplers.extend([i.proto() for i in self._samplers])
		instance.max_page_count.extend(self._max_page_count)
		instance.attributes.extend([i.proto() for i in self._attributes])
		instance.program.extend(self._program)
		instance.pbr_parameters = self._pbr_parameters.proto()

	def getmax_page_count(self) -> int :
		return self._max_page_count

	def setmax_page_count(self,value : int) :
		if self._max_page_count != value:
			self._max_page_count = value
			self.max_page_countChanged.emit(value)

	max_page_count = pyqtProperty(int, fget=getmax_page_count, fset=setmax_page_count, notify=max_page_countChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.name.extend(self._name)
		instance.tags = self._tags
		instance.vertex_program.extend(self._vertex_program)
		instance.fragment_program.extend(self._fragment_program)
		instance.vertex_space.extend(self._vertex_space)
		instance.vertex_constants.extend([i.proto() for i in self._vertex_constants])
		instance.fragment_constants.extend([i.proto() for i in self._fragment_constants])
		instance.textures = self._textures
		instance.samplers.extend([i.proto() for i in self._samplers])
		instance.max_page_count.extend(self._max_page_count)
		instance.attributes.extend([i.proto() for i in self._attributes])
		instance.program.extend(self._program)
		instance.pbr_parameters = self._pbr_parameters.proto()

	def getattributes(self) -> VertexAttribute :
		return self._attributes

	def setattributes(self,value : List[VertexAttribute]) :
		if self._attributes != value:
			self._attributes = value
			self.attributesChanged.emit(value)

	attributes = pyqtProperty(List, fget=getattributes, fset=setattributes, notify=attributesChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.name.extend(self._name)
		instance.tags = self._tags
		instance.vertex_program.extend(self._vertex_program)
		instance.fragment_program.extend(self._fragment_program)
		instance.vertex_space.extend(self._vertex_space)
		instance.vertex_constants.extend([i.proto() for i in self._vertex_constants])
		instance.fragment_constants.extend([i.proto() for i in self._fragment_constants])
		instance.textures = self._textures
		instance.samplers.extend([i.proto() for i in self._samplers])
		instance.max_page_count.extend(self._max_page_count)
		instance.attributes.extend([i.proto() for i in self._attributes])
		instance.program.extend(self._program)
		instance.pbr_parameters = self._pbr_parameters.proto()

	def getprogram(self) -> str :
		return self._program

	def setprogram(self,value : str) :
		if self._program != value:
			self._program = value
			self.programChanged.emit(value)

	program = pyqtProperty(str, fget=getprogram, fset=setprogram, notify=programChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.name.extend(self._name)
		instance.tags = self._tags
		instance.vertex_program.extend(self._vertex_program)
		instance.fragment_program.extend(self._fragment_program)
		instance.vertex_space.extend(self._vertex_space)
		instance.vertex_constants.extend([i.proto() for i in self._vertex_constants])
		instance.fragment_constants.extend([i.proto() for i in self._fragment_constants])
		instance.textures = self._textures
		instance.samplers.extend([i.proto() for i in self._samplers])
		instance.max_page_count.extend(self._max_page_count)
		instance.attributes.extend([i.proto() for i in self._attributes])
		instance.program.extend(self._program)
		instance.pbr_parameters = self._pbr_parameters.proto()

	def getpbr_parameters(self) -> PbrParameters :
		return self._pbr_parameters

	def setpbr_parameters(self,value : PbrParameters) :
		if self._pbr_parameters != value:
			self._pbr_parameters = value
			self.pbr_parametersChanged.emit(value)

	pbr_parameters = pyqtProperty(QObject, fget=getpbr_parameters, fset=setpbr_parameters, notify=pbr_parametersChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.name.extend(self._name)
		instance.tags = self._tags
		instance.vertex_program.extend(self._vertex_program)
		instance.fragment_program.extend(self._fragment_program)
		instance.vertex_space.extend(self._vertex_space)
		instance.vertex_constants.extend([i.proto() for i in self._vertex_constants])
		instance.fragment_constants.extend([i.proto() for i in self._fragment_constants])
		instance.textures = self._textures
		instance.samplers.extend([i.proto() for i in self._samplers])
		instance.max_page_count.extend(self._max_page_count)
		instance.attributes.extend([i.proto() for i in self._attributes])
		instance.program.extend(self._program)
		instance.pbr_parameters = self._pbr_parameters.proto()

# ------- Matrix4 ------- #
class Matrix4(QObject) :
	__PROTO__ = sdk.Matrix4
	def __init__(self,m00 :float = float() ,m01 :float = float() ,m02 :float = float() ,m03 :float = float() ,m10 :float = float() ,m11 :float = float() ,m12 :float = float() ,m13 :float = float() ,m20 :float = float() ,m21 :float = float() ,m22 :float = float() ,m23 :float = float() ,m30 :float = float() ,m31 :float = float() ,m32 :float = float() ,m33 :float = float() ) -> Matrix4 :
		self._m00 = m00
		self._m01 = m01
		self._m02 = m02
		self._m03 = m03
		self._m10 = m10
		self._m11 = m11
		self._m12 = m12
		self._m13 = m13
		self._m20 = m20
		self._m21 = m21
		self._m22 = m22
		self._m23 = m23
		self._m30 = m30
		self._m31 = m31
		self._m32 = m32
		self._m33 = m33
		pass
	def getm00(self) -> float :
		return self._m00

	def setm00(self,value : float) :
		if self._m00 != value:
			self._m00 = value
			self.m00Changed.emit(value)

	m00 = pyqtProperty(float, fget=getm00, fset=setm00, notify=m00Changed)

	def proto(self) :
		instance = self.__PROTO__()
		instance.m00.extend(self._m00)
		instance.m01.extend(self._m01)
		instance.m02.extend(self._m02)
		instance.m03.extend(self._m03)
		instance.m10.extend(self._m10)
		instance.m11.extend(self._m11)
		instance.m12.extend(self._m12)
		instance.m13.extend(self._m13)
		instance.m20.extend(self._m20)
		instance.m21.extend(self._m21)
		instance.m22.extend(self._m22)
		instance.m23.extend(self._m23)
		instance.m30.extend(self._m30)
		instance.m31.extend(self._m31)
		instance.m32.extend(self._m32)
		instance.m33.extend(self._m33)

	def getm01(self) -> float :
		return self._m01

	def setm01(self,value : float) :
		if self._m01 != value:
			self._m01 = value
			self.m01Changed.emit(value)

	m01 = pyqtProperty(float, fget=getm01, fset=setm01, notify=m01Changed)

	def proto(self) :
		instance = self.__PROTO__()
		instance.m00.extend(self._m00)
		instance.m01.extend(self._m01)
		instance.m02.extend(self._m02)
		instance.m03.extend(self._m03)
		instance.m10.extend(self._m10)
		instance.m11.extend(self._m11)
		instance.m12.extend(self._m12)
		instance.m13.extend(self._m13)
		instance.m20.extend(self._m20)
		instance.m21.extend(self._m21)
		instance.m22.extend(self._m22)
		instance.m23.extend(self._m23)
		instance.m30.extend(self._m30)
		instance.m31.extend(self._m31)
		instance.m32.extend(self._m32)
		instance.m33.extend(self._m33)

	def getm02(self) -> float :
		return self._m02

	def setm02(self,value : float) :
		if self._m02 != value:
			self._m02 = value
			self.m02Changed.emit(value)

	m02 = pyqtProperty(float, fget=getm02, fset=setm02, notify=m02Changed)

	def proto(self) :
		instance = self.__PROTO__()
		instance.m00.extend(self._m00)
		instance.m01.extend(self._m01)
		instance.m02.extend(self._m02)
		instance.m03.extend(self._m03)
		instance.m10.extend(self._m10)
		instance.m11.extend(self._m11)
		instance.m12.extend(self._m12)
		instance.m13.extend(self._m13)
		instance.m20.extend(self._m20)
		instance.m21.extend(self._m21)
		instance.m22.extend(self._m22)
		instance.m23.extend(self._m23)
		instance.m30.extend(self._m30)
		instance.m31.extend(self._m31)
		instance.m32.extend(self._m32)
		instance.m33.extend(self._m33)

	def getm03(self) -> float :
		return self._m03

	def setm03(self,value : float) :
		if self._m03 != value:
			self._m03 = value
			self.m03Changed.emit(value)

	m03 = pyqtProperty(float, fget=getm03, fset=setm03, notify=m03Changed)

	def proto(self) :
		instance = self.__PROTO__()
		instance.m00.extend(self._m00)
		instance.m01.extend(self._m01)
		instance.m02.extend(self._m02)
		instance.m03.extend(self._m03)
		instance.m10.extend(self._m10)
		instance.m11.extend(self._m11)
		instance.m12.extend(self._m12)
		instance.m13.extend(self._m13)
		instance.m20.extend(self._m20)
		instance.m21.extend(self._m21)
		instance.m22.extend(self._m22)
		instance.m23.extend(self._m23)
		instance.m30.extend(self._m30)
		instance.m31.extend(self._m31)
		instance.m32.extend(self._m32)
		instance.m33.extend(self._m33)

	def getm10(self) -> float :
		return self._m10

	def setm10(self,value : float) :
		if self._m10 != value:
			self._m10 = value
			self.m10Changed.emit(value)

	m10 = pyqtProperty(float, fget=getm10, fset=setm10, notify=m10Changed)

	def proto(self) :
		instance = self.__PROTO__()
		instance.m00.extend(self._m00)
		instance.m01.extend(self._m01)
		instance.m02.extend(self._m02)
		instance.m03.extend(self._m03)
		instance.m10.extend(self._m10)
		instance.m11.extend(self._m11)
		instance.m12.extend(self._m12)
		instance.m13.extend(self._m13)
		instance.m20.extend(self._m20)
		instance.m21.extend(self._m21)
		instance.m22.extend(self._m22)
		instance.m23.extend(self._m23)
		instance.m30.extend(self._m30)
		instance.m31.extend(self._m31)
		instance.m32.extend(self._m32)
		instance.m33.extend(self._m33)

	def getm11(self) -> float :
		return self._m11

	def setm11(self,value : float) :
		if self._m11 != value:
			self._m11 = value
			self.m11Changed.emit(value)

	m11 = pyqtProperty(float, fget=getm11, fset=setm11, notify=m11Changed)

	def proto(self) :
		instance = self.__PROTO__()
		instance.m00.extend(self._m00)
		instance.m01.extend(self._m01)
		instance.m02.extend(self._m02)
		instance.m03.extend(self._m03)
		instance.m10.extend(self._m10)
		instance.m11.extend(self._m11)
		instance.m12.extend(self._m12)
		instance.m13.extend(self._m13)
		instance.m20.extend(self._m20)
		instance.m21.extend(self._m21)
		instance.m22.extend(self._m22)
		instance.m23.extend(self._m23)
		instance.m30.extend(self._m30)
		instance.m31.extend(self._m31)
		instance.m32.extend(self._m32)
		instance.m33.extend(self._m33)

	def getm12(self) -> float :
		return self._m12

	def setm12(self,value : float) :
		if self._m12 != value:
			self._m12 = value
			self.m12Changed.emit(value)

	m12 = pyqtProperty(float, fget=getm12, fset=setm12, notify=m12Changed)

	def proto(self) :
		instance = self.__PROTO__()
		instance.m00.extend(self._m00)
		instance.m01.extend(self._m01)
		instance.m02.extend(self._m02)
		instance.m03.extend(self._m03)
		instance.m10.extend(self._m10)
		instance.m11.extend(self._m11)
		instance.m12.extend(self._m12)
		instance.m13.extend(self._m13)
		instance.m20.extend(self._m20)
		instance.m21.extend(self._m21)
		instance.m22.extend(self._m22)
		instance.m23.extend(self._m23)
		instance.m30.extend(self._m30)
		instance.m31.extend(self._m31)
		instance.m32.extend(self._m32)
		instance.m33.extend(self._m33)

	def getm13(self) -> float :
		return self._m13

	def setm13(self,value : float) :
		if self._m13 != value:
			self._m13 = value
			self.m13Changed.emit(value)

	m13 = pyqtProperty(float, fget=getm13, fset=setm13, notify=m13Changed)

	def proto(self) :
		instance = self.__PROTO__()
		instance.m00.extend(self._m00)
		instance.m01.extend(self._m01)
		instance.m02.extend(self._m02)
		instance.m03.extend(self._m03)
		instance.m10.extend(self._m10)
		instance.m11.extend(self._m11)
		instance.m12.extend(self._m12)
		instance.m13.extend(self._m13)
		instance.m20.extend(self._m20)
		instance.m21.extend(self._m21)
		instance.m22.extend(self._m22)
		instance.m23.extend(self._m23)
		instance.m30.extend(self._m30)
		instance.m31.extend(self._m31)
		instance.m32.extend(self._m32)
		instance.m33.extend(self._m33)

	def getm20(self) -> float :
		return self._m20

	def setm20(self,value : float) :
		if self._m20 != value:
			self._m20 = value
			self.m20Changed.emit(value)

	m20 = pyqtProperty(float, fget=getm20, fset=setm20, notify=m20Changed)

	def proto(self) :
		instance = self.__PROTO__()
		instance.m00.extend(self._m00)
		instance.m01.extend(self._m01)
		instance.m02.extend(self._m02)
		instance.m03.extend(self._m03)
		instance.m10.extend(self._m10)
		instance.m11.extend(self._m11)
		instance.m12.extend(self._m12)
		instance.m13.extend(self._m13)
		instance.m20.extend(self._m20)
		instance.m21.extend(self._m21)
		instance.m22.extend(self._m22)
		instance.m23.extend(self._m23)
		instance.m30.extend(self._m30)
		instance.m31.extend(self._m31)
		instance.m32.extend(self._m32)
		instance.m33.extend(self._m33)

	def getm21(self) -> float :
		return self._m21

	def setm21(self,value : float) :
		if self._m21 != value:
			self._m21 = value
			self.m21Changed.emit(value)

	m21 = pyqtProperty(float, fget=getm21, fset=setm21, notify=m21Changed)

	def proto(self) :
		instance = self.__PROTO__()
		instance.m00.extend(self._m00)
		instance.m01.extend(self._m01)
		instance.m02.extend(self._m02)
		instance.m03.extend(self._m03)
		instance.m10.extend(self._m10)
		instance.m11.extend(self._m11)
		instance.m12.extend(self._m12)
		instance.m13.extend(self._m13)
		instance.m20.extend(self._m20)
		instance.m21.extend(self._m21)
		instance.m22.extend(self._m22)
		instance.m23.extend(self._m23)
		instance.m30.extend(self._m30)
		instance.m31.extend(self._m31)
		instance.m32.extend(self._m32)
		instance.m33.extend(self._m33)

	def getm22(self) -> float :
		return self._m22

	def setm22(self,value : float) :
		if self._m22 != value:
			self._m22 = value
			self.m22Changed.emit(value)

	m22 = pyqtProperty(float, fget=getm22, fset=setm22, notify=m22Changed)

	def proto(self) :
		instance = self.__PROTO__()
		instance.m00.extend(self._m00)
		instance.m01.extend(self._m01)
		instance.m02.extend(self._m02)
		instance.m03.extend(self._m03)
		instance.m10.extend(self._m10)
		instance.m11.extend(self._m11)
		instance.m12.extend(self._m12)
		instance.m13.extend(self._m13)
		instance.m20.extend(self._m20)
		instance.m21.extend(self._m21)
		instance.m22.extend(self._m22)
		instance.m23.extend(self._m23)
		instance.m30.extend(self._m30)
		instance.m31.extend(self._m31)
		instance.m32.extend(self._m32)
		instance.m33.extend(self._m33)

	def getm23(self) -> float :
		return self._m23

	def setm23(self,value : float) :
		if self._m23 != value:
			self._m23 = value
			self.m23Changed.emit(value)

	m23 = pyqtProperty(float, fget=getm23, fset=setm23, notify=m23Changed)

	def proto(self) :
		instance = self.__PROTO__()
		instance.m00.extend(self._m00)
		instance.m01.extend(self._m01)
		instance.m02.extend(self._m02)
		instance.m03.extend(self._m03)
		instance.m10.extend(self._m10)
		instance.m11.extend(self._m11)
		instance.m12.extend(self._m12)
		instance.m13.extend(self._m13)
		instance.m20.extend(self._m20)
		instance.m21.extend(self._m21)
		instance.m22.extend(self._m22)
		instance.m23.extend(self._m23)
		instance.m30.extend(self._m30)
		instance.m31.extend(self._m31)
		instance.m32.extend(self._m32)
		instance.m33.extend(self._m33)

	def getm30(self) -> float :
		return self._m30

	def setm30(self,value : float) :
		if self._m30 != value:
			self._m30 = value
			self.m30Changed.emit(value)

	m30 = pyqtProperty(float, fget=getm30, fset=setm30, notify=m30Changed)

	def proto(self) :
		instance = self.__PROTO__()
		instance.m00.extend(self._m00)
		instance.m01.extend(self._m01)
		instance.m02.extend(self._m02)
		instance.m03.extend(self._m03)
		instance.m10.extend(self._m10)
		instance.m11.extend(self._m11)
		instance.m12.extend(self._m12)
		instance.m13.extend(self._m13)
		instance.m20.extend(self._m20)
		instance.m21.extend(self._m21)
		instance.m22.extend(self._m22)
		instance.m23.extend(self._m23)
		instance.m30.extend(self._m30)
		instance.m31.extend(self._m31)
		instance.m32.extend(self._m32)
		instance.m33.extend(self._m33)

	def getm31(self) -> float :
		return self._m31

	def setm31(self,value : float) :
		if self._m31 != value:
			self._m31 = value
			self.m31Changed.emit(value)

	m31 = pyqtProperty(float, fget=getm31, fset=setm31, notify=m31Changed)

	def proto(self) :
		instance = self.__PROTO__()
		instance.m00.extend(self._m00)
		instance.m01.extend(self._m01)
		instance.m02.extend(self._m02)
		instance.m03.extend(self._m03)
		instance.m10.extend(self._m10)
		instance.m11.extend(self._m11)
		instance.m12.extend(self._m12)
		instance.m13.extend(self._m13)
		instance.m20.extend(self._m20)
		instance.m21.extend(self._m21)
		instance.m22.extend(self._m22)
		instance.m23.extend(self._m23)
		instance.m30.extend(self._m30)
		instance.m31.extend(self._m31)
		instance.m32.extend(self._m32)
		instance.m33.extend(self._m33)

	def getm32(self) -> float :
		return self._m32

	def setm32(self,value : float) :
		if self._m32 != value:
			self._m32 = value
			self.m32Changed.emit(value)

	m32 = pyqtProperty(float, fget=getm32, fset=setm32, notify=m32Changed)

	def proto(self) :
		instance = self.__PROTO__()
		instance.m00.extend(self._m00)
		instance.m01.extend(self._m01)
		instance.m02.extend(self._m02)
		instance.m03.extend(self._m03)
		instance.m10.extend(self._m10)
		instance.m11.extend(self._m11)
		instance.m12.extend(self._m12)
		instance.m13.extend(self._m13)
		instance.m20.extend(self._m20)
		instance.m21.extend(self._m21)
		instance.m22.extend(self._m22)
		instance.m23.extend(self._m23)
		instance.m30.extend(self._m30)
		instance.m31.extend(self._m31)
		instance.m32.extend(self._m32)
		instance.m33.extend(self._m33)

	def getm33(self) -> float :
		return self._m33

	def setm33(self,value : float) :
		if self._m33 != value:
			self._m33 = value
			self.m33Changed.emit(value)

	m33 = pyqtProperty(float, fget=getm33, fset=setm33, notify=m33Changed)

	def proto(self) :
		instance = self.__PROTO__()
		instance.m00.extend(self._m00)
		instance.m01.extend(self._m01)
		instance.m02.extend(self._m02)
		instance.m03.extend(self._m03)
		instance.m10.extend(self._m10)
		instance.m11.extend(self._m11)
		instance.m12.extend(self._m12)
		instance.m13.extend(self._m13)
		instance.m20.extend(self._m20)
		instance.m21.extend(self._m21)
		instance.m22.extend(self._m22)
		instance.m23.extend(self._m23)
		instance.m30.extend(self._m30)
		instance.m31.extend(self._m31)
		instance.m32.extend(self._m32)
		instance.m33.extend(self._m33)

# ------- MeshDesc ------- #
class PrimitiveType(Enum):
	PRIMITIVE_LINES = 1
	PRIMITIVE_TRIANGLES = 4
	PRIMITIVE_TRIANGLE_STRIP = 5
class MeshDesc(QObject) :
	__PROTO__ = sdk.MeshDesc
	def __init__(self,material :str = str() ,vertices :str = str() ,textures :List[str] = [] ,primitive_type :int = int() ,position_stream :str = str() ,normal_stream :str = str() ) -> MeshDesc :
		self._material = material
		self._vertices = vertices
		self._textures = textures
		self._primitive_type = primitive_type
		self._position_stream = position_stream
		self._normal_stream = normal_stream
		pass
	def getmaterial(self) -> str :
		return self._material

	def setmaterial(self,value : str) :
		if self._material != value:
			self._material = value
			self.materialChanged.emit(value)

	material = pyqtProperty(str, fget=getmaterial, fset=setmaterial, notify=materialChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.material.extend(self._material)
		instance.vertices.extend(self._vertices)
		instance.textures = self._textures
		instance.primitive_type.extend(self._primitive_type)
		instance.position_stream.extend(self._position_stream)
		instance.normal_stream.extend(self._normal_stream)

	def getvertices(self) -> str :
		return self._vertices

	def setvertices(self,value : str) :
		if self._vertices != value:
			self._vertices = value
			self.verticesChanged.emit(value)

	vertices = pyqtProperty(str, fget=getvertices, fset=setvertices, notify=verticesChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.material.extend(self._material)
		instance.vertices.extend(self._vertices)
		instance.textures = self._textures
		instance.primitive_type.extend(self._primitive_type)
		instance.position_stream.extend(self._position_stream)
		instance.normal_stream.extend(self._normal_stream)

	def gettextures(self) -> str :
		return self._textures

	def settextures(self,value : List[str]) :
		if self._textures != value:
			self._textures = value
			self.texturesChanged.emit(value)

	textures = pyqtProperty(List, fget=gettextures, fset=settextures, notify=texturesChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.material.extend(self._material)
		instance.vertices.extend(self._vertices)
		instance.textures = self._textures
		instance.primitive_type.extend(self._primitive_type)
		instance.position_stream.extend(self._position_stream)
		instance.normal_stream.extend(self._normal_stream)

	def getprimitive_type(self) -> int :
		return self._primitive_type

	def setprimitive_type(self,value : int) :
		if self._primitive_type != value:
			self._primitive_type = value
			self.primitive_typeChanged.emit(value)

	primitive_type = pyqtProperty(int, fget=getprimitive_type, fset=setprimitive_type, notify=primitive_typeChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.material.extend(self._material)
		instance.vertices.extend(self._vertices)
		instance.textures = self._textures
		instance.primitive_type.extend(self._primitive_type)
		instance.position_stream.extend(self._position_stream)
		instance.normal_stream.extend(self._normal_stream)

	def getposition_stream(self) -> str :
		return self._position_stream

	def setposition_stream(self,value : str) :
		if self._position_stream != value:
			self._position_stream = value
			self.position_streamChanged.emit(value)

	position_stream = pyqtProperty(str, fget=getposition_stream, fset=setposition_stream, notify=position_streamChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.material.extend(self._material)
		instance.vertices.extend(self._vertices)
		instance.textures = self._textures
		instance.primitive_type.extend(self._primitive_type)
		instance.position_stream.extend(self._position_stream)
		instance.normal_stream.extend(self._normal_stream)

	def getnormal_stream(self) -> str :
		return self._normal_stream

	def setnormal_stream(self,value : str) :
		if self._normal_stream != value:
			self._normal_stream = value
			self.normal_streamChanged.emit(value)

	normal_stream = pyqtProperty(str, fget=getnormal_stream, fset=setnormal_stream, notify=normal_streamChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.material.extend(self._material)
		instance.vertices.extend(self._vertices)
		instance.textures = self._textures
		instance.primitive_type.extend(self._primitive_type)
		instance.position_stream.extend(self._position_stream)
		instance.normal_stream.extend(self._normal_stream)

# ------- Model ------- #
class Model(QObject) :
	__PROTO__ = sdk.Model
	def __init__(self,rig_scene :str = str() ,default_animation :str = str() ,materials :List[Material] = [],create_go_bones :bool = bool() ) -> Model :
		self._rig_scene = rig_scene
		self._default_animation = default_animation
		self._materials = materials
		self._create_go_bones = create_go_bones
		pass
	def getrig_scene(self) -> str :
		return self._rig_scene

	def setrig_scene(self,value : str) :
		if self._rig_scene != value:
			self._rig_scene = value
			self.rig_sceneChanged.emit(value)

	rig_scene = pyqtProperty(str, fget=getrig_scene, fset=setrig_scene, notify=rig_sceneChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.rig_scene.extend(self._rig_scene)
		instance.default_animation.extend(self._default_animation)
		instance.materials.extend([i.proto() for i in self._materials])
		instance.create_go_bones.extend(self._create_go_bones)

	def getdefault_animation(self) -> str :
		return self._default_animation

	def setdefault_animation(self,value : str) :
		if self._default_animation != value:
			self._default_animation = value
			self.default_animationChanged.emit(value)

	default_animation = pyqtProperty(str, fget=getdefault_animation, fset=setdefault_animation, notify=default_animationChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.rig_scene.extend(self._rig_scene)
		instance.default_animation.extend(self._default_animation)
		instance.materials.extend([i.proto() for i in self._materials])
		instance.create_go_bones.extend(self._create_go_bones)

	def getmaterials(self) -> Material :
		return self._materials

	def setmaterials(self,value : List[Material]) :
		if self._materials != value:
			self._materials = value
			self.materialsChanged.emit(value)

	materials = pyqtProperty(List, fget=getmaterials, fset=setmaterials, notify=materialsChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.rig_scene.extend(self._rig_scene)
		instance.default_animation.extend(self._default_animation)
		instance.materials.extend([i.proto() for i in self._materials])
		instance.create_go_bones.extend(self._create_go_bones)

	def getcreate_go_bones(self) -> bool :
		return self._create_go_bones

	def setcreate_go_bones(self,value : bool) :
		if self._create_go_bones != value:
			self._create_go_bones = value
			self.create_go_bonesChanged.emit(value)

	create_go_bones = pyqtProperty(bool, fget=getcreate_go_bones, fset=setcreate_go_bones, notify=create_go_bonesChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.rig_scene.extend(self._rig_scene)
		instance.default_animation.extend(self._default_animation)
		instance.materials.extend([i.proto() for i in self._materials])
		instance.create_go_bones.extend(self._create_go_bones)

# ------- ModelAnimationDone ------- #
class ModelAnimationDone(QObject) :
	__PROTO__ = sdk.ModelAnimationDone
	def __init__(self,animation_id :int = int() ,playback :int = int() ) -> ModelAnimationDone :
		self._animation_id = animation_id
		self._playback = playback
		pass
	def getanimation_id(self) -> int :
		return self._animation_id

	def setanimation_id(self,value : int) :
		if self._animation_id != value:
			self._animation_id = value
			self.animation_idChanged.emit(value)

	animation_id = pyqtProperty(int, fget=getanimation_id, fset=setanimation_id, notify=animation_idChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.animation_id.extend(self._animation_id)
		instance.playback.extend(self._playback)

	def getplayback(self) -> int :
		return self._playback

	def setplayback(self,value : int) :
		if self._playback != value:
			self._playback = value
			self.playbackChanged.emit(value)

	playback = pyqtProperty(int, fget=getplayback, fset=setplayback, notify=playbackChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.animation_id.extend(self._animation_id)
		instance.playback.extend(self._playback)

# ------- ModelCancelAnimation ------- #
class ModelCancelAnimation(QObject) :
	__PROTO__ = sdk.ModelCancelAnimation
	def __init__(self) -> ModelCancelAnimation :
		pass
# ------- ModelDesc ------- #
class ModelDesc(QObject) :
	__PROTO__ = sdk.ModelDesc
	def __init__(self,mesh :str = str() ,material :str = str() ,textures :List[str] = [] ,skeleton :str = str() ,animations :str = str() ,default_animation :str = str() ,name :str = str() ,materials :List[Material] = [],create_go_bones :bool = bool() ) -> ModelDesc :
		self._mesh = mesh
		self._material = material
		self._textures = textures
		self._skeleton = skeleton
		self._animations = animations
		self._default_animation = default_animation
		self._name = name
		self._materials = materials
		self._create_go_bones = create_go_bones
		pass
	def getmesh(self) -> str :
		return self._mesh

	def setmesh(self,value : str) :
		if self._mesh != value:
			self._mesh = value
			self.meshChanged.emit(value)

	mesh = pyqtProperty(str, fget=getmesh, fset=setmesh, notify=meshChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.mesh.extend(self._mesh)
		instance.material.extend(self._material)
		instance.textures = self._textures
		instance.skeleton.extend(self._skeleton)
		instance.animations.extend(self._animations)
		instance.default_animation.extend(self._default_animation)
		instance.name.extend(self._name)
		instance.materials.extend([i.proto() for i in self._materials])
		instance.create_go_bones.extend(self._create_go_bones)

	def getmaterial(self) -> str :
		return self._material

	def setmaterial(self,value : str) :
		if self._material != value:
			self._material = value
			self.materialChanged.emit(value)

	material = pyqtProperty(str, fget=getmaterial, fset=setmaterial, notify=materialChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.mesh.extend(self._mesh)
		instance.material.extend(self._material)
		instance.textures = self._textures
		instance.skeleton.extend(self._skeleton)
		instance.animations.extend(self._animations)
		instance.default_animation.extend(self._default_animation)
		instance.name.extend(self._name)
		instance.materials.extend([i.proto() for i in self._materials])
		instance.create_go_bones.extend(self._create_go_bones)

	def gettextures(self) -> str :
		return self._textures

	def settextures(self,value : List[str]) :
		if self._textures != value:
			self._textures = value
			self.texturesChanged.emit(value)

	textures = pyqtProperty(List, fget=gettextures, fset=settextures, notify=texturesChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.mesh.extend(self._mesh)
		instance.material.extend(self._material)
		instance.textures = self._textures
		instance.skeleton.extend(self._skeleton)
		instance.animations.extend(self._animations)
		instance.default_animation.extend(self._default_animation)
		instance.name.extend(self._name)
		instance.materials.extend([i.proto() for i in self._materials])
		instance.create_go_bones.extend(self._create_go_bones)

	def getskeleton(self) -> str :
		return self._skeleton

	def setskeleton(self,value : str) :
		if self._skeleton != value:
			self._skeleton = value
			self.skeletonChanged.emit(value)

	skeleton = pyqtProperty(str, fget=getskeleton, fset=setskeleton, notify=skeletonChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.mesh.extend(self._mesh)
		instance.material.extend(self._material)
		instance.textures = self._textures
		instance.skeleton.extend(self._skeleton)
		instance.animations.extend(self._animations)
		instance.default_animation.extend(self._default_animation)
		instance.name.extend(self._name)
		instance.materials.extend([i.proto() for i in self._materials])
		instance.create_go_bones.extend(self._create_go_bones)

	def getanimations(self) -> str :
		return self._animations

	def setanimations(self,value : str) :
		if self._animations != value:
			self._animations = value
			self.animationsChanged.emit(value)

	animations = pyqtProperty(str, fget=getanimations, fset=setanimations, notify=animationsChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.mesh.extend(self._mesh)
		instance.material.extend(self._material)
		instance.textures = self._textures
		instance.skeleton.extend(self._skeleton)
		instance.animations.extend(self._animations)
		instance.default_animation.extend(self._default_animation)
		instance.name.extend(self._name)
		instance.materials.extend([i.proto() for i in self._materials])
		instance.create_go_bones.extend(self._create_go_bones)

	def getdefault_animation(self) -> str :
		return self._default_animation

	def setdefault_animation(self,value : str) :
		if self._default_animation != value:
			self._default_animation = value
			self.default_animationChanged.emit(value)

	default_animation = pyqtProperty(str, fget=getdefault_animation, fset=setdefault_animation, notify=default_animationChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.mesh.extend(self._mesh)
		instance.material.extend(self._material)
		instance.textures = self._textures
		instance.skeleton.extend(self._skeleton)
		instance.animations.extend(self._animations)
		instance.default_animation.extend(self._default_animation)
		instance.name.extend(self._name)
		instance.materials.extend([i.proto() for i in self._materials])
		instance.create_go_bones.extend(self._create_go_bones)

	def getname(self) -> str :
		return self._name

	def setname(self,value : str) :
		if self._name != value:
			self._name = value
			self.nameChanged.emit(value)

	name = pyqtProperty(str, fget=getname, fset=setname, notify=nameChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.mesh.extend(self._mesh)
		instance.material.extend(self._material)
		instance.textures = self._textures
		instance.skeleton.extend(self._skeleton)
		instance.animations.extend(self._animations)
		instance.default_animation.extend(self._default_animation)
		instance.name.extend(self._name)
		instance.materials.extend([i.proto() for i in self._materials])
		instance.create_go_bones.extend(self._create_go_bones)

	def getmaterials(self) -> Material :
		return self._materials

	def setmaterials(self,value : List[Material]) :
		if self._materials != value:
			self._materials = value
			self.materialsChanged.emit(value)

	materials = pyqtProperty(List, fget=getmaterials, fset=setmaterials, notify=materialsChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.mesh.extend(self._mesh)
		instance.material.extend(self._material)
		instance.textures = self._textures
		instance.skeleton.extend(self._skeleton)
		instance.animations.extend(self._animations)
		instance.default_animation.extend(self._default_animation)
		instance.name.extend(self._name)
		instance.materials.extend([i.proto() for i in self._materials])
		instance.create_go_bones.extend(self._create_go_bones)

	def getcreate_go_bones(self) -> bool :
		return self._create_go_bones

	def setcreate_go_bones(self,value : bool) :
		if self._create_go_bones != value:
			self._create_go_bones = value
			self.create_go_bonesChanged.emit(value)

	create_go_bones = pyqtProperty(bool, fget=getcreate_go_bones, fset=setcreate_go_bones, notify=create_go_bonesChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.mesh.extend(self._mesh)
		instance.material.extend(self._material)
		instance.textures = self._textures
		instance.skeleton.extend(self._skeleton)
		instance.animations.extend(self._animations)
		instance.default_animation.extend(self._default_animation)
		instance.name.extend(self._name)
		instance.materials.extend([i.proto() for i in self._materials])
		instance.create_go_bones.extend(self._create_go_bones)

# ------- ModelPlayAnimation ------- #
class ModelPlayAnimation(QObject) :
	__PROTO__ = sdk.ModelPlayAnimation
	def __init__(self,animation_id :int = int() ,playback :int = int() ,blend_duration :float = float() ,offset :float = float() ,playback_rate :float = float() ) -> ModelPlayAnimation :
		self._animation_id = animation_id
		self._playback = playback
		self._blend_duration = blend_duration
		self._offset = offset
		self._playback_rate = playback_rate
		pass
	def getanimation_id(self) -> int :
		return self._animation_id

	def setanimation_id(self,value : int) :
		if self._animation_id != value:
			self._animation_id = value
			self.animation_idChanged.emit(value)

	animation_id = pyqtProperty(int, fget=getanimation_id, fset=setanimation_id, notify=animation_idChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.animation_id.extend(self._animation_id)
		instance.playback.extend(self._playback)
		instance.blend_duration.extend(self._blend_duration)
		instance.offset.extend(self._offset)
		instance.playback_rate.extend(self._playback_rate)

	def getplayback(self) -> int :
		return self._playback

	def setplayback(self,value : int) :
		if self._playback != value:
			self._playback = value
			self.playbackChanged.emit(value)

	playback = pyqtProperty(int, fget=getplayback, fset=setplayback, notify=playbackChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.animation_id.extend(self._animation_id)
		instance.playback.extend(self._playback)
		instance.blend_duration.extend(self._blend_duration)
		instance.offset.extend(self._offset)
		instance.playback_rate.extend(self._playback_rate)

	def getblend_duration(self) -> float :
		return self._blend_duration

	def setblend_duration(self,value : float) :
		if self._blend_duration != value:
			self._blend_duration = value
			self.blend_durationChanged.emit(value)

	blend_duration = pyqtProperty(float, fget=getblend_duration, fset=setblend_duration, notify=blend_durationChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.animation_id.extend(self._animation_id)
		instance.playback.extend(self._playback)
		instance.blend_duration.extend(self._blend_duration)
		instance.offset.extend(self._offset)
		instance.playback_rate.extend(self._playback_rate)

	def getoffset(self) -> float :
		return self._offset

	def setoffset(self,value : float) :
		if self._offset != value:
			self._offset = value
			self.offsetChanged.emit(value)

	offset = pyqtProperty(float, fget=getoffset, fset=setoffset, notify=offsetChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.animation_id.extend(self._animation_id)
		instance.playback.extend(self._playback)
		instance.blend_duration.extend(self._blend_duration)
		instance.offset.extend(self._offset)
		instance.playback_rate.extend(self._playback_rate)

	def getplayback_rate(self) -> float :
		return self._playback_rate

	def setplayback_rate(self,value : float) :
		if self._playback_rate != value:
			self._playback_rate = value
			self.playback_rateChanged.emit(value)

	playback_rate = pyqtProperty(float, fget=getplayback_rate, fset=setplayback_rate, notify=playback_rateChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.animation_id.extend(self._animation_id)
		instance.playback.extend(self._playback)
		instance.blend_duration.extend(self._blend_duration)
		instance.offset.extend(self._offset)
		instance.playback_rate.extend(self._playback_rate)

# ------- NodeDesc ------- #
class Type(Enum):
	TYPE_BOX = 0
	TYPE_TEXT = 1
	TYPE_PIE = 2
	TYPE_TEMPLATE = 3
	TYPE_SPINE = 4
	TYPE_PARTICLEFX = 5
	TYPE_CUSTOM = 6
class BlendMode(Enum):
	BLEND_MODE_ALPHA = 0
	BLEND_MODE_ADD = 1
	BLEND_MODE_ADD_ALPHA = 2
	BLEND_MODE_MULT = 3
	BLEND_MODE_SCREEN = 4
class ClippingMode(Enum):
	CLIPPING_MODE_NONE = 0
	CLIPPING_MODE_STENCIL = 2
class XAnchor(Enum):
	XANCHOR_NONE = 0
	XANCHOR_LEFT = 1
	XANCHOR_RIGHT = 2
class YAnchor(Enum):
	YANCHOR_NONE = 0
	YANCHOR_TOP = 1
	YANCHOR_BOTTOM = 2
class Pivot(Enum):
	PIVOT_CENTER = 0
	PIVOT_N = 1
	PIVOT_NE = 2
	PIVOT_E = 3
	PIVOT_SE = 4
	PIVOT_S = 5
	PIVOT_SW = 6
	PIVOT_W = 7
	PIVOT_NW = 8
class AdjustMode(Enum):
	ADJUST_MODE_FIT = 0
	ADJUST_MODE_ZOOM = 1
	ADJUST_MODE_STRETCH = 2
class SizeMode(Enum):
	SIZE_MODE_MANUAL = 0
	SIZE_MODE_AUTO = 1
class PieBounds(Enum):
	PIEBOUNDS_RECTANGLE = 0
	PIEBOUNDS_ELLIPSE = 1
class NodeDesc(QObject) :
	__PROTO__ = sdk.NodeDesc
	def __init__(self,position :Vector4 = None ,rotation :Vector4 = None ,scale :Vector4One = None ,size :Vector4 = None ,color :Vector4One = None ,type :int = int() ,blend_mode :int = int() ,text :str = str() ,texture :str = str() ,font :str = str() ,id :str = str() ,xanchor :int = int() ,yanchor :int = int() ,pivot :int = int() ,outline :Vector4WOne = None ,shadow :Vector4WOne = None ,adjust_mode :int = int() ,line_break :bool = bool() ,parent :str = str() ,layer :str = str() ,inherit_alpha :bool = bool() ,slice9 :Vector4 = None ,outerBounds :int = int() ,innerRadius :float = float() ,perimeterVertices :int = int() ,pieFillAngle :float = float() ,clipping_mode :int = int() ,clipping_visible :bool = bool() ,clipping_inverted :bool = bool() ,alpha :float = float() ,outline_alpha :float = float() ,shadow_alpha :float = float() ,overridden_fields :List[int] = [] ,template :str = str() ,template_node_child :bool = bool() ,text_leading :float = float() ,text_tracking :float = float() ,size_mode :int = int() ,spine_scene :str = str() ,spine_default_animation :str = str() ,spine_skin :str = str() ,spine_node_child :bool = bool() ,particlefx :str = str() ,custom_type :int = int() ,enabled :bool = bool() ,visible :bool = bool() ,material :str = str() ) -> NodeDesc :
		self._position = position
		self._rotation = rotation
		self._scale = scale
		self._size = size
		self._color = color
		self._type = type
		self._blend_mode = blend_mode
		self._text = text
		self._texture = texture
		self._font = font
		self._id = id
		self._xanchor = xanchor
		self._yanchor = yanchor
		self._pivot = pivot
		self._outline = outline
		self._shadow = shadow
		self._adjust_mode = adjust_mode
		self._line_break = line_break
		self._parent = parent
		self._layer = layer
		self._inherit_alpha = inherit_alpha
		self._slice9 = slice9
		self._outerBounds = outerBounds
		self._innerRadius = innerRadius
		self._perimeterVertices = perimeterVertices
		self._pieFillAngle = pieFillAngle
		self._clipping_mode = clipping_mode
		self._clipping_visible = clipping_visible
		self._clipping_inverted = clipping_inverted
		self._alpha = alpha
		self._outline_alpha = outline_alpha
		self._shadow_alpha = shadow_alpha
		self._overridden_fields = overridden_fields
		self._template = template
		self._template_node_child = template_node_child
		self._text_leading = text_leading
		self._text_tracking = text_tracking
		self._size_mode = size_mode
		self._spine_scene = spine_scene
		self._spine_default_animation = spine_default_animation
		self._spine_skin = spine_skin
		self._spine_node_child = spine_node_child
		self._particlefx = particlefx
		self._custom_type = custom_type
		self._enabled = enabled
		self._visible = visible
		self._material = material
		pass
	def getposition(self) -> Vector4 :
		return self._position

	def setposition(self,value : Vector4) :
		if self._position != value:
			self._position = value
			self.positionChanged.emit(value)

	position = pyqtProperty(QObject, fget=getposition, fset=setposition, notify=positionChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.position = self._position.proto()
		instance.rotation = self._rotation.proto()
		instance.scale = self._scale.proto()
		instance.size = self._size.proto()
		instance.color = self._color.proto()
		instance.type.extend(self._type)
		instance.blend_mode.extend(self._blend_mode)
		instance.text.extend(self._text)
		instance.texture.extend(self._texture)
		instance.font.extend(self._font)
		instance.id.extend(self._id)
		instance.xanchor.extend(self._xanchor)
		instance.yanchor.extend(self._yanchor)
		instance.pivot.extend(self._pivot)
		instance.outline = self._outline.proto()
		instance.shadow = self._shadow.proto()
		instance.adjust_mode.extend(self._adjust_mode)
		instance.line_break.extend(self._line_break)
		instance.parent.extend(self._parent)
		instance.layer.extend(self._layer)
		instance.inherit_alpha.extend(self._inherit_alpha)
		instance.slice9 = self._slice9.proto()
		instance.outerBounds.extend(self._outerBounds)
		instance.innerRadius.extend(self._innerRadius)
		instance.perimeterVertices.extend(self._perimeterVertices)
		instance.pieFillAngle.extend(self._pieFillAngle)
		instance.clipping_mode.extend(self._clipping_mode)
		instance.clipping_visible.extend(self._clipping_visible)
		instance.clipping_inverted.extend(self._clipping_inverted)
		instance.alpha.extend(self._alpha)
		instance.outline_alpha.extend(self._outline_alpha)
		instance.shadow_alpha.extend(self._shadow_alpha)
		instance.overridden_fields = self._overridden_fields
		instance.template.extend(self._template)
		instance.template_node_child.extend(self._template_node_child)
		instance.text_leading.extend(self._text_leading)
		instance.text_tracking.extend(self._text_tracking)
		instance.size_mode.extend(self._size_mode)
		instance.spine_scene.extend(self._spine_scene)
		instance.spine_default_animation.extend(self._spine_default_animation)
		instance.spine_skin.extend(self._spine_skin)
		instance.spine_node_child.extend(self._spine_node_child)
		instance.particlefx.extend(self._particlefx)
		instance.custom_type.extend(self._custom_type)
		instance.enabled.extend(self._enabled)
		instance.visible.extend(self._visible)
		instance.material.extend(self._material)

	def getrotation(self) -> Vector4 :
		return self._rotation

	def setrotation(self,value : Vector4) :
		if self._rotation != value:
			self._rotation = value
			self.rotationChanged.emit(value)

	rotation = pyqtProperty(QObject, fget=getrotation, fset=setrotation, notify=rotationChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.position = self._position.proto()
		instance.rotation = self._rotation.proto()
		instance.scale = self._scale.proto()
		instance.size = self._size.proto()
		instance.color = self._color.proto()
		instance.type.extend(self._type)
		instance.blend_mode.extend(self._blend_mode)
		instance.text.extend(self._text)
		instance.texture.extend(self._texture)
		instance.font.extend(self._font)
		instance.id.extend(self._id)
		instance.xanchor.extend(self._xanchor)
		instance.yanchor.extend(self._yanchor)
		instance.pivot.extend(self._pivot)
		instance.outline = self._outline.proto()
		instance.shadow = self._shadow.proto()
		instance.adjust_mode.extend(self._adjust_mode)
		instance.line_break.extend(self._line_break)
		instance.parent.extend(self._parent)
		instance.layer.extend(self._layer)
		instance.inherit_alpha.extend(self._inherit_alpha)
		instance.slice9 = self._slice9.proto()
		instance.outerBounds.extend(self._outerBounds)
		instance.innerRadius.extend(self._innerRadius)
		instance.perimeterVertices.extend(self._perimeterVertices)
		instance.pieFillAngle.extend(self._pieFillAngle)
		instance.clipping_mode.extend(self._clipping_mode)
		instance.clipping_visible.extend(self._clipping_visible)
		instance.clipping_inverted.extend(self._clipping_inverted)
		instance.alpha.extend(self._alpha)
		instance.outline_alpha.extend(self._outline_alpha)
		instance.shadow_alpha.extend(self._shadow_alpha)
		instance.overridden_fields = self._overridden_fields
		instance.template.extend(self._template)
		instance.template_node_child.extend(self._template_node_child)
		instance.text_leading.extend(self._text_leading)
		instance.text_tracking.extend(self._text_tracking)
		instance.size_mode.extend(self._size_mode)
		instance.spine_scene.extend(self._spine_scene)
		instance.spine_default_animation.extend(self._spine_default_animation)
		instance.spine_skin.extend(self._spine_skin)
		instance.spine_node_child.extend(self._spine_node_child)
		instance.particlefx.extend(self._particlefx)
		instance.custom_type.extend(self._custom_type)
		instance.enabled.extend(self._enabled)
		instance.visible.extend(self._visible)
		instance.material.extend(self._material)

	def getscale(self) -> Vector4One :
		return self._scale

	def setscale(self,value : Vector4One) :
		if self._scale != value:
			self._scale = value
			self.scaleChanged.emit(value)

	scale = pyqtProperty(QObject, fget=getscale, fset=setscale, notify=scaleChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.position = self._position.proto()
		instance.rotation = self._rotation.proto()
		instance.scale = self._scale.proto()
		instance.size = self._size.proto()
		instance.color = self._color.proto()
		instance.type.extend(self._type)
		instance.blend_mode.extend(self._blend_mode)
		instance.text.extend(self._text)
		instance.texture.extend(self._texture)
		instance.font.extend(self._font)
		instance.id.extend(self._id)
		instance.xanchor.extend(self._xanchor)
		instance.yanchor.extend(self._yanchor)
		instance.pivot.extend(self._pivot)
		instance.outline = self._outline.proto()
		instance.shadow = self._shadow.proto()
		instance.adjust_mode.extend(self._adjust_mode)
		instance.line_break.extend(self._line_break)
		instance.parent.extend(self._parent)
		instance.layer.extend(self._layer)
		instance.inherit_alpha.extend(self._inherit_alpha)
		instance.slice9 = self._slice9.proto()
		instance.outerBounds.extend(self._outerBounds)
		instance.innerRadius.extend(self._innerRadius)
		instance.perimeterVertices.extend(self._perimeterVertices)
		instance.pieFillAngle.extend(self._pieFillAngle)
		instance.clipping_mode.extend(self._clipping_mode)
		instance.clipping_visible.extend(self._clipping_visible)
		instance.clipping_inverted.extend(self._clipping_inverted)
		instance.alpha.extend(self._alpha)
		instance.outline_alpha.extend(self._outline_alpha)
		instance.shadow_alpha.extend(self._shadow_alpha)
		instance.overridden_fields = self._overridden_fields
		instance.template.extend(self._template)
		instance.template_node_child.extend(self._template_node_child)
		instance.text_leading.extend(self._text_leading)
		instance.text_tracking.extend(self._text_tracking)
		instance.size_mode.extend(self._size_mode)
		instance.spine_scene.extend(self._spine_scene)
		instance.spine_default_animation.extend(self._spine_default_animation)
		instance.spine_skin.extend(self._spine_skin)
		instance.spine_node_child.extend(self._spine_node_child)
		instance.particlefx.extend(self._particlefx)
		instance.custom_type.extend(self._custom_type)
		instance.enabled.extend(self._enabled)
		instance.visible.extend(self._visible)
		instance.material.extend(self._material)

	def getsize(self) -> Vector4 :
		return self._size

	def setsize(self,value : Vector4) :
		if self._size != value:
			self._size = value
			self.sizeChanged.emit(value)

	size = pyqtProperty(QObject, fget=getsize, fset=setsize, notify=sizeChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.position = self._position.proto()
		instance.rotation = self._rotation.proto()
		instance.scale = self._scale.proto()
		instance.size = self._size.proto()
		instance.color = self._color.proto()
		instance.type.extend(self._type)
		instance.blend_mode.extend(self._blend_mode)
		instance.text.extend(self._text)
		instance.texture.extend(self._texture)
		instance.font.extend(self._font)
		instance.id.extend(self._id)
		instance.xanchor.extend(self._xanchor)
		instance.yanchor.extend(self._yanchor)
		instance.pivot.extend(self._pivot)
		instance.outline = self._outline.proto()
		instance.shadow = self._shadow.proto()
		instance.adjust_mode.extend(self._adjust_mode)
		instance.line_break.extend(self._line_break)
		instance.parent.extend(self._parent)
		instance.layer.extend(self._layer)
		instance.inherit_alpha.extend(self._inherit_alpha)
		instance.slice9 = self._slice9.proto()
		instance.outerBounds.extend(self._outerBounds)
		instance.innerRadius.extend(self._innerRadius)
		instance.perimeterVertices.extend(self._perimeterVertices)
		instance.pieFillAngle.extend(self._pieFillAngle)
		instance.clipping_mode.extend(self._clipping_mode)
		instance.clipping_visible.extend(self._clipping_visible)
		instance.clipping_inverted.extend(self._clipping_inverted)
		instance.alpha.extend(self._alpha)
		instance.outline_alpha.extend(self._outline_alpha)
		instance.shadow_alpha.extend(self._shadow_alpha)
		instance.overridden_fields = self._overridden_fields
		instance.template.extend(self._template)
		instance.template_node_child.extend(self._template_node_child)
		instance.text_leading.extend(self._text_leading)
		instance.text_tracking.extend(self._text_tracking)
		instance.size_mode.extend(self._size_mode)
		instance.spine_scene.extend(self._spine_scene)
		instance.spine_default_animation.extend(self._spine_default_animation)
		instance.spine_skin.extend(self._spine_skin)
		instance.spine_node_child.extend(self._spine_node_child)
		instance.particlefx.extend(self._particlefx)
		instance.custom_type.extend(self._custom_type)
		instance.enabled.extend(self._enabled)
		instance.visible.extend(self._visible)
		instance.material.extend(self._material)

	def getcolor(self) -> Vector4One :
		return self._color

	def setcolor(self,value : Vector4One) :
		if self._color != value:
			self._color = value
			self.colorChanged.emit(value)

	color = pyqtProperty(QObject, fget=getcolor, fset=setcolor, notify=colorChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.position = self._position.proto()
		instance.rotation = self._rotation.proto()
		instance.scale = self._scale.proto()
		instance.size = self._size.proto()
		instance.color = self._color.proto()
		instance.type.extend(self._type)
		instance.blend_mode.extend(self._blend_mode)
		instance.text.extend(self._text)
		instance.texture.extend(self._texture)
		instance.font.extend(self._font)
		instance.id.extend(self._id)
		instance.xanchor.extend(self._xanchor)
		instance.yanchor.extend(self._yanchor)
		instance.pivot.extend(self._pivot)
		instance.outline = self._outline.proto()
		instance.shadow = self._shadow.proto()
		instance.adjust_mode.extend(self._adjust_mode)
		instance.line_break.extend(self._line_break)
		instance.parent.extend(self._parent)
		instance.layer.extend(self._layer)
		instance.inherit_alpha.extend(self._inherit_alpha)
		instance.slice9 = self._slice9.proto()
		instance.outerBounds.extend(self._outerBounds)
		instance.innerRadius.extend(self._innerRadius)
		instance.perimeterVertices.extend(self._perimeterVertices)
		instance.pieFillAngle.extend(self._pieFillAngle)
		instance.clipping_mode.extend(self._clipping_mode)
		instance.clipping_visible.extend(self._clipping_visible)
		instance.clipping_inverted.extend(self._clipping_inverted)
		instance.alpha.extend(self._alpha)
		instance.outline_alpha.extend(self._outline_alpha)
		instance.shadow_alpha.extend(self._shadow_alpha)
		instance.overridden_fields = self._overridden_fields
		instance.template.extend(self._template)
		instance.template_node_child.extend(self._template_node_child)
		instance.text_leading.extend(self._text_leading)
		instance.text_tracking.extend(self._text_tracking)
		instance.size_mode.extend(self._size_mode)
		instance.spine_scene.extend(self._spine_scene)
		instance.spine_default_animation.extend(self._spine_default_animation)
		instance.spine_skin.extend(self._spine_skin)
		instance.spine_node_child.extend(self._spine_node_child)
		instance.particlefx.extend(self._particlefx)
		instance.custom_type.extend(self._custom_type)
		instance.enabled.extend(self._enabled)
		instance.visible.extend(self._visible)
		instance.material.extend(self._material)

	def gettype(self) -> int :
		return self._type

	def settype(self,value : int) :
		if self._type != value:
			self._type = value
			self.typeChanged.emit(value)

	type = pyqtProperty(int, fget=gettype, fset=settype, notify=typeChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.position = self._position.proto()
		instance.rotation = self._rotation.proto()
		instance.scale = self._scale.proto()
		instance.size = self._size.proto()
		instance.color = self._color.proto()
		instance.type.extend(self._type)
		instance.blend_mode.extend(self._blend_mode)
		instance.text.extend(self._text)
		instance.texture.extend(self._texture)
		instance.font.extend(self._font)
		instance.id.extend(self._id)
		instance.xanchor.extend(self._xanchor)
		instance.yanchor.extend(self._yanchor)
		instance.pivot.extend(self._pivot)
		instance.outline = self._outline.proto()
		instance.shadow = self._shadow.proto()
		instance.adjust_mode.extend(self._adjust_mode)
		instance.line_break.extend(self._line_break)
		instance.parent.extend(self._parent)
		instance.layer.extend(self._layer)
		instance.inherit_alpha.extend(self._inherit_alpha)
		instance.slice9 = self._slice9.proto()
		instance.outerBounds.extend(self._outerBounds)
		instance.innerRadius.extend(self._innerRadius)
		instance.perimeterVertices.extend(self._perimeterVertices)
		instance.pieFillAngle.extend(self._pieFillAngle)
		instance.clipping_mode.extend(self._clipping_mode)
		instance.clipping_visible.extend(self._clipping_visible)
		instance.clipping_inverted.extend(self._clipping_inverted)
		instance.alpha.extend(self._alpha)
		instance.outline_alpha.extend(self._outline_alpha)
		instance.shadow_alpha.extend(self._shadow_alpha)
		instance.overridden_fields = self._overridden_fields
		instance.template.extend(self._template)
		instance.template_node_child.extend(self._template_node_child)
		instance.text_leading.extend(self._text_leading)
		instance.text_tracking.extend(self._text_tracking)
		instance.size_mode.extend(self._size_mode)
		instance.spine_scene.extend(self._spine_scene)
		instance.spine_default_animation.extend(self._spine_default_animation)
		instance.spine_skin.extend(self._spine_skin)
		instance.spine_node_child.extend(self._spine_node_child)
		instance.particlefx.extend(self._particlefx)
		instance.custom_type.extend(self._custom_type)
		instance.enabled.extend(self._enabled)
		instance.visible.extend(self._visible)
		instance.material.extend(self._material)

	def getblend_mode(self) -> int :
		return self._blend_mode

	def setblend_mode(self,value : int) :
		if self._blend_mode != value:
			self._blend_mode = value
			self.blend_modeChanged.emit(value)

	blend_mode = pyqtProperty(int, fget=getblend_mode, fset=setblend_mode, notify=blend_modeChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.position = self._position.proto()
		instance.rotation = self._rotation.proto()
		instance.scale = self._scale.proto()
		instance.size = self._size.proto()
		instance.color = self._color.proto()
		instance.type.extend(self._type)
		instance.blend_mode.extend(self._blend_mode)
		instance.text.extend(self._text)
		instance.texture.extend(self._texture)
		instance.font.extend(self._font)
		instance.id.extend(self._id)
		instance.xanchor.extend(self._xanchor)
		instance.yanchor.extend(self._yanchor)
		instance.pivot.extend(self._pivot)
		instance.outline = self._outline.proto()
		instance.shadow = self._shadow.proto()
		instance.adjust_mode.extend(self._adjust_mode)
		instance.line_break.extend(self._line_break)
		instance.parent.extend(self._parent)
		instance.layer.extend(self._layer)
		instance.inherit_alpha.extend(self._inherit_alpha)
		instance.slice9 = self._slice9.proto()
		instance.outerBounds.extend(self._outerBounds)
		instance.innerRadius.extend(self._innerRadius)
		instance.perimeterVertices.extend(self._perimeterVertices)
		instance.pieFillAngle.extend(self._pieFillAngle)
		instance.clipping_mode.extend(self._clipping_mode)
		instance.clipping_visible.extend(self._clipping_visible)
		instance.clipping_inverted.extend(self._clipping_inverted)
		instance.alpha.extend(self._alpha)
		instance.outline_alpha.extend(self._outline_alpha)
		instance.shadow_alpha.extend(self._shadow_alpha)
		instance.overridden_fields = self._overridden_fields
		instance.template.extend(self._template)
		instance.template_node_child.extend(self._template_node_child)
		instance.text_leading.extend(self._text_leading)
		instance.text_tracking.extend(self._text_tracking)
		instance.size_mode.extend(self._size_mode)
		instance.spine_scene.extend(self._spine_scene)
		instance.spine_default_animation.extend(self._spine_default_animation)
		instance.spine_skin.extend(self._spine_skin)
		instance.spine_node_child.extend(self._spine_node_child)
		instance.particlefx.extend(self._particlefx)
		instance.custom_type.extend(self._custom_type)
		instance.enabled.extend(self._enabled)
		instance.visible.extend(self._visible)
		instance.material.extend(self._material)

	def gettext(self) -> str :
		return self._text

	def settext(self,value : str) :
		if self._text != value:
			self._text = value
			self.textChanged.emit(value)

	text = pyqtProperty(str, fget=gettext, fset=settext, notify=textChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.position = self._position.proto()
		instance.rotation = self._rotation.proto()
		instance.scale = self._scale.proto()
		instance.size = self._size.proto()
		instance.color = self._color.proto()
		instance.type.extend(self._type)
		instance.blend_mode.extend(self._blend_mode)
		instance.text.extend(self._text)
		instance.texture.extend(self._texture)
		instance.font.extend(self._font)
		instance.id.extend(self._id)
		instance.xanchor.extend(self._xanchor)
		instance.yanchor.extend(self._yanchor)
		instance.pivot.extend(self._pivot)
		instance.outline = self._outline.proto()
		instance.shadow = self._shadow.proto()
		instance.adjust_mode.extend(self._adjust_mode)
		instance.line_break.extend(self._line_break)
		instance.parent.extend(self._parent)
		instance.layer.extend(self._layer)
		instance.inherit_alpha.extend(self._inherit_alpha)
		instance.slice9 = self._slice9.proto()
		instance.outerBounds.extend(self._outerBounds)
		instance.innerRadius.extend(self._innerRadius)
		instance.perimeterVertices.extend(self._perimeterVertices)
		instance.pieFillAngle.extend(self._pieFillAngle)
		instance.clipping_mode.extend(self._clipping_mode)
		instance.clipping_visible.extend(self._clipping_visible)
		instance.clipping_inverted.extend(self._clipping_inverted)
		instance.alpha.extend(self._alpha)
		instance.outline_alpha.extend(self._outline_alpha)
		instance.shadow_alpha.extend(self._shadow_alpha)
		instance.overridden_fields = self._overridden_fields
		instance.template.extend(self._template)
		instance.template_node_child.extend(self._template_node_child)
		instance.text_leading.extend(self._text_leading)
		instance.text_tracking.extend(self._text_tracking)
		instance.size_mode.extend(self._size_mode)
		instance.spine_scene.extend(self._spine_scene)
		instance.spine_default_animation.extend(self._spine_default_animation)
		instance.spine_skin.extend(self._spine_skin)
		instance.spine_node_child.extend(self._spine_node_child)
		instance.particlefx.extend(self._particlefx)
		instance.custom_type.extend(self._custom_type)
		instance.enabled.extend(self._enabled)
		instance.visible.extend(self._visible)
		instance.material.extend(self._material)

	def gettexture(self) -> str :
		return self._texture

	def settexture(self,value : str) :
		if self._texture != value:
			self._texture = value
			self.textureChanged.emit(value)

	texture = pyqtProperty(str, fget=gettexture, fset=settexture, notify=textureChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.position = self._position.proto()
		instance.rotation = self._rotation.proto()
		instance.scale = self._scale.proto()
		instance.size = self._size.proto()
		instance.color = self._color.proto()
		instance.type.extend(self._type)
		instance.blend_mode.extend(self._blend_mode)
		instance.text.extend(self._text)
		instance.texture.extend(self._texture)
		instance.font.extend(self._font)
		instance.id.extend(self._id)
		instance.xanchor.extend(self._xanchor)
		instance.yanchor.extend(self._yanchor)
		instance.pivot.extend(self._pivot)
		instance.outline = self._outline.proto()
		instance.shadow = self._shadow.proto()
		instance.adjust_mode.extend(self._adjust_mode)
		instance.line_break.extend(self._line_break)
		instance.parent.extend(self._parent)
		instance.layer.extend(self._layer)
		instance.inherit_alpha.extend(self._inherit_alpha)
		instance.slice9 = self._slice9.proto()
		instance.outerBounds.extend(self._outerBounds)
		instance.innerRadius.extend(self._innerRadius)
		instance.perimeterVertices.extend(self._perimeterVertices)
		instance.pieFillAngle.extend(self._pieFillAngle)
		instance.clipping_mode.extend(self._clipping_mode)
		instance.clipping_visible.extend(self._clipping_visible)
		instance.clipping_inverted.extend(self._clipping_inverted)
		instance.alpha.extend(self._alpha)
		instance.outline_alpha.extend(self._outline_alpha)
		instance.shadow_alpha.extend(self._shadow_alpha)
		instance.overridden_fields = self._overridden_fields
		instance.template.extend(self._template)
		instance.template_node_child.extend(self._template_node_child)
		instance.text_leading.extend(self._text_leading)
		instance.text_tracking.extend(self._text_tracking)
		instance.size_mode.extend(self._size_mode)
		instance.spine_scene.extend(self._spine_scene)
		instance.spine_default_animation.extend(self._spine_default_animation)
		instance.spine_skin.extend(self._spine_skin)
		instance.spine_node_child.extend(self._spine_node_child)
		instance.particlefx.extend(self._particlefx)
		instance.custom_type.extend(self._custom_type)
		instance.enabled.extend(self._enabled)
		instance.visible.extend(self._visible)
		instance.material.extend(self._material)

	def getfont(self) -> str :
		return self._font

	def setfont(self,value : str) :
		if self._font != value:
			self._font = value
			self.fontChanged.emit(value)

	font = pyqtProperty(str, fget=getfont, fset=setfont, notify=fontChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.position = self._position.proto()
		instance.rotation = self._rotation.proto()
		instance.scale = self._scale.proto()
		instance.size = self._size.proto()
		instance.color = self._color.proto()
		instance.type.extend(self._type)
		instance.blend_mode.extend(self._blend_mode)
		instance.text.extend(self._text)
		instance.texture.extend(self._texture)
		instance.font.extend(self._font)
		instance.id.extend(self._id)
		instance.xanchor.extend(self._xanchor)
		instance.yanchor.extend(self._yanchor)
		instance.pivot.extend(self._pivot)
		instance.outline = self._outline.proto()
		instance.shadow = self._shadow.proto()
		instance.adjust_mode.extend(self._adjust_mode)
		instance.line_break.extend(self._line_break)
		instance.parent.extend(self._parent)
		instance.layer.extend(self._layer)
		instance.inherit_alpha.extend(self._inherit_alpha)
		instance.slice9 = self._slice9.proto()
		instance.outerBounds.extend(self._outerBounds)
		instance.innerRadius.extend(self._innerRadius)
		instance.perimeterVertices.extend(self._perimeterVertices)
		instance.pieFillAngle.extend(self._pieFillAngle)
		instance.clipping_mode.extend(self._clipping_mode)
		instance.clipping_visible.extend(self._clipping_visible)
		instance.clipping_inverted.extend(self._clipping_inverted)
		instance.alpha.extend(self._alpha)
		instance.outline_alpha.extend(self._outline_alpha)
		instance.shadow_alpha.extend(self._shadow_alpha)
		instance.overridden_fields = self._overridden_fields
		instance.template.extend(self._template)
		instance.template_node_child.extend(self._template_node_child)
		instance.text_leading.extend(self._text_leading)
		instance.text_tracking.extend(self._text_tracking)
		instance.size_mode.extend(self._size_mode)
		instance.spine_scene.extend(self._spine_scene)
		instance.spine_default_animation.extend(self._spine_default_animation)
		instance.spine_skin.extend(self._spine_skin)
		instance.spine_node_child.extend(self._spine_node_child)
		instance.particlefx.extend(self._particlefx)
		instance.custom_type.extend(self._custom_type)
		instance.enabled.extend(self._enabled)
		instance.visible.extend(self._visible)
		instance.material.extend(self._material)

	def getid(self) -> str :
		return self._id

	def setid(self,value : str) :
		if self._id != value:
			self._id = value
			self.idChanged.emit(value)

	id = pyqtProperty(str, fget=getid, fset=setid, notify=idChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.position = self._position.proto()
		instance.rotation = self._rotation.proto()
		instance.scale = self._scale.proto()
		instance.size = self._size.proto()
		instance.color = self._color.proto()
		instance.type.extend(self._type)
		instance.blend_mode.extend(self._blend_mode)
		instance.text.extend(self._text)
		instance.texture.extend(self._texture)
		instance.font.extend(self._font)
		instance.id.extend(self._id)
		instance.xanchor.extend(self._xanchor)
		instance.yanchor.extend(self._yanchor)
		instance.pivot.extend(self._pivot)
		instance.outline = self._outline.proto()
		instance.shadow = self._shadow.proto()
		instance.adjust_mode.extend(self._adjust_mode)
		instance.line_break.extend(self._line_break)
		instance.parent.extend(self._parent)
		instance.layer.extend(self._layer)
		instance.inherit_alpha.extend(self._inherit_alpha)
		instance.slice9 = self._slice9.proto()
		instance.outerBounds.extend(self._outerBounds)
		instance.innerRadius.extend(self._innerRadius)
		instance.perimeterVertices.extend(self._perimeterVertices)
		instance.pieFillAngle.extend(self._pieFillAngle)
		instance.clipping_mode.extend(self._clipping_mode)
		instance.clipping_visible.extend(self._clipping_visible)
		instance.clipping_inverted.extend(self._clipping_inverted)
		instance.alpha.extend(self._alpha)
		instance.outline_alpha.extend(self._outline_alpha)
		instance.shadow_alpha.extend(self._shadow_alpha)
		instance.overridden_fields = self._overridden_fields
		instance.template.extend(self._template)
		instance.template_node_child.extend(self._template_node_child)
		instance.text_leading.extend(self._text_leading)
		instance.text_tracking.extend(self._text_tracking)
		instance.size_mode.extend(self._size_mode)
		instance.spine_scene.extend(self._spine_scene)
		instance.spine_default_animation.extend(self._spine_default_animation)
		instance.spine_skin.extend(self._spine_skin)
		instance.spine_node_child.extend(self._spine_node_child)
		instance.particlefx.extend(self._particlefx)
		instance.custom_type.extend(self._custom_type)
		instance.enabled.extend(self._enabled)
		instance.visible.extend(self._visible)
		instance.material.extend(self._material)

	def getxanchor(self) -> int :
		return self._xanchor

	def setxanchor(self,value : int) :
		if self._xanchor != value:
			self._xanchor = value
			self.xanchorChanged.emit(value)

	xanchor = pyqtProperty(int, fget=getxanchor, fset=setxanchor, notify=xanchorChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.position = self._position.proto()
		instance.rotation = self._rotation.proto()
		instance.scale = self._scale.proto()
		instance.size = self._size.proto()
		instance.color = self._color.proto()
		instance.type.extend(self._type)
		instance.blend_mode.extend(self._blend_mode)
		instance.text.extend(self._text)
		instance.texture.extend(self._texture)
		instance.font.extend(self._font)
		instance.id.extend(self._id)
		instance.xanchor.extend(self._xanchor)
		instance.yanchor.extend(self._yanchor)
		instance.pivot.extend(self._pivot)
		instance.outline = self._outline.proto()
		instance.shadow = self._shadow.proto()
		instance.adjust_mode.extend(self._adjust_mode)
		instance.line_break.extend(self._line_break)
		instance.parent.extend(self._parent)
		instance.layer.extend(self._layer)
		instance.inherit_alpha.extend(self._inherit_alpha)
		instance.slice9 = self._slice9.proto()
		instance.outerBounds.extend(self._outerBounds)
		instance.innerRadius.extend(self._innerRadius)
		instance.perimeterVertices.extend(self._perimeterVertices)
		instance.pieFillAngle.extend(self._pieFillAngle)
		instance.clipping_mode.extend(self._clipping_mode)
		instance.clipping_visible.extend(self._clipping_visible)
		instance.clipping_inverted.extend(self._clipping_inverted)
		instance.alpha.extend(self._alpha)
		instance.outline_alpha.extend(self._outline_alpha)
		instance.shadow_alpha.extend(self._shadow_alpha)
		instance.overridden_fields = self._overridden_fields
		instance.template.extend(self._template)
		instance.template_node_child.extend(self._template_node_child)
		instance.text_leading.extend(self._text_leading)
		instance.text_tracking.extend(self._text_tracking)
		instance.size_mode.extend(self._size_mode)
		instance.spine_scene.extend(self._spine_scene)
		instance.spine_default_animation.extend(self._spine_default_animation)
		instance.spine_skin.extend(self._spine_skin)
		instance.spine_node_child.extend(self._spine_node_child)
		instance.particlefx.extend(self._particlefx)
		instance.custom_type.extend(self._custom_type)
		instance.enabled.extend(self._enabled)
		instance.visible.extend(self._visible)
		instance.material.extend(self._material)

	def getyanchor(self) -> int :
		return self._yanchor

	def setyanchor(self,value : int) :
		if self._yanchor != value:
			self._yanchor = value
			self.yanchorChanged.emit(value)

	yanchor = pyqtProperty(int, fget=getyanchor, fset=setyanchor, notify=yanchorChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.position = self._position.proto()
		instance.rotation = self._rotation.proto()
		instance.scale = self._scale.proto()
		instance.size = self._size.proto()
		instance.color = self._color.proto()
		instance.type.extend(self._type)
		instance.blend_mode.extend(self._blend_mode)
		instance.text.extend(self._text)
		instance.texture.extend(self._texture)
		instance.font.extend(self._font)
		instance.id.extend(self._id)
		instance.xanchor.extend(self._xanchor)
		instance.yanchor.extend(self._yanchor)
		instance.pivot.extend(self._pivot)
		instance.outline = self._outline.proto()
		instance.shadow = self._shadow.proto()
		instance.adjust_mode.extend(self._adjust_mode)
		instance.line_break.extend(self._line_break)
		instance.parent.extend(self._parent)
		instance.layer.extend(self._layer)
		instance.inherit_alpha.extend(self._inherit_alpha)
		instance.slice9 = self._slice9.proto()
		instance.outerBounds.extend(self._outerBounds)
		instance.innerRadius.extend(self._innerRadius)
		instance.perimeterVertices.extend(self._perimeterVertices)
		instance.pieFillAngle.extend(self._pieFillAngle)
		instance.clipping_mode.extend(self._clipping_mode)
		instance.clipping_visible.extend(self._clipping_visible)
		instance.clipping_inverted.extend(self._clipping_inverted)
		instance.alpha.extend(self._alpha)
		instance.outline_alpha.extend(self._outline_alpha)
		instance.shadow_alpha.extend(self._shadow_alpha)
		instance.overridden_fields = self._overridden_fields
		instance.template.extend(self._template)
		instance.template_node_child.extend(self._template_node_child)
		instance.text_leading.extend(self._text_leading)
		instance.text_tracking.extend(self._text_tracking)
		instance.size_mode.extend(self._size_mode)
		instance.spine_scene.extend(self._spine_scene)
		instance.spine_default_animation.extend(self._spine_default_animation)
		instance.spine_skin.extend(self._spine_skin)
		instance.spine_node_child.extend(self._spine_node_child)
		instance.particlefx.extend(self._particlefx)
		instance.custom_type.extend(self._custom_type)
		instance.enabled.extend(self._enabled)
		instance.visible.extend(self._visible)
		instance.material.extend(self._material)

	def getpivot(self) -> int :
		return self._pivot

	def setpivot(self,value : int) :
		if self._pivot != value:
			self._pivot = value
			self.pivotChanged.emit(value)

	pivot = pyqtProperty(int, fget=getpivot, fset=setpivot, notify=pivotChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.position = self._position.proto()
		instance.rotation = self._rotation.proto()
		instance.scale = self._scale.proto()
		instance.size = self._size.proto()
		instance.color = self._color.proto()
		instance.type.extend(self._type)
		instance.blend_mode.extend(self._blend_mode)
		instance.text.extend(self._text)
		instance.texture.extend(self._texture)
		instance.font.extend(self._font)
		instance.id.extend(self._id)
		instance.xanchor.extend(self._xanchor)
		instance.yanchor.extend(self._yanchor)
		instance.pivot.extend(self._pivot)
		instance.outline = self._outline.proto()
		instance.shadow = self._shadow.proto()
		instance.adjust_mode.extend(self._adjust_mode)
		instance.line_break.extend(self._line_break)
		instance.parent.extend(self._parent)
		instance.layer.extend(self._layer)
		instance.inherit_alpha.extend(self._inherit_alpha)
		instance.slice9 = self._slice9.proto()
		instance.outerBounds.extend(self._outerBounds)
		instance.innerRadius.extend(self._innerRadius)
		instance.perimeterVertices.extend(self._perimeterVertices)
		instance.pieFillAngle.extend(self._pieFillAngle)
		instance.clipping_mode.extend(self._clipping_mode)
		instance.clipping_visible.extend(self._clipping_visible)
		instance.clipping_inverted.extend(self._clipping_inverted)
		instance.alpha.extend(self._alpha)
		instance.outline_alpha.extend(self._outline_alpha)
		instance.shadow_alpha.extend(self._shadow_alpha)
		instance.overridden_fields = self._overridden_fields
		instance.template.extend(self._template)
		instance.template_node_child.extend(self._template_node_child)
		instance.text_leading.extend(self._text_leading)
		instance.text_tracking.extend(self._text_tracking)
		instance.size_mode.extend(self._size_mode)
		instance.spine_scene.extend(self._spine_scene)
		instance.spine_default_animation.extend(self._spine_default_animation)
		instance.spine_skin.extend(self._spine_skin)
		instance.spine_node_child.extend(self._spine_node_child)
		instance.particlefx.extend(self._particlefx)
		instance.custom_type.extend(self._custom_type)
		instance.enabled.extend(self._enabled)
		instance.visible.extend(self._visible)
		instance.material.extend(self._material)

	def getoutline(self) -> Vector4WOne :
		return self._outline

	def setoutline(self,value : Vector4WOne) :
		if self._outline != value:
			self._outline = value
			self.outlineChanged.emit(value)

	outline = pyqtProperty(QObject, fget=getoutline, fset=setoutline, notify=outlineChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.position = self._position.proto()
		instance.rotation = self._rotation.proto()
		instance.scale = self._scale.proto()
		instance.size = self._size.proto()
		instance.color = self._color.proto()
		instance.type.extend(self._type)
		instance.blend_mode.extend(self._blend_mode)
		instance.text.extend(self._text)
		instance.texture.extend(self._texture)
		instance.font.extend(self._font)
		instance.id.extend(self._id)
		instance.xanchor.extend(self._xanchor)
		instance.yanchor.extend(self._yanchor)
		instance.pivot.extend(self._pivot)
		instance.outline = self._outline.proto()
		instance.shadow = self._shadow.proto()
		instance.adjust_mode.extend(self._adjust_mode)
		instance.line_break.extend(self._line_break)
		instance.parent.extend(self._parent)
		instance.layer.extend(self._layer)
		instance.inherit_alpha.extend(self._inherit_alpha)
		instance.slice9 = self._slice9.proto()
		instance.outerBounds.extend(self._outerBounds)
		instance.innerRadius.extend(self._innerRadius)
		instance.perimeterVertices.extend(self._perimeterVertices)
		instance.pieFillAngle.extend(self._pieFillAngle)
		instance.clipping_mode.extend(self._clipping_mode)
		instance.clipping_visible.extend(self._clipping_visible)
		instance.clipping_inverted.extend(self._clipping_inverted)
		instance.alpha.extend(self._alpha)
		instance.outline_alpha.extend(self._outline_alpha)
		instance.shadow_alpha.extend(self._shadow_alpha)
		instance.overridden_fields = self._overridden_fields
		instance.template.extend(self._template)
		instance.template_node_child.extend(self._template_node_child)
		instance.text_leading.extend(self._text_leading)
		instance.text_tracking.extend(self._text_tracking)
		instance.size_mode.extend(self._size_mode)
		instance.spine_scene.extend(self._spine_scene)
		instance.spine_default_animation.extend(self._spine_default_animation)
		instance.spine_skin.extend(self._spine_skin)
		instance.spine_node_child.extend(self._spine_node_child)
		instance.particlefx.extend(self._particlefx)
		instance.custom_type.extend(self._custom_type)
		instance.enabled.extend(self._enabled)
		instance.visible.extend(self._visible)
		instance.material.extend(self._material)

	def getshadow(self) -> Vector4WOne :
		return self._shadow

	def setshadow(self,value : Vector4WOne) :
		if self._shadow != value:
			self._shadow = value
			self.shadowChanged.emit(value)

	shadow = pyqtProperty(QObject, fget=getshadow, fset=setshadow, notify=shadowChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.position = self._position.proto()
		instance.rotation = self._rotation.proto()
		instance.scale = self._scale.proto()
		instance.size = self._size.proto()
		instance.color = self._color.proto()
		instance.type.extend(self._type)
		instance.blend_mode.extend(self._blend_mode)
		instance.text.extend(self._text)
		instance.texture.extend(self._texture)
		instance.font.extend(self._font)
		instance.id.extend(self._id)
		instance.xanchor.extend(self._xanchor)
		instance.yanchor.extend(self._yanchor)
		instance.pivot.extend(self._pivot)
		instance.outline = self._outline.proto()
		instance.shadow = self._shadow.proto()
		instance.adjust_mode.extend(self._adjust_mode)
		instance.line_break.extend(self._line_break)
		instance.parent.extend(self._parent)
		instance.layer.extend(self._layer)
		instance.inherit_alpha.extend(self._inherit_alpha)
		instance.slice9 = self._slice9.proto()
		instance.outerBounds.extend(self._outerBounds)
		instance.innerRadius.extend(self._innerRadius)
		instance.perimeterVertices.extend(self._perimeterVertices)
		instance.pieFillAngle.extend(self._pieFillAngle)
		instance.clipping_mode.extend(self._clipping_mode)
		instance.clipping_visible.extend(self._clipping_visible)
		instance.clipping_inverted.extend(self._clipping_inverted)
		instance.alpha.extend(self._alpha)
		instance.outline_alpha.extend(self._outline_alpha)
		instance.shadow_alpha.extend(self._shadow_alpha)
		instance.overridden_fields = self._overridden_fields
		instance.template.extend(self._template)
		instance.template_node_child.extend(self._template_node_child)
		instance.text_leading.extend(self._text_leading)
		instance.text_tracking.extend(self._text_tracking)
		instance.size_mode.extend(self._size_mode)
		instance.spine_scene.extend(self._spine_scene)
		instance.spine_default_animation.extend(self._spine_default_animation)
		instance.spine_skin.extend(self._spine_skin)
		instance.spine_node_child.extend(self._spine_node_child)
		instance.particlefx.extend(self._particlefx)
		instance.custom_type.extend(self._custom_type)
		instance.enabled.extend(self._enabled)
		instance.visible.extend(self._visible)
		instance.material.extend(self._material)

	def getadjust_mode(self) -> int :
		return self._adjust_mode

	def setadjust_mode(self,value : int) :
		if self._adjust_mode != value:
			self._adjust_mode = value
			self.adjust_modeChanged.emit(value)

	adjust_mode = pyqtProperty(int, fget=getadjust_mode, fset=setadjust_mode, notify=adjust_modeChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.position = self._position.proto()
		instance.rotation = self._rotation.proto()
		instance.scale = self._scale.proto()
		instance.size = self._size.proto()
		instance.color = self._color.proto()
		instance.type.extend(self._type)
		instance.blend_mode.extend(self._blend_mode)
		instance.text.extend(self._text)
		instance.texture.extend(self._texture)
		instance.font.extend(self._font)
		instance.id.extend(self._id)
		instance.xanchor.extend(self._xanchor)
		instance.yanchor.extend(self._yanchor)
		instance.pivot.extend(self._pivot)
		instance.outline = self._outline.proto()
		instance.shadow = self._shadow.proto()
		instance.adjust_mode.extend(self._adjust_mode)
		instance.line_break.extend(self._line_break)
		instance.parent.extend(self._parent)
		instance.layer.extend(self._layer)
		instance.inherit_alpha.extend(self._inherit_alpha)
		instance.slice9 = self._slice9.proto()
		instance.outerBounds.extend(self._outerBounds)
		instance.innerRadius.extend(self._innerRadius)
		instance.perimeterVertices.extend(self._perimeterVertices)
		instance.pieFillAngle.extend(self._pieFillAngle)
		instance.clipping_mode.extend(self._clipping_mode)
		instance.clipping_visible.extend(self._clipping_visible)
		instance.clipping_inverted.extend(self._clipping_inverted)
		instance.alpha.extend(self._alpha)
		instance.outline_alpha.extend(self._outline_alpha)
		instance.shadow_alpha.extend(self._shadow_alpha)
		instance.overridden_fields = self._overridden_fields
		instance.template.extend(self._template)
		instance.template_node_child.extend(self._template_node_child)
		instance.text_leading.extend(self._text_leading)
		instance.text_tracking.extend(self._text_tracking)
		instance.size_mode.extend(self._size_mode)
		instance.spine_scene.extend(self._spine_scene)
		instance.spine_default_animation.extend(self._spine_default_animation)
		instance.spine_skin.extend(self._spine_skin)
		instance.spine_node_child.extend(self._spine_node_child)
		instance.particlefx.extend(self._particlefx)
		instance.custom_type.extend(self._custom_type)
		instance.enabled.extend(self._enabled)
		instance.visible.extend(self._visible)
		instance.material.extend(self._material)

	def getline_break(self) -> bool :
		return self._line_break

	def setline_break(self,value : bool) :
		if self._line_break != value:
			self._line_break = value
			self.line_breakChanged.emit(value)

	line_break = pyqtProperty(bool, fget=getline_break, fset=setline_break, notify=line_breakChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.position = self._position.proto()
		instance.rotation = self._rotation.proto()
		instance.scale = self._scale.proto()
		instance.size = self._size.proto()
		instance.color = self._color.proto()
		instance.type.extend(self._type)
		instance.blend_mode.extend(self._blend_mode)
		instance.text.extend(self._text)
		instance.texture.extend(self._texture)
		instance.font.extend(self._font)
		instance.id.extend(self._id)
		instance.xanchor.extend(self._xanchor)
		instance.yanchor.extend(self._yanchor)
		instance.pivot.extend(self._pivot)
		instance.outline = self._outline.proto()
		instance.shadow = self._shadow.proto()
		instance.adjust_mode.extend(self._adjust_mode)
		instance.line_break.extend(self._line_break)
		instance.parent.extend(self._parent)
		instance.layer.extend(self._layer)
		instance.inherit_alpha.extend(self._inherit_alpha)
		instance.slice9 = self._slice9.proto()
		instance.outerBounds.extend(self._outerBounds)
		instance.innerRadius.extend(self._innerRadius)
		instance.perimeterVertices.extend(self._perimeterVertices)
		instance.pieFillAngle.extend(self._pieFillAngle)
		instance.clipping_mode.extend(self._clipping_mode)
		instance.clipping_visible.extend(self._clipping_visible)
		instance.clipping_inverted.extend(self._clipping_inverted)
		instance.alpha.extend(self._alpha)
		instance.outline_alpha.extend(self._outline_alpha)
		instance.shadow_alpha.extend(self._shadow_alpha)
		instance.overridden_fields = self._overridden_fields
		instance.template.extend(self._template)
		instance.template_node_child.extend(self._template_node_child)
		instance.text_leading.extend(self._text_leading)
		instance.text_tracking.extend(self._text_tracking)
		instance.size_mode.extend(self._size_mode)
		instance.spine_scene.extend(self._spine_scene)
		instance.spine_default_animation.extend(self._spine_default_animation)
		instance.spine_skin.extend(self._spine_skin)
		instance.spine_node_child.extend(self._spine_node_child)
		instance.particlefx.extend(self._particlefx)
		instance.custom_type.extend(self._custom_type)
		instance.enabled.extend(self._enabled)
		instance.visible.extend(self._visible)
		instance.material.extend(self._material)

	def getparent(self) -> str :
		return self._parent

	def setparent(self,value : str) :
		if self._parent != value:
			self._parent = value
			self.parentChanged.emit(value)

	parent = pyqtProperty(str, fget=getparent, fset=setparent, notify=parentChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.position = self._position.proto()
		instance.rotation = self._rotation.proto()
		instance.scale = self._scale.proto()
		instance.size = self._size.proto()
		instance.color = self._color.proto()
		instance.type.extend(self._type)
		instance.blend_mode.extend(self._blend_mode)
		instance.text.extend(self._text)
		instance.texture.extend(self._texture)
		instance.font.extend(self._font)
		instance.id.extend(self._id)
		instance.xanchor.extend(self._xanchor)
		instance.yanchor.extend(self._yanchor)
		instance.pivot.extend(self._pivot)
		instance.outline = self._outline.proto()
		instance.shadow = self._shadow.proto()
		instance.adjust_mode.extend(self._adjust_mode)
		instance.line_break.extend(self._line_break)
		instance.parent.extend(self._parent)
		instance.layer.extend(self._layer)
		instance.inherit_alpha.extend(self._inherit_alpha)
		instance.slice9 = self._slice9.proto()
		instance.outerBounds.extend(self._outerBounds)
		instance.innerRadius.extend(self._innerRadius)
		instance.perimeterVertices.extend(self._perimeterVertices)
		instance.pieFillAngle.extend(self._pieFillAngle)
		instance.clipping_mode.extend(self._clipping_mode)
		instance.clipping_visible.extend(self._clipping_visible)
		instance.clipping_inverted.extend(self._clipping_inverted)
		instance.alpha.extend(self._alpha)
		instance.outline_alpha.extend(self._outline_alpha)
		instance.shadow_alpha.extend(self._shadow_alpha)
		instance.overridden_fields = self._overridden_fields
		instance.template.extend(self._template)
		instance.template_node_child.extend(self._template_node_child)
		instance.text_leading.extend(self._text_leading)
		instance.text_tracking.extend(self._text_tracking)
		instance.size_mode.extend(self._size_mode)
		instance.spine_scene.extend(self._spine_scene)
		instance.spine_default_animation.extend(self._spine_default_animation)
		instance.spine_skin.extend(self._spine_skin)
		instance.spine_node_child.extend(self._spine_node_child)
		instance.particlefx.extend(self._particlefx)
		instance.custom_type.extend(self._custom_type)
		instance.enabled.extend(self._enabled)
		instance.visible.extend(self._visible)
		instance.material.extend(self._material)

	def getlayer(self) -> str :
		return self._layer

	def setlayer(self,value : str) :
		if self._layer != value:
			self._layer = value
			self.layerChanged.emit(value)

	layer = pyqtProperty(str, fget=getlayer, fset=setlayer, notify=layerChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.position = self._position.proto()
		instance.rotation = self._rotation.proto()
		instance.scale = self._scale.proto()
		instance.size = self._size.proto()
		instance.color = self._color.proto()
		instance.type.extend(self._type)
		instance.blend_mode.extend(self._blend_mode)
		instance.text.extend(self._text)
		instance.texture.extend(self._texture)
		instance.font.extend(self._font)
		instance.id.extend(self._id)
		instance.xanchor.extend(self._xanchor)
		instance.yanchor.extend(self._yanchor)
		instance.pivot.extend(self._pivot)
		instance.outline = self._outline.proto()
		instance.shadow = self._shadow.proto()
		instance.adjust_mode.extend(self._adjust_mode)
		instance.line_break.extend(self._line_break)
		instance.parent.extend(self._parent)
		instance.layer.extend(self._layer)
		instance.inherit_alpha.extend(self._inherit_alpha)
		instance.slice9 = self._slice9.proto()
		instance.outerBounds.extend(self._outerBounds)
		instance.innerRadius.extend(self._innerRadius)
		instance.perimeterVertices.extend(self._perimeterVertices)
		instance.pieFillAngle.extend(self._pieFillAngle)
		instance.clipping_mode.extend(self._clipping_mode)
		instance.clipping_visible.extend(self._clipping_visible)
		instance.clipping_inverted.extend(self._clipping_inverted)
		instance.alpha.extend(self._alpha)
		instance.outline_alpha.extend(self._outline_alpha)
		instance.shadow_alpha.extend(self._shadow_alpha)
		instance.overridden_fields = self._overridden_fields
		instance.template.extend(self._template)
		instance.template_node_child.extend(self._template_node_child)
		instance.text_leading.extend(self._text_leading)
		instance.text_tracking.extend(self._text_tracking)
		instance.size_mode.extend(self._size_mode)
		instance.spine_scene.extend(self._spine_scene)
		instance.spine_default_animation.extend(self._spine_default_animation)
		instance.spine_skin.extend(self._spine_skin)
		instance.spine_node_child.extend(self._spine_node_child)
		instance.particlefx.extend(self._particlefx)
		instance.custom_type.extend(self._custom_type)
		instance.enabled.extend(self._enabled)
		instance.visible.extend(self._visible)
		instance.material.extend(self._material)

	def getinherit_alpha(self) -> bool :
		return self._inherit_alpha

	def setinherit_alpha(self,value : bool) :
		if self._inherit_alpha != value:
			self._inherit_alpha = value
			self.inherit_alphaChanged.emit(value)

	inherit_alpha = pyqtProperty(bool, fget=getinherit_alpha, fset=setinherit_alpha, notify=inherit_alphaChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.position = self._position.proto()
		instance.rotation = self._rotation.proto()
		instance.scale = self._scale.proto()
		instance.size = self._size.proto()
		instance.color = self._color.proto()
		instance.type.extend(self._type)
		instance.blend_mode.extend(self._blend_mode)
		instance.text.extend(self._text)
		instance.texture.extend(self._texture)
		instance.font.extend(self._font)
		instance.id.extend(self._id)
		instance.xanchor.extend(self._xanchor)
		instance.yanchor.extend(self._yanchor)
		instance.pivot.extend(self._pivot)
		instance.outline = self._outline.proto()
		instance.shadow = self._shadow.proto()
		instance.adjust_mode.extend(self._adjust_mode)
		instance.line_break.extend(self._line_break)
		instance.parent.extend(self._parent)
		instance.layer.extend(self._layer)
		instance.inherit_alpha.extend(self._inherit_alpha)
		instance.slice9 = self._slice9.proto()
		instance.outerBounds.extend(self._outerBounds)
		instance.innerRadius.extend(self._innerRadius)
		instance.perimeterVertices.extend(self._perimeterVertices)
		instance.pieFillAngle.extend(self._pieFillAngle)
		instance.clipping_mode.extend(self._clipping_mode)
		instance.clipping_visible.extend(self._clipping_visible)
		instance.clipping_inverted.extend(self._clipping_inverted)
		instance.alpha.extend(self._alpha)
		instance.outline_alpha.extend(self._outline_alpha)
		instance.shadow_alpha.extend(self._shadow_alpha)
		instance.overridden_fields = self._overridden_fields
		instance.template.extend(self._template)
		instance.template_node_child.extend(self._template_node_child)
		instance.text_leading.extend(self._text_leading)
		instance.text_tracking.extend(self._text_tracking)
		instance.size_mode.extend(self._size_mode)
		instance.spine_scene.extend(self._spine_scene)
		instance.spine_default_animation.extend(self._spine_default_animation)
		instance.spine_skin.extend(self._spine_skin)
		instance.spine_node_child.extend(self._spine_node_child)
		instance.particlefx.extend(self._particlefx)
		instance.custom_type.extend(self._custom_type)
		instance.enabled.extend(self._enabled)
		instance.visible.extend(self._visible)
		instance.material.extend(self._material)

	def getslice9(self) -> Vector4 :
		return self._slice9

	def setslice9(self,value : Vector4) :
		if self._slice9 != value:
			self._slice9 = value
			self.slice9Changed.emit(value)

	slice9 = pyqtProperty(QObject, fget=getslice9, fset=setslice9, notify=slice9Changed)

	def proto(self) :
		instance = self.__PROTO__()
		instance.position = self._position.proto()
		instance.rotation = self._rotation.proto()
		instance.scale = self._scale.proto()
		instance.size = self._size.proto()
		instance.color = self._color.proto()
		instance.type.extend(self._type)
		instance.blend_mode.extend(self._blend_mode)
		instance.text.extend(self._text)
		instance.texture.extend(self._texture)
		instance.font.extend(self._font)
		instance.id.extend(self._id)
		instance.xanchor.extend(self._xanchor)
		instance.yanchor.extend(self._yanchor)
		instance.pivot.extend(self._pivot)
		instance.outline = self._outline.proto()
		instance.shadow = self._shadow.proto()
		instance.adjust_mode.extend(self._adjust_mode)
		instance.line_break.extend(self._line_break)
		instance.parent.extend(self._parent)
		instance.layer.extend(self._layer)
		instance.inherit_alpha.extend(self._inherit_alpha)
		instance.slice9 = self._slice9.proto()
		instance.outerBounds.extend(self._outerBounds)
		instance.innerRadius.extend(self._innerRadius)
		instance.perimeterVertices.extend(self._perimeterVertices)
		instance.pieFillAngle.extend(self._pieFillAngle)
		instance.clipping_mode.extend(self._clipping_mode)
		instance.clipping_visible.extend(self._clipping_visible)
		instance.clipping_inverted.extend(self._clipping_inverted)
		instance.alpha.extend(self._alpha)
		instance.outline_alpha.extend(self._outline_alpha)
		instance.shadow_alpha.extend(self._shadow_alpha)
		instance.overridden_fields = self._overridden_fields
		instance.template.extend(self._template)
		instance.template_node_child.extend(self._template_node_child)
		instance.text_leading.extend(self._text_leading)
		instance.text_tracking.extend(self._text_tracking)
		instance.size_mode.extend(self._size_mode)
		instance.spine_scene.extend(self._spine_scene)
		instance.spine_default_animation.extend(self._spine_default_animation)
		instance.spine_skin.extend(self._spine_skin)
		instance.spine_node_child.extend(self._spine_node_child)
		instance.particlefx.extend(self._particlefx)
		instance.custom_type.extend(self._custom_type)
		instance.enabled.extend(self._enabled)
		instance.visible.extend(self._visible)
		instance.material.extend(self._material)

	def getouterBounds(self) -> int :
		return self._outerBounds

	def setouterBounds(self,value : int) :
		if self._outerBounds != value:
			self._outerBounds = value
			self.outerBoundsChanged.emit(value)

	outerBounds = pyqtProperty(int, fget=getouterBounds, fset=setouterBounds, notify=outerBoundsChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.position = self._position.proto()
		instance.rotation = self._rotation.proto()
		instance.scale = self._scale.proto()
		instance.size = self._size.proto()
		instance.color = self._color.proto()
		instance.type.extend(self._type)
		instance.blend_mode.extend(self._blend_mode)
		instance.text.extend(self._text)
		instance.texture.extend(self._texture)
		instance.font.extend(self._font)
		instance.id.extend(self._id)
		instance.xanchor.extend(self._xanchor)
		instance.yanchor.extend(self._yanchor)
		instance.pivot.extend(self._pivot)
		instance.outline = self._outline.proto()
		instance.shadow = self._shadow.proto()
		instance.adjust_mode.extend(self._adjust_mode)
		instance.line_break.extend(self._line_break)
		instance.parent.extend(self._parent)
		instance.layer.extend(self._layer)
		instance.inherit_alpha.extend(self._inherit_alpha)
		instance.slice9 = self._slice9.proto()
		instance.outerBounds.extend(self._outerBounds)
		instance.innerRadius.extend(self._innerRadius)
		instance.perimeterVertices.extend(self._perimeterVertices)
		instance.pieFillAngle.extend(self._pieFillAngle)
		instance.clipping_mode.extend(self._clipping_mode)
		instance.clipping_visible.extend(self._clipping_visible)
		instance.clipping_inverted.extend(self._clipping_inverted)
		instance.alpha.extend(self._alpha)
		instance.outline_alpha.extend(self._outline_alpha)
		instance.shadow_alpha.extend(self._shadow_alpha)
		instance.overridden_fields = self._overridden_fields
		instance.template.extend(self._template)
		instance.template_node_child.extend(self._template_node_child)
		instance.text_leading.extend(self._text_leading)
		instance.text_tracking.extend(self._text_tracking)
		instance.size_mode.extend(self._size_mode)
		instance.spine_scene.extend(self._spine_scene)
		instance.spine_default_animation.extend(self._spine_default_animation)
		instance.spine_skin.extend(self._spine_skin)
		instance.spine_node_child.extend(self._spine_node_child)
		instance.particlefx.extend(self._particlefx)
		instance.custom_type.extend(self._custom_type)
		instance.enabled.extend(self._enabled)
		instance.visible.extend(self._visible)
		instance.material.extend(self._material)

	def getinnerRadius(self) -> float :
		return self._innerRadius

	def setinnerRadius(self,value : float) :
		if self._innerRadius != value:
			self._innerRadius = value
			self.innerRadiusChanged.emit(value)

	innerRadius = pyqtProperty(float, fget=getinnerRadius, fset=setinnerRadius, notify=innerRadiusChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.position = self._position.proto()
		instance.rotation = self._rotation.proto()
		instance.scale = self._scale.proto()
		instance.size = self._size.proto()
		instance.color = self._color.proto()
		instance.type.extend(self._type)
		instance.blend_mode.extend(self._blend_mode)
		instance.text.extend(self._text)
		instance.texture.extend(self._texture)
		instance.font.extend(self._font)
		instance.id.extend(self._id)
		instance.xanchor.extend(self._xanchor)
		instance.yanchor.extend(self._yanchor)
		instance.pivot.extend(self._pivot)
		instance.outline = self._outline.proto()
		instance.shadow = self._shadow.proto()
		instance.adjust_mode.extend(self._adjust_mode)
		instance.line_break.extend(self._line_break)
		instance.parent.extend(self._parent)
		instance.layer.extend(self._layer)
		instance.inherit_alpha.extend(self._inherit_alpha)
		instance.slice9 = self._slice9.proto()
		instance.outerBounds.extend(self._outerBounds)
		instance.innerRadius.extend(self._innerRadius)
		instance.perimeterVertices.extend(self._perimeterVertices)
		instance.pieFillAngle.extend(self._pieFillAngle)
		instance.clipping_mode.extend(self._clipping_mode)
		instance.clipping_visible.extend(self._clipping_visible)
		instance.clipping_inverted.extend(self._clipping_inverted)
		instance.alpha.extend(self._alpha)
		instance.outline_alpha.extend(self._outline_alpha)
		instance.shadow_alpha.extend(self._shadow_alpha)
		instance.overridden_fields = self._overridden_fields
		instance.template.extend(self._template)
		instance.template_node_child.extend(self._template_node_child)
		instance.text_leading.extend(self._text_leading)
		instance.text_tracking.extend(self._text_tracking)
		instance.size_mode.extend(self._size_mode)
		instance.spine_scene.extend(self._spine_scene)
		instance.spine_default_animation.extend(self._spine_default_animation)
		instance.spine_skin.extend(self._spine_skin)
		instance.spine_node_child.extend(self._spine_node_child)
		instance.particlefx.extend(self._particlefx)
		instance.custom_type.extend(self._custom_type)
		instance.enabled.extend(self._enabled)
		instance.visible.extend(self._visible)
		instance.material.extend(self._material)

	def getperimeterVertices(self) -> int :
		return self._perimeterVertices

	def setperimeterVertices(self,value : int) :
		if self._perimeterVertices != value:
			self._perimeterVertices = value
			self.perimeterVerticesChanged.emit(value)

	perimeterVertices = pyqtProperty(int, fget=getperimeterVertices, fset=setperimeterVertices, notify=perimeterVerticesChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.position = self._position.proto()
		instance.rotation = self._rotation.proto()
		instance.scale = self._scale.proto()
		instance.size = self._size.proto()
		instance.color = self._color.proto()
		instance.type.extend(self._type)
		instance.blend_mode.extend(self._blend_mode)
		instance.text.extend(self._text)
		instance.texture.extend(self._texture)
		instance.font.extend(self._font)
		instance.id.extend(self._id)
		instance.xanchor.extend(self._xanchor)
		instance.yanchor.extend(self._yanchor)
		instance.pivot.extend(self._pivot)
		instance.outline = self._outline.proto()
		instance.shadow = self._shadow.proto()
		instance.adjust_mode.extend(self._adjust_mode)
		instance.line_break.extend(self._line_break)
		instance.parent.extend(self._parent)
		instance.layer.extend(self._layer)
		instance.inherit_alpha.extend(self._inherit_alpha)
		instance.slice9 = self._slice9.proto()
		instance.outerBounds.extend(self._outerBounds)
		instance.innerRadius.extend(self._innerRadius)
		instance.perimeterVertices.extend(self._perimeterVertices)
		instance.pieFillAngle.extend(self._pieFillAngle)
		instance.clipping_mode.extend(self._clipping_mode)
		instance.clipping_visible.extend(self._clipping_visible)
		instance.clipping_inverted.extend(self._clipping_inverted)
		instance.alpha.extend(self._alpha)
		instance.outline_alpha.extend(self._outline_alpha)
		instance.shadow_alpha.extend(self._shadow_alpha)
		instance.overridden_fields = self._overridden_fields
		instance.template.extend(self._template)
		instance.template_node_child.extend(self._template_node_child)
		instance.text_leading.extend(self._text_leading)
		instance.text_tracking.extend(self._text_tracking)
		instance.size_mode.extend(self._size_mode)
		instance.spine_scene.extend(self._spine_scene)
		instance.spine_default_animation.extend(self._spine_default_animation)
		instance.spine_skin.extend(self._spine_skin)
		instance.spine_node_child.extend(self._spine_node_child)
		instance.particlefx.extend(self._particlefx)
		instance.custom_type.extend(self._custom_type)
		instance.enabled.extend(self._enabled)
		instance.visible.extend(self._visible)
		instance.material.extend(self._material)

	def getpieFillAngle(self) -> float :
		return self._pieFillAngle

	def setpieFillAngle(self,value : float) :
		if self._pieFillAngle != value:
			self._pieFillAngle = value
			self.pieFillAngleChanged.emit(value)

	pieFillAngle = pyqtProperty(float, fget=getpieFillAngle, fset=setpieFillAngle, notify=pieFillAngleChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.position = self._position.proto()
		instance.rotation = self._rotation.proto()
		instance.scale = self._scale.proto()
		instance.size = self._size.proto()
		instance.color = self._color.proto()
		instance.type.extend(self._type)
		instance.blend_mode.extend(self._blend_mode)
		instance.text.extend(self._text)
		instance.texture.extend(self._texture)
		instance.font.extend(self._font)
		instance.id.extend(self._id)
		instance.xanchor.extend(self._xanchor)
		instance.yanchor.extend(self._yanchor)
		instance.pivot.extend(self._pivot)
		instance.outline = self._outline.proto()
		instance.shadow = self._shadow.proto()
		instance.adjust_mode.extend(self._adjust_mode)
		instance.line_break.extend(self._line_break)
		instance.parent.extend(self._parent)
		instance.layer.extend(self._layer)
		instance.inherit_alpha.extend(self._inherit_alpha)
		instance.slice9 = self._slice9.proto()
		instance.outerBounds.extend(self._outerBounds)
		instance.innerRadius.extend(self._innerRadius)
		instance.perimeterVertices.extend(self._perimeterVertices)
		instance.pieFillAngle.extend(self._pieFillAngle)
		instance.clipping_mode.extend(self._clipping_mode)
		instance.clipping_visible.extend(self._clipping_visible)
		instance.clipping_inverted.extend(self._clipping_inverted)
		instance.alpha.extend(self._alpha)
		instance.outline_alpha.extend(self._outline_alpha)
		instance.shadow_alpha.extend(self._shadow_alpha)
		instance.overridden_fields = self._overridden_fields
		instance.template.extend(self._template)
		instance.template_node_child.extend(self._template_node_child)
		instance.text_leading.extend(self._text_leading)
		instance.text_tracking.extend(self._text_tracking)
		instance.size_mode.extend(self._size_mode)
		instance.spine_scene.extend(self._spine_scene)
		instance.spine_default_animation.extend(self._spine_default_animation)
		instance.spine_skin.extend(self._spine_skin)
		instance.spine_node_child.extend(self._spine_node_child)
		instance.particlefx.extend(self._particlefx)
		instance.custom_type.extend(self._custom_type)
		instance.enabled.extend(self._enabled)
		instance.visible.extend(self._visible)
		instance.material.extend(self._material)

	def getclipping_mode(self) -> int :
		return self._clipping_mode

	def setclipping_mode(self,value : int) :
		if self._clipping_mode != value:
			self._clipping_mode = value
			self.clipping_modeChanged.emit(value)

	clipping_mode = pyqtProperty(int, fget=getclipping_mode, fset=setclipping_mode, notify=clipping_modeChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.position = self._position.proto()
		instance.rotation = self._rotation.proto()
		instance.scale = self._scale.proto()
		instance.size = self._size.proto()
		instance.color = self._color.proto()
		instance.type.extend(self._type)
		instance.blend_mode.extend(self._blend_mode)
		instance.text.extend(self._text)
		instance.texture.extend(self._texture)
		instance.font.extend(self._font)
		instance.id.extend(self._id)
		instance.xanchor.extend(self._xanchor)
		instance.yanchor.extend(self._yanchor)
		instance.pivot.extend(self._pivot)
		instance.outline = self._outline.proto()
		instance.shadow = self._shadow.proto()
		instance.adjust_mode.extend(self._adjust_mode)
		instance.line_break.extend(self._line_break)
		instance.parent.extend(self._parent)
		instance.layer.extend(self._layer)
		instance.inherit_alpha.extend(self._inherit_alpha)
		instance.slice9 = self._slice9.proto()
		instance.outerBounds.extend(self._outerBounds)
		instance.innerRadius.extend(self._innerRadius)
		instance.perimeterVertices.extend(self._perimeterVertices)
		instance.pieFillAngle.extend(self._pieFillAngle)
		instance.clipping_mode.extend(self._clipping_mode)
		instance.clipping_visible.extend(self._clipping_visible)
		instance.clipping_inverted.extend(self._clipping_inverted)
		instance.alpha.extend(self._alpha)
		instance.outline_alpha.extend(self._outline_alpha)
		instance.shadow_alpha.extend(self._shadow_alpha)
		instance.overridden_fields = self._overridden_fields
		instance.template.extend(self._template)
		instance.template_node_child.extend(self._template_node_child)
		instance.text_leading.extend(self._text_leading)
		instance.text_tracking.extend(self._text_tracking)
		instance.size_mode.extend(self._size_mode)
		instance.spine_scene.extend(self._spine_scene)
		instance.spine_default_animation.extend(self._spine_default_animation)
		instance.spine_skin.extend(self._spine_skin)
		instance.spine_node_child.extend(self._spine_node_child)
		instance.particlefx.extend(self._particlefx)
		instance.custom_type.extend(self._custom_type)
		instance.enabled.extend(self._enabled)
		instance.visible.extend(self._visible)
		instance.material.extend(self._material)

	def getclipping_visible(self) -> bool :
		return self._clipping_visible

	def setclipping_visible(self,value : bool) :
		if self._clipping_visible != value:
			self._clipping_visible = value
			self.clipping_visibleChanged.emit(value)

	clipping_visible = pyqtProperty(bool, fget=getclipping_visible, fset=setclipping_visible, notify=clipping_visibleChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.position = self._position.proto()
		instance.rotation = self._rotation.proto()
		instance.scale = self._scale.proto()
		instance.size = self._size.proto()
		instance.color = self._color.proto()
		instance.type.extend(self._type)
		instance.blend_mode.extend(self._blend_mode)
		instance.text.extend(self._text)
		instance.texture.extend(self._texture)
		instance.font.extend(self._font)
		instance.id.extend(self._id)
		instance.xanchor.extend(self._xanchor)
		instance.yanchor.extend(self._yanchor)
		instance.pivot.extend(self._pivot)
		instance.outline = self._outline.proto()
		instance.shadow = self._shadow.proto()
		instance.adjust_mode.extend(self._adjust_mode)
		instance.line_break.extend(self._line_break)
		instance.parent.extend(self._parent)
		instance.layer.extend(self._layer)
		instance.inherit_alpha.extend(self._inherit_alpha)
		instance.slice9 = self._slice9.proto()
		instance.outerBounds.extend(self._outerBounds)
		instance.innerRadius.extend(self._innerRadius)
		instance.perimeterVertices.extend(self._perimeterVertices)
		instance.pieFillAngle.extend(self._pieFillAngle)
		instance.clipping_mode.extend(self._clipping_mode)
		instance.clipping_visible.extend(self._clipping_visible)
		instance.clipping_inverted.extend(self._clipping_inverted)
		instance.alpha.extend(self._alpha)
		instance.outline_alpha.extend(self._outline_alpha)
		instance.shadow_alpha.extend(self._shadow_alpha)
		instance.overridden_fields = self._overridden_fields
		instance.template.extend(self._template)
		instance.template_node_child.extend(self._template_node_child)
		instance.text_leading.extend(self._text_leading)
		instance.text_tracking.extend(self._text_tracking)
		instance.size_mode.extend(self._size_mode)
		instance.spine_scene.extend(self._spine_scene)
		instance.spine_default_animation.extend(self._spine_default_animation)
		instance.spine_skin.extend(self._spine_skin)
		instance.spine_node_child.extend(self._spine_node_child)
		instance.particlefx.extend(self._particlefx)
		instance.custom_type.extend(self._custom_type)
		instance.enabled.extend(self._enabled)
		instance.visible.extend(self._visible)
		instance.material.extend(self._material)

	def getclipping_inverted(self) -> bool :
		return self._clipping_inverted

	def setclipping_inverted(self,value : bool) :
		if self._clipping_inverted != value:
			self._clipping_inverted = value
			self.clipping_invertedChanged.emit(value)

	clipping_inverted = pyqtProperty(bool, fget=getclipping_inverted, fset=setclipping_inverted, notify=clipping_invertedChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.position = self._position.proto()
		instance.rotation = self._rotation.proto()
		instance.scale = self._scale.proto()
		instance.size = self._size.proto()
		instance.color = self._color.proto()
		instance.type.extend(self._type)
		instance.blend_mode.extend(self._blend_mode)
		instance.text.extend(self._text)
		instance.texture.extend(self._texture)
		instance.font.extend(self._font)
		instance.id.extend(self._id)
		instance.xanchor.extend(self._xanchor)
		instance.yanchor.extend(self._yanchor)
		instance.pivot.extend(self._pivot)
		instance.outline = self._outline.proto()
		instance.shadow = self._shadow.proto()
		instance.adjust_mode.extend(self._adjust_mode)
		instance.line_break.extend(self._line_break)
		instance.parent.extend(self._parent)
		instance.layer.extend(self._layer)
		instance.inherit_alpha.extend(self._inherit_alpha)
		instance.slice9 = self._slice9.proto()
		instance.outerBounds.extend(self._outerBounds)
		instance.innerRadius.extend(self._innerRadius)
		instance.perimeterVertices.extend(self._perimeterVertices)
		instance.pieFillAngle.extend(self._pieFillAngle)
		instance.clipping_mode.extend(self._clipping_mode)
		instance.clipping_visible.extend(self._clipping_visible)
		instance.clipping_inverted.extend(self._clipping_inverted)
		instance.alpha.extend(self._alpha)
		instance.outline_alpha.extend(self._outline_alpha)
		instance.shadow_alpha.extend(self._shadow_alpha)
		instance.overridden_fields = self._overridden_fields
		instance.template.extend(self._template)
		instance.template_node_child.extend(self._template_node_child)
		instance.text_leading.extend(self._text_leading)
		instance.text_tracking.extend(self._text_tracking)
		instance.size_mode.extend(self._size_mode)
		instance.spine_scene.extend(self._spine_scene)
		instance.spine_default_animation.extend(self._spine_default_animation)
		instance.spine_skin.extend(self._spine_skin)
		instance.spine_node_child.extend(self._spine_node_child)
		instance.particlefx.extend(self._particlefx)
		instance.custom_type.extend(self._custom_type)
		instance.enabled.extend(self._enabled)
		instance.visible.extend(self._visible)
		instance.material.extend(self._material)

	def getalpha(self) -> float :
		return self._alpha

	def setalpha(self,value : float) :
		if self._alpha != value:
			self._alpha = value
			self.alphaChanged.emit(value)

	alpha = pyqtProperty(float, fget=getalpha, fset=setalpha, notify=alphaChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.position = self._position.proto()
		instance.rotation = self._rotation.proto()
		instance.scale = self._scale.proto()
		instance.size = self._size.proto()
		instance.color = self._color.proto()
		instance.type.extend(self._type)
		instance.blend_mode.extend(self._blend_mode)
		instance.text.extend(self._text)
		instance.texture.extend(self._texture)
		instance.font.extend(self._font)
		instance.id.extend(self._id)
		instance.xanchor.extend(self._xanchor)
		instance.yanchor.extend(self._yanchor)
		instance.pivot.extend(self._pivot)
		instance.outline = self._outline.proto()
		instance.shadow = self._shadow.proto()
		instance.adjust_mode.extend(self._adjust_mode)
		instance.line_break.extend(self._line_break)
		instance.parent.extend(self._parent)
		instance.layer.extend(self._layer)
		instance.inherit_alpha.extend(self._inherit_alpha)
		instance.slice9 = self._slice9.proto()
		instance.outerBounds.extend(self._outerBounds)
		instance.innerRadius.extend(self._innerRadius)
		instance.perimeterVertices.extend(self._perimeterVertices)
		instance.pieFillAngle.extend(self._pieFillAngle)
		instance.clipping_mode.extend(self._clipping_mode)
		instance.clipping_visible.extend(self._clipping_visible)
		instance.clipping_inverted.extend(self._clipping_inverted)
		instance.alpha.extend(self._alpha)
		instance.outline_alpha.extend(self._outline_alpha)
		instance.shadow_alpha.extend(self._shadow_alpha)
		instance.overridden_fields = self._overridden_fields
		instance.template.extend(self._template)
		instance.template_node_child.extend(self._template_node_child)
		instance.text_leading.extend(self._text_leading)
		instance.text_tracking.extend(self._text_tracking)
		instance.size_mode.extend(self._size_mode)
		instance.spine_scene.extend(self._spine_scene)
		instance.spine_default_animation.extend(self._spine_default_animation)
		instance.spine_skin.extend(self._spine_skin)
		instance.spine_node_child.extend(self._spine_node_child)
		instance.particlefx.extend(self._particlefx)
		instance.custom_type.extend(self._custom_type)
		instance.enabled.extend(self._enabled)
		instance.visible.extend(self._visible)
		instance.material.extend(self._material)

	def getoutline_alpha(self) -> float :
		return self._outline_alpha

	def setoutline_alpha(self,value : float) :
		if self._outline_alpha != value:
			self._outline_alpha = value
			self.outline_alphaChanged.emit(value)

	outline_alpha = pyqtProperty(float, fget=getoutline_alpha, fset=setoutline_alpha, notify=outline_alphaChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.position = self._position.proto()
		instance.rotation = self._rotation.proto()
		instance.scale = self._scale.proto()
		instance.size = self._size.proto()
		instance.color = self._color.proto()
		instance.type.extend(self._type)
		instance.blend_mode.extend(self._blend_mode)
		instance.text.extend(self._text)
		instance.texture.extend(self._texture)
		instance.font.extend(self._font)
		instance.id.extend(self._id)
		instance.xanchor.extend(self._xanchor)
		instance.yanchor.extend(self._yanchor)
		instance.pivot.extend(self._pivot)
		instance.outline = self._outline.proto()
		instance.shadow = self._shadow.proto()
		instance.adjust_mode.extend(self._adjust_mode)
		instance.line_break.extend(self._line_break)
		instance.parent.extend(self._parent)
		instance.layer.extend(self._layer)
		instance.inherit_alpha.extend(self._inherit_alpha)
		instance.slice9 = self._slice9.proto()
		instance.outerBounds.extend(self._outerBounds)
		instance.innerRadius.extend(self._innerRadius)
		instance.perimeterVertices.extend(self._perimeterVertices)
		instance.pieFillAngle.extend(self._pieFillAngle)
		instance.clipping_mode.extend(self._clipping_mode)
		instance.clipping_visible.extend(self._clipping_visible)
		instance.clipping_inverted.extend(self._clipping_inverted)
		instance.alpha.extend(self._alpha)
		instance.outline_alpha.extend(self._outline_alpha)
		instance.shadow_alpha.extend(self._shadow_alpha)
		instance.overridden_fields = self._overridden_fields
		instance.template.extend(self._template)
		instance.template_node_child.extend(self._template_node_child)
		instance.text_leading.extend(self._text_leading)
		instance.text_tracking.extend(self._text_tracking)
		instance.size_mode.extend(self._size_mode)
		instance.spine_scene.extend(self._spine_scene)
		instance.spine_default_animation.extend(self._spine_default_animation)
		instance.spine_skin.extend(self._spine_skin)
		instance.spine_node_child.extend(self._spine_node_child)
		instance.particlefx.extend(self._particlefx)
		instance.custom_type.extend(self._custom_type)
		instance.enabled.extend(self._enabled)
		instance.visible.extend(self._visible)
		instance.material.extend(self._material)

	def getshadow_alpha(self) -> float :
		return self._shadow_alpha

	def setshadow_alpha(self,value : float) :
		if self._shadow_alpha != value:
			self._shadow_alpha = value
			self.shadow_alphaChanged.emit(value)

	shadow_alpha = pyqtProperty(float, fget=getshadow_alpha, fset=setshadow_alpha, notify=shadow_alphaChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.position = self._position.proto()
		instance.rotation = self._rotation.proto()
		instance.scale = self._scale.proto()
		instance.size = self._size.proto()
		instance.color = self._color.proto()
		instance.type.extend(self._type)
		instance.blend_mode.extend(self._blend_mode)
		instance.text.extend(self._text)
		instance.texture.extend(self._texture)
		instance.font.extend(self._font)
		instance.id.extend(self._id)
		instance.xanchor.extend(self._xanchor)
		instance.yanchor.extend(self._yanchor)
		instance.pivot.extend(self._pivot)
		instance.outline = self._outline.proto()
		instance.shadow = self._shadow.proto()
		instance.adjust_mode.extend(self._adjust_mode)
		instance.line_break.extend(self._line_break)
		instance.parent.extend(self._parent)
		instance.layer.extend(self._layer)
		instance.inherit_alpha.extend(self._inherit_alpha)
		instance.slice9 = self._slice9.proto()
		instance.outerBounds.extend(self._outerBounds)
		instance.innerRadius.extend(self._innerRadius)
		instance.perimeterVertices.extend(self._perimeterVertices)
		instance.pieFillAngle.extend(self._pieFillAngle)
		instance.clipping_mode.extend(self._clipping_mode)
		instance.clipping_visible.extend(self._clipping_visible)
		instance.clipping_inverted.extend(self._clipping_inverted)
		instance.alpha.extend(self._alpha)
		instance.outline_alpha.extend(self._outline_alpha)
		instance.shadow_alpha.extend(self._shadow_alpha)
		instance.overridden_fields = self._overridden_fields
		instance.template.extend(self._template)
		instance.template_node_child.extend(self._template_node_child)
		instance.text_leading.extend(self._text_leading)
		instance.text_tracking.extend(self._text_tracking)
		instance.size_mode.extend(self._size_mode)
		instance.spine_scene.extend(self._spine_scene)
		instance.spine_default_animation.extend(self._spine_default_animation)
		instance.spine_skin.extend(self._spine_skin)
		instance.spine_node_child.extend(self._spine_node_child)
		instance.particlefx.extend(self._particlefx)
		instance.custom_type.extend(self._custom_type)
		instance.enabled.extend(self._enabled)
		instance.visible.extend(self._visible)
		instance.material.extend(self._material)

	def getoverridden_fields(self) -> int :
		return self._overridden_fields

	def setoverridden_fields(self,value : List[int]) :
		if self._overridden_fields != value:
			self._overridden_fields = value
			self.overridden_fieldsChanged.emit(value)

	overridden_fields = pyqtProperty(List, fget=getoverridden_fields, fset=setoverridden_fields, notify=overridden_fieldsChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.position = self._position.proto()
		instance.rotation = self._rotation.proto()
		instance.scale = self._scale.proto()
		instance.size = self._size.proto()
		instance.color = self._color.proto()
		instance.type.extend(self._type)
		instance.blend_mode.extend(self._blend_mode)
		instance.text.extend(self._text)
		instance.texture.extend(self._texture)
		instance.font.extend(self._font)
		instance.id.extend(self._id)
		instance.xanchor.extend(self._xanchor)
		instance.yanchor.extend(self._yanchor)
		instance.pivot.extend(self._pivot)
		instance.outline = self._outline.proto()
		instance.shadow = self._shadow.proto()
		instance.adjust_mode.extend(self._adjust_mode)
		instance.line_break.extend(self._line_break)
		instance.parent.extend(self._parent)
		instance.layer.extend(self._layer)
		instance.inherit_alpha.extend(self._inherit_alpha)
		instance.slice9 = self._slice9.proto()
		instance.outerBounds.extend(self._outerBounds)
		instance.innerRadius.extend(self._innerRadius)
		instance.perimeterVertices.extend(self._perimeterVertices)
		instance.pieFillAngle.extend(self._pieFillAngle)
		instance.clipping_mode.extend(self._clipping_mode)
		instance.clipping_visible.extend(self._clipping_visible)
		instance.clipping_inverted.extend(self._clipping_inverted)
		instance.alpha.extend(self._alpha)
		instance.outline_alpha.extend(self._outline_alpha)
		instance.shadow_alpha.extend(self._shadow_alpha)
		instance.overridden_fields = self._overridden_fields
		instance.template.extend(self._template)
		instance.template_node_child.extend(self._template_node_child)
		instance.text_leading.extend(self._text_leading)
		instance.text_tracking.extend(self._text_tracking)
		instance.size_mode.extend(self._size_mode)
		instance.spine_scene.extend(self._spine_scene)
		instance.spine_default_animation.extend(self._spine_default_animation)
		instance.spine_skin.extend(self._spine_skin)
		instance.spine_node_child.extend(self._spine_node_child)
		instance.particlefx.extend(self._particlefx)
		instance.custom_type.extend(self._custom_type)
		instance.enabled.extend(self._enabled)
		instance.visible.extend(self._visible)
		instance.material.extend(self._material)

	def gettemplate(self) -> str :
		return self._template

	def settemplate(self,value : str) :
		if self._template != value:
			self._template = value
			self.templateChanged.emit(value)

	template = pyqtProperty(str, fget=gettemplate, fset=settemplate, notify=templateChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.position = self._position.proto()
		instance.rotation = self._rotation.proto()
		instance.scale = self._scale.proto()
		instance.size = self._size.proto()
		instance.color = self._color.proto()
		instance.type.extend(self._type)
		instance.blend_mode.extend(self._blend_mode)
		instance.text.extend(self._text)
		instance.texture.extend(self._texture)
		instance.font.extend(self._font)
		instance.id.extend(self._id)
		instance.xanchor.extend(self._xanchor)
		instance.yanchor.extend(self._yanchor)
		instance.pivot.extend(self._pivot)
		instance.outline = self._outline.proto()
		instance.shadow = self._shadow.proto()
		instance.adjust_mode.extend(self._adjust_mode)
		instance.line_break.extend(self._line_break)
		instance.parent.extend(self._parent)
		instance.layer.extend(self._layer)
		instance.inherit_alpha.extend(self._inherit_alpha)
		instance.slice9 = self._slice9.proto()
		instance.outerBounds.extend(self._outerBounds)
		instance.innerRadius.extend(self._innerRadius)
		instance.perimeterVertices.extend(self._perimeterVertices)
		instance.pieFillAngle.extend(self._pieFillAngle)
		instance.clipping_mode.extend(self._clipping_mode)
		instance.clipping_visible.extend(self._clipping_visible)
		instance.clipping_inverted.extend(self._clipping_inverted)
		instance.alpha.extend(self._alpha)
		instance.outline_alpha.extend(self._outline_alpha)
		instance.shadow_alpha.extend(self._shadow_alpha)
		instance.overridden_fields = self._overridden_fields
		instance.template.extend(self._template)
		instance.template_node_child.extend(self._template_node_child)
		instance.text_leading.extend(self._text_leading)
		instance.text_tracking.extend(self._text_tracking)
		instance.size_mode.extend(self._size_mode)
		instance.spine_scene.extend(self._spine_scene)
		instance.spine_default_animation.extend(self._spine_default_animation)
		instance.spine_skin.extend(self._spine_skin)
		instance.spine_node_child.extend(self._spine_node_child)
		instance.particlefx.extend(self._particlefx)
		instance.custom_type.extend(self._custom_type)
		instance.enabled.extend(self._enabled)
		instance.visible.extend(self._visible)
		instance.material.extend(self._material)

	def gettemplate_node_child(self) -> bool :
		return self._template_node_child

	def settemplate_node_child(self,value : bool) :
		if self._template_node_child != value:
			self._template_node_child = value
			self.template_node_childChanged.emit(value)

	template_node_child = pyqtProperty(bool, fget=gettemplate_node_child, fset=settemplate_node_child, notify=template_node_childChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.position = self._position.proto()
		instance.rotation = self._rotation.proto()
		instance.scale = self._scale.proto()
		instance.size = self._size.proto()
		instance.color = self._color.proto()
		instance.type.extend(self._type)
		instance.blend_mode.extend(self._blend_mode)
		instance.text.extend(self._text)
		instance.texture.extend(self._texture)
		instance.font.extend(self._font)
		instance.id.extend(self._id)
		instance.xanchor.extend(self._xanchor)
		instance.yanchor.extend(self._yanchor)
		instance.pivot.extend(self._pivot)
		instance.outline = self._outline.proto()
		instance.shadow = self._shadow.proto()
		instance.adjust_mode.extend(self._adjust_mode)
		instance.line_break.extend(self._line_break)
		instance.parent.extend(self._parent)
		instance.layer.extend(self._layer)
		instance.inherit_alpha.extend(self._inherit_alpha)
		instance.slice9 = self._slice9.proto()
		instance.outerBounds.extend(self._outerBounds)
		instance.innerRadius.extend(self._innerRadius)
		instance.perimeterVertices.extend(self._perimeterVertices)
		instance.pieFillAngle.extend(self._pieFillAngle)
		instance.clipping_mode.extend(self._clipping_mode)
		instance.clipping_visible.extend(self._clipping_visible)
		instance.clipping_inverted.extend(self._clipping_inverted)
		instance.alpha.extend(self._alpha)
		instance.outline_alpha.extend(self._outline_alpha)
		instance.shadow_alpha.extend(self._shadow_alpha)
		instance.overridden_fields = self._overridden_fields
		instance.template.extend(self._template)
		instance.template_node_child.extend(self._template_node_child)
		instance.text_leading.extend(self._text_leading)
		instance.text_tracking.extend(self._text_tracking)
		instance.size_mode.extend(self._size_mode)
		instance.spine_scene.extend(self._spine_scene)
		instance.spine_default_animation.extend(self._spine_default_animation)
		instance.spine_skin.extend(self._spine_skin)
		instance.spine_node_child.extend(self._spine_node_child)
		instance.particlefx.extend(self._particlefx)
		instance.custom_type.extend(self._custom_type)
		instance.enabled.extend(self._enabled)
		instance.visible.extend(self._visible)
		instance.material.extend(self._material)

	def gettext_leading(self) -> float :
		return self._text_leading

	def settext_leading(self,value : float) :
		if self._text_leading != value:
			self._text_leading = value
			self.text_leadingChanged.emit(value)

	text_leading = pyqtProperty(float, fget=gettext_leading, fset=settext_leading, notify=text_leadingChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.position = self._position.proto()
		instance.rotation = self._rotation.proto()
		instance.scale = self._scale.proto()
		instance.size = self._size.proto()
		instance.color = self._color.proto()
		instance.type.extend(self._type)
		instance.blend_mode.extend(self._blend_mode)
		instance.text.extend(self._text)
		instance.texture.extend(self._texture)
		instance.font.extend(self._font)
		instance.id.extend(self._id)
		instance.xanchor.extend(self._xanchor)
		instance.yanchor.extend(self._yanchor)
		instance.pivot.extend(self._pivot)
		instance.outline = self._outline.proto()
		instance.shadow = self._shadow.proto()
		instance.adjust_mode.extend(self._adjust_mode)
		instance.line_break.extend(self._line_break)
		instance.parent.extend(self._parent)
		instance.layer.extend(self._layer)
		instance.inherit_alpha.extend(self._inherit_alpha)
		instance.slice9 = self._slice9.proto()
		instance.outerBounds.extend(self._outerBounds)
		instance.innerRadius.extend(self._innerRadius)
		instance.perimeterVertices.extend(self._perimeterVertices)
		instance.pieFillAngle.extend(self._pieFillAngle)
		instance.clipping_mode.extend(self._clipping_mode)
		instance.clipping_visible.extend(self._clipping_visible)
		instance.clipping_inverted.extend(self._clipping_inverted)
		instance.alpha.extend(self._alpha)
		instance.outline_alpha.extend(self._outline_alpha)
		instance.shadow_alpha.extend(self._shadow_alpha)
		instance.overridden_fields = self._overridden_fields
		instance.template.extend(self._template)
		instance.template_node_child.extend(self._template_node_child)
		instance.text_leading.extend(self._text_leading)
		instance.text_tracking.extend(self._text_tracking)
		instance.size_mode.extend(self._size_mode)
		instance.spine_scene.extend(self._spine_scene)
		instance.spine_default_animation.extend(self._spine_default_animation)
		instance.spine_skin.extend(self._spine_skin)
		instance.spine_node_child.extend(self._spine_node_child)
		instance.particlefx.extend(self._particlefx)
		instance.custom_type.extend(self._custom_type)
		instance.enabled.extend(self._enabled)
		instance.visible.extend(self._visible)
		instance.material.extend(self._material)

	def gettext_tracking(self) -> float :
		return self._text_tracking

	def settext_tracking(self,value : float) :
		if self._text_tracking != value:
			self._text_tracking = value
			self.text_trackingChanged.emit(value)

	text_tracking = pyqtProperty(float, fget=gettext_tracking, fset=settext_tracking, notify=text_trackingChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.position = self._position.proto()
		instance.rotation = self._rotation.proto()
		instance.scale = self._scale.proto()
		instance.size = self._size.proto()
		instance.color = self._color.proto()
		instance.type.extend(self._type)
		instance.blend_mode.extend(self._blend_mode)
		instance.text.extend(self._text)
		instance.texture.extend(self._texture)
		instance.font.extend(self._font)
		instance.id.extend(self._id)
		instance.xanchor.extend(self._xanchor)
		instance.yanchor.extend(self._yanchor)
		instance.pivot.extend(self._pivot)
		instance.outline = self._outline.proto()
		instance.shadow = self._shadow.proto()
		instance.adjust_mode.extend(self._adjust_mode)
		instance.line_break.extend(self._line_break)
		instance.parent.extend(self._parent)
		instance.layer.extend(self._layer)
		instance.inherit_alpha.extend(self._inherit_alpha)
		instance.slice9 = self._slice9.proto()
		instance.outerBounds.extend(self._outerBounds)
		instance.innerRadius.extend(self._innerRadius)
		instance.perimeterVertices.extend(self._perimeterVertices)
		instance.pieFillAngle.extend(self._pieFillAngle)
		instance.clipping_mode.extend(self._clipping_mode)
		instance.clipping_visible.extend(self._clipping_visible)
		instance.clipping_inverted.extend(self._clipping_inverted)
		instance.alpha.extend(self._alpha)
		instance.outline_alpha.extend(self._outline_alpha)
		instance.shadow_alpha.extend(self._shadow_alpha)
		instance.overridden_fields = self._overridden_fields
		instance.template.extend(self._template)
		instance.template_node_child.extend(self._template_node_child)
		instance.text_leading.extend(self._text_leading)
		instance.text_tracking.extend(self._text_tracking)
		instance.size_mode.extend(self._size_mode)
		instance.spine_scene.extend(self._spine_scene)
		instance.spine_default_animation.extend(self._spine_default_animation)
		instance.spine_skin.extend(self._spine_skin)
		instance.spine_node_child.extend(self._spine_node_child)
		instance.particlefx.extend(self._particlefx)
		instance.custom_type.extend(self._custom_type)
		instance.enabled.extend(self._enabled)
		instance.visible.extend(self._visible)
		instance.material.extend(self._material)

	def getsize_mode(self) -> int :
		return self._size_mode

	def setsize_mode(self,value : int) :
		if self._size_mode != value:
			self._size_mode = value
			self.size_modeChanged.emit(value)

	size_mode = pyqtProperty(int, fget=getsize_mode, fset=setsize_mode, notify=size_modeChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.position = self._position.proto()
		instance.rotation = self._rotation.proto()
		instance.scale = self._scale.proto()
		instance.size = self._size.proto()
		instance.color = self._color.proto()
		instance.type.extend(self._type)
		instance.blend_mode.extend(self._blend_mode)
		instance.text.extend(self._text)
		instance.texture.extend(self._texture)
		instance.font.extend(self._font)
		instance.id.extend(self._id)
		instance.xanchor.extend(self._xanchor)
		instance.yanchor.extend(self._yanchor)
		instance.pivot.extend(self._pivot)
		instance.outline = self._outline.proto()
		instance.shadow = self._shadow.proto()
		instance.adjust_mode.extend(self._adjust_mode)
		instance.line_break.extend(self._line_break)
		instance.parent.extend(self._parent)
		instance.layer.extend(self._layer)
		instance.inherit_alpha.extend(self._inherit_alpha)
		instance.slice9 = self._slice9.proto()
		instance.outerBounds.extend(self._outerBounds)
		instance.innerRadius.extend(self._innerRadius)
		instance.perimeterVertices.extend(self._perimeterVertices)
		instance.pieFillAngle.extend(self._pieFillAngle)
		instance.clipping_mode.extend(self._clipping_mode)
		instance.clipping_visible.extend(self._clipping_visible)
		instance.clipping_inverted.extend(self._clipping_inverted)
		instance.alpha.extend(self._alpha)
		instance.outline_alpha.extend(self._outline_alpha)
		instance.shadow_alpha.extend(self._shadow_alpha)
		instance.overridden_fields = self._overridden_fields
		instance.template.extend(self._template)
		instance.template_node_child.extend(self._template_node_child)
		instance.text_leading.extend(self._text_leading)
		instance.text_tracking.extend(self._text_tracking)
		instance.size_mode.extend(self._size_mode)
		instance.spine_scene.extend(self._spine_scene)
		instance.spine_default_animation.extend(self._spine_default_animation)
		instance.spine_skin.extend(self._spine_skin)
		instance.spine_node_child.extend(self._spine_node_child)
		instance.particlefx.extend(self._particlefx)
		instance.custom_type.extend(self._custom_type)
		instance.enabled.extend(self._enabled)
		instance.visible.extend(self._visible)
		instance.material.extend(self._material)

	def getspine_scene(self) -> str :
		return self._spine_scene

	def setspine_scene(self,value : str) :
		if self._spine_scene != value:
			self._spine_scene = value
			self.spine_sceneChanged.emit(value)

	spine_scene = pyqtProperty(str, fget=getspine_scene, fset=setspine_scene, notify=spine_sceneChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.position = self._position.proto()
		instance.rotation = self._rotation.proto()
		instance.scale = self._scale.proto()
		instance.size = self._size.proto()
		instance.color = self._color.proto()
		instance.type.extend(self._type)
		instance.blend_mode.extend(self._blend_mode)
		instance.text.extend(self._text)
		instance.texture.extend(self._texture)
		instance.font.extend(self._font)
		instance.id.extend(self._id)
		instance.xanchor.extend(self._xanchor)
		instance.yanchor.extend(self._yanchor)
		instance.pivot.extend(self._pivot)
		instance.outline = self._outline.proto()
		instance.shadow = self._shadow.proto()
		instance.adjust_mode.extend(self._adjust_mode)
		instance.line_break.extend(self._line_break)
		instance.parent.extend(self._parent)
		instance.layer.extend(self._layer)
		instance.inherit_alpha.extend(self._inherit_alpha)
		instance.slice9 = self._slice9.proto()
		instance.outerBounds.extend(self._outerBounds)
		instance.innerRadius.extend(self._innerRadius)
		instance.perimeterVertices.extend(self._perimeterVertices)
		instance.pieFillAngle.extend(self._pieFillAngle)
		instance.clipping_mode.extend(self._clipping_mode)
		instance.clipping_visible.extend(self._clipping_visible)
		instance.clipping_inverted.extend(self._clipping_inverted)
		instance.alpha.extend(self._alpha)
		instance.outline_alpha.extend(self._outline_alpha)
		instance.shadow_alpha.extend(self._shadow_alpha)
		instance.overridden_fields = self._overridden_fields
		instance.template.extend(self._template)
		instance.template_node_child.extend(self._template_node_child)
		instance.text_leading.extend(self._text_leading)
		instance.text_tracking.extend(self._text_tracking)
		instance.size_mode.extend(self._size_mode)
		instance.spine_scene.extend(self._spine_scene)
		instance.spine_default_animation.extend(self._spine_default_animation)
		instance.spine_skin.extend(self._spine_skin)
		instance.spine_node_child.extend(self._spine_node_child)
		instance.particlefx.extend(self._particlefx)
		instance.custom_type.extend(self._custom_type)
		instance.enabled.extend(self._enabled)
		instance.visible.extend(self._visible)
		instance.material.extend(self._material)

	def getspine_default_animation(self) -> str :
		return self._spine_default_animation

	def setspine_default_animation(self,value : str) :
		if self._spine_default_animation != value:
			self._spine_default_animation = value
			self.spine_default_animationChanged.emit(value)

	spine_default_animation = pyqtProperty(str, fget=getspine_default_animation, fset=setspine_default_animation, notify=spine_default_animationChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.position = self._position.proto()
		instance.rotation = self._rotation.proto()
		instance.scale = self._scale.proto()
		instance.size = self._size.proto()
		instance.color = self._color.proto()
		instance.type.extend(self._type)
		instance.blend_mode.extend(self._blend_mode)
		instance.text.extend(self._text)
		instance.texture.extend(self._texture)
		instance.font.extend(self._font)
		instance.id.extend(self._id)
		instance.xanchor.extend(self._xanchor)
		instance.yanchor.extend(self._yanchor)
		instance.pivot.extend(self._pivot)
		instance.outline = self._outline.proto()
		instance.shadow = self._shadow.proto()
		instance.adjust_mode.extend(self._adjust_mode)
		instance.line_break.extend(self._line_break)
		instance.parent.extend(self._parent)
		instance.layer.extend(self._layer)
		instance.inherit_alpha.extend(self._inherit_alpha)
		instance.slice9 = self._slice9.proto()
		instance.outerBounds.extend(self._outerBounds)
		instance.innerRadius.extend(self._innerRadius)
		instance.perimeterVertices.extend(self._perimeterVertices)
		instance.pieFillAngle.extend(self._pieFillAngle)
		instance.clipping_mode.extend(self._clipping_mode)
		instance.clipping_visible.extend(self._clipping_visible)
		instance.clipping_inverted.extend(self._clipping_inverted)
		instance.alpha.extend(self._alpha)
		instance.outline_alpha.extend(self._outline_alpha)
		instance.shadow_alpha.extend(self._shadow_alpha)
		instance.overridden_fields = self._overridden_fields
		instance.template.extend(self._template)
		instance.template_node_child.extend(self._template_node_child)
		instance.text_leading.extend(self._text_leading)
		instance.text_tracking.extend(self._text_tracking)
		instance.size_mode.extend(self._size_mode)
		instance.spine_scene.extend(self._spine_scene)
		instance.spine_default_animation.extend(self._spine_default_animation)
		instance.spine_skin.extend(self._spine_skin)
		instance.spine_node_child.extend(self._spine_node_child)
		instance.particlefx.extend(self._particlefx)
		instance.custom_type.extend(self._custom_type)
		instance.enabled.extend(self._enabled)
		instance.visible.extend(self._visible)
		instance.material.extend(self._material)

	def getspine_skin(self) -> str :
		return self._spine_skin

	def setspine_skin(self,value : str) :
		if self._spine_skin != value:
			self._spine_skin = value
			self.spine_skinChanged.emit(value)

	spine_skin = pyqtProperty(str, fget=getspine_skin, fset=setspine_skin, notify=spine_skinChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.position = self._position.proto()
		instance.rotation = self._rotation.proto()
		instance.scale = self._scale.proto()
		instance.size = self._size.proto()
		instance.color = self._color.proto()
		instance.type.extend(self._type)
		instance.blend_mode.extend(self._blend_mode)
		instance.text.extend(self._text)
		instance.texture.extend(self._texture)
		instance.font.extend(self._font)
		instance.id.extend(self._id)
		instance.xanchor.extend(self._xanchor)
		instance.yanchor.extend(self._yanchor)
		instance.pivot.extend(self._pivot)
		instance.outline = self._outline.proto()
		instance.shadow = self._shadow.proto()
		instance.adjust_mode.extend(self._adjust_mode)
		instance.line_break.extend(self._line_break)
		instance.parent.extend(self._parent)
		instance.layer.extend(self._layer)
		instance.inherit_alpha.extend(self._inherit_alpha)
		instance.slice9 = self._slice9.proto()
		instance.outerBounds.extend(self._outerBounds)
		instance.innerRadius.extend(self._innerRadius)
		instance.perimeterVertices.extend(self._perimeterVertices)
		instance.pieFillAngle.extend(self._pieFillAngle)
		instance.clipping_mode.extend(self._clipping_mode)
		instance.clipping_visible.extend(self._clipping_visible)
		instance.clipping_inverted.extend(self._clipping_inverted)
		instance.alpha.extend(self._alpha)
		instance.outline_alpha.extend(self._outline_alpha)
		instance.shadow_alpha.extend(self._shadow_alpha)
		instance.overridden_fields = self._overridden_fields
		instance.template.extend(self._template)
		instance.template_node_child.extend(self._template_node_child)
		instance.text_leading.extend(self._text_leading)
		instance.text_tracking.extend(self._text_tracking)
		instance.size_mode.extend(self._size_mode)
		instance.spine_scene.extend(self._spine_scene)
		instance.spine_default_animation.extend(self._spine_default_animation)
		instance.spine_skin.extend(self._spine_skin)
		instance.spine_node_child.extend(self._spine_node_child)
		instance.particlefx.extend(self._particlefx)
		instance.custom_type.extend(self._custom_type)
		instance.enabled.extend(self._enabled)
		instance.visible.extend(self._visible)
		instance.material.extend(self._material)

	def getspine_node_child(self) -> bool :
		return self._spine_node_child

	def setspine_node_child(self,value : bool) :
		if self._spine_node_child != value:
			self._spine_node_child = value
			self.spine_node_childChanged.emit(value)

	spine_node_child = pyqtProperty(bool, fget=getspine_node_child, fset=setspine_node_child, notify=spine_node_childChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.position = self._position.proto()
		instance.rotation = self._rotation.proto()
		instance.scale = self._scale.proto()
		instance.size = self._size.proto()
		instance.color = self._color.proto()
		instance.type.extend(self._type)
		instance.blend_mode.extend(self._blend_mode)
		instance.text.extend(self._text)
		instance.texture.extend(self._texture)
		instance.font.extend(self._font)
		instance.id.extend(self._id)
		instance.xanchor.extend(self._xanchor)
		instance.yanchor.extend(self._yanchor)
		instance.pivot.extend(self._pivot)
		instance.outline = self._outline.proto()
		instance.shadow = self._shadow.proto()
		instance.adjust_mode.extend(self._adjust_mode)
		instance.line_break.extend(self._line_break)
		instance.parent.extend(self._parent)
		instance.layer.extend(self._layer)
		instance.inherit_alpha.extend(self._inherit_alpha)
		instance.slice9 = self._slice9.proto()
		instance.outerBounds.extend(self._outerBounds)
		instance.innerRadius.extend(self._innerRadius)
		instance.perimeterVertices.extend(self._perimeterVertices)
		instance.pieFillAngle.extend(self._pieFillAngle)
		instance.clipping_mode.extend(self._clipping_mode)
		instance.clipping_visible.extend(self._clipping_visible)
		instance.clipping_inverted.extend(self._clipping_inverted)
		instance.alpha.extend(self._alpha)
		instance.outline_alpha.extend(self._outline_alpha)
		instance.shadow_alpha.extend(self._shadow_alpha)
		instance.overridden_fields = self._overridden_fields
		instance.template.extend(self._template)
		instance.template_node_child.extend(self._template_node_child)
		instance.text_leading.extend(self._text_leading)
		instance.text_tracking.extend(self._text_tracking)
		instance.size_mode.extend(self._size_mode)
		instance.spine_scene.extend(self._spine_scene)
		instance.spine_default_animation.extend(self._spine_default_animation)
		instance.spine_skin.extend(self._spine_skin)
		instance.spine_node_child.extend(self._spine_node_child)
		instance.particlefx.extend(self._particlefx)
		instance.custom_type.extend(self._custom_type)
		instance.enabled.extend(self._enabled)
		instance.visible.extend(self._visible)
		instance.material.extend(self._material)

	def getparticlefx(self) -> str :
		return self._particlefx

	def setparticlefx(self,value : str) :
		if self._particlefx != value:
			self._particlefx = value
			self.particlefxChanged.emit(value)

	particlefx = pyqtProperty(str, fget=getparticlefx, fset=setparticlefx, notify=particlefxChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.position = self._position.proto()
		instance.rotation = self._rotation.proto()
		instance.scale = self._scale.proto()
		instance.size = self._size.proto()
		instance.color = self._color.proto()
		instance.type.extend(self._type)
		instance.blend_mode.extend(self._blend_mode)
		instance.text.extend(self._text)
		instance.texture.extend(self._texture)
		instance.font.extend(self._font)
		instance.id.extend(self._id)
		instance.xanchor.extend(self._xanchor)
		instance.yanchor.extend(self._yanchor)
		instance.pivot.extend(self._pivot)
		instance.outline = self._outline.proto()
		instance.shadow = self._shadow.proto()
		instance.adjust_mode.extend(self._adjust_mode)
		instance.line_break.extend(self._line_break)
		instance.parent.extend(self._parent)
		instance.layer.extend(self._layer)
		instance.inherit_alpha.extend(self._inherit_alpha)
		instance.slice9 = self._slice9.proto()
		instance.outerBounds.extend(self._outerBounds)
		instance.innerRadius.extend(self._innerRadius)
		instance.perimeterVertices.extend(self._perimeterVertices)
		instance.pieFillAngle.extend(self._pieFillAngle)
		instance.clipping_mode.extend(self._clipping_mode)
		instance.clipping_visible.extend(self._clipping_visible)
		instance.clipping_inverted.extend(self._clipping_inverted)
		instance.alpha.extend(self._alpha)
		instance.outline_alpha.extend(self._outline_alpha)
		instance.shadow_alpha.extend(self._shadow_alpha)
		instance.overridden_fields = self._overridden_fields
		instance.template.extend(self._template)
		instance.template_node_child.extend(self._template_node_child)
		instance.text_leading.extend(self._text_leading)
		instance.text_tracking.extend(self._text_tracking)
		instance.size_mode.extend(self._size_mode)
		instance.spine_scene.extend(self._spine_scene)
		instance.spine_default_animation.extend(self._spine_default_animation)
		instance.spine_skin.extend(self._spine_skin)
		instance.spine_node_child.extend(self._spine_node_child)
		instance.particlefx.extend(self._particlefx)
		instance.custom_type.extend(self._custom_type)
		instance.enabled.extend(self._enabled)
		instance.visible.extend(self._visible)
		instance.material.extend(self._material)

	def getcustom_type(self) -> int :
		return self._custom_type

	def setcustom_type(self,value : int) :
		if self._custom_type != value:
			self._custom_type = value
			self.custom_typeChanged.emit(value)

	custom_type = pyqtProperty(int, fget=getcustom_type, fset=setcustom_type, notify=custom_typeChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.position = self._position.proto()
		instance.rotation = self._rotation.proto()
		instance.scale = self._scale.proto()
		instance.size = self._size.proto()
		instance.color = self._color.proto()
		instance.type.extend(self._type)
		instance.blend_mode.extend(self._blend_mode)
		instance.text.extend(self._text)
		instance.texture.extend(self._texture)
		instance.font.extend(self._font)
		instance.id.extend(self._id)
		instance.xanchor.extend(self._xanchor)
		instance.yanchor.extend(self._yanchor)
		instance.pivot.extend(self._pivot)
		instance.outline = self._outline.proto()
		instance.shadow = self._shadow.proto()
		instance.adjust_mode.extend(self._adjust_mode)
		instance.line_break.extend(self._line_break)
		instance.parent.extend(self._parent)
		instance.layer.extend(self._layer)
		instance.inherit_alpha.extend(self._inherit_alpha)
		instance.slice9 = self._slice9.proto()
		instance.outerBounds.extend(self._outerBounds)
		instance.innerRadius.extend(self._innerRadius)
		instance.perimeterVertices.extend(self._perimeterVertices)
		instance.pieFillAngle.extend(self._pieFillAngle)
		instance.clipping_mode.extend(self._clipping_mode)
		instance.clipping_visible.extend(self._clipping_visible)
		instance.clipping_inverted.extend(self._clipping_inverted)
		instance.alpha.extend(self._alpha)
		instance.outline_alpha.extend(self._outline_alpha)
		instance.shadow_alpha.extend(self._shadow_alpha)
		instance.overridden_fields = self._overridden_fields
		instance.template.extend(self._template)
		instance.template_node_child.extend(self._template_node_child)
		instance.text_leading.extend(self._text_leading)
		instance.text_tracking.extend(self._text_tracking)
		instance.size_mode.extend(self._size_mode)
		instance.spine_scene.extend(self._spine_scene)
		instance.spine_default_animation.extend(self._spine_default_animation)
		instance.spine_skin.extend(self._spine_skin)
		instance.spine_node_child.extend(self._spine_node_child)
		instance.particlefx.extend(self._particlefx)
		instance.custom_type.extend(self._custom_type)
		instance.enabled.extend(self._enabled)
		instance.visible.extend(self._visible)
		instance.material.extend(self._material)

	def getenabled(self) -> bool :
		return self._enabled

	def setenabled(self,value : bool) :
		if self._enabled != value:
			self._enabled = value
			self.enabledChanged.emit(value)

	enabled = pyqtProperty(bool, fget=getenabled, fset=setenabled, notify=enabledChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.position = self._position.proto()
		instance.rotation = self._rotation.proto()
		instance.scale = self._scale.proto()
		instance.size = self._size.proto()
		instance.color = self._color.proto()
		instance.type.extend(self._type)
		instance.blend_mode.extend(self._blend_mode)
		instance.text.extend(self._text)
		instance.texture.extend(self._texture)
		instance.font.extend(self._font)
		instance.id.extend(self._id)
		instance.xanchor.extend(self._xanchor)
		instance.yanchor.extend(self._yanchor)
		instance.pivot.extend(self._pivot)
		instance.outline = self._outline.proto()
		instance.shadow = self._shadow.proto()
		instance.adjust_mode.extend(self._adjust_mode)
		instance.line_break.extend(self._line_break)
		instance.parent.extend(self._parent)
		instance.layer.extend(self._layer)
		instance.inherit_alpha.extend(self._inherit_alpha)
		instance.slice9 = self._slice9.proto()
		instance.outerBounds.extend(self._outerBounds)
		instance.innerRadius.extend(self._innerRadius)
		instance.perimeterVertices.extend(self._perimeterVertices)
		instance.pieFillAngle.extend(self._pieFillAngle)
		instance.clipping_mode.extend(self._clipping_mode)
		instance.clipping_visible.extend(self._clipping_visible)
		instance.clipping_inverted.extend(self._clipping_inverted)
		instance.alpha.extend(self._alpha)
		instance.outline_alpha.extend(self._outline_alpha)
		instance.shadow_alpha.extend(self._shadow_alpha)
		instance.overridden_fields = self._overridden_fields
		instance.template.extend(self._template)
		instance.template_node_child.extend(self._template_node_child)
		instance.text_leading.extend(self._text_leading)
		instance.text_tracking.extend(self._text_tracking)
		instance.size_mode.extend(self._size_mode)
		instance.spine_scene.extend(self._spine_scene)
		instance.spine_default_animation.extend(self._spine_default_animation)
		instance.spine_skin.extend(self._spine_skin)
		instance.spine_node_child.extend(self._spine_node_child)
		instance.particlefx.extend(self._particlefx)
		instance.custom_type.extend(self._custom_type)
		instance.enabled.extend(self._enabled)
		instance.visible.extend(self._visible)
		instance.material.extend(self._material)

	def getvisible(self) -> bool :
		return self._visible

	def setvisible(self,value : bool) :
		if self._visible != value:
			self._visible = value
			self.visibleChanged.emit(value)

	visible = pyqtProperty(bool, fget=getvisible, fset=setvisible, notify=visibleChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.position = self._position.proto()
		instance.rotation = self._rotation.proto()
		instance.scale = self._scale.proto()
		instance.size = self._size.proto()
		instance.color = self._color.proto()
		instance.type.extend(self._type)
		instance.blend_mode.extend(self._blend_mode)
		instance.text.extend(self._text)
		instance.texture.extend(self._texture)
		instance.font.extend(self._font)
		instance.id.extend(self._id)
		instance.xanchor.extend(self._xanchor)
		instance.yanchor.extend(self._yanchor)
		instance.pivot.extend(self._pivot)
		instance.outline = self._outline.proto()
		instance.shadow = self._shadow.proto()
		instance.adjust_mode.extend(self._adjust_mode)
		instance.line_break.extend(self._line_break)
		instance.parent.extend(self._parent)
		instance.layer.extend(self._layer)
		instance.inherit_alpha.extend(self._inherit_alpha)
		instance.slice9 = self._slice9.proto()
		instance.outerBounds.extend(self._outerBounds)
		instance.innerRadius.extend(self._innerRadius)
		instance.perimeterVertices.extend(self._perimeterVertices)
		instance.pieFillAngle.extend(self._pieFillAngle)
		instance.clipping_mode.extend(self._clipping_mode)
		instance.clipping_visible.extend(self._clipping_visible)
		instance.clipping_inverted.extend(self._clipping_inverted)
		instance.alpha.extend(self._alpha)
		instance.outline_alpha.extend(self._outline_alpha)
		instance.shadow_alpha.extend(self._shadow_alpha)
		instance.overridden_fields = self._overridden_fields
		instance.template.extend(self._template)
		instance.template_node_child.extend(self._template_node_child)
		instance.text_leading.extend(self._text_leading)
		instance.text_tracking.extend(self._text_tracking)
		instance.size_mode.extend(self._size_mode)
		instance.spine_scene.extend(self._spine_scene)
		instance.spine_default_animation.extend(self._spine_default_animation)
		instance.spine_skin.extend(self._spine_skin)
		instance.spine_node_child.extend(self._spine_node_child)
		instance.particlefx.extend(self._particlefx)
		instance.custom_type.extend(self._custom_type)
		instance.enabled.extend(self._enabled)
		instance.visible.extend(self._visible)
		instance.material.extend(self._material)

	def getmaterial(self) -> str :
		return self._material

	def setmaterial(self,value : str) :
		if self._material != value:
			self._material = value
			self.materialChanged.emit(value)

	material = pyqtProperty(str, fget=getmaterial, fset=setmaterial, notify=materialChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.position = self._position.proto()
		instance.rotation = self._rotation.proto()
		instance.scale = self._scale.proto()
		instance.size = self._size.proto()
		instance.color = self._color.proto()
		instance.type.extend(self._type)
		instance.blend_mode.extend(self._blend_mode)
		instance.text.extend(self._text)
		instance.texture.extend(self._texture)
		instance.font.extend(self._font)
		instance.id.extend(self._id)
		instance.xanchor.extend(self._xanchor)
		instance.yanchor.extend(self._yanchor)
		instance.pivot.extend(self._pivot)
		instance.outline = self._outline.proto()
		instance.shadow = self._shadow.proto()
		instance.adjust_mode.extend(self._adjust_mode)
		instance.line_break.extend(self._line_break)
		instance.parent.extend(self._parent)
		instance.layer.extend(self._layer)
		instance.inherit_alpha.extend(self._inherit_alpha)
		instance.slice9 = self._slice9.proto()
		instance.outerBounds.extend(self._outerBounds)
		instance.innerRadius.extend(self._innerRadius)
		instance.perimeterVertices.extend(self._perimeterVertices)
		instance.pieFillAngle.extend(self._pieFillAngle)
		instance.clipping_mode.extend(self._clipping_mode)
		instance.clipping_visible.extend(self._clipping_visible)
		instance.clipping_inverted.extend(self._clipping_inverted)
		instance.alpha.extend(self._alpha)
		instance.outline_alpha.extend(self._outline_alpha)
		instance.shadow_alpha.extend(self._shadow_alpha)
		instance.overridden_fields = self._overridden_fields
		instance.template.extend(self._template)
		instance.template_node_child.extend(self._template_node_child)
		instance.text_leading.extend(self._text_leading)
		instance.text_tracking.extend(self._text_tracking)
		instance.size_mode.extend(self._size_mode)
		instance.spine_scene.extend(self._spine_scene)
		instance.spine_default_animation.extend(self._spine_default_animation)
		instance.spine_skin.extend(self._spine_skin)
		instance.spine_node_child.extend(self._spine_node_child)
		instance.particlefx.extend(self._particlefx)
		instance.custom_type.extend(self._custom_type)
		instance.enabled.extend(self._enabled)
		instance.visible.extend(self._visible)
		instance.material.extend(self._material)

# ------- PathSettings ------- #
class PathSettings(QObject) :
	__PROTO__ = sdk.PathSettings
	def __init__(self,path :str = str() ,profile :str = str() ) -> PathSettings :
		self._path = path
		self._profile = profile
		pass
	def getpath(self) -> str :
		return self._path

	def setpath(self,value : str) :
		if self._path != value:
			self._path = value
			self.pathChanged.emit(value)

	path = pyqtProperty(str, fget=getpath, fset=setpath, notify=pathChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.path.extend(self._path)
		instance.profile.extend(self._profile)

	def getprofile(self) -> str :
		return self._profile

	def setprofile(self,value : str) :
		if self._profile != value:
			self._profile = value
			self.profileChanged.emit(value)

	profile = pyqtProperty(str, fget=getprofile, fset=setprofile, notify=profileChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.path.extend(self._path)
		instance.profile.extend(self._profile)

# ------- PauseSound ------- #
class PauseSound(QObject) :
	__PROTO__ = sdk.PauseSound
	def __init__(self,pause :bool = bool() ) -> PauseSound :
		self._pause = pause
		pass
	def getpause(self) -> bool :
		return self._pause

	def setpause(self,value : bool) :
		if self._pause != value:
			self._pause = value
			self.pauseChanged.emit(value)

	pause = pyqtProperty(bool, fget=getpause, fset=setpause, notify=pauseChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.pause.extend(self._pause)

# ------- PlatformProfile ------- #
class OS(Enum):
	OS_ID_GENERIC = 0
	OS_ID_WINDOWS = 1
	OS_ID_OSX = 2
	OS_ID_LINUX = 3
	OS_ID_IOS = 4
	OS_ID_ANDROID = 5
	OS_ID_WEB = 6
	OS_ID_SWITCH = 7
	OS_ID_PS4 = 8
	OS_ID_PS5 = 9
	OS_ID_XBOX = 10
class PlatformProfile(QObject) :
	__PROTO__ = sdk.PlatformProfile
	def __init__(self,os :int = int() ,formats :List[TextureFormatAlternative] = [],mipmaps :bool = bool() ,max_texture_size :int = int() ,premultiply_alpha :bool = bool() ) -> PlatformProfile :
		self._os = os
		self._formats = formats
		self._mipmaps = mipmaps
		self._max_texture_size = max_texture_size
		self._premultiply_alpha = premultiply_alpha
		pass
	def getos(self) -> int :
		return self._os

	def setos(self,value : int) :
		if self._os != value:
			self._os = value
			self.osChanged.emit(value)

	os = pyqtProperty(int, fget=getos, fset=setos, notify=osChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.os.extend(self._os)
		instance.formats.extend([i.proto() for i in self._formats])
		instance.mipmaps.extend(self._mipmaps)
		instance.max_texture_size.extend(self._max_texture_size)
		instance.premultiply_alpha.extend(self._premultiply_alpha)

	def getformats(self) -> TextureFormatAlternative :
		return self._formats

	def setformats(self,value : List[TextureFormatAlternative]) :
		if self._formats != value:
			self._formats = value
			self.formatsChanged.emit(value)

	formats = pyqtProperty(List, fget=getformats, fset=setformats, notify=formatsChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.os.extend(self._os)
		instance.formats.extend([i.proto() for i in self._formats])
		instance.mipmaps.extend(self._mipmaps)
		instance.max_texture_size.extend(self._max_texture_size)
		instance.premultiply_alpha.extend(self._premultiply_alpha)

	def getmipmaps(self) -> bool :
		return self._mipmaps

	def setmipmaps(self,value : bool) :
		if self._mipmaps != value:
			self._mipmaps = value
			self.mipmapsChanged.emit(value)

	mipmaps = pyqtProperty(bool, fget=getmipmaps, fset=setmipmaps, notify=mipmapsChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.os.extend(self._os)
		instance.formats.extend([i.proto() for i in self._formats])
		instance.mipmaps.extend(self._mipmaps)
		instance.max_texture_size.extend(self._max_texture_size)
		instance.premultiply_alpha.extend(self._premultiply_alpha)

	def getmax_texture_size(self) -> int :
		return self._max_texture_size

	def setmax_texture_size(self,value : int) :
		if self._max_texture_size != value:
			self._max_texture_size = value
			self.max_texture_sizeChanged.emit(value)

	max_texture_size = pyqtProperty(int, fget=getmax_texture_size, fset=setmax_texture_size, notify=max_texture_sizeChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.os.extend(self._os)
		instance.formats.extend([i.proto() for i in self._formats])
		instance.mipmaps.extend(self._mipmaps)
		instance.max_texture_size.extend(self._max_texture_size)
		instance.premultiply_alpha.extend(self._premultiply_alpha)

	def getpremultiply_alpha(self) -> bool :
		return self._premultiply_alpha

	def setpremultiply_alpha(self,value : bool) :
		if self._premultiply_alpha != value:
			self._premultiply_alpha = value
			self.premultiply_alphaChanged.emit(value)

	premultiply_alpha = pyqtProperty(bool, fget=getpremultiply_alpha, fset=setpremultiply_alpha, notify=premultiply_alphaChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.os.extend(self._os)
		instance.formats.extend([i.proto() for i in self._formats])
		instance.mipmaps.extend(self._mipmaps)
		instance.max_texture_size.extend(self._max_texture_size)
		instance.premultiply_alpha.extend(self._premultiply_alpha)

# ------- PlayAnimation ------- #
class PlayAnimation(QObject) :
	__PROTO__ = sdk.PlayAnimation
	def __init__(self,id :int = int() ,offset :float = float() ,playback_rate :float = float() ) -> PlayAnimation :
		self._id = id
		self._offset = offset
		self._playback_rate = playback_rate
		pass
	def getid(self) -> int :
		return self._id

	def setid(self,value : int) :
		if self._id != value:
			self._id = value
			self.idChanged.emit(value)

	id = pyqtProperty(int, fget=getid, fset=setid, notify=idChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.id.extend(self._id)
		instance.offset.extend(self._offset)
		instance.playback_rate.extend(self._playback_rate)

	def getoffset(self) -> float :
		return self._offset

	def setoffset(self,value : float) :
		if self._offset != value:
			self._offset = value
			self.offsetChanged.emit(value)

	offset = pyqtProperty(float, fget=getoffset, fset=setoffset, notify=offsetChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.id.extend(self._id)
		instance.offset.extend(self._offset)
		instance.playback_rate.extend(self._playback_rate)

	def getplayback_rate(self) -> float :
		return self._playback_rate

	def setplayback_rate(self,value : float) :
		if self._playback_rate != value:
			self._playback_rate = value
			self.playback_rateChanged.emit(value)

	playback_rate = pyqtProperty(float, fget=getplayback_rate, fset=setplayback_rate, notify=playback_rateChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.id.extend(self._id)
		instance.offset.extend(self._offset)
		instance.playback_rate.extend(self._playback_rate)

# ------- PlayParticleFX ------- #
class PlayParticleFX(QObject) :
	__PROTO__ = sdk.PlayParticleFX
	def __init__(self) -> PlayParticleFX :
		pass
# ------- PlaySound ------- #
class PlaySound(QObject) :
	__PROTO__ = sdk.PlaySound
	def __init__(self,delay :float = float() ,gain :float = float() ,pan :float = float() ,speed :float = float() ,play_id :int = int() ,start_time :float = float() ,start_frame :int = int() ) -> PlaySound :
		self._delay = delay
		self._gain = gain
		self._pan = pan
		self._speed = speed
		self._play_id = play_id
		self._start_time = start_time
		self._start_frame = start_frame
		pass
	def getdelay(self) -> float :
		return self._delay

	def setdelay(self,value : float) :
		if self._delay != value:
			self._delay = value
			self.delayChanged.emit(value)

	delay = pyqtProperty(float, fget=getdelay, fset=setdelay, notify=delayChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.delay.extend(self._delay)
		instance.gain.extend(self._gain)
		instance.pan.extend(self._pan)
		instance.speed.extend(self._speed)
		instance.play_id.extend(self._play_id)
		instance.start_time.extend(self._start_time)
		instance.start_frame.extend(self._start_frame)

	def getgain(self) -> float :
		return self._gain

	def setgain(self,value : float) :
		if self._gain != value:
			self._gain = value
			self.gainChanged.emit(value)

	gain = pyqtProperty(float, fget=getgain, fset=setgain, notify=gainChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.delay.extend(self._delay)
		instance.gain.extend(self._gain)
		instance.pan.extend(self._pan)
		instance.speed.extend(self._speed)
		instance.play_id.extend(self._play_id)
		instance.start_time.extend(self._start_time)
		instance.start_frame.extend(self._start_frame)

	def getpan(self) -> float :
		return self._pan

	def setpan(self,value : float) :
		if self._pan != value:
			self._pan = value
			self.panChanged.emit(value)

	pan = pyqtProperty(float, fget=getpan, fset=setpan, notify=panChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.delay.extend(self._delay)
		instance.gain.extend(self._gain)
		instance.pan.extend(self._pan)
		instance.speed.extend(self._speed)
		instance.play_id.extend(self._play_id)
		instance.start_time.extend(self._start_time)
		instance.start_frame.extend(self._start_frame)

	def getspeed(self) -> float :
		return self._speed

	def setspeed(self,value : float) :
		if self._speed != value:
			self._speed = value
			self.speedChanged.emit(value)

	speed = pyqtProperty(float, fget=getspeed, fset=setspeed, notify=speedChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.delay.extend(self._delay)
		instance.gain.extend(self._gain)
		instance.pan.extend(self._pan)
		instance.speed.extend(self._speed)
		instance.play_id.extend(self._play_id)
		instance.start_time.extend(self._start_time)
		instance.start_frame.extend(self._start_frame)

	def getplay_id(self) -> int :
		return self._play_id

	def setplay_id(self,value : int) :
		if self._play_id != value:
			self._play_id = value
			self.play_idChanged.emit(value)

	play_id = pyqtProperty(int, fget=getplay_id, fset=setplay_id, notify=play_idChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.delay.extend(self._delay)
		instance.gain.extend(self._gain)
		instance.pan.extend(self._pan)
		instance.speed.extend(self._speed)
		instance.play_id.extend(self._play_id)
		instance.start_time.extend(self._start_time)
		instance.start_frame.extend(self._start_frame)

	def getstart_time(self) -> float :
		return self._start_time

	def setstart_time(self,value : float) :
		if self._start_time != value:
			self._start_time = value
			self.start_timeChanged.emit(value)

	start_time = pyqtProperty(float, fget=getstart_time, fset=setstart_time, notify=start_timeChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.delay.extend(self._delay)
		instance.gain.extend(self._gain)
		instance.pan.extend(self._pan)
		instance.speed.extend(self._speed)
		instance.play_id.extend(self._play_id)
		instance.start_time.extend(self._start_time)
		instance.start_frame.extend(self._start_frame)

	def getstart_frame(self) -> int :
		return self._start_frame

	def setstart_frame(self,value : int) :
		if self._start_frame != value:
			self._start_frame = value
			self.start_frameChanged.emit(value)

	start_frame = pyqtProperty(int, fget=getstart_frame, fset=setstart_frame, notify=start_frameChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.delay.extend(self._delay)
		instance.gain.extend(self._gain)
		instance.pan.extend(self._pan)
		instance.speed.extend(self._speed)
		instance.play_id.extend(self._play_id)
		instance.start_time.extend(self._start_time)
		instance.start_frame.extend(self._start_frame)

# ------- Point3 ------- #
class Point3(QObject) :
	__PROTO__ = sdk.Point3
	def __init__(self,x :float = float() ,y :float = float() ,z :float = float() ,d :float = float() ) -> Point3 :
		self._x = x
		self._y = y
		self._z = z
		self._d = d
		pass
	def getx(self) -> float :
		return self._x

	def setx(self,value : float) :
		if self._x != value:
			self._x = value
			self.xChanged.emit(value)

	x = pyqtProperty(float, fget=getx, fset=setx, notify=xChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.x.extend(self._x)
		instance.y.extend(self._y)
		instance.z.extend(self._z)
		instance.d.extend(self._d)

	def gety(self) -> float :
		return self._y

	def sety(self,value : float) :
		if self._y != value:
			self._y = value
			self.yChanged.emit(value)

	y = pyqtProperty(float, fget=gety, fset=sety, notify=yChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.x.extend(self._x)
		instance.y.extend(self._y)
		instance.z.extend(self._z)
		instance.d.extend(self._d)

	def getz(self) -> float :
		return self._z

	def setz(self,value : float) :
		if self._z != value:
			self._z = value
			self.zChanged.emit(value)

	z = pyqtProperty(float, fget=getz, fset=setz, notify=zChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.x.extend(self._x)
		instance.y.extend(self._y)
		instance.z.extend(self._z)
		instance.d.extend(self._d)

	def getd(self) -> float :
		return self._d

	def setd(self,value : float) :
		if self._d != value:
			self._d = value
			self.dChanged.emit(value)

	d = pyqtProperty(float, fget=getd, fset=setd, notify=dChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.x.extend(self._x)
		instance.y.extend(self._y)
		instance.z.extend(self._z)
		instance.d.extend(self._d)

# ------- PropertyDeclarationEntry ------- #
class PropertyDeclarationEntry(QObject) :
	__PROTO__ = sdk.PropertyDeclarationEntry
	def __init__(self,key :str = str() ,id :int = int() ,index :int = int() ,element_ids :List[int] = [] ) -> PropertyDeclarationEntry :
		self._key = key
		self._id = id
		self._index = index
		self._element_ids = element_ids
		pass
	def getkey(self) -> str :
		return self._key

	def setkey(self,value : str) :
		if self._key != value:
			self._key = value
			self.keyChanged.emit(value)

	key = pyqtProperty(str, fget=getkey, fset=setkey, notify=keyChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.key.extend(self._key)
		instance.id.extend(self._id)
		instance.index.extend(self._index)
		instance.element_ids = self._element_ids

	def getid(self) -> int :
		return self._id

	def setid(self,value : int) :
		if self._id != value:
			self._id = value
			self.idChanged.emit(value)

	id = pyqtProperty(int, fget=getid, fset=setid, notify=idChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.key.extend(self._key)
		instance.id.extend(self._id)
		instance.index.extend(self._index)
		instance.element_ids = self._element_ids

	def getindex(self) -> int :
		return self._index

	def setindex(self,value : int) :
		if self._index != value:
			self._index = value
			self.indexChanged.emit(value)

	index = pyqtProperty(int, fget=getindex, fset=setindex, notify=indexChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.key.extend(self._key)
		instance.id.extend(self._id)
		instance.index.extend(self._index)
		instance.element_ids = self._element_ids

	def getelement_ids(self) -> int :
		return self._element_ids

	def setelement_ids(self,value : List[int]) :
		if self._element_ids != value:
			self._element_ids = value
			self.element_idsChanged.emit(value)

	element_ids = pyqtProperty(List, fget=getelement_ids, fset=setelement_ids, notify=element_idsChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.key.extend(self._key)
		instance.id.extend(self._id)
		instance.index.extend(self._index)
		instance.element_ids = self._element_ids

# ------- PropertyDeclarations ------- #
class PropertyDeclarations(QObject) :
	__PROTO__ = sdk.PropertyDeclarations
	def __init__(self,number_entries :List[PropertyDeclarationEntry] = [],hash_entries :List[PropertyDeclarationEntry] = [],url_entries :List[PropertyDeclarationEntry] = [],vector3_entries :List[PropertyDeclarationEntry] = [],vector4_entries :List[PropertyDeclarationEntry] = [],quat_entries :List[PropertyDeclarationEntry] = [],bool_entries :List[PropertyDeclarationEntry] = [],float_values :List[float] = [] ,hash_values :List[int] = [] ,string_values :List[str] = [] ) -> PropertyDeclarations :
		self._number_entries = number_entries
		self._hash_entries = hash_entries
		self._url_entries = url_entries
		self._vector3_entries = vector3_entries
		self._vector4_entries = vector4_entries
		self._quat_entries = quat_entries
		self._bool_entries = bool_entries
		self._float_values = float_values
		self._hash_values = hash_values
		self._string_values = string_values
		pass
	def getnumber_entries(self) -> PropertyDeclarationEntry :
		return self._number_entries

	def setnumber_entries(self,value : List[PropertyDeclarationEntry]) :
		if self._number_entries != value:
			self._number_entries = value
			self.number_entriesChanged.emit(value)

	number_entries = pyqtProperty(List, fget=getnumber_entries, fset=setnumber_entries, notify=number_entriesChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.number_entries.extend([i.proto() for i in self._number_entries])
		instance.hash_entries.extend([i.proto() for i in self._hash_entries])
		instance.url_entries.extend([i.proto() for i in self._url_entries])
		instance.vector3_entries.extend([i.proto() for i in self._vector3_entries])
		instance.vector4_entries.extend([i.proto() for i in self._vector4_entries])
		instance.quat_entries.extend([i.proto() for i in self._quat_entries])
		instance.bool_entries.extend([i.proto() for i in self._bool_entries])
		instance.float_values = self._float_values
		instance.hash_values = self._hash_values
		instance.string_values = self._string_values

	def gethash_entries(self) -> PropertyDeclarationEntry :
		return self._hash_entries

	def sethash_entries(self,value : List[PropertyDeclarationEntry]) :
		if self._hash_entries != value:
			self._hash_entries = value
			self.hash_entriesChanged.emit(value)

	hash_entries = pyqtProperty(List, fget=gethash_entries, fset=sethash_entries, notify=hash_entriesChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.number_entries.extend([i.proto() for i in self._number_entries])
		instance.hash_entries.extend([i.proto() for i in self._hash_entries])
		instance.url_entries.extend([i.proto() for i in self._url_entries])
		instance.vector3_entries.extend([i.proto() for i in self._vector3_entries])
		instance.vector4_entries.extend([i.proto() for i in self._vector4_entries])
		instance.quat_entries.extend([i.proto() for i in self._quat_entries])
		instance.bool_entries.extend([i.proto() for i in self._bool_entries])
		instance.float_values = self._float_values
		instance.hash_values = self._hash_values
		instance.string_values = self._string_values

	def geturl_entries(self) -> PropertyDeclarationEntry :
		return self._url_entries

	def seturl_entries(self,value : List[PropertyDeclarationEntry]) :
		if self._url_entries != value:
			self._url_entries = value
			self.url_entriesChanged.emit(value)

	url_entries = pyqtProperty(List, fget=geturl_entries, fset=seturl_entries, notify=url_entriesChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.number_entries.extend([i.proto() for i in self._number_entries])
		instance.hash_entries.extend([i.proto() for i in self._hash_entries])
		instance.url_entries.extend([i.proto() for i in self._url_entries])
		instance.vector3_entries.extend([i.proto() for i in self._vector3_entries])
		instance.vector4_entries.extend([i.proto() for i in self._vector4_entries])
		instance.quat_entries.extend([i.proto() for i in self._quat_entries])
		instance.bool_entries.extend([i.proto() for i in self._bool_entries])
		instance.float_values = self._float_values
		instance.hash_values = self._hash_values
		instance.string_values = self._string_values

	def getvector3_entries(self) -> PropertyDeclarationEntry :
		return self._vector3_entries

	def setvector3_entries(self,value : List[PropertyDeclarationEntry]) :
		if self._vector3_entries != value:
			self._vector3_entries = value
			self.vector3_entriesChanged.emit(value)

	vector3_entries = pyqtProperty(List, fget=getvector3_entries, fset=setvector3_entries, notify=vector3_entriesChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.number_entries.extend([i.proto() for i in self._number_entries])
		instance.hash_entries.extend([i.proto() for i in self._hash_entries])
		instance.url_entries.extend([i.proto() for i in self._url_entries])
		instance.vector3_entries.extend([i.proto() for i in self._vector3_entries])
		instance.vector4_entries.extend([i.proto() for i in self._vector4_entries])
		instance.quat_entries.extend([i.proto() for i in self._quat_entries])
		instance.bool_entries.extend([i.proto() for i in self._bool_entries])
		instance.float_values = self._float_values
		instance.hash_values = self._hash_values
		instance.string_values = self._string_values

	def getvector4_entries(self) -> PropertyDeclarationEntry :
		return self._vector4_entries

	def setvector4_entries(self,value : List[PropertyDeclarationEntry]) :
		if self._vector4_entries != value:
			self._vector4_entries = value
			self.vector4_entriesChanged.emit(value)

	vector4_entries = pyqtProperty(List, fget=getvector4_entries, fset=setvector4_entries, notify=vector4_entriesChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.number_entries.extend([i.proto() for i in self._number_entries])
		instance.hash_entries.extend([i.proto() for i in self._hash_entries])
		instance.url_entries.extend([i.proto() for i in self._url_entries])
		instance.vector3_entries.extend([i.proto() for i in self._vector3_entries])
		instance.vector4_entries.extend([i.proto() for i in self._vector4_entries])
		instance.quat_entries.extend([i.proto() for i in self._quat_entries])
		instance.bool_entries.extend([i.proto() for i in self._bool_entries])
		instance.float_values = self._float_values
		instance.hash_values = self._hash_values
		instance.string_values = self._string_values

	def getquat_entries(self) -> PropertyDeclarationEntry :
		return self._quat_entries

	def setquat_entries(self,value : List[PropertyDeclarationEntry]) :
		if self._quat_entries != value:
			self._quat_entries = value
			self.quat_entriesChanged.emit(value)

	quat_entries = pyqtProperty(List, fget=getquat_entries, fset=setquat_entries, notify=quat_entriesChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.number_entries.extend([i.proto() for i in self._number_entries])
		instance.hash_entries.extend([i.proto() for i in self._hash_entries])
		instance.url_entries.extend([i.proto() for i in self._url_entries])
		instance.vector3_entries.extend([i.proto() for i in self._vector3_entries])
		instance.vector4_entries.extend([i.proto() for i in self._vector4_entries])
		instance.quat_entries.extend([i.proto() for i in self._quat_entries])
		instance.bool_entries.extend([i.proto() for i in self._bool_entries])
		instance.float_values = self._float_values
		instance.hash_values = self._hash_values
		instance.string_values = self._string_values

	def getbool_entries(self) -> PropertyDeclarationEntry :
		return self._bool_entries

	def setbool_entries(self,value : List[PropertyDeclarationEntry]) :
		if self._bool_entries != value:
			self._bool_entries = value
			self.bool_entriesChanged.emit(value)

	bool_entries = pyqtProperty(List, fget=getbool_entries, fset=setbool_entries, notify=bool_entriesChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.number_entries.extend([i.proto() for i in self._number_entries])
		instance.hash_entries.extend([i.proto() for i in self._hash_entries])
		instance.url_entries.extend([i.proto() for i in self._url_entries])
		instance.vector3_entries.extend([i.proto() for i in self._vector3_entries])
		instance.vector4_entries.extend([i.proto() for i in self._vector4_entries])
		instance.quat_entries.extend([i.proto() for i in self._quat_entries])
		instance.bool_entries.extend([i.proto() for i in self._bool_entries])
		instance.float_values = self._float_values
		instance.hash_values = self._hash_values
		instance.string_values = self._string_values

	def getfloat_values(self) -> float :
		return self._float_values

	def setfloat_values(self,value : List[float]) :
		if self._float_values != value:
			self._float_values = value
			self.float_valuesChanged.emit(value)

	float_values = pyqtProperty(List, fget=getfloat_values, fset=setfloat_values, notify=float_valuesChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.number_entries.extend([i.proto() for i in self._number_entries])
		instance.hash_entries.extend([i.proto() for i in self._hash_entries])
		instance.url_entries.extend([i.proto() for i in self._url_entries])
		instance.vector3_entries.extend([i.proto() for i in self._vector3_entries])
		instance.vector4_entries.extend([i.proto() for i in self._vector4_entries])
		instance.quat_entries.extend([i.proto() for i in self._quat_entries])
		instance.bool_entries.extend([i.proto() for i in self._bool_entries])
		instance.float_values = self._float_values
		instance.hash_values = self._hash_values
		instance.string_values = self._string_values

	def gethash_values(self) -> int :
		return self._hash_values

	def sethash_values(self,value : List[int]) :
		if self._hash_values != value:
			self._hash_values = value
			self.hash_valuesChanged.emit(value)

	hash_values = pyqtProperty(List, fget=gethash_values, fset=sethash_values, notify=hash_valuesChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.number_entries.extend([i.proto() for i in self._number_entries])
		instance.hash_entries.extend([i.proto() for i in self._hash_entries])
		instance.url_entries.extend([i.proto() for i in self._url_entries])
		instance.vector3_entries.extend([i.proto() for i in self._vector3_entries])
		instance.vector4_entries.extend([i.proto() for i in self._vector4_entries])
		instance.quat_entries.extend([i.proto() for i in self._quat_entries])
		instance.bool_entries.extend([i.proto() for i in self._bool_entries])
		instance.float_values = self._float_values
		instance.hash_values = self._hash_values
		instance.string_values = self._string_values

	def getstring_values(self) -> str :
		return self._string_values

	def setstring_values(self,value : List[str]) :
		if self._string_values != value:
			self._string_values = value
			self.string_valuesChanged.emit(value)

	string_values = pyqtProperty(List, fget=getstring_values, fset=setstring_values, notify=string_valuesChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.number_entries.extend([i.proto() for i in self._number_entries])
		instance.hash_entries.extend([i.proto() for i in self._hash_entries])
		instance.url_entries.extend([i.proto() for i in self._url_entries])
		instance.vector3_entries.extend([i.proto() for i in self._vector3_entries])
		instance.vector4_entries.extend([i.proto() for i in self._vector4_entries])
		instance.quat_entries.extend([i.proto() for i in self._quat_entries])
		instance.bool_entries.extend([i.proto() for i in self._bool_entries])
		instance.float_values = self._float_values
		instance.hash_values = self._hash_values
		instance.string_values = self._string_values

# ------- PropertyDesc ------- #
class PropertyDesc(QObject) :
	__PROTO__ = sdk.PropertyDesc
	def __init__(self,id :str = str() ,value :str = str() ,type :int = int() ) -> PropertyDesc :
		self._id = id
		self._value = value
		self._type = type
		pass
	def getid(self) -> str :
		return self._id

	def setid(self,value : str) :
		if self._id != value:
			self._id = value
			self.idChanged.emit(value)

	id = pyqtProperty(str, fget=getid, fset=setid, notify=idChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.id.extend(self._id)
		instance.value.extend(self._value)
		instance.type.extend(self._type)

	def getvalue(self) -> str :
		return self._value

	def setvalue(self,value : str) :
		if self._value != value:
			self._value = value
			self.valueChanged.emit(value)

	value = pyqtProperty(str, fget=getvalue, fset=setvalue, notify=valueChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.id.extend(self._id)
		instance.value.extend(self._value)
		instance.type.extend(self._type)

	def gettype(self) -> int :
		return self._type

	def settype(self,value : int) :
		if self._type != value:
			self._type = value
			self.typeChanged.emit(value)

	type = pyqtProperty(int, fget=gettype, fset=settype, notify=typeChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.id.extend(self._id)
		instance.value.extend(self._value)
		instance.type.extend(self._type)

# ------- PrototypeDesc ------- #
class PrototypeDesc(QObject) :
	__PROTO__ = sdk.PrototypeDesc
	def __init__(self,components :List[ComponentDesc] = [],embedded_components :List[EmbeddedComponentDesc] = [],property_resources :List[str] = [] ) -> PrototypeDesc :
		self._components = components
		self._embedded_components = embedded_components
		self._property_resources = property_resources
		pass
	def getcomponents(self) -> ComponentDesc :
		return self._components

	def setcomponents(self,value : List[ComponentDesc]) :
		if self._components != value:
			self._components = value
			self.componentsChanged.emit(value)

	components = pyqtProperty(List, fget=getcomponents, fset=setcomponents, notify=componentsChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.components.extend([i.proto() for i in self._components])
		instance.embedded_components.extend([i.proto() for i in self._embedded_components])
		instance.property_resources = self._property_resources

	def getembedded_components(self) -> EmbeddedComponentDesc :
		return self._embedded_components

	def setembedded_components(self,value : List[EmbeddedComponentDesc]) :
		if self._embedded_components != value:
			self._embedded_components = value
			self.embedded_componentsChanged.emit(value)

	embedded_components = pyqtProperty(List, fget=getembedded_components, fset=setembedded_components, notify=embedded_componentsChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.components.extend([i.proto() for i in self._components])
		instance.embedded_components.extend([i.proto() for i in self._embedded_components])
		instance.property_resources = self._property_resources

	def getproperty_resources(self) -> str :
		return self._property_resources

	def setproperty_resources(self,value : List[str]) :
		if self._property_resources != value:
			self._property_resources = value
			self.property_resourcesChanged.emit(value)

	property_resources = pyqtProperty(List, fget=getproperty_resources, fset=setproperty_resources, notify=property_resourcesChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.components.extend([i.proto() for i in self._components])
		instance.embedded_components.extend([i.proto() for i in self._embedded_components])
		instance.property_resources = self._property_resources

# ------- Quat ------- #
class Quat(QObject) :
	__PROTO__ = sdk.Quat
	def __init__(self,x :float = float() ,y :float = float() ,z :float = float() ,w :float = float() ) -> Quat :
		self._x = x
		self._y = y
		self._z = z
		self._w = w
		pass
	def getx(self) -> float :
		return self._x

	def setx(self,value : float) :
		if self._x != value:
			self._x = value
			self.xChanged.emit(value)

	x = pyqtProperty(float, fget=getx, fset=setx, notify=xChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.x.extend(self._x)
		instance.y.extend(self._y)
		instance.z.extend(self._z)
		instance.w.extend(self._w)

	def gety(self) -> float :
		return self._y

	def sety(self,value : float) :
		if self._y != value:
			self._y = value
			self.yChanged.emit(value)

	y = pyqtProperty(float, fget=gety, fset=sety, notify=yChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.x.extend(self._x)
		instance.y.extend(self._y)
		instance.z.extend(self._z)
		instance.w.extend(self._w)

	def getz(self) -> float :
		return self._z

	def setz(self,value : float) :
		if self._z != value:
			self._z = value
			self.zChanged.emit(value)

	z = pyqtProperty(float, fget=getz, fset=setz, notify=zChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.x.extend(self._x)
		instance.y.extend(self._y)
		instance.z.extend(self._z)
		instance.w.extend(self._w)

	def getw(self) -> float :
		return self._w

	def setw(self,value : float) :
		if self._w != value:
			self._w = value
			self.wChanged.emit(value)

	w = pyqtProperty(float, fget=getw, fset=setw, notify=wChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.x.extend(self._x)
		instance.y.extend(self._y)
		instance.z.extend(self._z)
		instance.w.extend(self._w)

# ------- RayCastMissed ------- #
class RayCastMissed(QObject) :
	__PROTO__ = sdk.RayCastMissed
	def __init__(self,request_id :int = int() ) -> RayCastMissed :
		self._request_id = request_id
		pass
	def getrequest_id(self) -> int :
		return self._request_id

	def setrequest_id(self,value : int) :
		if self._request_id != value:
			self._request_id = value
			self.request_idChanged.emit(value)

	request_id = pyqtProperty(int, fget=getrequest_id, fset=setrequest_id, notify=request_idChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.request_id.extend(self._request_id)

# ------- RayCastResponse ------- #
class RayCastResponse(QObject) :
	__PROTO__ = sdk.RayCastResponse
	def __init__(self,fraction :float = float() ,position :Point3 = None ,normal :Vector3 = None ,id :int = int() ,group :int = int() ,request_id :int = int() ) -> RayCastResponse :
		self._fraction = fraction
		self._position = position
		self._normal = normal
		self._id = id
		self._group = group
		self._request_id = request_id
		pass
	def getfraction(self) -> float :
		return self._fraction

	def setfraction(self,value : float) :
		if self._fraction != value:
			self._fraction = value
			self.fractionChanged.emit(value)

	fraction = pyqtProperty(float, fget=getfraction, fset=setfraction, notify=fractionChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.fraction.extend(self._fraction)
		instance.position = self._position.proto()
		instance.normal = self._normal.proto()
		instance.id.extend(self._id)
		instance.group.extend(self._group)
		instance.request_id.extend(self._request_id)

	def getposition(self) -> Point3 :
		return self._position

	def setposition(self,value : Point3) :
		if self._position != value:
			self._position = value
			self.positionChanged.emit(value)

	position = pyqtProperty(QObject, fget=getposition, fset=setposition, notify=positionChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.fraction.extend(self._fraction)
		instance.position = self._position.proto()
		instance.normal = self._normal.proto()
		instance.id.extend(self._id)
		instance.group.extend(self._group)
		instance.request_id.extend(self._request_id)

	def getnormal(self) -> Vector3 :
		return self._normal

	def setnormal(self,value : Vector3) :
		if self._normal != value:
			self._normal = value
			self.normalChanged.emit(value)

	normal = pyqtProperty(QObject, fget=getnormal, fset=setnormal, notify=normalChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.fraction.extend(self._fraction)
		instance.position = self._position.proto()
		instance.normal = self._normal.proto()
		instance.id.extend(self._id)
		instance.group.extend(self._group)
		instance.request_id.extend(self._request_id)

	def getid(self) -> int :
		return self._id

	def setid(self,value : int) :
		if self._id != value:
			self._id = value
			self.idChanged.emit(value)

	id = pyqtProperty(int, fget=getid, fset=setid, notify=idChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.fraction.extend(self._fraction)
		instance.position = self._position.proto()
		instance.normal = self._normal.proto()
		instance.id.extend(self._id)
		instance.group.extend(self._group)
		instance.request_id.extend(self._request_id)

	def getgroup(self) -> int :
		return self._group

	def setgroup(self,value : int) :
		if self._group != value:
			self._group = value
			self.groupChanged.emit(value)

	group = pyqtProperty(int, fget=getgroup, fset=setgroup, notify=groupChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.fraction.extend(self._fraction)
		instance.position = self._position.proto()
		instance.normal = self._normal.proto()
		instance.id.extend(self._id)
		instance.group.extend(self._group)
		instance.request_id.extend(self._request_id)

	def getrequest_id(self) -> int :
		return self._request_id

	def setrequest_id(self,value : int) :
		if self._request_id != value:
			self._request_id = value
			self.request_idChanged.emit(value)

	request_id = pyqtProperty(int, fget=getrequest_id, fset=setrequest_id, notify=request_idChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.fraction.extend(self._fraction)
		instance.position = self._position.proto()
		instance.normal = self._normal.proto()
		instance.id.extend(self._id)
		instance.group.extend(self._group)
		instance.request_id.extend(self._request_id)

# ------- Reboot ------- #
class Reboot(QObject) :
	__PROTO__ = sdk.Reboot
	def __init__(self,arg1 :str = str() ,arg2 :str = str() ,arg3 :str = str() ,arg4 :str = str() ,arg5 :str = str() ,arg6 :str = str() ) -> Reboot :
		self._arg1 = arg1
		self._arg2 = arg2
		self._arg3 = arg3
		self._arg4 = arg4
		self._arg5 = arg5
		self._arg6 = arg6
		pass
	def getarg1(self) -> str :
		return self._arg1

	def setarg1(self,value : str) :
		if self._arg1 != value:
			self._arg1 = value
			self.arg1Changed.emit(value)

	arg1 = pyqtProperty(str, fget=getarg1, fset=setarg1, notify=arg1Changed)

	def proto(self) :
		instance = self.__PROTO__()
		instance.arg1.extend(self._arg1)
		instance.arg2.extend(self._arg2)
		instance.arg3.extend(self._arg3)
		instance.arg4.extend(self._arg4)
		instance.arg5.extend(self._arg5)
		instance.arg6.extend(self._arg6)

	def getarg2(self) -> str :
		return self._arg2

	def setarg2(self,value : str) :
		if self._arg2 != value:
			self._arg2 = value
			self.arg2Changed.emit(value)

	arg2 = pyqtProperty(str, fget=getarg2, fset=setarg2, notify=arg2Changed)

	def proto(self) :
		instance = self.__PROTO__()
		instance.arg1.extend(self._arg1)
		instance.arg2.extend(self._arg2)
		instance.arg3.extend(self._arg3)
		instance.arg4.extend(self._arg4)
		instance.arg5.extend(self._arg5)
		instance.arg6.extend(self._arg6)

	def getarg3(self) -> str :
		return self._arg3

	def setarg3(self,value : str) :
		if self._arg3 != value:
			self._arg3 = value
			self.arg3Changed.emit(value)

	arg3 = pyqtProperty(str, fget=getarg3, fset=setarg3, notify=arg3Changed)

	def proto(self) :
		instance = self.__PROTO__()
		instance.arg1.extend(self._arg1)
		instance.arg2.extend(self._arg2)
		instance.arg3.extend(self._arg3)
		instance.arg4.extend(self._arg4)
		instance.arg5.extend(self._arg5)
		instance.arg6.extend(self._arg6)

	def getarg4(self) -> str :
		return self._arg4

	def setarg4(self,value : str) :
		if self._arg4 != value:
			self._arg4 = value
			self.arg4Changed.emit(value)

	arg4 = pyqtProperty(str, fget=getarg4, fset=setarg4, notify=arg4Changed)

	def proto(self) :
		instance = self.__PROTO__()
		instance.arg1.extend(self._arg1)
		instance.arg2.extend(self._arg2)
		instance.arg3.extend(self._arg3)
		instance.arg4.extend(self._arg4)
		instance.arg5.extend(self._arg5)
		instance.arg6.extend(self._arg6)

	def getarg5(self) -> str :
		return self._arg5

	def setarg5(self,value : str) :
		if self._arg5 != value:
			self._arg5 = value
			self.arg5Changed.emit(value)

	arg5 = pyqtProperty(str, fget=getarg5, fset=setarg5, notify=arg5Changed)

	def proto(self) :
		instance = self.__PROTO__()
		instance.arg1.extend(self._arg1)
		instance.arg2.extend(self._arg2)
		instance.arg3.extend(self._arg3)
		instance.arg4.extend(self._arg4)
		instance.arg5.extend(self._arg5)
		instance.arg6.extend(self._arg6)

	def getarg6(self) -> str :
		return self._arg6

	def setarg6(self,value : str) :
		if self._arg6 != value:
			self._arg6 = value
			self.arg6Changed.emit(value)

	arg6 = pyqtProperty(str, fget=getarg6, fset=setarg6, notify=arg6Changed)

	def proto(self) :
		instance = self.__PROTO__()
		instance.arg1.extend(self._arg1)
		instance.arg2.extend(self._arg2)
		instance.arg3.extend(self._arg3)
		instance.arg4.extend(self._arg4)
		instance.arg5.extend(self._arg5)
		instance.arg6.extend(self._arg6)

# ------- ReleaseCameraFocus ------- #
class ReleaseCameraFocus(QObject) :
	__PROTO__ = sdk.ReleaseCameraFocus
	def __init__(self) -> ReleaseCameraFocus :
		pass
# ------- ReleaseInputFocus ------- #
class ReleaseInputFocus(QObject) :
	__PROTO__ = sdk.ReleaseInputFocus
	def __init__(self) -> ReleaseInputFocus :
		pass
# ------- Reload ------- #
class Reload(QObject) :
	__PROTO__ = sdk.Reload
	def __init__(self,resources :List[str] = [] ) -> Reload :
		self._resources = resources
		pass
	def getresources(self) -> str :
		return self._resources

	def setresources(self,value : List[str]) :
		if self._resources != value:
			self._resources = value
			self.resourcesChanged.emit(value)

	resources = pyqtProperty(List, fget=getresources, fset=setresources, notify=resourcesChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.resources = self._resources

# ------- RenderPrototypeDesc ------- #
class RenderPrototypeDesc(QObject) :
	__PROTO__ = sdk.RenderPrototypeDesc
	def __init__(self,script :str = str() ,materials :List[MaterialDesc] = [],render_resources :List[RenderResourceDesc] = []) -> RenderPrototypeDesc :
		self._script = script
		self._materials = materials
		self._render_resources = render_resources
		pass
	def getscript(self) -> str :
		return self._script

	def setscript(self,value : str) :
		if self._script != value:
			self._script = value
			self.scriptChanged.emit(value)

	script = pyqtProperty(str, fget=getscript, fset=setscript, notify=scriptChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.script.extend(self._script)
		instance.materials.extend([i.proto() for i in self._materials])
		instance.render_resources.extend([i.proto() for i in self._render_resources])

	def getmaterials(self) -> MaterialDesc :
		return self._materials

	def setmaterials(self,value : List[MaterialDesc]) :
		if self._materials != value:
			self._materials = value
			self.materialsChanged.emit(value)

	materials = pyqtProperty(List, fget=getmaterials, fset=setmaterials, notify=materialsChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.script.extend(self._script)
		instance.materials.extend([i.proto() for i in self._materials])
		instance.render_resources.extend([i.proto() for i in self._render_resources])

	def getrender_resources(self) -> RenderResourceDesc :
		return self._render_resources

	def setrender_resources(self,value : List[RenderResourceDesc]) :
		if self._render_resources != value:
			self._render_resources = value
			self.render_resourcesChanged.emit(value)

	render_resources = pyqtProperty(List, fget=getrender_resources, fset=setrender_resources, notify=render_resourcesChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.script.extend(self._script)
		instance.materials.extend([i.proto() for i in self._materials])
		instance.render_resources.extend([i.proto() for i in self._render_resources])

# ------- RequestVelocity ------- #
class RequestVelocity(QObject) :
	__PROTO__ = sdk.RequestVelocity
	def __init__(self) -> RequestVelocity :
		pass
# ------- ResetConstant ------- #
class ResetConstant(QObject) :
	__PROTO__ = sdk.ResetConstant
	def __init__(self,name_hash :int = int() ) -> ResetConstant :
		self._name_hash = name_hash
		pass
	def getname_hash(self) -> int :
		return self._name_hash

	def setname_hash(self,value : int) :
		if self._name_hash != value:
			self._name_hash = value
			self.name_hashChanged.emit(value)

	name_hash = pyqtProperty(int, fget=getname_hash, fset=setname_hash, notify=name_hashChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.name_hash.extend(self._name_hash)

# ------- ResetConstantParticleFX ------- #
class ResetConstantParticleFX(QObject) :
	__PROTO__ = sdk.ResetConstantParticleFX
	def __init__(self,emitter_id :int = int() ,name_hash :int = int() ) -> ResetConstantParticleFX :
		self._emitter_id = emitter_id
		self._name_hash = name_hash
		pass
	def getemitter_id(self) -> int :
		return self._emitter_id

	def setemitter_id(self,value : int) :
		if self._emitter_id != value:
			self._emitter_id = value
			self.emitter_idChanged.emit(value)

	emitter_id = pyqtProperty(int, fget=getemitter_id, fset=setemitter_id, notify=emitter_idChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.emitter_id.extend(self._emitter_id)
		instance.name_hash.extend(self._name_hash)

	def getname_hash(self) -> int :
		return self._name_hash

	def setname_hash(self,value : int) :
		if self._name_hash != value:
			self._name_hash = value
			self.name_hashChanged.emit(value)

	name_hash = pyqtProperty(int, fget=getname_hash, fset=setname_hash, notify=name_hashChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.emitter_id.extend(self._emitter_id)
		instance.name_hash.extend(self._name_hash)

# ------- ResetConstantTileMap ------- #
class ResetConstantTileMap(QObject) :
	__PROTO__ = sdk.ResetConstantTileMap
	def __init__(self,name_hash :int = int() ) -> ResetConstantTileMap :
		self._name_hash = name_hash
		pass
	def getname_hash(self) -> int :
		return self._name_hash

	def setname_hash(self,value : int) :
		if self._name_hash != value:
			self._name_hash = value
			self.name_hashChanged.emit(value)

	name_hash = pyqtProperty(int, fget=getname_hash, fset=setname_hash, notify=name_hashChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.name_hash.extend(self._name_hash)

# ------- Resize ------- #
class Resize(QObject) :
	__PROTO__ = sdk.Resize
	def __init__(self,width :int = int() ,height :int = int() ) -> Resize :
		self._width = width
		self._height = height
		pass
	def getwidth(self) -> int :
		return self._width

	def setwidth(self,value : int) :
		if self._width != value:
			self._width = value
			self.widthChanged.emit(value)

	width = pyqtProperty(int, fget=getwidth, fset=setwidth, notify=widthChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.width.extend(self._width)
		instance.height.extend(self._height)

	def getheight(self) -> int :
		return self._height

	def setheight(self,value : int) :
		if self._height != value:
			self._height = value
			self.heightChanged.emit(value)

	height = pyqtProperty(int, fget=getheight, fset=setheight, notify=heightChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.width.extend(self._width)
		instance.height.extend(self._height)

# ------- ResourceEntry ------- #
class ResourceEntry(QObject) :
	__PROTO__ = sdk.ResourceEntry
	def __init__(self,hash :HashDigest = None ,url :str = str() ,url_hash :int = int() ,size :int = int() ,compressed_size :int = int() ,flags :int = int() ,dependants :List[int] = [] ) -> ResourceEntry :
		self._hash = hash
		self._url = url
		self._url_hash = url_hash
		self._size = size
		self._compressed_size = compressed_size
		self._flags = flags
		self._dependants = dependants
		pass
	def gethash(self) -> HashDigest :
		return self._hash

	def sethash(self,value : HashDigest) :
		if self._hash != value:
			self._hash = value
			self.hashChanged.emit(value)

	hash = pyqtProperty(QObject, fget=gethash, fset=sethash, notify=hashChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.hash = self._hash.proto()
		instance.url.extend(self._url)
		instance.url_hash.extend(self._url_hash)
		instance.size.extend(self._size)
		instance.compressed_size.extend(self._compressed_size)
		instance.flags.extend(self._flags)
		instance.dependants = self._dependants

	def geturl(self) -> str :
		return self._url

	def seturl(self,value : str) :
		if self._url != value:
			self._url = value
			self.urlChanged.emit(value)

	url = pyqtProperty(str, fget=geturl, fset=seturl, notify=urlChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.hash = self._hash.proto()
		instance.url.extend(self._url)
		instance.url_hash.extend(self._url_hash)
		instance.size.extend(self._size)
		instance.compressed_size.extend(self._compressed_size)
		instance.flags.extend(self._flags)
		instance.dependants = self._dependants

	def geturl_hash(self) -> int :
		return self._url_hash

	def seturl_hash(self,value : int) :
		if self._url_hash != value:
			self._url_hash = value
			self.url_hashChanged.emit(value)

	url_hash = pyqtProperty(int, fget=geturl_hash, fset=seturl_hash, notify=url_hashChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.hash = self._hash.proto()
		instance.url.extend(self._url)
		instance.url_hash.extend(self._url_hash)
		instance.size.extend(self._size)
		instance.compressed_size.extend(self._compressed_size)
		instance.flags.extend(self._flags)
		instance.dependants = self._dependants

	def getsize(self) -> int :
		return self._size

	def setsize(self,value : int) :
		if self._size != value:
			self._size = value
			self.sizeChanged.emit(value)

	size = pyqtProperty(int, fget=getsize, fset=setsize, notify=sizeChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.hash = self._hash.proto()
		instance.url.extend(self._url)
		instance.url_hash.extend(self._url_hash)
		instance.size.extend(self._size)
		instance.compressed_size.extend(self._compressed_size)
		instance.flags.extend(self._flags)
		instance.dependants = self._dependants

	def getcompressed_size(self) -> int :
		return self._compressed_size

	def setcompressed_size(self,value : int) :
		if self._compressed_size != value:
			self._compressed_size = value
			self.compressed_sizeChanged.emit(value)

	compressed_size = pyqtProperty(int, fget=getcompressed_size, fset=setcompressed_size, notify=compressed_sizeChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.hash = self._hash.proto()
		instance.url.extend(self._url)
		instance.url_hash.extend(self._url_hash)
		instance.size.extend(self._size)
		instance.compressed_size.extend(self._compressed_size)
		instance.flags.extend(self._flags)
		instance.dependants = self._dependants

	def getflags(self) -> int :
		return self._flags

	def setflags(self,value : int) :
		if self._flags != value:
			self._flags = value
			self.flagsChanged.emit(value)

	flags = pyqtProperty(int, fget=getflags, fset=setflags, notify=flagsChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.hash = self._hash.proto()
		instance.url.extend(self._url)
		instance.url_hash.extend(self._url_hash)
		instance.size.extend(self._size)
		instance.compressed_size.extend(self._compressed_size)
		instance.flags.extend(self._flags)
		instance.dependants = self._dependants

	def getdependants(self) -> int :
		return self._dependants

	def setdependants(self,value : List[int]) :
		if self._dependants != value:
			self._dependants = value
			self.dependantsChanged.emit(value)

	dependants = pyqtProperty(List, fget=getdependants, fset=setdependants, notify=dependantsChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.hash = self._hash.proto()
		instance.url.extend(self._url)
		instance.url_hash.extend(self._url_hash)
		instance.size.extend(self._size)
		instance.compressed_size.extend(self._compressed_size)
		instance.flags.extend(self._flags)
		instance.dependants = self._dependants

# ------- ResumeRendering ------- #
class ResumeRendering(QObject) :
	__PROTO__ = sdk.ResumeRendering
	def __init__(self) -> ResumeRendering :
		pass
# ------- RunScript ------- #
class RunScript(QObject) :
	__PROTO__ = sdk.RunScript
	def __init__(self,module :LuaModule = None ) -> RunScript :
		self._module = module
		pass
	def getmodule(self) -> LuaModule :
		return self._module

	def setmodule(self,value : LuaModule) :
		if self._module != value:
			self._module = value
			self.moduleChanged.emit(value)

	module = pyqtProperty(QObject, fget=getmodule, fset=setmodule, notify=moduleChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.module = self._module.proto()

# ------- SceneDesc ------- #
class AdjustReference(Enum):
	ADJUST_REFERENCE_LEGACY = 0
	ADJUST_REFERENCE_PARENT = 1
	ADJUST_REFERENCE_DISABLED = 2
class SceneDesc(QObject) :
	__PROTO__ = sdk.SceneDesc
	def __init__(self,script :str = str() ,fonts :List[FontDesc] = [],textures :List[TextureDesc] = [],background_color :Vector4 = None ,nodes :List[NodeDesc] = [],layers :List[LayerDesc] = [],material :str = str() ,layouts :List[LayoutDesc] = [],adjust_reference :int = int() ,max_nodes :int = int() ,spine_scenes :List[SpineSceneDesc] = [],particlefxs :List[ParticleFXDesc] = [],resources :List[ResourceDesc] = [],materials :List[MaterialDesc] = [],max_dynamic_textures :int = int() ) -> SceneDesc :
		self._script = script
		self._fonts = fonts
		self._textures = textures
		self._background_color = background_color
		self._nodes = nodes
		self._layers = layers
		self._material = material
		self._layouts = layouts
		self._adjust_reference = adjust_reference
		self._max_nodes = max_nodes
		self._spine_scenes = spine_scenes
		self._particlefxs = particlefxs
		self._resources = resources
		self._materials = materials
		self._max_dynamic_textures = max_dynamic_textures
		pass
	def getscript(self) -> str :
		return self._script

	def setscript(self,value : str) :
		if self._script != value:
			self._script = value
			self.scriptChanged.emit(value)

	script = pyqtProperty(str, fget=getscript, fset=setscript, notify=scriptChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.script.extend(self._script)
		instance.fonts.extend([i.proto() for i in self._fonts])
		instance.textures.extend([i.proto() for i in self._textures])
		instance.background_color = self._background_color.proto()
		instance.nodes.extend([i.proto() for i in self._nodes])
		instance.layers.extend([i.proto() for i in self._layers])
		instance.material.extend(self._material)
		instance.layouts.extend([i.proto() for i in self._layouts])
		instance.adjust_reference.extend(self._adjust_reference)
		instance.max_nodes.extend(self._max_nodes)
		instance.spine_scenes.extend([i.proto() for i in self._spine_scenes])
		instance.particlefxs.extend([i.proto() for i in self._particlefxs])
		instance.resources.extend([i.proto() for i in self._resources])
		instance.materials.extend([i.proto() for i in self._materials])
		instance.max_dynamic_textures.extend(self._max_dynamic_textures)

	def getfonts(self) -> FontDesc :
		return self._fonts

	def setfonts(self,value : List[FontDesc]) :
		if self._fonts != value:
			self._fonts = value
			self.fontsChanged.emit(value)

	fonts = pyqtProperty(List, fget=getfonts, fset=setfonts, notify=fontsChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.script.extend(self._script)
		instance.fonts.extend([i.proto() for i in self._fonts])
		instance.textures.extend([i.proto() for i in self._textures])
		instance.background_color = self._background_color.proto()
		instance.nodes.extend([i.proto() for i in self._nodes])
		instance.layers.extend([i.proto() for i in self._layers])
		instance.material.extend(self._material)
		instance.layouts.extend([i.proto() for i in self._layouts])
		instance.adjust_reference.extend(self._adjust_reference)
		instance.max_nodes.extend(self._max_nodes)
		instance.spine_scenes.extend([i.proto() for i in self._spine_scenes])
		instance.particlefxs.extend([i.proto() for i in self._particlefxs])
		instance.resources.extend([i.proto() for i in self._resources])
		instance.materials.extend([i.proto() for i in self._materials])
		instance.max_dynamic_textures.extend(self._max_dynamic_textures)

	def gettextures(self) -> TextureDesc :
		return self._textures

	def settextures(self,value : List[TextureDesc]) :
		if self._textures != value:
			self._textures = value
			self.texturesChanged.emit(value)

	textures = pyqtProperty(List, fget=gettextures, fset=settextures, notify=texturesChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.script.extend(self._script)
		instance.fonts.extend([i.proto() for i in self._fonts])
		instance.textures.extend([i.proto() for i in self._textures])
		instance.background_color = self._background_color.proto()
		instance.nodes.extend([i.proto() for i in self._nodes])
		instance.layers.extend([i.proto() for i in self._layers])
		instance.material.extend(self._material)
		instance.layouts.extend([i.proto() for i in self._layouts])
		instance.adjust_reference.extend(self._adjust_reference)
		instance.max_nodes.extend(self._max_nodes)
		instance.spine_scenes.extend([i.proto() for i in self._spine_scenes])
		instance.particlefxs.extend([i.proto() for i in self._particlefxs])
		instance.resources.extend([i.proto() for i in self._resources])
		instance.materials.extend([i.proto() for i in self._materials])
		instance.max_dynamic_textures.extend(self._max_dynamic_textures)

	def getbackground_color(self) -> Vector4 :
		return self._background_color

	def setbackground_color(self,value : Vector4) :
		if self._background_color != value:
			self._background_color = value
			self.background_colorChanged.emit(value)

	background_color = pyqtProperty(QObject, fget=getbackground_color, fset=setbackground_color, notify=background_colorChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.script.extend(self._script)
		instance.fonts.extend([i.proto() for i in self._fonts])
		instance.textures.extend([i.proto() for i in self._textures])
		instance.background_color = self._background_color.proto()
		instance.nodes.extend([i.proto() for i in self._nodes])
		instance.layers.extend([i.proto() for i in self._layers])
		instance.material.extend(self._material)
		instance.layouts.extend([i.proto() for i in self._layouts])
		instance.adjust_reference.extend(self._adjust_reference)
		instance.max_nodes.extend(self._max_nodes)
		instance.spine_scenes.extend([i.proto() for i in self._spine_scenes])
		instance.particlefxs.extend([i.proto() for i in self._particlefxs])
		instance.resources.extend([i.proto() for i in self._resources])
		instance.materials.extend([i.proto() for i in self._materials])
		instance.max_dynamic_textures.extend(self._max_dynamic_textures)

	def getnodes(self) -> NodeDesc :
		return self._nodes

	def setnodes(self,value : List[NodeDesc]) :
		if self._nodes != value:
			self._nodes = value
			self.nodesChanged.emit(value)

	nodes = pyqtProperty(List, fget=getnodes, fset=setnodes, notify=nodesChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.script.extend(self._script)
		instance.fonts.extend([i.proto() for i in self._fonts])
		instance.textures.extend([i.proto() for i in self._textures])
		instance.background_color = self._background_color.proto()
		instance.nodes.extend([i.proto() for i in self._nodes])
		instance.layers.extend([i.proto() for i in self._layers])
		instance.material.extend(self._material)
		instance.layouts.extend([i.proto() for i in self._layouts])
		instance.adjust_reference.extend(self._adjust_reference)
		instance.max_nodes.extend(self._max_nodes)
		instance.spine_scenes.extend([i.proto() for i in self._spine_scenes])
		instance.particlefxs.extend([i.proto() for i in self._particlefxs])
		instance.resources.extend([i.proto() for i in self._resources])
		instance.materials.extend([i.proto() for i in self._materials])
		instance.max_dynamic_textures.extend(self._max_dynamic_textures)

	def getlayers(self) -> LayerDesc :
		return self._layers

	def setlayers(self,value : List[LayerDesc]) :
		if self._layers != value:
			self._layers = value
			self.layersChanged.emit(value)

	layers = pyqtProperty(List, fget=getlayers, fset=setlayers, notify=layersChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.script.extend(self._script)
		instance.fonts.extend([i.proto() for i in self._fonts])
		instance.textures.extend([i.proto() for i in self._textures])
		instance.background_color = self._background_color.proto()
		instance.nodes.extend([i.proto() for i in self._nodes])
		instance.layers.extend([i.proto() for i in self._layers])
		instance.material.extend(self._material)
		instance.layouts.extend([i.proto() for i in self._layouts])
		instance.adjust_reference.extend(self._adjust_reference)
		instance.max_nodes.extend(self._max_nodes)
		instance.spine_scenes.extend([i.proto() for i in self._spine_scenes])
		instance.particlefxs.extend([i.proto() for i in self._particlefxs])
		instance.resources.extend([i.proto() for i in self._resources])
		instance.materials.extend([i.proto() for i in self._materials])
		instance.max_dynamic_textures.extend(self._max_dynamic_textures)

	def getmaterial(self) -> str :
		return self._material

	def setmaterial(self,value : str) :
		if self._material != value:
			self._material = value
			self.materialChanged.emit(value)

	material = pyqtProperty(str, fget=getmaterial, fset=setmaterial, notify=materialChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.script.extend(self._script)
		instance.fonts.extend([i.proto() for i in self._fonts])
		instance.textures.extend([i.proto() for i in self._textures])
		instance.background_color = self._background_color.proto()
		instance.nodes.extend([i.proto() for i in self._nodes])
		instance.layers.extend([i.proto() for i in self._layers])
		instance.material.extend(self._material)
		instance.layouts.extend([i.proto() for i in self._layouts])
		instance.adjust_reference.extend(self._adjust_reference)
		instance.max_nodes.extend(self._max_nodes)
		instance.spine_scenes.extend([i.proto() for i in self._spine_scenes])
		instance.particlefxs.extend([i.proto() for i in self._particlefxs])
		instance.resources.extend([i.proto() for i in self._resources])
		instance.materials.extend([i.proto() for i in self._materials])
		instance.max_dynamic_textures.extend(self._max_dynamic_textures)

	def getlayouts(self) -> LayoutDesc :
		return self._layouts

	def setlayouts(self,value : List[LayoutDesc]) :
		if self._layouts != value:
			self._layouts = value
			self.layoutsChanged.emit(value)

	layouts = pyqtProperty(List, fget=getlayouts, fset=setlayouts, notify=layoutsChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.script.extend(self._script)
		instance.fonts.extend([i.proto() for i in self._fonts])
		instance.textures.extend([i.proto() for i in self._textures])
		instance.background_color = self._background_color.proto()
		instance.nodes.extend([i.proto() for i in self._nodes])
		instance.layers.extend([i.proto() for i in self._layers])
		instance.material.extend(self._material)
		instance.layouts.extend([i.proto() for i in self._layouts])
		instance.adjust_reference.extend(self._adjust_reference)
		instance.max_nodes.extend(self._max_nodes)
		instance.spine_scenes.extend([i.proto() for i in self._spine_scenes])
		instance.particlefxs.extend([i.proto() for i in self._particlefxs])
		instance.resources.extend([i.proto() for i in self._resources])
		instance.materials.extend([i.proto() for i in self._materials])
		instance.max_dynamic_textures.extend(self._max_dynamic_textures)

	def getadjust_reference(self) -> int :
		return self._adjust_reference

	def setadjust_reference(self,value : int) :
		if self._adjust_reference != value:
			self._adjust_reference = value
			self.adjust_referenceChanged.emit(value)

	adjust_reference = pyqtProperty(int, fget=getadjust_reference, fset=setadjust_reference, notify=adjust_referenceChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.script.extend(self._script)
		instance.fonts.extend([i.proto() for i in self._fonts])
		instance.textures.extend([i.proto() for i in self._textures])
		instance.background_color = self._background_color.proto()
		instance.nodes.extend([i.proto() for i in self._nodes])
		instance.layers.extend([i.proto() for i in self._layers])
		instance.material.extend(self._material)
		instance.layouts.extend([i.proto() for i in self._layouts])
		instance.adjust_reference.extend(self._adjust_reference)
		instance.max_nodes.extend(self._max_nodes)
		instance.spine_scenes.extend([i.proto() for i in self._spine_scenes])
		instance.particlefxs.extend([i.proto() for i in self._particlefxs])
		instance.resources.extend([i.proto() for i in self._resources])
		instance.materials.extend([i.proto() for i in self._materials])
		instance.max_dynamic_textures.extend(self._max_dynamic_textures)

	def getmax_nodes(self) -> int :
		return self._max_nodes

	def setmax_nodes(self,value : int) :
		if self._max_nodes != value:
			self._max_nodes = value
			self.max_nodesChanged.emit(value)

	max_nodes = pyqtProperty(int, fget=getmax_nodes, fset=setmax_nodes, notify=max_nodesChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.script.extend(self._script)
		instance.fonts.extend([i.proto() for i in self._fonts])
		instance.textures.extend([i.proto() for i in self._textures])
		instance.background_color = self._background_color.proto()
		instance.nodes.extend([i.proto() for i in self._nodes])
		instance.layers.extend([i.proto() for i in self._layers])
		instance.material.extend(self._material)
		instance.layouts.extend([i.proto() for i in self._layouts])
		instance.adjust_reference.extend(self._adjust_reference)
		instance.max_nodes.extend(self._max_nodes)
		instance.spine_scenes.extend([i.proto() for i in self._spine_scenes])
		instance.particlefxs.extend([i.proto() for i in self._particlefxs])
		instance.resources.extend([i.proto() for i in self._resources])
		instance.materials.extend([i.proto() for i in self._materials])
		instance.max_dynamic_textures.extend(self._max_dynamic_textures)

	def getspine_scenes(self) -> SpineSceneDesc :
		return self._spine_scenes

	def setspine_scenes(self,value : List[SpineSceneDesc]) :
		if self._spine_scenes != value:
			self._spine_scenes = value
			self.spine_scenesChanged.emit(value)

	spine_scenes = pyqtProperty(List, fget=getspine_scenes, fset=setspine_scenes, notify=spine_scenesChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.script.extend(self._script)
		instance.fonts.extend([i.proto() for i in self._fonts])
		instance.textures.extend([i.proto() for i in self._textures])
		instance.background_color = self._background_color.proto()
		instance.nodes.extend([i.proto() for i in self._nodes])
		instance.layers.extend([i.proto() for i in self._layers])
		instance.material.extend(self._material)
		instance.layouts.extend([i.proto() for i in self._layouts])
		instance.adjust_reference.extend(self._adjust_reference)
		instance.max_nodes.extend(self._max_nodes)
		instance.spine_scenes.extend([i.proto() for i in self._spine_scenes])
		instance.particlefxs.extend([i.proto() for i in self._particlefxs])
		instance.resources.extend([i.proto() for i in self._resources])
		instance.materials.extend([i.proto() for i in self._materials])
		instance.max_dynamic_textures.extend(self._max_dynamic_textures)

	def getparticlefxs(self) -> ParticleFXDesc :
		return self._particlefxs

	def setparticlefxs(self,value : List[ParticleFXDesc]) :
		if self._particlefxs != value:
			self._particlefxs = value
			self.particlefxsChanged.emit(value)

	particlefxs = pyqtProperty(List, fget=getparticlefxs, fset=setparticlefxs, notify=particlefxsChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.script.extend(self._script)
		instance.fonts.extend([i.proto() for i in self._fonts])
		instance.textures.extend([i.proto() for i in self._textures])
		instance.background_color = self._background_color.proto()
		instance.nodes.extend([i.proto() for i in self._nodes])
		instance.layers.extend([i.proto() for i in self._layers])
		instance.material.extend(self._material)
		instance.layouts.extend([i.proto() for i in self._layouts])
		instance.adjust_reference.extend(self._adjust_reference)
		instance.max_nodes.extend(self._max_nodes)
		instance.spine_scenes.extend([i.proto() for i in self._spine_scenes])
		instance.particlefxs.extend([i.proto() for i in self._particlefxs])
		instance.resources.extend([i.proto() for i in self._resources])
		instance.materials.extend([i.proto() for i in self._materials])
		instance.max_dynamic_textures.extend(self._max_dynamic_textures)

	def getresources(self) -> ResourceDesc :
		return self._resources

	def setresources(self,value : List[ResourceDesc]) :
		if self._resources != value:
			self._resources = value
			self.resourcesChanged.emit(value)

	resources = pyqtProperty(List, fget=getresources, fset=setresources, notify=resourcesChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.script.extend(self._script)
		instance.fonts.extend([i.proto() for i in self._fonts])
		instance.textures.extend([i.proto() for i in self._textures])
		instance.background_color = self._background_color.proto()
		instance.nodes.extend([i.proto() for i in self._nodes])
		instance.layers.extend([i.proto() for i in self._layers])
		instance.material.extend(self._material)
		instance.layouts.extend([i.proto() for i in self._layouts])
		instance.adjust_reference.extend(self._adjust_reference)
		instance.max_nodes.extend(self._max_nodes)
		instance.spine_scenes.extend([i.proto() for i in self._spine_scenes])
		instance.particlefxs.extend([i.proto() for i in self._particlefxs])
		instance.resources.extend([i.proto() for i in self._resources])
		instance.materials.extend([i.proto() for i in self._materials])
		instance.max_dynamic_textures.extend(self._max_dynamic_textures)

	def getmaterials(self) -> MaterialDesc :
		return self._materials

	def setmaterials(self,value : List[MaterialDesc]) :
		if self._materials != value:
			self._materials = value
			self.materialsChanged.emit(value)

	materials = pyqtProperty(List, fget=getmaterials, fset=setmaterials, notify=materialsChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.script.extend(self._script)
		instance.fonts.extend([i.proto() for i in self._fonts])
		instance.textures.extend([i.proto() for i in self._textures])
		instance.background_color = self._background_color.proto()
		instance.nodes.extend([i.proto() for i in self._nodes])
		instance.layers.extend([i.proto() for i in self._layers])
		instance.material.extend(self._material)
		instance.layouts.extend([i.proto() for i in self._layouts])
		instance.adjust_reference.extend(self._adjust_reference)
		instance.max_nodes.extend(self._max_nodes)
		instance.spine_scenes.extend([i.proto() for i in self._spine_scenes])
		instance.particlefxs.extend([i.proto() for i in self._particlefxs])
		instance.resources.extend([i.proto() for i in self._resources])
		instance.materials.extend([i.proto() for i in self._materials])
		instance.max_dynamic_textures.extend(self._max_dynamic_textures)

	def getmax_dynamic_textures(self) -> int :
		return self._max_dynamic_textures

	def setmax_dynamic_textures(self,value : int) :
		if self._max_dynamic_textures != value:
			self._max_dynamic_textures = value
			self.max_dynamic_texturesChanged.emit(value)

	max_dynamic_textures = pyqtProperty(int, fget=getmax_dynamic_textures, fset=setmax_dynamic_textures, notify=max_dynamic_texturesChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.script.extend(self._script)
		instance.fonts.extend([i.proto() for i in self._fonts])
		instance.textures.extend([i.proto() for i in self._textures])
		instance.background_color = self._background_color.proto()
		instance.nodes.extend([i.proto() for i in self._nodes])
		instance.layers.extend([i.proto() for i in self._layers])
		instance.material.extend(self._material)
		instance.layouts.extend([i.proto() for i in self._layouts])
		instance.adjust_reference.extend(self._adjust_reference)
		instance.max_nodes.extend(self._max_nodes)
		instance.spine_scenes.extend([i.proto() for i in self._spine_scenes])
		instance.particlefxs.extend([i.proto() for i in self._particlefxs])
		instance.resources.extend([i.proto() for i in self._resources])
		instance.materials.extend([i.proto() for i in self._materials])
		instance.max_dynamic_textures.extend(self._max_dynamic_textures)

# ------- ScriptMessage ------- #
class ScriptMessage(QObject) :
	__PROTO__ = sdk.ScriptMessage
	def __init__(self,descriptor_hash :int = int() ,payload_size :int = int() ,function :int = int() ,unref_function :bool = bool() ) -> ScriptMessage :
		self._descriptor_hash = descriptor_hash
		self._payload_size = payload_size
		self._function = function
		self._unref_function = unref_function
		pass
	def getdescriptor_hash(self) -> int :
		return self._descriptor_hash

	def setdescriptor_hash(self,value : int) :
		if self._descriptor_hash != value:
			self._descriptor_hash = value
			self.descriptor_hashChanged.emit(value)

	descriptor_hash = pyqtProperty(int, fget=getdescriptor_hash, fset=setdescriptor_hash, notify=descriptor_hashChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.descriptor_hash.extend(self._descriptor_hash)
		instance.payload_size.extend(self._payload_size)
		instance.function.extend(self._function)
		instance.unref_function.extend(self._unref_function)

	def getpayload_size(self) -> int :
		return self._payload_size

	def setpayload_size(self,value : int) :
		if self._payload_size != value:
			self._payload_size = value
			self.payload_sizeChanged.emit(value)

	payload_size = pyqtProperty(int, fget=getpayload_size, fset=setpayload_size, notify=payload_sizeChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.descriptor_hash.extend(self._descriptor_hash)
		instance.payload_size.extend(self._payload_size)
		instance.function.extend(self._function)
		instance.unref_function.extend(self._unref_function)

	def getfunction(self) -> int :
		return self._function

	def setfunction(self,value : int) :
		if self._function != value:
			self._function = value
			self.functionChanged.emit(value)

	function = pyqtProperty(int, fget=getfunction, fset=setfunction, notify=functionChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.descriptor_hash.extend(self._descriptor_hash)
		instance.payload_size.extend(self._payload_size)
		instance.function.extend(self._function)
		instance.unref_function.extend(self._unref_function)

	def getunref_function(self) -> bool :
		return self._unref_function

	def setunref_function(self,value : bool) :
		if self._unref_function != value:
			self._unref_function = value
			self.unref_functionChanged.emit(value)

	unref_function = pyqtProperty(bool, fget=getunref_function, fset=setunref_function, notify=unref_functionChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.descriptor_hash.extend(self._descriptor_hash)
		instance.payload_size.extend(self._payload_size)
		instance.function.extend(self._function)
		instance.unref_function.extend(self._unref_function)

# ------- ScriptUnrefMessage ------- #
class ScriptUnrefMessage(QObject) :
	__PROTO__ = sdk.ScriptUnrefMessage
	def __init__(self,reference :int = int() ) -> ScriptUnrefMessage :
		self._reference = reference
		pass
	def getreference(self) -> int :
		return self._reference

	def setreference(self,value : int) :
		if self._reference != value:
			self._reference = value
			self.referenceChanged.emit(value)

	reference = pyqtProperty(int, fget=getreference, fset=setreference, notify=referenceChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.reference.extend(self._reference)

# ------- SetCamera ------- #
class SetCamera(QObject) :
	__PROTO__ = sdk.SetCamera
	def __init__(self,aspect_ratio :float = float() ,fov :float = float() ,near_z :float = float() ,far_z :float = float() ,orthographic_projection :int = int() ,orthographic_zoom :float = float() ,orthographic_mode :int = int() ) -> SetCamera :
		self._aspect_ratio = aspect_ratio
		self._fov = fov
		self._near_z = near_z
		self._far_z = far_z
		self._orthographic_projection = orthographic_projection
		self._orthographic_zoom = orthographic_zoom
		self._orthographic_mode = orthographic_mode
		pass
	def getaspect_ratio(self) -> float :
		return self._aspect_ratio

	def setaspect_ratio(self,value : float) :
		if self._aspect_ratio != value:
			self._aspect_ratio = value
			self.aspect_ratioChanged.emit(value)

	aspect_ratio = pyqtProperty(float, fget=getaspect_ratio, fset=setaspect_ratio, notify=aspect_ratioChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.aspect_ratio.extend(self._aspect_ratio)
		instance.fov.extend(self._fov)
		instance.near_z.extend(self._near_z)
		instance.far_z.extend(self._far_z)
		instance.orthographic_projection.extend(self._orthographic_projection)
		instance.orthographic_zoom.extend(self._orthographic_zoom)
		instance.orthographic_mode.extend(self._orthographic_mode)

	def getfov(self) -> float :
		return self._fov

	def setfov(self,value : float) :
		if self._fov != value:
			self._fov = value
			self.fovChanged.emit(value)

	fov = pyqtProperty(float, fget=getfov, fset=setfov, notify=fovChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.aspect_ratio.extend(self._aspect_ratio)
		instance.fov.extend(self._fov)
		instance.near_z.extend(self._near_z)
		instance.far_z.extend(self._far_z)
		instance.orthographic_projection.extend(self._orthographic_projection)
		instance.orthographic_zoom.extend(self._orthographic_zoom)
		instance.orthographic_mode.extend(self._orthographic_mode)

	def getnear_z(self) -> float :
		return self._near_z

	def setnear_z(self,value : float) :
		if self._near_z != value:
			self._near_z = value
			self.near_zChanged.emit(value)

	near_z = pyqtProperty(float, fget=getnear_z, fset=setnear_z, notify=near_zChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.aspect_ratio.extend(self._aspect_ratio)
		instance.fov.extend(self._fov)
		instance.near_z.extend(self._near_z)
		instance.far_z.extend(self._far_z)
		instance.orthographic_projection.extend(self._orthographic_projection)
		instance.orthographic_zoom.extend(self._orthographic_zoom)
		instance.orthographic_mode.extend(self._orthographic_mode)

	def getfar_z(self) -> float :
		return self._far_z

	def setfar_z(self,value : float) :
		if self._far_z != value:
			self._far_z = value
			self.far_zChanged.emit(value)

	far_z = pyqtProperty(float, fget=getfar_z, fset=setfar_z, notify=far_zChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.aspect_ratio.extend(self._aspect_ratio)
		instance.fov.extend(self._fov)
		instance.near_z.extend(self._near_z)
		instance.far_z.extend(self._far_z)
		instance.orthographic_projection.extend(self._orthographic_projection)
		instance.orthographic_zoom.extend(self._orthographic_zoom)
		instance.orthographic_mode.extend(self._orthographic_mode)

	def getorthographic_projection(self) -> int :
		return self._orthographic_projection

	def setorthographic_projection(self,value : int) :
		if self._orthographic_projection != value:
			self._orthographic_projection = value
			self.orthographic_projectionChanged.emit(value)

	orthographic_projection = pyqtProperty(int, fget=getorthographic_projection, fset=setorthographic_projection, notify=orthographic_projectionChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.aspect_ratio.extend(self._aspect_ratio)
		instance.fov.extend(self._fov)
		instance.near_z.extend(self._near_z)
		instance.far_z.extend(self._far_z)
		instance.orthographic_projection.extend(self._orthographic_projection)
		instance.orthographic_zoom.extend(self._orthographic_zoom)
		instance.orthographic_mode.extend(self._orthographic_mode)

	def getorthographic_zoom(self) -> float :
		return self._orthographic_zoom

	def setorthographic_zoom(self,value : float) :
		if self._orthographic_zoom != value:
			self._orthographic_zoom = value
			self.orthographic_zoomChanged.emit(value)

	orthographic_zoom = pyqtProperty(float, fget=getorthographic_zoom, fset=setorthographic_zoom, notify=orthographic_zoomChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.aspect_ratio.extend(self._aspect_ratio)
		instance.fov.extend(self._fov)
		instance.near_z.extend(self._near_z)
		instance.far_z.extend(self._far_z)
		instance.orthographic_projection.extend(self._orthographic_projection)
		instance.orthographic_zoom.extend(self._orthographic_zoom)
		instance.orthographic_mode.extend(self._orthographic_mode)

	def getorthographic_mode(self) -> int :
		return self._orthographic_mode

	def setorthographic_mode(self,value : int) :
		if self._orthographic_mode != value:
			self._orthographic_mode = value
			self.orthographic_modeChanged.emit(value)

	orthographic_mode = pyqtProperty(int, fget=getorthographic_mode, fset=setorthographic_mode, notify=orthographic_modeChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.aspect_ratio.extend(self._aspect_ratio)
		instance.fov.extend(self._fov)
		instance.near_z.extend(self._near_z)
		instance.far_z.extend(self._far_z)
		instance.orthographic_projection.extend(self._orthographic_projection)
		instance.orthographic_zoom.extend(self._orthographic_zoom)
		instance.orthographic_mode.extend(self._orthographic_mode)

# ------- SetConstant ------- #
class SetConstant(QObject) :
	__PROTO__ = sdk.SetConstant
	def __init__(self,name_hash :int = int() ,value :Vector4 = None ,index :int = int() ) -> SetConstant :
		self._name_hash = name_hash
		self._value = value
		self._index = index
		pass
	def getname_hash(self) -> int :
		return self._name_hash

	def setname_hash(self,value : int) :
		if self._name_hash != value:
			self._name_hash = value
			self.name_hashChanged.emit(value)

	name_hash = pyqtProperty(int, fget=getname_hash, fset=setname_hash, notify=name_hashChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.name_hash.extend(self._name_hash)
		instance.value = self._value.proto()
		instance.index.extend(self._index)

	def getvalue(self) -> Vector4 :
		return self._value

	def setvalue(self,value : Vector4) :
		if self._value != value:
			self._value = value
			self.valueChanged.emit(value)

	value = pyqtProperty(QObject, fget=getvalue, fset=setvalue, notify=valueChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.name_hash.extend(self._name_hash)
		instance.value = self._value.proto()
		instance.index.extend(self._index)

	def getindex(self) -> int :
		return self._index

	def setindex(self,value : int) :
		if self._index != value:
			self._index = value
			self.indexChanged.emit(value)

	index = pyqtProperty(int, fget=getindex, fset=setindex, notify=indexChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.name_hash.extend(self._name_hash)
		instance.value = self._value.proto()
		instance.index.extend(self._index)

# ------- SetConstantParticleFX ------- #
class SetConstantParticleFX(QObject) :
	__PROTO__ = sdk.SetConstantParticleFX
	def __init__(self,emitter_id :int = int() ,name_hash :int = int() ,value :Matrix4 = None ,is_matrix4 :bool = bool() ) -> SetConstantParticleFX :
		self._emitter_id = emitter_id
		self._name_hash = name_hash
		self._value = value
		self._is_matrix4 = is_matrix4
		pass
	def getemitter_id(self) -> int :
		return self._emitter_id

	def setemitter_id(self,value : int) :
		if self._emitter_id != value:
			self._emitter_id = value
			self.emitter_idChanged.emit(value)

	emitter_id = pyqtProperty(int, fget=getemitter_id, fset=setemitter_id, notify=emitter_idChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.emitter_id.extend(self._emitter_id)
		instance.name_hash.extend(self._name_hash)
		instance.value = self._value.proto()
		instance.is_matrix4.extend(self._is_matrix4)

	def getname_hash(self) -> int :
		return self._name_hash

	def setname_hash(self,value : int) :
		if self._name_hash != value:
			self._name_hash = value
			self.name_hashChanged.emit(value)

	name_hash = pyqtProperty(int, fget=getname_hash, fset=setname_hash, notify=name_hashChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.emitter_id.extend(self._emitter_id)
		instance.name_hash.extend(self._name_hash)
		instance.value = self._value.proto()
		instance.is_matrix4.extend(self._is_matrix4)

	def getvalue(self) -> Matrix4 :
		return self._value

	def setvalue(self,value : Matrix4) :
		if self._value != value:
			self._value = value
			self.valueChanged.emit(value)

	value = pyqtProperty(QObject, fget=getvalue, fset=setvalue, notify=valueChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.emitter_id.extend(self._emitter_id)
		instance.name_hash.extend(self._name_hash)
		instance.value = self._value.proto()
		instance.is_matrix4.extend(self._is_matrix4)

	def getis_matrix4(self) -> bool :
		return self._is_matrix4

	def setis_matrix4(self,value : bool) :
		if self._is_matrix4 != value:
			self._is_matrix4 = value
			self.is_matrix4Changed.emit(value)

	is_matrix4 = pyqtProperty(bool, fget=getis_matrix4, fset=setis_matrix4, notify=is_matrix4Changed)

	def proto(self) :
		instance = self.__PROTO__()
		instance.emitter_id.extend(self._emitter_id)
		instance.name_hash.extend(self._name_hash)
		instance.value = self._value.proto()
		instance.is_matrix4.extend(self._is_matrix4)

# ------- SetConstantTileMap ------- #
class SetConstantTileMap(QObject) :
	__PROTO__ = sdk.SetConstantTileMap
	def __init__(self,name_hash :int = int() ,value :Vector4 = None ) -> SetConstantTileMap :
		self._name_hash = name_hash
		self._value = value
		pass
	def getname_hash(self) -> int :
		return self._name_hash

	def setname_hash(self,value : int) :
		if self._name_hash != value:
			self._name_hash = value
			self.name_hashChanged.emit(value)

	name_hash = pyqtProperty(int, fget=getname_hash, fset=setname_hash, notify=name_hashChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.name_hash.extend(self._name_hash)
		instance.value = self._value.proto()

	def getvalue(self) -> Vector4 :
		return self._value

	def setvalue(self,value : Vector4) :
		if self._value != value:
			self._value = value
			self.valueChanged.emit(value)

	value = pyqtProperty(QObject, fget=getvalue, fset=setvalue, notify=valueChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.name_hash.extend(self._name_hash)
		instance.value = self._value.proto()

# ------- SetFlipHorizontal ------- #
class SetFlipHorizontal(QObject) :
	__PROTO__ = sdk.SetFlipHorizontal
	def __init__(self,flip :int = int() ) -> SetFlipHorizontal :
		self._flip = flip
		pass
	def getflip(self) -> int :
		return self._flip

	def setflip(self,value : int) :
		if self._flip != value:
			self._flip = value
			self.flipChanged.emit(value)

	flip = pyqtProperty(int, fget=getflip, fset=setflip, notify=flipChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.flip.extend(self._flip)

# ------- SetFlipVertical ------- #
class SetFlipVertical(QObject) :
	__PROTO__ = sdk.SetFlipVertical
	def __init__(self,flip :int = int() ) -> SetFlipVertical :
		self._flip = flip
		pass
	def getflip(self) -> int :
		return self._flip

	def setflip(self,value : int) :
		if self._flip != value:
			self._flip = value
			self.flipChanged.emit(value)

	flip = pyqtProperty(int, fget=getflip, fset=setflip, notify=flipChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.flip.extend(self._flip)

# ------- SetGain ------- #
class SetGain(QObject) :
	__PROTO__ = sdk.SetGain
	def __init__(self,gain :float = float() ) -> SetGain :
		self._gain = gain
		pass
	def getgain(self) -> float :
		return self._gain

	def setgain(self,value : float) :
		if self._gain != value:
			self._gain = value
			self.gainChanged.emit(value)

	gain = pyqtProperty(float, fget=getgain, fset=setgain, notify=gainChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.gain.extend(self._gain)

# ------- SetGridShapeHull ------- #
class SetGridShapeHull(QObject) :
	__PROTO__ = sdk.SetGridShapeHull
	def __init__(self,shape :int = int() ,row :int = int() ,column :int = int() ,hull :int = int() ,flip_horizontal :int = int() ,flip_vertical :int = int() ,rotate90 :int = int() ) -> SetGridShapeHull :
		self._shape = shape
		self._row = row
		self._column = column
		self._hull = hull
		self._flip_horizontal = flip_horizontal
		self._flip_vertical = flip_vertical
		self._rotate90 = rotate90
		pass
	def getshape(self) -> int :
		return self._shape

	def setshape(self,value : int) :
		if self._shape != value:
			self._shape = value
			self.shapeChanged.emit(value)

	shape = pyqtProperty(int, fget=getshape, fset=setshape, notify=shapeChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.shape.extend(self._shape)
		instance.row.extend(self._row)
		instance.column.extend(self._column)
		instance.hull.extend(self._hull)
		instance.flip_horizontal.extend(self._flip_horizontal)
		instance.flip_vertical.extend(self._flip_vertical)
		instance.rotate90.extend(self._rotate90)

	def getrow(self) -> int :
		return self._row

	def setrow(self,value : int) :
		if self._row != value:
			self._row = value
			self.rowChanged.emit(value)

	row = pyqtProperty(int, fget=getrow, fset=setrow, notify=rowChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.shape.extend(self._shape)
		instance.row.extend(self._row)
		instance.column.extend(self._column)
		instance.hull.extend(self._hull)
		instance.flip_horizontal.extend(self._flip_horizontal)
		instance.flip_vertical.extend(self._flip_vertical)
		instance.rotate90.extend(self._rotate90)

	def getcolumn(self) -> int :
		return self._column

	def setcolumn(self,value : int) :
		if self._column != value:
			self._column = value
			self.columnChanged.emit(value)

	column = pyqtProperty(int, fget=getcolumn, fset=setcolumn, notify=columnChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.shape.extend(self._shape)
		instance.row.extend(self._row)
		instance.column.extend(self._column)
		instance.hull.extend(self._hull)
		instance.flip_horizontal.extend(self._flip_horizontal)
		instance.flip_vertical.extend(self._flip_vertical)
		instance.rotate90.extend(self._rotate90)

	def gethull(self) -> int :
		return self._hull

	def sethull(self,value : int) :
		if self._hull != value:
			self._hull = value
			self.hullChanged.emit(value)

	hull = pyqtProperty(int, fget=gethull, fset=sethull, notify=hullChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.shape.extend(self._shape)
		instance.row.extend(self._row)
		instance.column.extend(self._column)
		instance.hull.extend(self._hull)
		instance.flip_horizontal.extend(self._flip_horizontal)
		instance.flip_vertical.extend(self._flip_vertical)
		instance.rotate90.extend(self._rotate90)

	def getflip_horizontal(self) -> int :
		return self._flip_horizontal

	def setflip_horizontal(self,value : int) :
		if self._flip_horizontal != value:
			self._flip_horizontal = value
			self.flip_horizontalChanged.emit(value)

	flip_horizontal = pyqtProperty(int, fget=getflip_horizontal, fset=setflip_horizontal, notify=flip_horizontalChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.shape.extend(self._shape)
		instance.row.extend(self._row)
		instance.column.extend(self._column)
		instance.hull.extend(self._hull)
		instance.flip_horizontal.extend(self._flip_horizontal)
		instance.flip_vertical.extend(self._flip_vertical)
		instance.rotate90.extend(self._rotate90)

	def getflip_vertical(self) -> int :
		return self._flip_vertical

	def setflip_vertical(self,value : int) :
		if self._flip_vertical != value:
			self._flip_vertical = value
			self.flip_verticalChanged.emit(value)

	flip_vertical = pyqtProperty(int, fget=getflip_vertical, fset=setflip_vertical, notify=flip_verticalChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.shape.extend(self._shape)
		instance.row.extend(self._row)
		instance.column.extend(self._column)
		instance.hull.extend(self._hull)
		instance.flip_horizontal.extend(self._flip_horizontal)
		instance.flip_vertical.extend(self._flip_vertical)
		instance.rotate90.extend(self._rotate90)

	def getrotate90(self) -> int :
		return self._rotate90

	def setrotate90(self,value : int) :
		if self._rotate90 != value:
			self._rotate90 = value
			self.rotate90Changed.emit(value)

	rotate90 = pyqtProperty(int, fget=getrotate90, fset=setrotate90, notify=rotate90Changed)

	def proto(self) :
		instance = self.__PROTO__()
		instance.shape.extend(self._shape)
		instance.row.extend(self._row)
		instance.column.extend(self._column)
		instance.hull.extend(self._hull)
		instance.flip_horizontal.extend(self._flip_horizontal)
		instance.flip_vertical.extend(self._flip_vertical)
		instance.rotate90.extend(self._rotate90)

# ------- SetLight ------- #
class SetLight(QObject) :
	__PROTO__ = sdk.SetLight
	def __init__(self,position :Point3 = None ,rotation :Quat = None ,light :LightDesc = None ) -> SetLight :
		self._position = position
		self._rotation = rotation
		self._light = light
		pass
	def getposition(self) -> Point3 :
		return self._position

	def setposition(self,value : Point3) :
		if self._position != value:
			self._position = value
			self.positionChanged.emit(value)

	position = pyqtProperty(QObject, fget=getposition, fset=setposition, notify=positionChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.position = self._position.proto()
		instance.rotation = self._rotation.proto()
		instance.light = self._light.proto()

	def getrotation(self) -> Quat :
		return self._rotation

	def setrotation(self,value : Quat) :
		if self._rotation != value:
			self._rotation = value
			self.rotationChanged.emit(value)

	rotation = pyqtProperty(QObject, fget=getrotation, fset=setrotation, notify=rotationChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.position = self._position.proto()
		instance.rotation = self._rotation.proto()
		instance.light = self._light.proto()

	def getlight(self) -> LightDesc :
		return self._light

	def setlight(self,value : LightDesc) :
		if self._light != value:
			self._light = value
			self.lightChanged.emit(value)

	light = pyqtProperty(QObject, fget=getlight, fset=setlight, notify=lightChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.position = self._position.proto()
		instance.rotation = self._rotation.proto()
		instance.light = self._light.proto()

# ------- SetPan ------- #
class SetPan(QObject) :
	__PROTO__ = sdk.SetPan
	def __init__(self,pan :float = float() ) -> SetPan :
		self._pan = pan
		pass
	def getpan(self) -> float :
		return self._pan

	def setpan(self,value : float) :
		if self._pan != value:
			self._pan = value
			self.panChanged.emit(value)

	pan = pyqtProperty(float, fget=getpan, fset=setpan, notify=panChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.pan.extend(self._pan)

# ------- SetParent ------- #
class SetParent(QObject) :
	__PROTO__ = sdk.SetParent
	def __init__(self,parent_id :int = int() ,keep_world_transform :int = int() ) -> SetParent :
		self._parent_id = parent_id
		self._keep_world_transform = keep_world_transform
		pass
	def getparent_id(self) -> int :
		return self._parent_id

	def setparent_id(self,value : int) :
		if self._parent_id != value:
			self._parent_id = value
			self.parent_idChanged.emit(value)

	parent_id = pyqtProperty(int, fget=getparent_id, fset=setparent_id, notify=parent_idChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.parent_id.extend(self._parent_id)
		instance.keep_world_transform.extend(self._keep_world_transform)

	def getkeep_world_transform(self) -> int :
		return self._keep_world_transform

	def setkeep_world_transform(self,value : int) :
		if self._keep_world_transform != value:
			self._keep_world_transform = value
			self.keep_world_transformChanged.emit(value)

	keep_world_transform = pyqtProperty(int, fget=getkeep_world_transform, fset=setkeep_world_transform, notify=keep_world_transformChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.parent_id.extend(self._parent_id)
		instance.keep_world_transform.extend(self._keep_world_transform)

# ------- SetScale ------- #
class SetScale(QObject) :
	__PROTO__ = sdk.SetScale
	def __init__(self,scale :Vector3 = None ) -> SetScale :
		self._scale = scale
		pass
	def getscale(self) -> Vector3 :
		return self._scale

	def setscale(self,value : Vector3) :
		if self._scale != value:
			self._scale = value
			self.scaleChanged.emit(value)

	scale = pyqtProperty(QObject, fget=getscale, fset=setscale, notify=scaleChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.scale = self._scale.proto()

# ------- SetSpeed ------- #
class SetSpeed(QObject) :
	__PROTO__ = sdk.SetSpeed
	def __init__(self,speed :float = float() ) -> SetSpeed :
		self._speed = speed
		pass
	def getspeed(self) -> float :
		return self._speed

	def setspeed(self,value : float) :
		if self._speed != value:
			self._speed = value
			self.speedChanged.emit(value)

	speed = pyqtProperty(float, fget=getspeed, fset=setspeed, notify=speedChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.speed.extend(self._speed)

# ------- SetText ------- #
class SetText(QObject) :
	__PROTO__ = sdk.SetText
	def __init__(self,text :str = str() ) -> SetText :
		self._text = text
		pass
	def gettext(self) -> str :
		return self._text

	def settext(self,value : str) :
		if self._text != value:
			self._text = value
			self.textChanged.emit(value)

	text = pyqtProperty(str, fget=gettext, fset=settext, notify=textChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.text.extend(self._text)

# ------- SetTexture ------- #
class SetTexture(QObject) :
	__PROTO__ = sdk.SetTexture
	def __init__(self,texture_hash :int = int() ,texture_unit :int = int() ) -> SetTexture :
		self._texture_hash = texture_hash
		self._texture_unit = texture_unit
		pass
	def gettexture_hash(self) -> int :
		return self._texture_hash

	def settexture_hash(self,value : int) :
		if self._texture_hash != value:
			self._texture_hash = value
			self.texture_hashChanged.emit(value)

	texture_hash = pyqtProperty(int, fget=gettexture_hash, fset=settexture_hash, notify=texture_hashChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.texture_hash.extend(self._texture_hash)
		instance.texture_unit.extend(self._texture_unit)

	def gettexture_unit(self) -> int :
		return self._texture_unit

	def settexture_unit(self,value : int) :
		if self._texture_unit != value:
			self._texture_unit = value
			self.texture_unitChanged.emit(value)

	texture_unit = pyqtProperty(int, fget=gettexture_unit, fset=settexture_unit, notify=texture_unitChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.texture_hash.extend(self._texture_hash)
		instance.texture_unit.extend(self._texture_unit)

# ------- SetTimeStep ------- #
class SetTimeStep(QObject) :
	__PROTO__ = sdk.SetTimeStep
	def __init__(self,factor :float = float() ,mode :int = int() ) -> SetTimeStep :
		self._factor = factor
		self._mode = mode
		pass
	def getfactor(self) -> float :
		return self._factor

	def setfactor(self,value : float) :
		if self._factor != value:
			self._factor = value
			self.factorChanged.emit(value)

	factor = pyqtProperty(float, fget=getfactor, fset=setfactor, notify=factorChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.factor.extend(self._factor)
		instance.mode.extend(self._mode)

	def getmode(self) -> int :
		return self._mode

	def setmode(self,value : int) :
		if self._mode != value:
			self._mode = value
			self.modeChanged.emit(value)

	mode = pyqtProperty(int, fget=getmode, fset=setmode, notify=modeChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.factor.extend(self._factor)
		instance.mode.extend(self._mode)

# ------- SetUpdateFrequency ------- #
class SetUpdateFrequency(QObject) :
	__PROTO__ = sdk.SetUpdateFrequency
	def __init__(self,frequency :int = int() ) -> SetUpdateFrequency :
		self._frequency = frequency
		pass
	def getfrequency(self) -> int :
		return self._frequency

	def setfrequency(self,value : int) :
		if self._frequency != value:
			self._frequency = value
			self.frequencyChanged.emit(value)

	frequency = pyqtProperty(int, fget=getfrequency, fset=setfrequency, notify=frequencyChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.frequency.extend(self._frequency)

# ------- SetViewProjection ------- #
class SetViewProjection(QObject) :
	__PROTO__ = sdk.SetViewProjection
	def __init__(self,id :int = int() ,view :Matrix4 = None ,projection :Matrix4 = None ) -> SetViewProjection :
		self._id = id
		self._view = view
		self._projection = projection
		pass
	def getid(self) -> int :
		return self._id

	def setid(self,value : int) :
		if self._id != value:
			self._id = value
			self.idChanged.emit(value)

	id = pyqtProperty(int, fget=getid, fset=setid, notify=idChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.id.extend(self._id)
		instance.view = self._view.proto()
		instance.projection = self._projection.proto()

	def getview(self) -> Matrix4 :
		return self._view

	def setview(self,value : Matrix4) :
		if self._view != value:
			self._view = value
			self.viewChanged.emit(value)

	view = pyqtProperty(QObject, fget=getview, fset=setview, notify=viewChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.id.extend(self._id)
		instance.view = self._view.proto()
		instance.projection = self._projection.proto()

	def getprojection(self) -> Matrix4 :
		return self._projection

	def setprojection(self,value : Matrix4) :
		if self._projection != value:
			self._projection = value
			self.projectionChanged.emit(value)

	projection = pyqtProperty(QObject, fget=getprojection, fset=setprojection, notify=projectionChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.id.extend(self._id)
		instance.view = self._view.proto()
		instance.projection = self._projection.proto()

# ------- SetVsync ------- #
class SetVsync(QObject) :
	__PROTO__ = sdk.SetVsync
	def __init__(self,swap_interval :int = int() ) -> SetVsync :
		self._swap_interval = swap_interval
		pass
	def getswap_interval(self) -> int :
		return self._swap_interval

	def setswap_interval(self,value : int) :
		if self._swap_interval != value:
			self._swap_interval = value
			self.swap_intervalChanged.emit(value)

	swap_interval = pyqtProperty(int, fget=getswap_interval, fset=setswap_interval, notify=swap_intervalChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.swap_interval.extend(self._swap_interval)

# ------- ShaderDesc ------- #
class Language(Enum):
	LANGUAGE_GLSL_SM120 = 1
	LANGUAGE_GLES_SM100 = 2
	LANGUAGE_GLES_SM300 = 3
	LANGUAGE_SPIRV = 4
	LANGUAGE_PSSL = 5
	LANGUAGE_GLSL_SM430 = 6
	LANGUAGE_GLSL_SM330 = 7
	LANGUAGE_WGSL = 8
	LANGUAGE_HLSL_50 = 9
	LANGUAGE_HLSL_51 = 10
class ShaderType(Enum):
	SHADER_TYPE_VERTEX = 0
	SHADER_TYPE_FRAGMENT = 1
	SHADER_TYPE_COMPUTE = 2
class ShaderDataType(Enum):
	SHADER_TYPE_UNKNOWN = 0
	SHADER_TYPE_INT = 1
	SHADER_TYPE_UINT = 2
	SHADER_TYPE_FLOAT = 3
	SHADER_TYPE_VEC2 = 4
	SHADER_TYPE_VEC3 = 5
	SHADER_TYPE_VEC4 = 6
	SHADER_TYPE_MAT2 = 7
	SHADER_TYPE_MAT3 = 8
	SHADER_TYPE_MAT4 = 9
	SHADER_TYPE_SAMPLER2D = 10
	SHADER_TYPE_SAMPLER3D = 11
	SHADER_TYPE_SAMPLER_CUBE = 12
	SHADER_TYPE_SAMPLER2D_ARRAY = 13
	SHADER_TYPE_UNIFORM_BUFFER = 14
	SHADER_TYPE_UVEC2 = 15
	SHADER_TYPE_UVEC3 = 16
	SHADER_TYPE_UVEC4 = 17
	SHADER_TYPE_TEXTURE2D = 18
	SHADER_TYPE_UTEXTURE2D = 19
	SHADER_TYPE_RENDER_PASS_INPUT = 20
	SHADER_TYPE_UIMAGE2D = 21
	SHADER_TYPE_IMAGE2D = 22
	SHADER_TYPE_SAMPLER = 23
	SHADER_TYPE_STORAGE_BUFFER = 24
	SHADER_TYPE_TEXTURE2D_ARRAY = 25
	SHADER_TYPE_TEXTURE_CUBE = 26
	SHADER_TYPE_TEXTURE3D = 27
	SHADER_TYPE_UTEXTURE3D = 28
	SHADER_TYPE_UIMAGE3D = 29
	SHADER_TYPE_IMAGE3D = 30
	SHADER_TYPE_SAMPLER3D_ARRAY = 31
	SHADER_TYPE_TEXTURE3D_ARRAY = 32
class ShaderDesc(QObject) :
	__PROTO__ = sdk.ShaderDesc
	def __init__(self,shaders :List[Shader] = [],reflection :ShaderReflection = None ) -> ShaderDesc :
		self._shaders = shaders
		self._reflection = reflection
		pass
	def getshaders(self) -> Shader :
		return self._shaders

	def setshaders(self,value : List[Shader]) :
		if self._shaders != value:
			self._shaders = value
			self.shadersChanged.emit(value)

	shaders = pyqtProperty(List, fget=getshaders, fset=setshaders, notify=shadersChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.shaders.extend([i.proto() for i in self._shaders])
		instance.reflection = self._reflection.proto()

	def getreflection(self) -> ShaderReflection :
		return self._reflection

	def setreflection(self,value : ShaderReflection) :
		if self._reflection != value:
			self._reflection = value
			self.reflectionChanged.emit(value)

	reflection = pyqtProperty(QObject, fget=getreflection, fset=setreflection, notify=reflectionChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.shaders.extend([i.proto() for i in self._shaders])
		instance.reflection = self._reflection.proto()

# ------- SoundDesc ------- #
class SoundDesc(QObject) :
	__PROTO__ = sdk.SoundDesc
	def __init__(self,sound :str = str() ,looping :int = int() ,group :str = str() ,gain :float = float() ,pan :float = float() ,speed :float = float() ,loopcount :int = int() ) -> SoundDesc :
		self._sound = sound
		self._looping = looping
		self._group = group
		self._gain = gain
		self._pan = pan
		self._speed = speed
		self._loopcount = loopcount
		pass
	def getsound(self) -> str :
		return self._sound

	def setsound(self,value : str) :
		if self._sound != value:
			self._sound = value
			self.soundChanged.emit(value)

	sound = pyqtProperty(str, fget=getsound, fset=setsound, notify=soundChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.sound.extend(self._sound)
		instance.looping.extend(self._looping)
		instance.group.extend(self._group)
		instance.gain.extend(self._gain)
		instance.pan.extend(self._pan)
		instance.speed.extend(self._speed)
		instance.loopcount.extend(self._loopcount)

	def getlooping(self) -> int :
		return self._looping

	def setlooping(self,value : int) :
		if self._looping != value:
			self._looping = value
			self.loopingChanged.emit(value)

	looping = pyqtProperty(int, fget=getlooping, fset=setlooping, notify=loopingChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.sound.extend(self._sound)
		instance.looping.extend(self._looping)
		instance.group.extend(self._group)
		instance.gain.extend(self._gain)
		instance.pan.extend(self._pan)
		instance.speed.extend(self._speed)
		instance.loopcount.extend(self._loopcount)

	def getgroup(self) -> str :
		return self._group

	def setgroup(self,value : str) :
		if self._group != value:
			self._group = value
			self.groupChanged.emit(value)

	group = pyqtProperty(str, fget=getgroup, fset=setgroup, notify=groupChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.sound.extend(self._sound)
		instance.looping.extend(self._looping)
		instance.group.extend(self._group)
		instance.gain.extend(self._gain)
		instance.pan.extend(self._pan)
		instance.speed.extend(self._speed)
		instance.loopcount.extend(self._loopcount)

	def getgain(self) -> float :
		return self._gain

	def setgain(self,value : float) :
		if self._gain != value:
			self._gain = value
			self.gainChanged.emit(value)

	gain = pyqtProperty(float, fget=getgain, fset=setgain, notify=gainChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.sound.extend(self._sound)
		instance.looping.extend(self._looping)
		instance.group.extend(self._group)
		instance.gain.extend(self._gain)
		instance.pan.extend(self._pan)
		instance.speed.extend(self._speed)
		instance.loopcount.extend(self._loopcount)

	def getpan(self) -> float :
		return self._pan

	def setpan(self,value : float) :
		if self._pan != value:
			self._pan = value
			self.panChanged.emit(value)

	pan = pyqtProperty(float, fget=getpan, fset=setpan, notify=panChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.sound.extend(self._sound)
		instance.looping.extend(self._looping)
		instance.group.extend(self._group)
		instance.gain.extend(self._gain)
		instance.pan.extend(self._pan)
		instance.speed.extend(self._speed)
		instance.loopcount.extend(self._loopcount)

	def getspeed(self) -> float :
		return self._speed

	def setspeed(self,value : float) :
		if self._speed != value:
			self._speed = value
			self.speedChanged.emit(value)

	speed = pyqtProperty(float, fget=getspeed, fset=setspeed, notify=speedChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.sound.extend(self._sound)
		instance.looping.extend(self._looping)
		instance.group.extend(self._group)
		instance.gain.extend(self._gain)
		instance.pan.extend(self._pan)
		instance.speed.extend(self._speed)
		instance.loopcount.extend(self._loopcount)

	def getloopcount(self) -> int :
		return self._loopcount

	def setloopcount(self,value : int) :
		if self._loopcount != value:
			self._loopcount = value
			self.loopcountChanged.emit(value)

	loopcount = pyqtProperty(int, fget=getloopcount, fset=setloopcount, notify=loopcountChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.sound.extend(self._sound)
		instance.looping.extend(self._looping)
		instance.group.extend(self._group)
		instance.gain.extend(self._gain)
		instance.pan.extend(self._pan)
		instance.speed.extend(self._speed)
		instance.loopcount.extend(self._loopcount)

# ------- SoundEvent ------- #
class SoundEvent(QObject) :
	__PROTO__ = sdk.SoundEvent
	def __init__(self,play_id :int = int() ) -> SoundEvent :
		self._play_id = play_id
		pass
	def getplay_id(self) -> int :
		return self._play_id

	def setplay_id(self,value : int) :
		if self._play_id != value:
			self._play_id = value
			self.play_idChanged.emit(value)

	play_id = pyqtProperty(int, fget=getplay_id, fset=setplay_id, notify=play_idChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.play_id.extend(self._play_id)

# ------- SpriteDesc ------- #
class BlendMode(Enum):
	BLEND_MODE_ALPHA = 0
	BLEND_MODE_ADD = 1
	BLEND_MODE_ADD_ALPHA = 2
	BLEND_MODE_MULT = 3
	BLEND_MODE_SCREEN = 4
class SizeMode(Enum):
	SIZE_MODE_MANUAL = 0
	SIZE_MODE_AUTO = 1
class SpriteDesc(QObject) :
	__PROTO__ = sdk.SpriteDesc
	def __init__(self,tile_set :str = str() ,default_animation :str = str() ,material :str = str() ,blend_mode :int = int() ,slice9 :Vector4 = None ,size :Vector4 = None ,size_mode :int = int() ,offset :float = float() ,playback_rate :float = float() ,attributes :List[VertexAttribute] = [],textures :List[SpriteTexture] = []) -> SpriteDesc :
		self._tile_set = tile_set
		self._default_animation = default_animation
		self._material = material
		self._blend_mode = blend_mode
		self._slice9 = slice9
		self._size = size
		self._size_mode = size_mode
		self._offset = offset
		self._playback_rate = playback_rate
		self._attributes = attributes
		self._textures = textures
		pass
	def gettile_set(self) -> str :
		return self._tile_set

	def settile_set(self,value : str) :
		if self._tile_set != value:
			self._tile_set = value
			self.tile_setChanged.emit(value)

	tile_set = pyqtProperty(str, fget=gettile_set, fset=settile_set, notify=tile_setChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.tile_set.extend(self._tile_set)
		instance.default_animation.extend(self._default_animation)
		instance.material.extend(self._material)
		instance.blend_mode.extend(self._blend_mode)
		instance.slice9 = self._slice9.proto()
		instance.size = self._size.proto()
		instance.size_mode.extend(self._size_mode)
		instance.offset.extend(self._offset)
		instance.playback_rate.extend(self._playback_rate)
		instance.attributes.extend([i.proto() for i in self._attributes])
		instance.textures.extend([i.proto() for i in self._textures])

	def getdefault_animation(self) -> str :
		return self._default_animation

	def setdefault_animation(self,value : str) :
		if self._default_animation != value:
			self._default_animation = value
			self.default_animationChanged.emit(value)

	default_animation = pyqtProperty(str, fget=getdefault_animation, fset=setdefault_animation, notify=default_animationChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.tile_set.extend(self._tile_set)
		instance.default_animation.extend(self._default_animation)
		instance.material.extend(self._material)
		instance.blend_mode.extend(self._blend_mode)
		instance.slice9 = self._slice9.proto()
		instance.size = self._size.proto()
		instance.size_mode.extend(self._size_mode)
		instance.offset.extend(self._offset)
		instance.playback_rate.extend(self._playback_rate)
		instance.attributes.extend([i.proto() for i in self._attributes])
		instance.textures.extend([i.proto() for i in self._textures])

	def getmaterial(self) -> str :
		return self._material

	def setmaterial(self,value : str) :
		if self._material != value:
			self._material = value
			self.materialChanged.emit(value)

	material = pyqtProperty(str, fget=getmaterial, fset=setmaterial, notify=materialChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.tile_set.extend(self._tile_set)
		instance.default_animation.extend(self._default_animation)
		instance.material.extend(self._material)
		instance.blend_mode.extend(self._blend_mode)
		instance.slice9 = self._slice9.proto()
		instance.size = self._size.proto()
		instance.size_mode.extend(self._size_mode)
		instance.offset.extend(self._offset)
		instance.playback_rate.extend(self._playback_rate)
		instance.attributes.extend([i.proto() for i in self._attributes])
		instance.textures.extend([i.proto() for i in self._textures])

	def getblend_mode(self) -> int :
		return self._blend_mode

	def setblend_mode(self,value : int) :
		if self._blend_mode != value:
			self._blend_mode = value
			self.blend_modeChanged.emit(value)

	blend_mode = pyqtProperty(int, fget=getblend_mode, fset=setblend_mode, notify=blend_modeChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.tile_set.extend(self._tile_set)
		instance.default_animation.extend(self._default_animation)
		instance.material.extend(self._material)
		instance.blend_mode.extend(self._blend_mode)
		instance.slice9 = self._slice9.proto()
		instance.size = self._size.proto()
		instance.size_mode.extend(self._size_mode)
		instance.offset.extend(self._offset)
		instance.playback_rate.extend(self._playback_rate)
		instance.attributes.extend([i.proto() for i in self._attributes])
		instance.textures.extend([i.proto() for i in self._textures])

	def getslice9(self) -> Vector4 :
		return self._slice9

	def setslice9(self,value : Vector4) :
		if self._slice9 != value:
			self._slice9 = value
			self.slice9Changed.emit(value)

	slice9 = pyqtProperty(QObject, fget=getslice9, fset=setslice9, notify=slice9Changed)

	def proto(self) :
		instance = self.__PROTO__()
		instance.tile_set.extend(self._tile_set)
		instance.default_animation.extend(self._default_animation)
		instance.material.extend(self._material)
		instance.blend_mode.extend(self._blend_mode)
		instance.slice9 = self._slice9.proto()
		instance.size = self._size.proto()
		instance.size_mode.extend(self._size_mode)
		instance.offset.extend(self._offset)
		instance.playback_rate.extend(self._playback_rate)
		instance.attributes.extend([i.proto() for i in self._attributes])
		instance.textures.extend([i.proto() for i in self._textures])

	def getsize(self) -> Vector4 :
		return self._size

	def setsize(self,value : Vector4) :
		if self._size != value:
			self._size = value
			self.sizeChanged.emit(value)

	size = pyqtProperty(QObject, fget=getsize, fset=setsize, notify=sizeChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.tile_set.extend(self._tile_set)
		instance.default_animation.extend(self._default_animation)
		instance.material.extend(self._material)
		instance.blend_mode.extend(self._blend_mode)
		instance.slice9 = self._slice9.proto()
		instance.size = self._size.proto()
		instance.size_mode.extend(self._size_mode)
		instance.offset.extend(self._offset)
		instance.playback_rate.extend(self._playback_rate)
		instance.attributes.extend([i.proto() for i in self._attributes])
		instance.textures.extend([i.proto() for i in self._textures])

	def getsize_mode(self) -> int :
		return self._size_mode

	def setsize_mode(self,value : int) :
		if self._size_mode != value:
			self._size_mode = value
			self.size_modeChanged.emit(value)

	size_mode = pyqtProperty(int, fget=getsize_mode, fset=setsize_mode, notify=size_modeChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.tile_set.extend(self._tile_set)
		instance.default_animation.extend(self._default_animation)
		instance.material.extend(self._material)
		instance.blend_mode.extend(self._blend_mode)
		instance.slice9 = self._slice9.proto()
		instance.size = self._size.proto()
		instance.size_mode.extend(self._size_mode)
		instance.offset.extend(self._offset)
		instance.playback_rate.extend(self._playback_rate)
		instance.attributes.extend([i.proto() for i in self._attributes])
		instance.textures.extend([i.proto() for i in self._textures])

	def getoffset(self) -> float :
		return self._offset

	def setoffset(self,value : float) :
		if self._offset != value:
			self._offset = value
			self.offsetChanged.emit(value)

	offset = pyqtProperty(float, fget=getoffset, fset=setoffset, notify=offsetChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.tile_set.extend(self._tile_set)
		instance.default_animation.extend(self._default_animation)
		instance.material.extend(self._material)
		instance.blend_mode.extend(self._blend_mode)
		instance.slice9 = self._slice9.proto()
		instance.size = self._size.proto()
		instance.size_mode.extend(self._size_mode)
		instance.offset.extend(self._offset)
		instance.playback_rate.extend(self._playback_rate)
		instance.attributes.extend([i.proto() for i in self._attributes])
		instance.textures.extend([i.proto() for i in self._textures])

	def getplayback_rate(self) -> float :
		return self._playback_rate

	def setplayback_rate(self,value : float) :
		if self._playback_rate != value:
			self._playback_rate = value
			self.playback_rateChanged.emit(value)

	playback_rate = pyqtProperty(float, fget=getplayback_rate, fset=setplayback_rate, notify=playback_rateChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.tile_set.extend(self._tile_set)
		instance.default_animation.extend(self._default_animation)
		instance.material.extend(self._material)
		instance.blend_mode.extend(self._blend_mode)
		instance.slice9 = self._slice9.proto()
		instance.size = self._size.proto()
		instance.size_mode.extend(self._size_mode)
		instance.offset.extend(self._offset)
		instance.playback_rate.extend(self._playback_rate)
		instance.attributes.extend([i.proto() for i in self._attributes])
		instance.textures.extend([i.proto() for i in self._textures])

	def getattributes(self) -> VertexAttribute :
		return self._attributes

	def setattributes(self,value : List[VertexAttribute]) :
		if self._attributes != value:
			self._attributes = value
			self.attributesChanged.emit(value)

	attributes = pyqtProperty(List, fget=getattributes, fset=setattributes, notify=attributesChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.tile_set.extend(self._tile_set)
		instance.default_animation.extend(self._default_animation)
		instance.material.extend(self._material)
		instance.blend_mode.extend(self._blend_mode)
		instance.slice9 = self._slice9.proto()
		instance.size = self._size.proto()
		instance.size_mode.extend(self._size_mode)
		instance.offset.extend(self._offset)
		instance.playback_rate.extend(self._playback_rate)
		instance.attributes.extend([i.proto() for i in self._attributes])
		instance.textures.extend([i.proto() for i in self._textures])

	def gettextures(self) -> SpriteTexture :
		return self._textures

	def settextures(self,value : List[SpriteTexture]) :
		if self._textures != value:
			self._textures = value
			self.texturesChanged.emit(value)

	textures = pyqtProperty(List, fget=gettextures, fset=settextures, notify=texturesChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.tile_set.extend(self._tile_set)
		instance.default_animation.extend(self._default_animation)
		instance.material.extend(self._material)
		instance.blend_mode.extend(self._blend_mode)
		instance.slice9 = self._slice9.proto()
		instance.size = self._size.proto()
		instance.size_mode.extend(self._size_mode)
		instance.offset.extend(self._offset)
		instance.playback_rate.extend(self._playback_rate)
		instance.attributes.extend([i.proto() for i in self._attributes])
		instance.textures.extend([i.proto() for i in self._textures])

# ------- SpriteGeometry ------- #
class SpriteGeometry(QObject) :
	__PROTO__ = sdk.SpriteGeometry
	def __init__(self,width :int = int() ,height :int = int() ,center_x :float = float() ,center_y :float = float() ,rotated :bool = bool() ,trim_mode :int = int() ,vertices :List[float] = [] ,uvs :List[float] = [] ,indices :List[int] = [] ,pivot_x :float = float() ,pivot_y :float = float() ) -> SpriteGeometry :
		self._width = width
		self._height = height
		self._center_x = center_x
		self._center_y = center_y
		self._rotated = rotated
		self._trim_mode = trim_mode
		self._vertices = vertices
		self._uvs = uvs
		self._indices = indices
		self._pivot_x = pivot_x
		self._pivot_y = pivot_y
		pass
	def getwidth(self) -> int :
		return self._width

	def setwidth(self,value : int) :
		if self._width != value:
			self._width = value
			self.widthChanged.emit(value)

	width = pyqtProperty(int, fget=getwidth, fset=setwidth, notify=widthChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.width.extend(self._width)
		instance.height.extend(self._height)
		instance.center_x.extend(self._center_x)
		instance.center_y.extend(self._center_y)
		instance.rotated.extend(self._rotated)
		instance.trim_mode.extend(self._trim_mode)
		instance.vertices = self._vertices
		instance.uvs = self._uvs
		instance.indices = self._indices
		instance.pivot_x.extend(self._pivot_x)
		instance.pivot_y.extend(self._pivot_y)

	def getheight(self) -> int :
		return self._height

	def setheight(self,value : int) :
		if self._height != value:
			self._height = value
			self.heightChanged.emit(value)

	height = pyqtProperty(int, fget=getheight, fset=setheight, notify=heightChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.width.extend(self._width)
		instance.height.extend(self._height)
		instance.center_x.extend(self._center_x)
		instance.center_y.extend(self._center_y)
		instance.rotated.extend(self._rotated)
		instance.trim_mode.extend(self._trim_mode)
		instance.vertices = self._vertices
		instance.uvs = self._uvs
		instance.indices = self._indices
		instance.pivot_x.extend(self._pivot_x)
		instance.pivot_y.extend(self._pivot_y)

	def getcenter_x(self) -> float :
		return self._center_x

	def setcenter_x(self,value : float) :
		if self._center_x != value:
			self._center_x = value
			self.center_xChanged.emit(value)

	center_x = pyqtProperty(float, fget=getcenter_x, fset=setcenter_x, notify=center_xChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.width.extend(self._width)
		instance.height.extend(self._height)
		instance.center_x.extend(self._center_x)
		instance.center_y.extend(self._center_y)
		instance.rotated.extend(self._rotated)
		instance.trim_mode.extend(self._trim_mode)
		instance.vertices = self._vertices
		instance.uvs = self._uvs
		instance.indices = self._indices
		instance.pivot_x.extend(self._pivot_x)
		instance.pivot_y.extend(self._pivot_y)

	def getcenter_y(self) -> float :
		return self._center_y

	def setcenter_y(self,value : float) :
		if self._center_y != value:
			self._center_y = value
			self.center_yChanged.emit(value)

	center_y = pyqtProperty(float, fget=getcenter_y, fset=setcenter_y, notify=center_yChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.width.extend(self._width)
		instance.height.extend(self._height)
		instance.center_x.extend(self._center_x)
		instance.center_y.extend(self._center_y)
		instance.rotated.extend(self._rotated)
		instance.trim_mode.extend(self._trim_mode)
		instance.vertices = self._vertices
		instance.uvs = self._uvs
		instance.indices = self._indices
		instance.pivot_x.extend(self._pivot_x)
		instance.pivot_y.extend(self._pivot_y)

	def getrotated(self) -> bool :
		return self._rotated

	def setrotated(self,value : bool) :
		if self._rotated != value:
			self._rotated = value
			self.rotatedChanged.emit(value)

	rotated = pyqtProperty(bool, fget=getrotated, fset=setrotated, notify=rotatedChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.width.extend(self._width)
		instance.height.extend(self._height)
		instance.center_x.extend(self._center_x)
		instance.center_y.extend(self._center_y)
		instance.rotated.extend(self._rotated)
		instance.trim_mode.extend(self._trim_mode)
		instance.vertices = self._vertices
		instance.uvs = self._uvs
		instance.indices = self._indices
		instance.pivot_x.extend(self._pivot_x)
		instance.pivot_y.extend(self._pivot_y)

	def gettrim_mode(self) -> int :
		return self._trim_mode

	def settrim_mode(self,value : int) :
		if self._trim_mode != value:
			self._trim_mode = value
			self.trim_modeChanged.emit(value)

	trim_mode = pyqtProperty(int, fget=gettrim_mode, fset=settrim_mode, notify=trim_modeChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.width.extend(self._width)
		instance.height.extend(self._height)
		instance.center_x.extend(self._center_x)
		instance.center_y.extend(self._center_y)
		instance.rotated.extend(self._rotated)
		instance.trim_mode.extend(self._trim_mode)
		instance.vertices = self._vertices
		instance.uvs = self._uvs
		instance.indices = self._indices
		instance.pivot_x.extend(self._pivot_x)
		instance.pivot_y.extend(self._pivot_y)

	def getvertices(self) -> float :
		return self._vertices

	def setvertices(self,value : List[float]) :
		if self._vertices != value:
			self._vertices = value
			self.verticesChanged.emit(value)

	vertices = pyqtProperty(List, fget=getvertices, fset=setvertices, notify=verticesChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.width.extend(self._width)
		instance.height.extend(self._height)
		instance.center_x.extend(self._center_x)
		instance.center_y.extend(self._center_y)
		instance.rotated.extend(self._rotated)
		instance.trim_mode.extend(self._trim_mode)
		instance.vertices = self._vertices
		instance.uvs = self._uvs
		instance.indices = self._indices
		instance.pivot_x.extend(self._pivot_x)
		instance.pivot_y.extend(self._pivot_y)

	def getuvs(self) -> float :
		return self._uvs

	def setuvs(self,value : List[float]) :
		if self._uvs != value:
			self._uvs = value
			self.uvsChanged.emit(value)

	uvs = pyqtProperty(List, fget=getuvs, fset=setuvs, notify=uvsChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.width.extend(self._width)
		instance.height.extend(self._height)
		instance.center_x.extend(self._center_x)
		instance.center_y.extend(self._center_y)
		instance.rotated.extend(self._rotated)
		instance.trim_mode.extend(self._trim_mode)
		instance.vertices = self._vertices
		instance.uvs = self._uvs
		instance.indices = self._indices
		instance.pivot_x.extend(self._pivot_x)
		instance.pivot_y.extend(self._pivot_y)

	def getindices(self) -> int :
		return self._indices

	def setindices(self,value : List[int]) :
		if self._indices != value:
			self._indices = value
			self.indicesChanged.emit(value)

	indices = pyqtProperty(List, fget=getindices, fset=setindices, notify=indicesChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.width.extend(self._width)
		instance.height.extend(self._height)
		instance.center_x.extend(self._center_x)
		instance.center_y.extend(self._center_y)
		instance.rotated.extend(self._rotated)
		instance.trim_mode.extend(self._trim_mode)
		instance.vertices = self._vertices
		instance.uvs = self._uvs
		instance.indices = self._indices
		instance.pivot_x.extend(self._pivot_x)
		instance.pivot_y.extend(self._pivot_y)

	def getpivot_x(self) -> float :
		return self._pivot_x

	def setpivot_x(self,value : float) :
		if self._pivot_x != value:
			self._pivot_x = value
			self.pivot_xChanged.emit(value)

	pivot_x = pyqtProperty(float, fget=getpivot_x, fset=setpivot_x, notify=pivot_xChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.width.extend(self._width)
		instance.height.extend(self._height)
		instance.center_x.extend(self._center_x)
		instance.center_y.extend(self._center_y)
		instance.rotated.extend(self._rotated)
		instance.trim_mode.extend(self._trim_mode)
		instance.vertices = self._vertices
		instance.uvs = self._uvs
		instance.indices = self._indices
		instance.pivot_x.extend(self._pivot_x)
		instance.pivot_y.extend(self._pivot_y)

	def getpivot_y(self) -> float :
		return self._pivot_y

	def setpivot_y(self,value : float) :
		if self._pivot_y != value:
			self._pivot_y = value
			self.pivot_yChanged.emit(value)

	pivot_y = pyqtProperty(float, fget=getpivot_y, fset=setpivot_y, notify=pivot_yChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.width.extend(self._width)
		instance.height.extend(self._height)
		instance.center_x.extend(self._center_x)
		instance.center_y.extend(self._center_y)
		instance.rotated.extend(self._rotated)
		instance.trim_mode.extend(self._trim_mode)
		instance.vertices = self._vertices
		instance.uvs = self._uvs
		instance.indices = self._indices
		instance.pivot_x.extend(self._pivot_x)
		instance.pivot_y.extend(self._pivot_y)

# ------- SpriteTexture ------- #
class SpriteTexture(QObject) :
	__PROTO__ = sdk.SpriteTexture
	def __init__(self,sampler :str = str() ,texture :str = str() ) -> SpriteTexture :
		self._sampler = sampler
		self._texture = texture
		pass
	def getsampler(self) -> str :
		return self._sampler

	def setsampler(self,value : str) :
		if self._sampler != value:
			self._sampler = value
			self.samplerChanged.emit(value)

	sampler = pyqtProperty(str, fget=getsampler, fset=setsampler, notify=samplerChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.sampler.extend(self._sampler)
		instance.texture.extend(self._texture)

	def gettexture(self) -> str :
		return self._texture

	def settexture(self,value : str) :
		if self._texture != value:
			self._texture = value
			self.textureChanged.emit(value)

	texture = pyqtProperty(str, fget=gettexture, fset=settexture, notify=textureChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.sampler.extend(self._sampler)
		instance.texture.extend(self._texture)

# ------- StartRecord ------- #
class StartRecord(QObject) :
	__PROTO__ = sdk.StartRecord
	def __init__(self,file_name :str = str() ,frame_period :int = int() ,fps :int = int() ) -> StartRecord :
		self._file_name = file_name
		self._frame_period = frame_period
		self._fps = fps
		pass
	def getfile_name(self) -> str :
		return self._file_name

	def setfile_name(self,value : str) :
		if self._file_name != value:
			self._file_name = value
			self.file_nameChanged.emit(value)

	file_name = pyqtProperty(str, fget=getfile_name, fset=setfile_name, notify=file_nameChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.file_name.extend(self._file_name)
		instance.frame_period.extend(self._frame_period)
		instance.fps.extend(self._fps)

	def getframe_period(self) -> int :
		return self._frame_period

	def setframe_period(self,value : int) :
		if self._frame_period != value:
			self._frame_period = value
			self.frame_periodChanged.emit(value)

	frame_period = pyqtProperty(int, fget=getframe_period, fset=setframe_period, notify=frame_periodChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.file_name.extend(self._file_name)
		instance.frame_period.extend(self._frame_period)
		instance.fps.extend(self._fps)

	def getfps(self) -> int :
		return self._fps

	def setfps(self,value : int) :
		if self._fps != value:
			self._fps = value
			self.fpsChanged.emit(value)

	fps = pyqtProperty(int, fget=getfps, fset=setfps, notify=fpsChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.file_name.extend(self._file_name)
		instance.frame_period.extend(self._frame_period)
		instance.fps.extend(self._fps)

# ------- StopParticleFX ------- #
class StopParticleFX(QObject) :
	__PROTO__ = sdk.StopParticleFX
	def __init__(self,clear_particles :bool = bool() ) -> StopParticleFX :
		self._clear_particles = clear_particles
		pass
	def getclear_particles(self) -> bool :
		return self._clear_particles

	def setclear_particles(self,value : bool) :
		if self._clear_particles != value:
			self._clear_particles = value
			self.clear_particlesChanged.emit(value)

	clear_particles = pyqtProperty(bool, fget=getclear_particles, fset=setclear_particles, notify=clear_particlesChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.clear_particles.extend(self._clear_particles)

# ------- StopRecord ------- #
class StopRecord(QObject) :
	__PROTO__ = sdk.StopRecord
	def __init__(self) -> StopRecord :
		pass
# ------- StopSound ------- #
class StopSound(QObject) :
	__PROTO__ = sdk.StopSound
	def __init__(self,play_id :int = int() ) -> StopSound :
		self._play_id = play_id
		pass
	def getplay_id(self) -> int :
		return self._play_id

	def setplay_id(self,value : int) :
		if self._play_id != value:
			self._play_id = value
			self.play_idChanged.emit(value)

	play_id = pyqtProperty(int, fget=getplay_id, fset=setplay_id, notify=play_idChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.play_id.extend(self._play_id)

# ------- StreamDesc ------- #
class StreamDesc(QObject) :
	__PROTO__ = sdk.StreamDesc
	def __init__(self,name :str = str() ,value_type :int = int() ,value_count :int = int() ,ui :List[int] = [] ,i :List[int] = [] ,ui64 :List[int] = [] ,i64 :List[int] = [] ,f :List[float] = [] ,name_hash :int = int() ) -> StreamDesc :
		self._name = name
		self._value_type = value_type
		self._value_count = value_count
		self._ui = ui
		self._i = i
		self._ui64 = ui64
		self._i64 = i64
		self._f = f
		self._name_hash = name_hash
		pass
	def getname(self) -> str :
		return self._name

	def setname(self,value : str) :
		if self._name != value:
			self._name = value
			self.nameChanged.emit(value)

	name = pyqtProperty(str, fget=getname, fset=setname, notify=nameChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.name.extend(self._name)
		instance.value_type.extend(self._value_type)
		instance.value_count.extend(self._value_count)
		instance.ui = self._ui
		instance.i = self._i
		instance.ui64 = self._ui64
		instance.i64 = self._i64
		instance.f = self._f
		instance.name_hash.extend(self._name_hash)

	def getvalue_type(self) -> int :
		return self._value_type

	def setvalue_type(self,value : int) :
		if self._value_type != value:
			self._value_type = value
			self.value_typeChanged.emit(value)

	value_type = pyqtProperty(int, fget=getvalue_type, fset=setvalue_type, notify=value_typeChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.name.extend(self._name)
		instance.value_type.extend(self._value_type)
		instance.value_count.extend(self._value_count)
		instance.ui = self._ui
		instance.i = self._i
		instance.ui64 = self._ui64
		instance.i64 = self._i64
		instance.f = self._f
		instance.name_hash.extend(self._name_hash)

	def getvalue_count(self) -> int :
		return self._value_count

	def setvalue_count(self,value : int) :
		if self._value_count != value:
			self._value_count = value
			self.value_countChanged.emit(value)

	value_count = pyqtProperty(int, fget=getvalue_count, fset=setvalue_count, notify=value_countChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.name.extend(self._name)
		instance.value_type.extend(self._value_type)
		instance.value_count.extend(self._value_count)
		instance.ui = self._ui
		instance.i = self._i
		instance.ui64 = self._ui64
		instance.i64 = self._i64
		instance.f = self._f
		instance.name_hash.extend(self._name_hash)

	def getui(self) -> int :
		return self._ui

	def setui(self,value : List[int]) :
		if self._ui != value:
			self._ui = value
			self.uiChanged.emit(value)

	ui = pyqtProperty(List, fget=getui, fset=setui, notify=uiChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.name.extend(self._name)
		instance.value_type.extend(self._value_type)
		instance.value_count.extend(self._value_count)
		instance.ui = self._ui
		instance.i = self._i
		instance.ui64 = self._ui64
		instance.i64 = self._i64
		instance.f = self._f
		instance.name_hash.extend(self._name_hash)

	def geti(self) -> int :
		return self._i

	def seti(self,value : List[int]) :
		if self._i != value:
			self._i = value
			self.iChanged.emit(value)

	i = pyqtProperty(List, fget=geti, fset=seti, notify=iChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.name.extend(self._name)
		instance.value_type.extend(self._value_type)
		instance.value_count.extend(self._value_count)
		instance.ui = self._ui
		instance.i = self._i
		instance.ui64 = self._ui64
		instance.i64 = self._i64
		instance.f = self._f
		instance.name_hash.extend(self._name_hash)

	def getui64(self) -> int :
		return self._ui64

	def setui64(self,value : List[int]) :
		if self._ui64 != value:
			self._ui64 = value
			self.ui64Changed.emit(value)

	ui64 = pyqtProperty(List, fget=getui64, fset=setui64, notify=ui64Changed)

	def proto(self) :
		instance = self.__PROTO__()
		instance.name.extend(self._name)
		instance.value_type.extend(self._value_type)
		instance.value_count.extend(self._value_count)
		instance.ui = self._ui
		instance.i = self._i
		instance.ui64 = self._ui64
		instance.i64 = self._i64
		instance.f = self._f
		instance.name_hash.extend(self._name_hash)

	def geti64(self) -> int :
		return self._i64

	def seti64(self,value : List[int]) :
		if self._i64 != value:
			self._i64 = value
			self.i64Changed.emit(value)

	i64 = pyqtProperty(List, fget=geti64, fset=seti64, notify=i64Changed)

	def proto(self) :
		instance = self.__PROTO__()
		instance.name.extend(self._name)
		instance.value_type.extend(self._value_type)
		instance.value_count.extend(self._value_count)
		instance.ui = self._ui
		instance.i = self._i
		instance.ui64 = self._ui64
		instance.i64 = self._i64
		instance.f = self._f
		instance.name_hash.extend(self._name_hash)

	def getf(self) -> float :
		return self._f

	def setf(self,value : List[float]) :
		if self._f != value:
			self._f = value
			self.fChanged.emit(value)

	f = pyqtProperty(List, fget=getf, fset=setf, notify=fChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.name.extend(self._name)
		instance.value_type.extend(self._value_type)
		instance.value_count.extend(self._value_count)
		instance.ui = self._ui
		instance.i = self._i
		instance.ui64 = self._ui64
		instance.i64 = self._i64
		instance.f = self._f
		instance.name_hash.extend(self._name_hash)

	def getname_hash(self) -> int :
		return self._name_hash

	def setname_hash(self,value : int) :
		if self._name_hash != value:
			self._name_hash = value
			self.name_hashChanged.emit(value)

	name_hash = pyqtProperty(int, fget=getname_hash, fset=setname_hash, notify=name_hashChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.name.extend(self._name)
		instance.value_type.extend(self._value_type)
		instance.value_count.extend(self._value_count)
		instance.ui = self._ui
		instance.i = self._i
		instance.ui64 = self._ui64
		instance.i64 = self._i64
		instance.f = self._f
		instance.name_hash.extend(self._name_hash)

# ------- Texture ------- #
class Texture(QObject) :
	__PROTO__ = sdk.Texture
	def __init__(self,sampler :str = str() ,texture :str = str() ) -> Texture :
		self._sampler = sampler
		self._texture = texture
		pass
	def getsampler(self) -> str :
		return self._sampler

	def setsampler(self,value : str) :
		if self._sampler != value:
			self._sampler = value
			self.samplerChanged.emit(value)

	sampler = pyqtProperty(str, fget=getsampler, fset=setsampler, notify=samplerChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.sampler.extend(self._sampler)
		instance.texture.extend(self._texture)

	def gettexture(self) -> str :
		return self._texture

	def settexture(self,value : str) :
		if self._texture != value:
			self._texture = value
			self.textureChanged.emit(value)

	texture = pyqtProperty(str, fget=gettexture, fset=settexture, notify=textureChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.sampler.extend(self._sampler)
		instance.texture.extend(self._texture)

# ------- TextureFormatAlternative ------- #
class CompressionLevel(Enum):
	FAST = 0
	NORMAL = 1
	HIGH = 2
	BEST = 3
class TextureFormatAlternative(QObject) :
	__PROTO__ = sdk.TextureFormatAlternative
	def __init__(self,format :int = int() ,compression_level :int = int() ,compression_type :int = int() ,compressor :str = str() ,compressor_preset :str = str() ) -> TextureFormatAlternative :
		self._format = format
		self._compression_level = compression_level
		self._compression_type = compression_type
		self._compressor = compressor
		self._compressor_preset = compressor_preset
		pass
	def getformat(self) -> int :
		return self._format

	def setformat(self,value : int) :
		if self._format != value:
			self._format = value
			self.formatChanged.emit(value)

	format = pyqtProperty(int, fget=getformat, fset=setformat, notify=formatChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.format.extend(self._format)
		instance.compression_level.extend(self._compression_level)
		instance.compression_type.extend(self._compression_type)
		instance.compressor.extend(self._compressor)
		instance.compressor_preset.extend(self._compressor_preset)

	def getcompression_level(self) -> int :
		return self._compression_level

	def setcompression_level(self,value : int) :
		if self._compression_level != value:
			self._compression_level = value
			self.compression_levelChanged.emit(value)

	compression_level = pyqtProperty(int, fget=getcompression_level, fset=setcompression_level, notify=compression_levelChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.format.extend(self._format)
		instance.compression_level.extend(self._compression_level)
		instance.compression_type.extend(self._compression_type)
		instance.compressor.extend(self._compressor)
		instance.compressor_preset.extend(self._compressor_preset)

	def getcompression_type(self) -> int :
		return self._compression_type

	def setcompression_type(self,value : int) :
		if self._compression_type != value:
			self._compression_type = value
			self.compression_typeChanged.emit(value)

	compression_type = pyqtProperty(int, fget=getcompression_type, fset=setcompression_type, notify=compression_typeChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.format.extend(self._format)
		instance.compression_level.extend(self._compression_level)
		instance.compression_type.extend(self._compression_type)
		instance.compressor.extend(self._compressor)
		instance.compressor_preset.extend(self._compressor_preset)

	def getcompressor(self) -> str :
		return self._compressor

	def setcompressor(self,value : str) :
		if self._compressor != value:
			self._compressor = value
			self.compressorChanged.emit(value)

	compressor = pyqtProperty(str, fget=getcompressor, fset=setcompressor, notify=compressorChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.format.extend(self._format)
		instance.compression_level.extend(self._compression_level)
		instance.compression_type.extend(self._compression_type)
		instance.compressor.extend(self._compressor)
		instance.compressor_preset.extend(self._compressor_preset)

	def getcompressor_preset(self) -> str :
		return self._compressor_preset

	def setcompressor_preset(self,value : str) :
		if self._compressor_preset != value:
			self._compressor_preset = value
			self.compressor_presetChanged.emit(value)

	compressor_preset = pyqtProperty(str, fget=getcompressor_preset, fset=setcompressor_preset, notify=compressor_presetChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.format.extend(self._format)
		instance.compression_level.extend(self._compression_level)
		instance.compression_type.extend(self._compression_type)
		instance.compressor.extend(self._compressor)
		instance.compressor_preset.extend(self._compressor_preset)

# ------- TextureImage ------- #
class Type(Enum):
	TYPE_2D = 1
	TYPE_CUBEMAP = 2
	TYPE_2D_ARRAY = 3
	TYPE_2D_IMAGE = 4
	TYPE_3D = 5
	TYPE_3D_IMAGE = 6
class CompressionType(Enum):
	COMPRESSION_TYPE_DEFAULT = 0
	COMPRESSION_TYPE_WEBP = 1
	COMPRESSION_TYPE_WEBP_LOSSY = 2
	COMPRESSION_TYPE_BASIS_UASTC = 3
	COMPRESSION_TYPE_BASIS_ETC1S = 4
	COMPRESSION_TYPE_ASTC = 5
class CompressionFlags(Enum):
	COMPRESSION_FLAG_ALPHA_CLEAN = 1
class TextureFormat(Enum):
	TEXTURE_FORMAT_LUMINANCE = 0
	TEXTURE_FORMAT_RGB = 1
	TEXTURE_FORMAT_RGBA = 2
	TEXTURE_FORMAT_RGB_PVRTC_2BPPV1 = 3
	TEXTURE_FORMAT_RGB_PVRTC_4BPPV1 = 4
	TEXTURE_FORMAT_RGBA_PVRTC_2BPPV1 = 5
	TEXTURE_FORMAT_RGBA_PVRTC_4BPPV1 = 6
	TEXTURE_FORMAT_RGB_ETC1 = 7
	TEXTURE_FORMAT_RGB_16BPP = 8
	TEXTURE_FORMAT_RGBA_16BPP = 9
	TEXTURE_FORMAT_LUMINANCE_ALPHA = 10
	TEXTURE_FORMAT_RGBA_ETC2 = 11
	TEXTURE_FORMAT_RGBA_ASTC_4X4 = 12
	TEXTURE_FORMAT_RGBA_ASTC_4x4 = 12
	TEXTURE_FORMAT_RGB_BC1 = 13
	TEXTURE_FORMAT_RGBA_BC3 = 14
	TEXTURE_FORMAT_R_BC4 = 15
	TEXTURE_FORMAT_RG_BC5 = 16
	TEXTURE_FORMAT_RGBA_BC7 = 17
	TEXTURE_FORMAT_RGB16F = 18
	TEXTURE_FORMAT_RGB32F = 19
	TEXTURE_FORMAT_RGBA16F = 20
	TEXTURE_FORMAT_RGBA32F = 21
	TEXTURE_FORMAT_R16F = 22
	TEXTURE_FORMAT_RG16F = 23
	TEXTURE_FORMAT_R32F = 24
	TEXTURE_FORMAT_RG32F = 25
	TEXTURE_FORMAT_RGBA_ASTC_5X4 = 26
	TEXTURE_FORMAT_RGBA_ASTC_5X5 = 27
	TEXTURE_FORMAT_RGBA_ASTC_6X5 = 28
	TEXTURE_FORMAT_RGBA_ASTC_6X6 = 29
	TEXTURE_FORMAT_RGBA_ASTC_8X5 = 30
	TEXTURE_FORMAT_RGBA_ASTC_8X6 = 31
	TEXTURE_FORMAT_RGBA_ASTC_8X8 = 32
	TEXTURE_FORMAT_RGBA_ASTC_10X5 = 33
	TEXTURE_FORMAT_RGBA_ASTC_10X6 = 34
	TEXTURE_FORMAT_RGBA_ASTC_10X8 = 35
	TEXTURE_FORMAT_RGBA_ASTC_10X10 = 36
	TEXTURE_FORMAT_RGBA_ASTC_12X10 = 37
	TEXTURE_FORMAT_RGBA_ASTC_12X12 = 38
class TextureImage(QObject) :
	__PROTO__ = sdk.TextureImage
	def __init__(self,alternatives :List[Image] = [],type :int = int() ,count :int = int() ,usage_flags :int = int() ,image_data_address :int = int() ) -> TextureImage :
		self._alternatives = alternatives
		self._type = type
		self._count = count
		self._usage_flags = usage_flags
		self._image_data_address = image_data_address
		pass
	def getalternatives(self) -> Image :
		return self._alternatives

	def setalternatives(self,value : List[Image]) :
		if self._alternatives != value:
			self._alternatives = value
			self.alternativesChanged.emit(value)

	alternatives = pyqtProperty(List, fget=getalternatives, fset=setalternatives, notify=alternativesChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.alternatives.extend([i.proto() for i in self._alternatives])
		instance.type.extend(self._type)
		instance.count.extend(self._count)
		instance.usage_flags.extend(self._usage_flags)
		instance.image_data_address.extend(self._image_data_address)

	def gettype(self) -> int :
		return self._type

	def settype(self,value : int) :
		if self._type != value:
			self._type = value
			self.typeChanged.emit(value)

	type = pyqtProperty(int, fget=gettype, fset=settype, notify=typeChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.alternatives.extend([i.proto() for i in self._alternatives])
		instance.type.extend(self._type)
		instance.count.extend(self._count)
		instance.usage_flags.extend(self._usage_flags)
		instance.image_data_address.extend(self._image_data_address)

	def getcount(self) -> int :
		return self._count

	def setcount(self,value : int) :
		if self._count != value:
			self._count = value
			self.countChanged.emit(value)

	count = pyqtProperty(int, fget=getcount, fset=setcount, notify=countChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.alternatives.extend([i.proto() for i in self._alternatives])
		instance.type.extend(self._type)
		instance.count.extend(self._count)
		instance.usage_flags.extend(self._usage_flags)
		instance.image_data_address.extend(self._image_data_address)

	def getusage_flags(self) -> int :
		return self._usage_flags

	def setusage_flags(self,value : int) :
		if self._usage_flags != value:
			self._usage_flags = value
			self.usage_flagsChanged.emit(value)

	usage_flags = pyqtProperty(int, fget=getusage_flags, fset=setusage_flags, notify=usage_flagsChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.alternatives.extend([i.proto() for i in self._alternatives])
		instance.type.extend(self._type)
		instance.count.extend(self._count)
		instance.usage_flags.extend(self._usage_flags)
		instance.image_data_address.extend(self._image_data_address)

	def getimage_data_address(self) -> int :
		return self._image_data_address

	def setimage_data_address(self,value : int) :
		if self._image_data_address != value:
			self._image_data_address = value
			self.image_data_addressChanged.emit(value)

	image_data_address = pyqtProperty(int, fget=getimage_data_address, fset=setimage_data_address, notify=image_data_addressChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.alternatives.extend([i.proto() for i in self._alternatives])
		instance.type.extend(self._type)
		instance.count.extend(self._count)
		instance.usage_flags.extend(self._usage_flags)
		instance.image_data_address.extend(self._image_data_address)

# ------- TextureProfile ------- #
class TextureProfile(QObject) :
	__PROTO__ = sdk.TextureProfile
	def __init__(self,name :str = str() ,platforms :List[PlatformProfile] = []) -> TextureProfile :
		self._name = name
		self._platforms = platforms
		pass
	def getname(self) -> str :
		return self._name

	def setname(self,value : str) :
		if self._name != value:
			self._name = value
			self.nameChanged.emit(value)

	name = pyqtProperty(str, fget=getname, fset=setname, notify=nameChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.name.extend(self._name)
		instance.platforms.extend([i.proto() for i in self._platforms])

	def getplatforms(self) -> PlatformProfile :
		return self._platforms

	def setplatforms(self,value : List[PlatformProfile]) :
		if self._platforms != value:
			self._platforms = value
			self.platformsChanged.emit(value)

	platforms = pyqtProperty(List, fget=getplatforms, fset=setplatforms, notify=platformsChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.name.extend(self._name)
		instance.platforms.extend([i.proto() for i in self._platforms])

# ------- TextureProfiles ------- #
class TextureProfiles(QObject) :
	__PROTO__ = sdk.TextureProfiles
	def __init__(self,path_settings :List[PathSettings] = [],profiles :List[TextureProfile] = []) -> TextureProfiles :
		self._path_settings = path_settings
		self._profiles = profiles
		pass
	def getpath_settings(self) -> PathSettings :
		return self._path_settings

	def setpath_settings(self,value : List[PathSettings]) :
		if self._path_settings != value:
			self._path_settings = value
			self.path_settingsChanged.emit(value)

	path_settings = pyqtProperty(List, fget=getpath_settings, fset=setpath_settings, notify=path_settingsChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.path_settings.extend([i.proto() for i in self._path_settings])
		instance.profiles.extend([i.proto() for i in self._profiles])

	def getprofiles(self) -> TextureProfile :
		return self._profiles

	def setprofiles(self,value : List[TextureProfile]) :
		if self._profiles != value:
			self._profiles = value
			self.profilesChanged.emit(value)

	profiles = pyqtProperty(List, fget=getprofiles, fset=setprofiles, notify=profilesChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.path_settings.extend([i.proto() for i in self._path_settings])
		instance.profiles.extend([i.proto() for i in self._profiles])

# ------- TextureSet ------- #
class TextureSet(QObject) :
	__PROTO__ = sdk.TextureSet
	def __init__(self,texture :str = str() ,width :int = int() ,height :int = int() ,texture_hash :int = int() ,animations :List[TextureSetAnimation] = [],tile_width :int = int() ,tile_height :int = int() ,tile_count :int = int() ,collision_hull_points :List[float] = [] ,collision_groups :List[str] = [] ,convex_hulls :List[ConvexHull] = [],image_name_hashes :List[int] = [] ,frame_indices :List[int] = [] ,tex_coords :bytes = bytes() ,tex_dims :bytes = bytes() ,geometries :List[SpriteGeometry] = [],use_geometries :int = int() ,page_indices :List[int] = [] ,page_count :int = int() ) -> TextureSet :
		self._texture = texture
		self._width = width
		self._height = height
		self._texture_hash = texture_hash
		self._animations = animations
		self._tile_width = tile_width
		self._tile_height = tile_height
		self._tile_count = tile_count
		self._collision_hull_points = collision_hull_points
		self._collision_groups = collision_groups
		self._convex_hulls = convex_hulls
		self._image_name_hashes = image_name_hashes
		self._frame_indices = frame_indices
		self._tex_coords = tex_coords
		self._tex_dims = tex_dims
		self._geometries = geometries
		self._use_geometries = use_geometries
		self._page_indices = page_indices
		self._page_count = page_count
		pass
	def gettexture(self) -> str :
		return self._texture

	def settexture(self,value : str) :
		if self._texture != value:
			self._texture = value
			self.textureChanged.emit(value)

	texture = pyqtProperty(str, fget=gettexture, fset=settexture, notify=textureChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.texture.extend(self._texture)
		instance.width.extend(self._width)
		instance.height.extend(self._height)
		instance.texture_hash.extend(self._texture_hash)
		instance.animations.extend([i.proto() for i in self._animations])
		instance.tile_width.extend(self._tile_width)
		instance.tile_height.extend(self._tile_height)
		instance.tile_count.extend(self._tile_count)
		instance.collision_hull_points = self._collision_hull_points
		instance.collision_groups = self._collision_groups
		instance.convex_hulls.extend([i.proto() for i in self._convex_hulls])
		instance.image_name_hashes = self._image_name_hashes
		instance.frame_indices = self._frame_indices
		instance.tex_coords.extend(self._tex_coords)
		instance.tex_dims.extend(self._tex_dims)
		instance.geometries.extend([i.proto() for i in self._geometries])
		instance.use_geometries.extend(self._use_geometries)
		instance.page_indices = self._page_indices
		instance.page_count.extend(self._page_count)

	def getwidth(self) -> int :
		return self._width

	def setwidth(self,value : int) :
		if self._width != value:
			self._width = value
			self.widthChanged.emit(value)

	width = pyqtProperty(int, fget=getwidth, fset=setwidth, notify=widthChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.texture.extend(self._texture)
		instance.width.extend(self._width)
		instance.height.extend(self._height)
		instance.texture_hash.extend(self._texture_hash)
		instance.animations.extend([i.proto() for i in self._animations])
		instance.tile_width.extend(self._tile_width)
		instance.tile_height.extend(self._tile_height)
		instance.tile_count.extend(self._tile_count)
		instance.collision_hull_points = self._collision_hull_points
		instance.collision_groups = self._collision_groups
		instance.convex_hulls.extend([i.proto() for i in self._convex_hulls])
		instance.image_name_hashes = self._image_name_hashes
		instance.frame_indices = self._frame_indices
		instance.tex_coords.extend(self._tex_coords)
		instance.tex_dims.extend(self._tex_dims)
		instance.geometries.extend([i.proto() for i in self._geometries])
		instance.use_geometries.extend(self._use_geometries)
		instance.page_indices = self._page_indices
		instance.page_count.extend(self._page_count)

	def getheight(self) -> int :
		return self._height

	def setheight(self,value : int) :
		if self._height != value:
			self._height = value
			self.heightChanged.emit(value)

	height = pyqtProperty(int, fget=getheight, fset=setheight, notify=heightChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.texture.extend(self._texture)
		instance.width.extend(self._width)
		instance.height.extend(self._height)
		instance.texture_hash.extend(self._texture_hash)
		instance.animations.extend([i.proto() for i in self._animations])
		instance.tile_width.extend(self._tile_width)
		instance.tile_height.extend(self._tile_height)
		instance.tile_count.extend(self._tile_count)
		instance.collision_hull_points = self._collision_hull_points
		instance.collision_groups = self._collision_groups
		instance.convex_hulls.extend([i.proto() for i in self._convex_hulls])
		instance.image_name_hashes = self._image_name_hashes
		instance.frame_indices = self._frame_indices
		instance.tex_coords.extend(self._tex_coords)
		instance.tex_dims.extend(self._tex_dims)
		instance.geometries.extend([i.proto() for i in self._geometries])
		instance.use_geometries.extend(self._use_geometries)
		instance.page_indices = self._page_indices
		instance.page_count.extend(self._page_count)

	def gettexture_hash(self) -> int :
		return self._texture_hash

	def settexture_hash(self,value : int) :
		if self._texture_hash != value:
			self._texture_hash = value
			self.texture_hashChanged.emit(value)

	texture_hash = pyqtProperty(int, fget=gettexture_hash, fset=settexture_hash, notify=texture_hashChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.texture.extend(self._texture)
		instance.width.extend(self._width)
		instance.height.extend(self._height)
		instance.texture_hash.extend(self._texture_hash)
		instance.animations.extend([i.proto() for i in self._animations])
		instance.tile_width.extend(self._tile_width)
		instance.tile_height.extend(self._tile_height)
		instance.tile_count.extend(self._tile_count)
		instance.collision_hull_points = self._collision_hull_points
		instance.collision_groups = self._collision_groups
		instance.convex_hulls.extend([i.proto() for i in self._convex_hulls])
		instance.image_name_hashes = self._image_name_hashes
		instance.frame_indices = self._frame_indices
		instance.tex_coords.extend(self._tex_coords)
		instance.tex_dims.extend(self._tex_dims)
		instance.geometries.extend([i.proto() for i in self._geometries])
		instance.use_geometries.extend(self._use_geometries)
		instance.page_indices = self._page_indices
		instance.page_count.extend(self._page_count)

	def getanimations(self) -> TextureSetAnimation :
		return self._animations

	def setanimations(self,value : List[TextureSetAnimation]) :
		if self._animations != value:
			self._animations = value
			self.animationsChanged.emit(value)

	animations = pyqtProperty(List, fget=getanimations, fset=setanimations, notify=animationsChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.texture.extend(self._texture)
		instance.width.extend(self._width)
		instance.height.extend(self._height)
		instance.texture_hash.extend(self._texture_hash)
		instance.animations.extend([i.proto() for i in self._animations])
		instance.tile_width.extend(self._tile_width)
		instance.tile_height.extend(self._tile_height)
		instance.tile_count.extend(self._tile_count)
		instance.collision_hull_points = self._collision_hull_points
		instance.collision_groups = self._collision_groups
		instance.convex_hulls.extend([i.proto() for i in self._convex_hulls])
		instance.image_name_hashes = self._image_name_hashes
		instance.frame_indices = self._frame_indices
		instance.tex_coords.extend(self._tex_coords)
		instance.tex_dims.extend(self._tex_dims)
		instance.geometries.extend([i.proto() for i in self._geometries])
		instance.use_geometries.extend(self._use_geometries)
		instance.page_indices = self._page_indices
		instance.page_count.extend(self._page_count)

	def gettile_width(self) -> int :
		return self._tile_width

	def settile_width(self,value : int) :
		if self._tile_width != value:
			self._tile_width = value
			self.tile_widthChanged.emit(value)

	tile_width = pyqtProperty(int, fget=gettile_width, fset=settile_width, notify=tile_widthChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.texture.extend(self._texture)
		instance.width.extend(self._width)
		instance.height.extend(self._height)
		instance.texture_hash.extend(self._texture_hash)
		instance.animations.extend([i.proto() for i in self._animations])
		instance.tile_width.extend(self._tile_width)
		instance.tile_height.extend(self._tile_height)
		instance.tile_count.extend(self._tile_count)
		instance.collision_hull_points = self._collision_hull_points
		instance.collision_groups = self._collision_groups
		instance.convex_hulls.extend([i.proto() for i in self._convex_hulls])
		instance.image_name_hashes = self._image_name_hashes
		instance.frame_indices = self._frame_indices
		instance.tex_coords.extend(self._tex_coords)
		instance.tex_dims.extend(self._tex_dims)
		instance.geometries.extend([i.proto() for i in self._geometries])
		instance.use_geometries.extend(self._use_geometries)
		instance.page_indices = self._page_indices
		instance.page_count.extend(self._page_count)

	def gettile_height(self) -> int :
		return self._tile_height

	def settile_height(self,value : int) :
		if self._tile_height != value:
			self._tile_height = value
			self.tile_heightChanged.emit(value)

	tile_height = pyqtProperty(int, fget=gettile_height, fset=settile_height, notify=tile_heightChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.texture.extend(self._texture)
		instance.width.extend(self._width)
		instance.height.extend(self._height)
		instance.texture_hash.extend(self._texture_hash)
		instance.animations.extend([i.proto() for i in self._animations])
		instance.tile_width.extend(self._tile_width)
		instance.tile_height.extend(self._tile_height)
		instance.tile_count.extend(self._tile_count)
		instance.collision_hull_points = self._collision_hull_points
		instance.collision_groups = self._collision_groups
		instance.convex_hulls.extend([i.proto() for i in self._convex_hulls])
		instance.image_name_hashes = self._image_name_hashes
		instance.frame_indices = self._frame_indices
		instance.tex_coords.extend(self._tex_coords)
		instance.tex_dims.extend(self._tex_dims)
		instance.geometries.extend([i.proto() for i in self._geometries])
		instance.use_geometries.extend(self._use_geometries)
		instance.page_indices = self._page_indices
		instance.page_count.extend(self._page_count)

	def gettile_count(self) -> int :
		return self._tile_count

	def settile_count(self,value : int) :
		if self._tile_count != value:
			self._tile_count = value
			self.tile_countChanged.emit(value)

	tile_count = pyqtProperty(int, fget=gettile_count, fset=settile_count, notify=tile_countChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.texture.extend(self._texture)
		instance.width.extend(self._width)
		instance.height.extend(self._height)
		instance.texture_hash.extend(self._texture_hash)
		instance.animations.extend([i.proto() for i in self._animations])
		instance.tile_width.extend(self._tile_width)
		instance.tile_height.extend(self._tile_height)
		instance.tile_count.extend(self._tile_count)
		instance.collision_hull_points = self._collision_hull_points
		instance.collision_groups = self._collision_groups
		instance.convex_hulls.extend([i.proto() for i in self._convex_hulls])
		instance.image_name_hashes = self._image_name_hashes
		instance.frame_indices = self._frame_indices
		instance.tex_coords.extend(self._tex_coords)
		instance.tex_dims.extend(self._tex_dims)
		instance.geometries.extend([i.proto() for i in self._geometries])
		instance.use_geometries.extend(self._use_geometries)
		instance.page_indices = self._page_indices
		instance.page_count.extend(self._page_count)

	def getcollision_hull_points(self) -> float :
		return self._collision_hull_points

	def setcollision_hull_points(self,value : List[float]) :
		if self._collision_hull_points != value:
			self._collision_hull_points = value
			self.collision_hull_pointsChanged.emit(value)

	collision_hull_points = pyqtProperty(List, fget=getcollision_hull_points, fset=setcollision_hull_points, notify=collision_hull_pointsChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.texture.extend(self._texture)
		instance.width.extend(self._width)
		instance.height.extend(self._height)
		instance.texture_hash.extend(self._texture_hash)
		instance.animations.extend([i.proto() for i in self._animations])
		instance.tile_width.extend(self._tile_width)
		instance.tile_height.extend(self._tile_height)
		instance.tile_count.extend(self._tile_count)
		instance.collision_hull_points = self._collision_hull_points
		instance.collision_groups = self._collision_groups
		instance.convex_hulls.extend([i.proto() for i in self._convex_hulls])
		instance.image_name_hashes = self._image_name_hashes
		instance.frame_indices = self._frame_indices
		instance.tex_coords.extend(self._tex_coords)
		instance.tex_dims.extend(self._tex_dims)
		instance.geometries.extend([i.proto() for i in self._geometries])
		instance.use_geometries.extend(self._use_geometries)
		instance.page_indices = self._page_indices
		instance.page_count.extend(self._page_count)

	def getcollision_groups(self) -> str :
		return self._collision_groups

	def setcollision_groups(self,value : List[str]) :
		if self._collision_groups != value:
			self._collision_groups = value
			self.collision_groupsChanged.emit(value)

	collision_groups = pyqtProperty(List, fget=getcollision_groups, fset=setcollision_groups, notify=collision_groupsChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.texture.extend(self._texture)
		instance.width.extend(self._width)
		instance.height.extend(self._height)
		instance.texture_hash.extend(self._texture_hash)
		instance.animations.extend([i.proto() for i in self._animations])
		instance.tile_width.extend(self._tile_width)
		instance.tile_height.extend(self._tile_height)
		instance.tile_count.extend(self._tile_count)
		instance.collision_hull_points = self._collision_hull_points
		instance.collision_groups = self._collision_groups
		instance.convex_hulls.extend([i.proto() for i in self._convex_hulls])
		instance.image_name_hashes = self._image_name_hashes
		instance.frame_indices = self._frame_indices
		instance.tex_coords.extend(self._tex_coords)
		instance.tex_dims.extend(self._tex_dims)
		instance.geometries.extend([i.proto() for i in self._geometries])
		instance.use_geometries.extend(self._use_geometries)
		instance.page_indices = self._page_indices
		instance.page_count.extend(self._page_count)

	def getconvex_hulls(self) -> ConvexHull :
		return self._convex_hulls

	def setconvex_hulls(self,value : List[ConvexHull]) :
		if self._convex_hulls != value:
			self._convex_hulls = value
			self.convex_hullsChanged.emit(value)

	convex_hulls = pyqtProperty(List, fget=getconvex_hulls, fset=setconvex_hulls, notify=convex_hullsChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.texture.extend(self._texture)
		instance.width.extend(self._width)
		instance.height.extend(self._height)
		instance.texture_hash.extend(self._texture_hash)
		instance.animations.extend([i.proto() for i in self._animations])
		instance.tile_width.extend(self._tile_width)
		instance.tile_height.extend(self._tile_height)
		instance.tile_count.extend(self._tile_count)
		instance.collision_hull_points = self._collision_hull_points
		instance.collision_groups = self._collision_groups
		instance.convex_hulls.extend([i.proto() for i in self._convex_hulls])
		instance.image_name_hashes = self._image_name_hashes
		instance.frame_indices = self._frame_indices
		instance.tex_coords.extend(self._tex_coords)
		instance.tex_dims.extend(self._tex_dims)
		instance.geometries.extend([i.proto() for i in self._geometries])
		instance.use_geometries.extend(self._use_geometries)
		instance.page_indices = self._page_indices
		instance.page_count.extend(self._page_count)

	def getimage_name_hashes(self) -> int :
		return self._image_name_hashes

	def setimage_name_hashes(self,value : List[int]) :
		if self._image_name_hashes != value:
			self._image_name_hashes = value
			self.image_name_hashesChanged.emit(value)

	image_name_hashes = pyqtProperty(List, fget=getimage_name_hashes, fset=setimage_name_hashes, notify=image_name_hashesChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.texture.extend(self._texture)
		instance.width.extend(self._width)
		instance.height.extend(self._height)
		instance.texture_hash.extend(self._texture_hash)
		instance.animations.extend([i.proto() for i in self._animations])
		instance.tile_width.extend(self._tile_width)
		instance.tile_height.extend(self._tile_height)
		instance.tile_count.extend(self._tile_count)
		instance.collision_hull_points = self._collision_hull_points
		instance.collision_groups = self._collision_groups
		instance.convex_hulls.extend([i.proto() for i in self._convex_hulls])
		instance.image_name_hashes = self._image_name_hashes
		instance.frame_indices = self._frame_indices
		instance.tex_coords.extend(self._tex_coords)
		instance.tex_dims.extend(self._tex_dims)
		instance.geometries.extend([i.proto() for i in self._geometries])
		instance.use_geometries.extend(self._use_geometries)
		instance.page_indices = self._page_indices
		instance.page_count.extend(self._page_count)

	def getframe_indices(self) -> int :
		return self._frame_indices

	def setframe_indices(self,value : List[int]) :
		if self._frame_indices != value:
			self._frame_indices = value
			self.frame_indicesChanged.emit(value)

	frame_indices = pyqtProperty(List, fget=getframe_indices, fset=setframe_indices, notify=frame_indicesChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.texture.extend(self._texture)
		instance.width.extend(self._width)
		instance.height.extend(self._height)
		instance.texture_hash.extend(self._texture_hash)
		instance.animations.extend([i.proto() for i in self._animations])
		instance.tile_width.extend(self._tile_width)
		instance.tile_height.extend(self._tile_height)
		instance.tile_count.extend(self._tile_count)
		instance.collision_hull_points = self._collision_hull_points
		instance.collision_groups = self._collision_groups
		instance.convex_hulls.extend([i.proto() for i in self._convex_hulls])
		instance.image_name_hashes = self._image_name_hashes
		instance.frame_indices = self._frame_indices
		instance.tex_coords.extend(self._tex_coords)
		instance.tex_dims.extend(self._tex_dims)
		instance.geometries.extend([i.proto() for i in self._geometries])
		instance.use_geometries.extend(self._use_geometries)
		instance.page_indices = self._page_indices
		instance.page_count.extend(self._page_count)

	def gettex_coords(self) -> bytes :
		return self._tex_coords

	def settex_coords(self,value : bytes) :
		if self._tex_coords != value:
			self._tex_coords = value
			self.tex_coordsChanged.emit(value)

	tex_coords = pyqtProperty(bytes, fget=gettex_coords, fset=settex_coords, notify=tex_coordsChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.texture.extend(self._texture)
		instance.width.extend(self._width)
		instance.height.extend(self._height)
		instance.texture_hash.extend(self._texture_hash)
		instance.animations.extend([i.proto() for i in self._animations])
		instance.tile_width.extend(self._tile_width)
		instance.tile_height.extend(self._tile_height)
		instance.tile_count.extend(self._tile_count)
		instance.collision_hull_points = self._collision_hull_points
		instance.collision_groups = self._collision_groups
		instance.convex_hulls.extend([i.proto() for i in self._convex_hulls])
		instance.image_name_hashes = self._image_name_hashes
		instance.frame_indices = self._frame_indices
		instance.tex_coords.extend(self._tex_coords)
		instance.tex_dims.extend(self._tex_dims)
		instance.geometries.extend([i.proto() for i in self._geometries])
		instance.use_geometries.extend(self._use_geometries)
		instance.page_indices = self._page_indices
		instance.page_count.extend(self._page_count)

	def gettex_dims(self) -> bytes :
		return self._tex_dims

	def settex_dims(self,value : bytes) :
		if self._tex_dims != value:
			self._tex_dims = value
			self.tex_dimsChanged.emit(value)

	tex_dims = pyqtProperty(bytes, fget=gettex_dims, fset=settex_dims, notify=tex_dimsChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.texture.extend(self._texture)
		instance.width.extend(self._width)
		instance.height.extend(self._height)
		instance.texture_hash.extend(self._texture_hash)
		instance.animations.extend([i.proto() for i in self._animations])
		instance.tile_width.extend(self._tile_width)
		instance.tile_height.extend(self._tile_height)
		instance.tile_count.extend(self._tile_count)
		instance.collision_hull_points = self._collision_hull_points
		instance.collision_groups = self._collision_groups
		instance.convex_hulls.extend([i.proto() for i in self._convex_hulls])
		instance.image_name_hashes = self._image_name_hashes
		instance.frame_indices = self._frame_indices
		instance.tex_coords.extend(self._tex_coords)
		instance.tex_dims.extend(self._tex_dims)
		instance.geometries.extend([i.proto() for i in self._geometries])
		instance.use_geometries.extend(self._use_geometries)
		instance.page_indices = self._page_indices
		instance.page_count.extend(self._page_count)

	def getgeometries(self) -> SpriteGeometry :
		return self._geometries

	def setgeometries(self,value : List[SpriteGeometry]) :
		if self._geometries != value:
			self._geometries = value
			self.geometriesChanged.emit(value)

	geometries = pyqtProperty(List, fget=getgeometries, fset=setgeometries, notify=geometriesChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.texture.extend(self._texture)
		instance.width.extend(self._width)
		instance.height.extend(self._height)
		instance.texture_hash.extend(self._texture_hash)
		instance.animations.extend([i.proto() for i in self._animations])
		instance.tile_width.extend(self._tile_width)
		instance.tile_height.extend(self._tile_height)
		instance.tile_count.extend(self._tile_count)
		instance.collision_hull_points = self._collision_hull_points
		instance.collision_groups = self._collision_groups
		instance.convex_hulls.extend([i.proto() for i in self._convex_hulls])
		instance.image_name_hashes = self._image_name_hashes
		instance.frame_indices = self._frame_indices
		instance.tex_coords.extend(self._tex_coords)
		instance.tex_dims.extend(self._tex_dims)
		instance.geometries.extend([i.proto() for i in self._geometries])
		instance.use_geometries.extend(self._use_geometries)
		instance.page_indices = self._page_indices
		instance.page_count.extend(self._page_count)

	def getuse_geometries(self) -> int :
		return self._use_geometries

	def setuse_geometries(self,value : int) :
		if self._use_geometries != value:
			self._use_geometries = value
			self.use_geometriesChanged.emit(value)

	use_geometries = pyqtProperty(int, fget=getuse_geometries, fset=setuse_geometries, notify=use_geometriesChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.texture.extend(self._texture)
		instance.width.extend(self._width)
		instance.height.extend(self._height)
		instance.texture_hash.extend(self._texture_hash)
		instance.animations.extend([i.proto() for i in self._animations])
		instance.tile_width.extend(self._tile_width)
		instance.tile_height.extend(self._tile_height)
		instance.tile_count.extend(self._tile_count)
		instance.collision_hull_points = self._collision_hull_points
		instance.collision_groups = self._collision_groups
		instance.convex_hulls.extend([i.proto() for i in self._convex_hulls])
		instance.image_name_hashes = self._image_name_hashes
		instance.frame_indices = self._frame_indices
		instance.tex_coords.extend(self._tex_coords)
		instance.tex_dims.extend(self._tex_dims)
		instance.geometries.extend([i.proto() for i in self._geometries])
		instance.use_geometries.extend(self._use_geometries)
		instance.page_indices = self._page_indices
		instance.page_count.extend(self._page_count)

	def getpage_indices(self) -> int :
		return self._page_indices

	def setpage_indices(self,value : List[int]) :
		if self._page_indices != value:
			self._page_indices = value
			self.page_indicesChanged.emit(value)

	page_indices = pyqtProperty(List, fget=getpage_indices, fset=setpage_indices, notify=page_indicesChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.texture.extend(self._texture)
		instance.width.extend(self._width)
		instance.height.extend(self._height)
		instance.texture_hash.extend(self._texture_hash)
		instance.animations.extend([i.proto() for i in self._animations])
		instance.tile_width.extend(self._tile_width)
		instance.tile_height.extend(self._tile_height)
		instance.tile_count.extend(self._tile_count)
		instance.collision_hull_points = self._collision_hull_points
		instance.collision_groups = self._collision_groups
		instance.convex_hulls.extend([i.proto() for i in self._convex_hulls])
		instance.image_name_hashes = self._image_name_hashes
		instance.frame_indices = self._frame_indices
		instance.tex_coords.extend(self._tex_coords)
		instance.tex_dims.extend(self._tex_dims)
		instance.geometries.extend([i.proto() for i in self._geometries])
		instance.use_geometries.extend(self._use_geometries)
		instance.page_indices = self._page_indices
		instance.page_count.extend(self._page_count)

	def getpage_count(self) -> int :
		return self._page_count

	def setpage_count(self,value : int) :
		if self._page_count != value:
			self._page_count = value
			self.page_countChanged.emit(value)

	page_count = pyqtProperty(int, fget=getpage_count, fset=setpage_count, notify=page_countChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.texture.extend(self._texture)
		instance.width.extend(self._width)
		instance.height.extend(self._height)
		instance.texture_hash.extend(self._texture_hash)
		instance.animations.extend([i.proto() for i in self._animations])
		instance.tile_width.extend(self._tile_width)
		instance.tile_height.extend(self._tile_height)
		instance.tile_count.extend(self._tile_count)
		instance.collision_hull_points = self._collision_hull_points
		instance.collision_groups = self._collision_groups
		instance.convex_hulls.extend([i.proto() for i in self._convex_hulls])
		instance.image_name_hashes = self._image_name_hashes
		instance.frame_indices = self._frame_indices
		instance.tex_coords.extend(self._tex_coords)
		instance.tex_dims.extend(self._tex_dims)
		instance.geometries.extend([i.proto() for i in self._geometries])
		instance.use_geometries.extend(self._use_geometries)
		instance.page_indices = self._page_indices
		instance.page_count.extend(self._page_count)

# ------- TextureSetAnimation ------- #
class TextureSetAnimation(QObject) :
	__PROTO__ = sdk.TextureSetAnimation
	def __init__(self,id :str = str() ,width :int = int() ,height :int = int() ,start :int = int() ,end :int = int() ,fps :int = int() ,playback :int = int() ,flip_horizontal :int = int() ,flip_vertical :int = int() ) -> TextureSetAnimation :
		self._id = id
		self._width = width
		self._height = height
		self._start = start
		self._end = end
		self._fps = fps
		self._playback = playback
		self._flip_horizontal = flip_horizontal
		self._flip_vertical = flip_vertical
		pass
	def getid(self) -> str :
		return self._id

	def setid(self,value : str) :
		if self._id != value:
			self._id = value
			self.idChanged.emit(value)

	id = pyqtProperty(str, fget=getid, fset=setid, notify=idChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.id.extend(self._id)
		instance.width.extend(self._width)
		instance.height.extend(self._height)
		instance.start.extend(self._start)
		instance.end.extend(self._end)
		instance.fps.extend(self._fps)
		instance.playback.extend(self._playback)
		instance.flip_horizontal.extend(self._flip_horizontal)
		instance.flip_vertical.extend(self._flip_vertical)

	def getwidth(self) -> int :
		return self._width

	def setwidth(self,value : int) :
		if self._width != value:
			self._width = value
			self.widthChanged.emit(value)

	width = pyqtProperty(int, fget=getwidth, fset=setwidth, notify=widthChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.id.extend(self._id)
		instance.width.extend(self._width)
		instance.height.extend(self._height)
		instance.start.extend(self._start)
		instance.end.extend(self._end)
		instance.fps.extend(self._fps)
		instance.playback.extend(self._playback)
		instance.flip_horizontal.extend(self._flip_horizontal)
		instance.flip_vertical.extend(self._flip_vertical)

	def getheight(self) -> int :
		return self._height

	def setheight(self,value : int) :
		if self._height != value:
			self._height = value
			self.heightChanged.emit(value)

	height = pyqtProperty(int, fget=getheight, fset=setheight, notify=heightChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.id.extend(self._id)
		instance.width.extend(self._width)
		instance.height.extend(self._height)
		instance.start.extend(self._start)
		instance.end.extend(self._end)
		instance.fps.extend(self._fps)
		instance.playback.extend(self._playback)
		instance.flip_horizontal.extend(self._flip_horizontal)
		instance.flip_vertical.extend(self._flip_vertical)

	def getstart(self) -> int :
		return self._start

	def setstart(self,value : int) :
		if self._start != value:
			self._start = value
			self.startChanged.emit(value)

	start = pyqtProperty(int, fget=getstart, fset=setstart, notify=startChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.id.extend(self._id)
		instance.width.extend(self._width)
		instance.height.extend(self._height)
		instance.start.extend(self._start)
		instance.end.extend(self._end)
		instance.fps.extend(self._fps)
		instance.playback.extend(self._playback)
		instance.flip_horizontal.extend(self._flip_horizontal)
		instance.flip_vertical.extend(self._flip_vertical)

	def getend(self) -> int :
		return self._end

	def setend(self,value : int) :
		if self._end != value:
			self._end = value
			self.endChanged.emit(value)

	end = pyqtProperty(int, fget=getend, fset=setend, notify=endChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.id.extend(self._id)
		instance.width.extend(self._width)
		instance.height.extend(self._height)
		instance.start.extend(self._start)
		instance.end.extend(self._end)
		instance.fps.extend(self._fps)
		instance.playback.extend(self._playback)
		instance.flip_horizontal.extend(self._flip_horizontal)
		instance.flip_vertical.extend(self._flip_vertical)

	def getfps(self) -> int :
		return self._fps

	def setfps(self,value : int) :
		if self._fps != value:
			self._fps = value
			self.fpsChanged.emit(value)

	fps = pyqtProperty(int, fget=getfps, fset=setfps, notify=fpsChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.id.extend(self._id)
		instance.width.extend(self._width)
		instance.height.extend(self._height)
		instance.start.extend(self._start)
		instance.end.extend(self._end)
		instance.fps.extend(self._fps)
		instance.playback.extend(self._playback)
		instance.flip_horizontal.extend(self._flip_horizontal)
		instance.flip_vertical.extend(self._flip_vertical)

	def getplayback(self) -> int :
		return self._playback

	def setplayback(self,value : int) :
		if self._playback != value:
			self._playback = value
			self.playbackChanged.emit(value)

	playback = pyqtProperty(int, fget=getplayback, fset=setplayback, notify=playbackChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.id.extend(self._id)
		instance.width.extend(self._width)
		instance.height.extend(self._height)
		instance.start.extend(self._start)
		instance.end.extend(self._end)
		instance.fps.extend(self._fps)
		instance.playback.extend(self._playback)
		instance.flip_horizontal.extend(self._flip_horizontal)
		instance.flip_vertical.extend(self._flip_vertical)

	def getflip_horizontal(self) -> int :
		return self._flip_horizontal

	def setflip_horizontal(self,value : int) :
		if self._flip_horizontal != value:
			self._flip_horizontal = value
			self.flip_horizontalChanged.emit(value)

	flip_horizontal = pyqtProperty(int, fget=getflip_horizontal, fset=setflip_horizontal, notify=flip_horizontalChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.id.extend(self._id)
		instance.width.extend(self._width)
		instance.height.extend(self._height)
		instance.start.extend(self._start)
		instance.end.extend(self._end)
		instance.fps.extend(self._fps)
		instance.playback.extend(self._playback)
		instance.flip_horizontal.extend(self._flip_horizontal)
		instance.flip_vertical.extend(self._flip_vertical)

	def getflip_vertical(self) -> int :
		return self._flip_vertical

	def setflip_vertical(self,value : int) :
		if self._flip_vertical != value:
			self._flip_vertical = value
			self.flip_verticalChanged.emit(value)

	flip_vertical = pyqtProperty(int, fget=getflip_vertical, fset=setflip_vertical, notify=flip_verticalChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.id.extend(self._id)
		instance.width.extend(self._width)
		instance.height.extend(self._height)
		instance.start.extend(self._start)
		instance.end.extend(self._end)
		instance.fps.extend(self._fps)
		instance.playback.extend(self._playback)
		instance.flip_horizontal.extend(self._flip_horizontal)
		instance.flip_vertical.extend(self._flip_vertical)

# ------- TileCell ------- #
class TileCell(QObject) :
	__PROTO__ = sdk.TileCell
	def __init__(self,x :int = int() ,y :int = int() ,tile :int = int() ,h_flip :int = int() ,v_flip :int = int() ,rotate90 :int = int() ) -> TileCell :
		self._x = x
		self._y = y
		self._tile = tile
		self._h_flip = h_flip
		self._v_flip = v_flip
		self._rotate90 = rotate90
		pass
	def getx(self) -> int :
		return self._x

	def setx(self,value : int) :
		if self._x != value:
			self._x = value
			self.xChanged.emit(value)

	x = pyqtProperty(int, fget=getx, fset=setx, notify=xChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.x.extend(self._x)
		instance.y.extend(self._y)
		instance.tile.extend(self._tile)
		instance.h_flip.extend(self._h_flip)
		instance.v_flip.extend(self._v_flip)
		instance.rotate90.extend(self._rotate90)

	def gety(self) -> int :
		return self._y

	def sety(self,value : int) :
		if self._y != value:
			self._y = value
			self.yChanged.emit(value)

	y = pyqtProperty(int, fget=gety, fset=sety, notify=yChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.x.extend(self._x)
		instance.y.extend(self._y)
		instance.tile.extend(self._tile)
		instance.h_flip.extend(self._h_flip)
		instance.v_flip.extend(self._v_flip)
		instance.rotate90.extend(self._rotate90)

	def gettile(self) -> int :
		return self._tile

	def settile(self,value : int) :
		if self._tile != value:
			self._tile = value
			self.tileChanged.emit(value)

	tile = pyqtProperty(int, fget=gettile, fset=settile, notify=tileChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.x.extend(self._x)
		instance.y.extend(self._y)
		instance.tile.extend(self._tile)
		instance.h_flip.extend(self._h_flip)
		instance.v_flip.extend(self._v_flip)
		instance.rotate90.extend(self._rotate90)

	def geth_flip(self) -> int :
		return self._h_flip

	def seth_flip(self,value : int) :
		if self._h_flip != value:
			self._h_flip = value
			self.h_flipChanged.emit(value)

	h_flip = pyqtProperty(int, fget=geth_flip, fset=seth_flip, notify=h_flipChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.x.extend(self._x)
		instance.y.extend(self._y)
		instance.tile.extend(self._tile)
		instance.h_flip.extend(self._h_flip)
		instance.v_flip.extend(self._v_flip)
		instance.rotate90.extend(self._rotate90)

	def getv_flip(self) -> int :
		return self._v_flip

	def setv_flip(self,value : int) :
		if self._v_flip != value:
			self._v_flip = value
			self.v_flipChanged.emit(value)

	v_flip = pyqtProperty(int, fget=getv_flip, fset=setv_flip, notify=v_flipChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.x.extend(self._x)
		instance.y.extend(self._y)
		instance.tile.extend(self._tile)
		instance.h_flip.extend(self._h_flip)
		instance.v_flip.extend(self._v_flip)
		instance.rotate90.extend(self._rotate90)

	def getrotate90(self) -> int :
		return self._rotate90

	def setrotate90(self,value : int) :
		if self._rotate90 != value:
			self._rotate90 = value
			self.rotate90Changed.emit(value)

	rotate90 = pyqtProperty(int, fget=getrotate90, fset=setrotate90, notify=rotate90Changed)

	def proto(self) :
		instance = self.__PROTO__()
		instance.x.extend(self._x)
		instance.y.extend(self._y)
		instance.tile.extend(self._tile)
		instance.h_flip.extend(self._h_flip)
		instance.v_flip.extend(self._v_flip)
		instance.rotate90.extend(self._rotate90)

# ------- TileGrid ------- #
class BlendMode(Enum):
	BLEND_MODE_ALPHA = 0
	BLEND_MODE_ADD = 1
	BLEND_MODE_ADD_ALPHA = 2
	BLEND_MODE_MULT = 3
	BLEND_MODE_SCREEN = 4
class TileGrid(QObject) :
	__PROTO__ = sdk.TileGrid
	def __init__(self,tile_set :str = str() ,layers :List[TileLayer] = [],material :str = str() ,blend_mode :int = int() ) -> TileGrid :
		self._tile_set = tile_set
		self._layers = layers
		self._material = material
		self._blend_mode = blend_mode
		pass
	def gettile_set(self) -> str :
		return self._tile_set

	def settile_set(self,value : str) :
		if self._tile_set != value:
			self._tile_set = value
			self.tile_setChanged.emit(value)

	tile_set = pyqtProperty(str, fget=gettile_set, fset=settile_set, notify=tile_setChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.tile_set.extend(self._tile_set)
		instance.layers.extend([i.proto() for i in self._layers])
		instance.material.extend(self._material)
		instance.blend_mode.extend(self._blend_mode)

	def getlayers(self) -> TileLayer :
		return self._layers

	def setlayers(self,value : List[TileLayer]) :
		if self._layers != value:
			self._layers = value
			self.layersChanged.emit(value)

	layers = pyqtProperty(List, fget=getlayers, fset=setlayers, notify=layersChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.tile_set.extend(self._tile_set)
		instance.layers.extend([i.proto() for i in self._layers])
		instance.material.extend(self._material)
		instance.blend_mode.extend(self._blend_mode)

	def getmaterial(self) -> str :
		return self._material

	def setmaterial(self,value : str) :
		if self._material != value:
			self._material = value
			self.materialChanged.emit(value)

	material = pyqtProperty(str, fget=getmaterial, fset=setmaterial, notify=materialChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.tile_set.extend(self._tile_set)
		instance.layers.extend([i.proto() for i in self._layers])
		instance.material.extend(self._material)
		instance.blend_mode.extend(self._blend_mode)

	def getblend_mode(self) -> int :
		return self._blend_mode

	def setblend_mode(self,value : int) :
		if self._blend_mode != value:
			self._blend_mode = value
			self.blend_modeChanged.emit(value)

	blend_mode = pyqtProperty(int, fget=getblend_mode, fset=setblend_mode, notify=blend_modeChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.tile_set.extend(self._tile_set)
		instance.layers.extend([i.proto() for i in self._layers])
		instance.material.extend(self._material)
		instance.blend_mode.extend(self._blend_mode)

# ------- TileLayer ------- #
class TileLayer(QObject) :
	__PROTO__ = sdk.TileLayer
	def __init__(self,id :str = str() ,z :float = float() ,is_visible :int = int() ,id_hash :int = int() ,cell :List[TileCell] = []) -> TileLayer :
		self._id = id
		self._z = z
		self._is_visible = is_visible
		self._id_hash = id_hash
		self._cell = cell
		pass
	def getid(self) -> str :
		return self._id

	def setid(self,value : str) :
		if self._id != value:
			self._id = value
			self.idChanged.emit(value)

	id = pyqtProperty(str, fget=getid, fset=setid, notify=idChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.id.extend(self._id)
		instance.z.extend(self._z)
		instance.is_visible.extend(self._is_visible)
		instance.id_hash.extend(self._id_hash)
		instance.cell.extend([i.proto() for i in self._cell])

	def getz(self) -> float :
		return self._z

	def setz(self,value : float) :
		if self._z != value:
			self._z = value
			self.zChanged.emit(value)

	z = pyqtProperty(float, fget=getz, fset=setz, notify=zChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.id.extend(self._id)
		instance.z.extend(self._z)
		instance.is_visible.extend(self._is_visible)
		instance.id_hash.extend(self._id_hash)
		instance.cell.extend([i.proto() for i in self._cell])

	def getis_visible(self) -> int :
		return self._is_visible

	def setis_visible(self,value : int) :
		if self._is_visible != value:
			self._is_visible = value
			self.is_visibleChanged.emit(value)

	is_visible = pyqtProperty(int, fget=getis_visible, fset=setis_visible, notify=is_visibleChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.id.extend(self._id)
		instance.z.extend(self._z)
		instance.is_visible.extend(self._is_visible)
		instance.id_hash.extend(self._id_hash)
		instance.cell.extend([i.proto() for i in self._cell])

	def getid_hash(self) -> int :
		return self._id_hash

	def setid_hash(self,value : int) :
		if self._id_hash != value:
			self._id_hash = value
			self.id_hashChanged.emit(value)

	id_hash = pyqtProperty(int, fget=getid_hash, fset=setid_hash, notify=id_hashChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.id.extend(self._id)
		instance.z.extend(self._z)
		instance.is_visible.extend(self._is_visible)
		instance.id_hash.extend(self._id_hash)
		instance.cell.extend([i.proto() for i in self._cell])

	def getcell(self) -> TileCell :
		return self._cell

	def setcell(self,value : List[TileCell]) :
		if self._cell != value:
			self._cell = value
			self.cellChanged.emit(value)

	cell = pyqtProperty(List, fget=getcell, fset=setcell, notify=cellChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.id.extend(self._id)
		instance.z.extend(self._z)
		instance.is_visible.extend(self._is_visible)
		instance.id_hash.extend(self._id_hash)
		instance.cell.extend([i.proto() for i in self._cell])

# ------- TileSet ------- #
class TileSet(QObject) :
	__PROTO__ = sdk.TileSet
	def __init__(self,image :str = str() ,tile_width :int = int() ,tile_height :int = int() ,tile_margin :int = int() ,tile_spacing :int = int() ,collision :str = str() ,material_tag :str = str() ,convex_hulls :List[ConvexHull] = [],convex_hull_points :List[float] = [] ,collision_groups :List[str] = [] ,animations :List[Animation] = [],extrude_borders :int = int() ,inner_padding :int = int() ,sprite_trim_mode :int = int() ) -> TileSet :
		self._image = image
		self._tile_width = tile_width
		self._tile_height = tile_height
		self._tile_margin = tile_margin
		self._tile_spacing = tile_spacing
		self._collision = collision
		self._material_tag = material_tag
		self._convex_hulls = convex_hulls
		self._convex_hull_points = convex_hull_points
		self._collision_groups = collision_groups
		self._animations = animations
		self._extrude_borders = extrude_borders
		self._inner_padding = inner_padding
		self._sprite_trim_mode = sprite_trim_mode
		pass
	def getimage(self) -> str :
		return self._image

	def setimage(self,value : str) :
		if self._image != value:
			self._image = value
			self.imageChanged.emit(value)

	image = pyqtProperty(str, fget=getimage, fset=setimage, notify=imageChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.image.extend(self._image)
		instance.tile_width.extend(self._tile_width)
		instance.tile_height.extend(self._tile_height)
		instance.tile_margin.extend(self._tile_margin)
		instance.tile_spacing.extend(self._tile_spacing)
		instance.collision.extend(self._collision)
		instance.material_tag.extend(self._material_tag)
		instance.convex_hulls.extend([i.proto() for i in self._convex_hulls])
		instance.convex_hull_points = self._convex_hull_points
		instance.collision_groups = self._collision_groups
		instance.animations.extend([i.proto() for i in self._animations])
		instance.extrude_borders.extend(self._extrude_borders)
		instance.inner_padding.extend(self._inner_padding)
		instance.sprite_trim_mode.extend(self._sprite_trim_mode)

	def gettile_width(self) -> int :
		return self._tile_width

	def settile_width(self,value : int) :
		if self._tile_width != value:
			self._tile_width = value
			self.tile_widthChanged.emit(value)

	tile_width = pyqtProperty(int, fget=gettile_width, fset=settile_width, notify=tile_widthChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.image.extend(self._image)
		instance.tile_width.extend(self._tile_width)
		instance.tile_height.extend(self._tile_height)
		instance.tile_margin.extend(self._tile_margin)
		instance.tile_spacing.extend(self._tile_spacing)
		instance.collision.extend(self._collision)
		instance.material_tag.extend(self._material_tag)
		instance.convex_hulls.extend([i.proto() for i in self._convex_hulls])
		instance.convex_hull_points = self._convex_hull_points
		instance.collision_groups = self._collision_groups
		instance.animations.extend([i.proto() for i in self._animations])
		instance.extrude_borders.extend(self._extrude_borders)
		instance.inner_padding.extend(self._inner_padding)
		instance.sprite_trim_mode.extend(self._sprite_trim_mode)

	def gettile_height(self) -> int :
		return self._tile_height

	def settile_height(self,value : int) :
		if self._tile_height != value:
			self._tile_height = value
			self.tile_heightChanged.emit(value)

	tile_height = pyqtProperty(int, fget=gettile_height, fset=settile_height, notify=tile_heightChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.image.extend(self._image)
		instance.tile_width.extend(self._tile_width)
		instance.tile_height.extend(self._tile_height)
		instance.tile_margin.extend(self._tile_margin)
		instance.tile_spacing.extend(self._tile_spacing)
		instance.collision.extend(self._collision)
		instance.material_tag.extend(self._material_tag)
		instance.convex_hulls.extend([i.proto() for i in self._convex_hulls])
		instance.convex_hull_points = self._convex_hull_points
		instance.collision_groups = self._collision_groups
		instance.animations.extend([i.proto() for i in self._animations])
		instance.extrude_borders.extend(self._extrude_borders)
		instance.inner_padding.extend(self._inner_padding)
		instance.sprite_trim_mode.extend(self._sprite_trim_mode)

	def gettile_margin(self) -> int :
		return self._tile_margin

	def settile_margin(self,value : int) :
		if self._tile_margin != value:
			self._tile_margin = value
			self.tile_marginChanged.emit(value)

	tile_margin = pyqtProperty(int, fget=gettile_margin, fset=settile_margin, notify=tile_marginChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.image.extend(self._image)
		instance.tile_width.extend(self._tile_width)
		instance.tile_height.extend(self._tile_height)
		instance.tile_margin.extend(self._tile_margin)
		instance.tile_spacing.extend(self._tile_spacing)
		instance.collision.extend(self._collision)
		instance.material_tag.extend(self._material_tag)
		instance.convex_hulls.extend([i.proto() for i in self._convex_hulls])
		instance.convex_hull_points = self._convex_hull_points
		instance.collision_groups = self._collision_groups
		instance.animations.extend([i.proto() for i in self._animations])
		instance.extrude_borders.extend(self._extrude_borders)
		instance.inner_padding.extend(self._inner_padding)
		instance.sprite_trim_mode.extend(self._sprite_trim_mode)

	def gettile_spacing(self) -> int :
		return self._tile_spacing

	def settile_spacing(self,value : int) :
		if self._tile_spacing != value:
			self._tile_spacing = value
			self.tile_spacingChanged.emit(value)

	tile_spacing = pyqtProperty(int, fget=gettile_spacing, fset=settile_spacing, notify=tile_spacingChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.image.extend(self._image)
		instance.tile_width.extend(self._tile_width)
		instance.tile_height.extend(self._tile_height)
		instance.tile_margin.extend(self._tile_margin)
		instance.tile_spacing.extend(self._tile_spacing)
		instance.collision.extend(self._collision)
		instance.material_tag.extend(self._material_tag)
		instance.convex_hulls.extend([i.proto() for i in self._convex_hulls])
		instance.convex_hull_points = self._convex_hull_points
		instance.collision_groups = self._collision_groups
		instance.animations.extend([i.proto() for i in self._animations])
		instance.extrude_borders.extend(self._extrude_borders)
		instance.inner_padding.extend(self._inner_padding)
		instance.sprite_trim_mode.extend(self._sprite_trim_mode)

	def getcollision(self) -> str :
		return self._collision

	def setcollision(self,value : str) :
		if self._collision != value:
			self._collision = value
			self.collisionChanged.emit(value)

	collision = pyqtProperty(str, fget=getcollision, fset=setcollision, notify=collisionChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.image.extend(self._image)
		instance.tile_width.extend(self._tile_width)
		instance.tile_height.extend(self._tile_height)
		instance.tile_margin.extend(self._tile_margin)
		instance.tile_spacing.extend(self._tile_spacing)
		instance.collision.extend(self._collision)
		instance.material_tag.extend(self._material_tag)
		instance.convex_hulls.extend([i.proto() for i in self._convex_hulls])
		instance.convex_hull_points = self._convex_hull_points
		instance.collision_groups = self._collision_groups
		instance.animations.extend([i.proto() for i in self._animations])
		instance.extrude_borders.extend(self._extrude_borders)
		instance.inner_padding.extend(self._inner_padding)
		instance.sprite_trim_mode.extend(self._sprite_trim_mode)

	def getmaterial_tag(self) -> str :
		return self._material_tag

	def setmaterial_tag(self,value : str) :
		if self._material_tag != value:
			self._material_tag = value
			self.material_tagChanged.emit(value)

	material_tag = pyqtProperty(str, fget=getmaterial_tag, fset=setmaterial_tag, notify=material_tagChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.image.extend(self._image)
		instance.tile_width.extend(self._tile_width)
		instance.tile_height.extend(self._tile_height)
		instance.tile_margin.extend(self._tile_margin)
		instance.tile_spacing.extend(self._tile_spacing)
		instance.collision.extend(self._collision)
		instance.material_tag.extend(self._material_tag)
		instance.convex_hulls.extend([i.proto() for i in self._convex_hulls])
		instance.convex_hull_points = self._convex_hull_points
		instance.collision_groups = self._collision_groups
		instance.animations.extend([i.proto() for i in self._animations])
		instance.extrude_borders.extend(self._extrude_borders)
		instance.inner_padding.extend(self._inner_padding)
		instance.sprite_trim_mode.extend(self._sprite_trim_mode)

	def getconvex_hulls(self) -> ConvexHull :
		return self._convex_hulls

	def setconvex_hulls(self,value : List[ConvexHull]) :
		if self._convex_hulls != value:
			self._convex_hulls = value
			self.convex_hullsChanged.emit(value)

	convex_hulls = pyqtProperty(List, fget=getconvex_hulls, fset=setconvex_hulls, notify=convex_hullsChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.image.extend(self._image)
		instance.tile_width.extend(self._tile_width)
		instance.tile_height.extend(self._tile_height)
		instance.tile_margin.extend(self._tile_margin)
		instance.tile_spacing.extend(self._tile_spacing)
		instance.collision.extend(self._collision)
		instance.material_tag.extend(self._material_tag)
		instance.convex_hulls.extend([i.proto() for i in self._convex_hulls])
		instance.convex_hull_points = self._convex_hull_points
		instance.collision_groups = self._collision_groups
		instance.animations.extend([i.proto() for i in self._animations])
		instance.extrude_borders.extend(self._extrude_borders)
		instance.inner_padding.extend(self._inner_padding)
		instance.sprite_trim_mode.extend(self._sprite_trim_mode)

	def getconvex_hull_points(self) -> float :
		return self._convex_hull_points

	def setconvex_hull_points(self,value : List[float]) :
		if self._convex_hull_points != value:
			self._convex_hull_points = value
			self.convex_hull_pointsChanged.emit(value)

	convex_hull_points = pyqtProperty(List, fget=getconvex_hull_points, fset=setconvex_hull_points, notify=convex_hull_pointsChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.image.extend(self._image)
		instance.tile_width.extend(self._tile_width)
		instance.tile_height.extend(self._tile_height)
		instance.tile_margin.extend(self._tile_margin)
		instance.tile_spacing.extend(self._tile_spacing)
		instance.collision.extend(self._collision)
		instance.material_tag.extend(self._material_tag)
		instance.convex_hulls.extend([i.proto() for i in self._convex_hulls])
		instance.convex_hull_points = self._convex_hull_points
		instance.collision_groups = self._collision_groups
		instance.animations.extend([i.proto() for i in self._animations])
		instance.extrude_borders.extend(self._extrude_borders)
		instance.inner_padding.extend(self._inner_padding)
		instance.sprite_trim_mode.extend(self._sprite_trim_mode)

	def getcollision_groups(self) -> str :
		return self._collision_groups

	def setcollision_groups(self,value : List[str]) :
		if self._collision_groups != value:
			self._collision_groups = value
			self.collision_groupsChanged.emit(value)

	collision_groups = pyqtProperty(List, fget=getcollision_groups, fset=setcollision_groups, notify=collision_groupsChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.image.extend(self._image)
		instance.tile_width.extend(self._tile_width)
		instance.tile_height.extend(self._tile_height)
		instance.tile_margin.extend(self._tile_margin)
		instance.tile_spacing.extend(self._tile_spacing)
		instance.collision.extend(self._collision)
		instance.material_tag.extend(self._material_tag)
		instance.convex_hulls.extend([i.proto() for i in self._convex_hulls])
		instance.convex_hull_points = self._convex_hull_points
		instance.collision_groups = self._collision_groups
		instance.animations.extend([i.proto() for i in self._animations])
		instance.extrude_borders.extend(self._extrude_borders)
		instance.inner_padding.extend(self._inner_padding)
		instance.sprite_trim_mode.extend(self._sprite_trim_mode)

	def getanimations(self) -> Animation :
		return self._animations

	def setanimations(self,value : List[Animation]) :
		if self._animations != value:
			self._animations = value
			self.animationsChanged.emit(value)

	animations = pyqtProperty(List, fget=getanimations, fset=setanimations, notify=animationsChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.image.extend(self._image)
		instance.tile_width.extend(self._tile_width)
		instance.tile_height.extend(self._tile_height)
		instance.tile_margin.extend(self._tile_margin)
		instance.tile_spacing.extend(self._tile_spacing)
		instance.collision.extend(self._collision)
		instance.material_tag.extend(self._material_tag)
		instance.convex_hulls.extend([i.proto() for i in self._convex_hulls])
		instance.convex_hull_points = self._convex_hull_points
		instance.collision_groups = self._collision_groups
		instance.animations.extend([i.proto() for i in self._animations])
		instance.extrude_borders.extend(self._extrude_borders)
		instance.inner_padding.extend(self._inner_padding)
		instance.sprite_trim_mode.extend(self._sprite_trim_mode)

	def getextrude_borders(self) -> int :
		return self._extrude_borders

	def setextrude_borders(self,value : int) :
		if self._extrude_borders != value:
			self._extrude_borders = value
			self.extrude_bordersChanged.emit(value)

	extrude_borders = pyqtProperty(int, fget=getextrude_borders, fset=setextrude_borders, notify=extrude_bordersChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.image.extend(self._image)
		instance.tile_width.extend(self._tile_width)
		instance.tile_height.extend(self._tile_height)
		instance.tile_margin.extend(self._tile_margin)
		instance.tile_spacing.extend(self._tile_spacing)
		instance.collision.extend(self._collision)
		instance.material_tag.extend(self._material_tag)
		instance.convex_hulls.extend([i.proto() for i in self._convex_hulls])
		instance.convex_hull_points = self._convex_hull_points
		instance.collision_groups = self._collision_groups
		instance.animations.extend([i.proto() for i in self._animations])
		instance.extrude_borders.extend(self._extrude_borders)
		instance.inner_padding.extend(self._inner_padding)
		instance.sprite_trim_mode.extend(self._sprite_trim_mode)

	def getinner_padding(self) -> int :
		return self._inner_padding

	def setinner_padding(self,value : int) :
		if self._inner_padding != value:
			self._inner_padding = value
			self.inner_paddingChanged.emit(value)

	inner_padding = pyqtProperty(int, fget=getinner_padding, fset=setinner_padding, notify=inner_paddingChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.image.extend(self._image)
		instance.tile_width.extend(self._tile_width)
		instance.tile_height.extend(self._tile_height)
		instance.tile_margin.extend(self._tile_margin)
		instance.tile_spacing.extend(self._tile_spacing)
		instance.collision.extend(self._collision)
		instance.material_tag.extend(self._material_tag)
		instance.convex_hulls.extend([i.proto() for i in self._convex_hulls])
		instance.convex_hull_points = self._convex_hull_points
		instance.collision_groups = self._collision_groups
		instance.animations.extend([i.proto() for i in self._animations])
		instance.extrude_borders.extend(self._extrude_borders)
		instance.inner_padding.extend(self._inner_padding)
		instance.sprite_trim_mode.extend(self._sprite_trim_mode)

	def getsprite_trim_mode(self) -> int :
		return self._sprite_trim_mode

	def setsprite_trim_mode(self,value : int) :
		if self._sprite_trim_mode != value:
			self._sprite_trim_mode = value
			self.sprite_trim_modeChanged.emit(value)

	sprite_trim_mode = pyqtProperty(int, fget=getsprite_trim_mode, fset=setsprite_trim_mode, notify=sprite_trim_modeChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.image.extend(self._image)
		instance.tile_width.extend(self._tile_width)
		instance.tile_height.extend(self._tile_height)
		instance.tile_margin.extend(self._tile_margin)
		instance.tile_spacing.extend(self._tile_spacing)
		instance.collision.extend(self._collision)
		instance.material_tag.extend(self._material_tag)
		instance.convex_hulls.extend([i.proto() for i in self._convex_hulls])
		instance.convex_hull_points = self._convex_hull_points
		instance.collision_groups = self._collision_groups
		instance.animations.extend([i.proto() for i in self._animations])
		instance.extrude_borders.extend(self._extrude_borders)
		instance.inner_padding.extend(self._inner_padding)
		instance.sprite_trim_mode.extend(self._sprite_trim_mode)

# ------- TogglePhysicsDebug ------- #
class TogglePhysicsDebug(QObject) :
	__PROTO__ = sdk.TogglePhysicsDebug
	def __init__(self) -> TogglePhysicsDebug :
		pass
# ------- ToggleProfile ------- #
class ToggleProfile(QObject) :
	__PROTO__ = sdk.ToggleProfile
	def __init__(self) -> ToggleProfile :
		pass
# ------- Transform ------- #
class Transform(QObject) :
	__PROTO__ = sdk.Transform
	def __init__(self,rotation :Quat = None ,translation :Vector3 = None ,scale :Vector3 = None ) -> Transform :
		self._rotation = rotation
		self._translation = translation
		self._scale = scale
		pass
	def getrotation(self) -> Quat :
		return self._rotation

	def setrotation(self,value : Quat) :
		if self._rotation != value:
			self._rotation = value
			self.rotationChanged.emit(value)

	rotation = pyqtProperty(QObject, fget=getrotation, fset=setrotation, notify=rotationChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.rotation = self._rotation.proto()
		instance.translation = self._translation.proto()
		instance.scale = self._scale.proto()

	def gettranslation(self) -> Vector3 :
		return self._translation

	def settranslation(self,value : Vector3) :
		if self._translation != value:
			self._translation = value
			self.translationChanged.emit(value)

	translation = pyqtProperty(QObject, fget=gettranslation, fset=settranslation, notify=translationChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.rotation = self._rotation.proto()
		instance.translation = self._translation.proto()
		instance.scale = self._scale.proto()

	def getscale(self) -> Vector3 :
		return self._scale

	def setscale(self,value : Vector3) :
		if self._scale != value:
			self._scale = value
			self.scaleChanged.emit(value)

	scale = pyqtProperty(QObject, fget=getscale, fset=setscale, notify=scaleChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.rotation = self._rotation.proto()
		instance.translation = self._translation.proto()
		instance.scale = self._scale.proto()

# ------- Trigger ------- #
class Trigger(QObject) :
	__PROTO__ = sdk.Trigger
	def __init__(self,id :int = int() ,group :int = int() ) -> Trigger :
		self._id = id
		self._group = group
		pass
	def getid(self) -> int :
		return self._id

	def setid(self,value : int) :
		if self._id != value:
			self._id = value
			self.idChanged.emit(value)

	id = pyqtProperty(int, fget=getid, fset=setid, notify=idChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.id.extend(self._id)
		instance.group.extend(self._group)

	def getgroup(self) -> int :
		return self._group

	def setgroup(self,value : int) :
		if self._group != value:
			self._group = value
			self.groupChanged.emit(value)

	group = pyqtProperty(int, fget=getgroup, fset=setgroup, notify=groupChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.id.extend(self._id)
		instance.group.extend(self._group)

# ------- TriggerEvent ------- #
class TriggerEvent(QObject) :
	__PROTO__ = sdk.TriggerEvent
	def __init__(self,enter :bool = bool() ,a :Trigger = None ,b :Trigger = None ) -> TriggerEvent :
		self._enter = enter
		self._a = a
		self._b = b
		pass
	def getenter(self) -> bool :
		return self._enter

	def setenter(self,value : bool) :
		if self._enter != value:
			self._enter = value
			self.enterChanged.emit(value)

	enter = pyqtProperty(bool, fget=getenter, fset=setenter, notify=enterChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.enter.extend(self._enter)
		instance.a = self._a.proto()
		instance.b = self._b.proto()

	def geta(self) -> Trigger :
		return self._a

	def seta(self,value : Trigger) :
		if self._a != value:
			self._a = value
			self.aChanged.emit(value)

	a = pyqtProperty(QObject, fget=geta, fset=seta, notify=aChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.enter.extend(self._enter)
		instance.a = self._a.proto()
		instance.b = self._b.proto()

	def getb(self) -> Trigger :
		return self._b

	def setb(self,value : Trigger) :
		if self._b != value:
			self._b = value
			self.bChanged.emit(value)

	b = pyqtProperty(QObject, fget=getb, fset=setb, notify=bChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.enter.extend(self._enter)
		instance.a = self._a.proto()
		instance.b = self._b.proto()

# ------- TriggerResponse ------- #
class TriggerResponse(QObject) :
	__PROTO__ = sdk.TriggerResponse
	def __init__(self,other_id :int = int() ,enter :bool = bool() ,group :int = int() ,other_group :int = int() ,own_group :int = int() ) -> TriggerResponse :
		self._other_id = other_id
		self._enter = enter
		self._group = group
		self._other_group = other_group
		self._own_group = own_group
		pass
	def getother_id(self) -> int :
		return self._other_id

	def setother_id(self,value : int) :
		if self._other_id != value:
			self._other_id = value
			self.other_idChanged.emit(value)

	other_id = pyqtProperty(int, fget=getother_id, fset=setother_id, notify=other_idChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.other_id.extend(self._other_id)
		instance.enter.extend(self._enter)
		instance.group.extend(self._group)
		instance.other_group.extend(self._other_group)
		instance.own_group.extend(self._own_group)

	def getenter(self) -> bool :
		return self._enter

	def setenter(self,value : bool) :
		if self._enter != value:
			self._enter = value
			self.enterChanged.emit(value)

	enter = pyqtProperty(bool, fget=getenter, fset=setenter, notify=enterChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.other_id.extend(self._other_id)
		instance.enter.extend(self._enter)
		instance.group.extend(self._group)
		instance.other_group.extend(self._other_group)
		instance.own_group.extend(self._own_group)

	def getgroup(self) -> int :
		return self._group

	def setgroup(self,value : int) :
		if self._group != value:
			self._group = value
			self.groupChanged.emit(value)

	group = pyqtProperty(int, fget=getgroup, fset=setgroup, notify=groupChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.other_id.extend(self._other_id)
		instance.enter.extend(self._enter)
		instance.group.extend(self._group)
		instance.other_group.extend(self._other_group)
		instance.own_group.extend(self._own_group)

	def getother_group(self) -> int :
		return self._other_group

	def setother_group(self,value : int) :
		if self._other_group != value:
			self._other_group = value
			self.other_groupChanged.emit(value)

	other_group = pyqtProperty(int, fget=getother_group, fset=setother_group, notify=other_groupChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.other_id.extend(self._other_id)
		instance.enter.extend(self._enter)
		instance.group.extend(self._group)
		instance.other_group.extend(self._other_group)
		instance.own_group.extend(self._own_group)

	def getown_group(self) -> int :
		return self._own_group

	def setown_group(self,value : int) :
		if self._own_group != value:
			self._own_group = value
			self.own_groupChanged.emit(value)

	own_group = pyqtProperty(int, fget=getown_group, fset=setown_group, notify=own_groupChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.other_id.extend(self._other_id)
		instance.enter.extend(self._enter)
		instance.group.extend(self._group)
		instance.other_group.extend(self._other_group)
		instance.own_group.extend(self._own_group)

# ------- Vector3 ------- #
class Vector3(QObject) :
	__PROTO__ = sdk.Vector3
	def __init__(self,x :float = float() ,y :float = float() ,z :float = float() ,d :float = float() ) -> Vector3 :
		self._x = x
		self._y = y
		self._z = z
		self._d = d
		pass
	def getx(self) -> float :
		return self._x

	def setx(self,value : float) :
		if self._x != value:
			self._x = value
			self.xChanged.emit(value)

	x = pyqtProperty(float, fget=getx, fset=setx, notify=xChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.x.extend(self._x)
		instance.y.extend(self._y)
		instance.z.extend(self._z)
		instance.d.extend(self._d)

	def gety(self) -> float :
		return self._y

	def sety(self,value : float) :
		if self._y != value:
			self._y = value
			self.yChanged.emit(value)

	y = pyqtProperty(float, fget=gety, fset=sety, notify=yChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.x.extend(self._x)
		instance.y.extend(self._y)
		instance.z.extend(self._z)
		instance.d.extend(self._d)

	def getz(self) -> float :
		return self._z

	def setz(self,value : float) :
		if self._z != value:
			self._z = value
			self.zChanged.emit(value)

	z = pyqtProperty(float, fget=getz, fset=setz, notify=zChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.x.extend(self._x)
		instance.y.extend(self._y)
		instance.z.extend(self._z)
		instance.d.extend(self._d)

	def getd(self) -> float :
		return self._d

	def setd(self,value : float) :
		if self._d != value:
			self._d = value
			self.dChanged.emit(value)

	d = pyqtProperty(float, fget=getd, fset=setd, notify=dChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.x.extend(self._x)
		instance.y.extend(self._y)
		instance.z.extend(self._z)
		instance.d.extend(self._d)

# ------- Vector3One ------- #
class Vector3One(QObject) :
	__PROTO__ = sdk.Vector3One
	def __init__(self,x :float = float() ,y :float = float() ,z :float = float() ,d :float = float() ) -> Vector3One :
		self._x = x
		self._y = y
		self._z = z
		self._d = d
		pass
	def getx(self) -> float :
		return self._x

	def setx(self,value : float) :
		if self._x != value:
			self._x = value
			self.xChanged.emit(value)

	x = pyqtProperty(float, fget=getx, fset=setx, notify=xChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.x.extend(self._x)
		instance.y.extend(self._y)
		instance.z.extend(self._z)
		instance.d.extend(self._d)

	def gety(self) -> float :
		return self._y

	def sety(self,value : float) :
		if self._y != value:
			self._y = value
			self.yChanged.emit(value)

	y = pyqtProperty(float, fget=gety, fset=sety, notify=yChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.x.extend(self._x)
		instance.y.extend(self._y)
		instance.z.extend(self._z)
		instance.d.extend(self._d)

	def getz(self) -> float :
		return self._z

	def setz(self,value : float) :
		if self._z != value:
			self._z = value
			self.zChanged.emit(value)

	z = pyqtProperty(float, fget=getz, fset=setz, notify=zChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.x.extend(self._x)
		instance.y.extend(self._y)
		instance.z.extend(self._z)
		instance.d.extend(self._d)

	def getd(self) -> float :
		return self._d

	def setd(self,value : float) :
		if self._d != value:
			self._d = value
			self.dChanged.emit(value)

	d = pyqtProperty(float, fget=getd, fset=setd, notify=dChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.x.extend(self._x)
		instance.y.extend(self._y)
		instance.z.extend(self._z)
		instance.d.extend(self._d)

# ------- Vector4 ------- #
class Vector4(QObject) :
	__PROTO__ = sdk.Vector4
	def __init__(self,x :float = float() ,y :float = float() ,z :float = float() ,w :float = float() ) -> Vector4 :
		self._x = x
		self._y = y
		self._z = z
		self._w = w
		pass
	def getx(self) -> float :
		return self._x

	def setx(self,value : float) :
		if self._x != value:
			self._x = value
			self.xChanged.emit(value)

	x = pyqtProperty(float, fget=getx, fset=setx, notify=xChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.x.extend(self._x)
		instance.y.extend(self._y)
		instance.z.extend(self._z)
		instance.w.extend(self._w)

	def gety(self) -> float :
		return self._y

	def sety(self,value : float) :
		if self._y != value:
			self._y = value
			self.yChanged.emit(value)

	y = pyqtProperty(float, fget=gety, fset=sety, notify=yChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.x.extend(self._x)
		instance.y.extend(self._y)
		instance.z.extend(self._z)
		instance.w.extend(self._w)

	def getz(self) -> float :
		return self._z

	def setz(self,value : float) :
		if self._z != value:
			self._z = value
			self.zChanged.emit(value)

	z = pyqtProperty(float, fget=getz, fset=setz, notify=zChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.x.extend(self._x)
		instance.y.extend(self._y)
		instance.z.extend(self._z)
		instance.w.extend(self._w)

	def getw(self) -> float :
		return self._w

	def setw(self,value : float) :
		if self._w != value:
			self._w = value
			self.wChanged.emit(value)

	w = pyqtProperty(float, fget=getw, fset=setw, notify=wChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.x.extend(self._x)
		instance.y.extend(self._y)
		instance.z.extend(self._z)
		instance.w.extend(self._w)

# ------- Vector4One ------- #
class Vector4One(QObject) :
	__PROTO__ = sdk.Vector4One
	def __init__(self,x :float = float() ,y :float = float() ,z :float = float() ,w :float = float() ) -> Vector4One :
		self._x = x
		self._y = y
		self._z = z
		self._w = w
		pass
	def getx(self) -> float :
		return self._x

	def setx(self,value : float) :
		if self._x != value:
			self._x = value
			self.xChanged.emit(value)

	x = pyqtProperty(float, fget=getx, fset=setx, notify=xChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.x.extend(self._x)
		instance.y.extend(self._y)
		instance.z.extend(self._z)
		instance.w.extend(self._w)

	def gety(self) -> float :
		return self._y

	def sety(self,value : float) :
		if self._y != value:
			self._y = value
			self.yChanged.emit(value)

	y = pyqtProperty(float, fget=gety, fset=sety, notify=yChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.x.extend(self._x)
		instance.y.extend(self._y)
		instance.z.extend(self._z)
		instance.w.extend(self._w)

	def getz(self) -> float :
		return self._z

	def setz(self,value : float) :
		if self._z != value:
			self._z = value
			self.zChanged.emit(value)

	z = pyqtProperty(float, fget=getz, fset=setz, notify=zChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.x.extend(self._x)
		instance.y.extend(self._y)
		instance.z.extend(self._z)
		instance.w.extend(self._w)

	def getw(self) -> float :
		return self._w

	def setw(self,value : float) :
		if self._w != value:
			self._w = value
			self.wChanged.emit(value)

	w = pyqtProperty(float, fget=getw, fset=setw, notify=wChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.x.extend(self._x)
		instance.y.extend(self._y)
		instance.z.extend(self._z)
		instance.w.extend(self._w)

# ------- Vector4WOne ------- #
class Vector4WOne(QObject) :
	__PROTO__ = sdk.Vector4WOne
	def __init__(self,x :float = float() ,y :float = float() ,z :float = float() ,w :float = float() ) -> Vector4WOne :
		self._x = x
		self._y = y
		self._z = z
		self._w = w
		pass
	def getx(self) -> float :
		return self._x

	def setx(self,value : float) :
		if self._x != value:
			self._x = value
			self.xChanged.emit(value)

	x = pyqtProperty(float, fget=getx, fset=setx, notify=xChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.x.extend(self._x)
		instance.y.extend(self._y)
		instance.z.extend(self._z)
		instance.w.extend(self._w)

	def gety(self) -> float :
		return self._y

	def sety(self,value : float) :
		if self._y != value:
			self._y = value
			self.yChanged.emit(value)

	y = pyqtProperty(float, fget=gety, fset=sety, notify=yChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.x.extend(self._x)
		instance.y.extend(self._y)
		instance.z.extend(self._z)
		instance.w.extend(self._w)

	def getz(self) -> float :
		return self._z

	def setz(self,value : float) :
		if self._z != value:
			self._z = value
			self.zChanged.emit(value)

	z = pyqtProperty(float, fget=getz, fset=setz, notify=zChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.x.extend(self._x)
		instance.y.extend(self._y)
		instance.z.extend(self._z)
		instance.w.extend(self._w)

	def getw(self) -> float :
		return self._w

	def setw(self,value : float) :
		if self._w != value:
			self._w = value
			self.wChanged.emit(value)

	w = pyqtProperty(float, fget=getw, fset=setw, notify=wChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.x.extend(self._x)
		instance.y.extend(self._y)
		instance.z.extend(self._z)
		instance.w.extend(self._w)

# ------- VelocityResponse ------- #
class VelocityResponse(QObject) :
	__PROTO__ = sdk.VelocityResponse
	def __init__(self,linear_velocity :Vector3 = None ,angular_velocity :Vector3 = None ) -> VelocityResponse :
		self._linear_velocity = linear_velocity
		self._angular_velocity = angular_velocity
		pass
	def getlinear_velocity(self) -> Vector3 :
		return self._linear_velocity

	def setlinear_velocity(self,value : Vector3) :
		if self._linear_velocity != value:
			self._linear_velocity = value
			self.linear_velocityChanged.emit(value)

	linear_velocity = pyqtProperty(QObject, fget=getlinear_velocity, fset=setlinear_velocity, notify=linear_velocityChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.linear_velocity = self._linear_velocity.proto()
		instance.angular_velocity = self._angular_velocity.proto()

	def getangular_velocity(self) -> Vector3 :
		return self._angular_velocity

	def setangular_velocity(self,value : Vector3) :
		if self._angular_velocity != value:
			self._angular_velocity = value
			self.angular_velocityChanged.emit(value)

	angular_velocity = pyqtProperty(QObject, fget=getangular_velocity, fset=setangular_velocity, notify=angular_velocityChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.linear_velocity = self._linear_velocity.proto()
		instance.angular_velocity = self._angular_velocity.proto()

# ------- VertexAttribute ------- #
class DataType(Enum):
	TYPE_BYTE = 1
	TYPE_UNSIGNED_BYTE = 2
	TYPE_SHORT = 3
	TYPE_UNSIGNED_SHORT = 4
	TYPE_INT = 5
	TYPE_UNSIGNED_INT = 6
	TYPE_FLOAT = 7
class VectorType(Enum):
	VECTOR_TYPE_SCALAR = 1
	VECTOR_TYPE_VEC2 = 2
	VECTOR_TYPE_VEC3 = 3
	VECTOR_TYPE_VEC4 = 4
	VECTOR_TYPE_MAT2 = 5
	VECTOR_TYPE_MAT3 = 6
	VECTOR_TYPE_MAT4 = 7
class SemanticType(Enum):
	SEMANTIC_TYPE_NONE = 1
	SEMANTIC_TYPE_POSITION = 2
	SEMANTIC_TYPE_TEXCOORD = 3
	SEMANTIC_TYPE_PAGE_INDEX = 4
	SEMANTIC_TYPE_COLOR = 5
	SEMANTIC_TYPE_NORMAL = 6
	SEMANTIC_TYPE_TANGENT = 7
	SEMANTIC_TYPE_WORLD_MATRIX = 8
	SEMANTIC_TYPE_NORMAL_MATRIX = 9
	SEMANTIC_TYPE_BONE_WEIGHTS = 10
	SEMANTIC_TYPE_BONE_INDICES = 11
class VertexAttribute(QObject) :
	__PROTO__ = sdk.VertexAttribute
	def __init__(self,name :str = str() ,name_hash :int = int() ,semantic_type :int = int() ,element_count :int = int() ,normalize :bool = bool() ,data_type :int = int() ,coordinate_space :int = int() ,step_function :int = int() ,vector_type :int = int() ,long_values :LongValues = None ,double_values :DoubleValues = None ,binary_values :bytes = bytes() ) -> VertexAttribute :
		self._name = name
		self._name_hash = name_hash
		self._semantic_type = semantic_type
		self._element_count = element_count
		self._normalize = normalize
		self._data_type = data_type
		self._coordinate_space = coordinate_space
		self._step_function = step_function
		self._vector_type = vector_type
		self._long_values = long_values
		self._double_values = double_values
		self._binary_values = binary_values
		pass
	def getname(self) -> str :
		return self._name

	def setname(self,value : str) :
		if self._name != value:
			self._name = value
			self.nameChanged.emit(value)

	name = pyqtProperty(str, fget=getname, fset=setname, notify=nameChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.name.extend(self._name)
		instance.name_hash.extend(self._name_hash)
		instance.semantic_type.extend(self._semantic_type)
		instance.element_count.extend(self._element_count)
		instance.normalize.extend(self._normalize)
		instance.data_type.extend(self._data_type)
		instance.coordinate_space.extend(self._coordinate_space)
		instance.step_function.extend(self._step_function)
		instance.vector_type.extend(self._vector_type)
		instance.long_values = self._long_values.proto()
		instance.double_values = self._double_values.proto()
		instance.binary_values.extend(self._binary_values)

	def getname_hash(self) -> int :
		return self._name_hash

	def setname_hash(self,value : int) :
		if self._name_hash != value:
			self._name_hash = value
			self.name_hashChanged.emit(value)

	name_hash = pyqtProperty(int, fget=getname_hash, fset=setname_hash, notify=name_hashChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.name.extend(self._name)
		instance.name_hash.extend(self._name_hash)
		instance.semantic_type.extend(self._semantic_type)
		instance.element_count.extend(self._element_count)
		instance.normalize.extend(self._normalize)
		instance.data_type.extend(self._data_type)
		instance.coordinate_space.extend(self._coordinate_space)
		instance.step_function.extend(self._step_function)
		instance.vector_type.extend(self._vector_type)
		instance.long_values = self._long_values.proto()
		instance.double_values = self._double_values.proto()
		instance.binary_values.extend(self._binary_values)

	def getsemantic_type(self) -> int :
		return self._semantic_type

	def setsemantic_type(self,value : int) :
		if self._semantic_type != value:
			self._semantic_type = value
			self.semantic_typeChanged.emit(value)

	semantic_type = pyqtProperty(int, fget=getsemantic_type, fset=setsemantic_type, notify=semantic_typeChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.name.extend(self._name)
		instance.name_hash.extend(self._name_hash)
		instance.semantic_type.extend(self._semantic_type)
		instance.element_count.extend(self._element_count)
		instance.normalize.extend(self._normalize)
		instance.data_type.extend(self._data_type)
		instance.coordinate_space.extend(self._coordinate_space)
		instance.step_function.extend(self._step_function)
		instance.vector_type.extend(self._vector_type)
		instance.long_values = self._long_values.proto()
		instance.double_values = self._double_values.proto()
		instance.binary_values.extend(self._binary_values)

	def getelement_count(self) -> int :
		return self._element_count

	def setelement_count(self,value : int) :
		if self._element_count != value:
			self._element_count = value
			self.element_countChanged.emit(value)

	element_count = pyqtProperty(int, fget=getelement_count, fset=setelement_count, notify=element_countChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.name.extend(self._name)
		instance.name_hash.extend(self._name_hash)
		instance.semantic_type.extend(self._semantic_type)
		instance.element_count.extend(self._element_count)
		instance.normalize.extend(self._normalize)
		instance.data_type.extend(self._data_type)
		instance.coordinate_space.extend(self._coordinate_space)
		instance.step_function.extend(self._step_function)
		instance.vector_type.extend(self._vector_type)
		instance.long_values = self._long_values.proto()
		instance.double_values = self._double_values.proto()
		instance.binary_values.extend(self._binary_values)

	def getnormalize(self) -> bool :
		return self._normalize

	def setnormalize(self,value : bool) :
		if self._normalize != value:
			self._normalize = value
			self.normalizeChanged.emit(value)

	normalize = pyqtProperty(bool, fget=getnormalize, fset=setnormalize, notify=normalizeChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.name.extend(self._name)
		instance.name_hash.extend(self._name_hash)
		instance.semantic_type.extend(self._semantic_type)
		instance.element_count.extend(self._element_count)
		instance.normalize.extend(self._normalize)
		instance.data_type.extend(self._data_type)
		instance.coordinate_space.extend(self._coordinate_space)
		instance.step_function.extend(self._step_function)
		instance.vector_type.extend(self._vector_type)
		instance.long_values = self._long_values.proto()
		instance.double_values = self._double_values.proto()
		instance.binary_values.extend(self._binary_values)

	def getdata_type(self) -> int :
		return self._data_type

	def setdata_type(self,value : int) :
		if self._data_type != value:
			self._data_type = value
			self.data_typeChanged.emit(value)

	data_type = pyqtProperty(int, fget=getdata_type, fset=setdata_type, notify=data_typeChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.name.extend(self._name)
		instance.name_hash.extend(self._name_hash)
		instance.semantic_type.extend(self._semantic_type)
		instance.element_count.extend(self._element_count)
		instance.normalize.extend(self._normalize)
		instance.data_type.extend(self._data_type)
		instance.coordinate_space.extend(self._coordinate_space)
		instance.step_function.extend(self._step_function)
		instance.vector_type.extend(self._vector_type)
		instance.long_values = self._long_values.proto()
		instance.double_values = self._double_values.proto()
		instance.binary_values.extend(self._binary_values)

	def getcoordinate_space(self) -> int :
		return self._coordinate_space

	def setcoordinate_space(self,value : int) :
		if self._coordinate_space != value:
			self._coordinate_space = value
			self.coordinate_spaceChanged.emit(value)

	coordinate_space = pyqtProperty(int, fget=getcoordinate_space, fset=setcoordinate_space, notify=coordinate_spaceChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.name.extend(self._name)
		instance.name_hash.extend(self._name_hash)
		instance.semantic_type.extend(self._semantic_type)
		instance.element_count.extend(self._element_count)
		instance.normalize.extend(self._normalize)
		instance.data_type.extend(self._data_type)
		instance.coordinate_space.extend(self._coordinate_space)
		instance.step_function.extend(self._step_function)
		instance.vector_type.extend(self._vector_type)
		instance.long_values = self._long_values.proto()
		instance.double_values = self._double_values.proto()
		instance.binary_values.extend(self._binary_values)

	def getstep_function(self) -> int :
		return self._step_function

	def setstep_function(self,value : int) :
		if self._step_function != value:
			self._step_function = value
			self.step_functionChanged.emit(value)

	step_function = pyqtProperty(int, fget=getstep_function, fset=setstep_function, notify=step_functionChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.name.extend(self._name)
		instance.name_hash.extend(self._name_hash)
		instance.semantic_type.extend(self._semantic_type)
		instance.element_count.extend(self._element_count)
		instance.normalize.extend(self._normalize)
		instance.data_type.extend(self._data_type)
		instance.coordinate_space.extend(self._coordinate_space)
		instance.step_function.extend(self._step_function)
		instance.vector_type.extend(self._vector_type)
		instance.long_values = self._long_values.proto()
		instance.double_values = self._double_values.proto()
		instance.binary_values.extend(self._binary_values)

	def getvector_type(self) -> int :
		return self._vector_type

	def setvector_type(self,value : int) :
		if self._vector_type != value:
			self._vector_type = value
			self.vector_typeChanged.emit(value)

	vector_type = pyqtProperty(int, fget=getvector_type, fset=setvector_type, notify=vector_typeChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.name.extend(self._name)
		instance.name_hash.extend(self._name_hash)
		instance.semantic_type.extend(self._semantic_type)
		instance.element_count.extend(self._element_count)
		instance.normalize.extend(self._normalize)
		instance.data_type.extend(self._data_type)
		instance.coordinate_space.extend(self._coordinate_space)
		instance.step_function.extend(self._step_function)
		instance.vector_type.extend(self._vector_type)
		instance.long_values = self._long_values.proto()
		instance.double_values = self._double_values.proto()
		instance.binary_values.extend(self._binary_values)

	def getlong_values(self) -> LongValues :
		return self._long_values

	def setlong_values(self,value : LongValues) :
		if self._long_values != value:
			self._long_values = value
			self.long_valuesChanged.emit(value)

	long_values = pyqtProperty(QObject, fget=getlong_values, fset=setlong_values, notify=long_valuesChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.name.extend(self._name)
		instance.name_hash.extend(self._name_hash)
		instance.semantic_type.extend(self._semantic_type)
		instance.element_count.extend(self._element_count)
		instance.normalize.extend(self._normalize)
		instance.data_type.extend(self._data_type)
		instance.coordinate_space.extend(self._coordinate_space)
		instance.step_function.extend(self._step_function)
		instance.vector_type.extend(self._vector_type)
		instance.long_values = self._long_values.proto()
		instance.double_values = self._double_values.proto()
		instance.binary_values.extend(self._binary_values)

	def getdouble_values(self) -> DoubleValues :
		return self._double_values

	def setdouble_values(self,value : DoubleValues) :
		if self._double_values != value:
			self._double_values = value
			self.double_valuesChanged.emit(value)

	double_values = pyqtProperty(QObject, fget=getdouble_values, fset=setdouble_values, notify=double_valuesChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.name.extend(self._name)
		instance.name_hash.extend(self._name_hash)
		instance.semantic_type.extend(self._semantic_type)
		instance.element_count.extend(self._element_count)
		instance.normalize.extend(self._normalize)
		instance.data_type.extend(self._data_type)
		instance.coordinate_space.extend(self._coordinate_space)
		instance.step_function.extend(self._step_function)
		instance.vector_type.extend(self._vector_type)
		instance.long_values = self._long_values.proto()
		instance.double_values = self._double_values.proto()
		instance.binary_values.extend(self._binary_values)

	def getbinary_values(self) -> bytes :
		return self._binary_values

	def setbinary_values(self,value : bytes) :
		if self._binary_values != value:
			self._binary_values = value
			self.binary_valuesChanged.emit(value)

	binary_values = pyqtProperty(bytes, fget=getbinary_values, fset=setbinary_values, notify=binary_valuesChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.name.extend(self._name)
		instance.name_hash.extend(self._name_hash)
		instance.semantic_type.extend(self._semantic_type)
		instance.element_count.extend(self._element_count)
		instance.normalize.extend(self._normalize)
		instance.data_type.extend(self._data_type)
		instance.coordinate_space.extend(self._coordinate_space)
		instance.step_function.extend(self._step_function)
		instance.vector_type.extend(self._vector_type)
		instance.long_values = self._long_values.proto()
		instance.double_values = self._double_values.proto()
		instance.binary_values.extend(self._binary_values)

# ------- WindowResized ------- #
class WindowResized(QObject) :
	__PROTO__ = sdk.WindowResized
	def __init__(self,width :int = int() ,height :int = int() ) -> WindowResized :
		self._width = width
		self._height = height
		pass
	def getwidth(self) -> int :
		return self._width

	def setwidth(self,value : int) :
		if self._width != value:
			self._width = value
			self.widthChanged.emit(value)

	width = pyqtProperty(int, fget=getwidth, fset=setwidth, notify=widthChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.width.extend(self._width)
		instance.height.extend(self._height)

	def getheight(self) -> int :
		return self._height

	def setheight(self,value : int) :
		if self._height != value:
			self._height = value
			self.heightChanged.emit(value)

	height = pyqtProperty(int, fget=getheight, fset=setheight, notify=heightChanged)

	def proto(self) :
		instance = self.__PROTO__()
		instance.width.extend(self._width)
		instance.height.extend(self._height)

