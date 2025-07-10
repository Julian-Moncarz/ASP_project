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
event(OccupantArrival).
event(EnergyOptimization).
event(SecurityAlert).
event(ComfortMode).
event(PrivacyMode).

% =============================================================================
% MEASURE DEFINITIONS
% =============================================================================
% Define all measures that can be evaluated
measure(energyConsumption).
measure(temperature).
measure(humidity).
measure(isWorkHours).
measure(privacyLevel).
measure(isNightTime).
measure(securityThreat).

% =============================================================================
% MEASURE INSTANTIATION
% =============================================================================
% Boolean measures: at each timestep, each measure can be true or false
% Scale measures: must have exactly one value at each time
{ holds(energyConsumption, T) } :- time(T).
{ holds(temperature, T) } :- time(T).
{ holds(humidity, T) } :- time(T).
{ holds(isWorkHours, T) } :- time(T).
{ holds(privacyLevel, T) } :- time(T).
{ holds(isNightTime, T) } :- time(T).
{ holds(securityThreat, T) } :- time(T).

% =============================================================================
% TRIGGERING EVENT INSTANTIATION
% =============================================================================
% These events can occur independently at each timestep
% The solver will choose when these triggering events happen
{ happens(EnergyOptimization, T) } :- time(T).
{ happens(OccupantArrival, T) } :- time(T).
{ happens(PrivacyMode, T) } :- time(T).

% =============================================================================
% RULE IMPLEMENTATIONS
% =============================================================================
% R1: OccupantDeparture and ({energyConsumption} > maxEnergyConsumption/2) -> EnergyOptimization
happens(EnergyOptimization, T) :- OccupantDeparture, (holds(energyConsumption, V, T), measure_greater_than(energyConsumption, V, maxEnergyConsumption)/2), time(T).

% R2: OccupantDeparture -> SecurityAlert
happens(SecurityAlert, T) :- OccupantDeparture, time(T).

% R3: OccupantArrival and (({temperature} != optimalTemperature) or ({humidity} != optimalHumidity)) -> ComfortMode
happens(ComfortMode, T) :- happens(OccupantArrival, T), ((holds(temperature, T) != optimalTemperature) ; (holds(humidity, T) != optimalHumidity)), time(T).

% R4: OccupantArrival and {isWorkHours} and ({privacyLevel} = high) -> PrivacyMode
happens(PrivacyMode, T) :- happens(OccupantArrival, T), holds(isWorkHours, T), (holds(privacyLevel, high, T)), time(T).

% R5: {isNightTime} and ({securityThreat} >= medium) -> SecurityAlert
happens(SecurityAlert, T) :- holds(isNightTime, T), (holds(securityThreat, T) >= medium), time(T).

% R6: EnergyOptimization and ({temperature} < 10 or {temperature} > 35) -> not EnergyOptimization
nothappens(EnergyOptimization, T) :- happens(EnergyOptimization, T), (holds(temperature, V, T), measure_less_than(temperature, V, 10) ; holds(temperature, V, T), measure_greater_than(temperature, V, 35)), time(T).

% R7: PrivacyMode and ({securityThreat} = high) -> not PrivacyMode
nothappens(PrivacyMode, T) :- happens(PrivacyMode, T), (holds(securityThreat, high, T)), time(T).


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