# created November 2016
# by TEASER4 Development Team


import re
import uuid
import teaser.data.input.energy_carrier_input as energy_carrier_input
import teaser.data.output.energy_carrier_output as energy_carrier_output

class EnergyCarrier(object):
    '''This class represents a EnergyCarrier.

    Attributes (each KPI is based on 1 kWh of the energy_carrier)
    ----------
    name : str
        Individual name
        
    PE_non_regenerable (input) : float
        used non regenerable primary energy input to built the energy_carrier in MJ/kWh
        
    PE_regenerable (input) : float
        used regenerable primary energy input to built the energy_carrier in MJ/kWh
        
    secondary_fuels (input) : float
        used secondary fuels to built the energy_carrier in MJ/kWh
    
    water_use (input) : float
        used water in the manufacturing process of the energy_carrier in kg(Water)/kWh
        
    ore_dressing_residues (output) : float
        residues of ore emitted by the manufacturing process of the energy_carrier
        in kg(ore)/kWh
    
    industrial_waste (output) : float
        industrial waste emitted by the manufacturing process of the energy_carrier
        in kg(waste)/kWh
    
   hazardous_wastes (output) : float
       hazardous waste emitted by the manufacturing process of the energy_carrier
        in kg(waste)/kWh
        
    ADP (input) : float
        abiotic depletion potential used in the manufacturing process of the
        energy_carrier in kg (Sb-eqv.)/ kg
        
    EP (output) : float
        euthropication potential emitted by the manufacturing process of the 
        energy_carrier in kg(phosphate-eqv)/kWh
        
    ODP (output) : float
        ozone depletion potential emitted by the manufacturing process of the 
        energy_carrier in kg(R11eqv)/kWh
    
    POCP (output) : float
        photochemical ozone creation potential emitted by the manufacturing 
        process of the energy_carrier in kg(ethene-eqv)/kWh
    
    GWP_100 (output) : float
        global warming potential (greenhouse potential) emitted by the EnergyCarrier
        over his whole lifecyle in kg(CO2-eqv.)/kWh
        
        
    AP (output) : float
        acidification potential caused by the EnergyCarrier
        over his whole lifecyle in kg(SO2-eqv.)/kWh
    
    costs : float
        energy_carrier price in Euro/kWh    
        
    energy_carrier_id : str(uuid)
        UUID of energy_carrier, this is used to have similar behaviour like foreign
        key in SQL data bases for use in TypeBuildingElements and EnergyCarrier xml

    '''

    def __init__(self, parent=None):
        '''Constructor of EnergyCarrier.


        '''

        self._name = ""
        self._density = 0.0
        self._PE_non_regenerable = 0.0
        self._PE_regenerable = 0.0
        self._secondary_fuels = 0.0
        self._water_use = 0.0
        self._ore_dressing_residues = 0.0
        self._industrial_waste = 0.0
        self._hazardous_wastes = 0.0
        self._ADP = 0.0
        self._EP_100 = 0.0
        self._ODP = 0.0
        self._POCP = 0.0
        self._GWP_100 = 0.0
        self._AP = 0.0
        self._costs = 0.0

        self.energy_carrier_id = str(uuid.uuid1())

    def load_energy_carrier_template(self, enc_name, data_class=None):
        '''EnergyCarrier loader.

        Loads EnergyCarrier specified in the XML.

        Parameters
        ----------

        enc_name : str
            Code list for EnergyCarrier

        data_class : DataClass()
            DataClass containing the bindings for TypeBuildingElement and
            EnergyCarrier (typically this is the data class stored in prj.data,
            but the user can individually change that. Default is
            self.parent.parent.parent.parent.data which is data in project

        '''

        if data_class is None:
            data_class = self.parent.parent.parent.parent.data
        else:
            data_class = data_class

        energy_carrier_input.load_energy_carrier(energy_carrier=self,
                                     enc_name=enc_name,
                                     data_class=data_class)

    def save_energy_carrier_template(self, data_class):
        '''EnergyCarrier saver.

        Saves EnergyCarrier specified in the XML.

        Parameters
        ----------

        data_class : DataClass()
            DataClass containing the bindings for TypeBuildingElement and
            EnergyCarrier (typically this is the data class stored in prj.data,
            but the user can individually change that. Default is
            self.parent.parent.parent.parent.data which is data in project

        '''

        if data_class is None:
            data_class = self.parent.parent.parent.parent.data
        else:
            data_class = data_class

        energy_carrier_output.save_energy_carrier(energy_carrier=self, data_class=data_class)


    @property
    def energy_carrier_id(self):
        return self.__energy_carrier_id

    @energy_carrier_id.setter
    def energy_carrier_id(self, value):
        self.__energy_carrier_id = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str):
            regex = re.compile('[^a-zA-z0-9]')
            self._name = regex.sub('', value)
        else:
            try:
                value = str(value)
                regex = re.compile('[^a-zA-z0-9]')
                self._name = regex.sub('', value)
            except ValueError:
                print("Can't convert name to string")

    @property
    def thermal_conduc(self):
        return self._thermal_conduc

    @thermal_conduc.setter
    def thermal_conduc(self, value):

        if isinstance(value, float):
            pass
        elif value is None:
            pass
        else:
            try:
                value = float(value)
            except:
                raise ValueError("Can't convert thermal conduction to float")

        if value is not None:
            self._thermal_conduc = float(value)
            if self.parent is not None:
                if self.parent.parent is not None:
                    if self.parent.thickness is not None and\
                       self.parent.parent.inner_convection is not None and\
                       self.parent.parent.inner_radiation is not None and\
                       self.parent.parent.area is not None:
                        self.parent.parent.calc_ua_value()

    @property
    def density(self):
        return self._density

    @density.setter
    def density(self, value):

        if isinstance(value, float):
            self._density = value
        elif value is None:
            self._density = value
        else:
            try:
                value = float(value)
                self._density = value
            except:
                raise ValueError("Can't convert density to float")

    @property
    def PE_non_regenerable(self):
        return self._PE_non_regenerable

    @PE_non_regenerable.setter
    def PE_non_regenerable(self, value):

        if isinstance(value, float):
            self._PE_non_regenerable = value
        elif value is None:
            self._PE_non_regenerable = value
        else:
            try:
                value = float(value)
                self._PE_non_regenerable = value
            except:
                raise ValueError("Can't convert PE_non_regenerable to float")

    @property
    def PE_regenerable(self):
        return self._PE_regenerable
        
    @PE_regenerable.setter
    def PE_regenerable(self, value):

        if isinstance(value, float):
            self._PE_regenerable = value
        elif value is None:
            self._PE_regenerable = value
        else:
            try:
                value = float(value)
                self._PE_regenerable = value
            except:
                raise ValueError("Can't convert PE_regenerable to float")
                

    @property
    def secondary_fuels(self):
        return self._secondary_fuels
        
    @secondary_fuels.setter
    def secondary_fuels(self, value):

        if isinstance(value, float):
            self._secondary_fuels = value
        elif value is None:
            self._secondary_fuels = value
        else:
            try:
                value = float(value)
                self._secondary_fuels = value
            except:
                raise ValueError("Can't convert secondary_fuels to float")

    @property
    def water_use(self):
        return self._water_use

    @water_use.setter
    def water_use(self, value):

        if isinstance(value, float):
            self._water_use = value
        elif value is None:
            self._water_use = value
        else:
            try:
                value = float(value)
                self._water_use = value
            except:
                raise ValueError("Can't convert water_use to float")

    @property
    def ore_dressing_residues(self):
        return self._ore_dressing_residues

    @ore_dressing_residues.setter
    def ore_dressing_residues(self, value):

        if isinstance(value, float):
            self._ore_dressing_residues = value
        elif value is None:
            self._ore_dressing_residues = value
        else:
            try:
                value = float(value)
                self._ore_dressing_residues = value
            except:
                raise ValueError("Can't convert ore_dressing_residues to float")
                
    @property
    def industrial_waste(self):
        return self._industrial_waste

    @industrial_waste.setter
    def industrial_waste(self, value):

        if isinstance(value, float):
            self._industrial_waste = value
        elif value is None:
            self._industrial_waste = value
        else:
            try:
                value = float(value)
                self._industrial_waste = value
            except:
                raise ValueError("Can't industrial_waste cost to float")
                
    @property
    def hazardous_wastes(self):
        return self._hazardous_wastes

    @hazardous_wastes.setter
    def hazardous_wastes(self, value):

        if isinstance(value, float):
            self._hazardous_wastes = value
        elif value is None:
            self._hazardous_wastes = value
        else:
            try:
                value = float(value)
                self._hazardous_wastes = value
            except:
                raise ValueError("Can't convert hazardous_wastes to float")

    @property
    def ADP(self):
        return self._ADP
        
    @ADP.setter
    def ADP(self, value):

        if isinstance(value, float):
            self._ADP = value
        elif value is None:
            self._ADP = value
        else:
            try:
                value = float(value)
                self._ADP = value
            except:
                raise ValueError("Can't convert ADP to float")
                

    @property
    def EP(self):
        return self._EP
        
    @EP.setter
    def EP(self, value):

        if isinstance(value, float):
            self._EP = value
        elif value is None:
            self._EP = value
        else:
            try:
                value = float(value)
                self._EP = value
            except:
                raise ValueError("Can't convert EP to float")

    @property
    def ODP(self):
        return self._ODP

    @ODP.setter
    def ODP(self, value):

        if isinstance(value, float):
            self._ODP = value
        elif value is None:
            self._ODP = value
        else:
            try:
                value = float(value)
                self._ODP = value
            except:
                raise ValueError("Can't convert ODP to float")

    @property
    def POCP(self):
        return self._POCP

    @POCP.setter
    def POCP(self, value):

        if isinstance(value, float):
            self._POCP = value
        elif value is None:
            self._POCP = value
        else:
            try:
                value = float(value)
                self._POCP = value
            except:
                raise ValueError("Can't convert POCP to float")

    @property
    def GWP_100(self):
        return self._GWP_100

    @GWP_100.setter
    def GWP_100(self, value):

        if isinstance(value, float):
            self._GWP_100 = value
        elif value is None:
            self._GWP_100 = value
        else:
            try:
                value = float(value)
                self._GWP_100 = value
            except:
                raise ValueError("Can't convert GWP_100 to float")

    @property
    def AP(self):
        return self._AP

    @AP.setter
    def AP(self, value):

        if isinstance(value, float):
            self._AP = value
        elif value is None:
            self._AP = value
        else:
            try:
                value = float(value)
                self._AP = value
            except:
                raise ValueError("Can't convert AP to float")
                
    @property
    def costs(self):
        return self._costs

    @costs.setter
    def costs(self, value):

        if isinstance(value, float):
            self._costs = value
        elif value is None:
            self._costs = value
        else:
            try:
                value = float(value)
                self._costs = value
            except:
                raise ValueError("Can't convert costs to float")
