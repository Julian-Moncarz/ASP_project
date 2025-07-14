% =============================================================================
% SLEEC to Clingo Conversion (Original Format)
% =============================================================================
% 
% This file was automatically generated from SLEEC rules.
% Format: Direct rule translation following ASPEN.lp patterns
% 
% Generated Rules:
% R1: EncounterHuman and ({sameLanguage} and {humanUnderstands}) -> InformHuman
% R2: EncounterHuman -> IdentifyActivity


% =============================================================================
% TIME DOMAIN DEFINITION
% =============================================================================
time(0..10).

% =============================================================================
% EVENT DEFINITIONS
% =============================================================================
event(encounterhuman).
event(informhuman).
event(identifyactivity).

% =============================================================================
% MEASURE DEFINITIONS
% =============================================================================
measure(samelanguage).
measure(humanunderstands).

% =============================================================================
% MEASURE INSTANTIATION
% =============================================================================
{ holds(samelanguage, T) } :- time(T).
{ holds(humanunderstands, T) } :- time(T).

% =============================================================================
% TRIGGERING EVENT INSTANTIATION
% =============================================================================
{ happens(encounterhuman, T) } :- time(T).

% =============================================================================
% RULE IMPLEMENTATIONS
% =============================================================================
happens(informhuman, T) :- happens(encounterhuman, T), (holds(samelanguage, T), holds(humanunderstands, T)), time(T).
happens(identifyactivity, T) :- happens(encounterhuman, T), time(T).

% =============================================================================
% OUTPUT SPECIFICATION
% =============================================================================
#show happens/2.
#show holds/2.
#show holds/3.