# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####

# <pep8 compliant>
import bpy
from bpy.types import Header, Menu


class OUTLINER_HT_header(Header):
    bl_space_type = 'OUTLINER'

    def draw(self, context):
        layout = self.layout

        space = context.space_data
        display_mode = space.display_mode
        scene = context.scene
        ks = context.scene.keying_sets.active
        support_filters = display_mode in {'COLLECTIONS', 'VIEW_LAYER'}

        row = layout.row(align=True)
        row.template_header()

        layout.prop(space, "display_mode", text="")

        OUTLINER_MT_editor_menus.draw_collapsible(context, layout)

        if space.display_mode == 'DATABLOCKS':
            layout.separator()

            row = layout.row(align=True)
            row.operator("outliner.keyingset_add_selected", icon='ZOOMIN', text="")
            row.operator("outliner.keyingset_remove_selected", icon='ZOOMOUT', text="")

            if ks:
                row = layout.row()
                row.prop_search(scene.keying_sets, "active", scene, "keying_sets", text="")

                row = layout.row(align=True)
                row.operator("anim.keyframe_insert", text="", icon='KEY_HLT')
                row.operator("anim.keyframe_delete", text="", icon='KEY_DEHLT')
            else:
                row = layout.row()
                row.label(text="No Keying Set Active")

        row = layout.row(align=True)
        row.prop(space, "use_filter_search", text="")
        if space.use_filter_search:
            row.prop(space, "filter_text", text="")
            row.prop(space, "use_filter_complete", text="")
            row.prop(space, "use_filter_case_sensitive", text="")

        if support_filters:
            row.separator()

            row.prop(space, "use_filters", text="")
            if space.use_filters:
                row.separator()
                row.prop(space, "use_filter_collection", text="")
                row.prop(space, "use_filter_object", text="")
                sub = row.row(align=True)
                sub.active = space.use_filter_object
                sub.prop(space, "use_filter_object_content", text="")
                sub.prop(space, "use_filter_children", text="")

                sub.separator()
                sub.prop(space, "use_filter_object_type", text="")

                if space.use_filter_object_type:
                    if bpy.data.meshes:
                        sub.prop(space, "use_filter_object_mesh", text="")
                    if bpy.data.armatures:
                        sub.prop(space, "use_filter_object_armature", text="")
                    if bpy.data.lamps:
                        sub.prop(space, "use_filter_object_lamp", text="")
                    if bpy.data.cameras:
                        sub.prop(space, "use_filter_object_camera", text="")

                    sub.prop(space, "use_filter_object_empty", text="")

                    if bpy.data.curves or \
                       bpy.data.metaballs or \
                       bpy.data.lightprobes or \
                       bpy.data.lattices or \
                       bpy.data.fonts or bpy.data.speakers:
                        sub.prop(space, "use_filter_object_others", text="")

                sub.separator()
                sub.prop(space, "use_filter_object_state", text="")

                if space.use_filter_object_state:
                    sub.prop(space, "filter_state", text="", expand=True)


class OUTLINER_MT_editor_menus(Menu):
    bl_idname = "OUTLINER_MT_editor_menus"
    bl_label = ""

    def draw(self, context):
        self.draw_menus(self.layout, context)

    @staticmethod
    def draw_menus(layout, context):
        space = context.space_data

        layout.menu("OUTLINER_MT_view")

        if space.display_mode == 'DATABLOCKS':
            layout.menu("OUTLINER_MT_edit_datablocks")

        elif space.display_mode == 'ORPHAN_DATA':
            layout.menu("OUTLINER_MT_edit_orphan_data")

        elif space.display_mode == 'VIEW_LAYER':
            layout.menu("OUTLINER_MT_edit_view_layer")


class OUTLINER_MT_view(Menu):
    bl_label = "View"

    def draw(self, context):
        layout = self.layout

        space = context.space_data

        if space.display_mode != 'DATABLOCKS':
            layout.prop(space, "use_sort_alpha")
            layout.prop(space, "show_restrict_columns")
            layout.separator()
            layout.operator("outliner.show_active")

        layout.operator("outliner.show_one_level", text="Show One Level")
        layout.operator("outliner.show_one_level", text="Hide One Level").open = False
        layout.operator("outliner.show_hierarchy")

        layout.separator()

        layout.operator("screen.area_dupli")
        layout.operator("screen.screen_full_area")
        layout.operator("screen.screen_full_area", text="Toggle Fullscreen Area").use_hide_panels = True


class OUTLINER_MT_edit_view_layer(Menu):
    bl_label = "Edit"

    def draw(self, context):
        layout = self.layout

        layout.operator("outliner.collection_link", icon='LINKED')
        layout.operator("outliner.collection_new", icon='NEW')


class OUTLINER_MT_edit_datablocks(Menu):
    bl_label = "Edit"

    def draw(self, context):
        layout = self.layout

        layout.operator("outliner.keyingset_add_selected")
        layout.operator("outliner.keyingset_remove_selected")

        layout.separator()

        layout.operator("outliner.drivers_add_selected")
        layout.operator("outliner.drivers_delete_selected")


class OUTLINER_MT_edit_orphan_data(Menu):
    bl_label = "Edit"

    def draw(self, context):
        layout = self.layout
        layout.operator("outliner.orphans_purge")


class OUTLINER_MT_context_scene_collection(Menu):
    bl_label = "Collection"

    def draw(self, context):
        layout = self.layout

        layout.operator("outliner.collection_nested_new", text="New Collection", icon='NEW')
        layout.operator("outliner.collection_duplicate", text="Duplicate Collection")
        layout.operator("outliner.collection_delete_selected", text="Delete Collections", icon='X')
        layout.separator()
        layout.operator("outliner.collection_objects_add", text="Add Selected", icon='ZOOMIN')
        layout.operator("outliner.collection_objects_remove", text="Remove Selected", icon='ZOOMOUT')


class OUTLINER_MT_context_object_select(Menu):
    bl_label = "Object Operation Select"

    def draw(self, context):
        layout = self.layout

        layout.operator("outliner.object_operation", text="Select").type='SELECT'
        layout.operator("outliner.object_operation", text="Deselect").type='DESELECT'
        layout.operator("outliner.object_operation", text="Select Hierarchy").type='SELECT_HIERARCHY'


class OUTLINER_MT_context_object_delete(Menu):
    bl_label = "Object Operation Delete"

    def draw(self, context):
        layout = self.layout

        layout.operator("outliner.object_operation", text="Delete").type='DELETE'
        layout.operator("outliner.object_operation", text="Delete Hierarchy").type='DELETE_HIERARCHY'


class OUTLINER_MT_context_object_collection(Menu):
    bl_label = "Object Operation Collection"

    def draw(self, context):
        layout = self.layout

        layout.operator("outliner.object_add_to_new_collection", text="Add to New Collection", icon='ZOOMIN')
        layout.operator("outliner.object_remove_from_collection", text="Remove from Collection", icon='ZOOMOUT')


class OUTLINER_MT_context_object(Menu):
    bl_label = "Object"

    def draw(self, context):
        layout = self.layout

        layout.menu("OUTLINER_MT_context_object_select", text="Select")
        layout.menu("OUTLINER_MT_context_object_delete", text="Delete")
        layout.menu("OUTLINER_MT_context_object_collection", text="Collection")
        layout.separator()
        layout.operator("outliner.object_operation", text="Remap Users").type='REMAP'
        layout.operator("outliner.object_operation", text="Rename").type='RENAME'


classes = (
    OUTLINER_HT_header,
    OUTLINER_MT_editor_menus,
    OUTLINER_MT_view,
    OUTLINER_MT_edit_view_layer,
    OUTLINER_MT_edit_datablocks,
    OUTLINER_MT_edit_orphan_data,
    OUTLINER_MT_context_scene_collection,
    OUTLINER_MT_context_object,
    OUTLINER_MT_context_object_delete,
    OUTLINER_MT_context_object_select,
    OUTLINER_MT_context_object_collection,
)

if __name__ == "__main__":  # only for live edit.
    from bpy.utils import register_class
    for cls in classes:
        register_class(cls)
