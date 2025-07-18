% =============================================================================
% SLEEC to Clingo Conversion (Dalal's Format with Within Support)
% =============================================================================
% 
% This file was automatically generated from SLEEC rules.
% Format: Antecedent/consequent structure with temporal constraints
% 
% Generated Rules:
% R1: EncounterHuman and ({sameLanguage} and {humanUnderstands}) -> InformHuman
% R2: EncounterHuman -> IdentifyActivity

% =============================================================================
% DOMAIN DEFINITIONS
% =============================================================================

time(0..10).

% Events
event(encounterhuman).
event(informhuman).
event(identifyactivity).

% Measures
measure(samelanguage).
measure(humanunderstands).

% =============================================================================
% SLEEC RULE DEFINITIONS
% =============================================================================

exp(r1).

antecedent(r1, T) :- happens(encounterhuman, T, T), holds_at(samelanguage, T), holds_at(humanunderstands, T), time(T).

consequent(r1, T) :- time(T), happens(informhuman, T, T).

exp(r2).

antecedent(r2, T) :- happens(encounterhuman, T, T), time(T).

consequent(r2, T) :- time(T), happens(identifyactivity, T, T).

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

% Triggering event instantiation
{ happens(encounterhuman, T, T) } :- time(T).

% Action event instantiation 
{ happens(identifyactivity, T, T) } :- time(T).
{ happens(informhuman, T, T) } :- time(T).

% Measure instantiation
{ holds_at(samelanguage, T) } :- time(T).
{ holds_at(humanunderstands, T) } :- time(T).

% =============================================================================
% OUTPUT SPECIFICATION
% =============================================================================

#show holds_at/2.

#show happens/3. 