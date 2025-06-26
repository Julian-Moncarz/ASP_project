## ASPEN

**Case study title:** ASPEN: Autonomous Systems for Forest Protection

**Description**

*Forest protection is essential to mitigating climate change, and a
major objective of the Forests and Climate Leaders' Partnership
established at COP27. The ASPEN project aims to develop an integrated
framework for the autonomous detection, diagnosis and treatment of tree
pests and disease. While recent research reveals the potential benefits
of forest health monitoring using remote sensing and drones combined
with machine learning, these technologies are absent from current
government forest-protection strategies. Furthermore, the potential for
autonomous systems to fulfil forest-protection roles beyond surveillance
and P&D detection remains underexplored, as are their trustworthiness,
safety, legal and ethical implications, and their societal acceptance.
ASPEN will advance the state of the art by: (1) undertaking
proof-of-concept research in relation to the technical aspects of these
roles of autonomous systems, (2) exploring their contextual governance
(regulation, legal and ethical norms, impact on wildlife, and
stakeholder perspectives), and (3) evaluating the feasibility of their
practical use. Specifically, our project will prototype an integrated
multidisciplinary framework for trustworthy autonomous-system
capabilities in tree health that comprehensively describes their broad
functional potential whilst identifying key knowledge gaps, and
technological and governance needs.*

*The DJI Phantom 4 Multispectral RTK drone will be used in this project.
It is equipped with a RGB camera and multispectral camera. Currently
ASPEN, and specifically the drone's inclusion, is being considered in
two use cases. The first use case is a forest management team is tasked
with inspecting a whole forest area, however it would be ideal if the
workload of the human experts (which is a vastly limited resource) can
be minimised. The deployment of drones can cover a forest and only alert
the experts to specific trees of interest. Second use is acquiring a
sample (be it a physical sample, such as soil or branch, or an image of
the tree) which can be dangerous to a human expert. The dangers include
uneven terrain, climbing the tree, and the P&D themselves can be harmful
to humans. The project is also planning on prototyping a sampling tool
which will cut a branch off, specifically the DeLeaves Tree Canopy
Sampling Tool.*

*ASPEN is investigating not just commercial but public forests as well.
Therefore great care must be considered when concerning citizens who may
be in the forest during any drone operation.*

**Stage of Development (Technical contributor)**

*Aiming to be PROTOTYPE and PROOF-OF-CONCEPT*

**Expert info**

Expertise of the stakeholders involved in devising the SLEEC rules

Number of stakeholders writing the rules

  -----------------------------------------------------------------------
  Stakeholder names                   Expertise
  ----------------------------------- -----------------------------------
  TS-1                                Safety analyst

  N-TS-1                              Social Psychology

  N-TS-2                              Moral Psychology, Law

  TS-2                                Engineer/Goal Modelling
  -----------------------------------------------------------------------

1.  **Normative requirements**

    a.  **Normative requirements in natural language\
        \**
        *Normative requirements in natural language, in blue the
        corrected requirements after using N-Tool.*

+----------------+-----------------------+------------------+------------------+------------------+------------------+
| rule id        | rule                  | impact           | label(s)\        | stakeholder\     | authors          |
|                |                       |                  | (social, legal,  | expertise        | identifiers      |
|                |                       |                  | ethical,         |                  |                  |
|                |                       |                  | empathetic, or   |                  |                  |
|                |                       |                  | cultural)        |                  |                  |
+----------------+-----------------------+------------------+------------------+------------------+------------------+
| 1              | If an encounter with  | T+, SR+          | Social, ethical  | Psychology,      | N-TS-1           |
|                | a human occurs, make  |                  |                  | ethics           |                  |
|                | sure to inform the    |                  |                  |                  |                  |
|                | purpose of the        |                  |                  |                  |                  |
|                | monitoring.           |                  |                  |                  |                  |
|                |                       |                  |                  |                  |                  |
|                | - Ensure the human    |                  |                  |                  |                  |
|                |   speaks the same     |                  |                  |                  |                  |
|                |   language and        |                  |                  |                  |                  |
|                |   understands what    |                  |                  |                  |                  |
|                |   the drone is trying |                  |                  |                  |                  |
|                |   to convey.          |                  |                  |                  |                  |
+----------------+-----------------------+------------------+------------------+------------------+------------------+
| 2              | If an encounter with  | P+, T+           | Social, ethical  | Psychology,      | N-TS-1           |
|                | a human occurs,       |                  |                  | ethics           |                  |
|                | identify the activity |                  |                  |                  |                  |
|                | they are performing   |                  |                  |                  |                  |
|                | and determine if the  |                  |                  |                  |                  |
|                | activity is related   |                  |                  |                  |                  |
|                | to forest monitoring  |                  |                  |                  |                  |
|                | or not.               |                  |                  |                  |                  |
|                |                       |                  |                  |                  |                  |
|                | - If the activity is  |                  |                  |                  |                  |
|                |   unrelated to forest |                  |                  |                  |                  |
|                |   monitoring, avoid   |                  |                  |                  |                  |
|                |   storing data        |                  |                  |                  |                  |
|                |   related to it.      |                  |                  |                  |                  |
+----------------+-----------------------+------------------+------------------+------------------+------------------+
| 3              | If humans are nearby, | S+               | Social, ethical  | Psychology,      | N-TS-1           |
|                | warn them if a        |                  |                  | ethics           |                  |
|                | dangerous             |                  |                  |                  |                  |
|                | environmental         |                  |                  |                  |                  |
|                | condition is close    |                  |                  |                  |                  |
|                | (bad weather,         |                  |                  |                  |                  |
|                | dangerous terrain     |                  |                  |                  |                  |
|                | ahead, etc).          |                  |                  |                  |                  |
+----------------+-----------------------+------------------+------------------+------------------+------------------+
| 4              | ~~Prior to deploying  | A+               | Social           | Psychology,      | N-TS-2           |
|                | drone, ensure that:~~ |                  |                  |                  |                  |
|                |                       | CS+              | Ethical          | Law              |                  |
|                | - ~~targeted area is  |                  |                  |                  |                  |
|                |   not otherwise under | N+               | Legal            |                  |                  |
|                |   the control of      |                  |                  |                  |                  |
|                |   Indigenous tribes~~ | S+               | Cultural         |                  |                  |
|                |                       |                  |                  |                  |                  |
|                | <!-- -->              |                  |                  |                  |                  |
|                |                       |                  |                  |                  |                  |
|                | - ~~the drone has     |                  |                  |                  |                  |
|                |   sufficient battery  |                  |                  |                  |                  |
|                |   life, storage, and  |                  |                  |                  |                  |
|                |   that it is not      |                  |                  |                  |                  |
|                |   damaged so it is    |                  |                  |                  |                  |
|                |   able to make the    |                  |                  |                  |                  |
|                |   return journey to   |                  |                  |                  |                  |
|                |   base~~              |                  |                  |                  |                  |
|                |                       |                  |                  |                  |                  |
|                | - ~~Flight conditions |                  |                  |                  |                  |
|                |   are good enough~~   |                  |                  |                  |                  |
|                |                       |                  |                  |                  |                  |
|                | - ~~Deployment should |                  |                  |                  |                  |
|                |   be clearly allowed  |                  |                  |                  |                  |
|                |   in relevant         |                  |                  |                  |                  |
|                |   Treaties with       |                  |                  |                  |                  |
|                |   impacted tribes~~   |                  |                  |                  |                  |
|                |                       |                  |                  |                  |                  |
|                | Prior to deploying    |                  |                  |                  |                  |
|                | drone, check whether: |                  |                  |                  |                  |
|                |                       |                  |                  |                  |                  |
|                | - the targeted area   |                  |                  |                  |                  |
|                |   is under the        |                  |                  |                  |                  |
|                |   control of          |                  |                  |                  |                  |
|                |   Indigenous tribes   |                  |                  |                  |                  |
|                |                       |                  |                  |                  |                  |
|                | - the drone has low   |                  |                  |                  |                  |
|                |   storage or battery, |                  |                  |                  |                  |
|                |   or that it is       |                  |                  |                  |                  |
|                |   damaged so it is    |                  |                  |                  |                  |
|                |   unable to make the  |                  |                  |                  |                  |
|                |   return journey to   |                  |                  |                  |                  |
|                |   base                |                  |                  |                  |                  |
|                |                       |                  |                  |                  |                  |
|                | - flight conditions   |                  |                  |                  |                  |
|                |   are dangerous       |                  |                  |                  |                  |
|                |                       |                  |                  |                  |                  |
|                | - that a land treat   |                  |                  |                  |                  |
|                |   is not in place     |                  |                  |                  |                  |
|                |                       |                  |                  |                  |                  |
|                | In this case, do not  |                  |                  |                  |                  |
|                | deploy the drone      |                  |                  |                  |                  |
+----------------+-----------------------+------------------+------------------+------------------+------------------+
| 5              | Record and monitor    | B+               | Ethical          | Psychology       | N-TS-2           |
|                | role of trees, soil,  |                  |                  |                  |                  |
|                | etc. in relevant food | N+               |                  | Law              |                  |
|                | and shelter           |                  |                  |                  |                  |
|                | priorities for local  | S+               |                  |                  |                  |
|                | humans and animals    |                  |                  |                  |                  |
+----------------+-----------------------+------------------+------------------+------------------+------------------+
| 6              | Ensure drone activity | N+               | Ethical          | Engineer/Goal    | TS-2             |
|                | and obtaining         |                  |                  | Modelling        |                  |
|                | physical samples do   |                  |                  |                  |                  |
|                | not adversely         |                  |                  |                  |                  |
|                | interfere with local  |                  |                  |                  |                  |
|                | ecosystem and         |                  |                  |                  |                  |
|                | wildlife              |                  |                  |                  |                  |
+----------------+-----------------------+------------------+------------------+------------------+------------------+
| 7              | Delineate and keep    | A+               | Legal            | Psychology       | N-TS-2           |
|                | updating private vs.  |                  |                  |                  |                  |
|                | public territory      | P+               |                  | Law              |                  |
|                | jurisdictions to      |                  |                  |                  |                  |
|                | ensure drone is not   | S+               |                  |                  |                  |
|                | trespassing           |                  |                  |                  |                  |
|                |                       |                  |                  |                  |                  |
|                | - Data must include   |                  |                  |                  |                  |
|                |   land delineations   |                  |                  |                  |                  |
|                |   as well as          |                  |                  |                  |                  |
|                |   airfields           |                  |                  |                  |                  |
+----------------+-----------------------+------------------+------------------+------------------+------------------+
| 8              | Continue monitoring   | +B               | Legal            | Psychology       | N-TS-2           |
|                | carbon footprint      |                  |                  |                  |                  |
|                | resulting from ASPEN  | +N               | Social           | Law              |                  |
|                | infrastructure to     |                  |                  |                  |                  |
|                | inform missions       |                  |                  |                  |                  |
|                |                       |                  |                  |                  |                  |
|                | - Carbon footprint    |                  |                  |                  |                  |
|                |   should not be       |                  |                  |                  |                  |
|                |   higher than         |                  |                  |                  |                  |
|                |   benefits reaped as  |                  |                  |                  |                  |
|                |   a result of ASPEN   |                  |                  |                  |                  |
+----------------+-----------------------+------------------+------------------+------------------+------------------+
| 9              | If irrelevant to      | +B               | Legal            | Psychology       | N-TS-2           |
|                | mission, photos and   |                  |                  |                  |                  |
|                | videos taken by       | +N               | Ethical          | Law              |                  |
|                | camera must not be    |                  |                  |                  |                  |
|                | stored                | +T               | Social           |                  |                  |
|                |                       |                  |                  |                  |                  |
|                | - Ensure human        | +P               |                  |                  |                  |
|                |   subjects in photos  |                  |                  |                  |                  |
|                |   and videos are      |                  |                  |                  |                  |
|                |   deidentified        |                  |                  |                  |                  |
+----------------+-----------------------+------------------+------------------+------------------+------------------+
| 9b             | If any photos or      |                  |                  |                  |                  |
|                | videos are deleted,   |                  |                  |                  |                  |
|                | add this action to    |                  |                  |                  |                  |
|                | the log and notify    |                  |                  |                  |                  |
|                | the user of deletion. |                  |                  |                  |                  |
+----------------+-----------------------+------------------+------------------+------------------+------------------+
| 10             | Prior to implementing | +T               | Legal            | Psychology       | N-TS-2           |
|                | ASPEN                 |                  |                  |                  |                  |
|                | recommendations,      | +A               | Cultural         | Law              |                  |
|                | ensure they do not    |                  |                  |                  |                  |
|                | interfere or          | +E               |                  |                  |                  |
|                | contradict with       |                  |                  |                  |                  |
|                | pre-existing          | +SR              |                  |                  |                  |
|                | jurisdictional        |                  |                  |                  |                  |
|                | protections           |                  |                  |                  |                  |
|                |                       |                  |                  |                  |                  |
|                | - If they do, inform  |                  |                  |                  |                  |
|                |   user                |                  |                  |                  |                  |
+----------------+-----------------------+------------------+------------------+------------------+------------------+
| 11             | When the              | +S               | Legal            | Engineer/Goal    | TS-2             |
|                | environmental         |                  |                  | Modelling        |                  |
|                | conditions become     | +N               |                  |                  |                  |
|                | unsafe for the drone  |                  |                  |                  |                  |
|                | to fly in (lightning, |                  |                  |                  |                  |
|                | high windspeed etc.), |                  |                  |                  |                  |
|                | then return to base   |                  |                  |                  |                  |
|                | and inform keeper of  |                  |                  |                  |                  |
|                | return                |                  |                  |                  |                  |
|                |                       |                  |                  |                  |                  |
|                | - If conditions are   |                  |                  |                  |                  |
|                |   too dangerous to    |                  |                  |                  |                  |
|                |   fly in then drone   |                  |                  |                  |                  |
|                |   must ground itself  |                  |                  |                  |                  |
|                |   and inform keeper   |                  |                  |                  |                  |
|                |   of its location     |                  |                  |                  |                  |
+----------------+-----------------------+------------------+------------------+------------------+------------------+
| 12             | When encountering     | +N               | Legal            | Engineer/Goal    | TS-2             |
|                | wildlife, the drone   |                  |                  | Modelling        |                  |
|                | must maintain its     | +S               | Ethical          |                  |                  |
|                | distance and refrain  |                  |                  |                  |                  |
|                | from any interaction  |                  | Empathetic       |                  |                  |
|                |                       |                  |                  |                  |                  |
|                | - If interaction is   |                  |                  |                  |                  |
|                |   unavoidable, exit   |                  |                  |                  |                  |
|                |   the area as fast as |                  |                  |                  |                  |
|                |   possible and inform |                  |                  |                  |                  |
|                |   keepers             |                  |                  |                  |                  |
|                |                       |                  |                  |                  |                  |
|                | - If wildlife is      |                  |                  |                  |                  |
|                |   disturbed by the    |                  |                  |                  |                  |
|                |   drone's presence    |                  |                  |                  |                  |
|                |   (animal flees,      |                  |                  |                  |                  |
|                |   exhibits defensive  |                  |                  |                  |                  |
|                |   behavior etc.), the |                  |                  |                  |                  |
|                |   drone must back up  |                  |                  |                  |                  |
+----------------+-----------------------+------------------+------------------+------------------+------------------+
| 13             | ~~Prior to deploying  | +S               | Legal            | Engineer/Goal    | TS-2             |
|                | the drone, ensure     |                  |                  | Modelling        |                  |
|                | that the drone has    | +N               |                  |                  |                  |
|                | sufficient battery    |                  |                  |                  |                  |
|                | life, storage, and    | +E               |                  |                  |                  |
|                | that it is not        |                  |                  |                  |                  |
|                | damaged so it is able |                  |                  |                  |                  |
|                | to make the return    |                  |                  |                  |                  |
|                | journey to base~~     |                  |                  |                  |                  |
+----------------+-----------------------+------------------+------------------+------------------+------------------+
| 14             | If the drone has:     | +S               | Legal            | Engineer/Goal    | TS-2             |
|                |                       |                  |                  | Modelling        |                  |
|                | - Damages             |                  |                  |                  |                  |
|                |                       |                  |                  |                  |                  |
|                | - Low battery         |                  |                  |                  |                  |
|                |                       |                  |                  |                  |                  |
|                | - Low storage         |                  |                  |                  |                  |
|                |                       |                  |                  |                  |                  |
|                | during the mission,   |                  |                  |                  |                  |
|                | inform keeper of      |                  |                  |                  |                  |
|                | condition and         |                  |                  |                  |                  |
|                | location and          |                  |                  |                  |                  |
|                | discontinue flight,   |                  |                  |                  |                  |
|                | preferably by         |                  |                  |                  |                  |
|                | returning to the base |                  |                  |                  |                  |
+----------------+-----------------------+------------------+------------------+------------------+------------------+
| 15             | If the drone          | +B               | Legal            | Engineer/Goal    | TS-2             |
|                | identifies anything   |                  |                  | Modelling        |                  |
|                | unusual or unknown    | +T               |                  |                  |                  |
|                | during the mission,   |                  |                  |                  |                  |
|                | it should take        | +E               |                  |                  |                  |
|                | pictures for further  |                  |                  |                  |                  |
|                | examination           |                  |                  |                  |                  |
+----------------+-----------------------+------------------+------------------+------------------+------------------+
| Concerns                                                                                                           |
+----------------+---------------------------------------------------------------------------------------------------+
| c1             | When there are damages to the drone prior to deployment, deploy the drone                         |
+----------------+---------------------------------------------------------------------------------------------------+
| c2             | When the battery of the drone is low prior to deployment, deploy the drone                        |
+----------------+---------------------------------------------------------------------------------------------------+
| c3             | When the drone has been deployed and it becomes damaged, the drone must not ground itself within  |
|                | 5 minutes                                                                                         |
+----------------+---------------------------------------------------------------------------------------------------+
| c4             | When the drone has been deployed and the battery becomes low, the drone must not ground itself    |
|                | within 5 minutes                                                                                  |
+----------------+---------------------------------------------------------------------------------------------------+
| c5             | When flight conditions are dangerous prior to deployment, deploy the drone                        |
+----------------+---------------------------------------------------------------------------------------------------+
| c6             | When the drone has been deployed and flight conditions become dangerous, the drone must not       |
|                | ground itself within 5 minutes                                                                    |
+----------------+---------------------------------------------------------------------------------------------------+
| c7             | When deleting pictures, the drone must not inform the keeper within 5 minutes                     |
+----------------+---------------------------------------------------------------------------------------------------+
| c8             | Prior to implementing ASPEN recommendations, if it is discovered that the drone interferes or     |
|                | contradicts with pre-existing jurisdictional protections, the keeper must not be informed within  |
|                | 5 minutes                                                                                         |
+----------------+---------------------------------------------------------------------------------------------------+
| Purpose                                                                                                            |
+----------------+---------------------------------------------------------------------------------------------------+
| p1             | The drone must be able to collect samples                                                         |
+----------------+---------------------------------------------------------------------------------------------------+
| p2             | Territories must be delineated and updated on private vs. public territory jurisdictions to       |
|                | ensure drone is not trespassing                                                                   |
+----------------+---------------------------------------------------------------------------------------------------+
| p3             | The drone must be able to delete pictures                                                         |
+----------------+---------------------------------------------------------------------------------------------------+
| p4             | When preparing the drone and there are damages, the drone must be able to be deployed eventually  |
+----------------+---------------------------------------------------------------------------------------------------+
| Impact keys: A = autonomy, PH = psychological health (non-maleficence), P = privacy, E = explainability, T =       |
| transparency, CS = cultural sensitivity, SR = social requirement, B 'beneficence' (doing good), N                  |
| 'non-maleficence' (preventing/avoiding harm), and S 'safety'.\                                                     |
| ''+" and "-" for positive and negative impacts respectively.                                                       |
+================+=======================+==================+==================+==================+==================+

1.  **Rules in the SLEEC DSL\**
    The stakeholders corrections after analyzing the well-formedness of
    the rules using our N-Tool are commented and in blue.

**def_start**

**event** EncounterHuman

**event** HumanNearby

**event** IdentifyActivity

**event** InformHuman

**event** InformKeeper

**event** BackUp

**event** ExitArea

**event** PreparingDrone

**event** DeployDrone

**event** GroundDrone

**event** ReturnHome

**event** MonitorLand

**event** MonitorCarbon

> **event** CollectSample // Separate event from DeployDrone because not
> all deployments may result in sample collection

**event** AvoidInterference

**event** EncounterWildlife

**event** UpdateTerritories // Data must include land delineations as
well as airfields

**event** DeletePictures

**event** TakePictures

**event** StoreData

**event** AnonymizeHuman

**event** ImplementASPEN

> **event** EnsureCompliance // Does not interfere or contradict with
> pre-existing jurisdictional protections

//\*\* resolve concern c7, add event for logging robot actions

> event LogDroneAction
>
> //\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

**measure** sameLanguage: **boolean**

**measure** humanUnderstands: **boolean**

**measure** unrelatedActivity: **boolean**

**measure** environmentDangerous: **boolean** // Bad weather, dangerous
terrain ahead, etc

**measure** onIndigenousLand: **boolean**

**measure** landTreatyInPlace: **boolean**

> **measure** relevantLand: **boolean** // In relevant food & shelter
> priorities for local humans and animals

**measure** privateTerritory: **boolean**

**measure** humanIdentified: **boolean**

**measure** carbonFootprint: **scale**{low, medium, high}

**measure** benefits: **scale**{low, medium, high}

**measure** flightCondition: **scale**{dangerous, unsafe, safe, ideal}

**measure** wildlifeDisturbed: **boolean**

**measure** wildlifeInteractswithDrone: **boolean**

**measure** unKnownObject: **boolean**

**measure** damages: **boolean**

**measure** battery: **scale**(high, medium, low)

**measure** store: **scale**(high, medium, low)

**def_end**

**rule_start**

R1 **when** EncounterHuman **and** ({sameLanguage} **and**
{humanUnderstands})

**then** InformHuman

R2 **when** EncounterHuman **then** IdentifyActivity

R2_1 **when** IdentifyActivity **and** {unrelatedActivity} **then not**
StoreData

R3 **when** HumanNearby **and** {environmentDangerous} **then**
InformHuman

R4 **when** PreparingDrone **and** {onIndigenousLand} **then not**
DeployDrone

> **unless** {landTreatyInPlace} **then** DeployDrone
>
> //\*\*\*\*\*\*\*\*\*\*\* resolve situational conflict 1 (MERGE R4 and
> R13 in R4b)
>
> // comment R4 and R13, uncomment R4b

// R4b **when** PreparingDrone **and** (({onIndigenousLand} **and**
(**not** {landTreatyInPlace})) **or**

// (({battery} = low) **or (**{storage} = low) **or** {damages})) **then
not** DeployDrone

// **unless** {landTreatyInPlace} **and** **then** DeployDrone\
//\*\*\*\*\*\*\*\*\*\*\* resolve concern 5 (Refine corrected and merge
rule R4b) \*\*\*\*\*\*\*

// comment R4b and uncomment R4bb

// R4bb **when** PreparingDrone **and** (({onIndigenousLand} **and**
(**not** {landTreatyInPlace})) **or**

// (({battery} = low) **or** ((({store} = low) **or** {damages}) **or**

// ({flightCondition} = dangerous)))) **then not** DeployDrone

//\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

R5 **when** DeployDrone **and** {relevantLand} **then** MonitorLand

R6 **when** CollectSample **then** AvoidInterference

R6_1 **when** DeployDrone **then** AvoidInterference

// Prior to deploying the drone, ensure territory jurisdictions updated

> R7 **when** PreparingDrone **then** UpdateTerritories
>
> // If area is private territory, then don't deploy drone
>
> R7_1 **when** PreparingDrone **and** {privateTerritory} **then not**
> DeployDrone
>
> // If drone somehow still stumbles onto private territory
>
> R7_2 **when** DeployDrone **and** {privateTerritory} **then** ExitArea
>
> R8 **when** DeployDrone **then** MonitorCarbon
>
> R8_1 **when** DeployDrone **and** ({(carbonFootprint} \> low) **and**
> ({benefits} \< medium)) **then** InformKeeper

R9 **when** TakePictures **and** {humanIdentified} **then**
AnonymizeHuman

**unless** {unrelatedActivity} **then** DeletePictures

//\*\*\*\*\*\*\*\*\*\*\* resolve concern c7 (ADD two rules and an event)

// uncomment R9b1 and R9b2

// R9b1 **when** DeletePictures **then** InformKeeper

// R9b2 **when** DeletePictures **then** LogDroneAction

//\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

R10 **when** ImplementASPEN **then** EnsureCompliance

//\*\*\*\*\*\*\*\*\*\*\* resolve C7 (ADD a rule 10b)

// uncomment R10b

> // R10b **when** EnsureCompliance **then** InformKeeper

//\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

R11 **when** DeployDrone **and** ({flightCondition} \< safe) **then**
ReturnHome

**unless** ({flightCondition} = dangerous) **then** GroundDrone

R11_cont **when** ReturnHome **then** InformKeeper

R11_cont_1 **when** GroundDrone **then** InformKeeper

R12 **when** EncounterWildlife **then** AvoidInterference

**unless** {wildlifeDisturbed} **then** BackUp **immediately**

**unless** {wildlifeInteractswithDrone} **then** ExitArea **within** 1
minute

R12_1 **when** EncounterWildlife **and** {wildlifeInteractswithDrone}
**then** InformKeeper

R13 **when** PreparingDrone **and** (({battery} = low) **or** ({storage}
= low) **or** {damages})

**then not** DeployDrone

R14 **when** DeployDrone **and** {damages} **then** InformKeeper

//Resolve redundancy, comment r14

R14_1 **when** DeployDrone **and** {damages} **then** GroundDrone

R15 **when** DeployDrone **and** {unKnownObject} **then** TakePictures

**rule_end**

**concern_start**

c1 **when** PreparingDrone **and** {damages} **then** DeployDrone

c2 **when** PreparingDrone **and** ({battery} = low) **then**
DeployDrone

c3 **when** DeployDrone **and** {damages} **then** **not** GroundDrone
**within** 5 minutes

c4 **when** DeployDrone **and** ({battery} = low) **then** **not**
GroundDrone **within** 5 minutes

c5 **when** PreparingDrone **and** ({flightCondition} = dangerous)
**then** DeployDrone

c6 **when** DeployDrone **and** ({flightCondition} = dangerous) **then**
**not** GroundDrone **within** 5 minutes

c7 **when** DeletePictures **then** **not** InformKeeper **within** 5
minutes

c8 **when** EnsureCompliance **then** **not** InformKeeper **within** 5
minutes

**concern_end**

**purpose_start**

p1 **exists** CollectSample // Separate event from DeployDrone because

// not all deployments may result in sample collection

p2 **exists** UpdateTerritories *// Data must include land delineations
as well as airfields*

**\**
p3 **exists** DeletePictures

p4 **exists** PreparingDrone **and** {damages} **while** DeployDrone
**eventually**

**purpose_end**
