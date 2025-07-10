A SLEEC document consists of several main sections:

Note: things after // are comments

### 1. **Definitions Section** (`def_start` ... `def_end`)

Define events, measures, and constants used in the system.

```
def_start
    // Events - each word is capitalized
    // Events represent things that can happen in the system

    event UserTurnOn
    event SystemStart
    event EmergencyStop
  
    // Measures - camelCase: type of value
    // can be: numeric, boolean or scale(option1, option2, etc)
    // Measures are observable properties or sensor readings

    measure temperature: numeric
    measure isActive: boolean
    measure riskLevel: scale(low, medium, high)
  
    // Constants - camelCase
    // set equal to a number only
    constant maxTemp = 100
    constant timeoutDuration = 30
def_end
```

### 2. **Rules Section** (`rule_start` ... `rule_end`)

System responses to events

**Response Modifiers:**

- **and**: Conditions on **measures** with and / not logic
- **Unless**: Exception handling - again, only conditions on measures
- **Otherwise**: Alternative action
- **Within**: Time constraints the triggered action must happen within

```
rule_start
    // to use a measure, constant or event in a rule, it must be defined in definitions
    // Basic rule
    R1 when UserTurnOn then SystemStart
  
    // Unless a thing
    R2 when HumanOnFloor then CallEmergencyServices unless (not {humanAssents}) then not CallEmergencyServices

    // Unless with an otherwise statement - the measure must be in {}
    R3 when UserChangeRoute then CalculateShortestPath unless (not {commandClear}) then AskForClarification otherwise not ChangeCurrentDriving

    // With a time constraint
    R4 when SmokeDetectorAlarm then CallEmergencyServices within 5 minutes

    // With a condition for activation - the measure must be in {}
    R5 when TrackTime and ({timeBetweenMeals} > maxTimeBetweenMeals) then GiveSuggestion
rule_end
```

Note: this system seems convoluted - why not just have everything be based of and / or / not logic (which should also be triggerable based on events rather than just measures)? Get rid of unless and just make that another rule!

eg

R1 when Event and (not {condition}) then Reponse
R2 when Event and {condition} then ResponseYouWouldTriggerWithUnless


Note: Ah. This is what normalization is!

### 3. **Concerns Section** (`concern_start` ... `concern_end`)

Things you DO NOT want the system to do. Behaviors you want to AVOID.

**NOTE**: Events are not inherently conflicting, even if they appear so to a human! Eg you could have both AllowAccess and DenyAccess trigger at the same time for the same person and the system would have no way of knowing that was any more illogical that AllowAccess and BringFood unless you set AllowAcess and DenyAccess both triggering at the same time as a concern - how would you even write that?

c1 when DenyAccess then not AllowAccess

```
concern_start
    // Just like for rules, all event constants and measures must exist in the definitions
    // The c is not capitalised
    // I think that should be changed - all the other letters are capitalised eg R1 and P1

    // You dont want the bot to just leave them there to die
    c1 when HumanOnFloor and ({userOccupied} and ({riskLevel} = high)) then not CallEmergencyServices     

    // You don't want the Unauthorized person to be given Access
    c2 when Unauthorized then AccessGranted

    // You dont want the car to drive when the user says no and is not strapped in or the door is not closed or there is no destination

    c3 when SystemReady and ((not {userSaysYes}) and (((not {doorClosed}) or (not {seatBeltOn})) or (not {destinationExists}))) then CarDriving
concern_end
```

### 4. **Purposes Section** (`purpose_start` ... `purpose_end`)

The things that must be true about the system - the critical behaviors.

Note: naming is super inconsistant. Some of the examples use pr1, some use p1, some use P1...

**Ignore these for now**

```
purpose_start
    // A given event MUST exist?
    P1 exists SystemActive
  
    // Secondary objective
    P2 exists UserRequest while ProvideService
purpose_end
```
