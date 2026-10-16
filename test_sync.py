from sync import summarize


def test_summarize():
    rows = [{"berth": "B1", "vessel": "Kestrel", "arrive": "2026-10-20"}]
    assert summarize(rows) == {"berths": 1, "arrivals": 1}
