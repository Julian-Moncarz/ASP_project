%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%                           COMPLEX SLEEC RULE REQUIRING NORMALIZATION
%
% Original SLEEC Rule:
% R1 when OpenDoor and (({isDaytime} or {isWeekend}) and not ({isRaining} and {isWindy})) then PlaySound
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%                              1. DOMAIN DEFINITIONS
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% Events
event(openDoor).
event(playSound).

% Measures
measure(isDaytime).
measure(isWeekend).
measure(isRaining).
measure(isWindy).

% Time domain
time(0..10).

% Rule identifiers (generic pattern)
exp(r1).

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%                    2. SYSTEMATIC NORMALIZATION PATTERN
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% PROGRAMMATIC APPROACH: Break complex conditions into reusable components
%
% Pattern: For any complex rule "when A and (B or C) and not (D and E) then F"
% Step 1: Create intermediate_condition_1 for (B or C)  
% Step 2: Create intermediate_condition_2 for not (D and E) using De Morgan's
% Step 3: Create combined_antecedent for A and intermediate_condition_1 and intermediate_condition_2
% Step 4: Map to specific rule consequences
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% ----------------------------- INTERMEDIATE CONDITIONS (REUSABLE) -----------

% Intermediate condition 1:
% Pattern: ({isDaytime} or {isWeekend}) -> condition_1(T)
condition_1(T) :-
    time(T),
    holds_at(isDaytime, T).

condition_1(T) :-
    time(T),
    holds_at(isWeekend, T).

% Intermediate condition 2:
% Pattern: not ({isRaining} and {isWindy}) -> condition_2(T)
condition_2(T) :-
    time(T),
    not holds_at(isRaining, T).

condition_2(T) :-
    time(T),
    not holds_at(isWindy, T).

% Combined antecedent condition
% Pattern: Event and condition_1 and condition_2
complex_antecedent_satisfied(T) :-
    time(T),
    happens(openDoor, T),
    condition_1(T),
    condition_2(T).

% ----------------------------- RULE-SPECIFIC MAPPINGS (PROGRAMMATIC) --------
% Generic pattern: antecedent(RuleId, T) :- complex_antecedent_satisfied(T).

antecedent(r1, T) :-
    time(T),
    complex_antecedent_satisfied(T).

% ----------------------------- RULE-SPECIFIC CONSEQUENTS (MAPPABLE) ---------
% Pattern: consequent(RuleId, T) :- happens(SpecificEvent, T).

consequent(r1, T) :-
    time(T),
    happens(playSound, T).

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%                           3. GENERIC RULE SATISFACTION LOGIC
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% This logic is completely generic and works for any normalized rule

% Rule holds if it holds non-vacuously (antecedent true AND consequent met)
holds(R, T):-
	time(T), 
	exp(R),
	holds_nv(R, T).

% Rule holds vacuously (antecedent never true)
holds(R, T):-
	time(T), 
	exp(R),
	holds_v(R, T).

% Non-vacuous satisfaction (generic pattern)
holds_nv(R, T):-
	time(T),
	exp(R),
	antecedent(R, T),
	consequent(R, T).

% Vacuous satisfaction (generic pattern)
holds_v(R, T):-
	time(T),
	exp(R),
	not antecedent(R, T),
	not consequent(R, T).

% Generic constraint: every rule must be satisfied
:- exp(R), time(T), not holds(R,T).

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%                              4. EVENT GENERATION
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% Generate 0 or more events: ASP chooses which events to perform when
0{happens(A,T):event(A), time(T)}.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%                            5. SAMPLE SCENARIO
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% Test scenario: Daytime on a rainy day
holds_at(isDaytime, 0).
holds_at(isDaytime, 1).
holds_at(isRaining, 0).
holds_at(isRaining, 1).

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%                            6. SYSTEMATIC OUTPUT (DEBUGGABLE)
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% Show intermediate conditions for debugging normalization
#show holds_at/2.
#show happens/2.
#show time_condition_good/1.
#show weather_condition_safe/1.
#show complex_antecedent_satisfied/1.
#show antecedent/2.
#show consequent/2.
#show holds/2.