from django.db import models


class Simulation(models.Model):
    pass


class Scenario(models.Model):
    simulation = models.ForeignKey(
        Simulation, on_delete=models.CASCADE, related_name="scenarios"
    )
