import yaml

data = {
    "points_of_interest": {
        11 * 60 + 3: "normal_sinus_rhtyhm",
        25 * 60 + 13: "pvc",
        26 * 60 + 9: "apcs",
        27 * 60 + 55: "normal_sinus_rhythm",
    },
    "signal_quality": {"both_clean": {"episodes": 1, "duration": 30 * 60 + 6}},
    "rhythms": {
        "normal_sinus_rhythm": {"rate": "70-89", "episodes": 1, "duration": 30 * 60 + 6}
    },
    "supraventricular_ectopy": "33 isolated beats",
    "beats": {
        "normal": {"before_5am": 367, "after_5am": 1872},
        "apc": {"before_5am": 4, "after_5am": 29},
        "pvc": {"before_5am": 0, "after_5am": 1},
    },
    "medications": ["Aldomet", "Inderal"],
    "record": 100,
    "leads": ["MLII", "V5"],
    "sex": "male",
    "age": 69,
}

with open("example.yaml", "w") as f:
    yaml.dump(data, f)
