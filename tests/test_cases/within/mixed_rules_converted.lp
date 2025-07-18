% =============================================================================
% SLEEC to Clingo Conversion (Dalal's Format with Within Support)
% =============================================================================
% 
% This file was automatically generated from SLEEC rules.
% Format: Antecedent/consequent structure with temporal constraints
% 
% Generated Rules:
% R1: ButtonPress -> LightOn
% R2: LightOn and {isNight} -> AlarmSound within 2 minutes
% R3: AlarmSound -> NotifyUser within 1 minute

% =============================================================================
% DOMAIN DEFINITIONS
% =============================================================================

time(0..10).

% Events
event(buttonpress).
event(lighton).
event(alarmsound).
event(notifyuser).

% Measures
measure(isnight).

% =============================================================================
% SLEEC RULE DEFINITIONS
% =============================================================================

exp(r1).

antecedent(r1, T) :- happens(buttonpress, T, T), time(T).

consequent(r1, T) :- time(T), happens(lighton, T, T).

exp(r2).

antecedent(r2, T) :- happens(lighton, T, T), holds_at(isnight, T), time(T).

consequent(r2, T) :- time(T), happens(alarmsound, T, T2), T <= T2, T2 <= T+2, time(T2).

exp(r3).

antecedent(r3, T2) :- happens(alarmsound, T, T2), time(T), time(T2).

consequent(r3, T) :- time(T), happens(notifyuser, T, T2), T <= T2, T2 <= T+1, time(T2).

% =============================================================================
% RULE SATISFACTION LOGIC
% =============================================================================

% General holds logic
holds(G, T):-
    time(T), 
    exp(G),
    holds_nv(G, T).

holds(G, T):-
    time(T), 
    exp(G),
    holds_v(G, T).

% Non-vacuous satisfaction for r1
holds_nv(r1, T):-
    time(T),
    antecedent(r1, T),
    consequent(r1, T).

% Vacuous satisfaction for r1
holds_v(r1, T):-
    time(T),
    not antecedent(r1, T),
    not consequent(r1, T).

% Non-vacuous satisfaction for r2
holds_nv(r2, T):-
    time(T),
    antecedent(r2, T),
    consequent(r2, T).

% Vacuous satisfaction for r2
holds_v(r2, T):-
    time(T),
    not antecedent(r2, T),
    not consequent(r2, T).

% Non-vacuous satisfaction for r3
holds_nv(r3, T):-
    time(T),
    antecedent(r3, T),
    consequent(r3, T).

% Vacuous satisfaction for r3
holds_v(r3, T):-
    time(T),
    not antecedent(r3, T),
    not consequent(r3, T).

% Hard constraint: every rule must be satisfied at every time point
:- exp(R), time(T), not holds(R,T).

% =============================================================================
% ACTION GENERATION AND CONSTRAINTS
% =============================================================================

% Triggering event instantiation (TriggerTime = ActualTime for direct triggers)
{ happens(buttonpress, T, T) } :- time(T).

% Action event instantiation 
{ happens(lighton, T, T) } :- time(T).
{ happens(alarmsound, T1, T2) : T1 <= T2, T2 <= T1+2 } :- time(T1), time(T2).
{ happens(notifyuser, T1, T2) : T1 <= T2, T2 <= T1+1 } :- time(T1), time(T2).

% Measure instantiation
{ holds_at(isnight, T) } :- time(T).

% =============================================================================
% OUTPUT SPECIFICATION
% =============================================================================

#show holds_at/2.

#show happens/3. 