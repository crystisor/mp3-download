# Gemini CLI System Rules: Clean Code Engine

## 1. Core Engineering Principles
* **SOLID Compliance:** Enforce SRP, Open/Closed, Liskov Substitution, Interface Segregation, and Dependency Inversion.
* **Anti-Smell Detection:** Eliminate Long Methods, God Objects, Duplicated Code, and Shotgun Surgery.
* **KISS & YAGNI:** Prioritize the simplest solution; no over-engineering or speculative features.

## 2. Architecture & Design
* **Clean Architecture:** Maintain strict separation between Domain, Use Cases, and Infrastructure layers.
* **Design Patterns:** Use Creational, Structural, and Behavioral patterns only where they reduce complexity.
* **Naming Conventions:** * **Variables/Functions:** camelCase; descriptive, intention-revealing names.
    * **Classes/Interfaces:** PascalCase; nouns for classes, adjectives/nouns for interfaces.
    * **Booleans:** Prefix with `is`, `has`, or `can`.

---

## 3. Optimized Prompt Injection
> **Instruction:** When generating or refactoring code, always apply the following condensed rule-set to ensure high-quality output:

# Clean Coding & Architecture Principles

This document explains core software design principles and guidelines used to build **clean, scalable, and maintainable systems**. It is intended to guide agents, developers, and reviewers when writing or evaluating code.

---

## SOLID
A set of five object-oriented design principles that make software easier to understand, extend, and maintain.

- **S – Single Responsibility Principle**  
  A module/class should have **one reason to change**. Each unit does one job and does it well.

- **O – Open/Closed Principle**  
  Software entities should be **open for extension but closed for modification**. Add behavior without changing existing code.

- **L – Liskov Substitution Principle**  
  Subtypes must be replaceable for their base types **without breaking correctness**.

- **I – Interface Segregation Principle**  
  Prefer **many small, specific interfaces** over one large, general-purpose interface.

- **D – Dependency Inversion Principle**  
  Depend on **abstractions, not concrete implementations**. High-level modules should not depend on low-level details.

---

## DRY (Don’t Repeat Yourself)
Every piece of knowledge or logic should have **a single, authoritative source**.

- Avoid duplicated logic, constants, validations, and queries
- Changes should happen in **one place only**

---

## KISS (Keep It Simple, Stupid)
Favor **simplicity over cleverness**.

- Simple logic > complex abstractions
- Readability and clarity are more important than being "smart"

---

## No Code Smells
Code smells are signs of deeper design problems.

Avoid:
- God objects
- Long methods
- Deep nesting
- Duplicate logic
- Tight coupling
- Magic numbers / strings

Clean code should feel **obvious, boring, and predictable**.

---

## Clean Architecture
An architectural approach focused on **separation of concerns** and **independence from frameworks**.

Core ideas:
- Business logic is independent of UI, database, and frameworks
- Dependencies point **inward**, toward the core domain

Typical layers:
- Domain (entities, business rules)
- Application (use cases)
- Interface adapters (controllers, presenters)
- Infrastructure (DB, APIs, frameworks)

---

## Descriptive Naming
Names should clearly express **intent and responsibility**.

- Functions describe actions: `calculateTotal()`, `fetchUserById()`
- Variables describe meaning, not type: `userCount` not `uc`
- Avoid abbreviations unless universally understood

Good names reduce the need for comments.

---

## Simple Logic
Logic should be:
- Easy to follow
- Linear when possible
- Free of unnecessary branching

Prefer:
- Early returns
- Small functions
- Clear conditions

Complexity should be pushed **downward or outward**, not concentrated.

---

## Decoupling
Components should have **minimal knowledge of each other**.

Achieved through:
- Interfaces
- Dependency injection
- Events / messaging

Decoupling enables:
- Easier testing
- Safer refactoring
- Independent evolution of modules

---

## Zero Redundancy
No duplicated:
- Logic
- Data transformations
- Validation rules
- Configuration values

Redundancy increases bugs and maintenance cost.

---

## Maintainable Structure
A codebase should be optimized for **change over time**.

Characteristics:
- Clear folder/module boundaries
- Predictable file locations
- Consistent patterns
- Minimal cross-dependencies

A maintainable system allows new features to be added **without fear**.

---

## Guiding Philosophy
> Code is read far more often than it is written.

Prioritize:
- Clarity over cleverness
- Simplicity over abstraction
- Explicitness over magic

This document should be treated as a **non-negotiable baseline** for all generated and human-written code.


