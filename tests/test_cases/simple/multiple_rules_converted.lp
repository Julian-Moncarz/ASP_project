% =============================================================================
% SLEEC to Clingo Conversion (Dalal's Format with Within Support)
% =============================================================================
% 
% This file was automatically generated from SLEEC rules.
% Format: Antecedent/consequent structure with temporal constraints
% 
% Generated Rules:
% R1: Event1 -> Action1
% R2: Event2 and {condition1} -> Action2

% =============================================================================
% DOMAIN DEFINITIONS
% =============================================================================

time(0..10).

% Events
event(event1).
event(event2).
event(action1).
event(action2).

% Measures
measure(condition1).

% =============================================================================
% SLEEC RULE DEFINITIONS
% =============================================================================

exp(r1).

antecedent(r1, T) :- happens(event1, T, T), time(T).

consequent(r1, T) :- time(T), happens(action1, T, T).

exp(r2).

antecedent(r2, T) :- happens(event2, T, T), holds_at(condition1, T), time(T).

consequent(r2, T) :- time(T), happens(action2, T, T).

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

% Hard constraint: every rule must be satisfied at every time point
:- exp(R), time(T), not holds(R,T).

% =============================================================================
% ACTION GENERATION AND CONSTRAINTS
% =============================================================================

% Triggering event instantiation (TriggerTime = ActualTime for direct triggers)
{ happens(event1, T, T) } :- time(T).
{ happens(event2, T, T) } :- time(T).

% Action event instantiation 
{ happens(action1, T, T) } :- time(T).
{ happens(action2, T, T) } :- time(T).

% Measure instantiation
{ holds_at(condition1, T) } :- time(T).

% =============================================================================
% OUTPUT SPECIFICATION
% =============================================================================

#show holds_at/2.

#show happens/3. 