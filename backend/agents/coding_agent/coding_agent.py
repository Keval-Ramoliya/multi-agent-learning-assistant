from backend.agents.coding_agent.code_explainer import explain_code
from backend.agents.coding_agent.error_debugger import debug_code
from backend.agents.coding_agent.code_optimizer import optimize_code
from backend.agents.coding_agent.testcase_generator import generate_testcases

def handle_coding_task(message: str, intent: str):
    if intent == "explain":
        return explain_code(message)

    if intent == "debug":
        return debug_code(message)

    if intent == "optimize":
        return optimize_code(message)

    if intent == "testcase":
        return generate_testcases(message)

    return "I received your coding request but could not detect intent."



# """
# Coding Problem Solver Agent entry point.
# """
#
# from .code_explainer import explain_code
# from .error_debugger import debug_code_error
# from .code_optimizer import optimize_code
# from .testcase_generator import generate_test_cases_and_complexity
#
#
# def handle_coding_query(message: str, session_id: str | None = None) -> str:
#     # TODO: Replace with LLM/ADK-based reasoning and tool usage.
#     # For now, just a simple placeholder dispatch.
#     msg_lower = message.lower()
#
#     if "explain" in msg_lower:
#         return explain_code(message)
#     if "optimize" in msg_lower or "optimized" in msg_lower:
#         return optimize_code(message)
#     if "test case" in msg_lower or "testcase" in msg_lower:
#         return generate_test_cases_and_complexity(message)
#     if "error" in msg_lower or "bug" in msg_lower:
#         return debug_code_error(message)
#
#     # Default to code explanation
#     return explain_code(message)
