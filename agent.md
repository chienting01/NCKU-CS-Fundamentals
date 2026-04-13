# AGENTS.md

## Project Name
NCKU-CS-Fundamentals

## Project Mission
This repository is a structured long-term learning system for computer science, analytics, and engineering fundamentals.

It is not just a file dump.
It should preserve:
1. concept notes
2. runnable examples
3. exercises
4. mini-project artifacts
5. clean Git history
6. visible weekly learning progress

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

## Current Strategic Priority
Current top priorities:
1. 02_c-language
2. 99_git-version-control
3. 01_computer-organization
4. 03_data-structures
5. 04_algorithms

Python, SQL, Power BI, Industrial Engineering, and Kaggle should continue to progress, but they are currently secondary to the C / Git / Computer Organization foundation.

## Repository Principles
- Keep the top-level structure stable unless explicitly requested.
- Do not rename top-level folders unless explicitly requested.
- Keep `99_git-version-control`.
- Do not create `10_github`.
- Do not place source files randomly in the repository root.
- Notes and learning documents should be written in Markdown whenever possible.
- Respect `.gitignore`.
- Never keep compiled binaries or temporary outputs in the repository.

Examples of files that should not remain in the repo:
- `hello`
- `a.out`
- `*.out`
- `*.exe`
- object files
- temporary caches
- environment-specific junk files

## Learning System Design
Each topic area should aim to preserve three things:
1. what the concept means
2. how it is implemented or used
3. what was learned from doing it

This means the repository should gradually accumulate:
- notes
- runnable code
- exercises
- comparisons
- reflections
- weekly logs

## C Language Module Rules
Inside `02_c-language/`, use this structure:
- `notes/` for concept notes
- `basics/` for small runnable beginner examples
- `exercises/` for practice problems
- optional future folders such as `mini-projects/`, `debugging-notes/`, or `templates/` only when actually needed

For a new beginner lesson, prefer:
- `02_c-language/basics/<topic>/main.c`
- `02_c-language/basics/<topic>/README.md`
- `02_c-language/notes/<nn>-<topic>.md`

Examples:
- `02_c-language/basics/variables/main.c`
- `02_c-language/basics/variables/README.md`
- `02_c-language/notes/02-variables-and-data-types.md`

## Teaching Rules
Assume the learner is a beginner in C and is building fundamentals from zero.

Preferred style:
- simple
- incremental
- readable
- concrete
- beginner-safe

Do:
- prefer one concept at a time
- use small runnable examples
- explain why a file is created
- keep lesson scope tight
- connect concepts across topics when useful

Do not:
- over-engineer
- jump too early into advanced abstraction
- introduce unnecessary complexity
- refactor unrelated files
- silently change project structure
- mix too many concepts into one beginner lesson

## Computer Organization Rules
Inside `01_computer-organization/`, prefer:
- `notes/` for concept explanations
- optional `diagrams/` for figures
- optional `exercises/` for questions or practice
- optional `asm-labs/` only when actual assembly work starts

The early sequence should focus on:
1. binary and data representation
2. signed / unsigned
3. overflow
4. CPU basics
5. instruction cycle
6. memory hierarchy

## Data Structures Rules
Inside `03_data-structures/`, prefer:
- `notes/`
- `implementations/`
- `exercises/`
- `comparisons/`

Early focus:
- what a data structure is
- arrays
- linked lists
- stacks
- queues

## Algorithms Rules
Inside `04_algorithms/`, prefer:
- `notes/`
- `implementations/`
- `problem-solving/`
- `complexity-analysis/`

Early focus:
- time complexity
- space complexity
- iteration vs recursion
- searching
- sorting foundations

## Python Rules
Inside `07_python/`, prefer:
- `notes/`
- `basics/`
- `scripts/`
- `exercises/`

Python is currently secondary, but should still be documented in a structured way.

## SQL Rules
Inside `05_sql/`, prefer:
- `notes/`
- `queries/`
- `schemas/`
- `exercises/`

Early focus:
- SELECT
- FROM
- WHERE
- ORDER BY
- LIMIT
- aggregate functions
- GROUP BY

## Power BI / Kaggle / Industrial Engineering Rules
These areas should be organized clearly, but should grow only when there is actual content.
Avoid creating empty deep folder trees without immediate use.

## Git and Version Control Rules
- Keep commits scoped to the current lesson or current cleanup task.
- Avoid unrelated refactors.
- Never run destructive Git commands unless explicitly requested.
- Prefer clear commit messages.
- Do not commit compiled binaries.
- Do not commit environment-specific noise.
- When cleaning the repo, explain what is being removed and why.

Preferred commit message styles:
- `feat(c-language): add variables lesson`
- `docs(computer-organization): add binary representation note`
- `refactor(repo): clean lesson structure`
- `docs(progress): update week 1 status`

## Planning and Execution Rules
Before making meaningful edits:
1. summarize understanding
2. propose a short plan
3. list target files to create or edit
4. keep scope limited to the current task
5. avoid unrelated changes

For larger tasks:
- split work into steps
- state assumptions explicitly
- prefer the smallest useful change set
- avoid hidden broad refactors

## Progress Tracking Rules
This project uses separate planning and tracking files.

Use:
- `docs/progress.md` for current status
- `docs/learning-roadmap.md` for multi-week study plan
- `docs/weekly-log/` for weekly reviews

Do not overload `AGENTS.md` with rapidly changing daily status.
`AGENTS.md` should remain durable and stable.

## Response Format for Agent Work
When asked to perform a task, respond in this order:
1. brief understanding of the task
2. short plan
3. exact files to create or edit
4. implementation or proposed changes
5. concise summary of what changed

## Current Known Project State
At the time of this guidance:
- the top-level repository skeleton exists
- `02_c-language/` exists
- `02_c-language/basics/hello/hello.c` exists
- `02_c-language/notes/` exists
- `02_c-language/exercises/` exists
- `99_git-version-control` is the correct folder and must be kept
- `10_github` should not be created
- the repository is being developed as a learning system, not as a production software product

## Primary Goal for the Near Term
Build a strong and consistent foundation through:
- beginner C lessons
- Git hygiene
- computer organization notes
- early data structure / algorithm notes
- visible weekly progress in the repository