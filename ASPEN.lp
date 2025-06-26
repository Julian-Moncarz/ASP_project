%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% TIME
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

time(0..10). 
% duration of the trace - time ranges from 0 to 10

eot(10). 
% end of time is 10

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% ACTIONS (Events from SLEEC)
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

action(encounterHuman).
action(humanNearby).
action(identifyActivity).
action(informHuman).
action(informKeeper).
action(backUp).
action(exitArea).
action(preparingDrone).
action(deployDrone).
action(groundDrone).
action(returnHome).
action(monitorLand).
action(monitorCarbon).
action(collectSample).
action(avoidInterference).
action(encounterWildlife).
action(updateTerritories).
action(deletePictures).
action(takePictures).
action(storeData).
action(anonymizeHuman).
action(implementASPEN).
action(ensureCompliance).

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% MEASURES
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% Boolean measures
measure(sameLanguage).
measure(humanUnderstands).
measure(unrelatedActivity).
measure(environmentDangerous).
measure(onIndigenousLand).
measure(landTreatyInPlace).
measure(relevantLand).
measure(privateTerritory).
measure(humanIdentified).
measure(wildlifeDisturbed).
measure(wildlifeInteractswithDrone).
measure(unKnownObject).
measure(damages).

% Scale measures
carbonFootprint(low; medium; high).
benefits(low; medium; high).
flightCondition(dangerous; unsafe; safe; ideal).
battery(high; medium; low).
storage(high; medium; low).

% Measure predicates
measure(carbonFootprint(X)) :- carbonFootprint(X).
measure(benefits(X)) :- benefits(X).
measure(flightCondition(X)) :- flightCondition(X).
measure(battery(X)) :- battery(X).
measure(storage(X)) :- storage(X).

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% RULES
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% R1: when EncounterHuman and ({sameLanguage} and {humanUnderstands}) then InformHuman
exp(r1).
antecedent(r1,T):-
    time(T),
    happens(encounterHuman,T),
    holds_at(sameLanguage,T),
    holds_at(humanUnderstands,T).
consequent(r1,T):-
    time(T),
    time(T2),
    T<=T2,
    consequent(r1,T,T2).
consequent(r1,T,T2):-
    time(T),
    time(T2),
    T<=T2,
    T2<=T+1,
    happens(informHuman,T2).
consequent_met(r1,T,1):-
    time(T),
    time(T2),
    T<=T2,
    T2<=T+1,
    happens(informHuman,T2).

% R2: when EncounterHuman then IdentifyActivity
exp(r2).
antecedent(r2,T):-
    time(T),
    happens(encounterHuman,T).
consequent(r2,T):-
    time(T),
    time(T2),
    T<=T2,
    consequent(r2,T,T2).
consequent(r2,T,T2):-
    time(T),
    time(T2),
    T<=T2,
    T2<=T+1,
    happens(identifyActivity,T2).
consequent_met(r2,T,1):-
    time(T),
    time(T2),
    T<=T2,
    T2<=T+1,
    happens(identifyActivity,T2).

% R2_1: when IdentifyActivity and {unrelatedActivity} then not StoreData
exp(r2_1).
antecedent(r2_1,T):-
    time(T),
    happens(identifyActivity,T),
    holds_at(unrelatedActivity,T).
consequent(r2_1,T):-
    time(T),
    time(T2),
    T<=T2,
    consequent(r2_1,T,T2).
consequent(r2_1,T,T2):-
    time(T),
    time(T2),
    T<=T2,
    not happens(storeData,T2).
consequent_met(r2_1,T,1):-
    time(T),
    time(T2),
    T<=T2,
    T2<=T+1,
    not happens(storeData,T2).

% R3: when HumanNearby and {environmentDangerous} then InformHuman
exp(r3).
antecedent(r3,T):-
    time(T),
    happens(humanNearby,T),
    holds_at(environmentDangerous,T).
consequent(r3,T):-
    time(T),
    time(T2),
    T<=T2,
    consequent(r3,T,T2).
consequent(r3,T,T2):-
    time(T),
    time(T2),
    T<=T2,
    T2<=T+1,
    happens(informHuman,T2).
consequent_met(r3,T,1):-
    time(T),
    time(T2),
    T<=T2,
    T2<=T+1,
    happens(informHuman,T2).

% R4: when PreparingDrone and {onIndigenousLand} then not DeployDrone unless {landTreatyInPlace} then DeployDrone
exp(r4).
antecedent(r4,T):-
    time(T),
    happens(preparingDrone,T),
    holds_at(onIndigenousLand,T).
consequent(r4,T):-
    time(T),
    time(T2),
    T<=T2,
    consequent(r4,T,T2).
consequent(r4,T,T2):-
    time(T),
    time(T2),
    T<=T2,
    not holds_at(landTreatyInPlace,T),
    not happens(deployDrone,T2).
consequent(r4,T,T2):-
    time(T),
    time(T2),
    T<=T2,
    T2<=T+1,
    holds_at(landTreatyInPlace,T),
    happens(deployDrone,T2).
consequent_met(r4,T,1):-
    time(T),
    time(T2),
    T<=T2,
    T2<=T+1,
    not holds_at(landTreatyInPlace,T),
    not happens(deployDrone,T2).
consequent_met(r4,T,1):-
    time(T),
    time(T2),
    T<=T2,
    T2<=T+1,
    holds_at(landTreatyInPlace,T),
    happens(deployDrone,T2).

% R5: when DeployDrone and {relevantLand} then MonitorLand
exp(r5).
antecedent(r5,T):-
    time(T),
    happens(deployDrone,T),
    holds_at(relevantLand,T).
consequent(r5,T):-
    time(T),
    time(T2),
    T<=T2,
    consequent(r5,T,T2).
consequent(r5,T,T2):-
    time(T),
    time(T2),
    T<=T2,
    T2<=T+1,
    happens(monitorLand,T2).
consequent_met(r5,T,1):-
    time(T),
    time(T2),
    T<=T2,
    T2<=T+1,
    happens(monitorLand,T2).

% R6: when CollectSample then AvoidInterference
exp(r6).
antecedent(r6,T):-
    time(T),
    happens(collectSample,T).
consequent(r6,T):-
    time(T),
    time(T2),
    T<=T2,
    consequent(r6,T,T2).
consequent(r6,T,T2):-
    time(T),
    time(T2),
    T<=T2,
    T2<=T+1,
    happens(avoidInterference,T2).
consequent_met(r6,T,1):-
    time(T),
    time(T2),
    T<=T2,
    T2<=T+1,
    happens(avoidInterference,T2).

% R6_1: when DeployDrone then AvoidInterference
exp(r6_1).
antecedent(r6_1,T):-
    time(T),
    happens(deployDrone,T).
consequent(r6_1,T):-
    time(T),
    time(T2),
    T<=T2,
    consequent(r6_1,T,T2).
consequent(r6_1,T,T2):-
    time(T),
    time(T2),
    T<=T2,
    T2<=T+1,
    happens(avoidInterference,T2).
consequent_met(r6_1,T,1):-
    time(T),
    time(T2),
    T<=T2,
    T2<=T+1,
    happens(avoidInterference,T2).

% R7: when PreparingDrone then UpdateTerritories
exp(r7).
antecedent(r7,T):-
    time(T),
    happens(preparingDrone,T).
consequent(r7,T):-
    time(T),
    time(T2),
    T<=T2,
    consequent(r7,T,T2).
consequent(r7,T,T2):-
    time(T),
    time(T2),
    T<=T2,
    T2<=T+1,
    happens(updateTerritories,T2).
consequent_met(r7,T,1):-
    time(T),
    time(T2),
    T<=T2,
    T2<=T+1,
    happens(updateTerritories,T2).

% R7_1: when PreparingDrone and {privateTerritory} then not DeployDrone
exp(r7_1).
antecedent(r7_1,T):-
    time(T),
    happens(preparingDrone,T),
    holds_at(privateTerritory,T).
consequent(r7_1,T):-
    time(T),
    time(T2),
    T<=T2,
    consequent(r7_1,T,T2).
consequent(r7_1,T,T2):-
    time(T),
    time(T2),
    T<=T2,
    not happens(deployDrone,T2).
consequent_met(r7_1,T,1):-
    time(T),
    time(T2),
    T<=T2,
    T2<=T+1,
    not happens(deployDrone,T2).

% R7_2: when DeployDrone and {privateTerritory} then ExitArea
exp(r7_2).
antecedent(r7_2,T):-
    time(T),
    happens(deployDrone,T),
    holds_at(privateTerritory,T).
consequent(r7_2,T):-
    time(T),
    time(T2),
    T<=T2,
    consequent(r7_2,T,T2).
consequent(r7_2,T,T2):-
    time(T),
    time(T2),
    T<=T2,
    T2<=T+1,
    happens(exitArea,T2).
consequent_met(r7_2,T,1):-
    time(T),
    time(T2),
    T<=T2,
    T2<=T+1,
    happens(exitArea,T2).

% R8: when DeployDrone then MonitorCarbon
exp(r8).
antecedent(r8,T):-
    time(T),
    happens(deployDrone,T).
consequent(r8,T):-
    time(T),
    time(T2),
    T<=T2,
    consequent(r8,T,T2).
consequent(r8,T,T2):-
    time(T),
    time(T2),
    T<=T2,
    T2<=T+1,
    happens(monitorCarbon,T2).
consequent_met(r8,T,1):-
    time(T),
    time(T2),
    T<=T2,
    T2<=T+1,
    happens(monitorCarbon,T2).

% R8_1: when DeployDrone and (({carbonFootprint} > low) and ({benefits} < medium)) then InformKeeper
exp(r8_1).
antecedent(r8_1,T):-
    time(T),
    happens(deployDrone,T),
    holds_at(carbonFootprint(X),T),
    X != low,
    holds_at(benefits(Y),T),
    Y = low.
consequent(r8_1,T):-
    time(T),
    time(T2),
    T<=T2,
    consequent(r8_1,T,T2).
consequent(r8_1,T,T2):-
    time(T),
    time(T2),
    T<=T2,
    T2<=T+1,
    happens(informKeeper,T2).
consequent_met(r8_1,T,1):-
    time(T),
    time(T2),
    T<=T2,
    T2<=T+1,
    happens(informKeeper,T2).

% R9: when TakePictures and {humanIdentified} then AnonymizeHuman unless {unrelatedActivity} then DeletePictures
exp(r9).
antecedent(r9,T):-
    time(T),
    happens(takePictures,T),
    holds_at(humanIdentified,T).
consequent(r9,T):-
    time(T),
    time(T2),
    T<=T2,
    consequent(r9,T,T2).
consequent(r9,T,T2):-
    time(T),
    time(T2),
    T<=T2,
    T2<=T+1,
    not holds_at(unrelatedActivity,T),
    happens(anonymizeHuman,T2).
consequent(r9,T,T2):-
    time(T),
    time(T2),
    T<=T2,
    T2<=T+1,
    holds_at(unrelatedActivity,T),
    happens(deletePictures,T2).
consequent_met(r9,T,1):-
    time(T),
    time(T2),
    T<=T2,
    T2<=T+1,
    not holds_at(unrelatedActivity,T),
    happens(anonymizeHuman,T2).
consequent_met(r9,T,1):-
    time(T),
    time(T2),
    T<=T2,
    T2<=T+1,
    holds_at(unrelatedActivity,T),
    happens(deletePictures,T2).

% R10: when ImplementASPEN then EnsureCompliance
exp(r10).
antecedent(r10,T):-
    time(T),
    happens(implementASPEN,T).
consequent(r10,T):-
    time(T),
    time(T2),
    T<=T2,
    consequent(r10,T,T2).
consequent(r10,T,T2):-
    time(T),
    time(T2),
    T<=T2,
    T2<=T+1,
    happens(ensureCompliance,T2).
consequent_met(r10,T,1):-
    time(T),
    time(T2),
    T<=T2,
    T2<=T+1,
    happens(ensureCompliance,T2).

% R11: when DeployDrone and ({flightCondition} < safe) then ReturnHome unless ({flightCondition} = dangerous) then GroundDrone
exp(r11).
antecedent(r11,T):-
    time(T),
    happens(deployDrone,T),
    holds_at(flightCondition(X),T),
    X != safe,
    X != ideal.
consequent(r11,T):-
    time(T),
    time(T2),
    T<=T2,
    consequent(r11,T,T2).
consequent(r11,T,T2):-
    time(T),
    time(T2),
    T<=T2,
    T2<=T+1,
    holds_at(flightCondition(X),T),
    X != dangerous,
    happens(returnHome,T2).
consequent(r11,T,T2):-
    time(T),
    time(T2),
    T<=T2,
    T2<=T+1,
    holds_at(flightCondition(dangerous),T),
    happens(groundDrone,T2).
consequent_met(r11,T,1):-
    time(T),
    time(T2),
    T<=T2,
    T2<=T+1,
    holds_at(flightCondition(X),T),
    X != dangerous,
    happens(returnHome,T2).
consequent_met(r11,T,1):-
    time(T),
    time(T2),
    T<=T2,
    T2<=T+1,
    holds_at(flightCondition(dangerous),T),
    happens(groundDrone,T2).

% R11_cont: when ReturnHome then InformKeeper
exp(r11_cont).
antecedent(r11_cont,T):-
    time(T),
    happens(returnHome,T).
consequent(r11_cont,T):-
    time(T),
    time(T2),
    T<=T2,
    consequent(r11_cont,T,T2).
consequent(r11_cont,T,T2):-
    time(T),
    time(T2),
    T<=T2,
    T2<=T+1,
    happens(informKeeper,T2).
consequent_met(r11_cont,T,1):-
    time(T),
    time(T2),
    T<=T2,
    T2<=T+1,
    happens(informKeeper,T2).

% R11_cont_1: when GroundDrone then InformKeeper
exp(r11_cont_1).
antecedent(r11_cont_1,T):-
    time(T),
    happens(groundDrone,T).
consequent(r11_cont_1,T):-
    time(T),
    time(T2),
    T<=T2,
    consequent(r11_cont_1,T,T2).
consequent(r11_cont_1,T,T2):-
    time(T),
    time(T2),
    T<=T2,
    T2<=T+1,
    happens(informKeeper,T2).
consequent_met(r11_cont_1,T,1):-
    time(T),
    time(T2),
    T<=T2,
    T2<=T+1,
    happens(informKeeper,T2).

% R12: when EncounterWildlife then AvoidInterference unless {wildlifeDisturbed} then BackUp immediately unless {wildlifeInteractswithDrone} then ExitArea within 1 minute
exp(r12).
antecedent(r12,T):-
    time(T),
    happens(encounterWildlife,T).
consequent(r12,T):-
    time(T),
    time(T2),
    T<=T2,
    consequent(r12,T,T2).
consequent(r12,T,T2):-
    time(T),
    time(T2),
    T<=T2,
    T2<=T+1,
    not holds_at(wildlifeDisturbed,T),
    not holds_at(wildlifeInteractswithDrone,T),
    happens(avoidInterference,T2).
consequent(r12,T,T2):-
    time(T),
    time(T2),
    T<=T2,
    T2<=T+1,
    holds_at(wildlifeDisturbed,T),
    not holds_at(wildlifeInteractswithDrone,T),
    happens(backUp,T2).
consequent(r12,T,T2):-
    time(T),
    time(T2),
    T<=T2,
    T2<=T+1,
    holds_at(wildlifeInteractswithDrone,T),
    happens(exitArea,T2).
consequent_met(r12,T,1):-
    time(T),
    time(T2),
    T<=T2,
    T2<=T+1,
    not holds_at(wildlifeDisturbed,T),
    not holds_at(wildlifeInteractswithDrone,T),
    happens(avoidInterference,T2).
consequent_met(r12,T,1):-
    time(T),
    time(T2),
    T<=T2,
    T2<=T+1,
    holds_at(wildlifeDisturbed,T),
    not holds_at(wildlifeInteractswithDrone,T),
    happens(backUp,T2).
consequent_met(r12,T,1):-
    time(T),
    time(T2),
    T<=T2,
    T2<=T+1,
    holds_at(wildlifeInteractswithDrone,T),
    happens(exitArea,T2).

% R12_1: when EncounterWildlife and {wildlifeInteractswithDrone} then InformKeeper
exp(r12_1).
antecedent(r12_1,T):-
    time(T),
    happens(encounterWildlife,T),
    holds_at(wildlifeInteractswithDrone,T).
consequent(r12_1,T):-
    time(T),
    time(T2),
    T<=T2,
    consequent(r12_1,T,T2).
consequent(r12_1,T,T2):-
    time(T),
    time(T2),
    T<=T2,
    T2<=T+1,
    happens(informKeeper,T2).
consequent_met(r12_1,T,1):-
    time(T),
    time(T2),
    T<=T2,
    T2<=T+1,
    happens(informKeeper,T2).

% R13: when PreparingDrone and (({battery} = low) or ({storage} = low) or {damages}) then not DeployDrone
exp(r13).
antecedent(r13,T):-
    time(T),
    happens(preparingDrone,T),
    holds_at(battery(low),T).
antecedent(r13,T):-
    time(T),
    happens(preparingDrone,T),
    holds_at(storage(low),T).
antecedent(r13,T):-
    time(T),
    happens(preparingDrone,T),
    holds_at(damages,T).
consequent(r13,T):-
    time(T),
    time(T2),
    T<=T2,
    consequent(r13,T,T2).
consequent(r13,T,T2):-
    time(T),
    time(T2),
    T<=T2,
    not happens(deployDrone,T2).
consequent_met(r13,T,1):-
    time(T),
    time(T2),
    T<=T2,
    T2<=T+1,
    not happens(deployDrone,T2).

% R14: when DeployDrone and {damages} then InformKeeper
exp(r14).
antecedent(r14,T):-
    time(T),
    happens(deployDrone,T),
    holds_at(damages,T).
consequent(r14,T):-
    time(T),
    time(T2),
    T<=T2,
    consequent(r14,T,T2).
consequent(r14,T,T2):-
    time(T),
    time(T2),
    T<=T2,
    T2<=T+1,
    happens(informKeeper,T2).
consequent_met(r14,T,1):-
    time(T),
    time(T2),
    T<=T2,
    T2<=T+1,
    happens(informKeeper,T2).

% R14_1: when DeployDrone and {damages} then GroundDrone
exp(r14_1).
antecedent(r14_1,T):-
    time(T),
    happens(deployDrone,T),
    holds_at(damages,T).
consequent(r14_1,T):-
    time(T),
    time(T2),
    T<=T2,
    consequent(r14_1,T,T2).
consequent(r14_1,T,T2):-
    time(T),
    time(T2),
    T<=T2,
    T2<=T+1,
    happens(groundDrone,T2).
consequent_met(r14_1,T,1):-
    time(T),
    time(T2),
    T<=T2,
    T2<=T+1,
    happens(groundDrone,T2).

% R15: when DeployDrone and {unKnownObject} then TakePictures
exp(r15).
antecedent(r15,T):-
    time(T),
    happens(deployDrone,T),
    holds_at(unKnownObject,T).
consequent(r15,T):-
    time(T),
    time(T2),
    T<=T2,
    consequent(r15,T,T2).
consequent(r15,T,T2):-
    time(T),
    time(T2),
    T<=T2,
    T2<=T+1,
    happens(takePictures,T2).
consequent_met(r15,T,1):-
    time(T),
    time(T2),
    T<=T2,
    T2<=T+1,
    happens(takePictures,T2).

% R16: when EncounterHuman and {environmentDangerous} then not InformHuman (SAFETY CONFLICT)
exp(r16).
antecedent(r16,T):-
    time(T),
    happens(encounterHuman,T),
    holds_at(environmentDangerous,T).
consequent(r16,T):-
    time(T),
    time(T2),
    T<=T2,
    consequent(r16,T,T2).
consequent(r16,T,T2):-
    time(T),
    time(T2),
    T<=T2,
    not happens(informHuman,T2).
consequent_met(r16,T,1):-
    time(T),
    time(T2),
    T<=T2,
    T2<=T+1,
    not happens(informHuman,T2).

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% HOLDS
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

holds(G, T):-
    time(T), 
    exp(G), 
    holds_nv(G, T).

holds(G, T):-
    time(T), 
    exp(G),
    holds_v(G, T).

holds(G, T):-
    time(T),
    exp(G),
    holds_eot(G, T).

holds_eot(R,T):-
    time(T),
    antecedent(R,T),
    eot(T2),
    T2-T <= 1,
    not consequent_met(R,T,T2).

holds_eot(R,T):-
    time(T),
    antecedent(R,T),
    eot(T2),
    T2-T <= 1,
    consequent_met(R,T,T2).

holds_nv(R,T):-
    time(T),
    antecedent(R,T),
    consequent(R,T).

holds_v(R,T):-
    exp(R),
    time(T),
    not antecedent(R,T).

% rules MUST hold
:- exp(R), time(T), not holds(R,T).

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% COST & OPTIMIZATION
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

plan_length(N):-
    N= #count {T: time(T), action(A), happens(A,T)}.

% Minimize the value of T2 - make the required action happen ASAP after the trigger
#minimize {T2@3: exp(R), time(T), antecedent(R,T),time(T2), consequent(R,T, T2)}.

%minimize plan length
#minimize {N@2: plan_length(N)}.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% GENERATE TRACES
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% Allow up to 5 actions per time step
{ happens(A,T) : action(A) } <= 5 :- time(T).

% Ensure at least one action happens if any rule is triggered
:- holds_v(R,T), not happens(A,T) : action(A), rule_consequent(R,A).

% Optimization: prioritize rule satisfaction, then minimize unnecessary actions
#maximize { 1@2,R,T : holds_v(R,T) }.
#minimize { 1@1,A,T : happens(A,T) }.

% Allow any boolean measure to be true at any time
{ holds_at(M,T) : measure(M) } :- time(T).

% Allow scale measures to have any value at any time
{ holds_at(carbonFootprint(X),T) : carbonFootprint(X) } :- time(T).
{ holds_at(benefits(X),T) : benefits(X) } :- time(T).
{ holds_at(flightCondition(X),T) : flightCondition(X) } :- time(T).
{ holds_at(battery(X),T) : battery(X) } :- time(T).
{ holds_at(storage(X),T) : storage(X) } :- time(T).

% Boolean measures can only be true or false
:- time(T), measure(M), holds_at(M,T), holds_at(M,T2), T != T2.

% Scale measures can only have one value at a time
:- time(T), holds_at(carbonFootprint(X),T), holds_at(carbonFootprint(Y),T), X!=Y.
:- time(T), holds_at(benefits(X),T), holds_at(benefits(Y),T), X!=Y.
:- time(T), holds_at(flightCondition(X),T), holds_at(flightCondition(Y),T), X!=Y.
:- time(T), holds_at(battery(X),T), holds_at(battery(Y),T), X!=Y.
:- time(T), holds_at(storage(X),T), holds_at(storage(Y),T), X!=Y.

#show happens/2.
#show holds_nv/2.
#show holds_v/2.
#show holds_eot/2.
#show antecedent/2. 