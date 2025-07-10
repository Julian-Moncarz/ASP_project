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
event(HeaterOn).
event(CoolerOn).

% =============================================================================
% MEASURE DEFINITIONS
% =============================================================================
% Define all measures that can be evaluated
measure(temperature).
measure(desiredTemp).
measure(isManualOverride).

% =============================================================================
% MEASURE INSTANTIATION
% =============================================================================
% Boolean measures: at each timestep, each measure can be true or false
% Scale measures: must have exactly one value at each time
{ holds(temperature, T) } :- time(T).
{ holds(desiredTemp, T) } :- time(T).
{ holds(isManualOverride, T) } :- time(T).

% =============================================================================
% RULE IMPLEMENTATIONS
% =============================================================================
% R1: TempChangeRequest and ({temperature} < {desiredTemp}) and (not {isManualOverride}) -> HeaterOn
happens(HeaterOn, T) :- TempChangeRequest, (holds(temperature, T) < holds(desiredTemp, T)), (not holds(isManualOverride, T)), time(T).

% R2: TempChangeRequest and ({temperature} > {desiredTemp}) and (not {isManualOverride}) -> CoolerOn
happens(CoolerOn, T) :- TempChangeRequest, (holds(temperature, T) > holds(desiredTemp, T)), (not holds(isManualOverride, T)), time(T).


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