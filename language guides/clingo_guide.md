# Introduction to Clingo and Answer Set Programming

## What is Clingo?

Clingo is a grounder and solver for Answer Set Programming (ASP) - a declarative programming paradigm that's particularly good at solving combinatorial optimization problems, knowledge representation, and constraint satisfaction problems.

## ASP Symbol Reference Table

| Symbol | Natural Language Translation | Example |
|--------|------------------------------|---------|
| `.` | "This is a fact" | `color(red).` → "Red is a color" |
| `:-` | "IF ... THEN ..." or "This is true when..." | `bird(X) :- penguin(X).` → "X is a bird IF X is a penguin" |
| `:` | "Such that" or "Where" | `1 { lassign(X,Y) : task(Y) } 1` → "Assign exactly one Y to X where Y is a task" |
| `,` | "AND" | `happy(X) :- healthy(X), wealthy(X).` → "X is happy IF X is healthy AND wealthy" |
| `;` | "OR" (in choice) | `color(red;blue;green).` → "Color is red OR blue OR green" |
| `-` | "NOT" (classical negation) | `-married(john).` → "John is NOT married" |
| `not` | "There is no proof that..." (default negation) | `single(X) :- person(X), not married(X).` → "X is single IF X is a person AND there's no proof X is married" |
| `{ }` | "Choose from these options" | `{ selected(X) : item(X) }.` → "Choose any number of items X to be selected" |
| `m { } n` | "Choose at least m and at most n" | `2 { team(X) : player(X) } 5.` → "Choose between 2 and 5 players for the team" |
| `:-` (alone) | "It must not be the case that..." (constraint) | `:- edge(X,Y), color(X,C), color(Y,C).` → "It must not be that adjacent nodes X and Y have the same color C" |
| `..` | "Range from ... to ..." | `number(1..10).` → "Number is 1 to 10" |
| `#show` | "Display only these predicates" | `#show selected/1.` → "Only show the selected items in the output" |
| `/n` | "Predicate arity (number of arguments)" | `#show starts/3.` → "Show the predicate 'starts' that has exactly 3 arguments" |
| `#count{}` | "Aggregate: count number of elements in a set" | `N = #count{ X : p(X), q(X) }.` → "N is the number of X such that p(X) and q(X) hold" |
| `=` | "Equals" | `X = Y+1` → "X equals Y plus 1" |
| `!=` | "Not equals" | `X != Y` → "X is different from Y" |
| `<`, `>`, `<=`, `>=` | Comparison operators | `X < 10` → "X is less than 10" |

## Input Format

Clingo programs consist of **rules** written in ASP syntax. Here's what inputs look like:

### Basic Syntax Elements:

1. **Facts** - Simple statements about what's true:
```prolog
% Facts about colors
color(red).
color(blue).
color(green).

% Facts about objects
object(ball).
object(box).
```

2. **Rules** - Derive new facts from existing ones:
```prolog
% If X is a primary color, it's also a color
primary(red).
primary(blue).
is_color(X) :- primary(X).
```

3. **Choice Rules** - Generate possibilities:
```prolog
% Choose exactly one color for each object
1 { has_color(X,C) : color(C) } 1 :- object(X).
```

4. **Constraints** - Eliminate unwanted solutions:
```prolog
% No two adjacent objects can have the same color
:- adjacent(X,Y), has_color(X,C), has_color(Y,C).
```

## Output Format

Clingo produces **answer sets** (stable models) that satisfy all rules and constraints:

```
Answer: 1
has_color(ball,red) has_color(box,blue)

Answer: 2
has_color(ball,blue) has_color(box,red)

Answer: 3
has_color(ball,green) has_color(box,red)
...
```

## Example Problems Clingo Can Solve

### 1. **Graph Coloring**
```prolog
% Nodes
node(1..4).

% Edges
edge(1,2). edge(2,3). edge(3,4). edge(4,1). edge(1,3).

% Colors
color(red;green;blue).

% Each node must have exactly one color
1 { coloring(N,C) : color(C) } 1 :- node(N).

% Adjacent nodes can't have the same color
:- edge(X,Y), coloring(X,C), coloring(Y,C).

#show coloring/2.
```

### 2. **Sudoku Solver**
```prolog
% Define grid positions
pos(1..9,1..9).

% Each cell has exactly one value
1 { sudoku(X,Y,N) : N=1..9 } 1 :- pos(X,Y).

% Row constraint
:- sudoku(X,Y,N), sudoku(X,Y1,N), Y != Y1.

% Column constraint  
:- sudoku(X,Y,N), sudoku(X1,Y,N), X != X1.

% Box constraint
:- sudoku(X,Y,N), sudoku(X1,Y1,N), 
   (X-1)/3 == (X1-1)/3, 
   (Y-1)/3 == (Y1-1)/3, 
   (X,Y) != (X1,Y1).

% Initial values (example)
sudoku(1,1,5). sudoku(1,2,3).
% ... more initial values

#show sudoku/3.
```

### 3. **Scheduling Problems**
```prolog
% Time slots
time(1..5).

% Tasks
task(meeting_a; meeting_b; lunch; coding).

% Each task needs exactly one time slot
1 { schedule(T,Time) : time(Time) } 1 :- task(T).

% Some tasks can't overlap
:- schedule(meeting_a,T), schedule(meeting_b,T).

% Lunch must be between 12-1 (time slot 3)
:- schedule(lunch,T), T != 3.

#show schedule/2.
```

## Types of Problems Clingo Excels At:

1. **Combinatorial Optimization**: Finding optimal configurations among many possibilities
2. **Planning**: Determining sequences of actions to achieve goals
3. **Diagnosis**: Finding explanations for observations
4. **Configuration**: Assembling components under constraints
5. **Scheduling**: Allocating resources over time
6. **Puzzle Solving**: Sudoku, N-Queens, logic puzzles
7. **Knowledge Representation**: Modeling complex domains with rules

## Running Clingo:

Basic command:
```bash
clingo input.lp
```

With options:
```bash
clingo input.lp -n 0  # Show all answer sets
clingo input.lp -n 5  # Show first 5 answer sets
```

## Key Advantages:

- **Declarative**: You describe *what* you want, not *how* to compute it
- **Complete**: Finds all solutions or proves none exist
- **Expressive**: Can model complex constraints easily
- **Efficient**: Modern solvers are highly optimized