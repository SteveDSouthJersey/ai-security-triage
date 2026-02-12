AI Security Triage – Team Walkthrough
Objective

Demonstrate a structured, explainable vulnerability triage pipeline that:

- Merges asset context with vulnerability findings

- Applies deterministic risk scoring

- Categorizes risk type

- Flags escalation scenarios

- Outputs prioritized remediation guidance

1. Architecture Overview

Data Sources

- data/assets.csv

- data/vulnerabilities.csv

Processing Flow:

- Ingest data

- Merge asset + vulnerability context

- Apply risk scoring model

- Assign risk level

- Categorize risk

- Apply escalation logic

- Output prioritized results

2. Scoring Model Explanation

Risk Score Formula:

(severity_cvss × exploitability)
+ (business_criticality × data_sensitivity)
+ exposure_modifier


Design Principles:

- Deterministic

- Explainable

- Modular

- No black-box logic

3. Risk Tier Mapping
Score	Risk Level
≥ 75	Critical
≥ 50	High
≥ 25	Medium
< 25	Low
4. Risk Categorization

Rule-based classification:

- Critical Infrastructure

- Network Exposure

- Exploitable Vulnerability

- High Business Impact

- General Risk

Purpose:

- Improve interpretability

- Support remediation prioritization

5. Escalation Logic

Escalation triggers when:

- Risk level is Critical

- High risk on external asset

- Business criticality ≥ 8

- Exploitability ≥ 8

Outputs:

- escalation_flag

- escalation_reason

6. Live Demo Steps

Open input files in data/

Explain scoring model in scoring.py

Run:

python src/triage.py


Open output/results.csv

Review:

- Risk score

- Risk level

- Risk category

- Escalation flag

- Escalation reason

7. Future Enhancements

- Docker packaging

- REST API interface

- Dashboard visualization

- Configurable scoring weights

- CI/CD integration

- Closing Message

This project demonstrates a modular, explainable, and extensible vulnerability triage framework suitable for enterprise environments.
