from maya import cmds


def select_all_objects():
    """
    Select all objects in the scene.
    """

    cmds.select(all=True)


def search_object(name: str):
    """
    Search object in the scene and select them.

    Args:
        name (str): name of the object you search
    """
    print(name)

    # Clear the selection
    cmds.select(clear=True)

    selection = cmds.ls(name)
    
    for obj in selection: 
        cmds.select(obj, add=True)


def renamer(new_name: str):
    """
    Rename selected objects.

    Args:
        new_name (str): The new name you have choosen.
    """

    renamer = cmds.ls(selection=True)

    for obj in renamer:
        cmds.rename(obj, new_name)


def rename_number(new_name: str, start_value: int, padding: int):
    """
    Rename and padding selected objecs.

    Args:
        new_name (str): The new name you chose
        start_value (str): The start value of your padding
        padding (str): The dimension of your padding
    """
    
    selection = cmds.ls(selection=True)

    # Create the dimension of padding
    zeros = ""
    for i in range(padding-1):
        zeros = zeros + "0"

    # Rename objects
    for obj in selection:                
        cmds.rename(obj, f"{new_name}_{zeros}{start_value}")
    


def name_suffix(suffix: str):
    """
    Add a suffix.

    Args:
        suffix (str): The suffix you chose.
    """

    selection = cmds.ls(selection=True)

    for obj in selection:
        shortName = obj.split("|")[-1]
        cmds.rename(obj, f"{shortName}_{suffix}")


def name_suffix_msh():
    """
    Adding MSH as a suffix
    """

    selection = cmds.ls(selection=True)
    
    for obj in selection:
        cmds.rename(obj, f"{obj}_MSH")


def name_suffix_grp():
    """
    Adding GRP as a suffix
    """
    
    selection = cmds.ls(selection=True)
    
    for obj in selection:
        cmds.rename(obj, f"{obj}_GRP")


def name_suffix_jnt():
    """
    Adding JNT as a suffix
    """
    
    selection = cmds.ls(selection=True)
    
    for obj in selection:
        cmds.rename(obj, f"{obj}_JNT")


def name_suffix_con():
    """
    Adding CON as a suffix
    """
    
    selection = cmds.ls(selection=True)
    
    for obj in selection:
        cmds.rename(obj, f"{obj}_CON")


def name_prefix(prefix: str):
    """
    Add a prefix.

    Args:
        prefix (str): The prefix you chose.
    """

    selection = cmds.ls(selection=True)

    for obj in selection:
        shortName = obj.split("|")[-1]
        cmds.rename(obj, f"{prefix}_{shortName}")


def remove_character(first: int, end: int):
    """
    Remove characters at the beginning and end of the name object.

    Args:
        first (int): Number of character you want to remove at the beginning.
        end (int): Number of character you want to remove at the end.
    """

    selection = cmds.ls(selection=True)

    for obj in selection: 

        # remove character at the end
        if int(end) > 0:
            name = obj[:-int(end)]
        else:
            name = obj

        # remove character at the beginning of the name
        name = name[int(first):]

        try:
            cmds.rename(obj, name)
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
        cmds.select(ado=True, hi=True)
        selection=cmds.ls(selection=True, sn=True)

    if type == 2:
        selection=cmds.ls(selection=True, sn=True)
    
    if type == 3:
        cmds.select(hierarchy=True)
        selection = cmds.ls(selection=True)

    for obj in selection:
        
        new_name = obj.replace(search,replace)

        try:
            cmds.rename(obj, new_name)
        except:
            pass

