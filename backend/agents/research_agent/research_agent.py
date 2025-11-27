from google import genai
from backend.config.settings import GENAI_API_KEY
from .tutorial_finder import find_tutorials
from .github_explorer import find_github_repos
from .so_helper import stackoverflow_style_answer

client = genai.Client()


def handle_research(topic: str):
    tutorials = find_tutorials(topic)
    repos = find_github_repos(topic)
    so = stackoverflow_style_answer(topic)

    prompt = f"""
You are a research assistant. Summarize high-quality learning resources for:

Topic: {topic}

### 1. Summary
High-level overview.

### 2. Best Tutorials
{tutorials}

### 3. Best GitHub Repos
{repos}

### 4. StackOverflow Style Answers
{so}

### 5. Roadmap
Generate a learning roadmap from beginner to advanced.
"""

    res = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt
    )

    return res.text
