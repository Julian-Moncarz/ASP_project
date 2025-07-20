% =============================================================================
% SLEEC to Clingo Conversion (Dalal's Format with Within Support)
% =============================================================================
% 
% This file was automatically generated from SLEEC rules.
% Format: Antecedent/consequent structure with temporal constraints
% 
% Rules Converted:
% R1: MonitorMealTime -> InformUser within 10 minutes
% R2: AgentDeployed -> TrackTime
% R3: HumanOnFloor -> CallEmergencyServices
% R4: InterfereSafely and (not {safePathFound}) -> InformUser
    unless {userOccupied}
% R5: UserWantsToCook -> AllowUserToCook
% R6: UserHasLimitation -> InformUser
% R7: UserWantsToCook -> CheckTemperature
% R8: FoodPreparation -> TrackTime
% R9: MeetingUser -> CollectandRecordInformation
% R10: GiveSuggestion -> ConsiderUserPractices
% R11: MeetingUser -> AskForEmergencyContact
% R12: AgentDeployed and (not {personAuthorized}) -> not ShowDataHistory
% R13: UserUnpredictable -> not GiveUserDangerousObjects
% R14: AgentDeployed and (not {userAsksForAppropriateTasks}) -> RemindUserOfLimitations
    unless ({needLevel} > nmedium)
% R15: PreparingDeployment -> AgentHasAppropriateAppearance
    unless {userNeedsSpecialAccomodations}
% R16: PreparingDeployment -> CalibrateSpeech
% R17: GivingCookingInstructions -> UseFirstPersonPluralLanguage
% R18: BeforeCookingBegins -> AskForDetailLevelOfInstructions
% R19: UserChangeMind -> RecalculateApproach
    unless ({riskLevel} = high)
% R20: UserChangeItemLocation -> UpdateMap
% R21: SmokeDetectorAlarm -> CallEmergencyServices within 5 minutes

% =============================================================================
% DOMAIN DEFINITIONS
% =============================================================================

time(0..10).

% Events
event(preparingdeployment).
event(agentdeployed).
event(meetinguser).
event(informuser).
event(informcaregiver).
event(callemergencyservices).
event(remindlater).
event(agenthasappropriateappearance).
event(askfordetaillevelofinstructions).
event(usefirstpersonplurallanguage).
event(calibratespeech).
event(reminduseroflimitations).
event(askforemergencycontact).
event(humanonfloor).
event(smokedetectoralarm).
event(openwindows).
event(firesafetymeasures).
event(askuserifok).
event(interferesafely).
event(userhaslimitation).
event(checktemperature).
event(foodpreparation).
event(tracktime).
event(userunpredictable).
event(giveuserdangerousobjects).
event(monitormealtime).
event(beforecookingbegins).
event(userwantstocook).
event(allowusertocook).
event(givesuggestion).
event(givingcookinginstructions).
event(consideruserpractices).
event(userchangeitemlocation).
event(userchangemind).
event(recalculateapproach).
event(providedatasummaries).
event(collectandrecordinformation).
event(updateinformation).
event(showdatahistory).
event(updatemap).

% Measures
measure(useroccupied).
measure(timebetweenmeals).
measure(personauthorized).
measure(dataneedschecking).
measure(userasksforappropriatetasks).
measure(userneedsspecialaccomodations).
measure(userdisablesalarm).
measure(alarmrestarts).
measure(needlevel).
measure(humanassents).
measure(safepathfound).
measure(hazarddetected).
measure(kitchensafe).
measure(risklevel).
measure(alarmon).

% =============================================================================
% SLEEC RULE DEFINITIONS
% =============================================================================

exp(r1).

antecedent(r1, T) :- happens(monitormealtime, T, T), time(T).

consequent(r1, T) :- time(T), happens(informuser, T, T2), T <= T2, T2 <= T+10, time(T2).

exp(r2).

antecedent(r2, T) :- happens(agentdeployed, T, T), time(T).

consequent(r2, T) :- time(T), happens(tracktime, T, T).

exp(r3_primary).

antecedent(r3_primary, T) :- happens(humanonfloor, T, T), not not holds_at(humanassents, T), time(T).

consequent(r3_primary, T) :- time(T), happens(callemergencyservices, T, T).

exp(r4).

antecedent(r4, T) :- happens(interferesafely, T, T), not holds_at(safepathfound, T), time(T).

consequent(r4, T) :- time(T), happens(informuser
    unless {useroccupied}, T, T).

exp(r5).

antecedent(r5, T) :- happens(userwantstocook, T, T), time(T).

consequent(r5, T) :- time(T), happens(allowusertocook, T, T).

exp(r6).

antecedent(r6, T) :- happens(userhaslimitation, T, T), time(T).

consequent(r6, T) :- time(T), happens(informuser, T, T).

exp(r7).

antecedent(r7, T) :- happens(userwantstocook, T, T), time(T).

consequent(r7, T) :- time(T), happens(checktemperature, T, T).

exp(r8).

antecedent(r8, T) :- happens(foodpreparation, T, T), time(T).

consequent(r8, T) :- time(T), happens(tracktime, T, T).

exp(r9).

antecedent(r9, T) :- happens(meetinguser, T, T), time(T).

consequent(r9, T) :- time(T), happens(collectandrecordinformation, T, T).

exp(r10).

antecedent(r10, T) :- happens(givesuggestion, T, T), time(T).

consequent(r10, T) :- time(T), happens(consideruserpractices, T, T).

exp(r11).

antecedent(r11, T) :- happens(meetinguser, T, T), time(T).

consequent(r11, T) :- time(T), happens(askforemergencycontact, T, T).

exp(r12).

antecedent(r12, T) :- happens(agentdeployed, T, T), not holds_at(personauthorized, T), time(T).

consequent(r12, T) :- time(T), happens(not showdatahistory, T, T).

exp(r13).

antecedent(r13, T) :- happens(userunpredictable, T, T), time(T).

consequent(r13, T) :- time(T), happens(not giveuserdangerousobjects, T, T).

exp(r14).

antecedent(r14, T) :- happens(agentdeployed, T, T), not holds_at(userasksforappropriatetasks, T), time(T).

consequent(r14, T) :- time(T), happens(reminduseroflimitations
    unless ({needlevel} > nmedium), T, T).

exp(r15).

antecedent(r15, T) :- happens(preparingdeployment, T, T), time(T).

consequent(r15, T) :- time(T), happens(agenthasappropriateappearance
    unless {userneedsspecialaccomodations}, T, T).

exp(r16).

antecedent(r16, T) :- happens(preparingdeployment, T, T), time(T).

consequent(r16, T) :- time(T), happens(calibratespeech, T, T).

exp(r17).

antecedent(r17, T) :- happens(givingcookinginstructions, T, T), time(T).

consequent(r17, T) :- time(T), happens(usefirstpersonplurallanguage, T, T).

exp(r18).

antecedent(r18, T) :- happens(beforecookingbegins, T, T), time(T).

consequent(r18, T) :- time(T), happens(askfordetaillevelofinstructions, T, T).

exp(r19).

antecedent(r19, T) :- happens(userchangemind, T, T), time(T).

consequent(r19, T) :- time(T), happens(recalculateapproach
    unless ({risklevel} = high), T, T).

exp(r20_primary).

antecedent(r20_primary, T) :- happens(userchangeitemlocation, T, T), not holds_at(risklevel, high, T), time(T).

consequent(r20_primary, T) :- time(T), happens(updatemap, T, T).

exp(r20_unless1).

antecedent(r20_unless1, T) :- happens(userchangeitemlocation, T, T), holds_at(risklevel, high, T), time(T).

consequent(r20_unless1, T) :- time(T), happens(interferesafely, T, T).

exp(r21).

antecedent(r21, T) :- happens(smokedetectoralarm, T, T), time(T).

consequent(r21, T) :- time(T), happens(callemergencyservices, T, T2), T <= T2, T2 <= T+5, time(T2).

% =============================================================================
% RULE SATISFACTION LOGIC
% =============================================================================

% General holds logic
holds(G, T):-
    time(T), 
    exp(G),
    holds_nv(G, T).

holds(G, T):-
    time(T), 
    exp(G),
    holds_v(G, T).

% Non-vacuous satisfaction for r1
holds_nv(r1, T):-
    time(T),
    antecedent(r1, T),
    consequent(r1, T).

% Vacuous satisfaction for r1
holds_v(r1, T):-
    time(T),
    not antecedent(r1, T),
    not consequent(r1, T).

% Non-vacuous satisfaction for r2
holds_nv(r2, T):-
    time(T),
    antecedent(r2, T),
    consequent(r2, T).

% Vacuous satisfaction for r2
holds_v(r2, T):-
    time(T),
    not antecedent(r2, T),
    not consequent(r2, T).


% Non-vacuous satisfaction for r3_primary
holds_nv(r3_primary, T):-
    time(T),
    antecedent(r3_primary, T),
    consequent(r3_primary, T).


% Vacuous satisfaction for r3_primary
holds_v(r3_primary, T):-
    time(T),
    not antecedent(r3_primary, T),
    not consequent(r3_primary, T).

% Non-vacuous satisfaction for r4
holds_nv(r4, T):-
    time(T),
    antecedent(r4, T),
    consequent(r4, T).

% Vacuous satisfaction for r4
holds_v(r4, T):-
    time(T),
    not antecedent(r4, T),
    not consequent(r4, T).

% Non-vacuous satisfaction for r5
holds_nv(r5, T):-
    time(T),
    antecedent(r5, T),
    consequent(r5, T).

% Vacuous satisfaction for r5
holds_v(r5, T):-
    time(T),
    not antecedent(r5, T),
    not consequent(r5, T).

% Non-vacuous satisfaction for r6
holds_nv(r6, T):-
    time(T),
    antecedent(r6, T),
    consequent(r6, T).

% Vacuous satisfaction for r6
holds_v(r6, T):-
    time(T),
    not antecedent(r6, T),
    not consequent(r6, T).

% Non-vacuous satisfaction for r7
holds_nv(r7, T):-
    time(T),
    antecedent(r7, T),
    consequent(r7, T).

% Vacuous satisfaction for r7
holds_v(r7, T):-
    time(T),
    not antecedent(r7, T),
    not consequent(r7, T).

% Non-vacuous satisfaction for r8
holds_nv(r8, T):-
    time(T),
    antecedent(r8, T),
    consequent(r8, T).

% Vacuous satisfaction for r8
holds_v(r8, T):-
    time(T),
    not antecedent(r8, T),
    not consequent(r8, T).

% Non-vacuous satisfaction for r9
holds_nv(r9, T):-
    time(T),
    antecedent(r9, T),
    consequent(r9, T).

% Vacuous satisfaction for r9
holds_v(r9, T):-
    time(T),
    not antecedent(r9, T),
    not consequent(r9, T).

% Non-vacuous satisfaction for r10
holds_nv(r10, T):-
    time(T),
    antecedent(r10, T),
    consequent(r10, T).

% Vacuous satisfaction for r10
holds_v(r10, T):-
    time(T),
    not antecedent(r10, T),
    not consequent(r10, T).

% Non-vacuous satisfaction for r11
holds_nv(r11, T):-
    time(T),
    antecedent(r11, T),
    consequent(r11, T).

% Vacuous satisfaction for r11
holds_v(r11, T):-
    time(T),
    not antecedent(r11, T),
    not consequent(r11, T).

% Non-vacuous satisfaction for r12
holds_nv(r12, T):-
    time(T),
    antecedent(r12, T),
    consequent(r12, T).

% Vacuous satisfaction for r12
holds_v(r12, T):-
    time(T),
    not antecedent(r12, T),
    not consequent(r12, T).

% Non-vacuous satisfaction for r13
holds_nv(r13, T):-
    time(T),
    antecedent(r13, T),
    consequent(r13, T).

% Vacuous satisfaction for r13
holds_v(r13, T):-
    time(T),
    not antecedent(r13, T),
    not consequent(r13, T).

% Non-vacuous satisfaction for r14
holds_nv(r14, T):-
    time(T),
    antecedent(r14, T),
    consequent(r14, T).

% Vacuous satisfaction for r14
holds_v(r14, T):-
    time(T),
    not antecedent(r14, T),
    not consequent(r14, T).

% Non-vacuous satisfaction for r15
holds_nv(r15, T):-
    time(T),
    antecedent(r15, T),
    consequent(r15, T).

% Vacuous satisfaction for r15
holds_v(r15, T):-
    time(T),
    not antecedent(r15, T),
    not consequent(r15, T).

% Non-vacuous satisfaction for r16
holds_nv(r16, T):-
    time(T),
    antecedent(r16, T),
    consequent(r16, T).

% Vacuous satisfaction for r16
holds_v(r16, T):-
    time(T),
    not antecedent(r16, T),
    not consequent(r16, T).

% Non-vacuous satisfaction for r17
holds_nv(r17, T):-
    time(T),
    antecedent(r17, T),
    consequent(r17, T).

% Vacuous satisfaction for r17
holds_v(r17, T):-
    time(T),
    not antecedent(r17, T),
    not consequent(r17, T).

% Non-vacuous satisfaction for r18
holds_nv(r18, T):-
    time(T),
    antecedent(r18, T),
    consequent(r18, T).

% Vacuous satisfaction for r18
holds_v(r18, T):-
    time(T),
    not antecedent(r18, T),
    not consequent(r18, T).

% Non-vacuous satisfaction for r19
holds_nv(r19, T):-
    time(T),
    antecedent(r19, T),
    consequent(r19, T).

% Vacuous satisfaction for r19
holds_v(r19, T):-
    time(T),
    not antecedent(r19, T),
    not consequent(r19, T).


% Non-vacuous satisfaction for r20_primary
holds_nv(r20_primary, T):-
    time(T),
    antecedent(r20_primary, T),
    consequent(r20_primary, T).


% Vacuous satisfaction for r20_primary
holds_v(r20_primary, T):-
    time(T),
    not antecedent(r20_primary, T),
    not consequent(r20_primary, T).


% Non-vacuous satisfaction for r20_unless1
holds_nv(r20_unless1, T):-
    time(T),
    antecedent(r20_unless1, T),
    consequent(r20_unless1, T).


% Vacuous satisfaction for r20_unless1
holds_v(r20_unless1, T):-
    time(T),
    not antecedent(r20_unless1, T),
    not consequent(r20_unless1, T).

% Non-vacuous satisfaction for r21
holds_nv(r21, T):-
    time(T),
    antecedent(r21, T),
    consequent(r21, T).

% Vacuous satisfaction for r21
holds_v(r21, T):-
    time(T),
    not antecedent(r21, T),
    not consequent(r21, T).

% Hard constraint: every rule must be satisfied at every time point
:- exp(R), time(T), not holds(R,T).

% =============================================================================
% ACTION GENERATION AND CONSTRAINTS
% =============================================================================

% Triggering event instantiation (TriggerTime = ActualTime for direct triggers)
{ happens(givingcookinginstructions, T, T) } :- time(T).
{ happens(smokedetectoralarm, T, T) } :- time(T).
{ happens(agentdeployed, T, T) } :- time(T).
{ happens(beforecookingbegins, T, T) } :- time(T).
{ happens(userunpredictable, T, T) } :- time(T).
{ happens(monitormealtime, T, T) } :- time(T).
{ happens(foodpreparation, T, T) } :- time(T).
{ happens(userwantstocook, T, T) } :- time(T).
{ happens(givesuggestion, T, T) } :- time(T).
{ happens(userchangemind, T, T) } :- time(T).
{ happens(userchangeitemlocation, T, T) } :- time(T).
{ happens(preparingdeployment, T, T) } :- time(T).
{ happens(humanonfloor, T, T) } :- time(T).
{ happens(meetinguser, T, T) } :- time(T).
{ happens(userhaslimitation, T, T) } :- time(T).

% Action event instantiation 
{ happens(recalculateapproach
    unless ({risklevel} = high), T, T) } :- time(T).
{ happens(checktemperature, T, T) } :- time(T).
{ happens(askfordetaillevelofinstructions, T, T) } :- time(T).
{ happens(informuser
    unless {useroccupied}, T, T) } :- time(T).
{ happens(tracktime, T, T) } :- time(T).
{ happens(callemergencyservices, T, T) } :- time(T).
{ happens(agenthasappropriateappearance
    unless {userneedsspecialaccomodations}, T, T) } :- time(T).
{ happens(updatemap, T, T) } :- time(T).
{ happens(calibratespeech, T, T) } :- time(T).
{ happens(informuser, T, T) } :- time(T).
{ happens(consideruserpractices, T, T) } :- time(T).
{ happens(usefirstpersonplurallanguage, T, T) } :- time(T).
{ happens(interferesafely, T, T) } :- time(T).
{ happens(askforemergencycontact, T, T) } :- time(T).
{ happens(allowusertocook, T, T) } :- time(T).
{ happens(reminduseroflimitations
    unless ({needlevel} > nmedium), T, T) } :- time(T).
{ happens(collectandrecordinformation, T, T) } :- time(T).
{ happens(informuser, T1, T2) : T1 <= T2, T2 <= T1+10 } :- time(T1), time(T2).
{ happens(callemergencyservices, T1, T2) : T1 <= T2, T2 <= T1+5 } :- time(T1), time(T2).

% Measure instantiation
{ holds_at(useroccupied, T) } :- time(T).
{ holds_at(timebetweenmeals, V, T) : V = 0..10 } :- time(T).
{ holds_at(personauthorized, T) } :- time(T).
{ holds_at(dataneedschecking, T) } :- time(T).
{ holds_at(userasksforappropriatetasks, T) } :- time(T).
{ holds_at(userneedsspecialaccomodations, T) } :- time(T).
{ holds_at(userdisablesalarm, T) } :- time(T).
{ holds_at(alarmrestarts, T) } :- time(T).
1 { holds_at(needlevel, nlow, T) ; holds_at(needlevel, nmedium, T) ; holds_at(needlevel, nhigh, T) } 1 :- time(T).
{ holds_at(humanassents, T) } :- time(T).
{ holds_at(safepathfound, T) } :- time(T).
{ holds_at(hazarddetected, T) } :- time(T).
{ holds_at(kitchensafe, T) } :- time(T).
1 { holds_at(risklevel, low, T) ; holds_at(risklevel, medium, T) ; holds_at(risklevel, high, T) } 1 :- time(T).
{ holds_at(alarmon, T) } :- time(T).

% =============================================================================
% OUTPUT SPECIFICATION
% =============================================================================

#show holds_at/2.

#show happens/3. 