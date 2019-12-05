from parameters import WaterLPParameter
from math import exp


class Pinecrest_Reservoir_Storage_Value(WaterLPParameter):

    def _value(self, timestep, scenario_index):
        base_cost = -60
        if self.model.mode == 'planning':
            return base_cost
        elev = self.model.nodes[self.res_name].get_level(scenario_index)
        offset = 100

        max_elev = 1710.2
        k = 0.3
        val = min(-exp(k * (max_elev - elev)), -offset) + offset + base_cost
        return val

    def value(self, timestep, scenario_index):
        return self._value(timestep, scenario_index)

    @classmethod
    def load(cls, model, data):
        return cls(model, **data)


Pinecrest_Reservoir_Storage_Value.register()
print(" [*] Pinecrest_Reservoir_Storage_Value successfully registered")
