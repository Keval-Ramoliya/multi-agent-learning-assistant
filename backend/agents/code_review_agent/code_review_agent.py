from google import genai
from backend.config.settings import GENAI_API_KEY
from .code_quality_checker import analyze_quality
from .code_optimizer import optimize_code
from .code_security_analyzer import analyze_security

client = genai.Client()

def handle_code_review(message: str):
    code = message

    quality = analyze_quality(code)
    optimization = optimize_code(code)
    security = analyze_security(code)

    prompt = f"""
You are a senior software engineer. Provide a structured code review.

### 1. Summary
{quality['summary']}

### 2. Issues Found
{quality['issues']}

### 3. Line-by-line Analysis
{quality['line_review']}

### 4. Refactored Version
{optimization}

### 5. Why This Is Better
Explain improvements clearly.

### 6. Time & Space Complexity
Analyze algorithm complexity.

### 7. Security Issues
{security}
"""

    res = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt
    )

    return res.text
