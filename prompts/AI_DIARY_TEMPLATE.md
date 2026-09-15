# AI Collaboration Diary

Ground rules (see also the README section "Working with AI assistants"):
- Never commit code you cannot explain.
- Verify AI output with a hand calculation, textbook case, or physical limit - then keep that check as a unit test.
- Log your AI use here honestly; the diary is part of the deliverable.

For each significant AI interaction, explain briefly and honestly:
1. What you asked the assistant and why.
2. The key suggestions you received.
3. What you accepted or rejected and why.
4. How you verified the result (tests, equations, spot checks).

Append entries by date, for example:

## 2025-09-09
Prompt: "Help me structure a normal-depth solver with Newton's method."
Assistant suggestion: "Use Manning equation and derivative for Newton update."
Decision: Accepted structure, rewrote code and added unit conversion tests.
Verification: Compared with a hand calc for a rectangular channel; added
`test_normal_depth_against_hand_calculation` to tests/.
