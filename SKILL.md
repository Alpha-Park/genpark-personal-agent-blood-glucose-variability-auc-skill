---
name: genpark-personal-agent-blood-glucose-variability-auc-skill
version: "1.0.0"
description: "Zero-dependency Continuous Glucose Monitoring (CGM) glycemic variability calculator, Mean Amplitude of Glycemic Excursions (MAGE) modeler, and postprandial iAUC stabilizer."
license: MIT
dependencies:
  - python>=3.10
  - mcp>=1.0.0
entrypoint: client.py
---

# Personal Agent Blood Glucose Variability AUC Skill

Designed for **OpenClaw**, **Hermes**, and autonomous personal AI agents to govern metabolic longevity, quantify glycemic volatility (%CV and MAGE) from continuous glucose monitors, and neutralize oxidative stress from postprandial glucose rollercoasters.

## Agent In-Context Capabilities

- **Clinical Glycemic Metrics**: Calculates Coefficient of Variation (%CV <= 36%), Mean Amplitude of Glycemic Excursions (MAGE), Time in Range (70-140 mg/dL), and incremental Area Under the Curve (iAUC).
- **Reactive Hypoglycemia Elimination**: Prevents the compensatory hyperinsulinemic overshoot that triggers postprandial brain fog and mid-afternoon cognitive fatigue.
- **Biomechanical GLUT4 Scheduling**: Prescribes 10-15 minute non-insulin-mediated ambulation and food sequencing (Fiber -> Protein -> Starch).

## Tools Summary

1. `calculate_cgm_glycemic_variability`: Computes %CV, MAGE, Time in Range %, and iAUC.
2. `prescribe_glycemic_stabilization_protocol`: Recommends meal sequencing, light ambulation, and acetic acid timing.
