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
event(MotionDetected).
event(AlarmSound within 1 minute).
event(NotifyUser within notifyDelay minutes).

% =============================================================================
% MEASURE DEFINITIONS
% =============================================================================
% Define all measures that can be evaluated
measure(isArmed).
measure(motionCount).

% =============================================================================
% MEASURE INSTANTIATION
% =============================================================================
% Boolean measures: at each timestep, each measure can be true or false
% Scale measures: must have exactly one value at each time
{ holds(isArmed, T) } :- time(T).
{ holds(motionCount, T) } :- time(T).

% =============================================================================
% TRIGGERING EVENT INSTANTIATION
% =============================================================================
% These events can occur independently at each timestep
% The solver will choose when these triggering events happen
{ happens(MotionDetected, T) } :- time(T).

% =============================================================================
% RULE IMPLEMENTATIONS
% =============================================================================
% R1: MotionDetected and {isArmed} and ({motionCount} > maxMotions) -> AlarmSound within 1 minute
happens(AlarmSound within 1 minute, T) :- happens(MotionDetected, T), holds(isArmed, T), (holds(motionCount, V, T), measure_greater_than(motionCount, V, maxMotions)), time(T).

% R2: AlarmSound -> NotifyUser within notifyDelay minutes
happens(NotifyUser within notifyDelay minutes, T) :- AlarmSound, time(T).


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