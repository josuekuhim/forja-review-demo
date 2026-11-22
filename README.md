# forja-review demo

A sandbox repository for forja-review, a GitHub App that reviews pull requests in Portuguese with a 0.5B model post-trained on real bug fixes.

The open pull request adds code with **8 planted bugs** (SQL injection, an unclosed file, division by zero/empty list, an off-by-one in pagination, ...). The answer key lives in forja-review's `examples/gabarito-bugs-plantados.json`.
