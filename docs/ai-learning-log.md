# AI Learning Log

## Fellow: Ina Hadiza Isah

### Interaction #1 — Unittest assertion for exceptions and context managers
- **Problem:** I needed to understand how `self.assertRaises(ValueError)` works in Python `unittest` when testing invalid ticket status transitions.
- **My initial understanding:** I thought `assertRaises` was called like a standard function with arguments, but executing it directly caused the exception to crash the test.
- **Prompt to AI:** "Explain self.assertRaises with a 5-line example unrelated to CampusFlow, using a context manager. Then quiz me."
- **Useful AI guidance:** AI explained that `with self.assertRaises(Exception):` acts as a context manager that traps exceptions raised inside the indented block without crashing the suite.
- **My independent experiment/test:** I ran `python3 -m unittest discover -s tests -v` on `test_unassigned_cannot_move_to_in_progress` to confirm an unassigned ticket attempting to move to `in_progress` properly triggers a `ValueError`.
- **Verification source/result:** `Ran 11 tests in 0.007s ... OK`
- **Decision:** Accepted and implemented across all negative validation cases in `tests/test_workflow.py`.
- **Related file/commit:** `tests/test_workflow.py`, branch `feat/2-status-workflow`
- **What I can now explain without AI:** How context managers trap expected runtime exceptions in automated testing suites so edge cases can be verified cleanly.

---

### Interaction #2 — Sorting multi-key tuples in Python with `lambda`
- **Problem:** I needed to sort the work queue by priority (`critical` -> `high` -> `medium` -> `low`) and break priority ties using the numeric ticket ID (`T001` before `T002`).
- **My initial understanding:** I knew `sorted()` existed, but I wasn't sure how to map text priorities to numeric weights or sort by two criteria at once.
- **Prompt to AI:** "How does Python sort a list of dictionaries by two keys (a mapped string priority and a string ID) using a key function?"
- **Useful AI guidance:** AI showed how mapping string priorities to numbers (`{"critical": 1, "high": 2, ...}`) allows returning a tuple `(priority_weight, ticket_id)` inside a `lambda` key function.
- **My independent experiment/test:** Created `test_work_queue_sorting_by_priority_and_id` where `T003` (high) and `T004` (high) were tested to verify that `T003` comes first based on ID ordering.
- **Verification source/result:** Test passed with correct ID ordering `["T002", "T003", "T004"]`.
- **Decision:** Accepted and applied in `campusflow/workflow.py` under `get_work_queue()`.
- **Related file/commit:** `campusflow/workflow.py`, branch `feat/2-status-workflow`
- **What I can now explain without AI:** How tuple comparison in Python (`(a, b) < (c, d)`) compares the first element first, and only uses the second element to break ties.

---

### Interaction #3 — Handling JSON decoding errors without losing data
- **Problem:** I needed to make sure malformed or corrupted JSON files produce a clear error rather than crashing the program or overwriting existing data.
- **My initial understanding:** I thought `json.load()` would return `None` or an empty list if a file had invalid syntax.
- **Prompt to AI:** "What specific exception does json.load() raise when a file contains bad JSON, and how should I catch it?"
- **Useful AI guidance:** AI clarified that `json.load()` raises `json.JSONDecodeError`, which can be caught and re-raised as a user-friendly `ValueError`.
- **My independent experiment/test:** Built `test_corrupted_json_raises_value_error` in `tests/test_storage.py` that writes invalid syntax (`"{ invalid...`) to a temp file and asserts that `load_tickets()` raises `ValueError`.
- **Verification source/result:** Test passed successfully in `test_storage.py`.
- **Decision:** Accepted and implemented in `campusflow/storage.py`.
- **Related file/commit:** `campusflow/storage.py`, branch `feat/2-status-workflow`
- **What I can now explain without AI:** How to wrap low-level library exceptions like `json.JSONDecodeError` into domain-specific exceptions to protect application state.
