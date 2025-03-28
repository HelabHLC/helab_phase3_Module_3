
import json
import os

DATA_PATH = os.path.join(os.path.dirname(__file__), "../data/hlc_lab_full_reference.json")

with open(DATA_PATH, "r") as f:
    HLC_LAB_DATA = json.load(f)

def get_lab_from_hlc(hlc_code):
    return HLC_LAB_DATA.get(hlc_code)
