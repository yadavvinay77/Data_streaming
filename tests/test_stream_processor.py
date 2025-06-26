# tests/test_stream_processor.py
from datetime import datetime
from streaming_app.stream_processor import analyze_line

def test_long_word_extraction():
    # Given
    line = "Testing longerword and short"
    timestamp = datetime(2025, 1, 1, 0, 0, 0)

    # When
    result = analyze_line(1, line, timestamp)

    # Then
    assert result["batch"] == 1

    # Words ≥5 letters: “Testing”, “longerword”, “short”
    expected = {"Testing", "longerword", "short"}
    assert result["long_words"] == 3
    assert set(result["long_words_list"]) == expected

    # No digits in this line
    assert result["digits"] == 0

    # Timestamp formatting
    assert result["time"] == "2025-01-01 00:00:00"
