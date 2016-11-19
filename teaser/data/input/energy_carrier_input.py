#Created November 2016
#TEASER 4 Development Team

"""energy_carrier_input.py

This module contains function to load energy_carrier classes
"""


def load_energy_carrier(energy_carrier, enc_name, data_class):
    '''energy_carrier loader.

    Loads energy_carrier specified in the XML.

    Parameters
    ----------

    energy_carrier : energy_carrier()
        instance of TEASERS energy_carrier class

    enc_name : str
        Code list for energy_carrier

    data_class : DataClass()
        DataClass containing the bindings for TypeBuildingElement and
        energy_carrier (typically this is the data class stored in prj.data,
        but the user can individually change that.
    '''

    binding = data_class.energy_carrier_bind

    for enc in binding.energy_carrier:

        if enc.name == enc_name:

            energy_carrier.energy_carrier_id = enc.energy_carrier_id
            energy_carrier.name = enc.name
            energy_carrier.density = enc.density
            energy_carrier.PE_non_regenerable = enc.PE_non_regenerable
            energy_carrier.PE_regenerable = enc.PE_regenerable
            energy_carrier.secondary_fuels = enc.secondary_fuels
            energy_carrier.water_use = enc.water_use
            energy_carrier.ore_dressing_residues = enc.ore_dressing_residues
            energy_carrier.industrial_waste = enc.industrial_waste
            energy_carrier.hazardous_wastes = enc.hazardous_wastes
            energy_carrier.ADP = enc.ADP
            energy_carrier.EP = enc.EP
            energy_carrier.ODP = enc.ODP
            energy_carrier.POCP = enc.POCP
            energy_carrier.GWP_100 = enc.GWP_100
            energy_carrier.AP = enc.AP
            energy_carrier.cost = enc.cost


def load_energy_carrier_id(energy_carrier, enc_id, data_class):
    """energy_carrier loader by id.

    Loads energy_carrier specified in the XML by given energy_carrier_id.

    Parameters
    ----------

    energy_carrier : energy_carrier()
        instance of TEASERS energy_carrier class

    enc_id : name
        id of energy_carrier from XML

    data_class : DataClass()
        DataClass containing the bindings for TypeBuildingElement and
        energy_carrier (typically this is the data class stored in prj.data,
        but the user can individually change that.
    """

    binding = data_class.energy_carrier_bind

    for enc in binding.energy_carrier:

        if enc.energy_carrier_id == enc_id:

            energy_carrier.energy_carrier_id = enc.energy_carrier_id
            energy_carrier.name = enc.name
            energy_carrier.density = enc.density
            energy_carrier.PE_non_regenerable = enc.PE_non_regenerable
            energy_carrier.PE_non_regenerable = enc.PE_non_regenerable
            energy_carrier.PE_regenerable = enc.PE_regenerable
            energy_carrier.secondary_fuels = enc.secondary_fuels
            energy_carrier.water_use = enc.water_use
            energy_carrier.ore_dressing_residues = enc.ore_dressing_residues
            energy_carrier.industrial_waste = enc.industrial_waste
            energy_carrier.hazardous_wastes = enc.hazardous_wastes
            energy_carrier.ADP = enc.ADP
            energy_carrier.EP = enc.EP
            energy_carrier.ODP = enc.ODP
            energy_carrier.POCP = enc.POCP
            energy_carrier.GWP_100 = enc.GWP_100
            energy_carrier.AP = enc.AP
            energy_carrier.cost = enc.cost

