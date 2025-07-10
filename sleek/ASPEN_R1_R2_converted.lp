% =============================================================================
% SLEEC to Clingo Conversion
% =============================================================================
% 
% This file was automatically generated from SLEEC rules using the
% SLEEC to Clingo converter.
%
% Generated rules implement the logic using Answer Set Programming (ASP)
% with Clingo syntax.
% =============================================================================

% =============================================================================
% TIME DOMAIN DEFINITION
% =============================================================================
% Define the time steps for the simulation
time(0..10).

% =============================================================================
% EVENT DEFINITIONS
% =============================================================================
% Define all possible events that can occur in the system
event(encounterhuman).
event(informhuman).
event(identifyactivity).

% =============================================================================
% MEASURE DEFINITIONS
% =============================================================================
% Define all measures that can be evaluated
measure(samelanguage).
measure(humanunderstands).

% =============================================================================
% MEASURE INSTANTIATION
% =============================================================================
% Boolean measures: at each timestep, each measure can be true or false
% Scale measures: must have exactly one value at each time
{ holds(samelanguage, T) } :- time(T).
{ holds(humanunderstands, T) } :- time(T).

% =============================================================================
% TRIGGERING EVENT INSTANTIATION
% =============================================================================
% These events can occur independently at each timestep
% The solver will choose when these triggering events happen
{ happens(encounterhuman, T) } :- time(T).

% =============================================================================
% RULE IMPLEMENTATIONS
% =============================================================================
% R1: EncounterHuman and ({sameLanguage} and {humanUnderstands}) -> InformHuman
happens(informhuman, T) :- happens(encounterhuman, T), holds(samelanguage, T), holds(humanunderstands, T), time(T).

% R2: EncounterHuman -> IdentifyActivity
happens(identifyactivity, T) :- happens(encounterhuman, T), time(T).

% =============================================================================
% OUTPUT SPECIFICATION
% =============================================================================
% Specify what information to show in the answer sets
#show happens/2.          % Show all events that happen