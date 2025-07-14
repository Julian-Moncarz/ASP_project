%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% DAISY RULE 10 - SLEEC Safety Logic Implementation
% Medical Monitoring System with Temperature-Based Safety Rules
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% 1. DOMAIN DEFINITIONS
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% Available actions the system can perform - these are Events
action(monitorRoom).  %actions
action(callSupport).
action(checkPatient).

% Temperature domain and measurements
t(-20..20).  % temperature ranges from -20 to 20
measure(temp(X)):-t(X).
measure(patientDressed). %patientDressed is a measure
measure(patientResponsive). %patientResponsive is a measure

% SLEEC rule identifier - r1
exp(r1).  %r1 is the name of the SLEEC rule
% every rule needs to have a name - expression ID

% Time domain and priorities
time(0..10). %duration of the trace - time ranges from 0 to 10
pr(1..2).  % wanted to play with priorities - this just says priorities range from 1 to 2
eot(10). % end of time is 10

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% 2. ENVIRONMENT DYNAMICS
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% Temperature evolution: can stay same, increase by 1, or decrease by 1
{holds_at(temp(M),T+1); holds_at(temp(M+1),T+1); holds_at(temp(M-1),T+1)}:-
	time(T), 
	t(M), 
	holds_at(temp(M),T).   % what happens about temperature in each time point: temperature can increase or decrease only by 1 in each successive time point

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% 3. SLEEC RULE DEFINITION
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% Antecedent (WHEN condition): trigger when monitoring and temperature < 15
antecedent(r1,T):-
	time(T),
	happens(monitorRoom,T),
	t(M),
	holds_at(temp(M),T),
	M<15.  % when part

%r1 should have triggered at time T when: 
	% time is at T
	% monitorRoom happens at time T
	% M is a temperature 
	% holds_at(temp(M),T) temp at the time is M
	% temp M is < 15

%antecedent is the cause, consequent is the effect

% Consequent (THEN actions): define response actions with priorities
consequent(r1,T):-
		time(T),
		time(T2),
		T<=T2, % trigger time must be less than the time when the consiquent happens
		pr(P), % this is priority
		consequent(r1,P,T,T2).  % either one of the actions that satisfies the rule occurs

% Note - I don't rules in SLEEC have choice like this currently - rules cannot trigger a choice of events with one being higher priority than the other

%OH! this is a specific consequence of r1 triggering, which has priority 1 - the most important thing to do is checkPatient
consequent(r1,1, T,T2):- 
		time(T), % T is a time
		time(T2), % T2 is also a time
		T<=T2,
		T2<=T+5, % Patched - now is a within statement 'within 5 timesteps'
		happens(checkPatient,T2). % this event happens at T2

% r1,2 means this is priority 2 -  the 2nd most important thing to do is callSupport
consequent(r1,2,T, T2):- 
		time(T),
		time(T2),
		T<=T2,
		T2<=T+10, %Moded to be a within 10 T statement
		happens(callSupport,T2).



%%%%%%%%% QUESTIONS %%%%%%%%%%%%
% For simple rules (when X then Y), do we need more then one consequent statement or would one be enough?

% Check if consequent is met within deadline
consequent_met(r1,T):- 
		time(T), 
		consequent(r1,T).

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% 4. RULE SATISFACTION LOGIC
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% Rule holds if it holds non-vacuously (antecedent true AND consequent met)
holds(G, T):-
	time(T), 
	exp(G),
	holds_nv(G, T).  % a sleec rule is true if it holds vacuously or non-vacuously or holds in the end of time

% Rule holds vacuously (antecedent never true)
holds(G, T):-
	time(T), 
	exp(G),
	holds_v(G, T).  % vacuously

% Rule holds at end-of-time (antecedent was true but consequent not met in time)
holds(G, T):-
	time(T), 
	exp(G),
	holds_eot(G, T).  % end of times

%%%% WHAT IT MEANS FOR RULES TO HOLD:

% End-of-time satisfaction: rule fails if priority 1 deadline missed
holds_eot(r1,T):-
	time(T),
	antecedent(r1,T),
	eot(T2),
	T2-T <= 5,
	not consequent_met(r1,T,T2).

% End-of-time satisfaction: rule succeeds if priority 2 deadline met
holds_eot(r1,T):-
	time(T),
	antecedent(r1,T),
	eot(T2),
	priority(2),
	T2-T <= 10,
	consequent_met(r1,T,T2).

% Non-vacuous satisfaction: antecedent true AND consequent met
holds_nv(r1,T):-
	time(T),
	antecedent(r1,T),
	consequent(r1,T).

% Vacuous satisfaction: antecedent never true
holds_v(r1,T):-
	time(T),
	not antecedent(r1,T).

% Rule declaration
exp(r1). % This is repeated from above

% Cost domain
cost(1..5).

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% 5. RULES MUST ALWAYS BE SATISFIED
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% Hard constraint: every rule must be satisfied at every time point
:- exp(R), time(T), not holds(R,T). 

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% 6. OPTIMIZATION OBJECTIVES
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

plan_cost(N):-
	N= #max {C,T: cost(C,T),time(T),c(C)}.

plan_length(N):-
	N= #count {T: time(T), action(A), happens(A,T)}.

% when trigger/condition is satisfied then add weak constraint that gives lower cost to B over C.
% this doesnot say that the action in consequence 
% should happen sooner

% Minimize response time (prefer faster responses)
#minimize {T2@3: exp(R), time(T), antecedent(R,T),time(T2), consequent(R,_,T, T2)}.

% Minimize priority (prefer lower priority actions when possible)
#minimize {P@3: exp(R), time(T), antecedent(R,T),time(T2), consequent(R,P,T, T2)}.
% P@3 = this is the priority - it optimizes for this within the solutions that optimize higher level concerns (eg @2 or @1)
% Minimize priority - lower number = higher priority. When a rule is triggered, try to satisfy it with the most important things

% Minimize plan length (prefer fewer actions overall)
#minimize {N@2: plan_length(N)}.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% 7. INITIAL STATE AND EVENTS
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% Initial conditions: monitoring starts, temperature is 10 degrees
% assume an event happened at a point of time and something happened in the environment
happens(monitorRoom,0).
holds_at(temp(10),0).

% Additional events for testing
%happens(monitorRoom,0) happens(monitorRoom,1) happens(callSupport,2) holds_nv(r1,0) 
% check why callSupport is triggered
happens(monitorRoom,1).
holds_at(temp(10),1).
% penalising based on response with respect individual triggering of requirements not all 
% check when response is shared that this is the case

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% 8. ACTION GENERATION AND CONSTRAINTS
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% Generate 0 or more actions: ASP chooses which actions to perform when
% here we are asking ASP to generate 0 or more actions with particular goals to generate a plan
0{happens(A,T):action(A), time(T)}.

% temp increment/decrements
% might trigger the req from the initial state
% only one antecedent sat at a time

% Mutual exclusion: only one action can happen at the same time
% you cannot have two actions happening at the same time
:- time(T), action(A), happens(A,T), action(A2), happens(A2,T), A!=A2.

% Temperature consistency: only one temperature value at any time
:- t(M), time(T), holds_at(temp(M1),T), holds_at(temp(M2),T), M1!=M2.
% At any given time T, it must not be the case that two different temperature values (M1 and M2, where M1 ≠ M2) are both held at time T.

% Optional constraint (commented out)
%:- time(T), happens(checkPatient,T), 0<=T, T<=3.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% 9. OUTPUT SPECIFICATION
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% Show which actions happen when
#show happens/2.
% Show which rules are satisfied non-vacuously
#show holds_nv/2.
% Show antecedent conditions
#show antecedent/2.