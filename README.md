# Introduction to Design Patterns with Python — Source Code

*For further enquiry please contact Akin Kaldiroglu at akin@kaldiroglu.dev*

**Created:** 2026-06-03
**Project:** Companion source code for the course *Introduction to Design Patterns with Python* — the Python port of the Java edition. It backs the slides with runnable examples.

## Expected benefits

- A small, runnable codebase students can read alongside the video.
- The course examples in real, idiomatic Python:
  1. **Three "before" smells** — a nested `if-elif-else` access check (`complexifs`), a factory-heavy object graph (`complexobject`), and telescoping constructors (`db`).
  2. **The Proxy pattern** — the Citizen / Prime Minister exercise, in three refactoring stages (the *after* picture).

## Functional properties

This is a faithful, idiomatic-Python port of the author's Java repo. It covers **all four**
examples from the Java source — three "problem" (before) examples and the Proxy pattern in
three stages.

- **`problems.complexifs`** — `User` (many fields) + `UserProcessor.process_user`, a deeply nested `if` tree returning access-code strings (e.g. `FULL_ACCESS_GRANTED`). Kept deliberately as the Big Ball of Mud the course teaches you to refactor.
- **`problems.complexobject`** — a `UserService` that assembles a `User` graph from a `NewUserRequest` through several factories. The factories are deliberately left as **stubs that return `None`** — the "complex object construction" smell that motivates the **Factory / Builder** patterns.
- **`problems.db`** — `DatabaseConnection`, demonstrating the **telescoping constructor** smell that motivates the **Builder** pattern. `demo.run()` mirrors the Java `db/Main`'s four connection profiles.
- **`proxy.pm`** — the Gang of Four **Proxy** pattern, in three stages (`pm1`/`pm2`/`pm3`):
  - **pm1 (Solution 1):** `Citizen` → concrete `PM` (low cohesion — the PM sorts out *and* resolves).
  - **pm2 (Solution 2):** `Citizen` → `Proxy` → `PM` (the proxy sorts out and delegates).
  - **pm3 (Solution 3):** `PM` is an **abstract base class** (the *Subject*); `RealPM` and `ProxyPM` implement it; `PMSecretary` is a **factory** (`get_me_pm()`) serving a `ProxyPM` typed as `PM`; `Citizen` depends only on `PM`.

## Architectural approach

- Idiomatic Python: `@dataclass` data objects, **snake_case** methods (`find_job`, `tell_problem`), `abc.ABC` for the Solution-3 interface, plain public attributes (no getters/setters).
- The package tree honours the house root namespace **`dev.kaldiroglu`** — code lives under `src/dev/kaldiroglu/dp/intro/...`, so the import path mirrors the Java packages exactly (`dev.kaldiroglu.dp.intro.proxy.pm.pm1`).
- Java JavaBeans (private fields + getters/setters) become dataclass attributes; boxed `Long`/nullable `String` become `int | None` / `str | None`. Deliberately-incomplete stubs in the Java source are preserved as stubs, not "fixed".

## Layout

```
IntroductionToDesignPatternsWithPython/
└── src/dev/kaldiroglu/dp/intro/
    ├── main.py                          (runs the pm1/pm2/pm3 + db demos)
    ├── problems/
    │   ├── complexifs/   { user.py, user_processor.py }
    │   ├── complexobject/ { new_user_request.py, user_service.py,
    │   │                     user/ { entities.py, factories.py } }
    │   └── db/           { database_connection.py, demo.py }
    └── proxy/pm/         { pm1.py, pm2.py, pm3.py }
```

> The `complexobject` example has no `Main` in the Java repo, so (like the original) it is import-only — it demonstrates structure rather than running output.

This is a read-along companion to the course: there is no test project (the Java original has none either). The behaviour is shown by running the demos.

## Run it with

```sh
# from the repo root
cd src
python3 -m dev.kaldiroglu.dp.intro.main
```
