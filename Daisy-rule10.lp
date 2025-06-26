action(monitorRoom).  %actions - these are Events they should be CapsCase
action(callSupport).
action(checkPatient).

t(-20..20).  % temperature ranges from -20 to 20
measure(temp(X)):-t(X).
measure(patientDressed). %patientDressed is a measure
measure(patientResponsive). %patientResponsive is a measure

exp(r1).  %r1 is the name of the SLEEC rule 
% r1 is an exp whatever that means.

time(0..10). %duration of the trace - time ranges from 0 to 10

pr(1..2).  % wanted to play with priorities - this just says priorities range from 1 to 2?

eot(10). % end of time is 10

{holds_at(temp(M),T+1); holds_at(temp(M+1),T+1); holds_at(temp(M-1),T+1)}:-
	time(T), 
	t(M), 
	holds_at(temp(M),T).   % what happens about temperature in each time point:  temperature can increase or decrease only by 1 in each successive time point

% I don't understand this

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

antecedent(r1,T):-
	time(T),
	happens(monitorRoom,T),
	t(M),
	holds_at(temp(M),T),
	M<15.  % when part

%r1 triggers at time T when: 
	% time is at t
	% montiorRoom happens at time
	% M is a temperature - this can be anything there are no bounds
	% holds_at(temp(M),T) - I dont understand this really
	% temp M is < 15

%antecedent is the cause, consequent is the effect


consequent(r1,T):-
		time(T),
		time(T2),
		T<=T2, % trigger time must be less than effect time? What is T vs T2?
		pr(P), % OHH this is priority
		consequent(r1,P,T,T2).  % this thing activates

% r1 is consequent at time T when 

%OHHH this is a specific consequence of r1 tiggering, which has priority 1 - the most important thing to do is checkPatient
consequent(r1,1, T,T2):- % what does the r1,1 mean?
		time(T), % T is a time
		time(T2), % T2 is also a time
		T<=T2,
		T2<=T+5, % T2 must be less than or equal to 5 - if we want this to be a within statement, should it not be T2 - T <= 5 ? OR T2 <= T+5
		happens(checkPatient,T2). % this even happens at T2
		% Moded it to be a within statement

% what does r1,2 mean? -  is this rule 1.2?
% it means this is priority 2! The 2nd most important thing to do is callSupport
consequent(r1,2,T, T2):- 
		time(T),
		time(T2),
		T<=T2,
		T2<=T+10, %Moded to be a within 10 T statement
		happens(callSupport,T2).

% r1.2 triggers when callSupport at T2 (which must happen within 10?)

consequent_met(r1,1, T,5):-
		time(T),
		time(T1),
		time(T2),
		T<=T1,
		T1<=T+5,
		consequent(r1,T).

% when consequent_met - what does this mean? hmm

%%%%%%%%%
holds(G, T):-
	time(T), 
	exp(G), % exp = ?
	holds_nv(G, T).  % a sleec rule is true if it holds vacuously or non-vacuously or holds in the end of time 

% what is vacuously?

%rule G holds at time T when: 
	%T is a time
	%G is a rule ('exp')
	%G holds non vacuously at time T

holds(G, T):-
	time(T), 
	exp(G),
	holds_v(G, T).  % vacuously

holds(G, T):-
	time(T),
	exp(G),
	holds_eot(G, T).  % end of times
%%%%%%%%%


%%%% WHAT IT MEANS FOR RULES TO HOLD:


holds_eot(r1,T):-
	time(T),
	antecedent(r1,T),
	eot(T2),
	T2-T <= 5,
	not consequent_met(r1,T,T2).

% a rule holds at the end of time if:
	% T is a time	
	% r1 triggers (antecddent) at time t
	% T2 is the end of time
	% T2-T <= 5 - within 5 timesteps! This is how to encode within statements
	% there is no proof that the consequent of r1 is met. ahhh that makes sense

holds_eot(r1,T):-
	time(T),
	antecedent(r1,T),
	eot(T2),
	priority(2),
	T2-T <= 10,
	consequent_met(r1,T,T2).

% a rule holds at eot iof:
% a rule holds at the end of time if:
%   - T is a time
%   - r1 triggers (antecedent) at time T
%   - T2 is the end of time
%   - priority(2) is 2 / 2 is a priority
%   - T2-T <= 10 within 10 timesteps
%   - the consequent of r1 is met

% (already present above)

% You may want to define what priority(2) means if not already defined:
priority(2).

holds_nv(r1,T):-
	time(T),
	antecedent(r1,T),
	consequent(r1,T).

holds_v(r1,T):-
	time(T),
	not antecedent(r1,T).

% A rule holds if it has both its cause and its effect at time T (antecedent and consequent) 
% It also holds if there is no proof of its antecedent at time T

exp(r1). % This is repeated from above

cost(1..5).

:- exp(R), time(T), not holds(R,T). % it is not allowed for R to be a rule, for T to be a time and for there to be no proof the the rule holds at time T - rules MUST holds
% idk why rules must hold

% ignore from here until line 126 inclusive! - ??
plan_cost(N):-
	N= #max {C,T: cost(C,T),time(T),c(C)}.

% the cost of a plan is the max of Cost and Time, such that C at T is a cost, T is a time and C is a c ?
% This needs terms to be defined in other places - you need to define cost!

plan_length(N):-
	N= #count {T: time(T), action(A), happens(A,T)}.

%plan length is the count of times T such that T is a time, A is an action and action A happens at a Time

% when trigger/condition is satisfied then add weak constraint that gives lower cost to B over C.

% this doesnot say that the action in consequence 
% should happen sooner

%#minimize {T2@3: exp(R), time(T), antecedent(R,T),time(T2), consequent(R,_,T, T2)}.
% Minimze the value of T2 such that blah blah blah
% Make the required action happen ASAP after the trigger


%#minimize {P@3: exp(R), time(T), antecedent(R,T),time(T2), consequent(R,P,T, T2)}.
% P@3 = this is the priority - it optimizes for this within the solutions that optimize higher level concerns (eg @2 or @1)
% Minimize priority - lower number = higher priority. When a rule is triggered, try to satisfy it with the most important things


%#minimize {N@2: plan_length(N)}.
%minimize plan length - plan length is not defined anywhere yet

% assume an event happened at a point of time and something happened in the environment
happens(monitorRoom,0).
holds_at(temp(10),0).




%happens(monitorRoom,0) happens(monitorRoom,1) happens(callSupport,2) holds_nv(r1,0) 
% check why callSupport is triggered
%happens(monitorRoom,1).
%holds_at(temp(10),1).
% penalising based on response with respect individual triggering of requirements not all 
% check when response is shared that this is the case


% here we are asking ASP to generate 0 or more actions with particular goals to generate a plan
0{happens(A,T):action(A), time(T)}.

% temp increment/decrements
% might trigger the req from the initial state
% only one antecddent sat at a time

% you cannot have two actions happening at the same time
:- time(T), action(A), happens(A,T), action(A2), happens(A2,T), A!=A2.


:- t(M), time(T), holds_at(temp(M1),T), holds_at(temp(M2),T), M1!=M2.
% At any given time T, it must not be the case that two different temperature values (M1 and M2, where M1 ≠ M2) are both held at time T.

%:- time(T), happens(checkPatient,T), 0<=T, T<=3.

#show happens/2.
#show holds_nv/2.
#show antecedent/2.