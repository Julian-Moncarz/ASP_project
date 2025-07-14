%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%                           SIMPLE SLEEC RULE IMPLEMENTATION
%                              When OpenDoor and isDaytime then PlaySound
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%                              1. DOMAIN DEFINITIONS
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% Events
event(openDoor).
event(playSound).

% Measures
measure(isDaytime).

% Time domain
time(0..10).

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%                              2. SIMPLE RULE IMPLEMENTATION
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% Rule identifier
exp(r1).            % r1 is the name of the SLEEC rule

% ----------------------------- ANTECEDENT LOGIC -----------------------------
% The rule is triggered when OpenDoor is true at time T
antecedent(r1,T):-
	time(T),
	happens(openDoor,T),
	holds_at(isDaytime,T).

% ----------------------------- CONSEQUENT LOGIC -----------------------------
% NOTE: LINA SAID ON THE CALL THE CONSEQUENTS HAPPEN AT THE SAME TIMESTEP AS THE ANTECEDENT
% unless there is a within statement

consequent(r1,T) :- 
    time(T),
    happens(playSound,T).

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%                           3. RULE SATISFACTION LOGIC
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% ----------------------------- GENERAL HOLDS LOGIC -------------------------
% Rule holds if it holds non-vacuously (antecedent true AND consequent met)
holds(G, T):-
	time(T), 
	exp(G),
	holds_nv(G, T).

% Rule holds vacuously (antecedent never true)
holds(G, T):-
	time(T), 
	exp(G),
	holds_v(G, T).

% ----------------------------- SPECIFIC HOLDS LOGIC ------------------------
% WHAT IT MEANS FOR RULES TO HOLD:
% simple rules without within statements happen at the same time as the antecedent - 
% therefore, they cannot hold at the end of time

% Non-vacuous satisfaction: antecedent true AND consequent met
holds_nv(r1,T):-
	time(T),
	antecedent(r1,T),
	consequent(r1,T).

% Vacuous satisfaction: antecedent not true AND consequent does not happen
holds_v(r1,T):-
	time(T),
	not antecedent(r1,T),
	not consequent(r1,T).

% ----------------------------- HARD CONSTRAINTS ----------------------------
% Hard constraint: every rule must be satisfied at every time point
:- exp(R), time(T), not holds(R,T).

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%                              4. OUTPUT SPECIFICATION
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% Generate 0 or more events: ASP chooses which events to perform when
% here we are asking ASP to generate 0 or more events with particular goals to generate a plan
0{happens(A,T):event(A), time(T)}.

% ----------------------------- OPTIMIZATION ---------------------------------
% Plan length calculation
%plan_length(N):-
%	N= #count {T: time(T), event(A), happens(A,T)}.

% Minimize plan length (prefer fewer events overall)
%#minimize {N@2: plan_length(N)}.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%                            5. OUTPUT SPECIFICATION
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

holds_at(isDaytime, 0).
holds_at(isDaytime, 1).

% Show which events happen when
#show holds_at/2.
#show happens/2.