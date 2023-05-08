from glob import glob
from os.path import exists, isdir, join

DATA_DIR = "data"

records = set()
for fldr in glob(join(DATA_DIR, "*")):
    if not isdir(fldr):
        continue
    recs_fn = join(fldr, "RECORDS")
    if not exists(recs_fn):
        continue
    with open(recs_fn) as f:
        lines = f.readlines()
    recs = set([x.strip() for x in lines if x.strip()])
    p_n = len(records)
    records.update(recs)
    if p_n + len(recs) != len(records):
        print(f"duplicate records! {fldr}")
print(records)
print(len(records))
