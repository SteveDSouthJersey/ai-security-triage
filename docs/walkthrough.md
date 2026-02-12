# AI Security Triage – Team Walkthrough

## Objective

Demonstrate a structured, explainable vulnerability triage pipeline that:

- Merges asset context with vulnerability findings
- Applies deterministic risk scoring
- Categorizes risk type
- Flags escalation scenarios
- Outputs prioritized remediation guidance

---

## 1. Architecture Overview

### Data Sources

- `data/assets.csv`
- `data/vulnerabilities.csv`

### Processing Flow

1. Ingest data
2. Merge asset + vulnerability context
3. Apply risk scoring model
4. Assign risk level
5. Categorize risk
6. Apply escalation logic
7. Output prioritized results

---

## 2. Scoring Model Explanation

### Risk Score Formula

(severity_cvss × exploitability)

(business_criticality × data_sensitivity)

exposure_modifier


### Design Principles

- Deterministic
- Explainable
- Modular
- No black-box logic

---

## 3. Risk Tier Mapping

| Score | Risk Level |
|-------|------------|
| ≥ 75  | Critical   |
| ≥ 50  | High       |
| ≥ 25  | Medium     |
| < 25  | Low        |

---

## 4. Risk Categorization

Rule-based classification:

- Critical Infrastructure
- Network Exposure
- Exploitable Vulnerability
- High Business Impact
- General Risk

Purpose:

- Improve interpretability
- Support remediation prioritization

---

## 5. Escalation Logic

Escalation triggers when:

- Risk level is Critical
- High risk on an external asset
- Business criticality ≥ 8
- Exploitability ≥ 8

Outputs:

- `escalation_flag`
- `escalation_reason`

---

## 6. Live Demo Steps

1. Open input files in `data/`
   - `assets.csv`
   - `vulnerabilities.csv`

2. Explain the scoring model in `src/scoring.py`
   - Highlight the risk formula
   - Emphasize deterministic logic

3. Run the triage engine:

   ```bash
   python src/triage.py

4. Open the generated output file:
   - output/results.csv

5. Walk through the key output columns
   - risk_score
   - risk_level
   - risk_category
   - escalation_flag
   - escalation_reason

## 7. Future enhancements

   - Docker packaging
   - REST API interface
   - Dashboard visualization
   - Configurable scoring weights
   - CI/CD integration

Closing Message:

This project demonstrates a modular, explainable, and extensible vulnerability triage framework suitable for enterprise environments.

