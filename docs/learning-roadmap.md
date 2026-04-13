# Learning Roadmap

## Purpose
This roadmap defines the medium-term study direction for the repository.

It is not the same as `docs/progress.md`.

- `docs/progress.md` = current execution status
- `docs/learning-roadmap.md` = planned learning path
- `docs/weekly-log/` = actual weekly review and reflection

This roadmap is designed for a five-day study rhythm each week.

---

## Overall Strategy
The learning order is not flat.
The project should prioritize foundational dependencies first.

### Foundation Layer
1. C language
2. Git / version control
3. computer organization

### Core CS Layer
4. data structures
5. algorithms

### Tooling / Analysis Layer
6. Python
7. SQL

### Applied Layer
8. industrial engineering
9. Kaggle
10. Power BI

This means the repo should spend more energy early on:
- building C fluency
- building clean Git habits
- understanding low-level machine concepts
- preparing for DS and algorithms

---

## Weekly Rhythm
Recommended five-day structure:

### Day 1
C language + Git discipline

### Day 2
Computer organization + C concept connection

### Day 3
Data structures + algorithms

### Day 4
Python + SQL

### Day 5
Repository review + rotation topic
(rotation topic = industrial engineering / Kaggle / Power BI / Git deepening)

---

## 4-Week Initial Plan

# Week 1
## Theme
Build the initial repository rhythm and lesson pattern.

## Goals
- turn the repo into an actual learning system
- create the first C lesson after hello
- start computer organization notes
- create early DS / algorithm foundations
- create a weekly review habit

## Day 1
C language: variables and data types  
Git focus: compile, test, remove binary, commit cleanly

Target outputs:
- `02_c-language/basics/variables/main.c`
- `02_c-language/basics/variables/README.md`
- `02_c-language/notes/02-variables-and-data-types.md`

## Day 2
Computer organization: binary and data representation  
C connection: relate data types to representation

Target outputs:
- `01_computer-organization/notes/01-binary-and-data-representation.md`

## Day 3
Data structures: what is a data structure  
Algorithms: what is time complexity

Target outputs:
- `03_data-structures/notes/01-what-is-a-data-structure.md`
- `04_algorithms/notes/01-time-complexity.md`

## Day 4
Python: basics  
SQL: select / from / where

Target outputs:
- `07_python/notes/01-python-basics.md`
- `07_python/basics/hello.py`
- `05_sql/notes/01-select-from-where.md`
- `05_sql/queries/basic-queries.sql`

## Day 5
Rotation topic: industrial engineering introduction  
Repo task: weekly review

Target outputs:
- `08_industrial-engineering/notes/01-what-is-ie.md`
- `docs/weekly-log/week-01.md`

---

# Week 2
## Theme
Input, output, and flow control foundations.

## Goals
- learn C input/output
- understand signed / unsigned and overflow
- begin array thinking
- continue Python and SQL basics
- start Kaggle conceptual orientation

## Day 1
C language: input and output with `printf` / `scanf`

Target outputs:
- `02_c-language/basics/input-output/main.c`
- `02_c-language/basics/input-output/README.md`
- `02_c-language/notes/03-input-and-output.md`

## Day 2
Computer organization: signed / unsigned / overflow

Target outputs:
- `01_computer-organization/notes/02-signed-unsigned-overflow.md`

## Day 3
Data structures: array  
Algorithms: iteration vs recursion

Target outputs:
- `03_data-structures/notes/02-array.md`
- `04_algorithms/notes/02-iteration-vs-recursion.md`

## Day 4
Python: conditionals  
SQL: order by / limit

Target outputs:
- `07_python/basics/conditionals/main.py`
- `07_python/notes/02-conditionals.md`
- `05_sql/notes/02-order-by-limit.md`

## Day 5
Rotation topic: Kaggle workflow  
Repo task: weekly review

Target outputs:
- `09_kaggle/notes/01-kaggle-workflow.md`
- `docs/weekly-log/week-02.md`

---

# Week 3
## Theme
Decision-making, CPU basics, and stack-level thinking.

## Goals
- learn if / else in C
- learn CPU basic architecture and instruction cycle
- understand stack conceptually
- continue Python loops and SQL aggregate basics
- start Power BI conceptual orientation

## Day 1
C language: if / else

Target outputs:
- `02_c-language/basics/if-else/main.c`
- `02_c-language/basics/if-else/README.md`
- `02_c-language/notes/04-if-else.md`

## Day 2
Computer organization:
- CPU basic architecture
- instruction cycle

Target outputs:
- `01_computer-organization/notes/03-cpu-basic-architecture.md`
- `01_computer-organization/notes/04-instruction-cycle.md`

## Day 3
Data structures: stack  
Algorithms: more time complexity examples

Target outputs:
- `03_data-structures/notes/03-stack.md`
- `04_algorithms/notes/03-complexity-examples.md`

## Day 4
Python: loops  
SQL: aggregate functions

Target outputs:
- `07_python/basics/loops/main.py`
- `07_python/notes/03-loops.md`
- `05_sql/notes/03-aggregate-functions.md`

## Day 5
Rotation topic: Power BI dashboard thinking  
Repo task: weekly review

Target outputs:
- `06_power-bi/notes/01-dashboard-thinking.md`
- `docs/weekly-log/week-03.md`

---

# Week 4
## Theme
Looping, memory thinking, and queue/search foundations.

## Goals
- learn loops in C
- build pre-pointer memory intuition
- learn queue concepts
- start searching basics
- strengthen Git learning notes

## Day 1
C language: loops

Target outputs:
- `02_c-language/basics/loops/main.c`
- `02_c-language/basics/loops/README.md`
- `02_c-language/notes/05-loops.md`

## Day 2
Computer organization: memory hierarchy

Target outputs:
- `01_computer-organization/notes/05-memory-hierarchy.md`

## Day 3
Data structures: queue  
Algorithms: searching basics

Target outputs:
- `03_data-structures/notes/04-queue.md`
- `04_algorithms/notes/04-searching-basics.md`

## Day 4
Python: functions  
SQL: group by / having

Target outputs:
- `07_python/basics/functions/main.py`
- `07_python/notes/04-functions.md`
- `05_sql/notes/04-group-by-having.md`

## Day 5
Rotation topic: Git deepening  
Repo task: weekly review

Target outputs:
- `99_git-version-control/notes/01-basic-git-flow.md`
- `99_git-version-control/notes/02-gitignore-and-binaries.md`
- `docs/weekly-log/week-04.md`

---

## Learning Design Rules
When extending the roadmap:
- do not add advanced topics too early
- keep dependency order clear
- ensure each week has visible repo outputs
- prefer fewer but finished lessons
- avoid planning far beyond the current level in excessive detail

---

## What Good Progress Looks Like
Good progress means:
- the C module becomes richer every week
- notes and runnable code grow together
- computer organization supports C understanding
- DS and algorithms start with conceptual clarity
- Python and SQL remain active but secondary
- weekly logs show actual evidence of learning

---

## Roadmap Extension After Week 4
After the first four weeks, the likely next stage is:

### C Language
- functions
- arrays
- strings
- modular thinking
- pointer preparation

### Computer Organization
- registers
- assembly basics
- branch / loop in assembly
- stack and procedure call concepts

### Data Structures
- linked lists
- stack implementation
- queue implementation

### Algorithms
- linear search
- binary search
- sorting basics

### Python / SQL
- functions
- data structures in Python
- joins in SQL
- grouped analysis

### Applied Topics
- Power BI data modeling
- Kaggle baseline workflow
- industrial engineering process analysis basics