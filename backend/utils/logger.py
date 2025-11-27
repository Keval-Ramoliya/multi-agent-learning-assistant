import json
from datetime import datetime
from pathlib import Path

# Correct path to observability/agent_logs.json
LOG_FILE = Path(__file__).resolve().parents[1] / "observability" / "agent_logs.json"

def log_event(event_type, data):
    log_entry = {
        "timestamp": datetime.now().isoformat(),
        "event_type": event_type,
        "data": data
    }

    try:
        # If file does not exist or is empty → start with empty list
        if not LOG_FILE.exists() or LOG_FILE.read_text().strip() == "":
            existing = []
        else:
            try:
                existing = json.loads(LOG_FILE.read_text())
            except json.JSONDecodeError:
                # File exists but content is invalid → reset it
                existing = []

        # Append new log entry
        existing.append(log_entry)

        # Write back
        LOG_FILE.write_text(json.dumps(existing, indent=2))

    except Exception as e:
        print("Logging error:", e)
