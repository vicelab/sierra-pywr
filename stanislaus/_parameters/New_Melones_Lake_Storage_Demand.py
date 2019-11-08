from parameters import WaterLPParameter

from utilities.converter import convert
import datetime as dt


class New_Melones_Lake_Storage_Demand(WaterLPParameter):

    def _value(self, timestep, scenario_index):
        path = "Management/BAU/Flood Control/LakeMelones_FloodControl_Requirement.csv"
        flood_control_req = self.read_csv(path, index_col=[0], parse_dates=True, squeeze=True)
        start = self.datetime.strftime('%b-%d')
        if self.model.mode == 'scheduling':
            control_curve_target = flood_control_req[start]
        else:
            end = self.datetime.strftime('%b-{:02}'.format(self.days_in_month()))
            control_curve_target = flood_control_req[start:end].mean()
        max_storage = self.model.nodes["New Melones Lake" + self.month_suffix].max_volume
        return control_curve_target / max_storage
        # return control_curve_target

    def value(self, timestep, scenario_index):
        try:
            return self._value(timestep, scenario_index)
        except Exception as err:
            print('\nERROR for parameter {}'.format(self.name))
            print('File where error occurred: {}'.format(__file__))
            print(err)

    @classmethod
    def load(cls, model, data):
        return cls(model, **data)


New_Melones_Lake_Storage_Demand.register()
print(" [*] New_Melones_Lake_Storage_Demand successfully registered")