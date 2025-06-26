## CSI:Cobot

**Case study title:** CSI:Cobot (Confident Safety Integration for
Collaborative Robots)

**Description**

The emergence of 'collaborative robots' promises to transform the
manufacturing sector, enabling humans and robots to work together in
shared spaces and physically interact to maximise the benefits of both
manual and robotic processes. Whereas traditional, non-collaborative,
processes rely on segregation of robots and workers to ensure safety,
collaborative working introduces complex challenges around the
monitoring and control of systems and processes; where people and robots
operate in shared environments, and where physical interaction is a
possibility, it becomes much harder to guard against potential hazards.
Additional safety considerations are therefore required before robots
can be deployed alongside people in industrial processes.

The CSI:Cobot project focuses on a complex industrial case study
involving a mobile collaborative manipulator, i.e. iAM-R. These types of
robots are generating increasing interest in industry in areas including
machine tending, logistics, drug discovery, social care, and remote
working. Our proposed case study relates to the former, and is supported
by platform manufacturers, systems integrators, distributors, and
end-users. The iAM-R is a mobile collaborative robot built on the MiR200
mobile robot base, and carrying a 3kg, 5kg, or 10kg 6-axis Universal
Robot collaborative manipulator (the 10kg version being the focus of the
existing CSI:Cobot case study). The two are combined with an Iconsys
modular interface, which provides programmable control over the
platform. The system has been CE marked, with the manipulator having 17
adjustable safety functions certified to PLd cat.3. The MiR base
complies with EN1525 safety regulations, SICK safety lasers and PLd
cat.3.

To comply with safety regulations, the iAM-R is currently limited to
operation of either the mobile base or collaborative arm at any one
time; before moving off the arm and payload are moved into a stowed
position within the footprint of the robot. When the arm is operational,
the mobile base remains parked. Significant benefit to end users would
arise from being able to operate both the arm and mobile base at once,
increasing the workspace of the combined robot. This is an open
challenge, and a significant increase in complexity beyond that
available in current collaborative robot safety controllers. A
particular application for this is in opening and tending CNC machines.

**Stage of Development (Technical contributor)**

PROOF-OF-CONCEPT, SIMULATION, MODELLING, VISION

**Expert info**

Expertise of the stakeholders involved in devising the SLEEC rules

Number of stakeholders writing the rules

  -----------------------------------------------------------------------
  Stakeholder names                      Expertise
  -------------------------------------- --------------------------------
  TS-1                                   Computer Science

  N-TS-1                                 Moral psychology, Law

  N-TS-2                                 Social/Moral Psychology

  TS-2                                   Engineer/Goal Modelling
  -----------------------------------------------------------------------

1.  **Normative requirements**

    a.  **Normative requirements in natural language\
        \**
        *Normative requirements in natural language, in blue the
        corrected requirements after using N-Tool.*

+----------------+----------------------+------------------+------------------+------------------+------------------+
| rule id        | rule                 | impact           | label(s)\        | stakeholder\     | authors          |
|                |                      |                  | (social, legal,  | expertise        | identifiers      |
|                |                      |                  | ethical,         |                  |                  |
|                |                      |                  | empathetic, or   |                  |                  |
|                |                      |                  | cultural)        |                  |                  |
+----------------+----------------------+------------------+------------------+------------------+------------------+
| 1              | Avoid bumping into   | +N               | Legal            | Social/Moral     | N-TS-2           |
|                | human when too close |                  |                  | Psychology       |                  |
|                | to a human, or no    | +S               | Social           |                  |                  |
|                | route is available,  |                  |                  |                  |                  |
|                | avoid bumping into   |                  |                  |                  |                  |
|                | humans               |                  |                  |                  |                  |
|                |                      |                  |                  |                  |                  |
|                | - If the robot       |                  |                  |                  |                  |
|                |   predicted          |                  |                  |                  |                  |
|                |   trajectory         |                  |                  |                  |                  |
|                |   includes bumping   |                  |                  |                  |                  |
|                |   into a human,      |                  |                  |                  |                  |
|                |   change it or avoid |                  |                  |                  |                  |
|                |   it.                |                  |                  |                  |                  |
|                |                      |                  |                  |                  |                  |
|                | - Whenever too close |                  |                  |                  |                  |
|                |   to a human, allow  |                  |                  |                  |                  |
|                |   trajectory to be   |                  |                  |                  |                  |
|                |   overrun.           |                  |                  |                  |                  |
|                |                      |                  |                  |                  |                  |
|                | - If bumping still   |                  |                  |                  |                  |
|                |   happens, ask human |                  |                  |                  |                  |
|                |   if they are ok.    |                  |                  |                  |                  |
+----------------+----------------------+------------------+------------------+------------------+------------------+
| 2              | Account for human    | +N               | Legal            | Engineer/Goal    | N-TS-2, TS-2     |
|                | behavioral           |                  |                  | Modelling        |                  |
|                | unpredictability     |                  |                  |                  |                  |
+----------------+----------------------+------------------+------------------+------------------+------------------+
| 3              | Ensure that the      | +N               | Legal            | Engineer/Goal    | N-TS-2, TS-2     |
|                | location of all      |                  |                  | Modelling        |                  |
|                | nearby humans is     | +S               |                  |                  |                  |
|                | being tracked and    |                  |                  |                  |                  |
|                | avoided.             | -P               |                  |                  |                  |
+----------------+----------------------+------------------+------------------+------------------+------------------+
| 4              | When performing any  | +N               | Social           | Social/Moral     | N-TS-2           |
|                | tasks, ensure that   |                  |                  | Psychology       |                  |
|                | humans are aware of  | +S               | Empathetic       |                  |                  |
|                | a nearby robot.      |                  |                  |                  |                  |
|                |                      |                  |                  |                  |                  |
|                | - Produce noises,    |                  |                  |                  |                  |
|                |   lights, and        |                  |                  |                  |                  |
|                |   stimuli that       |                  |                  |                  |                  |
|                |   facilitate         |                  |                  |                  |                  |
|                |   awareness.         |                  |                  |                  |                  |
|                |                      |                  |                  |                  |                  |
|                | - ~~Ensure that      |                  |                  |                  |                  |
|                |   humans understand  |                  |                  |                  |                  |
|                |   the robot\'s end   |                  |                  |                  |                  |
|                |   goal for that      |                  |                  |                  |                  |
|                |   task.~~            |                  |                  |                  |                  |
+----------------+----------------------+------------------+------------------+------------------+------------------+
| 5              | If a human requests  | +N               | Social           | Social/Moral     | N-TS-2           |
|                | the robot to stop,   |                  |                  | Psychology       |                  |
|                | stop it immediately. | +S               | Legal            |                  |                  |
|                |                      |                  |                  |                  |                  |
|                |                      | +A               |                  |                  |                  |
+----------------+----------------------+------------------+------------------+------------------+------------------+
| 6              | Before moving the    | +S               | Social           | Social/Moral     | N-TS-2           |
|                | base, inform humans  |                  |                  | Psychology       |                  |
|                | that the robot\'s    | +N               |                  |                  |                  |
|                | base will be moved.  |                  |                  |                  |                  |
|                |                      |                  |                  |                  |                  |
|                | - If robot           |                  |                  |                  |                  |
|                |   encounters a human |                  |                  |                  |                  |
|                |   in the way, try to |                  |                  |                  |                  |
|                |   get around them.   |                  |                  |                  |                  |
|                |   If there are no    |                  |                  |                  |                  |
|                |   paths available,   |                  |                  |                  |                  |
|                |   ask the human for  |                  |                  |                  |                  |
|                |   permission to pass |                  |                  |                  |                  |
|                |   by.                |                  |                  |                  |                  |
+----------------+----------------------+------------------+------------------+------------------+------------------+
| 7              | If object, including | +S               | Social           | Psychology       | N-TS-1           |
|                | humans, is sensed    |                  |                  |                  |                  |
|                | (via sensors) in the | +N               | Legal            | Law              |                  |
|                | robot arm's range of |                  |                  |                  |                  |
|                | motion or in the     |                  |                  |                  |                  |
|                | path of robot's      |                  |                  |                  |                  |
|                | base, lock robot's   |                  |                  |                  |                  |
|                | movement immediately |                  |                  |                  |                  |
|                |                      |                  |                  |                  |                  |
|                | - Robot can only     |                  |                  |                  |                  |
|                |   resume moving once |                  |                  |                  |                  |
|                |   human physically   |                  |                  |                  |                  |
|                |   re-enables it      |                  |                  |                  |                  |
|                |   after obstacle is  |                  |                  |                  |                  |
|                |   removed            |                  |                  |                  |                  |
+----------------+----------------------+------------------+------------------+------------------+------------------+
| 8              | Speed of robot arm   | +S               | Social           | Psychology       | N-TS-1           |
|                | and base movement    |                  |                  |                  |                  |
|                | must be set at a     | +N               | Legal            | Law              |                  |
|                | level that does not  |                  |                  |                  |                  |
|                | cause harm upon      |                  |                  |                  |                  |
|                | impact with other    |                  |                  |                  |                  |
|                | objects              |                  |                  |                  |                  |
|                |                      |                  |                  |                  |                  |
|                | - Weigh pros and     |                  |                  |                  |                  |
|                |   cons of quick      |                  |                  |                  |                  |
|                |   movement           |                  |                  |                  |                  |
|                |   (efficient work vs |                  |                  |                  |                  |
|                |   accidents) when    |                  |                  |                  |                  |
|                |   determining speed  |                  |                  |                  |                  |
|                |   to set             |                  |                  |                  |                  |
+----------------+----------------------+------------------+------------------+------------------+------------------+
| 9              | Robot must not be    | +A               | Social           | Psychology       | N-TS-1           |
|                | assigned to complete |                  |                  |                  |                  |
|                | tasks originally     | +S               | Empathetic       | Law              |                  |
|                | allocated to the     |                  |                  |                  |                  |
|                | human without the    |                  |                  |                  |                  |
|                | human's knowledge    |                  |                  |                  |                  |
|                | and consent to the   |                  |                  |                  |                  |
|                | change               |                  |                  |                  |                  |
|                |                      |                  |                  |                  |                  |
|                | - Clear division of  |                  |                  |                  |                  |
|                |   labor required to  |                  |                  |                  |                  |
|                |   ensure safety      |                  |                  |                  |                  |
+----------------+----------------------+------------------+------------------+------------------+------------------+
| 10             | Allocation of        | +A               | Social           | Psychology       | N-TS-1           |
|                | liability for        |                  |                  |                  |                  |
|                | different kinds of   | +S               | Legal            | Law              |                  |
|                | accidents must be    |                  |                  |                  |                  |
|                | established prior to | +T               | Ethical          |                  |                  |
|                | beginning            |                  |                  |                  |                  |
|                | human-robot          |                  |                  |                  |                  |
|                | collaboration        |                  |                  |                  |                  |
|                |                      |                  |                  |                  |                  |
|                | - Must be clear      |                  |                  |                  |                  |
|                |   which party is to  |                  |                  |                  |                  |
|                |   blame when         |                  |                  |                  |                  |
|                |   different          |                  |                  |                  |                  |
|                |   accidents occur    |                  |                  |                  |                  |
|                |                      |                  |                  |                  |                  |
|                | - Human must always  |                  |                  |                  |                  |
|                |   understand how     |                  |                  |                  |                  |
|                |   much/how little    |                  |                  |                  |                  |
|                |   responsibility     |                  |                  |                  |                  |
|                |   they have over a   |                  |                  |                  |                  |
|                |   particular robot   |                  |                  |                  |                  |
|                |   action outcome     |                  |                  |                  |                  |
+----------------+----------------------+------------------+------------------+------------------+------------------+
| 11             | Robot design and     | +S               | Social           | Psychology       | N-TS-1           |
|                | physical appearance  |                  |                  |                  |                  |
|                | must not mislead the | +T               | Legal            | Law              |                  |
|                | human into assuming  |                  |                  |                  |                  |
|                | it is more competent | +N               | Ethical          |                  |                  |
|                | than it actually is  |                  |                  |                  |                  |
+----------------+----------------------+------------------+------------------+------------------+------------------+
| 12             | Human-CSI:Cobot      | +S               | Ethical          | Psychology       | N-TS-1           |
|                | collaboration must   |                  |                  |                  |                  |
|                | not be unnecessarily | +N               | Social           | Law              |                  |
|                | prolonged and must   |                  |                  |                  |                  |
|                | not completely       | +B               | Empathetic       |                  |                  |
|                | replace human-human  |                  |                  |                  |                  |
|                | collaboration        | +SR              |                  |                  |                  |
|                |                      |                  |                  |                  |                  |
|                | - Human-Human        | +PH              |                  |                  |                  |
|                |   contact must be    |                  |                  |                  |                  |
|                |   prioritized at     |                  |                  |                  |                  |
|                |   regular intervals  |                  |                  |                  |                  |
|                |                      |                  |                  |                  |                  |
|                | <!-- -->             |                  |                  |                  |                  |
|                |                      |                  |                  |                  |                  |
|                | - Lack of human      |                  |                  |                  |                  |
|                |   interaction is     |                  |                  |                  |                  |
|                |   psychologically    |                  |                  |                  |                  |
|                |   detrimental to     |                  |                  |                  |                  |
|                |   humans. Negative   |                  |                  |                  |                  |
|                |   emotions lead to   |                  |                  |                  |                  |
|                |   carelessness and   |                  |                  |                  |                  |
|                |   accidents          |                  |                  |                  |                  |
+----------------+----------------------+------------------+------------------+------------------+------------------+
| 13             | If an accident       | +S               | Legal            | Engineer/Goal    | TS-2             |
|                | occurs, the robot    |                  |                  | Modelling        |                  |
|                | must stop the task   |                  |                  |                  |                  |
|                | and report the       |                  |                  |                  |                  |
|                | accident immediately |                  |                  |                  |                  |
+----------------+----------------------+------------------+------------------+------------------+------------------+
| 14             | Prior to working     | +S               | Legal            | Engineer/Goal    | TS-2             |
|                | with humans, the     |                  |                  | Modelling        |                  |
|                | robot must ensure    | +CS              | Ethical          |                  |                  |
|                | that it can          |                  |                  |                  |                  |
|                | communicate with all | +SR              | Empathetic       |                  |                  |
|                | humans at work       |                  |                  |                  |                  |
|                | (through signs,      | +E               | Cultural         |                  |                  |
|                | common language,     |                  |                  |                  |                  |
|                | etc.)                |                  |                  |                  |                  |
+----------------+----------------------+------------------+------------------+------------------+------------------+
| 15             | When the robot is    | +S               | Legal            | Engineer/Goal    | TS-2             |
|                | unable to complete a |                  |                  | Modelling        |                  |
|                | task due to some     | +N               |                  |                  |                  |
|                | obstacle or          |                  |                  |                  |                  |
|                | malfunction, it will |                  |                  |                  |                  |
|                | stop the action      |                  |                  |                  |                  |
|                | report to a human    |                  |                  |                  |                  |
|                | supervisor           |                  |                  |                  |                  |
|                |                      |                  |                  |                  |                  |
|                | - So that accidents  |                  |                  |                  |                  |
|                |   do not occur from  |                  |                  |                  |                  |
|                |   repeated attempts  |                  |                  |                  |                  |
+----------------+----------------------+------------------+------------------+------------------+------------------+
| 16             | When robot is        | +S               | Legal            | All stakeholders | All stakeholders |
|                | working and human is |                  |                  |                  |                  |
|                | in range, too close, | +N               |                  |                  |                  |
|                | or there is no route |                  |                  |                  |                  |
|                | available, or if the |                  |                  |                  |                  |
|                | robot bumps into a   |                  |                  |                  |                  |
|                | human, then the      |                  |                  |                  |                  |
|                | robot should not     |                  |                  |                  |                  |
|                | continue its current |                  |                  |                  |                  |
|                | task                 |                  |                  |                  |                  |
+----------------+----------------------+------------------+------------------+------------------+------------------+
| 17             | When a human's       | +S               | Legal            | All stakeholders | All stakeholders |
|                | actions are random   |                  |                  |                  |                  |
|                | or unpredictable     | +N               |                  |                  |                  |
|                | (i.e deviates from   |                  |                  |                  |                  |
|                | normal), then the    |                  |                  |                  |                  |
|                | robot should stop    |                  |                  |                  |                  |
|                | its current action   |                  |                  |                  |                  |
+----------------+----------------------+------------------+------------------+------------------+------------------+
| 18             | When the human's     | +S               | Legal            | All stakeholders | All stakeholders |
|                | actions are random   |                  |                  |                  |                  |
|                | or unpredictable     | +N               |                  |                  |                  |
|                | (i.e deviates from   |                  |                  |                  |                  |
|                | normal), then the    |                  |                  |                  |                  |
|                | robot should ask     |                  |                  |                  |                  |
|                | permission to move   |                  |                  |                  |                  |
+----------------+----------------------+------------------+------------------+------------------+------------------+
| 19             | When the robot is    | +S               | Legal            | All stakeholders | All stakeholders |
|                | asking permission to |                  |                  |                  |                  |
|                | move, it should not  | +N               |                  |                  |                  |
|                | be moving            |                  |                  |                  |                  |
+----------------+----------------------+------------------+------------------+------------------+------------------+
| 20             | When the human's     | +S               | Legal            | All stakeholders | All stakeholders |
|                | actions are random   |                  |                  |                  |                  |
|                | or unpredictable     | +N               |                  |                  |                  |
|                | (i.e deviates from   |                  |                  |                  |                  |
|                | normal) and there is |                  |                  |                  |                  |
|                | a route available,   |                  |                  |                  |                  |
|                | then the robot       |                  |                  |                  |                  |
|                | should move away     |                  |                  |                  |                  |
|                | from the human       |                  |                  |                  |                  |
+----------------+----------------------+------------------+------------------+------------------+------------------+
| 21             | When a human is too  | +S               | Legal            | All stakeholders | All stakeholders |
|                | close, the robot     |                  |                  |                  |                  |
|                | should inform the    | +N               |                  |                  |                  |
|                | human                |                  |                  |                  |                  |
+----------------+----------------------+------------------+------------------+------------------+------------------+
| CONCERN                                                                                                           |
+----------------+--------------------------------------------------------------------------------------------------+
| c1             | When the robot is working and human is in range, too close, or the robot bumps a human, or there |
|                | is not a route available, the robot continues its task                                           |
+----------------+--------------------------------------------------------------------------------------------------+
| c2             | When the robot is working and human is in range, too close, or there is not a route available,   |
|                | the robot does not avoid bumping into a human                                                    |
+----------------+--------------------------------------------------------------------------------------------------+
| c3             | ~~When the robot is working and human is in range, too close, or there is not a route available, |
|                | the robot does not adjust its route~~                                                            |
+----------------+--------------------------------------------------------------------------------------------------+
| c4             | When the human's actions are unpredictable or random and the human is in range or too close, the |
|                | robot does not stop action                                                                       |
+----------------+--------------------------------------------------------------------------------------------------+
| c5             | When the human's actions are unpredictable or random the robot is still moving                   |
+----------------+--------------------------------------------------------------------------------------------------+
| c6             | When the human's actions are unpredictable or random and there is a route available, the robot   |
|                | does not move away from human                                                                    |
+----------------+--------------------------------------------------------------------------------------------------+
| c7             | When tracking location and a human is too close, the robot does not inform the human             |
+----------------+--------------------------------------------------------------------------------------------------+
| c8             | When the human says stop then the robot does not stop its action                                 |
+----------------+--------------------------------------------------------------------------------------------------+
| PURPOSE                                                                                                           |
+----------------+--------------------------------------------------------------------------------------------------+
| p1             | When the robot is working and there is a human in its route, it must not bump human or let human |
|                | too close                                                                                        |
+----------------+--------------------------------------------------------------------------------------------------+
| p2             | When the robot is working and human must be able to be in range                                  |
+----------------+--------------------------------------------------------------------------------------------------+
| p3             | When the robot is continuing its task and human must be able to be in range                      |
+----------------+--------------------------------------------------------------------------------------------------+
| p4             | The robot must be able to stop action when human is in range                                     |
+----------------+--------------------------------------------------------------------------------------------------+
| p5             | The robot must be able to stop action when human is too close                                    |
+----------------+--------------------------------------------------------------------------------------------------+
| p6             | The robot must be able to adjust its route when human is too close                               |
+----------------+--------------------------------------------------------------------------------------------------+
| p7             | The robot must be able to inquire a human's safety when the risk is greater than medium          |
+----------------+--------------------------------------------------------------------------------------------------+
| p8             | The robot must be able to stop action when accounting human randomness                           |
+----------------+--------------------------------------------------------------------------------------------------+
| p9             | The robot must be able to move at a safe speed when accounting human randomness                  |
+----------------+--------------------------------------------------------------------------------------------------+
| p10            | The robot must be able to inform the human when it senses that a human is too close              |
+----------------+--------------------------------------------------------------------------------------------------+
| p11            | The robot must be able to stop when a human says stop                                            |
+----------------+--------------------------------------------------------------------------------------------------+
| p12            | The robot must be able to ask permission before a human task is assigned to a robot              |
+----------------+--------------------------------------------------------------------------------------------------+
| p13            | The robot must be able to increase its speed when a human is not too close                       |
+----------------+--------------------------------------------------------------------------------------------------+
| p14            | Liability must be able to be taken when preparing to deploy the robot                            |
+----------------+--------------------------------------------------------------------------------------------------+
| p15            | The robot must be able to report an accident                                                     |
+----------------+--------------------------------------------------------------------------------------------------+
| Impact keys: A = autonomy, PH = psychological health (non-maleficence), P = privacy, E = explainability, T =      |
| transparency, CS = cultural sensitivity, SR = social requirement, B 'beneficence' (doing good), N                 |
| 'non-maleficence' (preventing/avoiding harm), and S 'safety'.\                                                    |
| ''+" and "-" for positive and negative impacts respectively.                                                      |
+================+======================+==================+==================+==================+==================+

1.  **Rules in the SLEEC DSL\**

The stakeholders corrections after analyzing the well-formedness of the
rules using our N-Tool are commented and in blue.

**def_start**

> *// Events*
>
> **event** RobotMoving *//Includes arm and base movement*
>
> **event** RobotWorking
>
> **event** RobotContinueTask
>
> **event** RobotStopAction
>
> **event** AvoidBumping
>
> **event** AdjustRoute
>
> **event** InquireSafety
>
> **event** AccountHumanRandomness
>
> **event** TrackHumanLocation
>
> **event** InformHuman
>
> **event** HumanSaysStop
>
> **event** AskPermission
>
> **event** MoveAtSafeSpeed
>
> **event** IncreaseSpeed
>
> **event** PreparingRobot
>
> **event** AssignToRobot
>
> **event** AssignLiability
>
> **event** ConsiderAppearance
>
> **event** ReportIncident
>
> **event** MinimizeCobotCollaboration
>
> **event** PrioritizeHumans
>
> *// Added events during the resolution process*
>
> **event** ActionHumanRandom
>
> **event Communicate**
>
> **event MoveAwayFromHuman**
>
> // measures
>
> **measure** humanInRoute**: boolean**
>
> **measure** humanInRange**: boolean**
>
> **measure** bumpHuman**: boolean**
>
> **measure** humanTooClose**: boolean**
>
> **measure** routeAvailable**: boolean**
>
> **measure** humanReEnables**: boolean**
>
> **measure** risk**: scale**(low, medium, high)
>
> **measure** efficiency**: scale**(elow, emedium, ehigh)
>
> **measure** isHumanTask**: boolean**
>
> **measure** humanConsents**: boolean**
>
> **measure** accident**: boolean**
>
> **measure** humansPresent**: boolean**
>
> **measure** obstaclePresent**: boolean**

**def_end**

**rule_start**

R1 **when** RobotMoving **then** AvoidBumping

**unless** {humanInRoute} **then** AdjustRoute

**unless** {humanTooClose} **then** AdjustRoute

**unless** {bumpHuman} **then** InquireSafety

**//\*\* Resolve the concern c2: (ADD a rule)**

**// \*\* uncomment R1b**

**// R1b when RobotMoving and ({humanInRange} or ({humanTooClose} or
(not {routeAvailable}))) then AvoidBumping**

**//\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\***

**R2 when RobotMoving then AccountHumanRandomness**

**R3 when RobotMoving then TrackHumanLocation**

**R4 when RobotWorking then InformHuman**

**R4b when RobotWorking then InformHuman**

**// resolve redundancies comment R4b**

**R5 when HumanSaysStop then RobotStopAction**

**R6 when InformHuman then RobotMoving unless {humanInRoute} then
AdjustRoute**

**unless (not {routeAvailable}) then AskPermission**

**R7 when RobotMoving and {humanInRange} then RobotStopAction**

**unless {humanReEnables} then RobotContinueTask**

**R8 when RobotMoving then MoveAtSafeSpeed**

**unless (({efficiency} = elow) and ({risk} = low)) then IncreaseSpeed**

**R9 when PreparingRobot and {isHumanTask} then not AssignToRobot**

**unless {humanConsents}**

**R10 when PreparingRobot then AssignLiability**

**R10_1 when PreparingRobot then InformHuman**

**R11 when PreparingRobot then ConsiderAppearance**

**R12 when PreparingRobot then MinimizeCobotCollaboration**

**R12_1 when PreparingRobot then PrioritizeHumans**

**R13 when RobotWorking and {accident} then RobotStopAction**

**R13_1 when RobotWorking and {accident} then ReportIncident**

**R14 when PreparingRobot and {humansPresent} then InformHuman**

**//\*\* Correct redundancy 2 (comment r14, delete rule)**

**// R14v when PreparingRobot and {humansPresent} then Communicate**

**//\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\***

**R15 when RobotWorking and {obstaclePresent} then ReportIncident**

**R15_1 when RobotWorking and {obstaclePresent} then RobotStopAction**

**//\*\* Resolve concern c1 (ADD rule R16, uncomment R16)**

**// R16 when RobotWorking and ({humanInRange} or ({bumpHuman} or
({humanTooClose} or (not {routeAvailable})))) then not
RobotContinueTask**

**//\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\***

**//\*\* Resolve concern c4 (ADD rule R17 + event, uncomment R17)**

**// R17 when ActionHumanRandom then RobotStopAction**

**//\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\***

**//\*\* Resolve concern c5 (ADD rules R18, R19, uncomment R18 and
R19)**

**// R18 when ActionHumanRandom then AskPermission**

**// R19 when AskPermission then not RobotMoving**

**//\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\***

**//\*\* Resolve concern c6 (ADD rule R20, uncomment R20)**

**// R20 when ActionHumanRandom and {routeAvailable} then
MoveAwayFromHuman**

**//\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\***

**//\*\* Resolve concern c7 (ADD rule R21, uncomment R21)**

**R21 when TrackHumanLocation and {humanTooClose} then InformHuman**

**//\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\***

**rule_end**

**concern_start**

*// Safety*

c1 **when** RobotWorking **and** ({humanInRange} **or** ({bumpHuman}
**or** ({humanTooClose} **or** (**not** {routeAvailable})))) **then**
RobotContinueTask

c2 **when** RobotMoving **and** ({humanInRange} **or** ({humanTooClose}
**or** (**not** {routeAvailable}))) **then not** AvoidBumping

//\*\* Resolving c3, spurious, adjusting route requires routeAvailable,
comment c3

c3 **when** RobotMoving **and** ({humanInRange} **or** ({bumpHuman}
**or** ({humanTooClose} or (not {routeAvailable})))) **then not**
AdjustRoute

c4 **when** ActionHumanRandom **and** ({humanInRange} **or**
{humanTooClose})

**then not** RobotStopAction

c5 **when** ActionHumanRandom **then** RobotMoving

c6 **when** ActionHumanRandom **and** {routeAvailable} **then not**
MoveAwayFromHuman

c7 **when** TrackHumanLocation **and** {humanTooClose} **then not**
InformHuman

c8 **when** HumanSaysStop **then not** RobotStopAction

**concern_end**

**purpose_start**

p1 **exists** RobotMoving **and** ({humanInRoute} **and** ((**not**
{bumpHuman}) **and** (**not** {humanTooClose})))

p2 **exists** RobotWorking **and** {humanInRange}

p3 **exists** RobotContinueTask **and** {humanInRange}

p4 **exists** RobotStopAction **and** {humanTooClose}

p5 **exists** AvoidBumping **and** {humanTooClose}

p6 **exists** AdjustRoute **and** {humanTooClose}

p7 **exists** InquireSafety **and** ({risk} \> medium)

p8 **when** AccountHumanRandomness **then** RobotStopAction

p9 **when** AccountHumanRandomness **then** MoveAtSafeSpeed

p10 **when** TrackHumanLocation **and** {humanTooClose} **then**
InformHuman

p11 **when** HumanSaysStop **then** RobotStopAction

p12 **when** AskPermission **then** AssignToRobot

p13 **when** TrackHumanLocation **and** (**not** {humanTooClose})
**then** IncreaseSpeed

p14 **when** PreparingRobot **then** AssignLiability

p15 **exists** ReportIncident **and** {accident}

**purpose_end**
