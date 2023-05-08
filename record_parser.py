import re
from os.path import join
from typing import Dict, List

import yaml
from bs4 import BeautifulSoup

KEY_ORDER = [
    "record",
    "age",
    "sex",
    "leads",
    "medications",
    "beats",
    "rhythms",
    "signal_quality",
    "*",
    "points_of_interest",
]


def parse_record(text):
    soup = BeautifulSoup(text, "html.parser")
    record = {}

    # Record, leads, sex, age
    h2 = soup.find("h2")
    record["record"] = int(re.search(r"\d+", h2.text).group())
    record["age"] = int(re.search(r"age (\d+)", h2.text).group(1))
    record["sex"] = re.search(r"(male|female)", h2.text).group()
    record["leads"] = [
        lead.strip()
        for lead in re.search(r"\((.*?)\)", h2.text).group(1).split(";")[0].split(",")
    ]

    # Medications
    medications = soup.find("i", text="Medications:")
    if medications:
        medication_list = (
            medications.find_next("br").previous_sibling.strip().split(", ")
        )
        record["medications"] = medication_list

    # Beats
    beats_table = soup.find_all("table")[0]
    beats_rows = beats_table.find_all("tr")[1:]
    record["beats"] = {}
    for row in beats_rows:
        cells = row.find_all("td")
        beat_type = cells[0].text.lower()
        if beat_type == "total":
            continue
        record["beats"][beat_type] = {
            "before_5am": int(cells[1].text) if cells[1].text != "-" else 0,
            "after_5am": int(cells[2].text) if cells[2].text != "-" else 0,
        }

    # Rhythms
    rhythms_table = soup.find_all("table")[1]
    rhythms_rows = rhythms_table.find_all("tr")[1:]
    record["rhythms"] = {}
    for row in rhythms_rows:
        cells = row.find_all("td")
        rhythm_type = cells[0].text.lower().replace(" ", "_")
        record["rhythms"][rhythm_type] = {
            "rate": cells[1].text,
            "episodes": int(cells[2].text),
            "duration": int(cells[3].text.split(":")[0]) * 60
            + int(cells[3].text.split(":")[1]),
        }

    # Ectopy
    ectopy_paragraphs = []
    for p in beats_table.find_all_next("p"):
        if p == rhythms_table.find_previous("p"):
            break
        ectopy_paragraphs.append(p)

    for p in ectopy_paragraphs:
        ectopy_type = p.i.text.strip().lower().replace(" ", "_")
        ectopy_list = p.ul.li.text.strip()
        record[ectopy_type] = ectopy_list

    # Signal quality
    signal_quality_table = soup.find_all("table")[2]
    signal_quality_rows = signal_quality_table.find_all("tr")[1:]
    record["signal_quality"] = {}
    for row in signal_quality_rows:
        cells = row.find_all("td")
        signal_quality_type = cells[0].text.lower().replace(" ", "_")
        record["signal_quality"][signal_quality_type] = {
            "episodes": int(cells[1].text),
            "duration": int(cells[2].text.split(":")[0]) * 60
            + int(cells[2].text.split(":")[1]),
        }

    # Points of interest
    points_of_interest = soup.find("h3", text=re.compile(r"Points of interest:"))
    if points_of_interest:
        record["points_of_interest"] = {}
        links = points_of_interest.find_all_next("a")
        for link in links:
            time = link.text.split(":")
            time_seconds = int(time[0]) * 60 + int(time[1])
            description = link.next_sibling.strip()
            record["points_of_interest"][time_seconds] = description.lower().replace(
                " ", "_"
            )

    return record


def order_keys(record: Dict) -> Dict:
    poi = "points_of_interest"
    ordered_dict = {k: record[k] for k in KEY_ORDER if k in record and k != poi}
    for k, v in record.items():
        if k != poi and k not in ordered_dict:
            ordered_dict[k] = v
    if poi in record:
        ordered_dict[poi] = record[poi]
    return ordered_dict


def split_records(fn: str) -> List[str]:
    with open(fn) as f:
        s = f.read()

    records = s.split("<hr>")
    print(len(records))
    return records[1:]


def parse_records(fn: str, output_dir: str):
    records = split_records(fn)
    for record in records:
        data = parse_record(record)
        out_fn = join(output_dir, f"{data['record']}.yaml")
        with open(out_fn, "w") as f:
            yaml.dump(data, f, sort_keys=False)
        break


if __name__ == "__main__":
    fn = "data/mit-bih-arrhythmia-database-1.0.0/mitdbdir/records.htm"
    parse_records(fn, ".")

    # parsed_record = parse_record(text)
    # print(parsed_record)
