from sierra.base_parameters import MinFlowParameter
from sierra.utilities.converter import convert
from numba import jit, njit, vectorize
from numba.experimental import jitclass

class IFR_bl_Bolsillo_Creek_Div_Min_Flow(MinFlowParameter):
    """"""

    @jit
    def _value(self, timestep, scenario_index):
        
        ifr_cfs = 0.4
        
        if self.model.mode == "planning":
            ifr_cfs *= self.days_in_month
        
        return ifr_cfs / 35.31
    
    def value(self, timestep, scenario_index):
        val = self.requirement(timestep, scenario_index, default=self._value)
        return convert(val, "m^3 s^-1", "m^3 day^-1", scale_in=1, scale_out=1000000.0)
            
    @classmethod
    def load(cls, model, data):
        try:
            return cls(model, **data)
        except Exception as err:
            print('File where error occurred: {}'.format(__file__))
            print(err)
            raise
        
IFR_bl_Bolsillo_Creek_Div_Min_Flow.register()
