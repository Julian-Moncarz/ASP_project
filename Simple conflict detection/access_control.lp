% Generate all possible assignments for the measures
1 { val(isBlacklisted,true); val(isBlacklisted,false) } 1.
1 { val(hasValidCredentials,true); val(hasValidCredentials,false) } 1.
1 { val(userLogin,true); val(userLogin,false) } 1.

% R1
accessGranted :- val(userLogin,true), val(hasValidCredentials,true).

% R2
notAccessGranted :- val(userLogin,true), val(isBlacklisted,true).

% There is a conflict if both accessGranted and notAccessGranted are true
conflict :- accessGranted, notAccessGranted.

% Only show models where a conflict occurs
:- not conflict.

#show val/2.