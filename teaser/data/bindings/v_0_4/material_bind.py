# .\material_bind.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:e92452c8d3e28a9e27abfc9994d2007779e7f4c9
# Generated 2016-10-19 23:27:48.662400 by PyXB version 1.2.4 using Python 3.5.2.final.0
# Namespace AbsentNamespace0

from __future__ import unicode_literals
import pyxb
import pyxb.binding
import pyxb.binding.saxer
import io
import pyxb.utils.utility
import pyxb.utils.domutils
import sys
import pyxb.utils.six as _six

# Unique identifier for bindings created at the same time
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:e20e432e-9642-11e6-a9c7-54ee7579a8e4')

# Version of PyXB used to generate the bindings
_PyXBVersion = '1.2.4'
# Generated bindings are not compatible across PyXB versions
if pyxb.__version__ != _PyXBVersion:
    raise pyxb.PyXBVersionError(_PyXBVersion)

# Import bindings for namespaces imported into schema
import pyxb.binding.datatypes

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.CreateAbsentNamespace()
Namespace.configureCategories(['typeBinding', 'elementBinding'])

def CreateFromDocument (xml_text, default_namespace=None, location_base=None):
    """Parse the given XML and use the document element to create a
    Python instance.

    @param xml_text An XML document.  This should be data (Python 2
    str or Python 3 bytes), or a text (Python 2 unicode or Python 3
    str) in the L{pyxb._InputEncoding} encoding.

    @keyword default_namespace The L{pyxb.Namespace} instance to use as the
    default namespace where there is no default namespace in scope.
    If unspecified or C{None}, the namespace of the module containing
    this function will be used.

    @keyword location_base: An object to be recorded as the base of all
    L{pyxb.utils.utility.Location} instances associated with events and
    objects handled by the parser.  You might pass the URI from which
    the document was obtained.
    """

    if pyxb.XMLStyle_saxer != pyxb._XMLStyle:
        dom = pyxb.utils.domutils.StringToDOM(xml_text)
        return CreateFromDOM(dom.documentElement, default_namespace=default_namespace)
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    saxer = pyxb.binding.saxer.make_parser(fallback_namespace=default_namespace, location_base=location_base)
    handler = saxer.getContentHandler()
    xmld = xml_text
    if isinstance(xmld, _six.text_type):
        xmld = xmld.encode(pyxb._InputEncoding)
    saxer.parse(io.BytesIO(xmld))
    instance = handler.rootObject()
    return instance

def CreateFromDOM (node, default_namespace=None):
    """Create a Python instance from the given DOM node.
    The node tag must correspond to an element declaration in this module.

    @deprecated: Forcing use of DOM interface is unnecessary; use L{CreateFromDocument}."""
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    return pyxb.binding.basis.element.AnyCreateFromDOM(node, default_namespace)


# Complex type MaterialType with content type ELEMENT_ONLY
class MaterialType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type MaterialType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'MaterialType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\Dude\\Documents\\UNI\\Masterarbeit\\pyxb-PyXB-1.2.4\\scripts\\MaterialTemplates.xsd', 4, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element name uses Python identifier name
    __name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__AbsentNamespace0_MaterialType_name', False, pyxb.utils.utility.Location('C:\\Users\\Dude\\Documents\\UNI\\Masterarbeit\\pyxb-PyXB-1.2.4\\scripts\\MaterialTemplates.xsd', 7, 6), )

    
    name = property(__name.value, __name.set, None, None)

    
    # Element density uses Python identifier density
    __density = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'density'), 'density', '__AbsentNamespace0_MaterialType_density', False, pyxb.utils.utility.Location('C:\\Users\\Dude\\Documents\\UNI\\Masterarbeit\\pyxb-PyXB-1.2.4\\scripts\\MaterialTemplates.xsd', 8, 6), )

    
    density = property(__density.value, __density.set, None, None)

    
    # Element thermal_conduc uses Python identifier thermal_conduc
    __thermal_conduc = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'thermal_conduc'), 'thermal_conduc', '__AbsentNamespace0_MaterialType_thermal_conduc', False, pyxb.utils.utility.Location('C:\\Users\\Dude\\Documents\\UNI\\Masterarbeit\\pyxb-PyXB-1.2.4\\scripts\\MaterialTemplates.xsd', 9, 6), )

    
    thermal_conduc = property(__thermal_conduc.value, __thermal_conduc.set, None, None)

    
    # Element heat_capac uses Python identifier heat_capac
    __heat_capac = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'heat_capac'), 'heat_capac', '__AbsentNamespace0_MaterialType_heat_capac', False, pyxb.utils.utility.Location('C:\\Users\\Dude\\Documents\\UNI\\Masterarbeit\\pyxb-PyXB-1.2.4\\scripts\\MaterialTemplates.xsd', 10, 6), )

    
    heat_capac = property(__heat_capac.value, __heat_capac.set, None, None)

    
    # Element solar_absorp uses Python identifier solar_absorp
    __solar_absorp = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'solar_absorp'), 'solar_absorp', '__AbsentNamespace0_MaterialType_solar_absorp', False, pyxb.utils.utility.Location('C:\\Users\\Dude\\Documents\\UNI\\Masterarbeit\\pyxb-PyXB-1.2.4\\scripts\\MaterialTemplates.xsd', 11, 6), )

    
    solar_absorp = property(__solar_absorp.value, __solar_absorp.set, None, None)

    
    # Element ir_emissivity uses Python identifier ir_emissivity
    __ir_emissivity = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'ir_emissivity'), 'ir_emissivity', '__AbsentNamespace0_MaterialType_ir_emissivity', False, pyxb.utils.utility.Location('C:\\Users\\Dude\\Documents\\UNI\\Masterarbeit\\pyxb-PyXB-1.2.4\\scripts\\MaterialTemplates.xsd', 12, 6), )

    
    ir_emissivity = property(__ir_emissivity.value, __ir_emissivity.set, None, None)

    
    # Element PE_non_regenerable uses Python identifier PE_non_regenerable
    __PE_non_regenerable = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'PE_non_regenerable'), 'PE_non_regenerable', '__AbsentNamespace0_MaterialType_PE_non_regenerable', False, pyxb.utils.utility.Location('C:\\Users\\Dude\\Documents\\UNI\\Masterarbeit\\pyxb-PyXB-1.2.4\\scripts\\MaterialTemplates.xsd', 13, 6), )

    
    PE_non_regenerable = property(__PE_non_regenerable.value, __PE_non_regenerable.set, None, None)

    
    # Element PE_regenerable uses Python identifier PE_regenerable
    __PE_regenerable = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'PE_regenerable'), 'PE_regenerable', '__AbsentNamespace0_MaterialType_PE_regenerable', False, pyxb.utils.utility.Location('C:\\Users\\Dude\\Documents\\UNI\\Masterarbeit\\pyxb-PyXB-1.2.4\\scripts\\MaterialTemplates.xsd', 14, 6), )

    
    PE_regenerable = property(__PE_regenerable.value, __PE_regenerable.set, None, None)

    
    # Element secondary_fuels uses Python identifier secondary_fuels
    __secondary_fuels = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'secondary_fuels'), 'secondary_fuels', '__AbsentNamespace0_MaterialType_secondary_fuels', False, pyxb.utils.utility.Location('C:\\Users\\Dude\\Documents\\UNI\\Masterarbeit\\pyxb-PyXB-1.2.4\\scripts\\MaterialTemplates.xsd', 15, 6), )

    
    secondary_fuels = property(__secondary_fuels.value, __secondary_fuels.set, None, None)

    
    # Element water_use uses Python identifier water_use
    __water_use = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'water_use'), 'water_use', '__AbsentNamespace0_MaterialType_water_use', False, pyxb.utils.utility.Location('C:\\Users\\Dude\\Documents\\UNI\\Masterarbeit\\pyxb-PyXB-1.2.4\\scripts\\MaterialTemplates.xsd', 16, 6), )

    
    water_use = property(__water_use.value, __water_use.set, None, None)

    
    # Element ore_dressing_residues uses Python identifier ore_dressing_residues
    __ore_dressing_residues = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'ore_dressing_residues'), 'ore_dressing_residues', '__AbsentNamespace0_MaterialType_ore_dressing_residues', False, pyxb.utils.utility.Location('C:\\Users\\Dude\\Documents\\UNI\\Masterarbeit\\pyxb-PyXB-1.2.4\\scripts\\MaterialTemplates.xsd', 17, 6), )

    
    ore_dressing_residues = property(__ore_dressing_residues.value, __ore_dressing_residues.set, None, None)

    
    # Element industrial_waste uses Python identifier industrial_waste
    __industrial_waste = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'industrial_waste'), 'industrial_waste', '__AbsentNamespace0_MaterialType_industrial_waste', False, pyxb.utils.utility.Location('C:\\Users\\Dude\\Documents\\UNI\\Masterarbeit\\pyxb-PyXB-1.2.4\\scripts\\MaterialTemplates.xsd', 18, 6), )

    
    industrial_waste = property(__industrial_waste.value, __industrial_waste.set, None, None)

    
    # Element hazardous_wastes uses Python identifier hazardous_wastes
    __hazardous_wastes = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'hazardous_wastes'), 'hazardous_wastes', '__AbsentNamespace0_MaterialType_hazardous_wastes', False, pyxb.utils.utility.Location('C:\\Users\\Dude\\Documents\\UNI\\Masterarbeit\\pyxb-PyXB-1.2.4\\scripts\\MaterialTemplates.xsd', 19, 6), )

    
    hazardous_wastes = property(__hazardous_wastes.value, __hazardous_wastes.set, None, None)

    
    # Element ADP uses Python identifier ADP
    __ADP = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'ADP'), 'ADP', '__AbsentNamespace0_MaterialType_ADP', False, pyxb.utils.utility.Location('C:\\Users\\Dude\\Documents\\UNI\\Masterarbeit\\pyxb-PyXB-1.2.4\\scripts\\MaterialTemplates.xsd', 20, 6), )

    
    ADP = property(__ADP.value, __ADP.set, None, None)

    
    # Element EP uses Python identifier EP
    __EP = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'EP'), 'EP', '__AbsentNamespace0_MaterialType_EP', False, pyxb.utils.utility.Location('C:\\Users\\Dude\\Documents\\UNI\\Masterarbeit\\pyxb-PyXB-1.2.4\\scripts\\MaterialTemplates.xsd', 21, 6), )

    
    EP = property(__EP.value, __EP.set, None, None)

    
    # Element ODP uses Python identifier ODP
    __ODP = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'ODP'), 'ODP', '__AbsentNamespace0_MaterialType_ODP', False, pyxb.utils.utility.Location('C:\\Users\\Dude\\Documents\\UNI\\Masterarbeit\\pyxb-PyXB-1.2.4\\scripts\\MaterialTemplates.xsd', 22, 6), )

    
    ODP = property(__ODP.value, __ODP.set, None, None)

    
    # Element POCP uses Python identifier POCP
    __POCP = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'POCP'), 'POCP', '__AbsentNamespace0_MaterialType_POCP', False, pyxb.utils.utility.Location('C:\\Users\\Dude\\Documents\\UNI\\Masterarbeit\\pyxb-PyXB-1.2.4\\scripts\\MaterialTemplates.xsd', 23, 6), )

    
    POCP = property(__POCP.value, __POCP.set, None, None)

    
    # Element GWP_100 uses Python identifier GWP_100
    __GWP_100 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'GWP_100'), 'GWP_100', '__AbsentNamespace0_MaterialType_GWP_100', False, pyxb.utils.utility.Location('C:\\Users\\Dude\\Documents\\UNI\\Masterarbeit\\pyxb-PyXB-1.2.4\\scripts\\MaterialTemplates.xsd', 24, 6), )

    
    GWP_100 = property(__GWP_100.value, __GWP_100.set, None, None)

    
    # Element AP uses Python identifier AP
    __AP = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'AP'), 'AP', '__AbsentNamespace0_MaterialType_AP', False, pyxb.utils.utility.Location('C:\\Users\\Dude\\Documents\\UNI\\Masterarbeit\\pyxb-PyXB-1.2.4\\scripts\\MaterialTemplates.xsd', 25, 6), )

    
    AP = property(__AP.value, __AP.set, None, None)

    
    # Element cost uses Python identifier cost
    __cost = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'cost'), 'cost', '__AbsentNamespace0_MaterialType_cost', False, pyxb.utils.utility.Location('C:\\Users\\Dude\\Documents\\UNI\\Masterarbeit\\pyxb-PyXB-1.2.4\\scripts\\MaterialTemplates.xsd', 26, 6), )

    
    cost = property(__cost.value, __cost.set, None, None)

    
    # Attribute material_id uses Python identifier material_id
    __material_id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'material_id'), 'material_id', '__AbsentNamespace0_MaterialType_material_id', pyxb.binding.datatypes.string)
    __material_id._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\Dude\\Documents\\UNI\\Masterarbeit\\pyxb-PyXB-1.2.4\\scripts\\MaterialTemplates.xsd', 5, 4)
    __material_id._UseLocation = pyxb.utils.utility.Location('C:\\Users\\Dude\\Documents\\UNI\\Masterarbeit\\pyxb-PyXB-1.2.4\\scripts\\MaterialTemplates.xsd', 5, 4)
    
    material_id = property(__material_id.value, __material_id.set, None, None)

    _ElementMap.update({
        __name.name() : __name,
        __density.name() : __density,
        __thermal_conduc.name() : __thermal_conduc,
        __heat_capac.name() : __heat_capac,
        __solar_absorp.name() : __solar_absorp,
        __ir_emissivity.name() : __ir_emissivity,
        __PE_non_regenerable.name() : __PE_non_regenerable,
        __PE_regenerable.name() : __PE_regenerable,
        __secondary_fuels.name() : __secondary_fuels,
        __water_use.name() : __water_use,
        __ore_dressing_residues.name() : __ore_dressing_residues,
        __industrial_waste.name() : __industrial_waste,
        __hazardous_wastes.name() : __hazardous_wastes,
        __ADP.name() : __ADP,
        __EP.name() : __EP,
        __ODP.name() : __ODP,
        __POCP.name() : __POCP,
        __GWP_100.name() : __GWP_100,
        __AP.name() : __AP,
        __cost.name() : __cost
    })
    _AttributeMap.update({
        __material_id.name() : __material_id
    })
Namespace.addCategoryObject('typeBinding', 'MaterialType', MaterialType)


# Complex type MaterialTemplatesType with content type ELEMENT_ONLY
class MaterialTemplatesType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type MaterialTemplatesType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'MaterialTemplatesType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\Dude\\Documents\\UNI\\Masterarbeit\\pyxb-PyXB-1.2.4\\scripts\\MaterialTemplates.xsd', 29, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Material uses Python identifier Material
    __Material = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Material'), 'Material', '__AbsentNamespace0_MaterialTemplatesType_Material', True, pyxb.utils.utility.Location('C:\\Users\\Dude\\Documents\\UNI\\Masterarbeit\\pyxb-PyXB-1.2.4\\scripts\\MaterialTemplates.xsd', 32, 6), )

    
    Material = property(__Material.value, __Material.set, None, None)

    
    # Attribute version uses Python identifier version
    __version = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'version'), 'version', '__AbsentNamespace0_MaterialTemplatesType_version', pyxb.binding.datatypes.string)
    __version._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\Dude\\Documents\\UNI\\Masterarbeit\\pyxb-PyXB-1.2.4\\scripts\\MaterialTemplates.xsd', 30, 4)
    __version._UseLocation = pyxb.utils.utility.Location('C:\\Users\\Dude\\Documents\\UNI\\Masterarbeit\\pyxb-PyXB-1.2.4\\scripts\\MaterialTemplates.xsd', 30, 4)
    
    version = property(__version.value, __version.set, None, None)

    _ElementMap.update({
        __Material.name() : __Material
    })
    _AttributeMap.update({
        __version.name() : __version
    })
Namespace.addCategoryObject('typeBinding', 'MaterialTemplatesType', MaterialTemplatesType)


MaterialTemplates = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'MaterialTemplates'), MaterialTemplatesType, location=pyxb.utils.utility.Location('C:\\Users\\Dude\\Documents\\UNI\\Masterarbeit\\pyxb-PyXB-1.2.4\\scripts\\MaterialTemplates.xsd', 3, 2))
Namespace.addCategoryObject('elementBinding', MaterialTemplates.name().localName(), MaterialTemplates)



MaterialType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'name'), pyxb.binding.datatypes.string, scope=MaterialType, location=pyxb.utils.utility.Location('C:\\Users\\Dude\\Documents\\UNI\\Masterarbeit\\pyxb-PyXB-1.2.4\\scripts\\MaterialTemplates.xsd', 7, 6)))

MaterialType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'density'), pyxb.binding.datatypes.float, scope=MaterialType, location=pyxb.utils.utility.Location('C:\\Users\\Dude\\Documents\\UNI\\Masterarbeit\\pyxb-PyXB-1.2.4\\scripts\\MaterialTemplates.xsd', 8, 6)))

MaterialType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'thermal_conduc'), pyxb.binding.datatypes.float, scope=MaterialType, location=pyxb.utils.utility.Location('C:\\Users\\Dude\\Documents\\UNI\\Masterarbeit\\pyxb-PyXB-1.2.4\\scripts\\MaterialTemplates.xsd', 9, 6)))

MaterialType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'heat_capac'), pyxb.binding.datatypes.float, scope=MaterialType, location=pyxb.utils.utility.Location('C:\\Users\\Dude\\Documents\\UNI\\Masterarbeit\\pyxb-PyXB-1.2.4\\scripts\\MaterialTemplates.xsd', 10, 6)))

MaterialType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'solar_absorp'), pyxb.binding.datatypes.float, scope=MaterialType, location=pyxb.utils.utility.Location('C:\\Users\\Dude\\Documents\\UNI\\Masterarbeit\\pyxb-PyXB-1.2.4\\scripts\\MaterialTemplates.xsd', 11, 6)))

MaterialType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'ir_emissivity'), pyxb.binding.datatypes.float, scope=MaterialType, location=pyxb.utils.utility.Location('C:\\Users\\Dude\\Documents\\UNI\\Masterarbeit\\pyxb-PyXB-1.2.4\\scripts\\MaterialTemplates.xsd', 12, 6)))

MaterialType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'PE_non_regenerable'), pyxb.binding.datatypes.float, scope=MaterialType, location=pyxb.utils.utility.Location('C:\\Users\\Dude\\Documents\\UNI\\Masterarbeit\\pyxb-PyXB-1.2.4\\scripts\\MaterialTemplates.xsd', 13, 6)))

MaterialType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'PE_regenerable'), pyxb.binding.datatypes.float, scope=MaterialType, location=pyxb.utils.utility.Location('C:\\Users\\Dude\\Documents\\UNI\\Masterarbeit\\pyxb-PyXB-1.2.4\\scripts\\MaterialTemplates.xsd', 14, 6)))

MaterialType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'secondary_fuels'), pyxb.binding.datatypes.float, scope=MaterialType, location=pyxb.utils.utility.Location('C:\\Users\\Dude\\Documents\\UNI\\Masterarbeit\\pyxb-PyXB-1.2.4\\scripts\\MaterialTemplates.xsd', 15, 6)))

MaterialType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'water_use'), pyxb.binding.datatypes.float, scope=MaterialType, location=pyxb.utils.utility.Location('C:\\Users\\Dude\\Documents\\UNI\\Masterarbeit\\pyxb-PyXB-1.2.4\\scripts\\MaterialTemplates.xsd', 16, 6)))

MaterialType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'ore_dressing_residues'), pyxb.binding.datatypes.float, scope=MaterialType, location=pyxb.utils.utility.Location('C:\\Users\\Dude\\Documents\\UNI\\Masterarbeit\\pyxb-PyXB-1.2.4\\scripts\\MaterialTemplates.xsd', 17, 6)))

MaterialType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'industrial_waste'), pyxb.binding.datatypes.float, scope=MaterialType, location=pyxb.utils.utility.Location('C:\\Users\\Dude\\Documents\\UNI\\Masterarbeit\\pyxb-PyXB-1.2.4\\scripts\\MaterialTemplates.xsd', 18, 6)))

MaterialType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'hazardous_wastes'), pyxb.binding.datatypes.float, scope=MaterialType, location=pyxb.utils.utility.Location('C:\\Users\\Dude\\Documents\\UNI\\Masterarbeit\\pyxb-PyXB-1.2.4\\scripts\\MaterialTemplates.xsd', 19, 6)))

MaterialType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'ADP'), pyxb.binding.datatypes.float, scope=MaterialType, location=pyxb.utils.utility.Location('C:\\Users\\Dude\\Documents\\UNI\\Masterarbeit\\pyxb-PyXB-1.2.4\\scripts\\MaterialTemplates.xsd', 20, 6)))

MaterialType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'EP'), pyxb.binding.datatypes.float, scope=MaterialType, location=pyxb.utils.utility.Location('C:\\Users\\Dude\\Documents\\UNI\\Masterarbeit\\pyxb-PyXB-1.2.4\\scripts\\MaterialTemplates.xsd', 21, 6)))

MaterialType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'ODP'), pyxb.binding.datatypes.float, scope=MaterialType, location=pyxb.utils.utility.Location('C:\\Users\\Dude\\Documents\\UNI\\Masterarbeit\\pyxb-PyXB-1.2.4\\scripts\\MaterialTemplates.xsd', 22, 6)))

MaterialType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'POCP'), pyxb.binding.datatypes.float, scope=MaterialType, location=pyxb.utils.utility.Location('C:\\Users\\Dude\\Documents\\UNI\\Masterarbeit\\pyxb-PyXB-1.2.4\\scripts\\MaterialTemplates.xsd', 23, 6)))

MaterialType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'GWP_100'), pyxb.binding.datatypes.float, scope=MaterialType, location=pyxb.utils.utility.Location('C:\\Users\\Dude\\Documents\\UNI\\Masterarbeit\\pyxb-PyXB-1.2.4\\scripts\\MaterialTemplates.xsd', 24, 6)))

MaterialType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'AP'), pyxb.binding.datatypes.float, scope=MaterialType, location=pyxb.utils.utility.Location('C:\\Users\\Dude\\Documents\\UNI\\Masterarbeit\\pyxb-PyXB-1.2.4\\scripts\\MaterialTemplates.xsd', 25, 6)))

MaterialType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'cost'), pyxb.binding.datatypes.float, scope=MaterialType, location=pyxb.utils.utility.Location('C:\\Users\\Dude\\Documents\\UNI\\Masterarbeit\\pyxb-PyXB-1.2.4\\scripts\\MaterialTemplates.xsd', 26, 6)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\Dude\\Documents\\UNI\\Masterarbeit\\pyxb-PyXB-1.2.4\\scripts\\MaterialTemplates.xsd', 11, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\Dude\\Documents\\UNI\\Masterarbeit\\pyxb-PyXB-1.2.4\\scripts\\MaterialTemplates.xsd', 12, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\Dude\\Documents\\UNI\\Masterarbeit\\pyxb-PyXB-1.2.4\\scripts\\MaterialTemplates.xsd', 13, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\Dude\\Documents\\UNI\\Masterarbeit\\pyxb-PyXB-1.2.4\\scripts\\MaterialTemplates.xsd', 14, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\Dude\\Documents\\UNI\\Masterarbeit\\pyxb-PyXB-1.2.4\\scripts\\MaterialTemplates.xsd', 15, 6))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\Dude\\Documents\\UNI\\Masterarbeit\\pyxb-PyXB-1.2.4\\scripts\\MaterialTemplates.xsd', 16, 6))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\Dude\\Documents\\UNI\\Masterarbeit\\pyxb-PyXB-1.2.4\\scripts\\MaterialTemplates.xsd', 17, 6))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\Dude\\Documents\\UNI\\Masterarbeit\\pyxb-PyXB-1.2.4\\scripts\\MaterialTemplates.xsd', 18, 6))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\Dude\\Documents\\UNI\\Masterarbeit\\pyxb-PyXB-1.2.4\\scripts\\MaterialTemplates.xsd', 19, 6))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\Dude\\Documents\\UNI\\Masterarbeit\\pyxb-PyXB-1.2.4\\scripts\\MaterialTemplates.xsd', 20, 6))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\Dude\\Documents\\UNI\\Masterarbeit\\pyxb-PyXB-1.2.4\\scripts\\MaterialTemplates.xsd', 21, 6))
    counters.add(cc_10)
    cc_11 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\Dude\\Documents\\UNI\\Masterarbeit\\pyxb-PyXB-1.2.4\\scripts\\MaterialTemplates.xsd', 22, 6))
    counters.add(cc_11)
    cc_12 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\Dude\\Documents\\UNI\\Masterarbeit\\pyxb-PyXB-1.2.4\\scripts\\MaterialTemplates.xsd', 23, 6))
    counters.add(cc_12)
    cc_13 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\Dude\\Documents\\UNI\\Masterarbeit\\pyxb-PyXB-1.2.4\\scripts\\MaterialTemplates.xsd', 24, 6))
    counters.add(cc_13)
    cc_14 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\Dude\\Documents\\UNI\\Masterarbeit\\pyxb-PyXB-1.2.4\\scripts\\MaterialTemplates.xsd', 25, 6))
    counters.add(cc_14)
    cc_15 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\Dude\\Documents\\UNI\\Masterarbeit\\pyxb-PyXB-1.2.4\\scripts\\MaterialTemplates.xsd', 26, 6))
    counters.add(cc_15)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(MaterialType._UseForTag(pyxb.namespace.ExpandedName(None, 'name')), pyxb.utils.utility.Location('C:\\Users\\Dude\\Documents\\UNI\\Masterarbeit\\pyxb-PyXB-1.2.4\\scripts\\MaterialTemplates.xsd', 7, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(MaterialType._UseForTag(pyxb.namespace.ExpandedName(None, 'density')), pyxb.utils.utility.Location('C:\\Users\\Dude\\Documents\\UNI\\Masterarbeit\\pyxb-PyXB-1.2.4\\scripts\\MaterialTemplates.xsd', 8, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(MaterialType._UseForTag(pyxb.namespace.ExpandedName(None, 'thermal_conduc')), pyxb.utils.utility.Location('C:\\Users\\Dude\\Documents\\UNI\\Masterarbeit\\pyxb-PyXB-1.2.4\\scripts\\MaterialTemplates.xsd', 9, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(MaterialType._UseForTag(pyxb.namespace.ExpandedName(None, 'heat_capac')), pyxb.utils.utility.Location('C:\\Users\\Dude\\Documents\\UNI\\Masterarbeit\\pyxb-PyXB-1.2.4\\scripts\\MaterialTemplates.xsd', 10, 6))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(MaterialType._UseForTag(pyxb.namespace.ExpandedName(None, 'solar_absorp')), pyxb.utils.utility.Location('C:\\Users\\Dude\\Documents\\UNI\\Masterarbeit\\pyxb-PyXB-1.2.4\\scripts\\MaterialTemplates.xsd', 11, 6))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(MaterialType._UseForTag(pyxb.namespace.ExpandedName(None, 'ir_emissivity')), pyxb.utils.utility.Location('C:\\Users\\Dude\\Documents\\UNI\\Masterarbeit\\pyxb-PyXB-1.2.4\\scripts\\MaterialTemplates.xsd', 12, 6))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(MaterialType._UseForTag(pyxb.namespace.ExpandedName(None, 'PE_non_regenerable')), pyxb.utils.utility.Location('C:\\Users\\Dude\\Documents\\UNI\\Masterarbeit\\pyxb-PyXB-1.2.4\\scripts\\MaterialTemplates.xsd', 13, 6))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(MaterialType._UseForTag(pyxb.namespace.ExpandedName(None, 'PE_regenerable')), pyxb.utils.utility.Location('C:\\Users\\Dude\\Documents\\UNI\\Masterarbeit\\pyxb-PyXB-1.2.4\\scripts\\MaterialTemplates.xsd', 14, 6))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(MaterialType._UseForTag(pyxb.namespace.ExpandedName(None, 'secondary_fuels')), pyxb.utils.utility.Location('C:\\Users\\Dude\\Documents\\UNI\\Masterarbeit\\pyxb-PyXB-1.2.4\\scripts\\MaterialTemplates.xsd', 15, 6))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(MaterialType._UseForTag(pyxb.namespace.ExpandedName(None, 'water_use')), pyxb.utils.utility.Location('C:\\Users\\Dude\\Documents\\UNI\\Masterarbeit\\pyxb-PyXB-1.2.4\\scripts\\MaterialTemplates.xsd', 16, 6))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(MaterialType._UseForTag(pyxb.namespace.ExpandedName(None, 'ore_dressing_residues')), pyxb.utils.utility.Location('C:\\Users\\Dude\\Documents\\UNI\\Masterarbeit\\pyxb-PyXB-1.2.4\\scripts\\MaterialTemplates.xsd', 17, 6))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(MaterialType._UseForTag(pyxb.namespace.ExpandedName(None, 'industrial_waste')), pyxb.utils.utility.Location('C:\\Users\\Dude\\Documents\\UNI\\Masterarbeit\\pyxb-PyXB-1.2.4\\scripts\\MaterialTemplates.xsd', 18, 6))
    st_11 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(MaterialType._UseForTag(pyxb.namespace.ExpandedName(None, 'hazardous_wastes')), pyxb.utils.utility.Location('C:\\Users\\Dude\\Documents\\UNI\\Masterarbeit\\pyxb-PyXB-1.2.4\\scripts\\MaterialTemplates.xsd', 19, 6))
    st_12 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(MaterialType._UseForTag(pyxb.namespace.ExpandedName(None, 'ADP')), pyxb.utils.utility.Location('C:\\Users\\Dude\\Documents\\UNI\\Masterarbeit\\pyxb-PyXB-1.2.4\\scripts\\MaterialTemplates.xsd', 20, 6))
    st_13 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_13)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_10, False))
    symbol = pyxb.binding.content.ElementUse(MaterialType._UseForTag(pyxb.namespace.ExpandedName(None, 'EP')), pyxb.utils.utility.Location('C:\\Users\\Dude\\Documents\\UNI\\Masterarbeit\\pyxb-PyXB-1.2.4\\scripts\\MaterialTemplates.xsd', 21, 6))
    st_14 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_14)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_11, False))
    symbol = pyxb.binding.content.ElementUse(MaterialType._UseForTag(pyxb.namespace.ExpandedName(None, 'ODP')), pyxb.utils.utility.Location('C:\\Users\\Dude\\Documents\\UNI\\Masterarbeit\\pyxb-PyXB-1.2.4\\scripts\\MaterialTemplates.xsd', 22, 6))
    st_15 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_15)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_12, False))
    symbol = pyxb.binding.content.ElementUse(MaterialType._UseForTag(pyxb.namespace.ExpandedName(None, 'POCP')), pyxb.utils.utility.Location('C:\\Users\\Dude\\Documents\\UNI\\Masterarbeit\\pyxb-PyXB-1.2.4\\scripts\\MaterialTemplates.xsd', 23, 6))
    st_16 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_16)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_13, False))
    symbol = pyxb.binding.content.ElementUse(MaterialType._UseForTag(pyxb.namespace.ExpandedName(None, 'GWP_100')), pyxb.utils.utility.Location('C:\\Users\\Dude\\Documents\\UNI\\Masterarbeit\\pyxb-PyXB-1.2.4\\scripts\\MaterialTemplates.xsd', 24, 6))
    st_17 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_17)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_14, False))
    symbol = pyxb.binding.content.ElementUse(MaterialType._UseForTag(pyxb.namespace.ExpandedName(None, 'AP')), pyxb.utils.utility.Location('C:\\Users\\Dude\\Documents\\UNI\\Masterarbeit\\pyxb-PyXB-1.2.4\\scripts\\MaterialTemplates.xsd', 25, 6))
    st_18 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_18)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_15, False))
    symbol = pyxb.binding.content.ElementUse(MaterialType._UseForTag(pyxb.namespace.ExpandedName(None, 'cost')), pyxb.utils.utility.Location('C:\\Users\\Dude\\Documents\\UNI\\Masterarbeit\\pyxb-PyXB-1.2.4\\scripts\\MaterialTemplates.xsd', 26, 6))
    st_19 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_19)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    transitions.append(fac.Transition(st_10, [
         ]))
    transitions.append(fac.Transition(st_11, [
         ]))
    transitions.append(fac.Transition(st_12, [
         ]))
    transitions.append(fac.Transition(st_13, [
         ]))
    transitions.append(fac.Transition(st_14, [
         ]))
    transitions.append(fac.Transition(st_15, [
         ]))
    transitions.append(fac.Transition(st_16, [
         ]))
    transitions.append(fac.Transition(st_17, [
         ]))
    transitions.append(fac.Transition(st_18, [
         ]))
    transitions.append(fac.Transition(st_19, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_8, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_8, False) ]))
    st_12._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_9, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_9, False) ]))
    st_13._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_10, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_10, False) ]))
    st_14._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_11, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_11, False) ]))
    st_15._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_12, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_12, False) ]))
    st_16._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_13, True) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_13, False) ]))
    st_17._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_14, True) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_14, False) ]))
    st_18._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_15, True) ]))
    st_19._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
MaterialType._Automaton = _BuildAutomaton()




MaterialTemplatesType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Material'), MaterialType, scope=MaterialTemplatesType, location=pyxb.utils.utility.Location('C:\\Users\\Dude\\Documents\\UNI\\Masterarbeit\\pyxb-PyXB-1.2.4\\scripts\\MaterialTemplates.xsd', 32, 6)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('C:\\Users\\Dude\\Documents\\UNI\\Masterarbeit\\pyxb-PyXB-1.2.4\\scripts\\MaterialTemplates.xsd', 31, 1))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(MaterialTemplatesType._UseForTag(pyxb.namespace.ExpandedName(None, 'Material')), pyxb.utils.utility.Location('C:\\Users\\Dude\\Documents\\UNI\\Masterarbeit\\pyxb-PyXB-1.2.4\\scripts\\MaterialTemplates.xsd', 32, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
MaterialTemplatesType._Automaton = _BuildAutomaton_()

