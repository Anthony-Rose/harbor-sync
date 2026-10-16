"""harbor-sync: merge berth schedule CSVs into a weekly summary."""
import csv


def load_rows(path):
    with open(path, newline="") as f:
        return list(csv.DictReader(f))


def summarize(rows):
    return {"berths": len({r["berth"] for r in rows}), "arrivals": len(rows)}


if __name__ == "__main__":
    print(summarize(load_rows("sample.csv")))
