"""AXEZENT A-Z: deterministic cross-domain discovery candidate index.

Shawn Calvin Snelling — 2026-11-12

Not an autonomous scientific discovery system or physical predictive engine.
Reports hypotheses and test obligations from an explicitly supplied topic catalog.
Uses Python standard library only.
"""
from __future__ import annotations
import argparse
import csv
import json
from pathlib import Path

HERE=Path(__file__).resolve().parent
TOPICS=HERE / "topic_inventory_curated.csv"

CANDIDATES=[
 {"id":"AZ-STR-001","title":"Density-matched gyroid stress concentration comparison",
  "fields":("geometry","fracture mechanics","additive manufacturing"),
  "question":"Does the ray-phase correction reduce peak stress at equal manufactured material mass?",
  "approach":"Mesh convergence, measured polymer properties, calibrated FEA, replicate compression",
  "negative_control":"Uncorrected cube at equal solid volume and print orientation",
  "primary_metric":"Peak stress and absorbed energy per mass with uncertainty intervals",
  "risk":"HIGH","status":"HYPOTHESIS","feasibility":4,"falsifiability":5},
 {"id":"AZ-OPT-001","title":"Sample-pair cross-ratio calibration of optical chirality",
  "fields":("photonics","nanotechnology","measurement science","statistics"),
  "question":"Does the modeled estimator remain unbiased under measured instrument drift?",
  "approach":"Paired handedness, circular polarizations, randomized measurement order, blanks",
  "negative_control":"Sample-specific polarization-dependent gains and additive backgrounds",
  "primary_metric":"Recovered chirality bias and 95% confidence interval",
  "risk":"HIGH","status":"SIMULATED","feasibility":4,"falsifiability":5},
 {"id":"AZ-SEN-001","title":"Drift-aware weak-signal sensor benchmark",
  "fields":("photonics","signal processing","Bayesian inference"),
  "question":"Can calibrated detection reduce false positives under preregistered drift patterns?",
  "approach":"Held-out noise sets, blind labels, reference sensor and calibration curve",
  "negative_control":"Randomized labels and intentionally shifted sensor response",
  "primary_metric":"False-alarm rate at fixed recall with confidence intervals",
  "risk":"MEDIUM","status":"HYPOTHESIS","feasibility":5,"falsifiability":5},
 {"id":"AZ-MAT-001","title":"Distinguishing polymer recovery from sensor baseline drift",
  "fields":("material science","embedded sensors","statistics"),
  "question":"Are mechanical properties restored, or only sensor baselines?",
  "approach":"Repeated fracture and load tests combined with blinded instrument calibration",
  "negative_control":"Unhealed specimens with reset sensor calibration",
  "primary_metric":"Recovered load capacity versus baseline drift",
  "risk":"HIGH","status":"HYPOTHESIS","feasibility":3,"falsifiability":5},
 {"id":"AZ-COM-001","title":"Sparse addressing for adaptive 3D defect simulation",
  "fields":("integer mathematics","sparse algorithms","structural topology"),
  "question":"Can collision-free logical addresses improve traceability of adaptive mesh simulations?",
  "approach":"Exact 64-bit encoding and decoding, sparse allocations, reproducible hash receipts",
  "negative_control":"Naive indexing with deliberate collisions and overflow cases",
  "primary_metric":"Collision count, memory footprint, correct index recovery",
  "risk":"LOW","status":"VERIFIED_FINITE","feasibility":5,"falsifiability":5},
]

def read_topics(filename=TOPICS):
    with Path(filename).open(newline="",encoding="utf-8") as h:
        rows=list(csv.DictReader(h))
    cleaned={row["topic"].strip().lower() for row in rows if row.get("topic","").strip()}
    return cleaned


def candidates(topics=None):
    topics=read_topics() if topics is None else {t.strip().lower() for t in topics}
    found=[]
    for entry in CANDIDATES:
        missing=sorted(set(entry["fields"])-topics)
        out=dict(entry)
        out["missing_fields"]=missing
        out["ready_for_formulation"]=not bool(missing)
        out["priority_score"]=entry["feasibility"]+entry["falsifiability"]-len(missing)*2
        out["evidence_label"]=entry["status"]
        found.append(out)
    return sorted(found,key=lambda c:(-c["priority_score"],c["id"]))


def audit_registry(entries):
    ids=set()
    for item in entries:
        assert item["id"] not in ids
        ids.add(item["id"])
        assert item["status"] in {"PROVED","VERIFIED_FINITE","SIMULATED","CONDITIONAL","HYPOTHESIS","OPEN"}
        for field in ("question","approach","negative_control","primary_metric","risk"):
            assert item[field].strip(), (item["id"],field)
        assert 1<=item["feasibility"]<=5
        assert 1<=item["falsifiability"]<=5
    return True


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--topics",type=Path,default=TOPICS)
    parser.add_argument("--output",type=Path,default=None)
    args=parser.parse_args()
    audit_registry(CANDIDATES)
    result={"author":"Shawn Calvin Snelling","research_status":"HYPOTHESIS_GENERATOR_NOT_AUTONOMOUS_DISCOVERY",
            "topic_count":len(read_topics(args.topics)),
            "candidate_count":len(CANDIDATES),
            "candidates":candidates(read_topics(args.topics))}
    rendered=json.dumps(result,indent=2,ensure_ascii=False)+"\n"
    if args.output:
        args.output.parent.mkdir(parents=True,exist_ok=True)
        args.output.write_text(rendered,encoding="utf-8")
    else:
        print(rendered,end="")


if __name__=="__main__":
    main()
