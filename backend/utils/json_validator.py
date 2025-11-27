# backend/utils/json_validator.py
import json
import re

def safe_parse_router_json(text: str):
    """
    Attempts to extract a JSON object from a model's text and parse it.
    Returns dict or None.
    """
    # Try to find the first { ... } block
    m = re.search(r"\{.*\}", text, re.S)
    if not m:
        return None
    try:
        obj_text = m.group(0)
        # Defensive cleanup: remove trailing commas
        obj_text = re.sub(r",\s*}", "}", obj_text)
        obj_text = re.sub(r",\s*\]", "]", obj_text)
        parsed = json.loads(obj_text)
        return parsed
    except Exception:
        try:
            # As a last resort, eval in safe mode (not recommended) - skip for safety
            return None
        except Exception:
            return None







# import json
#
# def safe_parse_json(text: str):
#     try:
#         return json.loads(text), None
#     except json.JSONDecodeError as e:
#         return None, str(e)
