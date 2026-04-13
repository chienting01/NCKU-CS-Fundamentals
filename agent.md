# AGENTS.md

## Project Name
NCKU-CS-Fundamentals

## Project Goal
This repository is a structured long-term learning system for computer science and analytics fundamentals.

It is not just a file dump.
It should preserve:
1. concept notes
2. runnable examples
3. exercises
4. mini-project artifacts
5. clean Git history

## Main Learning Areas
- 01_computer-organization
- 02_c-language
- 03_data-structures
- 04_algorithms
- 05_sql
- 06_power-bi
- 07_python
- 08_industrial-engineering
- 09_kaggle
- 99_git-version-control

## Current Priority
Current top priorities:
1. 02_c-language
2. 99_git-version-control
3. 01_computer-organization

## Current Repository State
- The top-level folder skeleton already exists.
- `02_c-language/` already exists with:
  - `basics/`
  - `notes/`
  - `exercises/`
- The hello lesson already exists under:
  - `02_c-language/basics/hello/hello.c`
- `99_git-version-control` should be kept.
- Do not create `10_github`.
- Compiled binaries should not remain in the repository.

## Repository Rules
- Keep the top-level structure stable unless explicitly requested.
- Do not rename top-level folders unless explicitly requested.
- Do not place source files randomly in the repo root.
- Prefer Markdown for notes and documentation.
- Respect `.gitignore`.
- Never keep compiled binaries such as `hello`, `a.out`, `.out`, or `.exe` in the repository.

## C Language Module Rules
Inside `02_c-language/`, use this structure:
- `notes/` for concept notes
- `basics/` for small runnable examples
- `exercises/` for practice problems

For a new beginner lesson, prefer:
- `02_c-language/basics/<topic>/main.c`
- `02_c-language/basics/<topic>/README.md`
- `02_c-language/notes/<nn>-<topic>.md`

## Teaching Rules
Assume the learner is a beginner in C.
Use incremental scope.
Prefer simple and readable examples.
Do not jump to advanced abstractions too early.
Do not over-engineer.
Do not introduce pointers, structs, dynamic memory, or file I/O unless the task explicitly asks for them.

## Git Rules
- Keep commits scoped to the current lesson.
- Avoid unrelated refactors.
- Never run destructive Git commands unless explicitly requested.
- Prefer clear commit messages.

## Execution Rules
Before making large edits:
1. summarize the plan
2. list the target files
3. keep the scope small
4. avoid unrelated changes

## Response Style
For implementation tasks:
1. summarize understanding
2. propose a short plan
3. list files to create or edit
4. make the smallest useful change
5. summarize what changed