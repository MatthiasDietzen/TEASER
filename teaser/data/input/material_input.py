#Created April 2016
#TEASER 4 Development Team

"""material_input.py

This module contains function to load material classes
"""


def load_material(material, mat_name, data_class):
    '''Material loader.

    Loads Material specified in the XML.

    Parameters
    ----------

    material : Material()
        instance of TEASERS Material class

    mat_name : str
        Code list for Material

    data_class : DataClass()
        DataClass containing the bindings for TypeBuildingElement and
        Material (typically this is the data class stored in prj.data,
        but the user can individually change that.
    '''

    binding = data_class.material_bind

    for mat in binding.Material:

        if mat.name == mat_name:

            material.material_id = mat.material_id
            material.name = mat.name
            material.density = mat.density
            material.thermal_conduc = float(mat.thermal_conduc)
            material.heat_capac = mat.heat_capac
            material.PE_non_regenerable = mat.PE_non_regenerable
            material.PE_regenerable = mat.PE_regenerable
            material.secondary_fuels = mat.secondary_fuels
            material.water_use = mat.water_use
            material.ore_dressing_residues = mat.ore_dressing_residues
            material.industrial_waste = mat.industrial_waste
            material.hazardous_wastes = mat.hazardous_wastes
            material.ADP = mat.ADP
            material.EP = mat.EP
            material.ODP = mat.ODP
            material.POCP = mat.POCP
            material.GWP_100 = mat.GWP_100
            material.AP = mat.AP
            material.costs = mat.costs


def load_material_id(material, mat_id, data_class):
    """Material loader by id.

    Loads Material specified in the XML by given material_id.

    Parameters
    ----------

    material : Material()
        instance of TEASERS Material class

    mat_id : name
        id of material from XML

    data_class : DataClass()
        DataClass containing the bindings for TypeBuildingElement and
        Material (typically this is the data class stored in prj.data,
        but the user can individually change that.
    """

    binding = data_class.material_bind

    for mat in binding.Material:

        if mat.material_id == mat_id:

            material.material_id = mat.material_id
            material.name = mat.name
            material.density = mat.density
            material.thermal_conduc = float(mat.thermal_conduc)
            material.heat_capac = mat.heat_capac
            material.PE_non_regenerable = mat.PE_non_regenerable
            material.PE_non_regenerable = mat.PE_non_regenerable
            material.PE_regenerable = mat.PE_regenerable
            material.secondary_fuels = mat.secondary_fuels
            material.water_use = mat.water_use
            material.ore_dressing_residues = mat.ore_dressing_residues
            material.industrial_waste = mat.industrial_waste
            material.hazardous_wastes = mat.hazardous_wastes
            material.ADP = mat.ADP
            material.EP = mat.EP
            material.ODP = mat.ODP
            material.POCP = mat.POCP
            material.GWP_100 = mat.GWP_100
            material.AP = mat.AP
            material.costs = mat.costs

