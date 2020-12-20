from django.contrib import admin

from .models import Simulation, SimulationSource, Scenario


class SimulationSourceInlineAdmin(admin.TabularInline):
    model = SimulationSource


class ScenarioChoiceInlineAdmin(admin.TabularInline):
    model = Scenario.choices.through


@admin.register(Simulation)
class SimulationAdmin(admin.ModelAdmin):
    inlines = [SimulationSourceInlineAdmin]


@admin.register(Scenario)
class ScenarioAdmin(admin.ModelAdmin):
    inlines = [ScenarioChoiceInlineAdmin]
