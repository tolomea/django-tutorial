from django.contrib import admin

from .models import Simulation, Scenario


@admin.register(Simulation)
class SimulationAdmin(admin.ModelAdmin):
    pass


@admin.register(Scenario)
class ScenarioAdmin(admin.ModelAdmin):
    pass
