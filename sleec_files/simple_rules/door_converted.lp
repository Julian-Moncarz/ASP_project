% =============================================================================
% SLEEC to Clingo Conversion (Dalal's Format)
% =============================================================================
% 
% This file was automatically generated from SLEEC rules.
% Format: Antecedent/consequent structure with rule satisfaction logic
% 
% Generated Rules:
% R1: DoorOpen and (not {isLocked}) -> AlarmActivate

% =============================================================================
% DOMAIN DEFINITIONS
% =============================================================================

time(0..10).

% Events
event(dooropen).
event(alarmactivate).

% Measures
measure(islocked).

% =============================================================================
% SLEEC RULE DEFINITIONS
% =============================================================================

exp(r1).

antecedent(r1, T) :- happens(dooropen, T), not holds_at(islocked, T), time(T).

consequent(r1, T) :- time(T), happens(alarmactivate, T).

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


% Hard constraint: every rule must be satisfied at every time point
:- exp(R), time(T), not holds(R,T).

% =============================================================================
% ACTION GENERATION AND CONSTRAINTS
% =============================================================================

% Triggering event instantiation
{ happens(dooropen, T) } :- time(T).

% Action event instantiation
{ happens(alarmactivate, T) } :- time(T).

% Measure instantiation
{ holds_at(islocked, T) } :- time(T).

% =============================================================================
% OUTPUT SPECIFICATION
% =============================================================================

#show holds_nv/2.
#show holds_v/2.