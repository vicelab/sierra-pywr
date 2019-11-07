from parameters import WaterLPParameter

from utilities.converter import convert

class Cherry_Lake_Observed_Storage(WaterLPParameter):
    """"""

    def _value(self, timestep, scenario_index):
        
        df = self.read_csv("Observed/Reservoirs/GaugeReservoir_mcm_TUO_R3.csv", index_col=0, header=0)
        return df["Cherry Lake Reservoir"][timestep.datetime]
        
    def value(self, timestep, scenario_index):
        try:
            return self._value(timestep, scenario_index)
        except Exception as err:
            print('ERROR for parameter {}'.format(self.name))
            if type(err) == AssertionError:
                print('Value should return a real number, not a string')
            print('File where error occurred: {}'.format(__file__))
            print(err)
            raise

    @classmethod
    def load(cls, model, data):
        try:
            return cls(model, **data)
        except Exception as err:
            print('File where error occurred: {}'.format(__file__))
            print(err)
            raise
        
Cherry_Lake_Observed_Storage.register()
print(" [*] Cherry_Lake_Observed_Storage successfully registered")