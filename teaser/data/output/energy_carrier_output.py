#Created November 2016
#TEASER 4 Development Team

"""energy_carrier_output.py

This module contains function to save energy_carrier classes
"""
import teaser.data.bindings.v_0_4.energy_carrier_bind as enc_bind
import teaser.logic.utilities as utilitis
import warnings
import pyxb

def save_energy_carrier(energy_carrier, data_class):
    """EnergyCarrier saver.

    Saves EnergyCarrier specified in the XML.

    Parameters
    ----------
    energy_carrier : EnergyCarrier()
        instance of TEASERS EnergyCarrier class

    data_class : DataClass()
        DataClass containing the bindings for TypeBuildingElement and
        EnergyCarrier (typically this is the data class stored in prj.data,
        but the user can individually change that.

    """
    enc_binding = data_class.energy_carrier_bind
    add_to_xml = True
    enc_binding.version = "0.4"
    warning_text = ("EnergyCarrier with same name and same properties already "
                    "exists in XML, consider this energy_carrier or revising your "
                    "properties")

    pyxb.utils.domutils.BindingDOMSupport.DeclareNamespace(
        enc_bind.Namespace, 'energy_carriers')

    for check in enc_binding.EnergyCarrier:
        if check.name == energy_carrier.name and \
                check.density == energy_carrier.density:
            warnings.warn(warning_text)
            add_to_xml = False
            break

    if add_to_xml is True:
        enc_pyxb = enc_bind.EnergyCarrierType()

        enc_pyxb.energy_carrier_id = energy_carrier.energy_carrier_id
        enc_pyxb.name = energy_carrier.name
        enc_pyxb.density = energy_carrier.density
        enc_pyxb.PE_non_regenerable = energy_carrier.PE_non_regenerable
        enc_pyxb.PE_regenerable = energy_carrier.PE_regenerable
        enc_pyxb.secondary_fuels = energy_carrier.secondary_fuels
        enc_pyxb.water_use = energy_carrier.water_use
        enc_pyxb.ore_dressing_residues = energy_carrier.ore_dressing_residues
        enc_pyxb.industrial_waste = energy_carrier.industrial_waste
        enc_pyxb.hazardous_wastes = energy_carrier.hazardous_wastes
        enc_pyxb.ADP = energy_carrier.ADP
        enc_pyxb.EP = energy_carrier.EP
        enc_pyxb.ODP = energy_carrier.ODP
        enc_pyxb.POCP = energy_carrier.POCP 
        enc_pyxb.GWP_100 = energy_carrier.GWP_100
        enc_pyxb.AP = energy_carrier.AP
        enc_pyxb.costs = energy_carrier.costs

        enc_binding.EnergyCarrier.append(enc_pyxb)
        out_file = open(utilitis.get_full_path(data_class.path_enc), "w")

        out_file.write(enc_binding.toDOM().toprettyxml())
