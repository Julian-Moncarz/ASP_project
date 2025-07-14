% =============================================================================
% ASPEN Implementation in Clingo
% =============================================================================
% 
% This file implements the ASPEN (Autonomous System Policy Engine) rules using
% Answer Set Programming (ASP) with Clingo syntax.
%
% Core Rules Implemented:
% - Rule 1: when EncounterHuman and ({sameLanguage} and {humanUnderstands}) then InformHuman
% - Rule 2: when EncounterHuman then IdentifyActivity  
% - Rule 2_1: when IdentifyActivity and {unrelatedActivity} then not StoreData
% - Rule 11: when DeployDrone and ({flightCondition} < safe) then ReturnHome 
%            unless ({flightCondition} = dangerous) then GroundDrone
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
event(encounterHuman).    % Human encounter event
event(informHuman).       % Inform human action
event(identifyActivity).  % Activity identification
event(storeData).         % Data storage action
event(deployDrone).       % Drone deployment
event(returnHome).        % Return home action
event(groundDrone).       % Ground drone action

% =============================================================================
% MEASURE DEFINITIONS
% =============================================================================
% Define all measures that can be evaluated
measure(sameLanguage).      % Boolean: same language available
measure(humanUnderstands).  % Boolean: human understands
measure(unrelatedActivity). % Boolean: activity is unrelated
measure(flightCondition).   % Scale: dangerous/unsafe/safe/ideal

% =============================================================================
% MEASURE INSTANTIATION
% =============================================================================
% Boolean measures: at each timestep, each measure can be true or false
% These are choice rules - the solver will choose appropriate values
{ holds(sameLanguage, T) } :- time(T).
{ holds(humanUnderstands, T) } :- time(T).
{ holds(unrelatedActivity, T) } :- time(T).

% Scale measure: flightCondition must have exactly one value at each time
% The values are ordered: dangerous < unsafe < safe < ideal
1 { holds(flightCondition, dangerous, T) ; 
    holds(flightCondition, unsafe, T) ; 
    holds(flightCondition, safe, T) ; 
    holds(flightCondition, ideal, T) } 1 
    :- time(T).

% =============================================================================
% TRIGGERING EVENT INSTANTIATION
% =============================================================================
% These events can occur independently at each timestep
% The solver will choose when these triggering events happen
{ happens(encounterHuman, T) } :- time(T).
{ happens(deployDrone, T) } :- time(T).

% =============================================================================
% ASPEN RULE IMPLEMENTATIONS
% =============================================================================

% - Rule 1: when EncounterHuman and ({sameLanguage} and {humanUnderstands}) then InformHuman
% Condition: encounterHuman AND sameLanguage AND humanUnderstands
% Action: informHuman
happens(informHuman, T) :- 
    happens(encounterHuman, T), 
    holds(sameLanguage, T), 
    holds(humanUnderstands, T),
    time(T).

% Rule 2: When EncounterHuman occurs, IdentifyActivity must happen
% Condition: encounterHuman
% Action: identifyActivity
happens(identifyActivity, T) :- 
    happens(encounterHuman, T),
    time(T).

% Rule 2_1: When IdentifyActivity occurs and unrelatedActivity is true, StoreData must NOT happen
% Condition: identifyActivity AND unrelatedActivity
% Action: NOT storeData (negative action)
nothappens(storeData, T) :-
    happens(identifyActivity, T), 
    holds(unrelatedActivity, T), 
    time(T).

% Rule 11: When DeployDrone occurs and flightCondition < safe, ReturnHome must happen
% Unless flightCondition = dangerous, then GroundDrone must happen instead

% Case 1: flightCondition = unsafe (and not dangerous) -> ReturnHome
happens(returnHome, T) :- 
    happens(deployDrone, T),
    holds(flightCondition, unsafe, T),
    not holds(flightCondition, dangerous, T),
    time(T).

% Case 2: flightCondition = dangerous -> GroundDrone
happens(groundDrone, T) :- 
    happens(deployDrone, T),
    holds(flightCondition, dangerous, T),
    time(T).



% =============================================================================
% CONTRADICTORY RULE FOR TESTING
% =============================================================================
% This rule creates a contradiction with Rule 2_1 to test conflict detection
% Rule: When IdentifyActivity occurs, StoreData happens
happens(storeData, T) :- happens(identifyActivity, T), time(T).


% =============================================================================
% CONTRADICTION DETECTION
% =============================================================================
% Detect when an event both happens and doesn't happen (contradiction)
contradiction(E, T) :- happens(E, T), nothappens(E, T), event(E), time(T).

% Ensure at least one contradiction exists
% This forces the solver to find scenarios where rules conflict
% :- not 1 { contradiction(E, T) : event(E), time(T) }.

% =============================================================================
% OUTPUT SPECIFICATION
% =============================================================================


% TESTING RULE 11
% Enforce that flightCondition is dangerous at all times
%:- time(T), not holds(flightCondition, unsafe, T).
% Enforce that deployDrone must happen at every time
%:- time(T), not happens(deployDrone, T).


% Specify what information to show in the answer sets
%#show contradiction/2.    % Show all contradictions
%#show nothappens/2.       % Show all events that are prevented from happening
#show happens/2.          % Show all events that happen
#show holds/3.
