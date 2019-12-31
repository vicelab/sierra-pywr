from parameters import WaterLPParameter

from utilities.converter import convert


class IFR_bl_Huntington_Lake_Min_Flow(WaterLPParameter):
    """"""

    def _value(self, timestep, scenario_index):

        return_val = 0

        if (4, 15) <= (self.datetime.month, self.datetime.day) <= (12, 15):
            return_val = 2

        if self.model.mode == "planning":
            return_val *= self.days_in_month()
        return return_val

    def value(self, timestep, scenario_index):
        try:
            return convert(self._value(timestep, scenario_index), "m^3 s^-1", "m^3 day^-1", scale_in=1,
                           scale_out=1000000.0)
        except Exception as err:
            print('ERROR for parameter {}'.format(self.name))
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


IFR_bl_Huntington_Lake_Min_Flow.register()
print(" [*] IFR_bl_Huntington_Lake_Min_Flow successfully registered")
