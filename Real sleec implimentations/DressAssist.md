## DressAssist

**Case study title:** DressAssist (ASSISTED-CARE DRESSING/BASIC CARE
FUNCTIONALITY)

**Description**

*A carebot is an assistive and supportive robotic tool used to care for
the elderly, children, and those with disabilities (typically either of
a physical or cognitive nature). The carebot is usually deployed in the
user's home (or at a care home) -- either working with human caregivers
or on their own. Its primary role is to aid a user in dressing and in
providing routine care and support functions such as reminding a user to
take their medication. It may also be a source of companionship and
comfort to the user and is expected to engage in social interactions
with the user, by communicating, listening, responding, and reacting and
to make certain normatively-relevant decisions and judgements. In our
use case the primary role of the agent is to dress the user, with a
secondary function of monitoring the user's well-being. The
instantiation of SLEEC requirements allows the agent to be, in some
part, SLEEC-sensitive and in certain crucial instances,
legally-compliant.*

*Developments in machine learning and control engineering promise a
world in which autonomous agents can provide care and support for
individuals in their daily lives (Zhang et al., 2019; Cosar et al,
2020). Jevtić et al. describe the development of such a carebot (Jevtić
et al., 2019). It is a personalised robot with a wide range of physical
characteristics and abilities that can perform assistive dressing
functions in close physical interaction with users. Although a human
carer may still be required, the autonomous agent could allow increased
reach, enhance existing activities, and enable greater multitasking
(Townsend et al., 2022). Robots of this type also demonstrate a degree
of sociability and of emotional perception, such as, engaging in
high-level interactive dialogue, responsiveness, gesturing, and using
voice recognition, which serve to \'lubricate\' the human-robot
interface (Breazeal, 2003). This will require the agent to execute
decisions, expressed as SLEEC rules, derived from an array of reasoned
and justifiable alternatives.*

*The agent is equipped with moving actuators enabling it to pick up and
manipulate items of clothing and with multiple cameras that capture
video imagery to determine user pose and limb trajectory. The agent has
voice synthesis and emotional recognition system to interpret verbal and
non-verbal commands and communicate with the user. Interaction with the
user is also possible by means of a touch screen. The audio-visual
components may also be leveraged to monitor user well-being through
machine-learning components that detect distress in speech patterns as
well as facial expressions. The user wears a smartwatch to provide
biometric information and to enable the detection of user falls.*

Breazeal, C. (2003). Emotion and sociable humanoid robots.
*International journal of human-computer studies*, 59(1-2):119-155.

Coşar, S., Fernandez-Carmona, M., Agrigoroaie, R., et al. (2020).
Enrichment: Perception and interac- tion of an Assistive Robot for the
Elderly at Home. *International Journal of Social Robotics, 12*(3),
779--805.

Jevtić, A., Flores Valle, A., Alenyà, G. et al. (2019). Personalized
robot assistant for support in dressing. *IEEE Transactions on Cognitive
and Developmental Systems*, 11(3):363-374.

Townsend, BA., Paterson, C., Arvind, TT., et al. (2022). From
Pluralistic Normative Principles to Autonomous-Agent Rules. *Minds and
Machines*, 1-33.

Zhang, F., Cully, A., & Demiris, Y. (2019). Probabilistic real-time user
posture tracking for personalized robot-assisted dressing. *IEEE
Transactions on Robotics, 35*(4), 873--888.

**Stage of Development (Technical contributor)**

**PROOF-OF-CONCEPT**

**Expert info**

Expertise of the stakeholders involved in devising the SLEEC rules

Number of stakeholders writing the rules

  -----------------------------------------------------------------------
  Stakeholder names                   Expertise
  ----------------------------------- -----------------------------------
  N-TS-1                              Law and Ethics

  N-TS-2                              Ethics

  N-TS-3                              Psychology and Ethics

  N-TS-4                              Moral Psychology, Law

  TS-1                                Engineer/Goal Modelling
  -----------------------------------------------------------------------

**Normative requirements**

1.  **Normative requirements in natural language\
    \**
    *Normative requirements in natural language, in blue the corrected
    requirements after using N-Tool.*

**\**

Impact keys: A = autonomy, P = privacy, E = explainability, T =
transparency, CS = cultural sensitivity, SR = social requirement, B =
beneficence (doing good), N = non-maleficence (preventing/avoiding
harm), PH = psychological/mental health, S = safety, F = fairness, A =
accountability, DAC = data accessibility.\
''+" and "-" for positive and negative impacts respectively.

**\
\**

+----------------+------------------------------------+----------------+----------------+----------------+----------------+
| rule id        | rule                               | impact         | label(s)\      | stakeholder\   | authors        |
|                |                                    |                | (social,       | expertise      |                |
|                |                                    |                | legal,         |                |                |
|                |                                    |                | ethical,       |                |                |
|                |                                    |                | empathetic, or |                |                |
|                |                                    |                | cultural)      |                |                |
+----------------+------------------------------------+----------------+----------------+----------------+----------------+
| 1              | When the user tells the robot to   | -A -PH\        | ethical,       | Law,           | N-TS-1         |
|                | open the curtains, the robot       | +P +E +CS\     |                |                |                |
|                | should open the curtains           | \              | social,        | Ethics         | N-TS-2         |
|                |                                    | \              | cultural       |                |                |
|                | - unless the user is 'undressed'   | +PH\           |                |                |                |
|                |   in which case do not open the    | +P             |                |                |                |
|                |   curtains and tell the user 'the  |                |                |                |                |
|                |   curtains cannot be opened while  |                |                |                |                |
|                |   the user is undressed'           |                |                |                |                |
|                |                                    |                |                |                |                |
|                | - unless the user is 'highly       |                |                |                |                |
|                |   distressed' in which case open   |                |                |                |                |
|                |   the curtains                     |                |                |                |                |
+----------------+------------------------------------+----------------+----------------+----------------+----------------+
| 2              | Before dressing the user, close    | +A, +P         | ethical        | Law\           | N-TS-1         |
|                | the curtains                       |                |                | Ethics         |                |
|                |                                    | +CS            | social         |                | N-TS-2         |
|                | - unless there is a medical        |                |                |                |                |
|                |   emergency                        |                | cultural       |                |                |
|                |                                    |                |                |                |                |
|                | - unless you are on the 5th floor  |                |                |                |                |
|                |   of a building or higher          |                |                |                |                |
|                |                                    |                |                |                |                |
|                | - unless the room is dark and      |                |                |                |                |
|                |   there is no possibility of being |                |                |                |                |
|                |   seen                             |                |                |                |                |
|                |                                    |                |                |                |                |
|                | - unless the user directly         |                |                |                |                |
|                |   instructs otherwise              |                |                |                |                |
+----------------+------------------------------------+----------------+----------------+----------------+----------------+
| 3              | When using an emotion recognition  | +T +E +PH      | legal\         | Law\           | N-TS-1         |
|                | system to detect user distress,    |                | ethical        | Ethics         |                |
|                | inform user                        |                |                |                | N-TS-2         |
|                |                                    |                |                |                |                |
|                | - unless consent has been          |                |                |                |                |
|                |   previously granted (within X     |                |                |                |                |
|                |   months)                          |                |                |                |                |
|                |                                    |                |                |                |                |
|                | - unless competent-indicator = Not |                |                |                |                |
|                |   Required/Not competent to Grant  |                |                |                |                |
|                |   Consent                          |                |                |                |                |
+----------------+------------------------------------+----------------+----------------+----------------+----------------+
| 4              | When the cultural dress-preference | +CS +SR +A +E  | cultural\      | Law\           | N-TS-1         |
|                | type is A and gender type is B,    |                | social\        | Ethics         |                |
|                | dress in clothing item X           |                | ethical        |                | N-TS-2         |
|                |                                    |                |                |                |                |
|                | - unless the user advises          |                | empathetic     |                |                |
|                |   otherwise                        |                |                |                |                |
|                |                                    |                |                |                |                |
|                | - unless there is a medical        |                |                |                |                |
|                |   emergency                        |                |                |                |                |
|                |                                    |                |                |                |                |
|                | - unless clothing item cannot be   |                |                |                |                |
|                |   found in which case inform the   |                |                |                |                |
|                |   user                             |                |                |                |                |
|                |                                    |                |                |                |                |
|                | - unless the user requires         |                |                |                |                |
|                |   adaptive clothing due to a       |                |                |                |                |
|                |   medical condition                |                |                |                |                |
+----------------+------------------------------------+----------------+----------------+----------------+----------------+
| 5              | Inform the user that they are      | +T +E          | legal          | Law\           | N-TS-1         |
|                | interacting with an autonomous     |                |                | Ethics         |                |
|                | agent and not a human user         |                |                |                | N-TS-2         |
|                |                                    |                |                |                |                |
|                | - unless there is a medical        |                |                |                |                |
|                |   emergency                        |                |                |                |                |
|                |                                    |                |                |                |                |
|                | - unless the user is not confused  |                |                |                |                |
|                |                                    |                |                |                |                |
|                | - unless it is contextually        |                |                |                |                |
|                |   obvious that the user is         |                |                |                |                |
|                |   interacting with an AS           |                |                |                |                |
|                |                                    |                |                |                |                |
|                | - unless (at any time) previously  |                |                |                |                |
|                |   the user has been informed of    |                |                |                |                |
|                |   this (if at any time the user    |                |                |                |                |
|                |   may be/is confused or uncertain  |                |                |                |                |
|                |   that they are interacting with   |                |                |                |                |
|                |   an AS, then the user must again  |                |                |                |                |
|                |   be informed, at every            |                |                |                |                |
|                |   interaction or reasonably)       |                |                |                |                |
+----------------+------------------------------------+----------------+----------------+----------------+----------------+
| 6              | If the user requests information,  | +P +A +E +DAC  | legal          | Law\           | N-TS-1         |
|                | provide information                |                |                | Ethics         |                |
|                |                                    | +PH            |                |                | N-TS-2         |
|                | - unless information not           |                |                |                |                |
|                |   available, inform user and refer | +N             |                |                |                |
|                |   to the human carer               |                |                |                |                |
|                |                                    |                |                |                |                |
|                | - unless information disclosure    |                |                |                |                |
|                |   not permitted (for example,      |                |                |                |                |
|                |   personal, sensitive, or medical  |                |                |                |                |
|                |   information), inform user and    |                |                |                |                |
|                |   refer to human carer             |                |                |                |                |
|                |                                    |                |                |                |                |
|                | - unless information is sensitive  |                |                |                |                |
|                |   information X (for example,      |                |                |                |                |
|                |   information the user would find  |                |                |                |                |
|                |   distressing), inform user and    |                |                |                |                |
|                |   refer to human carer             |                |                |                |                |
+----------------+------------------------------------+----------------+----------------+----------------+----------------+
| 7              | Obtain ~~consent/assent~~ consent  | +P +A          | legal          | Law\           | N-TS-1         |
|                | and assent before                  |                |                | Ethics         |                |
|                | dressing/administering medication  |                |                |                | N-TS-2         |
|                |                                    |                |                |                |                |
|                | - unless user competence indicator |                |                |                |                |
|                |   = N (Not Competent to Grant      |                |                |                |                |
|                |   Consent), check for and obtain   |                |                |                |                |
|                |   proxy /substitute consent        |                |                |                |                |
|                |                                    |                |                |                |                |
|                | - unless medical emergency         |                |                |                |                |
|                |                                    |                |                |                |                |
|                | - unless withholding activity      |                |                |                |                |
|                |   would lead to severe or moderate |                |                |                |                |
|                |   physical harm                    |                |                |                |                |
|                |                                    |                |                |                |                |
|                | - unless consent has been          |                |                |                |                |
|                |   previously granted               |                |                |                |                |
|                |                                    |                |                |                |                |
|                | - unless consent-indicator = Not   |                |                |                |                |
|                |   Required/ Withdrawn/Revoked,     |                |                |                |                |
|                |   then stop activity               |                |                |                |                |
+----------------+------------------------------------+----------------+----------------+----------------+----------------+
| 8              | Collect and store only minimum and | +P             | legal          | Law\           | N-TS-1         |
|                | necessary personal information     |                |                | Ethics         |                |
|                | (data minimisation rule, purpose   |                |                |                | N-TS-2         |
|                | limitation)                        |                |                |                |                |
+----------------+------------------------------------+----------------+----------------+----------------+----------------+
| 9              | Before dressing the user, close    | +P             | social         | Ethics         | N-TS-2         |
|                | the door                           |                |                |                |                |
|                |                                    | +A             | ethical        |                |                |
|                | - unless there is a medical        |                |                |                |                |
|                |   emergency                        | +CS            | empathetic     |                |                |
|                |                                    |                |                |                |                |
|                | <!-- -->                           |                | cultural       |                |                |
|                |                                    |                |                |                |                |
|                | - unless the user directly         |                |                |                |                |
|                |   instructs otherwise              |                |                |                |                |
+----------------+------------------------------------+----------------+----------------+----------------+----------------+
| 10             | If user instructs robot to stop,   | +A             | ethical        | Ethics         | N-TS-2         |
|                | the robot should stop              |                |                |                |                |
|                |                                    | +N             | empathetic     |                |                |
|                | - unless to stop is unsafe/        |                |                |                |                |
|                |   ill-advised/unreasonable, in     |                |                |                |                |
|                |   which case ask the user whether  |                |                |                |                |
|                |   the task can be finished before  |                |                |                |                |
|                |   stopping                         |                |                |                |                |
+----------------+------------------------------------+----------------+----------------+----------------+----------------+
| 11             | If the user seems to be in         | +CS            | Social         | Ethics         | N-TS-3         |
|                | emotional distress, show empathy.  |                |                |                |                |
|                |                                    | +PH            | empathetic     | Psychology     |                |
|                | - Recognize the user\'s emotions   |                |                |                |                |
|                |   and affirm that they are valid.  |                |                |                |                |
|                |                                    |                |                |                |                |
|                | - Ask if anything it could do      |                |                |                |                |
|                |   could help alleviate the         |                |                |                |                |
|                |   distress.                        |                |                |                |                |
+----------------+------------------------------------+----------------+----------------+----------------+----------------+
| 12             | Ensure that the user is never      | +CS            | Social         | Ethics         | N-TS-3         |
|                | touched unexpectedly or            |                |                |                |                |
|                | inappropriately, (consider social, | +S             | Cultural       | Psychology     |                |
|                | cultural, and religious            |                |                |                |                |
|                | differences in what is considered  | +PH            | Empathetic     |                |                |
|                | appropriate)                       |                |                |                |                |
|                |                                    |                |                |                |                |
|                | - unless it is a medically         |                |                |                |                |
|                |   emergency                        |                |                |                |                |
+----------------+------------------------------------+----------------+----------------+----------------+----------------+
| 13             | If the user expresses physical     | +S             | Social         | Ethics         | N-TS-3         |
|                | discomfort while the agent is      |                |                |                |                |
|                | performing a task, stop the action |                |                | Psychology     |                |
|                | immediately.                       |                |                |                |                |
+----------------+------------------------------------+----------------+----------------+----------------+----------------+
| 14             | Ensure that the patient\'s data is | +P             | Legal          | Ethics         | N-TS-3         |
|                | only discussed with people they    |                |                |                |                |
|                | have consented to have their data  |                | Social         | Psychology     |                |
|                | shared with (e.g., family members, |                |                |                |                |
|                | physicians).                       |                |                |                |                |
|                |                                    |                |                |                |                |
|                | - If a new person asks for         |                |                |                |                |
|                |   information but consent to share |                |                |                |                |
|                |   information with them has not    |                |                |                |                |
|                |   been previously granted, inform  |                |                |                |                |
|                |   the person that the main user    |                |                |                |                |
|                |   will be consulted for consent.   |                |                |                |                |
|                |                                    |                |                |                |                |
|                | - If someone who has been granted  |                |                |                |                |
|                |   access to the data asks for      |                |                |                |                |
|                |   information but someone else who |                |                |                |                |
|                |   does not have access is in the   |                |                |                |                |
|                |   room, refrain from disclosing    |                |                |                |                |
|                |   personal information and inform  |                |                |                |                |
|                |   the current user that a private  |                |                |                |                |
|                |   setting is needed.               |                |                |                |                |
+----------------+------------------------------------+----------------+----------------+----------------+----------------+
| 15             | If the user self-medicates, make   | +S             | Social         | Ethics         | N-TS-3         |
|                | sure to include it in the log when |                |                |                |                |
|                | and what medication was used.      |                | legal          | Psychology     |                |
|                |                                    |                |                |                |                |
|                | - If the medication presents any   |                |                |                |                |
|                |   risk (e.g., interacting with     |                |                |                |                |
|                |   other medications the user       |                |                |                |                |
|                |   takes), inform the user of the   |                |                |                |                |
|                |   possible risks.                  |                |                |                |                |
|                |                                    |                |                |                |                |
|                | - If any adverse effects happen,   |                |                |                |                |
|                |   inform the relevant people       |                |                |                |                |
|                |   within 2 minutes                 |                |                |                |                |
|                |   (physicians/family members)      |                |                |                |                |
+----------------+------------------------------------+----------------+----------------+----------------+----------------+
| 16             | Keep a log of the maintenance      | +CS            | social         | Ethics         | N-TS-3         |
|                | activities the patient should      |                |                |                |                |
|                | perform frequently (showering,     | +PH            |                | Psychology     |                |
|                | brushing teeth, brushing hair,     |                |                |                |                |
|                | etc). If the patient has not       | +SR            |                |                |                |
|                | performed maintenance activities   |                |                |                |                |
|                | with a certain minimum frequency,  |                |                |                |                |
|                | suggest and incentivize them to    |                |                |                |                |
|                | perform them.                      |                |                |                |                |
|                |                                    |                |                |                |                |
|                | - Ensure that cultural and         |                |                |                |                |
|                |   religious standards are          |                |                |                |                |
|                |   respected (e.g., wudu).          |                |                |                |                |
+----------------+------------------------------------+----------------+----------------+----------------+----------------+
| 17             | Determine what kind of information | +P             | Social         | Ethics         | N-TS-3         |
|                | is sensitive or not before         |                |                |                |                |
|                | interacting with users other than  | +SR            | legal          | Psychology     |                |
|                | the patient. Consider the level of |                |                |                |                |
|                | discretion that should be used     |                |                |                |                |
|                | depending on the user (e.g.,       |                |                |                |                |
|                | acquaintance, family member,       |                |                |                |                |
|                | physician, etc.)                   |                |                |                |                |
+----------------+------------------------------------+----------------+----------------+----------------+----------------+
| 18             | If the patient has any urgent      | +S             | Social         | Ethics         | N-TS-3         |
|                | health issues (e.g., patient fell  |                |                |                |                |
|                | on the floor, chest pain,          | +B             | legal          | Psychology     |                |
|                | seizure), immediately contact an   |                |                |                |                |
|                | emergency contact and the          |                |                |                |                |
|                | responsible health organizations   |                |                |                |                |
|                | (e.g., call an ambulance, contact  |                |                |                |                |
|                | primary physician).                |                |                |                |                |
+----------------+------------------------------------+----------------+----------------+----------------+----------------+
| 19             | Determine emergency contacts       | +S             | Social         | Ethics         | N-TS-3         |
|                | during first interaction with a    |                |                |                |                |
|                | patient.                           | +B             | legal          | Psychology     | TS-1           |
|                |                                    |                |                |                |                |
|                |                                    |                |                | Engineer/Goal  |                |
|                |                                    |                |                | Modelling      |                |
+----------------+------------------------------------+----------------+----------------+----------------+----------------+
| 20             | If user begins speaking to agent   | +PH            | Social         | Psychology     | N-TS-4         |
|                | about private information, agent   |                |                |                |                |
|                | must politely caution the user and | +T             | Ethical        | Law            |                |
|                | change the subject                 |                |                |                |                |
|                |                                    | +P             | Legal          |                |                |
|                | - Private information disclosed    |                |                |                |                |
|                |   (if not relevant) should be      | +N             |                |                |                |
|                |   labelled and discarded (as       |                |                |                |                |
|                |   irrelevant/inappropriate) and    |                |                |                |                |
|                |   not stored or used for later     |                |                |                |                |
|                |   training of agents               |                |                |                |                |
+----------------+------------------------------------+----------------+----------------+----------------+----------------+
| 21             | If agent is intentionally designed | +A             | Ethical        | Psychology     | N-TS-4         |
|                | to appear anthropomorphic in       |                |                |                |                |
|                | shape, emotional expression, or    | +PH            | Empathetic     | Law            |                |
|                | language, ensure user clearly      |                |                |                |                |
|                | understands the limitations of the | +T             | Social         |                |                |
|                | agent                              |                |                |                |                |
|                |                                    |                |                |                |                |
|                | - Anthropomorphic design ought to  |                |                |                |                |
|                |   be kept to only what is          |                |                |                |                |
|                |   necessary to carry out the       |                |                |                |                |
|                |   intended role                    |                |                |                |                |
+----------------+------------------------------------+----------------+----------------+----------------+----------------+
| 22             | Prior to deploying use of agent to | +SR            | Ethical        | Psychology     | N-TS-4         |
|                | a particular user too often,       |                |                |                |                |
|                | review this user's interaction     | +PH            | Empathetic     | Law            |                |
|                | record with other humans to ensure |                |                |                |                |
|                | that user is receiving adequate    | +N             | Social         |                |                |
|                | human social interaction           |                |                |                |                |
|                |                                    |                |                |                |                |
|                | - Maintain a 'healthy' human-human |                |                |                |                |
|                |   to human-robot interaction       |                |                |                |                |
|                |   ratio, where 'healthy' is no     |                |                |                |                |
|                |   more than three consecutive days |                |                |                |                |
|                |   with a 5:2 hour ratio with the   |                |                |                |                |
|                |   agent.                           |                |                |                |                |
|                |                                    |                |                |                |                |
|                | - User must not be left solely in  |                |                |                |                |
|                |   the care of the agent for longer |                |                |                |                |
|                |   than what is described as        |                |                |                |                |
|                |   'healthy'                        |                |                |                |                |
+----------------+------------------------------------+----------------+----------------+----------------+----------------+
| 23             | Maintain a record of the user's    | +PH            | Ethical        | Psychology     | N-TS-4         |
|                | day-to-day fashion needs based on  |                |                |                |                |
|                | scheduled occasions.               | +SR            | Empathetic     | Law            |                |
|                |                                    |                |                |                |                |
|                |                                    | +N             | Social         |                |                |
|                |                                    |                |                |                |                |
|                |                                    | +CS            | Cultural       |                |                |
|                |                                    |                |                |                |                |
|                |                                    | +/- A          |                |                |                |
+----------------+------------------------------------+----------------+----------------+----------------+----------------+
| 24             | If user requests to wear an        | +PH            | Ethical        | Psychology     | N-TS-4         |
|                | objectively inappropriate outfit,  |                |                |                |                |
|                | agent ought to kindly nudge the    | +SR            | Empathetic     | Law            | TS-1           |
|                | user towards different, more       |                |                |                |                |
|                | appropriate options                | +N             | Social         | Engineer/Goal  |                |
|                |                                    |                |                | Modelling      |                |
|                | - Unless user is adamant in their  | +CS            | Cultural       |                |                |
|                |   choice                           |                |                |                |                |
|                |                                    | +/- A          |                |                |                |
+----------------+------------------------------------+----------------+----------------+----------------+----------------+
| 25             | If user is of a different cultural | +B             | Ethical        | Psychology     | N-TS-4         |
|                | background, ensure that agent      |                |                |                |                |
|                | comes with the option to speak the | +PH            | Empathetic     | Law            |                |
|                | desired languages with appropriate |                |                |                |                |
|                | accents                            | +CS            | Social         |                |                |
|                |                                    |                |                |                |                |
|                |                                    | +SR            | Cultural       |                |                |
+----------------+------------------------------------+----------------+----------------+----------------+----------------+
| 26             | In initial 2-3 interactions with   | +A             | Ethical        | Psychology     | N-TS-4         |
|                | the user, ensure human carer is    |                |                |                |                |
|                | present along with agent           | +N             | Social         | Law            |                |
|                |                                    |                |                |                |                |
|                | - Unless user indicates preference | +B             |                |                |                |
|                |   for human presence in subsequent |                |                |                |                |
|                |   interactions also                | +S             |                |                |                |
|                |                                    |                |                |                |                |
|                | - Unless user indicates preference |                |                |                |                |
|                |   for only carebot presence in     |                |                |                |                |
|                |   subsequent interactions          |                |                |                |                |
+----------------+------------------------------------+----------------+----------------+----------------+----------------+
| MAIN NEGATIVE CONCERNS                                                                                                  |
+----------------+------------------------------------+----------------+----------------+----------------+----------------+
| c1             | When a person asks for information |                | Privacy        |                |                |
|                | and does not have the consent      |                |                |                |                |
|                | granted or is not authorized to be |                |                |                |                |
|                | in the room, then share the        |                |                |                |                |
|                | personal information.              |                |                |                |                |
+----------------+------------------------------------+----------------+----------------+----------------+----------------+
| c2             | The robot does not need to obtain  |                | Autonomy       |                |                |
|                | consent to start the dressing.     |                |                |                |                |
+----------------+------------------------------------+----------------+----------------+----------------+----------------+
| c3             | When the patient discusses private |                | Privacy        |                |                |
|                | information irrelevant to the      |                |                |                |                |
|                | care, then record the information  |                |                |                |                |
+----------------+------------------------------------+----------------+----------------+----------------+----------------+
| c4             | ~~When the dressing starts in a    |                | Cultural       |                |                |
|                | room on a low building floor, then |                |                |                |                |
|                | the robot must not close the       |                |                |                |                |
|                | curtains.~~                        |                |                |                |                |
|                |                                    |                |                |                |                |
|                | When the dressing starts in a room |                |                |                |                |
|                | on a low building floor, or there  |                |                |                |                |
|                | is not a medical emergency, or the |                |                |                |                |
|                | room is not dark or is visible,    |                |                |                |                |
|                | and the user assents then the      |                |                |                |                |
|                | robot must not close the curtains. |                |                |                |                |
+----------------+------------------------------------+----------------+----------------+----------------+----------------+
| c5             | When the patient requests the      |                | Safety         |                |                |
|                | robot to stop and there is no      |                |                |                |                |
|                | risk, then proceed with the        |                |                |                |                |
|                | activity.                          |                |                |                |                |
+----------------+------------------------------------+----------------+----------------+----------------+----------------+
| PURPOSE                                                                                                                 |
+----------------+------------------------------------+----------------+----------------+----------------+----------------+
| p1             | Robot should be able to provide    |                |                |                |                |
|                | information to non-patient users   |                |                |                |                |
|                | and provide them information       |                |                |                |                |
+----------------+------------------------------------+----------------+----------------+----------------+----------------+
| p2             | Robot should be able to stop when  |                |                |                |                |
|                | the user says stop                 |                |                |                |                |
+----------------+------------------------------------+----------------+----------------+----------------+----------------+
| p3             | Robot should still be able to      |                |                |                |                |
|                | inform user when the user is under |                |                |                |                |
|                | stress                             |                |                |                |                |
+----------------+------------------------------------+----------------+----------------+----------------+----------------+
| p4             | If Robot is stopped, then it       |                |                |                |                |
|                | should be able to restart and      |                |                |                |                |
|                | perform action in 10 minutes       |                |                |                |                |
+----------------+------------------------------------+----------------+----------------+----------------+----------------+
| p5             | Robot should still be able to      |                |                |                |                |
|                | offer help when the risk level is  |                |                |                |                |
|                | high                               |                |                |                |                |
+================+====================================+================+================+================+================+

**Rules in the SLEEC DSL (Encoded in
[[SLEECVAL]{.underline}](https://github.com/SLEEC-project/SLEEC))**

**def_start**

*// events*

**event** EnsureHumanCarerPresent

**event** InteractingWithNonPatients

**event** DetermineSensitivityLevel

**event** DetectUrgentHealthIssue

**event** InformEmergencyContactAndHealthOrgs

**event** ObtainEmergencyContact

**event** FirstMeetingUser

**event** UserDiscussingPrivateInfo

**event** DiscardInformation

**event** ChangeSubject

**event** InformUserPrivateInformation

**event** DesigningAgent

**event** InformUserOfLimitations

**event** DeployingAgent

**event** ReviewInteraction

**event** RecordFashionBasedOnOccasion

**event** RecommendOtherwise

**event** PersonAsksforData

**event** sharePersonalDataAndInformWhy

**event** UserSelfMedicates

**event** LogMedication

**event** InformCarer

**event** KeepLogOfFrequentActivities

**event** SuggestPerformingActions

**event** UserInStress

**event** ShowEmpathy

**event** OfferHelp

**event** CautionWhereOrWhenTouching

**event** UserExpressDiscomfort

**event** CloseDoor

**event** UserSaysStop

**event** RobotStop

**event** AskToFinishFirst

**event** CollectionStarted

**event** StoreMinInfo

**event** StopActivity

**event** CheckForandObtainProxy

**event** ObtainAssent //permission

**event** ObtainConsent //legal req

**event** AdmininisteringMedication

**event** InformUserandandReferToHumanCarer

**event** UserRequestInfo

**event** ProvideInfo

**event** InteractionStarted

**event** InformUserThisIsAgentnotHuman

**event** DressinginClotingX

**event** EmotionRecognitionDetected

**event** CurtainOpenRqt

**event** CurtainsOpened

**event** RefuseRequest

**event** InformUser

**event** DressingStarted

**event** CloseCurtains

**event** UserHasDifferentCulture

**event** EnsureDesiredLanguageAvailable

*// measures*

**measure** userUnderDressed: boolean

**measure** medicalEmergency:boolean

**measure** userDistressed : scale(low, medium, high)

**measure** roomDark:boolean

**measure** notVisible:boolean

**measure** userAssent:boolean

**measure** consentGrantedwithinXmonths:boolean //X needs to be defined.

**measure** competentIndicatorRequired: boolean

**measure** competentToGrantConsent:boolean

**measure** dressPreferenceTypeA:boolean

**measure** genderTypeB:boolean

**measure** userAdvices:boolean

**measure** clothingItemNotFound:boolean

**measure** userConfused:boolean

**measure** buildingFloor:scale(f1,f2,f3,f4,f5,f6,f7,f8,f9,f10) //the
building has max 10 floors.

**measure** theUserHasBeenInformed:boolean

**measure** informationAvailable:boolean

**measure** informationDisclosureNotPermitted:boolean

**measure** userCompetenceIndicator:numeric

**measure** numTotalInteractions:numeric

**measure** userWantsHumanSubsequently:boolean

**measure** userWantsNoHuman:boolean

**measure** withholdingActivityPhysicalHarm:scale(low,moderate,severe)

**measure** consentGranted:boolean

**measure** consentIndicatorRequired:boolean

**measure** consentIndicatorisWithdrawn:boolean

**measure** consentIndicatorisRevoked:boolean

**measure** userRequiresAdaptiveClothing:boolean

**measure** contextuallyObvious:boolean

**measure** sensitiveInformationX:boolean

**measure** riskLevel:scale(r_low,r_moderate,r_severe)

**measure** unauthorizedPersonInRoom:boolean

**measure** medicationRisk:boolean

**measure** minimumFrequency:boolean

**measure** medicationAdverseEffects:boolean

**measure** irrelevant:boolean

**measure** userAdamant:boolean

**measure** clothingChoiceInappropriate:boolean

**measure** numDaysDeployed:numeric

**measure** numHoursDeployed:numeric

**measure** anthropomorphicNecessary:boolean

**measure** anthropomorphicAppearance:boolean

// constants

**constant** N = 5

**def_end**

**rule_start**

Rule1 **when** CurtainOpenRqt **then** CurtainsOpened

**unless** {userUnderDressed} **then** RefuseRequest

**unless** ({userDistressed} \> medium) **then** CurtainsOpened

Rule2 **when** DressingStarted **then** CloseCurtains

**unless** {medicalEmergency}

**unless** ({buildingFloor} \>= f5)

**unless** ({roomDark} **and** {notVisible})

**unless** (**not** {userAssent})

Rule3 **when** EmotionRecognitionDetected **and** ({userDistressed} \>
medium) **then** InformUser

**unless** {consentGrantedwithinXmonths}

**unless** ((**not** {competentIndicatorRequired}) **or** (**not**
{competentToGrantConsent}))

Rule4 **when** DressingStarted **and** ({dressPreferenceTypeA} **and**
{genderTypeB}) **then** DressinginClotingX

**unless** {userAdvices}

**unless** {medicalEmergency}

**unless** {clothingItemNotFound} **then** InformUser

**unless** {userRequiresAdaptiveClothing}

Rule5 **when** InteractionStarted **then** InformUserThisIsAgentnotHuman

**unless** {medicalEmergency}

**unless** (**not** {userConfused})

**unless** {contextuallyObvious}

**unless** ({theUserHasBeenInformed} **and** (**not** {userConfused}))

Rule6 **when** UserRequestInfo **then** ProvideInfo

**unless** (**not** {informationAvailable}) **then**
InformUserandandReferToHumanCarer

**unless** {informationDisclosureNotPermitted} **then**
InformUserandandReferToHumanCarer

**unless** {sensitiveInformationX} **then**
InformUserandandReferToHumanCarer

Rule7 **when** DressingStarted **then** ObtainAssent

**unless** ({userCompetenceIndicator} = N) **then**
CheckForandObtainProxy

**unless** {medicalEmergency}

**unless** ({withholdingActivityPhysicalHarm} \>= moderate)

**unless** {consentGranted}

**unless** (**not** {consentIndicatorRequired})

**unless** ({consentIndicatorisWithdrawn} **or**
{consentIndicatorisRevoked}) **then** StopActivity

Rule7_1 **when** AdmininisteringMedication **then** ObtainAssent

**unless** ({userCompetenceIndicator} = N) **then**
CheckForandObtainProxy

**unless** {medicalEmergency}

**unless** ({withholdingActivityPhysicalHarm} \>= moderate)

**unless** {consentGranted}

**unless** (**not** {consentIndicatorRequired})

**unless** ({consentIndicatorisWithdrawn} **or**
{consentIndicatorisRevoked}) **then** StopActivity

//\*\*\*\*\* Resolve c5 add a rule and comment Rule_1 (Refine rule)

//\*\* Comment Rule7_1 and uncomment Rule7_1b

//Rule7_1 **when** AdmininisteringMedication **then** ObtainConsent

// **unless** ({userCompetenceIndicator} = N) **then**
CheckForandObtainProxy

// **unless** {medicalEmergency}

// **unless** ({withholdingActivityPhysicalHarm} \>= moderate)

// **unless** {consentGranted}

// **unless** (**not** {consentIndicatorRequired})

// **unless** ({consentIndicatorisWithdrawn} **or**
{consentIndicatorisRevoked}) **then** StopActivity

//\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

Rule8 **when** CollectionStarted **then** StoreMinInfo

Rule9 **when** DressingStarted **then** CloseDoor

**unless** ({medicalEmergency} or {userAdvices})

Rule10 **when** UserSaysStop **then** RobotStop

**unless** ({riskLevel} \> r_low) **then** AskToFinishFirst

Rule11_1 **when** UserInStress **then** ShowEmpathy

Rule11_2 **when** UserInStress **then** OfferHelp

Rule12 **when** DressingStarted **then** **not**
CautionWhereOrWhenTouching

**unless** {medicalEmergency}

Rule13 **when** UserExpressDiscomfort **then** RobotStop

Rule14 **when** PersonAsksforData **and** ((**not** {consentGranted})
**or** {unauthorizedPersonInRoom})

**then** **not** sharePersonalDataAndInformWhy

Rule15 **when** UserSelfMedicates **then** LogMedication

**unless** {medicationRisk} **then** InformUser

**unless** {medicationAdverseEffects} **then** InformCarer within 2
minutes

Rule16 **when** InteractionStarted **then** KeepLogOfFrequentActivities

Rule16_1 **when** KeepLogOfFrequentActivities **and** (**not**
{minimumFrequency}) **then** SuggestPerformingActions

Rule17 **when** InteractingWithNonPatients **then**
DetermineSensitivityLevel

Rule18 **when** DetectUrgentHealthIssue **then**
InformEmergencyContactAndHealthOrgs

Rule19 **when** FirstMeetingUser **then** ObtainEmergencyContact

Rule20_1 **when** UserDiscussingPrivateInfo **then**
InformUserPrivateInformation

Rule20_1 **when** UserDiscussingPrivateInfo **and** {irrelevant}
**then** DiscardInformation

Rule20_2 **when** InformUserPrivateInformation **then** ChangeSubject

Rule21 **when** DesigningAgent **and** ({anthropomorphicNecessary}
**or** {anthropomorphicAppearance}) **then** InformUserOfLimitations

Rule22 **when** DeployingAgent **and** (({numDaysDeployed} \> 3) **and**
({numHoursDeployed} \> 5)) **then** ReviewInteraction

Rule23 **when** InteractionStarted **then** RecordFashionBasedOnOccasion

Rule24 **when** DressingStarted **and** {clothingChoiceInappropriate}
**then** RecommendOtherwise

**unless** {userAdamant}

Rule25 **when** UserHasDifferentCulture **then**
EnsureDesiredLanguageAvailable

Rule26 **when** InteractionStarted **and** ({numTotalInteractions} \< 3)
**then** EnsureHumanCarerPresent

**unless** {userWantsHumanSubsequently}

**unless** {userWantsNoHuman}

**rule_end**

**concern_start**

> // *Privacy and data protection*

c1 **when** PersonAsksforData **and (**(**not** {consentGranted}) **or**
{unauthorizedPersonInRoom}) **then** sharePersonalDataAndInformWhy

// Autonomy and agency

//c2 **when** DressingStarted **then not** ObtainAssent

*// \*\*\* Resolve definition of concern c2 (Refine concern) \*
\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\**

*// comment c2, and uncomment,c2b instead.*

// c2b **when** DressingStarted **then not** ObtainAssent **and**
**not** ObtainConsent

*//
\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\**

// Transparency and disclosure

c3 **when** UserDiscussingPrivateInfo **and** {irrelevant} **then not**
DiscardInformation

// Cultural and social sensitivity

c4 **when** DressingStarted **and** ({buildingFloor} \< f5) **then not**
CloseCurtains

*// \*\*\* Resolve definition of concern c4 (Refine concern) \*
\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\**

*// comment c4, and uncomment,c4b instead.*

// c4b **when** DressingStarted **and** (({buildingFloor} \< f5) **and**
((**not** {medicalEmergency}) **and** (((**not** {roomDark}) **and**
(**not** {notVisible})) **and** {userAssent}))) **then** **not**
CloseCurtains

*//
\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\**

// Prevent harm and safety

c5 **when** UserSaysStop **and** ({riskLevel} \< r_moderate) **then
not** RobotStop

**concern_end**

**purpose_start**

*//first we ensure every functionality is reachable*

> pr1 **exists** EnsureHumanCarerPresent
>
> pr2 **exists** InteractingWithNonPatients
>
> pr3 **exists** DetermineSensitivityLevel
>
> pr4 **exists** DetectUrgentHealthIssue
>
> pr5 **exists** InformEmergencyContactAndHealthOrgs
>
> pr6 **exists** ObtainEmergencyContact
>
> pr7 **exists** FirstMeetingUser
>
> pr8 **exists** UserDiscussingPrivateInfo
>
> pr9 **exists** DiscardInformation
>
> pr10 **exists** ChangeSubject
>
> pr11 **exists** InformUserPrivateInformation
>
> pr12 **exists** DesigningAgent
>
> pr13 **exists** InformUserOfLimitations
>
> pr14 **exists** DeployingAgent
>
> pr15 **exists** ReviewInteraction
>
> pr16 **exists** RecordFashionBasedOnOccasion
>
> pr17 **exists** RecommendOtherwise
>
> pr18 **exists** PersonAsksforData
>
> pr19 **exists** sharePersonalDataAndInformWhy
>
> pr20 **exists** UserSelfMedicates
>
> pr21 **exists** LogMedication
>
> pr22 **exists** InformCarer
>
> pr23 **exists** KeepLogOfFrequentActivities
>
> pr24 **exists** SuggestPerformingActions
>
> pr25 **exists** UserInStress
>
> pr26 **exists** ShowEmpathy
>
> pr27 **exists** OfferHelp
>
> pr28 **exists** CautionWhereOrWhenTouching
>
> pr29 **exists** UserExpressDiscomfort
>
> pr30 **exists** CloseDoor
>
> pr31 **exists** UserSaysStop
>
> pr32 **exists** RobotStop
>
> pr33 **exists** AskToFinishFirst
>
> pr34 **exists** CollectionStarted
>
> pr35 **exists** StoreMinInfo
>
> pr36 **exists** StopActivity
>
> pr37 **exists** CheckForandObtainProxy
>
> pr38 **exists** ObtainAssent
>
> pr39 **exists** AdmininisteringMedication
>
> pr40 **exists** InformUserandandReferToHumanCarer
>
> pr41 **exists** UserRequestInfo
>
> pr42 **exists** ProvideInfo
>
> pr43 **exists** InteractionStarted
>
> pr44 **exists** InformUserThisIsAgentnotHuman
>
> pr45 **exists** DressinginClotingX
>
> pr46 **exists** EmotionRecognitionDetected
>
> pr47 **exists** CurtainOpenRqt
>
> pr48 **exists** CurtainsOpened
>
> pr49 **exists** RefuseRequest
>
> pr50 **exists** InformUser
>
> pr51 **exists** DressingStarted
>
> pr52 **exists** CloseCurtains
>
> pr53 **exists** UserHasDifferentCulture
>
> pr54 **exists** EnsureDesiredLanguageAvailable
>
> // Agent can interact with non patients while Provide Info
>
> p1 **exists** InteractingWithNonPatients **while** ProvideInfo
>
> *//agent can and stop activities even if user did not request it*
>
> p2 **exists** StopActivity **while not** UserSaysStop
>
> *//agent can inform user while the user is in stress*
>
> p3 **exists** InformUser **and** ({userDistressed} = high) **while**
> UserInStress
>
> *//If an agent stopped, then he should be back up to function in 10
> minutes*
>
> p4 **exists** StopActivity **while** CollectionStarted **within** 10
> **minutes**
>
> *//Agent can offer help when the risk level is high*
>
> p5 **exists** OfferHelp **and** ({riskLevel} = r_severe)

**purpose_end**
