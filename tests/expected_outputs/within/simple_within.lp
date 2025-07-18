% =============================================================================
% SLEEC to Clingo Conversion (Dalal's Format with Within Support)
% =============================================================================
% 
% This file was automatically generated from SLEEC rules.
% Format: Antecedent/consequent structure with temporal constraints
% 
% Generated Rules:
% R1: MotionDetected and {isArmed} -> AlarmSound within 3 minutes

% =============================================================================
% DOMAIN DEFINITIONS
% =============================================================================

time(0..10).

% Events
event(motiondetected).
event(alarmsound).

% Measures
measure(isarmed).

% =============================================================================
% SLEEC RULE DEFINITIONS
% =============================================================================

exp(r1).

antecedent(r1, T) :- happens(motiondetected, T, T), holds_at(isarmed, T), time(T).

consequent(r1, T) :- time(T), happens(alarmsound, T, T2), T <= T2, T2 <= T+3, time(T2).

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

% Triggering event instantiation (TriggerTime = ActualTime for non-within events)
{ happens(motiondetected, T, T) } :- time(T).

% Action event instantiation (can be triggered at any time within temporal window)
{ happens(alarmsound, T1, T2) : T1 <= T2, T2 <= T1+3 } :- time(T1), time(T2).

% Measure instantiation
{ holds_at(isarmed, T) } :- time(T).

% =============================================================================
% OUTPUT SPECIFICATION
% =============================================================================

#show holds_at/2.

#show happens/3. 