% =============================================================================
        % SLEEC to Clingo Conversion (Dalal's Format)
        % =============================================================================
        % 
        % This file was automatically generated from SLEEC rules.
        % Format: Antecedent/consequent structure with rule satisfaction logic
        % 
        % Generated Rules:
        % R1: ButtonPress -> LightOn
% R2: LightOn and {isNight} -> AlarmSound
% R3: AlarmSound -> NotifyUser

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

consequent(r2, T) :- time(T), happens(alarmsound, T, T+120).

exp(r3).

antecedent(r3, T) :- happens(alarmsound, T, T), time(T).

consequent(r3, T) :- time(T), happens(notifyuser, T, T+60).

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

% Triggering event instantiation
{ happens(buttonpress, T, T) } :- time(T).

% Action event instantiation
{ happens(notifyuser, T, T) } :- time(T).
{ happens(lighton, T, T) } :- time(T).
{ happens(alarmsound, T, T) } :- time(T).

% Measure instantiation
{ holds_at(isnight, T) } :- time(T).

% =============================================================================
% OUTPUT SPECIFICATION
% =============================================================================

#show holds_at/2.

#show happens/3.