from sync import summarize


def test_summarize():
    rows = [{"berth": "B1", "vessel": "Kestrel", "arrive": "2026-10-20"}]
    assert summarize(rows) == {"berths": 1, "arrivals": 1, "vessels": 1}


def test_summarize_multiple_vessels():
    rows = [
        {"berth": "B1", "vessel": "Kestrel", "arrive": "2026-10-20"},
        {"berth": "B2", "vessel": "Merlin", "arrive": "2026-10-21"},
        {"berth": "B1", "vessel": "Kestrel", "arrive": "2026-10-22"},
    ]
    assert summarize(rows) == {"berths": 2, "arrivals": 3, "vessels": 2}
