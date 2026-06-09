"""Telecharge (ou rafraichit) les jeux de donnees utilises dans les modules.

A executer une seule fois, en local. En Colab, ce n'est pas necessaire :
les notebooks tombent automatiquement sur l'URL si le cache local est absent.
"""

from __future__ import annotations

import hashlib
import sys
import urllib.request
from pathlib import Path

HERE = Path(__file__).resolve().parent

SOURCES: dict[str, str] = {
    "gapminder.tsv": (
        "https://raw.githubusercontent.com/jennybc/gapminder/master/"
        "inst/extdata/gapminder.tsv"
    ),
    "pima_indians_diabetes.csv": (
        "https://raw.githubusercontent.com/jbrownlee/Datasets/master/"
        "pima-indians-diabetes.data.csv"
    ),
    "heart_uci.csv": (
        "https://raw.githubusercontent.com/sharmaroshan/Heart-UCI-Dataset/"
        "master/heart.csv"
    ),
    "framingham.csv": (
        "https://raw.githubusercontent.com/GauravPadawe/"
        "Framingham-Heart-Study/master/framingham.csv"
    ),
}


def fetch(name: str, url: str, force: bool = False) -> Path:
    dest = HERE / name
    if dest.exists() and not force:
        return dest
    print(f"  telechargement de {name} ...", flush=True)
    with urllib.request.urlopen(url, timeout=30) as r:
        data = r.read()
    dest.write_bytes(data)
    digest = hashlib.sha256(data).hexdigest()[:16]
    print(f"    {len(data):>10d} octets, sha256[:16]={digest}")
    return dest


def main() -> int:
    print(f"Dossier cache : {HERE}")
    ok = 0
    for name, url in SOURCES.items():
        try:
            fetch(name, url)
            ok += 1
        except Exception as exc:  # noqa: BLE001
            print(f"  ECHEC {name}: {exc}")
    print(f"Termine. {ok}/{len(SOURCES)} jeux de donnees disponibles.")
    return 0 if ok == len(SOURCES) else 1


if __name__ == "__main__":
    sys.exit(main())
