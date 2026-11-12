#!/usr/bin/env python3
"""Losslessly reconstruct public-site assets from GitHub-sized chunks.

All output hashes are verified against the project source files recorded in
`data/asset-parts-manifest.json`. No third-party downloads or credentials needed.
"""
from __future__ import annotations
import gzip
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "data" / "asset-parts-manifest.json"

def reassemble() -> None:
    spec = json.loads(MANIFEST.read_text(encoding="utf-8"))
    for relpath, info in spec.items():
        payload = b"".join((ROOT / part).read_bytes() for part in info["parts"])
        if len(payload) != info["stored_size"]:
            raise ValueError(f"Unexpected packed size for {relpath}")
        data = gzip.decompress(payload) if info["compression"] == "gzip" else payload
        digest = hashlib.sha256(data).hexdigest()
        if len(data) != info["source_size"] or digest != info["source_sha256"]:
            raise ValueError(f"Source hash/length mismatch for {relpath}")
        output = ROOT / relpath
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_bytes(data)
        print(f"PASS {relpath}: {len(data):,} bytes; SHA256 {digest}")

if __name__ == "__main__":
    reassemble()
