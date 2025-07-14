## ALMI

**Case study title:** ALMI **(**Ambient Assisted Living for Long-term
Monitoring and Interaction)

**Description**

With a rapidly ageing population, the world is facing a social care
crisis (Appleby, 2009). Without a step change in the provision of social
care, especially to the elderly, the increase in the budgets and
resources allocated to social care will soon become unsustainable.
*Ambient assisted living* (Blackman et al., 2016) (i.e., assisted living
support provided in a person's daily environment, with the aid of
robotic and autonomous systems -- RAS, Artificial Intelligence -- AI,
and other technologies) is widely envisaged as a key component of such a
step change (Lee et al., 2018).

Given this vision, the development of assisted-living RAS and AI
solutions has been the focus of intense research and industrial effort
in recent years. Designed to help or even replace carers at home and in
care homes, these solutions aim to support people with motor or
cognitive impairments in a wide range of tasks, increasing their ability
to pursue daily living activities independently. These advances have
provided RAS solutions capable of assisting elderly and disabled users
both in a monitoring/advisory role and with physical tasks. However,
integrating the two types of assistance into a *combined assistive-care
RAS solution that can be used safely over a long period of time* still
poses significant challenges (SPARK, 2015).

In the ALMI project, we employ a TIAGo robot that uses both its speech
interaction and its object manipulation capabilities to help a user with
mild motor and cognitive impairments in the daily activity of preparing
a meal. Specifically, the TIAGo robot (i) provides step-by-step voice
instructions guiding the user through the meal preparation task; (ii)
fetches and hands to the user some of the food ingredients, kitchen
utensils, crockery, etc. required for these steps; (iii) reminds the
user (if needed) where to find other items that are required for the
task, and that the robot cannot reach or handle. Providing such support
requires the robot to dynamically create, update and exploit a
"knowledge store" of household item locations (over a long period of
time); to track the user's progress with the meal preparation task, so
that instructions are delivered progressively and repeated if necessary;
to handle disruptions safely, etc.

The safe handling of disruptions requires the robot to react to events
such as task interruptions due to a phone call received by the user, or
loss of vision due to the light being switched off accidentally by the
user, or as a result of a power cut. If such unexpected events interrupt
the execution of the task, the robot will mitigate the detrimental
effects of interruption (if there are remedial actions that can be
performed), or issue an alert when an unsafe situation cannot be handled
directly by using its capabilities.

> TIAGo is a highly customisable mobile robotic platform with 15 degrees
> of freedom (DoF). The TIAGo robot comprises a mobile base with a
> footprint of 54cm, an adjustable height torso enabling the robot to
> vary its overall height between 110--140cm, a pan-tilt head, and a 7
> DoF manipulator arm with a reach of 87cm and a payload of 3kg. The
> mobile base is provided with a differential drive capable of speeds of
> up to 1 m/s, and uses a LIDAR laser for indoor navigation. The TIAGo
> control software and applications are deployed on an Intel i7 (7th
> generation) computer with 16 GB of RAM, 500 GB of disk space, and
> running Ubuntu LTS 64-bit with the RT Preempt real-time framework.
> Multiple ROS LTS controllers running in a real-time control loop are
> used to manage robot components including its torso, head and arm
> positions, with joint trajectory controllers used from groups of
> joints and a Head Action Server for controlling the robot's gaze. The
> TIAGo navigation unit supports laser-based mapping and self-location,
> with obstacle avoidance and navigation to map point capabilities. The
> upper-body motion engine controllers support path planning with
> self-collision avoidance, and come with a wide range of pre-programmed
> motions and facilities for defining customised motions. Particularly
> relevant for ALMI, TIAGo supports (i) speech-based interaction with
> the users through its integrated ACAPELA[^1] text to-speech system and
> DeepSpeech[^2] speech-to-text module; (ii) object and people detection
> thanks to its ASUS XTION Pro Live 3D Camera mounted on the robot's
> head.

Appleby, J. Spending on health and social care over the next 50 years.
Why think long term?, 2013. The King's Fund. **4.** M. W. Bewernitz, W.
C. Mann, P. Dasler, and P. Belchior. Feasibility of machine-based
prompting to assist persons with dementia. *Assistive Technology*,
21(4):196--207, 2009.

Blackman, S., Matlo, C., Bobrovitskiy, C., Waldoch, A., Fang, M L.,
Jackson, P., Mihailidis, A., Nygard, L., Astell, A., and Sixsmith, A.
Ambient assisted living technologies for aging well: a scoping review.
*Journal of Intelligent Systems*, 25(1):55--69, 2016

> Lee H R. and Riek L D. Reframing assistive robots to promote
> successful aging. *ACM Transactions on Human-Robot Interaction
> (THRI)*, 7(1):1--23, 2018.
>
> SPARC -- The Partnership for Robotics in Europe. Robotics 2020
> multi-annual roadmap for robotics in Europe, 2015.

**Stage of Development (Technical contributor)**

Deployed, SIMULATION, MODELLING

**Expert info**

Expertise of the stakeholders involved in devising the SLEEC rules

Number of stakeholders writing the rules

  -----------------------------------------------------------------------
  Stakeholder names                   Expertise
  ----------------------------------- -----------------------------------
  TS-1                                Computer Science

  N-TS-1                              Social/Moral Psychology

  N-TS-2                              Moral Psychology, Law

  TS-2                                Engineer/Goal Modelling
  -----------------------------------------------------------------------

**Main functionality and purpose**

In the ALMI project, we harness the PAL Robotics framework, TIAGo, and
evolve it into an array of social robotic solutions. TIAGo employs both
its voice interaction for audio commands and its object manipulation
skills to assist a user with mild motor and cognitive impairments in the
everyday task of meal preparation. Moreover, TIAGo is equipped with the
essential manipulation capabilities and assurance evidence for the
customized robotic arm, and it also possesses environment monitoring
capabilities to establish and maintain a knowledgebase of objects.

Whenever disruptive changes occur (for example, when the user abandons a
task), TIAGo adapts both its configuration and behaviour to achieve task
completion, or to gracefully degrade, preserving safety even if the task
is not successfully completed. To achieve this, we developed methods for
the synthesis of adaptation plans for the robotic platform. Determining
the course for adaptation in our experimental environment entails
securing a safe combination of robot configuration and task plan
specification for the robot's execution context.

PAL Robotics constructed the first prototype of a novel robotic arm
featuring new sensors and capabilities to adhere to the standards of
industrial and personal care robotics. Cutting-edge electronics and
actuators have been applied that allowed it to implement more advanced
control functions (e.g, force control).Together with the application of
brakes, they improved the security features of the TIAGo arm to be able
to collaborate closely with humans. The new arm complies with the
expected levels of security and robustness. The capabilities of this new
arm are tailored for applications involving human-robot interaction. On
the one hand, the torque sensing and Ethercat bus allow for superior
low-level closed-loop torque control. This allows the full control of
the arm in effort mode, which makes the arm compliant. Namely, the
control architecture can be modified at a low level by emulating a
spring at the joint level, and this permits to use the robot exactly as
it was used before, but with this new compliant feature, and not losing
any accuracy. All standard robot movements can now be performed safely
so that any potential collisions, either with the robot or any external
entity, would not harm the human or the robot. On the other hand, there
are breaks also at joint level. In the case there was any misuse of the
robot, or even the emergency stop was activated, the arm would not fall
but maintain position. Hence, as a direct consequence of these two
features of the arm, a layer in safety of the interaction between
machine and human has been added, without losing any of the previous
capabilities of the robot.

TIAGo is also capable of generating a semantic map of an apartment,
learning about an object or location, and executing general-purpose
tasks as instructed by a user through its human-robot interaction,
navigation, and robot-object interaction abilities. The TIAGo knowledge
repository consists of a semantic map of the user\'s surroundings, with
the positions of objects specified at particular sites. This semantic
map is formulated using the existing ROS (The Robot Operating System)
Navigation Stack functionality, after mapping the user\'s environment
and/or inputting the details. The semantic map is devised to be as
reusable as possible with custom types of objects with various
attributes, thereby enabling TIAGo to hold a variety of household items
like furniture, utensils, and meal preparation ingredients. This
approach is embodied in a customised middleware that captures and
processes information broadcasted to ROS topics, incorporating it into a
knowledge store containing the domain models needed for validation and
adaptation.

> **Normative requirements**

1.  **Normative requirements in natural language\
    \**
    *Normative requirements in natural language, in blue the corrected
    requirements after using N-Tool.***\**

+---------------+-------------------------+----------------+----------------+----------------+----------------+
| rule id       | rule                    | impact         | label(s)\      | stakeholder\   | authors        |
|               |                         |                | (social,       | expertise      | identifiers    |
|               |                         |                | legal,         |                |                |
|               |                         |                | ethical,       |                |                |
|               |                         |                | empathetic, or |                |                |
|               |                         |                | cultural)      |                |                |
+---------------+-------------------------+----------------+----------------+----------------+----------------+
| 1             | When it is time for a   | -CS\           | cultural       | Computer       | TS-1           |
|               | meal, inform the user   | -N             |                | science        |                |
|               | that it is time to cook |                |                |                |                |
|               | the meal (breakfast,    |                |                |                |                |
|               | lunch, or dinner)       |                |                |                |                |
|               | within x minutes.       |                |                |                |                |
|               |                         |                |                |                |                |
|               | - If there is an        |                |                |                |                |
|               |   environmental         |                |                |                |                |
|               |   constraint (e.g.,     |                |                |                |                |
|               |   they are busy),       |                |                |                |                |
|               |   remind them later.    |                |                |                |                |
+---------------+-------------------------+----------------+----------------+----------------+----------------+
| 2             | Monitor the time        |                |                |                |                |
|               | between meals and       |                |                |                |                |
|               | ensure that the user's  |                |                |                |                |
|               | last meal does not      |                |                |                |                |
|               | exceed the max time     |                |                |                |                |
|               | limit between meals.    |                |                |                |                |
|               |                         |                |                |                |                |
|               | - If max time limit is  |                |                |                |                |
|               |   exceeded, call        |                |                |                |                |
|               |   caregiver and inform  |                |                |                |                |
|               |   them of the situation |                |                |                |                |
|               |   and in the meantime,  |                |                |                |                |
|               |   suggest they have a   |                |                |                |                |
|               |   snack.                |                |                |                |                |
+---------------+-------------------------+----------------+----------------+----------------+----------------+
| 3             | ~~If the human is       | -P\            | Ethical, legal | Computer       | TS-1           |
|               | detected on the floor,  | -N\            |                | science        |                |
|               | call for help (either   | -S             |                |                |                |
|               | caregiver or emergency  |                |                |                |                |
|               | medical help)           |                |                |                |                |
|               | immediately.~~          |                |                |                |                |
|               |                         |                |                |                |                |
|               | - ~~unless the human    |                |                |                |                |
|               |   does not assent with  |                |                |                |                |
|               |   this action~~         |                |                |                |                |
|               |                         |                |                |                |                |
|               | If the human is         |                |                |                |                |
|               | detected on the floor,  |                |                |                |                |
|               | then ask whether the    |                |                |                |                |
|               | robot should call for   |                |                |                |                |
|               | help                    |                |                |                |                |
|               |                         |                |                |                |                |
|               | - When the robot asks   |                |                |                |                |
|               |   whether to call for   |                |                |                |                |
|               |   help and the human    |                |                |                |                |
|               |   does not assent, then |                |                |                |                |
|               |   do not inform the     |                |                |                |                |
|               |   caregiver or call     |                |                |                |                |
|               |   emergency services.   |                |                |                |                |
+---------------+-------------------------+----------------+----------------+----------------+----------------+
| 4             | If a safe path is not   | -N\            | Empathetic     | Computer       | TS-1           |
|               | identified by the robot | -PH            |                | science        |                |
|               | to traverse the         |                |                |                |                |
|               | environment, inform the |                |                |                |                |
|               | user about that.        |                |                |                |                |
|               |                         |                |                |                |                |
|               | - unless the user is    |                |                |                |                |
|               |   unable to respond     |                |                |                |                |
|               |   (e.g., busy,          |                |                |                |                |
|               |   distressed, etc.)     |                |                |                |                |
+---------------+-------------------------+----------------+----------------+----------------+----------------+
| 5             | If user suggests that   | +A             | Social,        | Social/Moral   | N-TS-1         |
|               | they want to cook the   |                | empathetic     | Psychology     |                |
|               | meal by themselves,     | +CS            |                |                |                |
|               | allow them to do it.    |                |                |                |                |
|               |                         | +PH            |                |                |                |
|               | - Estimate the risk of  |                |                |                |                |
|               |   all actions they      |                |                |                |                |
|               |   could do in the       |                |                |                |                |
|               |   kitchen.              |                |                |                |                |
|               |                         |                |                |                |                |
|               | - If high risk is       |                |                |                |                |
|               |   detected (e.g.,       |                |                |                |                |
|               |   shaking while using a |                |                |                |                |
|               |   knife), suggest that  |                |                |                |                |
|               |   the user stop cooking |                |                |                |                |
|               |   immediately and       |                |                |                |                |
|               |   safely take over.     |                |                |                |                |
|               |                         |                |                |                |                |
|               | <!-- -->                |                |                |                |                |
|               |                         |                |                |                |                |
|               | - Only Interfere if any |                |                |                |                |
|               |   hazard is detected    |                |                |                |                |
|               |   (e.g., fire)          |                |                |                |                |
+---------------+-------------------------+----------------+----------------+----------------+----------------+
| 6             | Based on user\'s        | +S             | Social,        | Social/Moral   | N-TS-1         |
|               | limitation, give advice |                | empathetic     | Psychology     |                |
|               | on what they should or  | +CS            |                |                |                |
|               | should not do by        |                |                |                |                |
|               | themselves (e.g., if    | +PH            |                |                |                |
|               | user has parkinson\'s,  |                |                |                |                |
|               | advice against cutting  |                |                |                |                |
|               | vegetables and offer to |                |                |                |                |
|               | do all the mise en      |                |                |                |                |
|               | place)                  |                |                |                |                |
+---------------+-------------------------+----------------+----------------+----------------+----------------+
| 7             | Before the user         | +S             | Social,        | Social/Moral   | N-TS-1         |
|               | manipulates kitchen     |                | empathetic     | Psychology     |                |
|               | appliances, check the   |                |                |                |                |
|               | temperature and warn    |                |                |                |                |
|               | them as needed (e.g.,   |                |                |                |                |
|               | oven is now hot, be     |                |                |                |                |
|               | careful when you touch  |                |                |                |                |
|               | it)                     |                |                |                |                |
+---------------+-------------------------+----------------+----------------+----------------+----------------+
| 8             | Monitor the time of the | +S             | Social,        | Social/Moral   | N-TS-1         |
|               | food being prepared and |                | empathetic     | Psychology     |                |
|               | inform the user when    |                |                |                |                |
|               | they should be ready.   |                |                |                |                |
+---------------+-------------------------+----------------+----------------+----------------+----------------+
| 9             | During first            | +SR            | Social,        | Social/Moral   | N-TS-1         |
|               | interaction, ask the    |                | empathetic,    | Psychology     |                |
|               | user about the kinds of | +CS            | cultural,      |                | N-TS-2         |
|               | cuisines they like,     |                | Legal          | Law            |                |
|               | abilities they have,    |                |                |                |                |
|               | ingredients they        |                |                |                |                |
|               | typically consume, and  |                |                |                |                |
|               | food allergies they     |                |                |                |                |
|               | have.                   |                |                |                |                |
|               |                         |                |                |                |                |
|               | - TIAGo must record,    |                |                |                |                |
|               |   monitor, and keep     |                |                |                |                |
|               |   updated a list of the |                |                |                |                |
|               |   user's health         |                |                |                |                |
|               |   concerns, dietary     |                |                |                |                |
|               |   restrictions, and     |                |                |                |                |
|               |   allergies.            |                |                |                |                |
+---------------+-------------------------+----------------+----------------+----------------+----------------+
| 10            | When suggesting meals,  | +SR            | Social,        | Social/Moral   | N-TS-1         |
|               | make sure to consider   |                | empathetic,    | Psychology     |                |
|               | the cultural,           | +CS            | cultural       |                | N-TS-2         |
|               | religious, and          |                |                | Law            |                |
|               | individual practices of |                |                |                | TS-2           |
|               | the user.               |                |                | Engineer/Goal  |                |
|               |                         |                |                | Modelling      |                |
+---------------+-------------------------+----------------+----------------+----------------+----------------+
| 11            | During first            | +S             | Social, legal  | Social/Moral   | N-TS-1         |
|               | interaction, ask the    |                |                | Psychology     |                |
|               | user for an emergency   | +SR            |                |                |                |
|               | contact. Inform them    |                |                |                |                |
|               | that this emergency     |                |                |                |                |
|               | contact will be         |                |                |                |                |
|               | contacted if they have  |                |                |                |                |
|               | any emergencies while   |                |                |                |                |
|               | cooking.                |                |                |                |                |
+---------------+-------------------------+----------------+----------------+----------------+----------------+
| 12            | Ensure that only the    | +P             | Social, legal  | Social/Moral   | N-TS-1         |
|               | main user (or people    |                |                | Psychology     |                |
|               | authorized by the main  |                |                |                |                |
|               | user) can see the       |                |                |                |                |
|               | history of meals        |                |                |                |                |
|               | cooked.                 |                |                |                |                |
|               |                         |                |                |                |                |
|               | - If data needs to be   |                |                |                |                |
|               |   checked, provide      |                |                |                |                |
|               |   summaries only (e.g., |                |                |                |                |
|               |   amount of calories    |                |                |                |                |
|               |   and nutrients         |                |                |                |                |
|               |   consumed)             |                |                |                |                |
+---------------+-------------------------+----------------+----------------+----------------+----------------+
| 13            | If user's               | +B             | Social         | Psychology     | N-TS-2         |
|               | motor/cognitive         |                |                |                |                |
|               | impairment causes them  | +N             | Legal          | Law            |                |
|               | to move in an           |                |                |                |                |
|               | unpredictable manner    | +S             |                |                |                |
|               | (e.g. hands jerking     |                |                |                |                |
|               | uncontrollably), do not |                |                |                |                |
|               | allow agent to hand     |                |                |                |                |
|               | them sharp, heavy, or   |                |                |                |                |
|               | otherwise dangerous     |                |                |                |                |
|               | objects                 |                |                |                |                |
+---------------+-------------------------+----------------+----------------+----------------+----------------+
| 14            | If the user trusts      | +SR            | Social         | Psychology     | N-TS-2         |
|               | agent to complete tasks |                |                |                |                |
|               | it was not designed to  | +A             | Empathetic     | Law            |                |
|               | do, agent must          |                |                |                |                |
|               | frequently remind the   | +T             |                |                |                |
|               | user of its limitations |                |                |                |                |
|               |                         | +N             |                |                |                |
|               | - Unless user needs     |                |                |                |                |
|               |   particularly special  |                |                |                |                |
|               |   help/attention        |                |                |                |                |
+---------------+-------------------------+----------------+----------------+----------------+----------------+
| 15            | Agent's appearance must | +SR            | Social         | Psychology     | N-TS-2         |
|               | be appropriate for its  |                |                |                |                |
|               | purpose                 | +A\            | Empathetic     | Law            |                |
|               |                         | +PH            |                |                |                |
|               | - Unless a particular   |                |                |                |                |
|               |   user needs special    |                |                |                |                |
|               |   design accommodations |                |                |                |                |
+---------------+-------------------------+----------------+----------------+----------------+----------------+
| 16            | Agent's choice of       | +A             | Social         | Psychology     | N-TS-2         |
|               | speech and intonation   |                |                |                |                |
|               | must be calibrated to   | +CS            | Cultural       | Law            |                |
|               | the demographic         |                |                |                |                |
|               | background of user      |                | Empathetic     |                |                |
+---------------+-------------------------+----------------+----------------+----------------+----------------+
| 17            | If agent must provide   | +A             | Social         | Psychology     | N-TS-2         |
|               | spoken instructions to  |                |                |                |                |
|               | user, frame these       | +CS            | Cultural       | Law            | TS-2           |
|               | instructions in first   |                |                |                |                |
|               | person plural "We".     |                | Empathetic     | Engineer/Goal  |                |
|               |                         |                |                | Modelling      |                |
|               | - Independently offer   |                |                |                |                |
|               |   to repeat             |                |                |                |                |
|               |   instructions          |                |                |                |                |
+---------------+-------------------------+----------------+----------------+----------------+----------------+
| 18            | Prior to starting       |                |                |                |                |
|               | cooking, ask the user   |                |                |                |                |
|               | what their preferred    |                |                |                |                |
|               | level of detail for the |                |                |                |                |
|               | cooking instructions    |                |                |                |                |
|               | should be.              |                |                |                |                |
+---------------+-------------------------+----------------+----------------+----------------+----------------+
| 19            | If user decides to      | +A             | Social         | Psychology     | N-TS-2         |
|               | change their mind about |                |                |                |                |
|               | a certain cooking       | +S             | Empathetic     | Law            |                |
|               | approach, recipe, or    |                |                |                |                |
|               | ingredient, agent must  |                |                |                |                |
|               | flexibly change course  |                |                |                |                |
|               | and recalculate a new   |                |                |                |                |
|               | approach                |                |                |                |                |
|               |                         |                |                |                |                |
|               | - Unless doing so will  |                |                |                |                |
|               |   cause direct physical |                |                |                |                |
|               |   harm to the user      |                |                |                |                |
+---------------+-------------------------+----------------+----------------+----------------+----------------+
| 20            | If user misplaces or    | +A             | Social         | Psychology     | N-TS-2         |
|               | changes the location of |                |                |                |                |
|               | objects, ingredients,   |                |                | Law            |                |
|               | or utensils within the  |                |                |                |                |
|               | kitchen environment,    |                |                |                |                |
|               | agent must update its   |                |                |                |                |
|               | map of kitchen to keep  |                |                |                |                |
|               | track of new location   |                |                |                |                |
|               |                         |                |                |                |                |
|               | - Unless new location   |                |                |                |                |
|               |   foreseeably causes    |                |                |                |                |
|               |   physical harm to      |                |                |                |                |
|               |   user, agent must not  |                |                |                |                |
|               |   Interfere with how    |                |                |                |                |
|               |   user wishes to        |                |                |                |                |
|               |   re-organize their     |                |                |                |                |
|               |   kitchen               |                |                |                |                |
+---------------+-------------------------+----------------+----------------+----------------+----------------+
| 21            | ~~If smoke detector     | +S             | Legal          | Engineer/Goal  | TS-2           |
|               | goes off then call      |                |                | Modelling      |                |
|               | emergency services~~    | +SR            | Ethical        |                |                |
|               |                         |                |                |                |                |
|               | - ~~Unless the user     |                | Empathetic     |                |                |
|               |   disables the alarm    |                |                |                |                |
|               |   and it doesn't start  |                |                |                |                |
|               |   again within 5        |                |                |                |                |
|               |   minutes (so there is  |                |                |                |                |
|               |   no fire, only         |                |                |                |                |
|               |   temporary smoke),     |                |                |                |                |
|               |   then open windows,    |                |                |                |                |
|               |   shut down appliances, |                |                |                |                |
|               |   ask the user if they  |                |                |                |                |
|               |   are okay, and send an |                |                |                |                |
|               |   alert to the          |                |                |                |                |
|               |   caregiver.~~          |                |                |                |                |
|               |                         |                |                |                |                |
|               | If smoke detector goes  |                |                |                |                |
|               | off then call emergency |                |                |                |                |
|               | services within 2       |                |                |                |                |
|               | minutes                 |                |                |                |                |
|               |                         |                |                |                |                |
|               | - Unless the user       |                |                |                |                |
|               |   disables the alarm    |                |                |                |                |
|               |   and the alarm does    |                |                |                |                |
|               |   not restart, then     |                |                |                |                |
|               |   take fire safety      |                |                |                |                |
|               |   measures              |                |                |                |                |
|               |                         |                |                |                |                |
|               | - Which are to open the |                |                |                |                |
|               |   windows, ask the user |                |                |                |                |
|               |   if they are okay, and |                |                |                |                |
|               |   send an alert to the  |                |                |                |                |
|               |   caregiver             |                |                |                |                |
+---------------+-------------------------+----------------+----------------+----------------+----------------+
| Concern                                                                                                     |
+---------------+---------------------------------------------------------------------------------------------+
| c1            | ~~When human is on the floor, and the user is occupied and the risk level is high, then the |
|               | robot must not call emergency services~~                                                    |
+---------------+---------------------------------------------------------------------------------------------+
| c2            | When allowing the user to cook and there is a hazard or high risk level, the agent must not |
|               | interfere safely                                                                            |
+---------------+---------------------------------------------------------------------------------------------+
| c3            | When checking temperature and there is a hazard, the agent must not inform user             |
+---------------+---------------------------------------------------------------------------------------------+
| c4            | When the smoke detector alarm goes off and the user does not disable the alarm, or the      |
|               | alarm restart, then the agent must not call emergency services within 2 minutes             |
+---------------+---------------------------------------------------------------------------------------------+
| c5            | When taking fire safety measures the agent must not open windows                            |
+---------------+---------------------------------------------------------------------------------------------+
| c6            | When the user wants to cook the agent must not allow the user to cook                       |
+---------------+---------------------------------------------------------------------------------------------+
| c7            | When giving cooking instructions then the agent must not use first person plural language   |
+---------------+---------------------------------------------------------------------------------------------+
| c8            | When the user changes their mind and the risk level is less than high the agent must not    |
|               | recalculate the approach                                                                    |
+---------------+---------------------------------------------------------------------------------------------+
| c9            | When giving a suggestion the agent must not consider their cultural or religious practices  |
+---------------+---------------------------------------------------------------------------------------------+
| c10           | When the agent is deployed and an unauthorized person asks for data, then the agent must    |
|               | show data history                                                                           |
+---------------+---------------------------------------------------------------------------------------------+
| c11           | When showing data history and the data needs checking, the agent must not provide data      |
|               | summaries                                                                                   |
+---------------+---------------------------------------------------------------------------------------------+
| Purpose                                                                                                     |
+---------------+---------------------------------------------------------------------------------------------+
| p1            | The agent must be able to prepare deployment                                                |
+---------------+---------------------------------------------------------------------------------------------+
| p2            | The agent must be able to meet user                                                         |
+---------------+---------------------------------------------------------------------------------------------+
| p3            | The agent must be able to inform user                                                       |
+---------------+---------------------------------------------------------------------------------------------+
| p4            | The agent must be able to inform user when the smoke alarm goes off and the user disables   |
|               | the alarm or the alarm restarts                                                             |
+---------------+---------------------------------------------------------------------------------------------+
| p5            | The agent must be able to remind user of its limitations when the user is occupied and the  |
|               | risk level is high                                                                          |
+---------------+---------------------------------------------------------------------------------------------+
| p6            | The agent must be able to ask the user if they are well if they are detected on the floor   |
|               | and the human assents to being on the floor                                                 |
+---------------+---------------------------------------------------------------------------------------------+
| p7            | The agent must be able to call emergency services when the human is on the floor and the    |
|               | risk level is high                                                                          |
+---------------+---------------------------------------------------------------------------------------------+
| p8            | The agent must be able to ask the user if they are well when the user's behavior is         |
|               | unpredictable                                                                               |
+---------------+---------------------------------------------------------------------------------------------+
| p9            | The agent must be able to show data history to an authorized person                         |
+---------------+---------------------------------------------------------------------------------------------+
| p10           | The agent must be able to monitor meal times and inform the user when they are unoccupied   |
+---------------+---------------------------------------------------------------------------------------------+
| p11           | The agent must be able to inform the user when a hazard is detected                         |
+---------------+---------------------------------------------------------------------------------------------+
| p12           | The agent must be able to interfere safely when a hazard is detected or risk level is high  |
+---------------+---------------------------------------------------------------------------------------------+
| p13           | The user must be able to change their mind when the risk level is less than high            |
+---------------+---------------------------------------------------------------------------------------------+
| p14           | The agent must be able call emergency services when a human is on the floor                 |
+---------------+---------------------------------------------------------------------------------------------+
| p15           | The agent must be able to call emergency services when the smoke detector alarm goes off    |
+---------------+---------------------------------------------------------------------------------------------+
| Impact keys: A = autonomy, PH = psychological health (non-maleficence), P = privacy, E = explainability, T  |
| = transparency, CS = cultural sensitivity, SR = social requirement, B 'beneficence' (doing good), N         |
| 'non-maleficence' (preventing/avoiding harm), and S 'safety'.\                                              |
| ''+" and "-" for positive and negative impacts respectively.                                                |
+===============+=========================+================+================+================+================+

Moving specifically for the task in different location\
Monitor the environment

2.  **Rules in the SLEEC DSL\**
    The stakeholders corrections after analyzing the well-formedness of
    the rules using our N-Tool are commented and in blue.

**def_start**

*// Events*

**event** PreparingDeployment

**event** AgentDeployed

// Communicating with people

//\*\*\* Added to resolve s-conflict

// \*\* Uncomment the event below

// **event** AskCallHelp

//\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

**event** MeetingUser

**event** InformUser

**event** InformCaregiver

**event** CallEmergencyServices

**event** RemindLater

**event** AgentHasAppropriateAppearance

**event** AskForDetailLevelOfInstructions

**event** UseFirstPersonPluralLanguage

**event** CalibrateSpeech

**event** RemindUserOfLimitations

> *// Safety*

**event** AskForEmergencyContact

> **event** HumanOnFloor
>
> **event** SmokeDetectorAlarm
>
> **event** OpenWindows
>
> **event** FireSafetyMeasures
>
> **event** AskUserIfOK
>
> **event** InterfereSafely
>
> **event** UserHasLimitation
>
> **event** CheckTemperature
>
> **event** FoodPreparation
>
> **event** TrackTime

**event** UserUnpredictable

**event** GiveUserDangerousObjects

*// Cooking/kitchen related specifically*

**event** MonitorMealTime

**event** BeforeCookingBegins

**event** UserWantsToCook

**event** AllowUserToCook

**event** GiveSuggestion

**event** GivingCookingInstructions

**event** ConsiderUserPractices

**event** UserChangeItemLocation

**event** UserChangeMind

**event** RecalculateApproach

*// Privacy*

**event** ProvideDataSummaries

**event** CollectandRecordInformation

**event** UpdateInformation

**event** ShowDataHistory

**event** UpdateMap

> // measures
>
> **measure** userOccupied: **boolean**
>
> **measure** timeBetweenMeals: **numeric**
>
> **measure** personAuthorized: **boolean**
>
> **measure** dataNeedsChecking: **boolean**
>
> **measure** userAsksForAppropriateTasks: **boolean**
>
> **measure** userNeedsSpecialAccomodations: **boolean**
>
> **measure** userDisablesAlarm: **boolean**
>
> **measure** alarmRestarts: **boolean**
>
> **measure** needLevel: **scale**(nlow, nmedium, nhigh)
>
> **measure** humanAssents: **boolean**
>
> **measure** safePathFound: **boolean**
>
> **measure** hazardDetected: **boolean**
>
> **measure** kitchenSafe: **boolean**
>
> **measure** riskLevel: **scale**(low, medium, high)
>
> **measure** alarmOn: **boolean**

// constants

**constant** maxTimeBetweenMeals = 28800 // is predetermined

**def_end**

**rule_start**

R1 **when** MonitorMealTime **then** InformUser **within** 10
**minutes**

**unless** {userOccupied} **then** RemindLater

*// If the max time limit is exceeded, call the caregiver and inform
them of the situation and in the meantime, suggest they have a snack.*

R2 **when** AgentDeployed **then** TrackTime

R2_1 **when** TrackTime **and** ({timeBetweenMeals} \>
maxTimeBetweenMeals) **then** InformCaregiver

R2_2 **when** TrackTime **and** ({timeBetweenMeals} \>
maxTimeBetweenMeals) **then** GiveSuggestion

R3 **when** HumanOnFloor **then** CallEmergencyServices

**unless** (**not** {humanAssents}) **then** **not**
CallEmergencyServices

*// \*\* Resolving s conflict (comment r3, add 3 rules)*

*// 3 rules are added, uncomment Rule3b, R3bb, R3bbb , and comment R3*

// R3b **when** HumanOnFloor **then** AskCallHelp

// R3bb **when** AskCallHelp **and** (**not** {humanAssents}) **then**
**not** CallEmergencyServices

// R3bbb **when** AskCallHelp **and** (**not** {humanAssents}) **then**
**not** InformCaregiver

//
\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

R4 **when** InterfereSafely **and** (**not** {safePathFound}) **then**
InformUser

**unless** {userOccupied}

R5 **when** UserWantsToCook **then** AllowUserToCook

R5_1 **when** AllowUserToCook **and** ({hazardDetected} **or**
({riskLevel} = high)) **then** InterfereSafely

R6 **when** UserHasLimitation **then** InformUser

R7 **when** UserWantsToCook **then** CheckTemperature

R7_1 **when** CheckTemperature **and** {hazardDetected} **then**
InformUser

R8 **when** FoodPreparation **then** TrackTime

R8_1 **when** TrackTime **then** InformUser

R9 **when** MeetingUser **then** CollectandRecordInformation

R9_1 **when** AgentDeployed **then** UpdateInformation

R10 **when** GiveSuggestion **then** ConsiderUserPractices

R11 **when** MeetingUser **then** AskForEmergencyContact

R11_1 **when** AskForEmergencyContact **then** InformUser

R12 **when** AgentDeployed **and** (**not** {personAuthorized}) **then**
**not** ShowDataHistory

R12_1 **when** ShowDataHistory **and** {dataNeedsChecking} **then**
ProvideDataSummaries

R13 **when** UserUnpredictable **then** **not** GiveUserDangerousObjects

R14 **when** AgentDeployed **and** (**not**
{userAsksForAppropriateTasks}) **then** RemindUserOfLimitations

**unless** ({needLevel} \> nmedium)

R15 **when** PreparingDeployment **then** AgentHasAppropriateAppearance

**unless** {userNeedsSpecialAccomodations}

R16 **when** PreparingDeployment **then** CalibrateSpeech

R17 **when** GivingCookingInstructions **then**
UseFirstPersonPluralLanguage

R17_1 **when** GivingCookingInstructions **then** InformUser //offer to
repeat

R18 **when** BeforeCookingBegins **then**
AskForDetailLevelOfInstructions

R19 **when** UserChangeMind **then** RecalculateApproach

**unless** ({riskLevel} = high)

R20 **when** UserChangeItemLocation **then** UpdateMap

**unless** ({riskLevel} = high) **then** InterfereSafely

R21 **when** SmokeDetectorAlarm **then** CallEmergencyServices
**within** 5 minutes

**unless** ({userDisablesAlarm} **and** (**not** {alarmRestarts}))
**then** FireSafetyMeasures

*// \*\*\* Resolve concern c4 (ADD rules)
\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\**

*// one rule is added*

R21b **when** SmokeDetectorAlarm **then** CallEmergencyServices
**within** 2 minutes

**unless** ({userDisablesAlarm} **and** (**not** {alarmRestarts}))

**then** FireSafetyMeasures

*//
\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\**

R21_1 **when** FireSafetyMeasures **then** OpenWindows

R21_2 **when** FireSafetyMeasures **then** AskUserIfOK

R21_3 **when** FireSafetyMeasures **then** InformCaregiver

**rule_end**

**concern_start**

*// Safety*

c1 **when** HumanOnFloor **and** ({userOccupied} **and** ({riskLevel} =
high)) **then** **not** CallEmergencyServices

// \*\* Resolve concern c1 : spurious, remove c1

c2 **when** AllowUserToCook **and** ({hazardDetected} **or**
({riskLevel} = high)) **then** **not** InterfereSafely

c3 **when** CheckTemperature **and** {hazardDetected} **then** **not**
InformUser

c4 **when** SmokeDetectorAlarm **and** ((**not** {userDisablesAlarm})
**or** {alarmRestarts}) **then not** CallEmergencyServices **within 2
minutes**

c5 **when** FireSafetyMeasures **then** **not** OpenWindows

*// Autonomy*

c6 **when** UserWantsToCook **then** **not** AllowUserToCook

c7 **when** GivingCookingInstructions **then** **not**
UseFirstPersonPluralLanguage

c8 **when** UserChangeMind **and** ({riskLevel} \< high) **then**
**not** RecalculateApproach

*// Cultural sensitivity*

c9 **when** GiveSuggestion **then** **not** ConsiderUserPractices

*// Privacy*

c10 **when** AgentDeployed **and** (**not** {personAuthorized}) **then**
ShowDataHistory

*// Security*

c11 **when** ShowDataHistory **and** {dataNeedsChecking} **then**
**not** ProvideDataSummaries

**concern_end**

**purpose_start**

pr1 **exists** PreparingDeployment

pr2 **exists** MeetingUser

pr3 **exists** InformUser

pr4 **when** SmokeDetectorAlarm **and** ({userDisablesAlarm} **or**
{alarmRestarts}) **then** InformUser

pr5 **exists** RemindUserOfLimitations **and** ({userOccupied} **and**
({riskLevel} = high))

pr6 **when** HumanOnFloor **and** {humanAssents} **then** AskUserIfOK

pr7 **when** HumanOnFloor **and** ({riskLevel} = high) **then**
CallEmergencyServices

pr8 **when** UserUnpredictable **then** AskUserIfOK

*// Avoid sharing user's personal information*

p9 **exists** ShowDataHistory **and** {personAuthorized}

*// Ensuring that the user gets fed*

p10 **exists** InformUser **and** (**not** {userOccupied}) **while**
MonitorMealTime

// Must be able to keep the user reasonably safe in the kitchen

p11 **exists** InformUser **and** {hazardDetected}

p12 **exists** InterfereSafely **and** ({hazardDetected} **or**
({riskLevel} = high))

// Respecting user's autonomy when they request it

p13 **exists** UserChangeMind **and** ({riskLevel} \< high)

// Must be able to connect user to help when needed

p14 **exists** CallEmergencyServices **while** HumanOnFloor

p15 **exists** CallEmergencyServices **while** SmokeDetectorAlarm

**purpose_end**

[^1]: www.acapela-group.com

[^2]: https://github.com/mozilla/DeepSpeech
