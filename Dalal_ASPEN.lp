%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% implimenting  R1 when EncounterHuman then IdentifyActivity
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% 1. DOMAIN DEFINITIONS
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% these are actions (events that the system can perform)
action(identifyActivity).

% Time domain and priorities
time(0..10). %duration of the trace - time ranges from 0 to 10
eot(10). % end of time is 10

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% 2. SLEEC RULE SPECIFICATION
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

exp(r1).  %r1 is the name of the SLEEC rule

antecedent(r1,T):-
	time(T),
	happens(encounterHuman,T).

consequent_met(r1,T):-
	time(T),
	antecedent(r1,T),
	time(T2),
	T2 >= T,
	T2 <= T+1,
	happens(identifyActivity,T2).

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% 3. RULE SATISFACTION
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% Three ways for rules to hold:
% 1. Non-vacuously: antecedent true AND consequent met within timeframe
% 2. Vacuously: antecedent never true
% 3. End-of-time: antecedent true but insufficient time for consequent

% Rule holds non-vacuously (antecedent true AND consequent met)
holds_nv(r1,T) :-
	time(T),
	antecedent(r1,T),
	consequent_met(r1,T).

% Rule holds vacuously (antecedent never true)
holds_v(r1,T) :-
	time(T),
	not antecedent(r1,T).

% Rule holds at end-of-time (antecedent true but no time left for consequent)
holds_eot(r1,T) :-
	time(T),
	antecedent(r1,T),
	eot(EOT),
	T+1 > EOT,
	not consequent_met(r1,T).

% Rule satisfaction at any time
holds(r1,T) :-
	time(T),
	holds_nv(r1,T).

holds(r1,T) :-
	time(T),
	holds_v(r1,T).

holds(r1,T) :-
	time(T),
	holds_eot(r1,T).

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% 4. EVENT GENERATION
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% Choice: encounterHuman may happen at any time
{ happens(encounterHuman, T) } :- time(T).

% Generate actions as needed to satisfy rules
{ happens(A,T) : action(A), time(T) }.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% 5. CONSTRAINTS
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% Every rule must be satisfied at every time point
:- exp(R), time(T), not holds(R,T).

% ADDITIONAL CONSTRAINT: identifyActivity can only happen if it helps satisfy a rule
:- happens(identifyActivity,T), 
   not antecedent_within_window(T).

antecedent_within_window(T) :-
   time(T),
   time(T1),
   antecedent(r1,T1),
   T >= T1,
   T <= T1+1.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% 6. OUTPUT
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

#show happens/2.
#show holds_nv/2.