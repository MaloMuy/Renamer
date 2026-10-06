#import libraries
import bpy
import fnmatch


def get_selection():
    return list(bpy.context.view_layer.objects.selected)


def select_all_objects():
    """
    Select all objects in the scene.
    """

    bpy.ops.object.select_all(action="SELECT")


def search_object(name: str):
    """
    Search object in the scene and select them.

    Args:
        name (str): name of the object you search
    """

    view_layer = bpy.context.view_layer

    # Clear the selection
    for obj in view_layer.objects:
        obj.select_set(False)

    # Select matches
    for obj in view_layer.objects:
        if fnmatch.fnmatch(obj.name.lower(), name.lower()):
            obj.select_set(True)


def renamer(new_name: str):
    """
    Rename selected objects.

    Args:
        new_name (str): The new name you have choosen.
    """

    selection = get_selection()

    for obj in selection:
        obj.name = new_name


def rename_number(new_name: str, start_value: int, padding: int):
    """
    Rename and padding selected objecs.

    Args:
        new_name (str): The new name you chose
        start_value (str): The start value of your padding
        padding (str): The dimension of your padding
    """

    selection = get_selection()

    # Rename objects
    for obj in selection:
        obj.name = f"{new_name}_{str(start_value).zfill(padding)}"


def name_suffix(suffix: str):
    """
    Add a suffix.

    Args:
        suffix (str): The suffix you chose.
    """

    selection = get_selection()

    for obj in selection:
        obj.name = f"{obj.name}_{suffix}"


def name_suffix_msh():
    """
    Adding MSH as a suffix
    """

    selection = get_selection()
    
    for obj in selection:
        obj.name = f"{obj.name}_MSH"


def name_suffix_grp():
    """
    Adding GRP as a suffix
    """
    
    selection = get_selection()
    
    for obj in selection:
        obj.name = f"{obj.name}_GRP"


def name_suffix_jnt():
    """
    Adding JNT as a suffix
    """
    
    selection = get_selection()
    
    for obj in selection:
        obj.name = f"{obj.name}_JNT"


def name_suffix_con():
    """
    Adding CON as a suffix
    """
    
    selection = get_selection()
    
    for obj in selection:
        obj.name = f"{obj.name}_CON"


def name_prefix(prefix: str):
    """
    Add a prefix.

    Args:
        prefix (str): The prefix you chose.
    """

    selection = get_selection()

    for obj in selection:
        obj.name = f"{prefix}_{obj.name}"


def remove_character(first: int, end: int):
    """
    Remove characters at the beginning and end of the name object.

    Args:
        first (int): Number of character you want to remove at the beginning.
        end (int): Number of character you want to remove at the end.
    """

    selection = get_selection()

    for obj in selection: 
        
        if int(end) > 0:
            name = obj.name[:-int(end)]
        else:
            name = obj.name
        
        name = name[int(first):]

        try:
            obj.name = name
        except:
            pass


def search_replace(search: str, replace: str, type: str):
    """
    Search a string and replace by other thing in the name of the object.

    Args:
        search (str): search string you want to find
        replace (str): replace by a string you want to replace
        type (str): Select the type of selection you have selected
    """
    
    if type == 1:
        selection = list(bpy.context.scene.objects)

    if type == 2:
        selection = get_selection()
    
    if type == 3:
        selection = list(bpy.context.scene.objects)
    
    for obj in selection:
        try:
            obj.name = obj.name.replace(search,replace)
        except:
            pass
