import auto_prefetch
from django.db import models


class Simulation(auto_prefetch.Model):
    pass


class SimulationSource(auto_prefetch.Model):
    name = models.CharField(max_length=10)
    simulation = auto_prefetch.ForeignKey(
        Simulation, on_delete=models.CASCADE, related_name="simulation_sources"
    )


class Scenario(auto_prefetch.Model):
    simulation = auto_prefetch.ForeignKey(
        Simulation, on_delete=models.CASCADE, related_name="scenarios"
    )

    choices = models.ManyToManyField(
        SimulationSource, through="ScenarioChoice", related_name="scenarios"
    )


class ScenarioChoice(auto_prefetch.Model):
    scenario = auto_prefetch.ForeignKey(
        Scenario, on_delete=models.CASCADE, related_name="scenario_choices"
    )
    simulation_source = auto_prefetch.ForeignKey(
        SimulationSource, on_delete=models.CASCADE, related_name="scenario_choices"
    )
