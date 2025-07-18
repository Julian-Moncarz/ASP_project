% =============================================================================
% SLEEC to Clingo Conversion (Dalal's Format)
% =============================================================================
% 
% This file was automatically generated from SLEEC rules.
% Format: Antecedent/consequent structure with rule satisfaction logic
% 
% Generated Rules:
% R1: TriggerEvent -> ActionEvent

% =============================================================================
% DOMAIN DEFINITIONS
% =============================================================================

time(0..10).

% Events
event(triggerevent).
event(actionevent).

% =============================================================================
% SLEEC RULE DEFINITIONS
% =============================================================================

exp(r1).

antecedent(r1, T) :- happens(triggerevent, T, T), time(T).

consequent(r1, T) :- time(T), happens(actionevent, T, T).

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
{ happens(triggerevent, T, T) } :- time(T).

% Action event instantiation
{ happens(actionevent, T, T) } :- time(T).

% =============================================================================
% OUTPUT SPECIFICATION
% =============================================================================

#show happens/3. 