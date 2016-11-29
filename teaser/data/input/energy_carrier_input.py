#Created November 2016
#TEASER 4 Development Team

"""energy_carrier_input.py

This module contains function to load energy_carrier classes
"""


def load_energy_carrier(energy_carrier, enc_name, data_class):
    '''EnergyCarrier loader.

    Loads EnergyCarrier specified in the XML.

    Parameters
    ----------

    energy_carrier : EnergyCarrier()
        instance of TEASERS EnergyCarrier class

    enc_name : str
        Code list for EnergyCarrier

    data_class : DataClass()
        DataClass containing the bindings for TypeBuildingElement and
        EnergyCarrier (typically this is the data class stored in prj.data,
        but the user can individually change that.
    '''

    binding = data_class.energy_carrier_bind

    for enc in binding.EnergyCarrier:

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
            energy_carrier.costs = enc.costs


def load_energy_carrier_id(energy_carrier, enc_id, data_class):
    """EnergyCarrier loader by id.

    Loads EnergyCarrier specified in the XML by given energy_carrier_id.

    Parameters
    ----------

    energy_carrier : EnergyCarrier()
        instance of TEASERS EnergyCarrier class

    enc_id : name
        id of energy_carrier from XML

    data_class : DataClass()
        DataClass containing the bindings for TypeBuildingElement and
        EnergyCarrier (typically this is the data class stored in prj.data,
        but the user can individually change that.
    """

    binding = data_class.energy_carrier_bind

    for enc in binding.EnergyCarrier:

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
            energy_carrier.costs = enc.costs

