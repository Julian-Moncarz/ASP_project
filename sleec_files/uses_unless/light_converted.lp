% =============================================================================
% SLEEC to Clingo Conversion (Dalal's Format)
% =============================================================================
% 
% This file was automatically generated from SLEEC rules.
% Format: Antecedent/consequent structure with rule satisfaction logic
% 
% Generated Rules:
% R1: MotionDetected -> TurnOnLight

% =============================================================================
% DOMAIN DEFINITIONS
% =============================================================================

time(0..10).

% Events
event(motiondetected).
event(turnonlight).
event(playjingle).

% Measures
measure(isoccupied).
measure(isdaytime).

% =============================================================================
% SLEEC RULE DEFINITIONS
% =============================================================================

exp(r1_primary).

antecedent(r1_primary, T) :- happens(motiondetected, T, T), not holds_at(isdaytime, T), time(T).

consequent(r1_primary, T) :- time(T), happens(turnonlight, T, T).

exp(r1_unless1).

antecedent(r1_unless1, T) :- happens(motiondetected, T, T), holds_at(isdaytime, T), time(T).

consequent(r1_unless1, T) :- time(T), happens(playjingle, T, T).

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


% Non-vacuous satisfaction for r1_primary
holds_nv(r1_primary, T):-
    time(T),
    antecedent(r1_primary, T),
    consequent(r1_primary, T).


% Vacuous satisfaction for r1_primary
holds_v(r1_primary, T):-
    time(T),
    not antecedent(r1_primary, T),
    not consequent(r1_primary, T).


% Non-vacuous satisfaction for r1_unless1
holds_nv(r1_unless1, T):-
    time(T),
    antecedent(r1_unless1, T),
    consequent(r1_unless1, T).


% Vacuous satisfaction for r1_unless1
holds_v(r1_unless1, T):-
    time(T),
    not antecedent(r1_unless1, T),
    not consequent(r1_unless1, T).


% Hard constraint: every rule must be satisfied at every time point
:- exp(R), time(T), not holds(R,T).

% =============================================================================
% ACTION GENERATION AND CONSTRAINTS
% =============================================================================

% Triggering event instantiation
{ happens(motiondetected, T, T) } :- time(T).

% Action event instantiation
{ happens(turnonlight, T, T) } :- time(T).

% Measure instantiation
{ holds_at(isoccupied, T) } :- time(T).
{ holds_at(isdaytime, T) } :- time(T).

% =============================================================================
% OUTPUT SPECIFICATION
% =============================================================================

#show holds_at/2.

#show happens/2.