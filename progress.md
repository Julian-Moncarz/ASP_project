# SLEEC to Clingo Converter - Progress Report

## 📊 **Support Matrix**


| SLEEC Feature           | Support Level | Example                 | Priority   |
| ------------------------- | --------------- | ------------------------- | ------------ |
| Basic rules             | ✅ Full       | `R1 when A then B`      | Core       |
| AND conditions          | ✅ Full       | `A and {B}`             | Core       |
| NOT conditions          | ✅ Full       | `not {B}`               | Core       |
| Simple OR               | ✅ Full       | `{A} or {B}`            | Core       |
| Otherwise clauses       | ✅ Full       | `then A otherwise B`    | Core       |
| Boolean measures        | ✅ Full       | `measure x: boolean`    | Core       |
| Numeric measures        | ✅ Full       | `measure x: numeric`    | Core       |
| Scale measures          | ✅ Full       | `measure x: scale(a,b)` | Core       |
| **Unless clauses**      | ✅ Full       | `unless {x} then Y`     | **High**   |
| **Within clauses**      | ❌ None       | `then X within 5 min`   | **High**   |
| **Measure comparisons** | ❌ None       | `{temp} > 30`           | **Medium** |
| **Constants in rules**  | ❌ None       | `{x} > maxVal`          | **Medium** |
| **Concern sections**    | ❌ None       | `concern_start...`      | **Medium** |
| **Purpose sections**    | ❌ None       | `purpose_start...`      | **Medium** |
| Complex nested logic    | ⚠️ Limited  | Deep nesting fails      | Low        |

### **1. `within` Time Constraints**

**What it is:** Temporal requirements for actions

```sleec
R1 when AlarmSound then NotifyUser within 2 minutes
R2 when Motion then Response within notifyDelay seconds
```

**Status:** ❌ **NOT SUPPORTED**

- Parser treats the `within` clause as part of the action name
- No temporal logic generation in Clingo output

### **2. `concern` Sections**

**What it is:** Behaviors to avoid/prevent

```sleec
concern_start
    c1 when HumanOnFloor and {riskLevel} = high then not CallEmergencyServices
concern_end
```

**Status:** ❌ **NOT SUPPORTED**

- Parser only handles `def_start`/`def_end` and `rule_start`/`rule_end`
- Concern sections are completely ignored

### **3. `purpose` Sections**

**What it is:** Critical behaviors that must be true

```sleec
purpose_start
    p1 when Emergency then ResponseWithin5Minutes
purpose_end
```

**Status:** ❌ **NOT SUPPORTED**

- Parser doesn't recognize purpose sections
- No generation of purpose constraints

### **4. Complex Nested OR Logic**

**What it is:** Complex logical expressions with nested parentheses

```sleec
R1 when Event and (({A} or {B}) and not ({C} and {D})) then Action
```

**Status:** ⚠️ **PARTIALLY SUPPORTED**

- Simple OR works: `{A} or {B}` → `(holds_at(a,T); holds_at(b,T))`
- Complex nested expressions may produce incorrect Clingo syntax

### **5. Measure Comparisons with Operators**

**What it is:** Numeric and relational comparisons

```sleec
R1 when Event and ({temperature} > 30) then Action
R2 when Event and ({count} >= maxValue) then Action
```

**Status:** ❌ **NOT SUPPORTED**

- Only supports basic measure existence checks: `{measure}`
- No support for `>`, `<`, `>=`, `<=`, `=`, `!=` operators

### **6. Constants in Rule Conditions**

**What it is:** Using defined constants in rule logic

```sleec
constant maxTemp = 100
R1 when Event and ({temperature} > maxTemp) then Action
```

**Status:** ❌ **NOT SUPPORTED**

- Constants are parsed but not used in rule generation
- No substitution of constant values in conditions
