uniform int object_id = 0;
uniform vec3 object_color = vec3(1.0, 0.0, 1.0);

#ifdef V3D_LIGHTING_STUDIO
in vec3 normal_viewport;
#endif /* V3D_LIGHTING_STUDIO */

layout(location=0) out uint objectId;
layout(location=1) out vec4 diffuseColor;
#ifdef V3D_LIGHTING_STUDIO
#ifdef WORKBENCH_ENCODE_NORMALS
layout(location=2) out vec2 normalViewport;
#else /* WORKBENCH_ENCODE_NORMALS */
layout(location=2) out vec3 normalViewport;
#endif /* WORKBENCH_ENCODE_NORMALS */
#endif /* V3D_LIGHTING_STUDIO */

void main()
{
	objectId = uint(object_id);
	diffuseColor = vec4(object_color, 0.0);
#ifdef V3D_LIGHTING_STUDIO
#ifdef WORKBENCH_ENCODE_NORMALS
	if (!gl_FrontFacing) {
		normalViewport = normal_encode(-normal_viewport);
		diffuseColor.a = 1.0;
	} else {
		normalViewport = normal_encode(normal_viewport);
	}
#else /* WORKBENCH_ENCODE_NORMALS */
	normalViewport = normal_viewport;
#endif /* WORKBENCH_ENCODE_NORMALS */
#endif /* V3D_LIGHTING_STUDIO */
}
