% =============================================================================
% SLEEC to Clingo Conversion (Dalal's Format with Within Support)
% =============================================================================
% 
% This file was automatically generated from SLEEC rules.
% Format: Antecedent/consequent structure with temporal constraints
% 
% Generated Rules:
% R1: StartProcess -> FinishProcess within 15 minutes

% =============================================================================
% DOMAIN DEFINITIONS
% =============================================================================

time(0..10).

% Events
event(startprocess).
event(finishprocess).

% =============================================================================
% SLEEC RULE DEFINITIONS
% =============================================================================

exp(r1).

antecedent(r1, T) :- happens(startprocess, T, T), time(T).

consequent(r1, T) :- time(T), happens(finishprocess, T, T2), T <= T2, T2 <= T+15, time(T2).

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
{ happens(startprocess, T, T) } :- time(T).

% Action event instantiation (window constrained by time domain)
{ happens(finishprocess, T1, T2) : T1 <= T2, T2 <= T1+15 } :- time(T1), time(T2).

% =============================================================================
% OUTPUT SPECIFICATION
% =============================================================================

#show happens/3. 