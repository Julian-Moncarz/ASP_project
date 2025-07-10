% =============================================================================
% ASPEN Rules R1 and R2 Implementation in Clingo
% =============================================================================
% 
% This file implements only rules R1 and R2 from the ASPEN policy using
% Answer Set Programming (ASP) with Clingo syntax.
%
% Rules Implemented:
% - Rule 1: when EncounterHuman and ({sameLanguage} and {humanUnderstands}) then InformHuman
% - Rule 2: when EncounterHuman then IdentifyActivity  
% - Rule 2_1: when IdentifyActivity and {unrelatedActivity} then not StoreData
% =============================================================================

% =============================================================================
% TIME DOMAIN DEFINITION
% =============================================================================
% Define the time steps for the simulation
time(0..10).

% =============================================================================
% EVENT DEFINITIONS
% =============================================================================
% Define only the events needed for R1 and R2
event(encounterHuman).    % Human encounter event
event(informHuman).       % Inform human action
event(identifyActivity).  % Activity identification
event(storeData).         % Data storage action

% =============================================================================
% MEASURE DEFINITIONS
% =============================================================================
% Define only the measures needed for R1 and R2
measure(sameLanguage).      % Boolean: same language available
measure(humanUnderstands).  % Boolean: human understands
measure(unrelatedActivity). % Boolean: activity is unrelated

% =============================================================================
% MEASURE INSTANTIATION
% =============================================================================
% Boolean measures: at each timestep, each measure can be true or false
% These are choice rules - the solver will choose appropriate values
{ holds(sameLanguage, T) } :- time(T).
{ holds(humanUnderstands, T) } :- time(T).
{ holds(unrelatedActivity, T) } :- time(T).

% =============================================================================
% TRIGGERING EVENT INSTANTIATION
% =============================================================================
% EncounterHuman can occur independently at each timestep
{ happens(encounterHuman, T) } :- time(T).

% =============================================================================
% ASPEN RULE IMPLEMENTATIONS - R1 and R2 ONLY
% =============================================================================

% Rule 1: when EncounterHuman and ({sameLanguage} and {humanUnderstands}) then InformHuman
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

% =============================================================================
% CONTRADICTORY RULE FOR TESTING (optional)
% =============================================================================
% This rule creates a contradiction with Rule 2_1 to test conflict detection
% Rule: When IdentifyActivity occurs, StoreData happens
% happens(storeData, T) :- happens(identifyActivity, T), time(T).

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
#show holds/2.            % Show all measure values
#show contradiction/2.    % Show any contradictions 