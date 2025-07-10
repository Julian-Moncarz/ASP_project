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
event(buttonpress).
event(lighton).
event(setbrightnesstomax).

% =============================================================================
% MEASURE DEFINITIONS
% =============================================================================
% Define all measures that can be evaluated
measure(isnight).

% =============================================================================
% MEASURE INSTANTIATION
% =============================================================================
% Boolean measures: at each timestep, each measure can be true or false
% Scale measures: must have exactly one value at each time
{ holds(isnight, T) } :- time(T).

% =============================================================================
% TRIGGERING EVENT INSTANTIATION
% =============================================================================
% These events can occur independently at each timestep
% The solver will choose when these triggering events happen
{ happens(buttonpress, T) } :- time(T).
{ happens(lighton, T) } :- time(T).

% =============================================================================
% RULE IMPLEMENTATIONS
% =============================================================================
% R1: ButtonPress -> LightOn
happens(lighton, T) :- happens(buttonpress, T), time(T).

% R2: LightOn and {isNight} -> SetBrightnessToMax
happens(setbrightnesstomax, T) :- happens(lighton, T), holds(isnight, T), time(T).


% =============================================================================
% CONTRADICTION DETECTION
% =============================================================================
% Detect when an event both happens and doesn't happen (contradiction)
contradiction(E, T) :- happens(E, T), nothappens(E, T), event(E), time(T).

% =============================================================================
% OUTPUT SPECIFICATION
% =============================================================================
% Specify what information to show in the answer sets
#show happens/2.          % Show all events that happen
#show holds/2.            % Show boolean measures
#show holds/3.            % Show scale/numeric measures
#show contradiction/2.    % Show contradictions if any