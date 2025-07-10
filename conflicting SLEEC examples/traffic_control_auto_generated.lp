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
event(EmergencyVehicleApproach).
event(EmergencyOverride).
event(TrafficLightChange).

% =============================================================================
% MEASURE DEFINITIONS
% =============================================================================
% Define all measures that can be evaluated
measure(emergencyPriority).
measure(isRushHour).
measure(trafficDensity).
measure(pedestrianCount).
measure(weatherCondition).

% =============================================================================
% MEASURE INSTANTIATION
% =============================================================================
% Boolean measures: at each timestep, each measure can be true or false
% Scale measures: must have exactly one value at each time
{ holds(emergencyPriority, T) } :- time(T).
{ holds(isRushHour, T) } :- time(T).
{ holds(trafficDensity, T) } :- time(T).
{ holds(pedestrianCount, T) } :- time(T).
{ holds(weatherCondition, T) } :- time(T).

% =============================================================================
% TRIGGERING EVENT INSTANTIATION
% =============================================================================
% These events can occur independently at each timestep
% The solver will choose when these triggering events happen
{ happens(EmergencyVehicleApproach, T) } :- time(T).

% =============================================================================
% RULE IMPLEMENTATIONS
% =============================================================================
% R1: EmergencyVehicleApproach and ({emergencyPriority} = high) -> EmergencyOverride
happens(EmergencyOverride, T) :- happens(EmergencyVehicleApproach, T), (holds(emergencyPriority, high, T)), time(T).

% R2: RegularTrafficFlow and {isRushHour} and ({trafficDensity} > maxTrafficDensity/2) -> TrafficLightChange
happens(TrafficLightChange, T) :- RegularTrafficFlow, holds(isRushHour, T), (holds(trafficDensity, V, T), measure_greater_than(trafficDensity, V, maxTrafficDensity)/2), time(T).

% R3: PedestrianCrossing and ({pedestrianCount} > 0) -> TrafficLightChange
happens(TrafficLightChange, T) :- PedestrianCrossing, (holds(pedestrianCount, V, T), measure_greater_than(pedestrianCount, V, 0)), time(T).

% R4: RegularTrafficFlow and ({weatherCondition} = snow) and ({trafficDensity} > maxTrafficDensity/3) -> TrafficLightChange
happens(TrafficLightChange, T) :- RegularTrafficFlow, (holds(weatherCondition, snow, T)), (holds(trafficDensity, V, T), measure_greater_than(trafficDensity, V, maxTrafficDensity)/3), time(T).

% R5: EmergencyVehicleApproach and {isRushHour} and ({trafficDensity} > maxTrafficDensity*0.8) -> not EmergencyOverride
nothappens(EmergencyOverride, T) :- happens(EmergencyVehicleApproach, T), holds(isRushHour, T), (holds(trafficDensity, V, T), measure_greater_than(trafficDensity, V, maxTrafficDensity)*0.8), time(T).


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