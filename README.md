# Urban Grocers App – Kit Creation
### My very first automation project ever – TripleTen Sprint 7

![Python](https://img.shields.io/badge/Python-3.11%2B-blue)
![Pytest](https://img.shields.io/badge/Pytest-9.0%2B-blue)
![Coverage](https://img.shields.io/badge/Coverage-100%25-brightgreen)
![Tests](https://img.shields.io/badge/Tests-10/10%20Passed-success)

Hey there! I'm Jerry (jerryfinol17) and this repo is literally **the first time I ever wrote automated tests in my life**.

Back in July, during Sprint 7 of the TripleTen QA bootcamp, I had to automate the validation of the `POST /api/v1/kits` endpoint. The task seemed simple: test all the rules for the `name` field (length, special chars, numbers, empty values, etc.).

Plot twist: the backend they gave us was intentionally super permissive. Most "negative" cases that should return 400 actually create the kit with a happy 201. That’s by design — they wanted us to learn how to deal with unexpected API behavior.

### What this tiny project taught me (and I still use every day)
- First time using `requests` + `pytest`
- How to separate configuration, data, and helpers
- Never trust only the status code — always check the response body
- A failing test isn’t always your fault
- Refactoring old code is a superpower

A few months later, I came back to this repo just to translate the comments… and wow. What a beautiful mess it was!  
So I gave it a gentle refactor: moved tests into a `tests/` folder, cleaned up helpers, shortened names, and added proper coverage.  
Result? 10 tests, 100% coverage, runs in ~10 seconds, and now looks like something I wouldn’t be ashamed to show in an interview.

### Current status
- 10 automated tests
- 100% test coverage
- Clean, readable structure
- Still works against TripleTen’s private server (when it’s not down )

### Final words
This was my absolute first step into automation. I’ve improved a lot since then, but I’m still learning every day.  
If you spot something that could be done better — please tell me! Feedback (even brutal) is more than welcome.

Thanks for stopping by, have an awesome day (or night), and keep growing!

Jerry  
2025
