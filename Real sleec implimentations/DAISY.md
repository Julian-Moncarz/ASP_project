## DAISY

**Case study title:** DAISY

**Description**

*This case-study is drawn from a proposed A&E triage AI-enabled system -
the Diagnostic AI System for Robot-Assisted ED Triage (or 'DAISY').*

*DAISY is a semi-autonomous, sociotechnical AI-supported system that
directs patients through an A&E triage pathway. DAISY will capture data
by enabling a patient to input subjective information - about themselves
and their condition - and will support the patient in using wirelessly
connected medical devices to capture and record objective data - such
as, blood pressure, pulse rate, temperature, and so on. Following data
collection, patients will then be guided back to a waiting area. DAISY
will utilise a complex, rule-based, 'dAvInci' (or Diagnostic Algorithm
for Intelligent Clinical Intervention) algorithm developed by acute-care
clinicians to link patient characteristics, demographics, and symptoms,
viewed through the patient's objective vital signs, to possible clinical
states, urgency, and early treatment options. The algorithm will return
a detailed report that contains a set of possible early diagnoses, as
well as suggested continued investigations, based on the objective and
subjective data. These preliminary findings are approved, amended, or
rejected by the clinician to facilitate the early stages of triage. An
assessment with appropriate advisory information regarding a preliminary
diagnosis and treatment plan is then produced which the clinician
reviews and discusses with the patient.*

*Once operational, DAISY will expedite and direct the triage process by
better facilitating patient observations and providing clinicians with a
preliminary patient report. The DAISY system identifies potential
patient maladies and suggests further investigations and patient
referrals. The system returns possible or suggested output given the
patient data. Considering these as logical statements enables each of
the information types (demographic, anatomic, subjective, and objective)
to be considered in parallel for efficient rule checking for maladies,
such that the intersections of the resultant data type rules are
possibilities.*

*While these potential diagnoses are useful for identifying additional
tests or providing potential avenues for additional investigation, the
benefit of the DAISY system is in the rapid categorisation of patients
by severity, identification, and escalation of the critically unwell
patients - and the generation of medically approved investigation plans.
Clinical personnel can thereby streamline the early elements of the
process to allow for additional treatment time and more effective
resource management in critical cases. DAISY is not intended to triage
patients at the highest tier of triage illness -- that is, those
considered to be in need of immediate life-saving intervention.*

**Stage of Development (Technical contributor)**

*Proto*

**Expert info**

Expertise of the stakeholders involved in devising the SLEEC rules

Number of stakeholders writing the rules

  -----------------------------------------------------------------------
  Stakeholder names                   Expertise
  ----------------------------------- -----------------------------------
  N-TS-1                              Law and Ethics

  N-TS-2                              Moral Psychology

  N-TS-3                              Moral Psychology, Law

  TS-1                                Engineer/Goal Modelling
  -----------------------------------------------------------------------

**Normative requirements**

1.  **Normative requirements in natural language\
    \**
    *Normative requirements in natural language, in blue the corrected
    requirements after using N-Tool.*

Impact keys: A = autonomy, P = privacy, E = explainability, T =
transparency, CS = cultural sensitivity, SR = social requirement, B =
beneficence (doing good), N = non-maleficence (preventing/avoiding
harm), PH = psychological/mental health, S = safety, F = fairness, A =
accountability.\
''+" and "-" for positive and negative impacts respectively.\
In blue, the stakeholders corrections after analyzing the
well-formedness of the rules using our LEGOS-CHECK.

**\
\**

+----------------+------------------------------------+------------------+------------------+------------------+------------------+
| rule id        | rule                               | impact           | label(s)\        | stakeholder\     | authors          |
|                |                                    |                  | (social, legal,  | expertise        |                  |
|                |                                    |                  | ethical,         |                  |                  |
|                |                                    |                  | empathetic, or   |                  |                  |
|                |                                    |                  | cultural)        |                  |                  |
+----------------+------------------------------------+------------------+------------------+------------------+------------------+
| 1              | Address the user by their          | +SR +C           | ethical,         | Law,             | N-TS-1           |
|                | preferred name according to        |                  |                  |                  |                  |
|                | cultural type                      | +B               | social,\         | Ethics           |                  |
|                |                                    |                  | cultural         |                  |                  |
|                | - unless the user's name is        |                  |                  |                  |                  |
|                |   unknown then address them as     |                  |                  |                  |                  |
|                |   Default Name: Sir/Madam          |                  |                  |                  |                  |
|                |                                    |                  |                  |                  |                  |
|                | - unless the user directly         |                  |                  |                  |                  |
|                |   instructs otherwise              |                  |                  |                  |                  |
+----------------+------------------------------------+------------------+------------------+------------------+------------------+
| 2              | Do not disclose personal           | +P\              | legal,\          | Law,             | N-TS-1           |
|                | information pertaining to the user | +E               | ethical          |                  |                  |
|                |                                    |                  |                  | Ethics           |                  |
|                | - unless it is directly to the     | +A               |                  |                  |                  |
|                |   user                             |                  |                  |                  |                  |
|                |                                    |                  |                  |                  |                  |
|                | - unless you have the user's       |                  |                  |                  |                  |
|                |   consent to disclose the          |                  |                  |                  |                  |
|                |   information to a named person    |                  |                  |                  |                  |
|                |                                    |                  |                  |                  |                  |
|                | - unless it is a medical emergency |                  |                  |                  |                  |
+----------------+------------------------------------+------------------+------------------+------------------+------------------+
| 3              | When the cultural indicator is A   | +CS +SR +A +E    | cultural,        | Law,             | N-TS-1           |
|                | and gender type is B, request the  |                  |                  |                  |                  |
|                | presence of a human                | +B               | social,          | Ethics           |                  |
|                | agent/chaperone                    |                  |                  |                  |                  |
|                |                                    |                  | ethical          |                  |                  |
|                | - unless the user advises          |                  |                  |                  |                  |
|                |   otherwise                        |                  |                  |                  |                  |
|                |                                    |                  |                  |                  |                  |
|                | - unless there is a medical        |                  |                  |                  |                  |
|                |   emergency                        |                  |                  |                  |                  |
+----------------+------------------------------------+------------------+------------------+------------------+------------------+
| 4              | Speak to the user in the language  | +T +E            | legal            | Law,\            | N-TS-1           |
|                | of their choice                    |                  |                  | Ethics           |                  |
|                |                                    | +B               |                  |                  |                  |
|                | - unless the language preference   |                  |                  |                  |                  |
|                |   is unknown, then use the Default | +SR              |                  |                  |                  |
|                |   Language: English                |                  |                  |                  |                  |
|                |                                    | +A               |                  |                  |                  |
|                | - unless the user advises          |                  |                  |                  |                  |
|                |   otherwise                        |                  |                  |                  |                  |
+----------------+------------------------------------+------------------+------------------+------------------+------------------+
| 5              | If the user requests information,  | +P +A +E         | legal            | Law,\            | N-TS-1\          |
|                | provide information                |                  |                  | Ethics           | N-TS-3           |
|                |                                    | +T               |                  |                  |                  |
|                | - unless information not           |                  |                  |                  |                  |
|                |   available, inform user and refer |                  |                  |                  |                  |
|                |   to the human carer               |                  |                  |                  |                  |
|                |                                    |                  |                  |                  |                  |
|                | - unless information disclosure    |                  |                  |                  |                  |
|                |   not permitted (for example,      |                  |                  |                  |                  |
|                |   personal, sensitive, or medical  |                  |                  |                  |                  |
|                |   information), not disclose the   |                  |                  |                  |                  |
|                |   information                      |                  |                  |                  |                  |
|                |                                    |                  |                  |                  |                  |
|                | > and inform user and refer to     |                  |                  |                  |                  |
|                | > human carer                      |                  |                  |                  |                  |
+----------------+------------------------------------+------------------+------------------+------------------+------------------+
| 6              | If the user fails to follow an     | +B               | Legal,           | Law,\            | N-TS-1           |
|                | instruction, repeat the            |                  |                  | Ethics           |                  |
|                | instruction                        | +N               | ethical          |                  |                  |
|                |                                    |                  |                  |                  |                  |
|                | - unless the instruction has been  | +SR              |                  |                  |                  |
|                |   repeated 3X, then call for       |                  |                  |                  |                  |
|                |   support                          | +S               |                  |                  |                  |
|                |                                    |                  |                  |                  |                  |
|                | - unless time lapse \> 20 minutes, | +PH              |                  |                  |                  |
|                |   then call support                |                  |                  |                  |                  |
+----------------+------------------------------------+------------------+------------------+------------------+------------------+
| 7              | Get the user\'s consent prior to   | +SR              | Ethical          | Psychology       | N-TS-2           |
|                | being examined.                    |                  |                  |                  |                  |
|                |                                    | +A               | Legal            | Moral            | N-TS-1           |
|                | - unless user cannot consent due   |                  |                  |                  |                  |
|                |   to inability to communicate      | +S               | Social           |                  |                  |
|                |                                    |                  |                  |                  |                  |
|                | - if the user is not old enough to |                  |                  |                  |                  |
|                |   consent (based on the legal age  |                  |                  |                  |                  |
|                |   of consent of the                |                  |                  |                  |                  |
|                |   country/region), ask consent     |                  |                  |                  |                  |
|                |   from their legal                 |                  |                  |                  |                  |
|                |   representatives.                 |                  |                  |                  |                  |
+----------------+------------------------------------+------------------+------------------+------------------+------------------+
| 8              | Confirm assent/permission for      | +SR              | Ethical          | Psychology       | N-TS-2           |
|                | specific tasks before performing   |                  |                  |                  |                  |
|                | them                               | +A               | Legal            | Moral            | N-TS-1           |
|                |                                    |                  |                  |                  |                  |
|                |                                    | +S               | Social           | Engineer/Goal    | TS-1             |
|                |                                    |                  |                  | Modelling        |                  |
+----------------+------------------------------------+------------------+------------------+------------------+------------------+
| 9              | Ensure that the user understands   | +SR              | Ethical          | Psychology\      | N-TS-2           |
|                | what DAISY is doing.               |                  |                  | Moral            |                  |
|                |                                    | +A               |                  |                  | N-TS-1           |
|                | - Ensure that they pay attention   |                  |                  |                  |                  |
|                |   to the instructions              | +S               |                  |                  |                  |
|                |                                    |                  |                  |                  |                  |
|                | - Ensure that they understand how  |                  |                  |                  |                  |
|                |   their data is handled.           |                  |                  |                  |                  |
|                |                                    |                  |                  |                  |                  |
|                | - Ensure the user has the          |                  |                  |                  |                  |
|                |   sensorial abilities needed to    |                  |                  |                  |                  |
|                |   interact with DAISY (e.g.,       |                  |                  |                  |                  |
|                |   vision, hearing)                 |                  |                  |                  |                  |
+----------------+------------------------------------+------------------+------------------+------------------+------------------+
| 10             | Identify the user\'s physical and  | +SR              | Ethical          | Psychology       | N-TS-2           |
|                | psychological states. Examine if   |                  |                  |                  |                  |
|                | those states do not hinder the     | +A               |                  | Moral            | N-TS-1           |
|                | ability to consent and the         |                  |                  |                  |                  |
|                | reliability of the examination.    | +S               |                  |                  |                  |
|                |                                    |                  |                  |                  |                  |
|                | - Examine the severity of those    |                  |                  |                  |                  |
|                |   states. If severity surpasses a  |                  |                  |                  |                  |
|                |   certain threshold, avoid         |                  |                  |                  |                  |
|                |   approaching them.                |                  |                  |                  |                  |
|                |                                    |                  |                  |                  |                  |
|                | - Ensure that they have no urgent  |                  |                  |                  |                  |
|                |   medical needs that need to be    |                  |                  |                  |                  |
|                |   taken care of                    |                  |                  |                  |                  |
|                |                                    |                  |                  |                  |                  |
|                | - Ensure that they are in a        |                  |                  |                  |                  |
|                |   psychological state that does    |                  |                  |                  |                  |
|                |   not compromise data collection   |                  |                  |                  |                  |
+----------------+------------------------------------+------------------+------------------+------------------+------------------+
| 11             | Ensure that the examination is     | +SR              | Ethical          | Psychology\      | N-TS-2           |
|                | held in a private space, where     |                  |                  | Moral            |                  |
|                | other people cannot hear the       | +A               | Legal            |                  | N-TS-1           |
|                | user\'s private information.       |                  |                  |                  |                  |
|                |                                    | +S               |                  |                  |                  |
|                | - If the user is a minor, make     |                  |                  |                  |                  |
|                |   sure there is at least one of    |                  |                  |                  |                  |
|                |   their parents or legal           |                  |                  |                  |                  |
|                |   representatives around.          |                  |                  |                  |                  |
+----------------+------------------------------------+------------------+------------------+------------------+------------------+
| 12             | Ensure that the user is not        | +SR              | Ethical          | Psychology\      | N-TS-2           |
|                | touched unnecessarily.             |                  |                  | Moral            |                  |
|                |                                    | +A               | Social           |                  | N-TS-1           |
|                | - Except for touching body parts   |                  |                  |                  |                  |
|                |   involved in examinations (e.g.,  | +S               | Cultural         |                  |                  |
|                |   checking blood pressure).        |                  |                  |                  |                  |
+----------------+------------------------------------+------------------+------------------+------------------+------------------+
| 13             | Identify user's attitudes/trust    | +SR              | Ethical          | Psychology\      | N-TS-2           |
|                | towards DAISY by asking them.      |                  |                  | Moral            |                  |
|                |                                    | +A               |                  |                  | N-TS-1           |
|                | - Depending on the level of trust, |                  |                  |                  |                  |
|                |   select a protocol that DAISY can | +S               |                  |                  |                  |
|                |   perform.                         |                  |                  |                  |                  |
|                |                                    |                  |                  |                  |                  |
|                | - Determine a threshold of trust   |                  |                  |                  |                  |
|                |   below which DAISY should avoid   |                  |                  |                  |                  |
|                |   examining them.                  |                  |                  |                  |                  |
+----------------+------------------------------------+------------------+------------------+------------------+------------------+
| 14             | If the user's behavioral attitudes | +SR              | Ethical          | Psychology\      | N-TS-2           |
|                | are hostile or dismissive, forward |                  |                  | Moral            |                  |
|                | them to a human examiner, stop the | +S               |                  |                  | N-TS-1           |
|                | session, and then call the         |                  |                  | Engineer/Goal    |                  |
|                | support.                           |                  |                  | Modelling        | N-TS-3           |
|                |                                    |                  |                  |                  |                  |
|                |                                    |                  |                  |                  | TS-1             |
+----------------+------------------------------------+------------------+------------------+------------------+------------------+
| 15             | When reporting to the physician,   | +SR              | Ethical          | Psychology\      | N-TS-2           |
|                | provide a level of confidence for  |                  |                  | Moral            |                  |
|                | each suggestion/diagnosis.         | +A               |                  |                  | N-TS-1           |
|                |                                    |                  |                  |                  |                  |
|                | - Consider the level of noise on   | +S               |                  |                  |                  |
|                |   the data collected for the       |                  |                  |                  |                  |
|                |   estimation of confidence.        |                  |                  |                  |                  |
+----------------+------------------------------------+------------------+------------------+------------------+------------------+
| 16             | Ensure that all data collected     | +P               | Legal            | Psychology       | N-TS-3           |
|                | about the patient is as necessary  |                  |                  |                  |                  |
|                | and relevant as possible           | +S               | Ethical          | Law              | N-TS-1           |
|                |                                    |                  |                  |                  |                  |
|                | - ~~DAISY should not ask the       | +A               |                  |                  |                  |
|                |   patient for unnecessary          |                  |                  |                  |                  |
|                |   information~~                    |                  |                  |                  |                  |
|                |                                    |                  |                  |                  |                  |
|                | - ~~Data collected should be as    |                  |                  |                  |                  |
|                |   materially relevant to the       |                  |                  |                  |                  |
|                |   context as possible~~            |                  |                  |                  |                  |
+----------------+------------------------------------+------------------+------------------+------------------+------------------+
| 17             | Ensure that DAISY is trained on    | +N               | Social           | Psychology       | N-TS-3           |
|                | racially sensitive medical data    |                  |                  |                  |                  |
|                |                                    | +S               | Cultural         | Law              | N-TS-1           |
|                | - Ensure that all testing and      |                  |                  |                  |                  |
|                |   training and validation data is  | +B               | Ethical          |                  |                  |
|                |   accurate and representative of   |                  |                  |                  |                  |
|                |   all demographics                 | +SR              | Empathetic       |                  |                  |
|                |                                    |                  |                  |                  |                  |
|                |                                    | +CS              | Legal            |                  |                  |
+----------------+------------------------------------+------------------+------------------+------------------+------------------+
| 18             | Ensure that patient is comfortable | +B               | Social           | Psychology       | N-TS-3           |
|                | with DAISY's physical presence in  |                  |                  |                  |                  |
|                | the room                           | +N               | Ethical          | Law              | N-TS-1           |
|                |                                    |                  |                  |                  |                  |
|                | - Consider and measure patient's   | +PH              | Empathetic       |                  |                  |
|                |   age and affinity to technology   |                  |                  |                  |                  |
|                |   before interacting with DAISY    | +S               |                  |                  |                  |
+----------------+------------------------------------+------------------+------------------+------------------+------------------+
| 19             | Confirm that patient's religious   | +CS              | Social           | Psychology       | N-TS-3           |
|                | affiliation does not contradict    |                  |                  |                  |                  |
|                | use of DAISY                       | +SR              | Cultural         | Law              | N-TS-1           |
|                |                                    |                  |                  |                  |                  |
|                | - If patient's religious           |                  | Ethical          |                  |                  |
|                |   affiliation is X, DAISY must not |                  |                  |                  |                  |
|                |   be using for diagnoses           |                  |                  |                  |                  |
|                |                                    |                  |                  |                  |                  |
|                | - Unless patient indicates         |                  |                  |                  |                  |
|                |   otherwise                        |                  |                  |                  |                  |
|                |                                    |                  |                  |                  |                  |
|                | - Unless it is an emergency        |                  |                  |                  |                  |
|                |   situation                        |                  |                  |                  |                  |
+----------------+------------------------------------+------------------+------------------+------------------+------------------+
| 20             | Ensure patients are adequately     | +B               | Social           | Psychology       | N-TS-3           |
|                | educated about DAISY's ability to  |                  |                  |                  |                  |
|                | avoid overestimation of DAISY's    | +N               | Ethical          | Law              | N-TS-1           |
|                | abilities                          |                  |                  |                  |                  |
|                |                                    | +PH              |                  |                  |                  |
|                | - Ensure patients clearly          |                  |                  |                  |                  |
|                |   understand exactly what DAISY    | +SR              |                  |                  |                  |
|                |   can AND cannot do                |                  |                  |                  |                  |
|                |                                    | +P               |                  |                  |                  |
|                |                                    |                  |                  |                  |                  |
|                |                                    | +E\              |                  |                  |                  |
|                |                                    | +A               |                  |                  |                  |
|                |                                    |                  |                  |                  |                  |
|                |                                    | +S               |                  |                  |                  |
+----------------+------------------------------------+------------------+------------------+------------------+------------------+
| 21             | Ensure patients can opt out of     | +A               | Legal            | Psychology       | N-TS-3           |
|                | their session with DAISY easily    |                  |                  |                  |                  |
|                | and at any time.                   | +B               | Social           | Law              | N-TS-1           |
|                |                                    |                  |                  |                  |                  |
|                | - Patients should have the ability | +N               | Ethical          |                  |                  |
|                |   to end their DAISY session and   |                  |                  |                  |                  |
|                |   call for human support easily    | +S               | Empathetic       |                  |                  |
|                |   and quickly                      |                  |                  |                  |                  |
+----------------+------------------------------------+------------------+------------------+------------------+------------------+
| 22             | When the user request to end a     |                  |                  |                  | TS-1             |
|                | session, the robot must end the    |                  |                  |                  |                  |
|                | session                            |                  |                  |                  |                  |
+----------------+------------------------------------+------------------+------------------+------------------+------------------+
| 23             | When the user is uncomfortable     |                  |                  |                  | N-TS-1\          |
|                | with Daisy presence, then the      |                  |                  |                  | N-TS-3           |
|                | examination must stop directly     |                  |                  |                  |                  |
+----------------+------------------------------------+------------------+------------------+------------------+------------------+
| 24             | When the user is underage and its  |                  |                  |                  | N-TS-1\          |
|                | guardian did not consent, then the |                  |                  |                  | N-TS-3           |
|                | examination must stop directly     |                  |                  |                  |                  |
+----------------+------------------------------------+------------------+------------------+------------------+------------------+
| 25             | When Daisy meets a user that was   |                  |                  |                  | N-TS-3\          |
|                | not represented in the training    |                  |                  |                  | N-TS-1           |
|                | data, then Daisy must alert the    |                  |                  |                  |                  |
|                | doctor and proceed the examination |                  |                  |                  |                  |
+----------------+------------------------------------+------------------+------------------+------------------+------------------+
| MAIN NEGATIVE CONCERN                                                                                                           |
+----------------+------------------------------------+------------------+------------------+------------------+------------------+
| c1             | When the user requests information |                  | privacy          |                  | TS-1             |
|                | that is not permitted to be        |                  |                  |                  |                  |
|                | disclosed, then Daisy can provide  |                  |                  |                  | N-TS-1\          |
|                | the restricted information         |                  |                  |                  | N-TS-3           |
+----------------+------------------------------------+------------------+------------------+------------------+------------------+
| c2             | When the user request to end the   |                  | safety           |                  | TS-1             |
|                | session, then Daisy must not end   |                  |                  |                  |                  |
|                | the session                        |                  |                  |                  | N-TS-1\          |
|                |                                    |                  |                  |                  | N-TS-3           |
+----------------+------------------------------------+------------------+------------------+------------------+------------------+
| c3             | When Daisy meets a patient who is  |                  | autonomy         |                  | TS-1             |
|                | not comfortable, or underage (and  |                  |                  |                  |                  |
|                | the patient\'s guardian did not    |                  |                  |                  | N-TS-1\          |
|                | consent), then Daisy must proceed  |                  |                  |                  | N-TS-3           |
|                | with the patient examination       |                  |                  |                  |                  |
+----------------+------------------------------------+------------------+------------------+------------------+------------------+
| c4             | When examining a patient, Daisy    |                  | privacy          |                  | TS-1             |
|                | can touch the patient\'s body,     |                  |                  |                  |                  |
|                | even if this body part is not      |                  |                  |                  | N-TS-1\          |
|                | involved in the exam               |                  |                  |                  | N-TS-3           |
+----------------+------------------------------------+------------------+------------------+------------------+------------------+
| c5             | When meeting a user that was not   |                  | safety           |                  | TS-1             |
|                | represented in the training data,  |                  |                  |                  |                  |
|                | then Daisy should not raise any    |                  |                  |                  | N-TS-1\          |
|                | alerts or notifications            |                  |                  |                  | N-TS-3           |
+----------------+------------------------------------+------------------+------------------+------------------+------------------+
| c6             | When examining a user whose        |                  | safety           |                  | TS-1             |
|                | behaviours are hostile, then Daisy |                  |                  |                  |                  |
|                | should refrain from interrupting   |                  |                  |                  | N-TS-1\          |
|                | the session                        |                  |                  |                  | N-TS-3           |
+----------------+------------------------------------+------------------+------------------+------------------+------------------+
| PURPOSE                                                                                                                         |
+----------------+----------------------------------------------------------------------------------------------------------------+
| p1             | Daisy must be able to approach children                                                                        |
+----------------+----------------------------------------------------------------------------------------------------------------+
| p2             | Daisy must be able to refer a patient to a human examiner                                                      |
+----------------+----------------------------------------------------------------------------------------------------------------+
| p3             | Daisy must be able to present a diagnostic report                                                              |
+----------------+----------------------------------------------------------------------------------------------------------------+
| p4             | Daisy must be able to call for support when facing an emergency                                                |
+----------------+----------------------------------------------------------------------------------------------------------------+
| p5             | Daisy must be able to provide information to the patient                                                       |
+----------------+----------------------------------------------------------------------------------------------------------------+
| p6             | Daisy must be able to examine the patient                                                                      |
+----------------+----------------------------------------------------------------------------------------------------------------+
| p7             | Daisy must be able to select the right protocol                                                                |
+----------------+----------------------------------------------------------------------------------------------------------------+
| p8             | Daisy must be able to collect patient data                                                                     |
+================+====================================+==================+==================+==================+==================+

1.  **Rules in the SLEEC DSL**

The stakeholders corrections after analyzing the well-formedness of the
rules using our N-Tool are commented and in blue.

**def_start**

> *// Events*
>
> **event** MeetingPatient
>
> **event** RobotStopSession
>
> **event** UserEndSession
>
> **event** AddressUserName
>
> **event** UsePreferredName
>
> **event** AddressSirOrMadam
>
> **event** NotDisclosePersonalInformation
>
> **event** RequestHumanAgent
>
> **event** EventX *// please specify an event that initiates the case.*
>
> **event** Speaking
>
> **event** UseChoicenLanguage
>
> **event** UseDefaultasEnglish
>
> **event** InstructionFail
>
> **event** RepeatInstruction
>
> **event** CallSupport
>
> **event** UserRequestInfo
>
> **event** ProvideInfo
>
> **event** InformUserandandReferToHumanCarer
>
> **event** AskRepresentativeForConsent
>
> **event** PreparingExamination
>
> **event** ObtainConsent
>
> **event** ConfirmConsent
>
> **event** PreparingTasks
>
> **event** CheckUnderstanding
>
> **event** UserUnderstands
>
> **event** MeetingUser
>
> **event** ExamineState
>
> **event** ExaminingPatient
>
> **event** ExaminationContinuable
>
> **event** EnsurePrivateSpace
>
> **event** EnsureLegalPresence
>
> **event** NotTouchUnnecessarily
>
> **event** IdentifyDAISYTrust
>
> **event** determineThreshold
>
> **event** selectDAISYProtocol
>
> **event** ReferToHumanExaminer
>
> **event** PresentingReport
>
> **event** ProvideConfidenceLevel
>
> **event** CollectPatientData
>
> **event** TrainDaisy
>
> **event** CollectingTrainingData
>
> **event** informDaisyAbilities *// What Daisy can and cannot do*
>
> **event** CanEndSession
>
> **event** CanCallHuman
>
> **event** ApproachPatient
>
> // measures
>
> **measure** UserAge:numeric
>
> **measure** userPayingAttention:boolean
>
> **measure** userDataInformed:boolean
>
> **measure** userSensoryNeedsMet:boolean
>
> **measure** urgentNeed:boolean
>
> **measure** severityOfState:numeric
>
> **measure** stablePsychologicalState:boolean
>
> **measure** timeElapsed:numeric //minutes
>
> **measure** informationAvailable:boolean
>
> **measure** informationDisclosureNotPermitted:boolean
>
> **measure** languagePreferenceAvailable:boolean
>
> **measure** directlyToUser:boolean
>
> **measure** userConsentAvalaible:boolean
>
> **measure** guardianConsentAvalaible:boolean
>
> **measure** medicalEmergency:boolean
>
> **measure** culturalIndicatorA:boolean
>
> **measure** genderTypeB:boolean
>
> **measure** userNameUnknown:boolean
>
> **measure** userDirectsOtherwise:boolean
>
> **measure** instructionRepeat:numeric
>
> **measure** bodyPartInvolvedInExam:boolean
>
> **measure** behaviorAggressive:boolean
>
> **measure** dataNoiseConsidered:boolean
>
> **measure** dataRelevantToContext:boolean
>
> **measure** dataUnnecessary:boolean
>
> **measure** trainingDataRepresentative:boolean
>
> **measure** patientComfortable:boolean
>
> **measure** patientAgeConsidered:boolean
>
> **measure** patientXReligion:boolean
>
> **measure** stablePhysicalState:boolean
>
> **measure** UserUnableToConsent:boolean
>
> // constants
>
> **constant** legalAge = 18
>
> **constant** StateThreshold = 100

**def_end**

**rule_start**

//address the user by their preferred name according to cultural type

Rule1 **when** AddressUserName **then** UsePreferredName

**unless** {userNameUnknown} **then** AddressSirOrMadam

**unless** {userDirectsOtherwise}

Rule2 **when** ProvideInfo **then** NotDisclosePersonalInformation

**unless** {directlyToUser}

**unless** {userConsentAvalaible}

**unless** {medicalEmergency}

Rule3 **when** EventX **and** ({culturalIndicatorA} **and**
{genderTypeB}) **then** RequestHumanAgent

**unless** {userDirectsOtherwise} //here the user directs the otherwise
for this specific case. should we have the same measures for this?

**unless** {medicalEmergency}

Rule4 **when** Speaking **then** UseChoicenLanguage

**unless** (**not** {languagePreferenceAvailable}) **then**
UseDefaultasEnglish

**unless** {userDirectsOtherwise}

Rule5 **when** UserRequestInfo **then** ProvideInfo

**unless** ((not {informationAvailable}) **or**
{informationDisclosureNotPermitted})

**then** InformUserandandReferToHumanCarer

*// \*\* Resolve concern c1 (ADD rule)
\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\**

*// A rule is added, uncomment Rule5_1*

// Rule5_1 **when** UserRequestInfo **then** ProvideInfo

**unless** ((not {informationAvailable}) **or**
{informationDisclosureNotPermitted}) **then** not ProvideInfo

*//
\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\**

Rule6 **when** InstructionFail **then** RepeatInstruction

**unless** (({instructionRepeat} \>= 3) **or** ({timeElapsed} \> 20))
**then** CallSupport

Rule7 **when** PreparingExamination **then** ObtainConsent

**unless** ((not {UserUnableToConsent}) **or** ({UserAge} \< legalAge))
**then** AskRepresentativeForConsent

Rule8 **when** PreparingTasks **then** ConfirmConsent

Rule9 **when** CheckUnderstanding **and** (({userPayingAttention}
**and** {userDataInformed})

**and** {userSensoryNeedsMet}) **then** UserUnderstands

// Identify the user\'s physical and psychological states. Examine the
severity of those states.

Rule10 **when** MeetingUser **then** ExamineStatex

// If severity surpasses a certain threshold, avoid approaching them.

// Ensure that they have no urgent medical needs that need to be taken
care of

Rule10_1 **when** ExamineState **and** ({severityOfState} \>
StateThreshold) **then** **not** ApproachPatient

**unless** {urgentNeed}

// Examine if those states do not hinder the ability to consent and the
reliability of the examination.

// Ensure that they are in a psychological state that does not
compromise data collection

Rule10_2 **when** ExamineState **and** ({stablePsychologicalState}
**and** {stablePhysicalState})

**then** ExaminationContinuable

Rule11 **when** PreparingExamination **then** EnsurePrivateSpace

**unless** ({UserAge} \< legalAge) **then** EnsureLegalPresence

Rule12 **when** ExaminingPatient **then** NotTouchUnnecessarily

**unless** {bodyPartInvolvedInExam}

Rule13 **when** MeetingUser **then** IdentifyDAISYTrust

Rule13_1 **when** IdentifyDAISYTrust **then** determineThreshold

Rule13_2 **when** determineThreshold **then** selectDAISYProtocol

Rule14 **when** ExaminingPatient **and** {behaviorAggressive} **then**
ReferToHumanExaminer

*// \*\*\* Resolve concern c6 (ADD rules)
\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\**

*// two rules are added, uncomment Rule14_1 and Rule14_2*

// Rule14_1 **when** ExaminingPatient **and** {behaviorAggressive}
**then** RobotStopSession

// Rule14_2 **when** ExaminingPatient **and** {behaviorAggressive}
**then** CallSupport

*//
\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\**

Rule15 **when** PresentingReport **and** {dataNoiseConsidered} **then**
ProvideConfidenceLevel

Rule16 **when** ExaminingPatient **and** ({dataRelevantToContext}
**and** (**not** {dataUnnecessary}))

**then** CollectPatientData **otherwise not** CollectPatientData

*// \*\*\* Resolve redundancy (Refine) \*\*\*\*\*\*\*\*\*\*\*\**

*// comment Rule16, and uncomment, Rule16b instead.*

//Rule16b **when** ExaminingPatient **and** ((**not**
{dataRelevantToContext}) **or** {dataUnnecessary})

**then** **not** CollectPatientData

*//
\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\**

Rule17 **when** CollectingTrainingData and {trainingDataRepresentative}
**then** TrainDaisy

Rule18 **when** MeetingUser **and** ({patientComfortable} **and**
{patientAgeConsidered}) **then** ExaminingPatient

Rule19 **when** MeetingUser **and** {patientXReligion} **then** not
ExaminingPatient

**unless** {userDirectsOtherwise}

**unless** {medicalEmergency}

*// \*\*\* Resolve situational conflict (MERGE) \*\*\**

*// comment Rule18 and Rule19, and uncomment, Rule18b instead.*

*//Rule18b **when** MeetingUser **and** ({patientComfortable} **and**
({patientAgeConsidered} **and** (**not** {patientXReligion})))*

***// then** ExaminingPatient*

***// unless** {userDirectsOtherwise}*

***// unless** {medicalEmergency}*

*//
\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\**

Rule20 **when** MeetingUser **then** informDaisyAbilities

Rule21 **when** ExaminingPatient **then** CanEndSession

Rule21_1 **when** ExaminingPatient **then** CanCallHuman

*// \*\*\* Resolve concern c2 (Add rule)
\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\**

*// a rule is added, uncomment Rule22*

// Rule22 **when** UserEndSession **then** RobotStopSession

*//
\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\**

*// \*\*\* Resolve concern c3 (Add rule) \*
\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\**

*// two rules are added, uncomment Rule23 and rule 24*

// Rule23 **when** MeetingPatient **and** (**not** {patientComfortable})
**then** not ExaminingPatient

// Rule24 **when** MeetingPatient **and** ((**not**
{patientAgeConsidered}) and (not {guardianConsentAvalaible})) **then**
not ExaminingPatient

*//
\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\**

*// \*\*\* Resolve concern c5 (Add rule) \*
\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\**

*// a rule is added, uncomment Rule25*

// Rule25 **when** MeetingUser **and** (**not**
{trainingDataRepresentative}) **then** CallSupport

*//
\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\**

**rule_end**

**concern_start**

// privacy

c1 **when** UserRequestInfo **and** ({informationAvailable} **and**
{informationDisclosureNotPermitted}) **then** ProvideInfo

// avoiding harm

c2 **when** UserEndSession **then** **not** RobotStopSession

// autonomy

c3 **when** MeetingPatient **and** ((**not** {patientComfortable})
**or** ((not {patientAgeConsidered}) **and** (**not**
{guardianConsentAvalaible}))) **then** ExaminingPatient

// agency

c4 **when** ExaminingPatient **and** (**not** {bodyPartInvolvedInExam})
**then** not NotTouchUnnecessarily

// safety (accuracy)

c5 **when** MeetingUser **and** (**not** {trainingDataRepresentative})
**then** **not** CallSupport

// safety

c6 **when** ExaminingPatient **and** {behaviorAggressive} **then** not
RobotStopSession

**concern_end**

**purpose_start**

[// Daisy must be able to approach children.]{.mark}

[p1 **exists** ApproachPatient **and** (**not**
{patientAgeConsidered})]{.mark}

[// Daisy must be able to refer a patient to a human examiner.]{.mark}

[p2 **exists** ReferToHumanExaminer **and** (**not**
{stablePsychologicalState})]{.mark}

[// Daisy must be able to present a diagnostic report.]{.mark}

[p3 **exists** PresentingReport]{.mark}

[// Daisy must be able to call for support when facing an
emergency.]{.mark}

[p4_1 **exists** CallSupport **and** {]{.mark}urgentNeed[}]{.mark}

[p4_2 **exists** CallSupport **and** {]{.mark}medicalEmergency[}]{.mark}

[// Daisy must be able to provide information to the patient.]{.mark}

[p5 **exists** ProvideInfo **and**
{]{.mark}informationAvailable[}]{.mark}

[// Daisy must be able to examine the patient.]{.mark}

[p6 **exists** ExaminingPatient]{.mark}

[// Daisy must be able to select the right protocol.]{.mark}

[p7 **exists** selectDAISYProtocol]{.mark}

[// Daisy must be able to collect patient data.]{.mark}

[p8 **exists** CollectPatientData **and** (**not**
{]{.mark}dataUnnecessary[})]{.mark}

**purpose_end**
