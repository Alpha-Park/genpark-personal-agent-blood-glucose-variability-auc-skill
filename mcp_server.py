# -*- coding: utf-8 -*-
"""FastMCP Server for Personal Agent Blood Glucose Variability AUC Skill."""

from mcp.server.fastmcp import FastMCP
from client import PersonalAgentBloodGlucoseVariabilityAuc

mcp = FastMCP("PersonalAgentBloodGlucoseVariabilityAuc")
client = PersonalAgentBloodGlucoseVariabilityAuc()

@mcp.tool()
def calculate_cgm_glycemic_variability(
    glucose_readings_mg_dl: list[float],
    sampling_interval_minutes: float = 15.0
) -> str:
    """Calculates %CV, MAGE excursion amplitude, Time in Range, and iAUC from CGM readings."""
    import json
    return json.dumps(client.calculate_cgm_glycemic_variability(
        glucose_readings_mg_dl, sampling_interval_minutes
    ), indent=2)

@mcp.tool()
def prescribe_glycemic_stabilization_protocol(
    cv_percentage: float,
    peak_glucose_mg_dl: float = 160.0
) -> str:
    """Prescribes food sequencing, GLUT4 ambulation, and acetic acid protocols to blunt spikes."""
    import json
    return json.dumps(client.prescribe_glycemic_stabilization_protocol(
        cv_percentage, peak_glucose_mg_dl
    ), indent=2)

if __name__ == "__main__":
    mcp.run()
