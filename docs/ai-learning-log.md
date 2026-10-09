# AI Learning Log

## Fellow: Ina Hadiza Isah
### Interaction #1 — Unittest assertion for exceptions and dictionary state mutation

- **Problem:** I needed to understand how `self.assertRaises(ValueError)` works in Python `unittest` when testing invalid ticket status transitions, and how dictionaries pass by reference during workflow updates.
- **My initial understanding:** I thought `assertRaises` was called like a standard function with arguments, but it threw a syntax error or executed the function too early.
- **Prompt to AI:** "Explain self.assertRaises with a 5-line example unrelated to CampusFlow, using a context manager. Then quiz me."
- **Useful AI guidance:** AI explained that `with self.assertRaises(Exception):` acts as a context manager that catches the exception raised inside the indented block rather than letting the test crash.
- **My independent experiment/test:** I ran `python3 -m unittest discover -s tests -v` on `test_unassigned_cannot_move_to_in_progress` to confirm that an unassigned ticket attempting to move to `in_progress` properly triggers a `ValueError` without stopping test execution.
- **Verification source/result:** `Ran 8 tests in 0.001s ... OK`
- **Decision:** Accepted and implemented across all negative validation cases in `tests/test_workflow.py`.
- **Related file/commit:** `tests/test_workflow.py`, branch `feat/2-status-workflow`
- **What I can now explain without AI:** How context managers trap expected runtime exceptions in automated testing suites so edge cases can be verified without breaking test execution.
