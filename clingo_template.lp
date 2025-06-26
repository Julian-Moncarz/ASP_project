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

action(monitorRoom).
action(checkPatient).
action(callSupport).

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% MEASURES
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

t(-20..20).  % temperature ranges from -20 to 20
measure(temp(X)) :- t(X).
measure(patientDressed). 
measure(patientResponsive).


% Temperature can increase or decrease by 1, or say the same, in each successive time point

{holds_at(temp(M),T+1); holds_at(temp(M+1),T+1); holds_at(temp(M-1),T+1)}:-
	time(T), 
	t(M), 
	holds_at(temp(M),T).   
    
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% RULES
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

pr(1..2).  % priorities can be from 1 to 2 (so 1 or 2)

exp(r1).  %r1 is the name of the SLEEC rule 

antecedent(r1,T):-
	time(T),
	happens(monitorRoom,T),
	t(M),
	holds_at(temp(M),T),
	M<15.  % when part

consequent(r1,T):-
		time(T),
		time(T2),
		T<=T2, % trigger time must be less than effect time? What is T vs T2?
		pr(P), % OHH this is priority
		consequent(r1,P,T,T2).  % this thing activates

% Priority 1 response:
consequent(r1,1, T,T2):- % what does the r1,1 mean?
		time(T), % T is a time
		time(T2), % T2 is also a time
		T<=T2,
		T2<=T+5, % T2 must be less than or equal to 5 - if we want this to be a within statement, should it not be T2 - T <= 5 ? OR T2 <= T+5
		happens(checkPatient,T2). % this even happens at T2
		% Moded it to be a within statement

consequent_met(r1,1, T,5):-
		time(T),
		time(T1),
		time(T2),
		T<=T1,
		T1<=T+5,
		consequent(r1,T).        

% Priority 2 response:
consequent(r1,2,T, T2) :- 
		time(T),
		time(T2),
		T<=T2,
		T2<=T+10, %Moded to be a within 10 T statement
		happens(callSupport,T2).


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% HOLDS
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

holds(G, T):-
	time(T), 
	exp(G), % exp = ?
	holds_nv(G, T).  % a sleec rule is true if it holds vacuously or non-vacuously or holds in the end of time 

holds(G, T):-
	time(T), 
	exp(G),
	holds_v(G, T).  % vacuously

holds(G, T):-
	time(T),
	exp(G),
	holds_eot(G, T).  % end of times

holds_eot(r1,T):-
	time(T),
	antecedent(r1,T),
	eot(T2),
	T2-T <= 5,
	not consequent_met(r1,T,T2).

holds_eot(r1,T):-
	time(T),
	antecedent(r1,T),
	eot(T2),
	pr(2),
	T2-T <= 10,
	consequent_met(r1,T,T2).

holds_nv(r1,T):-
	time(T),
	antecedent(r1,T),
	consequent(r1,T).

holds_v(r1,T):-
	time(T),
	not antecedent(r1,T).

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

% Initial state
happens(monitorRoom,0).
holds_at(temp(10),0).


% here we are asking ASP to generate 0 or more actions with particular goals to generate a plan
0{happens(A,T):action(A), time(T)}.

% you cannot have two actions happening at the same time
:- time(T), action(A), happens(A,T), action(A2), happens(A2,T), A!=A2.

% At any given time T, it must not be the case that two different temperature values (M1 and M2, where M1 ≠ M2) are both held at time T.
:- t(M), time(T), holds_at(temp(M1),T), holds_at(temp(M2),T), M1!=M2.

#show happens/2.
#show holds_nv/2.
#show antecedent/2.