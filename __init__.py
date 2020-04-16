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

# ------------------------------- MyFaceMask --------------------------------- #
# ------------------------------- version 0.1 -------------------------------- #
#                                                                              #
#                      Alessandro Zomparelli with WASP                         #
#                                   (2020)                                     #
#                                                                              #
# ############################################################################ #

bl_info = {
    "name": "MyFaceMask",
    "author": "Alessandro Zomparelli with WASP",
    "version": (0, 2, 0),
    "blender": (2, 82, 0),
    "location": "Viewport > Right panel",
    "description": "Custom made 3D printable breathing Mask, based on 3D scanned face",
    "warning": "",
    "wiki_url": "https://www.3dwasp.com/my-face-mask-addon-blender/",
    "tracker_url": "https://github.com/alessandro-zomparelli/myfacemask/issues",
    "category": "Object"}


translation_dict = {
        'it' : {
            ('Operator', 'Adapt mask') : 'Adatta maschera',
            ('Operator', 'Remesh') : 'Ricostruisci',
            ('*', 'Change brush mode') : 'Cambia modalità pennello',
            ('*', 'Manually add ID tag') : 'Aggiungi manualmente un tag identificativo',
            ('*', 'Extract mask border based on red area') : "Estrai il contorno dell'area rossa e adatta la maschera",
            ('*', 'Invert border symmetry') : 'Inverti la simmetria del bordo',
            ('*', 'Symmetrize contact border') : 'Rendi simmetrico il bordo di contatto',
            ('*', 'Automatically remesh surface') : 'Ricostruisci automaticamente la superficie chiudendo eventuali fori',
            ('*', 'Manually edit control points') : 'Modifica manuale dei punti di controllo',
            ('*', 'You are going to do a destructive operation') : "Attenzione, stai per eseguire un'operazione distruttiva",
            ('*', 'Press ESC to undo') : 'Premi ESC per annullare',
            ('*', 'End manual editing') : 'Termina modifica manuale',
            ('*', 'End manual tag insertion') : 'Termina inserimento identificativo',
            ('*', 'Define the area on the face using the brush tool') : "Definisci l'area sul volto utilizzando il pennello",
            ('*', 'Prepare model for 3D printing') : 'Prepara il modello per la stampa',
            ('*', 'Prepare 3D print:') : 'Prepara stampa 3D:',
            ('*', 'Manually place holes') : 'Posiziona manualmente i fori',
            ('*', 'Manually align position and rotation of the filter') : 'Allinea manualmente la posiizione e la rotazione del filtro',
            ('*', 'Identification code to manually emboss on the surface') : 'Codice identificativo da inserire in rilievo sulla superficie',
            ('*', 'You are creating a new scene, all the unsaved work will be lost!') : 'Stai per creare una nuova scena, tutto il lavoro non salvato verrà perso!',
            ('*', 'Setup a new scene for MyFaceMask') : 'Imposta una nuova scena per MyFaceMask',
            ('Operator', 'Prepare model') : 'Prepara modello',
            ('Operator', 'Invert symmetry') : 'Inverti simmetria',
            ('Operator', 'Define area') : 'Definisci area',
            ('Operator', 'Symmetric border on') : 'Attiva simmetria',
            ('Operator', 'Symmetric border off') : 'Disattiva simmetria',
            ('Operator', 'Align filter') : 'Allinea filtro',
            ('Operator', 'Manual editing') : 'Modifica manuale',
            ('Operator', 'Setup scene') : 'Imposta scena',
            ('Operator', 'Done') : 'Fatto',
            ('Operator', 'End editing') : 'Termina modifica',
            ('*', 'Nose pressure') : 'Pressione naso',
            ('*', 'Import scan:') : 'Importa scansione:',
            ('*', 'Adapt mask:') : 'Adatta maschera:',
            ('*', 'Adjust:') : 'Rifinisci:',
            ('*', 'Identity:') : 'Identità:',
            ('*', 'Export:') : 'Esporta:',
            ('Operator', 'Insert tag') : 'Inserisci tag',
            ('Operator', 'Show holes') : 'Visualizza fori',
            ('Operator', 'Align filter on') : 'Attiva allinea filtro',
            ('Operator', 'Align filter off') : 'Disattiva allinea filtro',
            ('Operator', 'Hide holes') : 'Nascondi fori',
            ('Operator', 'Prepare model') : 'Prepara modello',
            ('Operator', 'Place holes') : 'Posiziona fori'
        },
        'es' : {
            ('Operator', 'Adapt mask') : 'Adaptar máscara',
            ('Operator', 'Remesh') : 'Rehacer malla',
            ('*', 'Change brush mode') : 'Cambiar pincel',
            ('*', 'Manually add ID tag') : 'Añadir manualmente un código de identificación ',
            ('*', 'Extract mask border based on red area') : "Extraer el contorno del área roja y adaptar la màscara",
            ('*', 'Invert border symmetry') : 'Invertir la simetría del borde',
            ('*', 'Symmetrize contact border') : 'Hacer que el borde de contacto sea simétrico',
            ('*', 'Automatically remesh surface') : 'Reconstruir automáticamente la superficie cerrando cualquier hoyo',
            ('*', 'Manually edit control points') : 'Modificar manualmente puntos de control',
            ('*', 'You are going to do a destructive operation') : "Atención, estas haciendo una operación destructiva",
            ('*', 'Press ESC to undo') : 'Presiona la tecla ESCAPE para deshacer',
            ('*', 'End manual editing') : 'Terminar modificación manual',
            ('*', 'End manual tag insertion') : 'Terminar inserción de identificación manual',
            ('*', 'Define the area on the face using the brush tool') : "Definir el área del rostro mediante el pincel",
            ('*', 'Prepare model for 3D printing') : 'Preparar modelo para impresión 3D',
            ('*', 'Prepare 3D print:') : 'Preparar impresión 3D:',
            ('*', 'Manually place holes') : 'Colocar manualmente los hoyos',
            ('*', 'Manually align position and rotation of the filter') : 'Alinear manualmente la posición y la rotación del filtro',
            ('*', 'Identification code to manually emboss on the surface') : 'Añadir código de identificación en relieve en el área',
            ('*', 'You are creating a new scene, all the unsaved work will be lost!') : '¡Estas creando una nueva escena, todo el trabajo que no está guardado sera perdido!',
            ('*', 'Setup a new scene for MyFaceMask') : 'Configurar una nueva escena para MyFaceMask',
            ('Operator', 'Prepare model') : 'Preparar modelo',
            ('Operator', 'Invert symmetry') : 'Invertir simetría',
            ('Operator', 'Define area') : 'Definir el área',
            ('Operator', 'Symmetric border on') : 'Activar simetría',
            ('Operator', 'Symmetric border off') : 'Desactivar simetría',
            ('Operator', 'Align filter') : 'Alinear filtro',
            ('Operator', 'Manual editing') : 'Editar manualmente',
            ('Operator', 'Setup scene') : 'Configurar escena',
            ('Operator', 'Done') : 'Hecho',
            ('Operator', 'End editing') : 'Terminar la modificación',
            ('*', 'Nose pressure') : 'Presión nariz',
            ('*', 'Import scan:') : 'Importar escaneo:',
            ('*', 'Adapt mask:') : 'Adaptar máscara:',
            ('*', 'Adjust:') : 'Refinar:',
            ('*', 'Identity:') : 'Identidad:',
            ('*', 'Export:') : 'Exportar:',
            ('Operator', 'Insert tag') : 'Añadir etiqueta',
            ('Operator', 'Show holes') : 'Mostrar hoyos',
            ('Operator', 'Align filter on') : 'Activar alineación filtro',
            ('Operator', 'Align filter off') : 'Desactivar alineación filtro',
            ('Operator', 'Hide holes') : 'Ocultar hoyos',
            ('Operator', 'Prepare model') : 'Preparar modelo',
            ('Operator', 'Place holes') : 'Colocar hoyos'
        }
    }


if "bpy" in locals():
    import importlib
    importlib.reload(myfacemask_tools)
    importlib.reload(utils)

else:
    from . import myfacemask_tools
    from . import utils

import bpy
from bpy.props import PointerProperty, CollectionProperty, BoolProperty, EnumProperty
from bpy.app.handlers import persistent

classes = (
    myfacemask_tools.myfacemask_props,
    myfacemask_tools.myfacemask_remesh,
    myfacemask_tools.myfacemask_adapt_mask,
    myfacemask_tools.myfacemask_weight_toggle,
    myfacemask_tools.myfacemask_weight_add_subtract,
    myfacemask_tools.myfacemask_mirror_border,
    myfacemask_tools.myfacemask_mirror_border_flip,
    myfacemask_tools.myfacemask_boolean,
    myfacemask_tools.myfacemask_holes_snap,
    myfacemask_tools.myfacemask_edit_mask,
    myfacemask_tools.myfacemask_place_filter,
    myfacemask_tools.myfacemask_edit_mask_off,
    myfacemask_tools.myfacemask_tag_mask_off,
    myfacemask_tools.myfacemask_generate_tag,
    myfacemask_tools.myfacemask_setup,
    myfacemask_tools.MYFACEMASK_PT_weight
)

def update_thickness(self, context):
    myfacemask_tools.update_assets()
    t = context.scene.myfacemask_thickness
    #try:
        #coll = bpy.data.collections['Filters'].objects
        #for o in coll:
        #    if 'Filter_' in o.name and 'Displace' in o.modifiers.keys():
        #        o.modifiers['Displace'].strength = max((t-1.6)*1.6,0)
    #except: pass
    try:
        coll = bpy.data.collections['Filters'].objects
        for o in coll:
            if 'Surface_' in o.name:
                o.modifiers['Thickness'].thickness = t
    except: pass
    return

@persistent
def load_handler(dummy):
    myfacemask_tools.update_assets()

def register():
    from bpy.utils import register_class
    for cls in classes:
        bpy.utils.register_class(cls)
    #myfacemask_tools.update_assets()

    bpy.types.Scene.myfacemask_hangs = ""#EnumProperty()
    bpy.types.Scene.myfacemask_border = ""#EnumProperty()
    bpy.types.Scene.myfacemask_model = ""#EnumProperty()
    #bpy.types.Scene.myfacemask = EnumProperty(type = myfacemask_tools.myfacemask_props)

    bpy.types.Scene.myfacemask_filter = bpy.props.StringProperty()
    bpy.types.Scene.myfacemask_surface = bpy.props.StringProperty()

    #myfacemask_tools.update_assets()
    bpy.app.handlers.load_post.append(load_handler)

    bpy.types.Scene.myfacemask_id = bpy.props.StringProperty(
        name='ID',
        description='Identification code to manually emboss on the surface',
        default = 'WASP')
    bpy.types.Scene.myfacemask_thickness = bpy.props.FloatProperty(
        name='Thickness',
        description='Mask thickness',
        min=0.1,
        max=5,
        default=1.6,
        update=update_thickness
        )
    bpy.app.translations.register(__name__, translation_dict)

def unregister():
    from bpy.utils import unregister_class
    for cls in classes:
        bpy.utils.unregister_class(cls)
    bpy.app.translations.unregister(__name__)

if __name__ == "__main__":
    register()
