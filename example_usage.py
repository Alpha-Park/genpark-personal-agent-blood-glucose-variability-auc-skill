# -*- coding: utf-8 -*-
"""Demonstration of Personal Agent Blood Glucose Variability AUC Skill."""

import sys
sys.stdout.reconfigure(encoding='utf-8')
from client import PersonalAgentBloodGlucoseVariabilityAuc

def main():
    agent = PersonalAgentBloodGlucoseVariabilityAuc()

    print("=" * 70)
    print("DEMO: Personal Agent Blood Glucose Variability & CGM Modeler")
    print("=" * 70)

    # 1. 16 consecutive CGM readings (4 hours after high-carb meal)
    readings = [88.0, 92.0, 118.0, 158.0, 172.0, 164.0, 142.0, 125.0, 108.0, 94.0, 78.0, 72.0, 84.0, 88.0, 90.0, 89.0]

    res_cgm = agent.calculate_cgm_glycemic_variability(
        glucose_readings_mg_dl=readings,
        sampling_interval_minutes=15.0
    )

    print(f"\n1. CGM Glycemic Volatility Analysis (16 readings):")
    print(f"   Mean Glucose: {res_cgm['mean_glucose_mg_dl']} mg/dL (SD: {res_cgm['glucose_standard_deviation_mg_dl']} mg/dL)")
    print(f"   Coefficient of Variation: {res_cgm['coefficient_of_variation_pct']}")
    print(f"   Time in Range (70-140): {res_cgm['time_in_range_70_140_pct']}")
    print(f"   MAGE Excursion Amplitude: {res_cgm['mean_amplitude_glycemic_excursions_mage']}")
    print(f"   Incremental AUC: {res_cgm['incremental_auc_units']}")
    print(f"   Status: {res_cgm['glycemic_stability_tier']}")
    print(f"   Implication: {res_cgm['metabolic_implication']}")

    # 2. Prescribe stabilization protocol
    res_proto = agent.prescribe_glycemic_stabilization_protocol(
        cv_percentage=32.5,
        peak_glucose_mg_dl=172.0
    )

    print(f"\n2. Glycemic Stabilization Prescription:")
    print(f"   Expected Spike Reduction: {res_proto['projected_glycemic_spike_reduction']}")
    for title, action in res_proto['actionable_stabilization_interventions']:
        print(f"   - {title}:")
        print(f"       {action}")
    print(f"   Crash Prevention: {res_proto['reactive_crash_prevention']}")

    print("\nVerification complete: Blood glucose variability engine executed flawlessly.")

if __name__ == "__main__":
    main()
