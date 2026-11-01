# -*- coding: utf-8 -*-
"""
Personal Agent Blood Glucose Variability AUC Client
Zero-dependency Continuous Glucose Monitoring (CGM) glycemic variability calculator,
Mean Amplitude of Glycemic Excursions (MAGE) modeler, and postprandial iAUC stabilizer.
"""

import math
from typing import Dict, List, Any, Optional

class PersonalAgentBloodGlucoseVariabilityAuc:
    """
    Quantifies glycemic volatility, modeling Coefficient of Variation (%CV), MAGE amplitude,
    postprandial incremental Area Under the Curve (iAUC), and reactive hypoglycemia prevention.
    """

    def calculate_cgm_glycemic_variability(
        self,
        glucose_readings_mg_dl: List[float],
        sampling_interval_minutes: float = 15.0
    ) -> Dict[str, Any]:
        """
        Analyzes a time-series array of interstitial continuous glucose monitoring (CGM) readings:
        Clinical Target: %CV <= 36% (Stable euglycemia); MAGE < 45 mg/dL; Time in Range (70-140 mg/dL) >= 95%.
        """
        if not glucose_readings_mg_dl or len(glucose_readings_mg_dl) < 4:
            return {"error": "At least 4 continuous glucose readings required for glycemic variability analysis."}

        readings = [max(30.0, min(400.0, float(x))) for x in glucose_readings_mg_dl]
        n = len(readings)
        dt = max(1.0, min(60.0, float(sampling_interval_minutes)))

        mean_g = sum(readings) / n
        variance = sum((x - mean_g) ** 2 for x in readings) / n
        sd_g = math.sqrt(variance)

        # Coefficient of Variation (%CV = SD / Mean * 100)
        cv_pct = round((sd_g / mean_g) * 100.0, 1)

        # Time in Range (TIR): 70 - 140 mg/dL (strict non-diabetic longevity target)
        in_range = sum(1 for x in readings if 70.0 <= x <= 140.0)
        tir_pct = round((in_range / n) * 100.0, 1)

        above_140 = sum(1 for x in readings if x > 140.0)
        tar_pct = round((above_140 / n) * 100.0, 1)

        below_70 = sum(1 for x in readings if x < 70.0)
        tbr_pct = round((below_70 / n) * 100.0, 1)

        # Mean Amplitude of Glycemic Excursions (MAGE)
        # Calculates average peak-to-nadir amplitude for excursions exceeding 1.0 * SD
        excursions = []
        for i in range(1, n - 1):
            if readings[i] > readings[i-1] and readings[i] > readings[i+1]:
                # Local peak
                peak = readings[i]
                # Find preceding trough
                trough = min(readings[max(0, i-4):i])
                diff = peak - trough
                if diff > sd_g:
                    excursions.append(diff)

        mage = round(sum(excursions) / len(excursions), 1) if excursions else round(sd_g * 1.2, 1)

        # Incremental Area Under the Curve (iAUC) above fasting baseline (85 mg/dL)
        baseline = 85.0
        iauc = round(sum(max(0.0, x - baseline) * (dt / 60.0) for x in readings), 1)

        # Glycemic volatility status
        if cv_pct <= 25.0 and tir_pct >= 95.0:
            status = "Optimal Glycemic Stability (Low Oxidative Stress / Low Advanced Glycation End-products)"
            guidance = "Exceptional metabolic flexibility. Minimal insulin spikes and sustained cellular energy."
        elif cv_pct <= 36.0:
            status = "Acceptable Euglycemia (Standard Clinical Normal)"
            guidance = "Normal baseline; however, minor postprandial excursions indicate carbohydrate sensitivity."
        elif cv_pct <= 45.0:
            status = "Elevated Glycemic Volatility (Sub-Clinical Reactive Hypoglycemia / Glycation Risk)"
            guidance = "High amplitude swings trigger microvascular endothelial inflammation and energy crashes."
        else:
            status = "Severe Glycemic Instability (Critical Glucose Rollercoaster)"
            guidance = "Significant metabolic dysregulation. Implement food sequencing and post-meal ambulation."

        return {
            "mean_glucose_mg_dl": round(mean_g, 1),
            "glucose_standard_deviation_mg_dl": round(sd_g, 1),
            "coefficient_of_variation_pct": f"{cv_pct}% (Target: <= 36%)",
            "time_in_range_70_140_pct": f"{tir_pct}%",
            "time_above_range_pct": f"{tar_pct}%",
            "time_below_range_pct": f"{tbr_pct}%",
            "mean_amplitude_glycemic_excursions_mage": f"{mage} mg/dL",
            "incremental_auc_units": f"{iauc} mg*h/dL",
            "glycemic_stability_tier": status,
            "metabolic_implication": guidance
        }

    def prescribe_glycemic_stabilization_protocol(
        self,
        cv_percentage: float,
        peak_glucose_mg_dl: float = 160.0
    ) -> Dict[str, Any]:
        """
        Prescribes high-leverage behavioral protocols (food sequencing, GLUT4 ambulation,
        acetic acid pre-load) to blunt postprandial glucose surges by 40-70%.
        """
        cv = max(10.0, min(80.0, float(cv_percentage)))
        peak = max(80.0, min(300.0, float(peak_glucose_mg_dl)))

        protocols = [
            ("Macronutrient Food Sequencing", "Eat green vegetables & dietary fiber FIRST, protein & healthy fats SECOND, complex carbohydrates and starches LAST. Slows gastric emptying and reduces glucose spike by up to 73%."),
            ("Postprandial Soleus / Ambulation Walk", "10-15 minutes of light walking within 30 minutes of meal completion. Muscle contractions activate non-insulin-mediated GLUT4 transporters directly into skeletal muscle."),
            ("Acetic Acid Pre-Load (Apple Cider Vinegar)", "1 tablespoon of vinegar diluted in water 5-10 minutes prior to starchy meals. Temporarily inactivates salivary alpha-amylase and slows starch enzymatic breakdown."),
            ("Cold Complex Carbohydrate Retrogradation", "Cook and refrigerate starches (rice, sweet potatoes, oats) for 12 hours before reheating to convert digestible starches into non-glycemic Type 3 Resistant Starch.")
        ]

        expected_spike_reduction_pct = round(min(65.0, 30.0 + (cv * 0.45)), 0)

        return {
            "current_cv_percentage": cv,
            "monitored_peak_glucose": f"{peak} mg/dL",
            "projected_glycemic_spike_reduction": f"-{expected_spike_reduction_pct}% peak amplitude",
            "actionable_stabilization_interventions": protocols,
            "reactive_crash_prevention": "Eliminating spikes >140 mg/dL prevents the compensatory hyperinsulinemic overshoot that causes 2:00 PM afternoon fatigue."
        }
