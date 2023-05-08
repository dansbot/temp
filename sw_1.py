from os.path import join

import wfdb

DATA_DIR = "data"
DATABASE = "mit-bih-arrhythmia-database-1.0.0"
record_num = "100"

rec_num = join(DATA_DIR, DATABASE, record_num)
print(rec_num)
record = wfdb.rdrecord(rec_num)
ann = wfdb.rdann(rec_num, "atr")

print(dir(ann))

# print(ann.symbol)
# print(ann.sample)
# print(wfdb.io.annotation.ann_label_table)
print(record.fs)
df = record.to_dataframe()
df.to_csv("test.csv")

# wfdb.plot_wfdb(
#     record=record,
#     annotation=ann,
#     plot_sym=True,
#     time_units="seconds",
#     title="MIT-BIH Record 100",
#     figsize=(10, 4),
#     ecg_grids="all",
# )
ann_labels = {}
for i, row in wfdb.io.annotation.ann_label_table.iterrows():
    ann_labels[row.symbol] = {"desc": row.description, "indices": []}
from pprint import pprint

for i, sym in enumerate(ann.symbol):
    ann_labels[sym]["indices"].append(ann.sample[i])
for k in ann_labels.keys():
    ann_labels[k]["indices"] = len(ann_labels[k]["indices"])

pprint(ann_labels)
