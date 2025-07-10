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
event(PatientArrival).
event(AdministerMedication).
event(WithholdMedication).

% =============================================================================
% MEASURE DEFINITIONS
% =============================================================================
% Define all measures that can be evaluated
measure(hasAllergy).
measure(bloodPressure).
measure(heartRate).
measure(isEmergency).
measure(patientAge).
measure(medicationLevel).

% =============================================================================
% MEASURE INSTANTIATION
% =============================================================================
% Boolean measures: at each timestep, each measure can be true or false
% Scale measures: must have exactly one value at each time
{ holds(hasAllergy, T) } :- time(T).
{ holds(bloodPressure, T) } :- time(T).
{ holds(heartRate, T) } :- time(T).
{ holds(isEmergency, T) } :- time(T).
{ holds(patientAge, T) } :- time(T).
{ holds(medicationLevel, T) } :- time(T).

% =============================================================================
% TRIGGERING EVENT INSTANTIATION
% =============================================================================
% These events can occur independently at each timestep
% The solver will choose when these triggering events happen
{ happens(AdministerMedication, T) } :- time(T).
{ happens(PatientArrival, T) } :- time(T).

% =============================================================================
% RULE IMPLEMENTATIONS
% =============================================================================
% R1: PatientArrival and (not {hasAllergy}) and ({bloodPressure} >= minBloodPressure) and ({heartRate} <= maxHeartRate) -> AdministerMedication
happens(AdministerMedication, T) :- happens(PatientArrival, T), (not holds(hasAllergy, T)), (holds(bloodPressure, T) >= minBloodPressure), (holds(heartRate, T) <= maxHeartRate), time(T).

% R2: PatientArrival and {isEmergency} -> AdministerMedication
happens(AdministerMedication, T) :- happens(PatientArrival, T), holds(isEmergency, T), time(T).

% R3: PatientArrival and ({hasAllergy} or ({bloodPressure} < minBloodPressure) or ({heartRate} > maxHeartRate)) -> WithholdMedication
happens(WithholdMedication, T) :- happens(PatientArrival, T), (holds(hasAllergy, T) ; (holds(bloodPressure, V, T), measure_less_than(bloodPressure, V, minBloodPressure)) ; (holds(heartRate, V, T), measure_greater_than(heartRate, V, maxHeartRate))), time(T).

% R4: AdministerMedication and ({patientAge} >= criticalAge) and ({medicationLevel} > maxDosage) -> WithholdMedication
happens(WithholdMedication, T) :- happens(AdministerMedication, T), (holds(patientAge, T) >= criticalAge), (holds(medicationLevel, V, T), measure_greater_than(medicationLevel, V, maxDosage)), time(T).


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