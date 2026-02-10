"""
scoring.py
- Computes a single risk score per vulnerability
- Buckets scores into clear risk levels
"""

from __future__ import annotations
import pandas as pd


def exposure_modifier(exposure: str) -> int:
    """
    External assets carry higher risk than internal ones.
    """
    exposure = str(exposure).lower().strip()
    if exposure == "external":
        return 5
    return 0


def calculate_risk_score(row: pd.Series) -> int:
    """
    Explainable risk scoring formula.

    Components:
    - Technical risk: severity_cvss × exploitability
    - Business impact: business_criticality × data_sensitivity
    - Exposure bonus: external-facing assets
    """

    technical_risk = row["severity_cvss"] * row["exploitability"]
    business_impact = row["business_criticality"] * row["data_sensitivity"]
    exposure_bonus = exposure_modifier(row["exposure"])

    total_score = technical_risk + business_impact + exposure_bonus

    return int(round(total_score))


def risk_level(score: int) -> str:
    """
    Convert numeric score into human-readable risk tiers.
    """
    if score >= 75:
        return "Critical"
    if score >= 50:
        return "High"
    if score >= 25:
        return "Medium"
    return "Low"


def score_vulnerabilities(df: pd.DataFrame) -> pd.DataFrame:
    """
    Adds risk_score and risk_level columns to a merged asset/vuln dataframe.
    """
    df = df.copy()

    df["risk_score"] = df.apply(calculate_risk_score, axis=1)
    df["risk_level"] = df["risk_score"].apply(risk_level)

    return df

