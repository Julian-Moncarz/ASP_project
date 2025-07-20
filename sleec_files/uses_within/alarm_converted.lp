% =============================================================================
% SLEEC to Clingo Conversion (Dalal's Format with Within Support)
% =============================================================================
% 
% This file was automatically generated from SLEEC rules.
% Format: Antecedent/consequent structure with temporal constraints
% 
% Rules Converted:
% R1: MotionDetected and {isArmed} and ({motionCount} > maxMotions) -> AlarmSound within 1 minute
% R2: AlarmSound -> NotifyUser within notifyDelay minutes

% =============================================================================
% DOMAIN DEFINITIONS
% =============================================================================

time(0..10).

% Events
event(motiondetected).
event(alarmsound).
event(notifyuser).

% Measures
measure(isarmed).
measure(motioncount).

% =============================================================================
% SLEEC RULE DEFINITIONS
% =============================================================================

exp(r1).

antecedent(r1, T) :- happens(motiondetected, T, T), holds_at(isarmed, T), (holds_at(motioncount, T) > maxmotions), time(T).

consequent(r1, T) :- time(T), happens(alarmsound, T, T2), T <= T2, T2 <= T+1, time(T2).

exp(r2).

antecedent(r2, T2) :- happens(alarmsound, T, T2), time(T), time(T2).

consequent(r2, T) :- time(T), happens(notifyuser, T, T2), T <= T2, T2 <= T+notifyDelay, time(T2).

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

% Triggering event instantiation (TriggerTime = ActualTime for non-within events)
{ happens(motiondetected, T, T) } :- time(T).

% Action event instantiation (window constrained by time domain)
{ happens(alarmsound, T1, T2) : T1 <= T2, T2 <= T1+1 } :- time(T1), time(T2).
{ happens(notifyuser, T1, T2) : T1 <= T2, T2 <= T1+notifyDelay } :- time(T1), time(T2).

% Measure instantiation
{ holds_at(isarmed, T) } :- time(T).
{ holds_at(motioncount, V, T) : V = 0..10 } :- time(T).

% =============================================================================
% OUTPUT SPECIFICATION
% =============================================================================

#show holds_at/2.

#show happens/3. 