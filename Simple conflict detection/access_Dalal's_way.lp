%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% TIME
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

time(0..10). 
% duration of the trace - time ranges from 0 to 10

eot(10). 
% end of time is 10

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% ACTIONS
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% these are Events in SLEEC - they must start with a lowercase letter in clingo
% Eg. action(monitorRoom). - this says 'montiorRoom is an action'

action(userLogin).
action(accessGranted).
action(not_accessGranted)

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% MEASURES
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

measure(isBlacklisted). 
measure(hasValidCredentials).

% Generate all possible assignments for the measures
1 { val(isBlacklisted,true); val(isBlacklisted,false) } 1.
1 { val(hasValidCredentials,true); val(hasValidCredentials,false) } 1.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% RULES
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

exp(r1).  % R1: If user logs in and has valid credentials, grant access within 5 steps
exp(r2).  % R2: If user logs in and is blacklisted, deny access

% R1 antecedent: user logs in and has valid credentials
antecedent(r1,T):-
	time(T),
	happens(userLogin,T),
	val(hasValidCredentials,true).

% R1 consequent: grant access within 5 steps
consequent(r1,T):-
	time(T),
	time(T2),
	T<=T2,
	T2<=T+5,
	happens(accessGranted,T2).

% R2 antecedent: user logs in and is blacklisted
antecedent(r2,T):-
	time(T),
	happens(userLogin,T),
	val(isBlacklisted,true).

% R2 consequent: deny access (not accessGranted)
consequent(r2,T):-
	time(T),
	happens(not_accessGranted,T).

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

% R1 holds at end of time if triggered but not satisfied within 5 steps
holds_eot(r1,T):-
	time(T),
	antecedent(r1,T),
	eot(T2),
	T2-T <= 5,
	not consequent(r1,T).

% R2 holds at end of time if triggered but not satisfied
holds_eot(r2,T):-
	time(T),
	antecedent(r2,T),
	eot(T2),
	not consequent(r2,T).

holds_nv(r1,T):-
	time(T),
	antecedent(r1,T),
	consequent(r1,T).

holds_nv(r2,T):-
	time(T),
	antecedent(r2,T),
	consequent(r2,T).

holds_v(r1,T):-
	time(T),
	not antecedent(r1,T).

holds_v(r2,T):-
	time(T),
	not antecedent(r2,T).

% rules MUST hold
:- exp(R), time(T), not holds(R,T). 

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% COST & OPTIMIZATION
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

cost(1..5).

plan_cost(N):-
	N= #max {C,T: cost(C,T),time(T),c(C)}.

plan_length(N):-
	N= #count {T: time(T), action(A), happens(A,T)}.


% Minimze the value of T2 - make the required action happen ASAP after the trigger
#minimize {T2@3: exp(R), time(T), antecedent(R,T),time(T2), consequent(R,_,T, T2)}.

% Minimize priority - lower number = higher priority. When a rule is triggered, try to satisfy it with the most important things
#minimize {P@3: exp(R), time(T), antecedent(R,T),time(T2), consequent(R,P,T, T2)}.

%minimize plan length
#minimize {N@2: plan_length(N)}.


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% GENERATE TRACES
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% Initial state - user logs in
happens(userLogin,0).

% here we are asking ASP to generate 0 or more actions with particular goals to generate a plan
0{happens(A,T):action(A), time(T)}.

% you cannot have two actions happening at the same time
:- time(T), action(A), happens(A,T), action(A2), happens(A2,T), A!=A2.

#show happens/2.
#show holds_nv/2.
#show antecedent/2.
#show val/2.