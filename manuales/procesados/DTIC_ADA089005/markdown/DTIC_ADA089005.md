# DTIC ADA089005

*Documento procesado el 2026-05-18 18:28:20*

---

--- Página 1 ---

ENGINEERING

REPORT

MIS "MO

IS UBST QL1ALI1'! ?AtofW

TM OPY yUMiIIED TO DDC C()NTAPJ A

sI M-,I FICAIT NLiJJBR OF

PA M~ W* WM

WIN1tD=C LEGIBLY %

A DIVISION OF

PACIFIC CAR AND FOUNDRY COMPANY

1400 NORTH 4TH STREET, RENTON, WASHINGTON 98055

8091oOO9

--- Página 2 ---

DISCLAIMER NOTICE

THIS DOCUMENT IS BEST QUALITY

PRACTICABLE. THE COPY FURNISHED

TO DTIC CONTAINED A SIGNIFICANT

NUMBER OF PAGES WHICH DO NOT

REPRODUCE LEGIBLY.

--- Página 3 ---

AINAL REP

Integrated Artillery Recoil

Mechanism and Automated

Handling Design for

155mm Self-Propelled Howitz

ract N

AAKW79E-C~

D. over.

-ee

07801

Prepared for

~U.S. ARMY ARMAMENT RESEARCH AND

-' ,"

DEVELOPMENT COMMAND

Prepared by:

Approved by:

"L.Ainley, Project Engineer

R. Magnuson, Chief'Engineer

/ = .

/ l

....

PACIFIC CAR AND FOUNDRY COMPANY

RRenton,

Washington

I,'

-"(

<..I

--- Página 4 ---

CONTENTS

Section

Page

1.0

INTRODUCTION

2.0

AUTOLOADER

2.1

Rationale

2.2 Design

2.2.,

Autoloader

2.2.2

Stowage and Feeder

2.2.3

Primer Loader

2.2.4

Controls

2.3 Conclusions and Growth Potential

3.0

RECOIL SYSTEM

3.1

Rationale

3.2 Design

3.2.1

Recoil Cylinder

3.2.2

Counterrecoil Cylinder

3.2.3

Controls

3.3 Conclusiois and Growth Potential

4.0

RAM-0

4.1

Autoloaa ? R&M Model

I i

5 ,. ,-

o -

1.-

IDi

--- Página 5 ---

ILLUSTRATIONS

Figure

Page

.2-1

Autoload and Feed System

2-2

Autoloader Force and Time Calculations (3 Sheets)

2-3

Stowage Rack Model

2-4

Stowage Rack Model

2-5

Autoloader Panel

2-6

Standard Type Programmable Controller

3-1

Recoil System Digital Readout Panel

4-1

Autoloader/Recoil System, R&M Model Block Diagram

4-2

Rammer Assembly, R&M Model Block Diagram

4-3

Carriage Assembly, R&M Model Block Diagram

4-4

Ammo Stowage/Feed Assembly, R&M Model Block Diagram

4-5

Recoil Assembly, R&M Model Block Diagram

•j V

iii

--- Página 6 ---

APPENDIXES

A. Autoloader Calculations

A-1

81.

M109 Recoil Cylinders

131-1

2. Orifice Area Derivation

132-1

83. Vehicle Motion Resulting from Firing

133-1

?Large

Weapons

84. Stress Calculations

134-1

C. Engineering Drawings

C-1

D. Engineering Layouts

iJv

--- Página 7 ---

1.0 INTRODUCTION

The objectives of Contract

*were to design prototype auto-

loader and recoil systems for the 155mm howitzer mounted in the M109A2 vehicle.

These systems were to require the minimum changes possible to the existing

vehicle and were not to impair the 360-degree traverse and 0- to 75-degree

elevation capability of the weapon. Projectiles and powder charges would be

stored and fed automatically by either powered or manual operation of all

functions, with a burst rate of three rounds in 10 seconds and a sustained rate

of four rounds per minute. The howitzer would have a sliding breech and a fixed

or variable recoil length. The primers would be fed and ejected automatically

as well.

The system should be recoil operated with instantaneous selection cf

the various powder charges and projectiles from the gunner's station. The

ammunition stowage racks should hold more than 43 rounds and permit setting of

the fuzes in the stowed position.

LThe

recoil system should be of modular design with each module replaceable

without draining oil or gas. All cylinders should be designed for a maintenance-

free life of 10,000 rounds, Each pair should be identical, and the system should

function on one each of the recoil and counterrecoil cylinders. Both systems

should maintain simplicity and adequate reliability while operating over a

temperature range of -50iF to +160F.

The following is a report of the methodology and design of the aurcloader

and recoil system designed by Pacific Car and Foundry Company (PCF) to best

fulfill the above requirements in the most practical and reliable manner.

--- Página 8 ---

2.0 AUTOLOADER

2.1

RATIONALE

The original proposal concept provided a stowage rack mounted across the

rear of the vehicle with the projectiles and powder raised from the stowed

position and transported along their respective sides to a feeder which held

multiple rounds. The magazine type feeder on each side of the gun would move

up to the stowage rack to load and then down to the gun position to present

the projectile and powder to the rammer. During the initial evaluation of this

design, questions arose as to its ability to perform the necessary functions

within the firing cycle constraints.

Initially, the idea of a multi-round

magazine that would follow the weapon in elevation for the burst-fire rate

seemed to be the best method of reserving the maximum allowable time for load-

ing a projectile and powder charge. However, several compromises were necessary

with this system. A prefilled magazine of heavy projectiles and charges of one

type presented the necessity of removal by hand should the fire order be

changed or cancelled. The feed system required projectiles and charges to be

lifted from the stowage racks to cab roof level and then moved forward to the

magazines, which would lower them to the weapon elevation. Also, the system

required all projectiles to be stored on one side of the vehicle's longitudinal

center, creating a gross ImbalAnce. Depending on the amount of ammunition used,

this imbalance would change greatly as rounds were consumed, requiring a sophi-

stication of the vehicle's suspension system.

Certain design parameters become apparent during this initial study of

the autoloading system. To conserve energy and reduce time, it would be de-

sirable to move the projectiles and charges as short a distance as possible

--- Página 9 ---

while attempting to use gravity to the best advantage. A gravity feed system

was considered. However, a study of such a system indicated a reduced

reliability. A system which would advance one type of projectile and charge

at a time would eliminate the necessity to remove unused rounds. The stowage

racks should retain the projectiles and powder in a positive manner during

recoil and vehicle operation. Also, the system should stow the projectiles

as low and evenly across the vehicle as possible to maintain an even trim and

low center of gravity for the vehicle. At least five types of projectiles

and charges should be readily available. Also, a modular design of the stowage

racks would enhance reloading capabilities as well as provide greater reli-

ability.

The resulting design presented in this report reflects a departure from

the proposal for a more effective and reliable system, while meeting the ob-

jectives of the contract as well.

2.2 DESIGN

2.2.1 Autoloader

The autoloader design evolved from the combination of requirements and

trade-offs necessary to produce a system that would meet the required firing

rate and yet be operable by hand. The preliminary conceptual design assumed

that the firing rate could be met only by using a magazine type loader holding

two or three projectiles and powder charges and moving in elevation with the

weapon. During the initial design phase of this system, it became apparent

that although the system would meet the requirements, it would be desirable

to eliminate certain features if possible. The necessity to elevate the ammuni-

tion from the feed racks to the reload point for the magazines would pose a

--- Página 10 ---

7- 7

problem for manual operation. Also, the mechanism would be fairly complicated,

and a weapon stoppage for any reason would require removal of the ammunition

in the magazines by hand. Also, multiple handling of the ammunition reduces

the system's reliability. In addition to maintaining the proper vehicle trim,

the projectiles should be stored completely across the vehicle and as low as

possible. To accomplish this, it would have been necessary to reduce the types

of rounds carried and complicate the feed system considerably; therefore, concepts

for alternate methods were evaluated. A system that would advance one round

at a time would be desirable. However, to do this would require a system that

would follow the gun during full elevation and yet accept ammunition from a fixed

point.

In the design resulting from this study, a simple system of sliding arms

(see Figure 2-1, Item A) was devised so that during elevation of the weapon (see

Figure 2-1, Item B) about the trunnions, the support anchors (see Figure 2-1,

Item C) which are firmly attached to the gun, provide a fixed point for the

telescoping arms at all elevations. A fixed reference point at the vehicle is

provided by anchors (see Figure 2-1, Item D) attached to the turret. The geometry

is such that as the gun changes elevation, the fixed anchors at the gun and the

feeder lengthen or reduce the length of the arms (Item A) appropriately. These

arms provide a track for the feed carriage (see Figure 2-1, Item E) to travel

on. Since the carriage is firmly affixed to the tracks and due to the geometry

of the followers on the carriage, the carriage will always be level at the feeder

position and assume the angle of the gun when moved to the gun position. The

carriage is powered by a hydraulic motor (see Figure 2-1, Item F) which drives

a chain (designed to become rigid under compression) on each side of the carriage

(see Figure 2-1, Item G).

During retraction the chains will bend in one direction

--- Página 11 ---

SLIDING ARMS

®WEAPON

@ SUPPORT ANCHORS

@ FIXED ANCHORS

@FEED CARRIAGE

(fHYDRAULIC MOTOR

CHAI N

®RAMMER MODULE

RAMMER

MODULAR AMMUNITION RACK

@TRAYS

--- Página 12 ---

X~5'*"

Figure 2-1.. AutolWe end Food Sytm

* FACSC C"AM

FWOOY WANY

Pag

--- Página 13 ---

only, which allows them to turn around the sprocket and store in a small place.

Upon arrival of the carriage at the gun (shown level in Figure 2-1 for clarity),

the rammer module (see Figure 2-1, Item H) rises from its stowed position below

the recoil path of the gun. The rammer module is carried with the gun on a solid

structure (see Figure 2-1, Item C) to maintain its relationship with the bore

centerline. On its fin0l bit of travel, it picks up the carriage that the powder

and projectile have been transferred on and makes the final alignment with the

bore for ramming. The projectile is always carried on the centerline of the

weapon; therefore, the system is always moving the heaviest items the shortest

distance. The carriage moves downward when carrying a projectile and powder,

except when loading at gun tube angles of 0 to -10 degress of elevation. A

handcrank at the motor would allow rapid operation of the system in the manual

mode.

The rammer (see Figure 2-1, Item J) is of unique design to allow stowage

in the least possible space and ram the projectile and powder separately in the

SLi

least possible time.

The rammer is a "flick" rammer in that it accelerates the

projectile to above 10 ft/sec to provide proper seating force. After acceleration

of the projectile, the rammer leaves the base of the projectile 1 inch inside the

chamber,

The rammer is capable of velocities above 10 ft/sec if found necessary

during testing. Also, the alignment of the projectile and rammer to the center-

line of the weapon can be adjusted to eliminate balloting during the projectile

free travel.

After ramming the projectile, the rammer returns to the retracted

position, and the powder charge is moved over in line with the weapon and pushed

into the chamber. The rammer is throttled to leave the powder the required 1 inch

inside the breech surface. The rammer is retracted and lowered while the carriage

returns to the feed position to allow full recoil at any elevation. The breech

--- Página 14 ---

will close automatically, feeding a primer and arming the weapon, ready to fire.

The weapon is oriented so that thE breech block rises when opened and the rammer

assembly provides a tray to the rear of the chamber for the projectile and powder

charge to travel on during ramming. The rammer cylinder is controlled by means

of a valve to provide the speed necessary for projectile seating and reduced

force to place the powder in the proper position.

For manual operation or when using the Copperhead projectile, the weapon

should be loaded level or at a low angle to allow use of the hand rammer. However,

the hydraulic rammer could be used with manual control, if desired, by the addition

of an accumulator and hand pump.

A study to determine the feasibility of using the recoil stroke to charge

accumulators to self-power the system resulted in the conclusion that such a

system would reduce reliability and result in undesirable complexity. Past

experience in the recovery of recoil energy has proved unprofitable due to the

short time and stroke of recoil (approximately 20 miliseconds and 22 inches of

travel), If required, a system to recover energy could be developed in the future.

Although the autoloader is primarily designed to accommodate a sliding

breech and modular charge, the system could be modified to use the present

rotating breech, The addition of an extendable tray on the rammer assembly

to bridge the threaded portion of the chamber would accomplish this. Bagged

powder could be used with this system with the addition of a plastic disc to

. -

retain the bag in the chamber at elevation.

The autoloader as presently designed will accommodate the 155mm howitzer

mounted in the M109A2 vehicle with no major modifications needed for operation

up to 45 to 50 degrees of elevation. To achieve a full 75 degrees of elevation,

the weapon trunnions would need to be raised approximately 6 inches or the rammer

--- Página 15 ---

assembly modified to stow below and slightly to the side of weapon. This would

result in a slightly slower rate of fire. Computer time and energy studies of

the autoloader mechanism show the ability to achieve the 5 second burst rate

within reasonable velocities and energy levels. The computer studies (see

Figure 2-2) were conducted using 50 percent of the time to accelerate the

mechanisms and 50 percent for deceleration. Additional studies using 60 percent

acceleration and 40 percent deceleration and 70 percent acceleration and 30 per-

cent deceleration show that the accelerations and energy levels could be optimized

if necessary.

Stress and friction calculations and details of the autoloader are con-

tained in Appendix A.

The design of the autoloader uses fabricated and commercially available

parts, rather than castings, extrusions, and special parts, to facilitate the

building of a prototype prior to production engineering.

2.2.2 Stowage and Feeder

The stowage and feed system was presented a challenge in the need to provide

six different types of projectiles and powder charges, readily available and in

any order. The feed system must offer safe reliable stowage for the components,

yet provide ready access for changing fuses or charges, and for replenishment.

A unique system using a lead screw type device to advance the units in rows was

concepted (see Figure 2-1, Item K).

Each row would use two lead screws to capture

the units in the rack. These same lead screws would advance the units simply

by rotating one revolution. To reverse the feed, the drive to the lead screws is

reversed. The projectiles and charges would be advanced to an elevator incorp-

orating the same type of lead screws. The elevator would lower the projectile

--- Página 16 ---

C ..-.....

ACCELS., FORCOS, VTC., WITH RESPECT TO ALLOTTIEO

TIMES.

100b,

P41

FOR ORATIONS ARE-

(z,

1,1719.5908

15.Z157

0iiW~~M~~ TAI

MITKY GMC WITH 4Mi ,L0V*rjIOR

Jim,.

uI"MwO

INWH~u~S.S4IMIvTW

L&THN A AMU"I

M1,

CAAIMA41 R

(2,

M.WU

CYCLE (3)

ALL-Ps OwIt..

04.

n-4).-'-

JIM~g.

A04

$$1OO

25 10267

150.441

S CARRIAGE SWI PRTO

NGlo ALLOTTED ARE

* ~

SSLNM S A6I.O

0EL STS.? Yes (1), No 02).

)I as>

VGL. ("/S&C)

DIST. (IN)

CHAIN LOTH. (IN)

/1 FORCE (LB)

CHAIN LO. 0-11)

.34O5.5622

203.13

248.074

16.0002

3.60004

109489

203.13

224:569

. .:

t 0004

14.4002

22.0e1R

203.13

208.439

1 0

gur 22

00t03d Forc

nd Time92

4ultins2

See 14 of 3

600

680

3.1

4-5

I.1

-. U 9 - 9

O -5 7 21 32

6- ,54

--- Página 17 ---

.-.

ausys-j

It(O

"*ft

im FAG

U68 (USCINAL)

TENN~S.

*IT.

A/- PA#, 4l

.,.M

a.~T

MIS%

ow,

i.eo

.9.O

', j%

V..

t-~

~~~'t

A";M~

smoe

27.M89

31.0233

-128.218

-27

ACIL. PLATE I-a~

Figure 2-2. Autoloader Force and Time Calculations (Sheet 2 of 3)

--- Página 18 ---

fMt8NS ALLOTTED ARte-

iJiTg4AqL" PMPt9TLI

M!A9

kTS. 7F

MO (2).'t

t;,

ACM

.79"44

274

-97.712

l~f

4MW

-~W~vi~~~'T

*-j

'ss

.WL9*9

Onn

2~~

cbbflAAWi PRWflfl0S ALLOTTED

ARE- -

AM.. Clt.DIVS.? Y"

M), me Cr).

limp.

f041

33.7778

37.5397

-50.038

-56.25M

2563

-211.29

-23a.4#1

___

----

1.89-

__-21236_-

1801855.3956

53.9531

-211.2

-212.172

IT067.5556

6.:314

-2111829

-212.064

Figure 2-2. Autoloader Force and Time Calculations (Sheet 3 of 3)

--- Página 19 ---

I Land

powder charge to trays at the lowest level of the system. These trays are

in line with the feed carriage in the stowed position (see Figure 2-1, Item L).

A set of pushers moves the ammo components forward to the feed carriage upon

demand. The simplicity of this system is very desirable (see Appendix C, Draw-

ing C-1, Sheet 4). Also, the system is never required to lift the projectiles

and powder charges. They are rolled with a minimum of friction, horizontally

to the elevator, where they are lowered to the ready position. The drive motors

for the stowage racks are fitted with a handcrank receptacle for manual operation.

The elevator motor, which is also used as a brake, is fitted with a receptacle

for manual operation, as is the motor that advances the units to the feed carriage.

Hydraulic motors are used for compatibility with the turret drive system.

Energy and friction requirements are minimized by the use of plastic or nylon

coatings on the wearing surfaces of the system. Projectiles and powder charges

are firmly held in place at all times, and it is expected that advancement and

lowering of the units could be accomplished while the vehicle is in motion or

,during

recoil.

However, the system is designed to advance the next ready round

during the autoloader cycle.

The stowage and feed concept was so unusual that it was decided to fabri-

cate a half-size model to prove the theory prior to finializing the design

(see Figures 2-3 and 2-4). The model, although unrefined, shows the ability

to use the concept and is submitted as part of this report. The racks as designed

can be accommodated aboard the M109A2 with a minimum of modifications. It will

require a slightly higher bustle and the addition of a set of doors across the

back, The doors are designed to lower to a horizontal position to provide a

platform for individual loading of projectiles and powder charges. The doors

can also be dropped to a vertical position to provide access if a modular rack

I Z

--- Página 20 ---

Figure 2-3. Stowage Rack Model

--- Página 21 ---

Fir,'-re 2-4. Stowage Rack Model

--- Página 22 ---

is used. The present configuration will hold 30 complete ready rounds (6 rounds

of 5 types). Adaptability to the present M109 vehicle and modular design were

the prime considerations for this configuration. A modular rack is shown in

Figure 2-1 (K).

The elevator section remains with the vehicle as do the drives for

the stowage rack. The concept shows fork lift pockets to facilitate removal of

the entire rack except the drives. The racks and drives are simple and would

be fairly light. The racks would be filled at the depot area and transported

to the vehicle directly. Either a fork lift or boom crane could be used to

remove and replace the racks. Excess room was left at the bottom of thuze

racks for a test situation; however, 35 ready rounds could be carried by utili-

zation of this area with very little additional modification. Stress calculations

and specific details are contained in Appendix A. The system is designed to

be fabricated from available material welded, etc., as a prototype.

Production

design would include the use of castings, extrusions, etc.

2.2.3 Primer Loader

The automatic primer feed system for the 155mm autoloader performs basically

LIthe

same function as a small arms automatic weapon. However, the shape of the

M82 or M119 primer does not lend itself well to autoloadlng as the sharp square

11 ifront

and the rim at the base create difficulties not normally encountered with

regular cartridges. Also, the necessity for the primer loader to operate in

conjunction with the breech presents a unique cycling problem. The sliding breech

was selected as the prime candidate for the autoloader system. Therefore, the

-"primary

emphasis of the design is the use of this type of breech. Although

either of the concepts could work with the rotating breech, a rotating bolt type

mechanism would probably be used.

H:1

--- Página 23 ---

....

gal.--

------.-

I I

''1

.Standard

automatic weapon actions generally extract and feed by recoil or

gas pressure. It was not deemed desirable to extract the primer while pressure

remained in the bore. Also, a primer should not be fed into the firing position

until just before firing the cannon. The system also should be activated by

the motion of the breech rather than be externally powered.

To meet the above criteria, it appeared that a straight line locking

arrangement would be in order to simplify the system and take advantage of the

sliding breech motion. The initial design used a basic rotating bolt type lock.

However, this was activated by a straight forward and aft motion of the bolt

carrier (see Appendix D, Layouts D-1 and D-2). This system had the disadvantage

of length, complexity, and probably the necessity to round the forward end of the

primer to permit smooth feeding into the chamber.

The concept chosen (see Appendix C, Drawing C-2) is a simple mechanism

activated by a cam surface on the breech, which provides a straight rearward

pull on the bolt lever. As the bolt carrier moves to the rear, the firing pin

is retracted, releasing the locking lugs. The bolt comes forward, driven by a

cam on the breech, as the breech closes. This feeds a primer from the basic

10-round clip or optional 30- to 60-round drum (see Appendix D, Layout D-3).

The primer is positively guided into the chamber and is engaged by the extractor.

When fired, the bolt is driven forward by a spring developing approximately

60 pounds force. The firing pin reacts directly on the locking lugs. The

forward motion of the firing pin moves the locking lugs out into position and

fires the primer. If the bolt is not locked or the lugs are unable to lock for

any reason, the primer cannot be fired. During the breech opening, the bolt

carrier moves to the rear with the firing pin. The locking lugs are released

and the spent primer extracted and ejected. The firing pin locks in the rear,

--- Página 24 ---

or cocked, position. The entire assembly is mounted in an interrupted thread

housing which allows easy, fast removal from the weapon for service or replace-

ment. The primer may be fired using the integral solenoid or manually with a

lanyard.

(See Appendix C, Drawing C-2 and Appendix D, Layout D-3.)

All components of the primer feeder are rugged, minimum tolerance parts

for reliability and ease of maintenance.

2.2.4 Controls

The autoloader controls (see Figure 2-5) present a go/no-go display for

the gunner and/or assistant gunner. Standard solid state circuitry techniques

will be used (see Figure 2-6). The controls are capable of fully automated

operation when interfaced with a fire control computer system or they can

operate in an autonomous fashion. Three modes of operation are available.

The manual mode requires the gunner to address each function and activate it

as well.

The auto mode requires the gunner to select rate, projectile, charge,

and number of rounds only. All other functions except the fire initiate are

done automatically. In the computer mode, the system is interfaced with the

fire control system and reacts to the fire order sent from the FDC. The gunner

Coo r,ads by excetin, and can hold or abort the mission from his controls. In

Ethe

use of the computer controlled system, the FDC could have a similar control

panel or a reduced function panel to monitor the system functions and maintain

ultimate control of each weapon system. Should a problem occur during operation

of the system, it will show a red light and stop at that function until corrective

action is taken. Each operation is fail safe and must be in a "go" mode for

the system to advance to the next position. During the automatic operation,

the go/no-go signal will appear as the function is performed. The fire order

--- Página 25 ---

(Not to Scale)

FUNCTION

Fail

Ready

MODE

RATE

I IGEISUSTAINED

NUMBERm

mmm

ROUNDSJ LEJL]LLIJ iYYI

r--

PROJECTILE

REMAINING

CHARGE(3G

FEEDER

SELECTED PROJECTILE AND

CHARGE IN POSITION

FEEDER

ESSTE FALSGASEURS HC

FRCI AELECE PROJETILEAND

LOADER

PROJECTILE AND CHARGE

AC VT

ITIOG

PROJECTILE AND CHARGE

IIRAMMED-NO

FALLBACK

BREECHVQ

PRIMER

RECOIL SYSTEM -FAIL SIGNAL REQUIRES CHECK OF RECOIL PANEL

FRE ORDER

FIRE ORDER

COORDINATE I

GUN POSITION4

GUN POSITION

AZIMUTH

ELEVATION

COVERED

TUBE TEMI'

TIME

FIRE

3R)

Figure 2-5. Autoloader Panel

--- Página 26 ---

Figure 2-6. Standard Type Programmable Controller

--- Página 27 ---

coordinates are displayed in the upper panels, and the system will not advance

to the fire mode until these numbers are matched either manually or by the gun

system. The go/no-go light for the recoil system will indicate if a problem

exists, thereby, notifying the gunner to check the recoil system panel for the

specific problem. The panel could incorporate fallback indication as well as

tube temperature and the amount of time the breech has been closed or the safe

time to cook-off. The hold button will simply hold the system ready and require

the gunner to lift the cover and press the fire button. The abort switch will

open the breech and extract the primer. The ammunition select buttons will

also serve as an indicator for the number of each type of projectile and charge

remaining in the stowage racks. As the gunner selects the type and number of

projectiles and powder, the switches will light up, e.g., if he should press

the number 4 to indicate 4 rounds, and then selects HE for the projectile, the

number 2 indicator would begin flashing if he only had 2 HE rounds left in the

rack. The same would hold true for the charge as well.

An added feature would

be a digital.counter to indicate the number of units remaining for each. To

ensure the proper projectile and powder charge will be fed to the weapon, sensors

for weight of charge and type of projectile are incorporated on the feed trays.

The system will hold and indicate the type of units in the feed trays by flashing

the appropriate select buttons.

The use of a simple micro-processor with a memory will allow the unit to

be used for other uses such as hatch and spade positions, engine functions,

vareious liquid levels, etc., if desired. If a fire control system is used, the

fire control computer could be interfaced with the control sensors, thus,

eliminating the need for a separate micro-processor.

--- Página 28 ---

2.3 CONCLUSIONS AND GROWTH POTENTIAL

The complete autoloader system offers a growth potential for the 155mm

weapon mounted in the M109 vehicle and all other cannons usirng one- or two-part

ammunition desiring the ability to load and fire at all degrees of elevation

or while stabilized or moving.

The basic design, as reported here, is the result of a study in a limited

time with specific requirements for interface with the existing weapon system.

An improved version of the system, as desired for the M109, would include

development of some of the following areas.

Additional racks of ammunition can be carried in the area forward of the

existing racks using a mechanism to move the ammunition rearward to be accepted

by the existing carriage. Either of these systems would provide up to 50 or

60 ready rounds in the existing vehicle. The vehicle would still maintain

enough space to carry an adequate supply of Copperhead and special purpose

rounds.

A study to determine the feasibility of an underslung carriage to accept

the projectiles and powder charges directly from the elevator would provide

a simple solution for the addition of another rack of ammunition forward of

the existing racks.

The compact nature of the autoloader and storage racks will permit isola-

tion of the gunner and assistant gunner by providing an enclosure that will

turn with the turret, with doors into the gun compartment as well as hatches

in the turret roof. This arrangement would provide smoke, heat, noise, and

CBR protection for both crewmen. The system should be capable of manual opera-

tion and maintenance by the gunner and/or assistant gunner, eliminating the

need for additional crewmen. Should sustained firing be required, additional

crewmen would be assigned. The autoloader system as designed could provide

l21

--- Página 29 ---

total autonomous operation of the M109 when interfaced with a fire control

system.

The telescoping arms of the autoloader could possibly be replaced by a

strong back chain, over which the carriage could travel.

This would eliminate

some complexity of the system.

A compromise of the turrets ability to traverse through approximately

120 degrees rather than 360 degrees could provide a lower profile with increased

stowage of ammunition because the bustle would extend much lower and turn with

the turret.

The anticipated 5 seconds between rounds might be further optimized,

depending on the weapon configuration and recoil system.

--- Página 30 ---

3.0 RECOIL SYSTEM

3.1

RATIONALE

The basic goal of this effort was to design a recoil system that could

be retrofitted to the Ml09 and that would provide a significant improvement

in reliability and maintainability over the existing system. This was a-

chieved. The integral buffers and replenishers which eliminate all hydraulic

plumbing will provide this significant improvement.

A secondary goal to provide safe operation if one cylinder of either

pair of recoil or counterrecoil cylinders becomes inoperative was not achieved.

This is due to the following two reasons.

First, to permit a reasonable retrofit, onty one counterrecoil cylinder

can be utilized. The location where a seccnd cylinder could be installed is

occupied by the direct fire telescope. There seems to be no practical way

to relocate this telescope in a retrofit program.

Second, the impulse of the rounds expected to be fired from the new

gun is so great that it became impractical to consider permitting firing

with only tne recoil cylinder operating.

Modification of the gun mount structure required to accept the new

recoil system consists basically of cutting off and boring out tne existing

welded-in recoil cylinders.

The new gun mount assembly will be very

"clean". The buffer cylinder, replenisher cylinder, and all hydraulic

tubing and fittings will be gone.

A constant length recoil system was selected because analysis showed

that recoil length had little effect on vehicle motion resulting from

firing.

(See Appendix B3.)

Vehicle motion is primarily a function of the

magnitude of the impulse of the round fired. It is effected only slightly by

--- Página 31 ---

changes in trunnion reaction, unless the recoil length can be made long enough

so that static equilibrium is approached. Such a long recoil travel is not

practical in the M109.

Although the new gun and ammunition have not been finalized, the

following weapon characteristics were furnished by ARRADCOM for design

purposes:

Projectile weight ..........

98 lb

Projectile velocity. . .

3,250 ft/sec

Propellant weight. .

. ...

40 lb

Recoiling weight ........

9,600 lb

3.2 DESIGN

(see Appendix B1 and Appendix C, Drawings C-3, Sheets 1 and 2)

3.2.1

Recoil Cylinder

The following is a discussion of the major features of the recoil

cylinder.

3.2.1.1

Rod Seal

The rod seal is a unique feature of the recoil cylinder design. The

seal is not subjected to the high pressure (over 6,000 psi) during recoil.

The high pressure is reduced to almost zero by the labyrinth groves and is

then bled off to the low pressure end of the cylinder. The rod seal will

be subjected to only the pressure required to move the oil that leaks through

the labyrinth grooves to the front end of the cylinder. During recoil, the

front end of the cylinder is actually under a vacuum caused by the displace-

ment of the piston rod.

--- Página 32 ---

3.2.1.2 Buffer

The buffer i; i.

1-3/4 inch diameter, 6-inch-long spear which plugs

into a cavity in the piston rod. The spear has three parabolic shaped

orifice grooves designed to bring the weapon to a stop with a constant

force acting over a 6-inch travel.

The buffer is absolutely foolproof

since it has no moving parts. Also, during counterrecoil, oil is forced

from the front end of the cylinder to the rear end, transferring the vacuum

from front to rear, thereby, assuring the buffer cavity is full of oil.

3.2.1.3 Orifice Sleeve

For a fixed-length recoil system, the orifice sleeve has a number of

advantages over a control rod. The piston, piston rod, and buffer are

much simpler. In addition, the sleeve provides a means of piping the bleed

oil from the labyrinth seal in the rod gland to the other end of the cy-

linder without external plumbing.

3.2.1.4 Replenisher

Both recoil cylinders are equipped with an integral replensiher. The

replenishers have a nitrogen spring and are at sufficient capacity to ac-

commodate all operational temperatures and provide a maintenance-free life

of over 10,000 rounds.

Electronic sensors are installed in the replenisher to indicate the

status of the oil volume, which is displayed as estimated rounds before

maintenance on a display panel.

3.2.2 Counterrecoil Cylinder

The existing M109 counterrecoil cylinder is completely self-contained,

'25

--- Página 33 ---

and this basic design has been retained. However, two major modifications

have been made to the cylinder:

s The cylinder has been shortened by approximately 16 inches to

take advantage of the fixed 21-inch recoil travel.

Electronic sensors have been included to provide a readout on

a display panel of the conditions of the rod seal and piston

seal.

3.2.3 Controls

The Recoil System digital readout panel (see Figure 3-1) can be mounted

either at the gunner's station or at both the gunner's and assistant qunner's

station. Each unit indicates the condition of the recoil system by a per-.

centage readout. If any function reaches its lower limit, an X will begin

flashing in the numeral 1 position of that indicator. Simultaneously, the

fire inhibit circuit will be activated, interrupting the trigger switch,

Therefore, to fire the weapon, the gunner will be required to engage the

override switch on the panel, thus, acknowledging a lower limit condition

within the system. The orange displays can be quickly and easily read in

direct sunlight and at a distance of 20 feet. This will aflow the displays

to be monitored while recharging.

3.3 CONCLUSIONS AND GROWTH POTENTIAL

The recoil syst, m discussed here is a significant improvement for the

M109A2 because it is a simple design that will provide improved performance,

it is designed for RAM-D improvement, and it enhances performance of the

autoloadr. As explained earlier, the recommended approach has traded-off

the redundancy possible with a four-cylinder system in order to make

.----

--- Página 34 ---

RECOIL SYSTEM DIGITAL READOUT PANEL

(SCALE: FULL SIZE)

BECKMAN SP330 DISPLAYS

RECOIL FUNCTIONS

LOWER RECOIL

UPPER RECOIL

COUNTER RECOIL

COLNTER RECOIL FUNCTIONS

PRESSURE %

PRESSURE %

PRESSURE %

REPLENISHER PRESSURE

CYLINDER PRESSURE

PSI

I 0 0 0

LOW LIMIT 10

LOW LIMIT 10

LOW LIMIT 1500

PISTON OIL%

PISTON OIL%

PISTON OIL%

REPLENISHER OIL VOLUME

PISTON OIL VOLUME

100 /10

/170

LOW LIMIT 5

LOW LIMIT 5

LOW LIMIT 5

FIRING SWITCH

TEST

ROU OIL %

FIRE INHIBIT SWITCH

ROD OIL VOLUME

WITH COMBAT OVERRIDE

ALL UNITS

INHIBIT

100%

LOW LIMIT 5

TEST SWITCH

MOMENTARY ON, ALL

INDICATORS READ 100%

Figure 3-1. Recoil System Digital Readout Panel

(Scale: Full Size)

--- Página 35 ---

possible a low-cost adaptation to the MlO9A2.

future design of an all-new guu znd turret combination can use paired

41 )recoil

and counterrecoil cylinders. The potential safety and life advan-

tages of such a system would then have to be traded-off against the extra

weight and cost.

i [1

--- Página 36 ---

4.0

RAM-D

4.1

AUTOLOADER R&M MODEL

This report presents a preliminary assessment of reliability and main-

tainahility characteristics of an automatic feed, load, and recoil system

concept for a 155mm self-propelled howitzer. The data presented are con-

sidered to represent typical values for generic components in a severe

environment. While the assessed values for individual components likely

possess a large degree of inherent error, both high and low, some errors

should cancel, and the result indicates a ballpark figure for the toal

assembly. In this regard, the analysis should not be considered as con-

clusive, but rather as a point of departure to stimulate thinking, arouse

concerns, and guide follow-on efforts.

The three values presented on the block diagrams are defined below:

e F Failures/10 6 rounds

Where failure results in complete loss of autoload capability.

No allowance is made for the capability to revert to manual

loading.

a Xm = Maintenance actions/10 6 rounds

Where maintenance action is considered as any repair necessary

to retain full capability. This includes replacement of

failed components, adjustments, and preventive repair (tighten

bolts, replace seats, etc.)

.T= Average corrective mainten i, ce time in hours for maintenance

- ,

actions. This includes only action immediate to the autoloader/

recoil assembly and assumes repair parts are readily available.

--- Página 37 ---

h10

MRBF = Mean Rounds Between Failure

MRBMA = Mean Rounds Between

Maintenance Action

Any discrepancy in terminology between this portion of the report and

other sections, the other sections will prevail.

The R&M Model and related data are depicted in Figures 4-1 through 4-5.

Figure 4-1 shows the top diagram with its major subassemblies while Figures 4-2

through 4-5 show the details of the major assemblies

--- Página 38 ---

~~~~ *

* -

_ _ _ _ _

u Itn

0fw

<co

Ccw

U..

til

.U.W L

LL.

--- Página 39 ---

U.1

-. .

LAcn w

C.)~

I-xXx

I"cc

L32

NvizV I

--- Página 40 ---

-R~

If11x.

InI

Lc).

0: M

Cizj mI

ui in

; 433

--- Página 41 ---

0w~

1R11L

1 1i

1.J

(0 N

c<c

U 2 U

-XL

U.-

--- Página 42 ---

coo

o uf

U)l

W)M()(

W C

0~~~

.<RL

U)~

N U35

--- Página 43 ---

APPENDIX A

Autoloader Calculations

--- Página 44 ---

PACIFIC CAR AND FOUNDRY COMPANY

-~ENGINEERING

DEPARTMENT

NAME

REFERENCE

DATE

____

PAGE

27.

VLpT ,

TuLRk

1/ 6

T?2

Th u l ) 'SVP~l?)7 F

MOV~i vct-H T06

Goo4. 7%& AFT

7fr Ck $Q0Pi06)-,-

I--

PCF-RN- 1284A-

--- Página 45 ---

PACIFIC CAR AND FOUNDRY COMPANY

ENGINEERING DEPARTMENT

NAME

111.REFERENCE

PIK___________

DATE

/0297

PAGE____

OF____

,'. ~~~Sa

o,,-,

(aR)

, O2 ..o

2.5

2.0

I I

.... ...

__._

___)__-5

t-P.o

-"-o-T(2)

+ -,

.,(

.1..

fer-

- uz Told: (-e.)

PCF-RN-1284

A-2

(?6G

--- Página 46 ---

PACIFIC CAR AND FOUNDRY COMPANY

SNAME

ENGINEERING DEPARTMENT-

NAME

REFERENCE AL7

DATE

& 2 .' g--79

PAGE

' -

,5:.

C-,,

l.J

T 4x

- -(4

-1.25

52(--- ..

7 L

Oo TI F4,0. T"gm :~

13 i,, 3.8" iv,

?J Oo -r-

p,Ik-- 1.

346.57T

,.~

1--

44t_

m50

PCF-RM-1284

A-3

--- Página 47 ---

PACIFIC CAR AND FOUNDRY COMPANY

lit)

ENGINEERING DEPARTMENT

NAME

REFERENCE

_____

DATE

AEOF

-7-

...

7/-

A-4

vKJ,

----

, .-

P or: U-

A)~k~~

PCF-RN- 1284

.....

--- Página 48 ---

Z I

flPACIFIC

CAR AND FOUNDRY COMPANY

ENGINEERING DEPARTMENTA

-NAME

_______________REFERENCE

____________

DATE

-2PAGE

_____

fP't

IRC

)6F

A-5

_____

_____

--- Página 49 ---

PACIFIC CAR AND FOUNDRY COMPANY

NAMEENGINEERING

DEPARTMENT

t L~ x

NAT1E 3

REFERENCE

_____________

DATE

/1-1-79

PAGE

OF___

LA- lauee T?ACK) 4F7 c$Of-'LI Y'

14'

I I

-45

PCF-RN- 1284

A-6

J7T7"

--- Página 50 ---

PACIFIC CAR AND FOUNDRY COMPANY

/<I6

ENGINEERING DEPARTMENT

,7 C(

NAME

A_____________

REFERENCE-A

L1-.

DATE

0-3

-79

PAGE7

OF_

7~+L OTUI9 -7-(

cK)II

/4i11

2,o3

1- .

AAm

PCF-RN-124

A-7

--- Página 51 ---

PACIFIC CAR AND FOUNDRY COMPANY

ENGINEERING DEPARTMENT

NAME

_______________

REFERENCE______________

DATE

11h-9

PAGE

/0,

~cm

IIe&.s

-128

6255

PC"R

__-8

--- Página 52 ---

PACIFIC CAR AND FOUNDRY COMPANY

ENGINEERING DEPARTMENT

NAME _________________REFERENCE

______________

DATE,

11-2- 79

PAGE

/ V

liPCF-RN-

1284

' I - i i-i

--- Página 53 ---

PACIFIC CAR AND FOUNDRY COMPANY

ENGINEERING DEPARTMENT

NAME-

I ,3a ~c

REFERENCE

___________

DATE

It---

-7a

PAGE

1.25

CBLjiV/-'OIE

0 "

0-6[/A.

D/A.-

OA91____

-TypNoLE

tlz

PCINTs

AI1

--- Página 54 ---

NAME

PACIFIC CAR AND FOUNDRY COMPANYA-

ENGINEERING DEPARTMENT

DATE

___________PAGE

OF_____

7TIV5 5Y$TeMAA'o7o

jA ILL

AJe'

OA27) FQ

erc~

'57A -:5 T/#4TA

7C4'( t4~&(~

A4FT 7T#5

___

______

_____

50jIpa AtvH

PCF-RN- 1284

A-11

--- Página 55 ---

PACIFIC CAR AND FOUNDRY COMPANY

NAME

ENGINEERING DEPARTMENT

NAME

...

_REFERENCE

DATE

__PAGE

_2._

o, //-

v9,

MOT0o,

} "

<~--L2-o

r-.,4L

r2hU.

GoVP SEC'

PC-N18

A-12

J "

)i'e

S5thAFT

"PCF-RN-1284

A-12

--- Página 56 ---

PACIFIC CAR AND FOUNDRY COMPANY

ENGINEERING DEPARTMENT

NAME

_---___

REFERENCE _-

DATE_______________A

2.35"375.

,ThLL

SWET5

,2{'X

(3L7-7E713

li¢

-N-

A-13

<,5,

--- Página 57 ---

PACIFIC CAR AND FOUNDRY COMPANY

NAME

_ .

ENGINEERING DEPARTMENT

NAME

13u

f-REFERENCE

DATE

1---79

PAGE

44o

DATEAT

Ik&4,1

r e

No----

PC-R-18

4,7

fh;II

IsA i

_'u-

"TP.

pCF-RN-1284

A-14

--- Página 58 ---

PACIFIC CAR AND FOUNDRY COMPANY

NAME

ENGINEERING DEPARTMENT

NAME

.REFERENCE

DATE

P-23--3

PAGE

OF_

FI'ures FF'O {

37O-GAff5((

Cciu'P.uTa/,J.

F?&"x,:,,t /4I? "'

7 1 o__C.AW__o .6...c_.e.

, -. t2.,

(('0.°-_)f..

AP-IcaA

-77,U

i- (.

-F&,cP U,

50,K4, 0

'32 7/V.

C,49-<7v

To Q

oeC)C

) I

2-I

Tt -hYD, /Aolb k T7qUE

2 3o9 i19.i

_oo 5.._

RPM

-30-0

(-RiS.)

PCF-RN-1284

A-15

--- Página 59 ---

PACIFIC CAR AND FOUNDRY COMPANY

ENGINEERING DEPARTMENT

NAME

,__

REFERENCE

DATE

/I-_

-_ __

_I_

(AN

..h&T

71-

Ile,

*1 i

PCF-RN-1284

A-16

lo no

, III

m6-

--- Página 60 ---

PACIFIC CAR AND FOUNDRY COMPANY

NAME_______

ENGINEERING DEPARTMENT

A-LC

DATE

/-/379

PAGE

Comeioo

-o~

I ,

i"PCFRN-1284

A-17

, : ....g: 1 %t;=-

C , 'v*

G W IC

7 -

........

. ......

--- Página 61 ---

PACIFIC CAR AND FOUNDRY COMPANY

V~2..

ENGINEERING DEPARTMENT

NAME __REFERENCE

DATE__

PAGE

o,,,-o~~CO-o

!t.5-7

!, o

,57,,

Th2/c c57?271,C/J2- Cc.MF& 2C--(.

PCF-RN-1284

A -18

.. . "

" -'..

. .

-mCImmf

I==

--- Página 62 ---

PACIFIC CAR AND FOUNDRY COMPANY

NAEENGINEERING

DEPARTMENTo^

NAME

REFERENCE

_._

2ATE

PAGE

~G &

'IS

-i-,

7,"

~),

09 *)6f

PCFRNJ2S

194

--- Página 63 ---

PACIFIC CAR AND FOUNDRY COMPANY

ENGINEERING DEPARTMENT

__E

REFERENCE

DATE

PE/-

2-7

PAE___

OF___

Lo5 " M-'), C-'

v-'

4-- 2-

-_---,

__2

'44)

"S&l}5""56 I C3

0"? <

4'i'

= I{3D12.

72L, q 4"L I ?z'

....

I_.---

P CF-R N-127.

--- Página 64 ---

PACIFIC CAR AND FOUNDRY COMPANY

ENGINEERING DEPARTMENT

NAME

REFERENCE t,

,, f ,4 "

DATE

~PAGE

__OF

....

Q , > ';L

ij~

$1PFRN18

A -21

%-IVo(22~

1,7 ' "4 "

/,'

.--

(I,'

3 ,

, -

,- ,t

." -- ?

-- / .

--- Página 65 ---

PACIFIC CAR AND FOUNDRY COMPANY

1,20

ENGINEERING DEPARTMENT

vPt

NAM

___________

REFERENCE

/! 1-79

S,,o,

2..

DATE

PAGE

5,c . C4LOS.

b JELD L//dg- ,V,.hvL 'is§

S, ,u&c- ALAL-

(O6t-T4

t4.

M -5

51, 2,"

-/72, 9JII

4-,

ij- -

-..

: ..

2,07 V -- 67 54-5-,

d +

P--I2r

PCF-RN- I2e4

A-22

ek,'

--- Página 66 ---

PACIFIC CAR AND FOUNDRY COMPANY

ENGINEERING DEPARTMENT

NAME

_______________

REFERENCE fi-.

DATE

f12fJPAGE_____

OF___

,!,-

-2 94.

I ~-?9v

<,22

. .

.........

2 4 .,

r I

PKi-RN-124

--- Página 67 ---

PACIFIC CAR AND FOUNDRY COMPANY

NAMEENGINEERING

DEPARTMENT

DATE

REFERENCE__________

1L______

DATE____________

PAGE

OF______ ______

),h((obMU2 5 S.c

, r

.,A &kfD

FE7paLD

(--70,ql

PCF-RN-1284

(cif)A-24

" -".-

--.

a T

--- Página 68 ---

PACIFIC CAR AND FOUNDRY COMPANY

ENGINEERING DEPARTMENT

NAME

REFERENCE 4

DATE

1PAGE

OF _-__,,_o

5Th&5q d C

AWE'.c(

JL+D

22,0 ,'

, : .

"),-'

, s

z '-.-a,

". ,,

: ..

E::

-m4--

AT LH. 5o-o-T

! I tii "

=. " 5 74

7%05

'3,77

'A-

t,)':'5

cv, ,,-C,".

'. s..

LL !A

.CF-R

128

4-.

--- Página 69 ---

PACIFIC CAR AND FOUNDRY COMPANY

- 2

ENGINEERING DEPARTMENT

NAME

_-_REFERENCE

.""

DATE

PAGE

\I.

-, J

~7 4!j

g" PCF-RN-o

-T4 A "-"-2,"6 I~ '

( "

(4' .CLi~ )e

_______

U;.'

- .

...

f, Jvy&.W" h

ii 'k ,2... t

I/0

LC -Th;z. fper4. 6

,,,,

__ _

A -tZ7__,.--____

. -...

. .

¢ Z

4 i

3PCF-RN-I

.-2

--- Página 70 ---

PACIFIC CAR AND FOUNDRY COMPANY

"If

ENGINEERING DEPARTMENT

NAME

__REFERENCE

DATE

OFZ

PAGE-

t,.L

C)7. 12s

( o

AI-3

PF,-24

.627

--- Página 71 ---

PACIFIC CAR AND FOUNDRY COMPANY

ENGINEERING DEPARTMENTA

NAME

REFERENCE

DATE

PAGE _

OF:

CAlump p16c

CtQ

,(J

1222

-4 3 ,.

FL6

.......

(-7

PC-FN, 18

If 8

mPCF-RN-12U

A-28'

--- Página 72 ---

PACIFIC CAR AND FOUNDRY COMPANY

NAME

~~~ENGINEERING DEPARTMENTEC

A C'

NAME

°REFERENCE

DATE

PAGE

_OF_

PCF-RN-1284

A-29

--- Página 73 ---

PCFCCAR ADFDRY COMPANY /J

NAME_______________________

DAEREFERENCE

OATE

___

________

________PAGE

A~i-II

r.376-

242

Y~A

L7G

CF- RN 18

.4A

--- Página 74 ---

PACIFIC CAR AND FOUNDRY COMPANY

ENZ'NEERING DEPARTMENT

NAME__________

REFERENCE 1A

S.DATE

//-/

-79

PAGE

'50PPORT/ AP,,W~tS

2.9375 .O

"*....

.5,7 75-

'281

0!5375

/o.:

_p e

,376'

_.,

...

.,_ ,,

/),,

O~~o.

D7€

.Ott FtLe T D.

317

2o0

'277

100

I234

____

_ o e f,,-

---

PCF-RN-2S4

12)A-31

--- Página 75 ---

PACIFIC CAR AND FOUNDRY COMPANY

NAME /43"

ENGINEERING DEPARTMENT

DATE.

/-5- -79

PAGE

3?-

7/4E

-TR/4+ 15/6'13~7I-"~

S -rs

X×_

oAJ Tkt

C,e,,Q.A

7P4,

.IT_ c-: J/

L. ,

u P

r' 51DE t,

E/f"--"

s OD:-44

~tj

,),

Lo--

{.,

T_(

EUQ P(..-eN

A--LLO T/-)i4U57E/k ,i

.broTT's oFF 14(2ct)o.V7T-L. 7-ti-yes

... .. .. .

. .. ..

. ..

". 0E D-

j TTe L 66L,")

-,//s/g- /j

J- '' ,:"

;,-

e 0 A

ni7LC

LbOAJ-,U

{5) P-

174

M/5s I4r-79(7 f65U.'PZ

PCF-Rt- 1284

L 2

f5 -AO/61 L)6- A3

--- Página 76 ---

PACIFIC CAR AND FOUNDRY COMPANY

ENGINEERING DEPARTMENT

__NAME

J,,,_

_,_

REFERENCE

ATE ______________

PAGE

DAE 2-

_.. 3"

?~4)

chA

F&)ot,

OL)TL4 'L

,AL

L o -fl' .=

A-36

F l

i ii i

,'-:

PCF-RN- 1284A3

--- Página 77 ---

PACIFIC CAR AND FOUNDRY COMPANY

NAME

ENGINEERING DEPARTMENT

NAME

REFERENCE Al

DATE1

PAGE

-TOF_

-: °p,

i/t-7

-?f-

,svo

54 , o

Tg7>'vs

7Ff' T~'. /-k)Lo TW PXG~ -:.

&Wi:-,.4..-Kc

-7 7

P :L I,

--.

,V.N

-+C

RN1&

ht/

A-344U

• ,~O

ELoJ,<

• [j

oc:-'

c::' ;I

<:1

=,oe ,

0---72

L=v&- to

57/

F ':"I,.'3{3,'79tps, (vc c4 ),

--- Página 78 ---

PACIFIC CAR AND FOUNDRY COMPANY

ENGINEERING DEPARTMENT

,~,

NAME

A,&I'

'2----

REFERENCE

DATE

-7S

PAGEE

?57

.....

'-~t

Ii-R-18

A-35

~i45*2

--- Página 79 ---

PACIFIC CAR AND FOUNDRY COMPANY

NAME

ENGINEERING DEPARTMENT

DATE

71 9

PAGE___G

iELA D.,- Levo?, AFs\/.

:--

PCF-RN- 1284

.36

--- Página 80 ---

PACIFIC CAR AND FOUNDRY COMPANY

1ENGINEERING

DEPARTMENT

NAME

REFERENCE A

DATE

__-9,79

PAGE

-_ OF

4126-

Ii:

".'219

1,8757

3,0

/ 0

4_i

ELG

3k,)

Cf-JR1

28L4L

-TO /

c <

..,fl

&) LAU-37Z

I r

.. .CF

RN-

A -3 7

( r /, . (. . S C eA -A ./

!!l.

__ _i-

--- Página 81 ---

PACIFIC CAR AND FOUNDRY COMPANY

NAME

ENGINEERING DEPARTMENT

NAEREFERENCE

.TE-PAGE

OF___

j.... -- -U

4,.4 4 ,

8 (

A-3

( tom /LAT PA T

TG, .AJ)

,~L

(JuG sCALs')

<(K.

PC-N-24A-38

--- Página 82 ---

PACIFIC CAR AND FOUNDRY COMPANY

NAME A

ENGINEERING DEPARTMENT

_, ,,'i

,i "

NAM E

REFERENCE

/ r

DATE

PAGE

OF_

C- o./~~

WAe

,4,MEP-

73ov'voCi'j

c C-.,A, A

. ,, ,_,

%Nt~4

FT CYL ... ::

'Th'T

6ii

4 4-

r,5

0.-9

8 z

....

.....

"tI![I

.,e

': 1

14-

DimsA

PCF-RN- 1284

A-39~

--- Página 83 ---

PACIFIC CAR AND FOUNDRY COMPANY

NAME

ENGINEERING DEPARTMENT

NAME

REFERENCE A

DATE

9PA/E -7

PG_

__OF_

BODY

/ ffi AhPj

j c- c -

..... --

z -

252

.37

ItA

.,.0

75.2._V

Cro

TO 510

/9.5w

IA._

, 300

2.625'

A-'

GVOE

ALAT4.

--- Página 84 ---

PACIFIC CAR AND FOUNDRY COMPANY

ENGINEERING DEPARTMENT

NAME

REFERENCE

DATE

PAGE

r.,.

.................

___.[_ff

_-_,5

V~ +'

__I_,.

L .

, 1

IFN I-

1- (A

CYLv

,tou 43 -.eel -3A V)

Ci-C

U2) =5pl

e/E A ,

())

• 1PCF-RN-

1284

A-41

--- Página 85 ---

PACIFIC CAR AND FOUNDRY COMPANY

ENGINEERING DEPARTMENT

NAME _______________REFERENCE

DATE _____________

_______O

____

A Co Po er/z P*l

U-5eo_ rOF

77tlF

IAf/Z~ P60/6 T)__

L)-q_

IJ~

/ ~~

1 1)Y

___M__T

_A4 -

ItF

A-42

--- Página 86 ---

PACIFIC CAR AND FOUNDRY COMPANY

NAME

ENGINEERING DEPARTMENT

oATE

12 -7

PAGE

KBAXISi

08:33

12/03/79

t'.ONDAY

106

1 DATA 20,79.3933

2 DATA 5.1875

4 DATA 1.25,2.25,.0625

10 READ E1,E2,S9

20 READ Sls2,S3

30 READ R1,R2,R3

40 A9=E2/2-EI

50-A2=RAD(A9)

60 Ml=TAN(A2)

70 M2=TAN(&PI/2+A2)

80--A3:RAU(E2)

......

90 PRINT 'STROKE','RADIUS', 'CHORD','L-COL.', 'L-EXT. 1'D','D1'

100 PRINT

12.0 FOR S=Si TO- S2 STEP S3

-5 i2

CO'_

120 L1=S+S9

130 L2=S+LI

140-FOR R=R1 TO R2 STEP R3,

&-" J-AO

150 H=R::COS(A3/2)

160 C=2:cSQR(Rt2-Ht2)

..l-O.S=(Li+L2+C)/2 -

-..

180 IF S05L2 THEN 330

190 R0=SQR((S0-LI)::(S0-L2): (S0-C)/S0)

i !

--200o A4=2-!:ATN RO -~ 0 -

... .... ... ..... ....

......

210 X=L2::COS(A4)-C/2

220 Y=L2::SIN(A4)

230- B2-=Y-M 2::X . .... . . . ... ... ..

. . .. . ..

240 XI=(B2-H)/(41-M2)

250 Y=1M2::Xl+B2

270 IF D1<1.4375 THEN 320

280 IF D1>2 THEN 320

('-

QcL+)

--29Q U-b

SQR (Xl

t2 +CYi-H.) 2-)

....

........

300 IF D>6.8125 THEN 320

310 PRINT S,RC, LI, L2,D,D1

330 NEXT

340 NEXT S

350 GO TO 370

360 PRINTT'CPU>9.'

370 ENJD

PCF-RN-1234

A-43

--- Página 87 ---

PACIFIC CAR AND FOUNDRY COMPANY

NAME

ENGINEERING DEPARTMENTF

NAME

REFERENCE'

DATE

,.-

-- 79

PAG

OF____

KBAXIS1

08:35

12/03/79

QIONDAY

106

STROKE

RADIUS

CHORD

L-COL.

1.25

1.3125

1.67665

6.4375

1.25

1.375

1.75649

6.4375

1.5625

1.99601

6.6875

1.5

1.625

2.07585

6.6875

1.75

1.8125

2.31537

6.9375

1.75

1.875

2.39521

6.9375

1.75

1.9375

2.47505

6.9375

2.25

2.87425

7.1875

L-EXT.

7.6875

6.1921

1.671475

7.6875

6.03465

1.94505

8.1875

6.49588

1.56213 -4

8.1875

6.35434

1.80455

8.6875

6.79439

1.45981

8.6875

6.66439

1.6806

8.6875

6.53676

1.87036

9.1875

6.73144

1.90012

"tPRPP-D ,q

P12 M) -6)0

OF Pos0511-:-,

.,,.,-.-C'

Ct?C

COe

' !.5M

c-.

£9LOXO : s./7_

Ate"/

....

lq" t kL

P7PF

,',

FUR'LL T? " 5Ltt

N--5

-7012

PCF-RN-12S4

A-44

--- Página 88 ---

PACIFIC CAR AND FOUNDRY COMPANY

ENGINEERING DEPARTMENTA

NAME

REFERENCE A -L,

9-1-79

PAGE

- rip

L15 1

PA5E.

. ...

. ... .......

3E__

_ _ _ _ _ _ _ _ _ _ _

_______!2t

e~CF-RN-12U4A4

3A-45

--- Página 89 ---

PACIFIC CAR AND FOUNDRY COMPANY

NAME

ENGINEERING DEPARTMENT

A-L

NAME

REFERENCE A"

DATE

3-I'2--79

PAGE

4(a

OF_

<5110e 13LOc4

SLIOEiZ PS

CATe'-0

uoe7 1a3LOcDe /-5

01-47E o

TOE/

6EPE. '

C",

-Ft

(oQ GeTT1/9.

PCF-RN-1284

--- Página 90 ---

PACIFIC CAR AND FOUNDRY COMPANY

NAME

,oENGINEERING DEPARTMENT

DATE

9-12-79

PAGE

4 7

BOO

I,,/-

____ ___ __L OF

___________-5

(yt& ATFCg AgMt,'

PCF-RN- 12U

A-47

--- Página 91 ---

PACIFIC CAR AND FOUNDRY COMPANY

"A..L .

NAME

VPENGINEERING DEPARTMENT

eFte

rREFERENCE

______________

DATE

9PAGEA

OF___

/"-A

i________

[jC-A

rtN&

,.2

_ .

II,

_____

A-48_-,

FCF-RN- 1284

A-48

--- Página 92 ---

PACIFIC CAR AND FOUNDRY COMPANY

NAME

, /'

ENGINEERING DEPARTMENT

NAME---&

?_L

REFERENCE

---

__.____

DATE

PAGE

Pic

~~~ This

5A :e--*;je-"-;%j-

o d '

________________

V~ 6

A4j77

2 PF 5/

~_____

- '

jL2.

"J'

G, .5

:.1.

',-

PCF-RN-1284

A-49

--- Página 93 ---

PACIFIC CAR AND FOUNDRY COMPANY

ENGINEERING DEPARTMENT

REFERENCE

DATE

P-5-79

PAGE

___i_.....

r_"_"

YT-

-21s

ot,"c

Ito2

rza

20uV

20.

PCF-RN-I

A-50

--- Página 94 ---

jPACIFIC

CAR AND FOUNDRY COMPANY

V. NAMEENGINEERING

DEPARTMENT

DATE

-~PAGE

OF ______

22:21,467S

.Anel MA 5.)

= 2 ;. 7T4 "

6a 2

P5 20 (4 2- )

T~q

v~v14

}1'('

P(efj 3 (

/42(..42). 5,

-!-

04u

PCF-RN- 1284

A-51

--- Página 95 ---

PACIFIC CAR AND FOUNDRY COMPANY

NAME

ENGINEERING DEPARTMENT

A b

DATE

52___________

CAGE

(364>1

-)TA7

P-.

KZcsps~

____T!_

Rk Ift0

t441

~ ~

~~~T

2iThL&)

&~:

(JTAO(/

xpouAl

PCF-RN-12U

A-5

--- Página 96 ---

PACIFIC CAR AND FOUNDRY COMPANY

ENGINEERING DEPARTMENT

NAME

R~"

EFERENCE______________

DATE

I2L~-c)PAGE

____

7c\0-xc

q--

- ~-

~-0CO

L -T0L

N J 3.t-

o% r?-~ I

f-o\ ~ t-CO .

u0,-

0O.D

'oco

___

___

-!1

_j ~~~'

_____rjr4Cjc~

y m( -r -

H H~~

N mA

nL- z zr

r o -i C',

r-i 0

V\ \-Q H -r

H N0 o

t'l

z-t

c".

--z

" ulH

I Hr-r-IHN

(nU-%.oWO

' 0C\

0 LtCO HO

m t-0

cuv

C!DC

t-0vc

L'N= 0 ar-H

4T -

(y)(V ( ce

Cu(N

Cu Cu u- H

t- a\.~

(\)

T -1 \.c L

-% 0C

C H 0 Lr%

II1:I

0()

Z7C

O L

(,U 0\,

_-x _-x _r m~ N' N r-4 0 .r\

Ho Hl u: OH

LnmO,

Cu7M

H H N

*..

...

0 a.

C-0 0

n NN %_oH

%oco n

U"% 0

~.~Cu

IHH

Cu 0

l-T k3 \ 0007 H

N NN

NCV0

H' 0'Nr.,

LZ-i H

A-53

--- Página 97 ---

PACIFIC CAR AND FOUNDRY COMPANY

ENGINEERING DEPARTMENT

iiN

5'-4/

NAME

______________

REFERENCE

DATE

________

PAGE

___

-. o ,.

/-tc-7

.°o

11411I~u,

12.

/"f,

A-V-0(..07-

M0w

4/,&9/

3 o4j/zl

=!".'J .:6 19.1K$ "'

Vz4IW4V

27, 022

- 77..-<'

o..

;''t- -24

.n 4 ,

>....

ii.

...

r'4

PCF-N 1284

A-5...4

.'1

____(,_,___,._¢

-a-

--- Página 98 ---

PACIFIC CAR AND FOUNDRY COMPANY

ENGINEERING DEPARTMENT

NAE

_____________________

EFERENCE (1

DATE

11-t9-79

PAGE

OF_

.2?

%: ,

,', 2 4

,55 .)

771TG

L .

-'t

:C-

rEE]£

Ltt.

, C I" k

CIA-"" ,C.

PCF-RN-1284

A-55

--- Página 99 ---

PACIFIC CAR AND FOUNDRY COMPANY

LENGINEERING DEPARTMENT

NAME

REFERENCE

DATE

/PAGE

OF_______

ST.UD

-/<,

,..:.

KBEARSTR _ 14138

11/19/79 MONDAY

I06

THIS PROG. CALCS. BEARING STRESS IN

HOLES DUE TO BOLT BEARING & IOMtENT.

ENTER HOLT (SHAFT) & HOLE DIAMETERS.

? .369,.375

ENTER HOLE DEPTH, BOLT LOAD & MOMENT ARM.

? •375,713•5133, .25

ENTER POISSONS RATIO & "E" FOR BOLT MATERIAL.

? .29,29500000

ENTER POISSONS RATIO & "E" FOR HOLE MATERIAL.

-- --.

29-,-2950ooo0o

...

....

......

...

ENTER HOLE DEPTH INCREMENT (INCHES) FOR LOOP LIMIT.

? .03125

NO.-

STRESS-ROARK

.. -B-ROARK

-.- B-ALT-

IL.

65041.6

.186755

.186755

60550.4

.173859

.173859

....

3- ...

----------55698i3---

1599-27

---.159927 .

50381.

.14466

.14466

44431.9

.127578

.127578

-- . ....

.. .....-..

......

-----

51- 8..... .. .....

- ,-

107&2-3----- .107823 ..-

.......

.. ....

29087.5

8.35193E-02

8.35193E-02

16793.7

4.82201E-02

4.82201E-02

- --

t7---

-4.8219E-02 -

4; 82198E-02------...

29087.5

8.35192E-02

8.35192E-02

37551.8

.107823

.107823

...

I ..

.....

4 3

.9 . .

. . ... 1275-78- ....... .. .-175

78 ..... ....

50381.

.14466

.14466

--THE--FOL LOW44G-PR INT-OUTS- ARE-FOR- (-2:)--FAST -METHODS-fOR- MAX.-B RG -STRESS- -CALCS.

ROARK "B"

P/A: 10188.2 P51

M/S: 54337.2

'5(

TOTAL= 64525.5

B-ALT.

P/A= 10188.2

M/S= 54337.2

TOTAL= 64525.5

--SE-C-TI-O-YOD,: 3.282OE-03 - FOR ROARK "B" &

3.28280E-03- -FOR B-ALT.

NOTE: IF ROARK "B'1< BOLT DIAM., PRINT-OUTS WILL BE EQUAL.

.... ...

A-56

--- Página 100 ---

PACIFIC CAR AND FOUNDRY COMPANY

ENGINEERING DEPARTMENT

NAM

__________,______________._

REFERENCE AI .

* i

DATE

D__________

PAGE____

-OF

/m Pl

It!- 4.y-,

-_____

i,,--

p Ai

PC~-

!+CC

6L&.

66S. )

- 1-

8) Ale

• .

4 R)z.

""o3"OF'

M.;,

:t) ............ .

...

.......

"I1t, 5

5'-

5zS, S"

CPCF-RN-1284

A-57

--- Página 101 ---

i i

PACIFIC CAR AND FOUNDRY COMPANY

ENGINEERING DEPARTMENT

NAME

_"_--_.

.,REFERENCE

OATE

.L'/fPAGE.5

OF_____

1'-;,

AAV

tJ T~oS()-)

,'2,-,

P& s

-J-

i~~~~~~

............

.'.J-

PCF-RN- 1284

A-58

--- Página 102 ---

PACIFIC CAR AND FOUNDRY COMPANY

ENGINEERING DEPARTMENT

NAME

REFERENCE

U -'"

(/-26 -79

: _9

DATE

...

g/ockv.,.,T/ f

&o r c.

| .PCF-RN-1284

A-59

--- Página 103 ---

,PACIFIC

CAR AND FOUNDRY COMPANY

DATE

ENGINEERING DEPARTMENT

PAG-79

PAGE

~L)PF'O T Cf+4Aik)E

iAT. 5TetL

5375-11f437.

PCF-RN- 1284

A-60

--- Página 104 ---

.PACIFIC

CAR AND FOUNDRY COMPANY

NAME

ENGINEERING DEPARTMENT

"NAME

REFERENCE"

DATE

PAGE

, 'JP P

CPkJJE L.

OF 51 TOP,

-- N-,

7,1 -A

-to

low

c0-

PCF-RN*

124A0

--- Página 105 ---

PACIFIC CAR AND FOUNDRY COMPANY

uI,0

ENGINEERING DEPARTMENT

NAEREFERENCE

L___________

AA__

Pie_

DATE ____________

PAGE

____OF______

"~~

n-27g Sl

g'L ( o)g

___

____.______.____

174

-..

--- Página 106 ---

PACIFIC CAR AND FOUNDRY COMPANY

NAME

~ENGINEERING OEPARTMENT

L~1t

DATE

_________________

PAGE

_____

~5ppo

r?T- C&,4E

/iAG

470P

~~2c~-d~z.~-'

~--"74

_____

IL)

T/E SUROPoQT

~z~O -k~

TT~kE ARE T.c

O/)ADJQ0 57,+6E3T

~TP

5T09,

4.5r o2

4.93765 r

PCF-RN- 1284

A-G3

--- Página 107 ---

PACIFIC CAR AND FOUNDRY COMPANY

ENGINEERING DEPARTMENT

NAME

REFERENCEA I.?4'/i

DATE

/8~

PAGE

OF______

2~2oi 7 74

~pLi'

I?.148Z4

2OJ9S

161770

AD.4,9

2eti

rfjRj~ .

:1t)

1365Ac ) 5IFIEce k)/7'8 A

7-'PA)AtEOA

llur$J

PCFL-RN-1284L4Ou~ iiL

~Te4M~~)c

PCF-R-1284A-64

--- Página 108 ---

j U

PACIFIC CAR AND FOUNDRY COMPANY

/72

ENGINEERING DEPARTMENTA

JJL

]Jl

NAME

If.~c~fb

17REFERENCE

DATE

PAGE

ii'i

E .. '

. 1 J

(.425

_____

_____

2&323

4 -

2.N

5uP0E?-r cHA~VA&6?EF.)

ruL L 5/iz__

PCF-RN-24

A-65

JT&A(~

--- Página 109 ---

PACIFIC CAR AND FOUNDRY COMPANY

ENGINEERING DEPARTMENT

NAM

.__ "_

REFERENCE

DATE

TI-

PAGE

___

J _

/ i

il~r

j 6-,

SC(.iA{,JUL

.__

___

Akcjr&:

ANJ f367 IAC

PCF-RN-l2a4

A-66

--- Página 110 ---

PACIFIC CAR AND FOUNDRY COMPANY

NAME

ENGINEERING DEPARTMENT

DATE

PAGEJ.

77Tr

(C,2).

.CF-1 -5 Ol,r

0cYL.

I500_P51 .

,,Z9..L?

. .....

) C ,

-c .

--_

PC-N-24A-67

O/)

re~

--- Página 111 ---

PACIFIC CAR AND FOUNDRY COMPANY

NAME

ENGINEERING DEPARTMENT

DATE

PAIG'E9

PAGE

(08

:a To1? C/#4t/JCIS

474

-4--

1275

,:zs

4AI.(

+ti4

(Al V

-ID ,-

PCF-RNA1

A-68

--- Página 112 ---

PACIFIC CAR AND IFOJNDRY COMPANY

ENGINEERING DEPARTMENT

NM -E

REFERENCE A Lt-

DATE

AGE___

OF___

I2 K15

-7-

A Co,)TEA

PeGP,4*\

6EFL 4)(?mi

154 j5-ome

79) /SE

A~~

0 137ii'c) 7thE TOTktL Q&FLe&70Q

(3~/t$,

5/ce77H-

~A) OxD F 77I (z

K~if41~-: F~

A OPUV() Dre:r~

3-'

PCF-RN-1284

A-69

--- Página 113 ---

I H

PACIFIC CAR AND FOUNDRY COMPANY

ENGINEERING DEPARTMENT

NAME

_____________

__REFERENCE

LV -

DATE

12-

PAGE

otDA

04i

ICA

-QPP "J~~

AKk

\ck;OD

t-O-~

T8'

lf> m ,.,

0 c-o)

A74.A4

2 /36

P"oc a/

HN)

A-70

--- Página 114 ---

PACIFIC CAR AND FOUNDRY COMPANY

NAME

ENGINEERING DEPARTMENT

DATE

/!-f1--79

PAGE

~!7 h

Ct'

~%T1:

,0. .

7)'

ef'

K1r,,7

(• ie....9)

_ ...

I-y.,_

"j--

____

_ .

.....

T h

. _

___,,>

Ilot)

N-18

A-71

--- Página 115 ---

PACIFIC CAR AND FOUNDRY COMPANY

NAMEENGINEERING

DEPARTMENT

jNAME

,REFERENCE,4

',m"

DATE

,2l'9PAGE

OF___

' i?.-:-?l-' ,9,

(? r.)?

T.4I)

Y2-J

-7)-~

PC-N1S

- 72<

: U . -i 1

(Li

:aj

i ....

L ..

.. ,

-"..

(p,.,),,-

_ _ _ _ _ _ _i

--- Página 116 ---

PACIFIC CAR AND FOUNDRY COMPANY

ENGINEERING DEPARTMENT

NAME

-________________

REFERENCE

______________

DATE

12-11_--79

_PAGE-

OF_

CEN TE R P79 6,iL>

/I V

>n,

(Fn

17v~~k~~9)

(F3)~~(~24~2

PCF-RN-]2a4

A-73

--- Página 117 ---

S I

--.... u l_

ill~l~~:-]=-.~ _ . .....

---

,,, --.

- --'4.

PACIFIC CAR AND FOUNDRY COMPANY

NAME

ENGINEERING DEPARTMENT

NAME ...

_REFERENCE,

DATE_

PA GE__

-OF

M l

.r.

- 70

" .

/T_ 4

.,FW)L::

.lL

V79

L3 i'5/ )(T

7 )/-

&Tf*L )7. .

SPCF-RN-1284

A-74

--- Página 118 ---

PACIFIC CAR AND FOUNORY COMPANY

ENGINEERING DEPARTMENT

NAME _______________REFERENCEA,\-t

1DATE

2-/2-9

PAGE

75",

__W<-. 7714!:CI-

4"-,'L.C&,t

Ct 9

LOF

Et)C14

CfH W1-~(~

7-w)

10 L I --, 0 52 5, 2 6,

/5z

t.o0,

(e t4

r2-

1(,l.)-/S

')/17 &

3(O)/-C7

PCF-RN-1284

A-75

--- Página 119 ---

PACIFIC CAR AND FOUNDRY COMPANY

ENGINEERING DEPARTMENTA

NAME

_-,

_-_'7

REFERENCE

7:--,

DATE

PAGE

____

(I ?g'.CTI

C1-JA{J.JLS

5T? - C /

C,4

'~i S

/.rf Td_:? "T-W& $e_./<...4

rJWJ. A P ,pT-cj- , E

"T:-re- E//3A(,_Loi ",.

',-~

)3 A,-...

/-C.j ,..

'bU R-

KuUEFL4

_ 0:44

12/12/79. WVEDNESVAY

106

PkUO.

CALCS. UEFL.,LOADSMOIIS. & STRLSSES OF RA1HU,

R ERECTOR CHANS.

N, .. ......-*1 HOR. U...

#1 DEFL.

#2 DEFL. REQ.

257.822"

-,142738 in.135753i.

MAX. bULN.

STkESSES IN CHANNELS.

Nu.

41-T-T

9551.3 PS1.

-10332.5

PSI.

11228.J4 P51.

#2 ifOR. LD.

R2 DEFL.

HOR. ANGLE

- ..

98833 -

lo422.2 P51.

PCF-RN- 1284

A-76

--- Página 120 ---

PACIFIC CAR AND FOUNDRY COMPANY

NAME

o,4,t,3

ENGINEERING DEPARTMENT

NAME

REFERENCE

-r7

DATE

l2---f

PAGE

C45 I CeJ5'Q~LD ,. tL '77j )64, 3T- .

C. 7:,.,. .

.9L

A L

fo)""-/A- f

N ,

17.5

*~.

______

,.j\=

(A)A-S UW UZI~

-jHL7

6k/~)(.

tC)

,.h , ..-

,..,. ,,,-,®.,

C--.r

,ti .. J,)&L 7 ,:L! A 1F2 e 'W

' ..

.**.

PAZ

OEF67&6, AV-E0

77lt: UVJYCHW L

KBUEFWV1

12:48

12/19/79 WEDNESDAY

106

250 T8 _9

"T * 572

Y'COS (A2)

* j74I Y4=Y9::sII4(A2)

576 A3=LEG(ATN((Y3+Y4)/L9))

7bU

REM

1090

"" """--".....

1095 Y- =Y~T;S IKA1)

'PCF-RN-1284

A-77

--- Página 121 ---

PACIFIC CAR AND FOUNDRY COMPANY

NAME

ENGINEERING DEPARTMENT

_NAME

REFERENCE

OATE

IZ-9

7.9

PAGE

y~~LC7D? C/ ,/J,-eIK 'S.

6VR KiWEFL4,.KBDEFWV1

12:149

12/19/79 WEDNESDAY .IO6

PRUG... CALCS.

DEFL.,LUADS,MOMS.

£ STRESSES OF RAINER ERECTOR CHANS.

NO.

#1 HOR.

LD.

#1 DEFL.

#2 DEFL.

REQ.

175

-9.b642&E-02

-. 128643

tNAX.

END.

STkLSSES

IN CIIANNE LS.

NO.

-i-T

#1-8

#2-T

1 .

66o3..6

7434.82

14475.

#2 HOR. LD.

#2 DEFL.

HOR. ANGLE

-.2391108

.755235

#2-B

/k)o¢ T/T Tfh'- ACWO/irL

2O ft. IS if'oEE ThA'.,J .:

IC4) " ? DRL

C4s6 7TN Jcor Is /OA-7

8/,.'v

PCF-RN- 1284

A-78

--- Página 122 ---

PACIFIC CAR AND FOUNDRY COMPANY

ENGINEERING DEPARTMENT

NAME

As__

_REEEC

DATE

2__

PAGE

_____

),.J

1A 0

, -_ -

" - *.4

I--

,'.-I

!/h,, ,(..jj'

('4 "

Rcr

F 5A77

(.337) ,i

.. ,_:

F - .,-lqwlr--,

PCF-R; Ii

A.-7

--- Página 123 ---

PACIFIC CAR AND FOUNDRY COMPANY

ENGINEERING DEPARTMENT

f..

NAME _______________REFERENCE_____________

ATE

PAE

80~~1

1-<

' .........

"3...

....-

( 7 .

-128

LIA

-8,0

A--

i!ij~

3M-

T O'1/

--- Página 124 ---

PACIFIC CAR AND FOUNDRY COMPANY

"-ENGINEERING

DEPARTMENT

9-(.-79

PAGE

OF_

T -'5ppa,,zr- c -vtuec is

u, Tepya

-'m_,TH

,JTkat.. )The,45 Ck,,) B ALei td16uJA~rEO) "' 7>

3ar"tL, Put4W

75,

PCF-RN- 1284

cw1(. )

A-81

--- Página 125 ---

PACIFIC CAR AND FOUNDRY COMPANY

ENGINEERING DEPARTMENT

NAME_______

REFERENCE AI!

~WENO

DATE

PAGE

r-r

I.."-Af 's

.L"

, r

/77(2)

2(2S425) (2

/9667

793

-3 50-

012.13'.q

FL~cT(OCJ5 1C Tw /JTtmEA4ED/ 4'

'STPOCTO11L. M

LEte

S VUYL

ADD 7 T--..........

PCF-RN-1284

--- Página 126 ---

j. l

PACIF IC CAR AND FOUNDRY COMPANY

ENGINEERING DEPARTMENT

I ~

NAME___________

REFERENCE /-

DATE

9___ -?

79______

PAGE

63_____

OF______

V~C~TcASOF -TV15 k1

/UV

CA1J L3-

li! APCOM

7EDF6e B Y

WP)Q-Tt-J@_ThF

llb(T/ob__41 TrlTuoe6r-?A

-r6$'-

CFbOJU

Dff(S 15Dr)00E_13_)00<1005 L/eCA)EP7

OFf TIE

77fE7)

C-tA JbEL .1 CtOC //J 177I

*5c0(YZkT

CI±4/W,3CL. 10 )Y

t VA)T,

Y6E oP77omom4

",tm"

0FThE_ 'AMMEK

Ut)

JLL HAUJC TD /3C DET6hi2-

124

77(2),31.iz -

1777(-;)

PCF-RN-1284

(clk

--- Página 127 ---

PACIFIC CAR AND FOUNDRY COMPANY

ENGINEERING DEPARTMENT

NAME-1&vc

REFERENCE A-to

Am Q

DATE

PAGE

U N'..

3 5

---

-4I

D/oTe: O04.'-i

oie

C4,U t):L. -'ct u' uo~,

1 5¢r, (, '

A1l

~A~L~

--- Página 128 ---

PACIFIC CAR AND FOUNDRY COMPANY

ENGINEERING DEPARTMENT

NAME

___________REFERENCEA

PI1m~i

DATE

1-709

PAGE

OF____

J P

-O i - OF 5A. FS

A LE

I-)

_T____

---7t

2CO$ I3f

PCF-RNP

128

(0Lx.

A-4(4

--- Página 129 ---

PACIFIC CAR AND FOUNDRY COMPANY

NAME

~~ENGINEERING DEPARTMENT

A-?~1e

DATE

PAG

'9-07 - -7!2

6uepo --

r-,mm~w z Assq,

6o wc-co 120

11,-,

F7.1eTI.t~_

0 t#

+ I oc% 4

/20

~I4,32._ -- b * -- b~ 2.430o4'? 3'

djse ,

,r) -

12el

PCF-RN-1284

A-86

--- Página 130 ---

.PACIFIC

CAR AND FOUNDRY COMPANY

ENGINEERING DEPARTMENT.

NAME

________________REFERENCE

DAT

PAGE________OF_____

G(h-U&

P-)

E74 1A)L

T t T' U U / TS/,W:

0 7(CXOU THEIJ 77- c:14,

Nww

PCF-RN1284&L

A-87S)))~4b~L~

--- Página 131 ---

PACIFIC CAR AND FOUN|DRY COMPANY

NAME

ENGINEERING DEPARTMENT,

NAME

REFEiREN.f A

DATE

''~PAGE

____________

________

3PA___AL 5C-7/00 VIGO _ OF IM____P_

5(Ej~ TL

COOSO

.4 I~

I3LcC

TL-, L.

111i

~iI

R{/V&&(PAP

PC.-VI'

I c1

A-88

SPCF-RIN-

1284

A-88

--- Página 132 ---

PACIFIC CAR AND FOUNDRY COMPANY

ENGINEERING DEPARTMENT.

NAME ___________RFRENCEtT

DATE

224- 5PAGE

89 -

____

4C-N1S

A-8

--- Página 133 ---

PACIFIC CAR AND FOUNDRY COMPANY

ENGNEEIN

DEPARTMENTI

NAME

REFERENCE .

. AAA-6!ti7-i/',"

DATE

ENGINEERING

PAGE

ToCP T.P...

'velckL ToP C- .

"0"'6

-.'

0_0 Is

PCF-RN- 1284

A-90

--- Página 134 ---

I j

PACIFIC CAR AND FOUNDRY COMPANY

ENGINEERING DEPARTMENT

NAME

__REFERENCEGA

Ir&

/'J

DATE

'22-

OPAGE

OF__

AJOT0/7~

SW6~eJt;E - f'CQ$0,,PowOc-7Z

CmVIdJ(5 mEps

)/307F

F01Z 77//71LL

e'-

1ol~T op 7TOE

Y&YOA(Jc e6c~2_

4,~~J

7A24t/

DW5crtL r-A6tec

07-z A NJt.

~~3k~~~~&A

,+YeA&,C

64)

4 ~C-N11

A______91_____

~ //'~7&1

~77O9

4~OOC0

~~~'Z

C!&r,16

--- Página 135 ---

PACIFIC CAR AND FOUNDRY COMPANY

ENGINEERING DEPARTMENT

NAME ______________

__REFERENCE

DATE

PAGE

CLAe-/C

PC-N124A9

--- Página 136 ---

PACIFIC CAR AND FOUNDRY COMPANY

ENGINEERING DEPARTMENT

NAME

____________f

___

REFERENCE

DATE__2-

PAGE

2CeJTRz'VCV6

769

We..

~ae

1~e

oLOveeY

1..16k

OFc4

PC-N) 4A9

--- Página 137 ---

~W:0-.5

PACIFIC CAR AND FOUNDRY COMPANY

NAEENGINEERING

DEPARTMENT

DAE

Z7l

PAGE

OF____

I-it/I2A OF 051A)( r

Pk~

~(ccJ

1A) A Cb/J L) e

V W6

Y"57

-5 4J) 7 beA)

IA) 50

CT 7D!CeR-,<

LO7~M 0 rW'

PC-N

12S

--- Página 138 ---

PACIFIC CAR AND FOUNDRY COMPANY

ilD

ENGINEERING DEPARTMENT

NAME

P/1

a1~l

REFERENCE

DATE

PAGE

2"7--7

12:311

02/27/80 WEDNESDAY

x06

ANL

4.02768

11.02768

.005537

1.12019

3.22215

3.111131

219

12.3779

1.2033

1.611571

2.81938

3.261!55

21.C'!81

2.013814

2.56326

2.01384

3.25973

Ill. 23511

2.141661

2.93268

1.61107

3.341607

3.59c985

2 ,i

8l1j

3."215

3.158

3.50;102111

54.6036

40277

3.60295

530399

74.

625.

1. 90735E-0-3.

6256

-... 5. 9

C70)L---

-4.80537-

3.58037

.402766

3.60295

53.6096

4.t3322

3.11750

.805534

3.5110411

55.0781

5 .675

2.93269

1.61107

3.311607

3.98438

6:0..

2.5b327

2.013814

3.2 971

67118

3.110

1.61572

2.801938

3.261155

22.3425

7.214983

1.12019

3.222111

3.111131

12.7625

y tG..259____- .5.6'108

.9735Eig-0----3.669 5-

5--

917-

-M.6J5il697.03

4.02768

4.60279

2547695

LIST

12:36

02/27/80 WEDNESDAY

106

:.39

.25_PRINT

'Y,~!P!'NLr

30 UlzfPl/C2:B)*

40 0p2:1/1

60 Y=:ISIIJC0'X)

565

IF X1

3 4Tt

1N3

70 L:81l-X

72 GO TO

74 L X-1

84 ncm

85 F r. 1.0

TH.EN 9/

-966i 0

=3.

B 0 TO 100

90 E=DEG(ATt(Y/L))

92 E INT( )

94 I =PiI()::6O

96 E2:INT(E!)

110 IF CPU>9

THEN 160

120 1.'EXT X

l-30f~i-

150 GO TO 170

16u -PRINT f.Q!,U>9,

fm. 0-A,

! "176

L111)

PC4-RN-1284-'

10 E=II

(YtL.))

El~flIT(4

--- Página 139 ---

PACIFIC CAR AND FOUNDRY COMPANY

I ~~

ENGINEERING DEPARTMENT

NAME ___________________

REFERENCE

DATE

_PAGE,_

6P(iie L 6ol)JEYOk DP((/Cs

'&5

7~/WUC

ci2

PC4

!LaE?4v(P

THE7 PO6A)E(2- <1cn)M .Tt

2~~6>2

,AL

'T1V&L$4:

W7747

3&O Ct

A ~

Fu3

1-rLrh---5

k,----,)

II4,PAUL

k.) .~4

____I,,_________

___

___

___7_(-7F<

________________________________7_

if E

PCF-RN- 1284

k 7e-

A-96

--- Página 140 ---

PACIFIC CAR AND FOUNDRY COMPANY

ENGINEERING DEPARTMENT

NAME_____________

REFERENCE

oATE

PAGE

Fvoo A5-/

POLL Pau

liLAA

AFT 5UP(V2

IPCF-RN- 1284

--- Página 141 ---

PACIFIC CAR AND FOUNDRY COMPANY

"EN

DEPARTM

PARTMENT

NAME

EGNRIGREFERENCE~A-

DATE_

PAGE

m, "

--:-~~v

7 4 :

-7..

,d;

o,;''. '.

~~ -Y)5

goo 77Qi?4)

c&(t:

To 0 U..¢

;to~ 57Z,

l / A.Th 7M)

7u'To 4?u&

5 Psi

I CY.

-ro 2.A.

(PCF-RN-1284

A-98

--- Página 142 ---

PACIFIC CAR AND FOUNDRY COMPANYf

ENGINEERING DEPARTMENT

4C~~

DATE

6PAGE

TF~

~2ftL

P-qtJ/O U77UZE-S 7W)

Pou c -PQ4-ft1J LOOS' RTE- 4-IaE 72ycL

Et5CA,

IIf~ Y)~~~'

FPZ Th'Siee r

7/Jr C0hu71-(u

/)4

o/96

SV97%h

flp, PLET6E I

JVs 3 77i WhEP1J

(AJ(LV

?tU

P6,5iTYOA9 Fo)( 7W6-)KL49:

Jf51erjT(

,Oby

4 VSo2T Po,5H-

IAP

'5EFC

PC__N_28

A-99&

4A i6&

--- Página 143 ---

VPACIFIC

CAR AND FOUNDRY COMPANY

NAME

ENGINEERING DEPARTMENT

NAME

REFERENCE

:: o,

o,_____

DATE_____

PAGE.

OF L~r&

2".0-U&Ec FCC-reg-

cfifDE Lj feL7

-PCH1

AJ'-

,.g2

7 Cs

eP rr¢ t,

F'7z~c4 91A. 2,514~~

i-'-

PCF-RN-12S4

'.'.A-100

.-* m . .....

.. .-*" -i"

.." -....

-* 'T " , -T-:-

, ".":'<

-'.

',- .. ..

.4;r, s;

--- Página 144 ---

PACIFIC CAR AND FOUNDRY COMPANY

ENGINEERING DEPARTMEN T

NAME ____________

__REFERENCE

DATE

______

PAGE

OF_

P4 A

I?9j

7'C/t(4$ c C0

6-r t!JE6 fA i-ro

klw~r$

,toLcv

IAuG

6-t& k Wt-

~'&

X E

peah

7' U7 5ThINWJ2

orTtt- 7,6cioo4s1b

-7E

e-6-7t

-400-7g

C-2?lc A lu7OT

77fE

C{JZ SP6C-

PCF-RN-128 6A.10

--- Página 145 ---

PACIFIC CAR AND FOUNDRY COMPANY

NAME

~ENGINEERING DEPARTMENTEC

DATE________

PAGE

(0)2

OF____

- -

- --.-- R -

-3 75- -1

rz.

V~,21~

-6.4/9/-,.J..(reF.

CIOE-oGlr'O1)

OF /(.4*

5.7, -

5,F

, ~

THE.2.

130?\ 04~l r&47 2.o6s

Co./ P/c/,u 04) 74

4, 64

1S!

PCF-RN-1284

A-102

--- Página 146 ---

PACIFIC CAR AND FOUNDRY COMPANY

NAME

~ENGINEERING DEPARTMENT

m &

DATE

?~9 OPAGE

OF___

Au-r!A4Azc LoAD

u&act--

1$ DPOPPEC F) P F tlU

____

4 t

Lovk'u

t4 -FJd .

5T-k itXG 0OR

!3/Iuc/,'}G / $ /i1 -

PCF-RN-1284

A-103

---

4 1

--- Página 147 ---

j7~

-'"c--I

bO.A'~ C,

,-~.

~1~-

~,Jf

(JVv\Q'J1~TK~19

C~cc

Ckc ~

U-I'

I I

4'I

)~ioIdj.

14~

'5,

p ~

,.,.

~t I

jI,'~,

I.'

h7tJL~O

-- 4-

t\~

C~~>L-\

~~1\/

Ai(~1i~

,.1'

'II

-4i~N~41/~<~A.1O4

- I

--- Página 148 ---

APPENDIX

1B1

M109 Recoil Cylinders

Orifice Area Derivation

Vehicle Motion Resulting from Firing

Large Weapons

Stress Calculations

,I]

--- Página 149 ---

APPENDIX B1

M109 RECOIL CYLINDERS

Tentative parameters (Telecon Walter Pape November 21, 1979)

Projectile velocity ...................

3250 ft/sec

Projectile weight .....................

98 lb

Powder weight ......................

40 lb

Recoiling weight ....................

9600 lb

Impulse

(1.3) (3250) (98 + T

= 15483 lb /sec

32.2

Free recoil energy .

(15483)2 (32.2)

= 402,036 ft-lb

(2) (9600)

Nominal reaction for 21-inch recoil

R = (0.8) (402036) (12)

= 184,000 lb

Nominal time for ;'ecoil

= 15483

= 0.084 sec

184000

Use 200,000 lb reaction for design.

Maximum 0.0. of cylinder

= 6.5 in.

(For reasonable retrofit)

Assume piston rod diameter

= 2.5 in.

[Assume 3/8 cylinder wall and 1/4 sleeve

Trial piston diameter

= 6.5 - 1.25 = 5.25 in.

Piston area

(5.25 2 - 2.5 2 )

= 16.739 sq in.

100000

= 5974 psi

Nominal pressure =16.739

Hoop stress = (5974) (5.75)

= 45,800 psi

(OK)

.75

Orifice area =

N Ape S (See Appendix B2)

*31-

--- Página 150 ---

Where:

A = Recoil piston area

sq in.

= Number of recoil cylinders

= Recoil oil density

lb/cu in.

= Distance to end of recoil in.

= Recoiling weight

= Orifice discharge coefficient

= Ratio of orifice generated resistance to total resistance to recoil.

Ube a sharp edge orifice because it is influenced less by variations in viscosity than a

round edge and ', live better with contaminates. The discharge coefficient "K" for a sharp

edge orifice is .61.

For guns whose trunnion reaction are very high compared to their weight, item "C" is

very nearly equal to 1.0 and can be ignored in the initial design.

Then the approximate maximum orifice area =

Ao  = 16.739

/(2)_(16.739)(.0313) (21)

.61

9600

Ao = 1.314sq in.

Orifice sleeve area

= -

(5.752 -

5,252 )

4.320 sq in.

Percent cutout

1.314

= 30%

(OK)

4.320

1B1-2

--- Página 151 ---

The classic expression for orifice area derived in Appendix B2 will give precise values for the

portion of recoil stroke coming after the chamber pressure has ceased to produce a

significant force on the breech. For weapons with a relatively long recoil stroke, this

expression is all that is needed since the travel consumed while the recoil pressure is building

up to maximum is a small part of the total travel.

FL.r weapons with a relatively short recoil stroke, like this one, the recoil travel

consumed during the time the weapon is being accelerated can be a significant part of total

travel. To optimize the recoil system (i.e. minimum trunnion reaction) for these weapons,

the orifice calculations should take into account the varying breech force.

A very successful solution to this is to determine the position in recoil, where the

net force on the gun is zero and apply the classic orifice area formula from there to end of

recoil. Then hold the orifice area, at the zero force point, constant to the beginning of recoil.

Another method is to actually solve for the recoil velocity at small recoil increments

during the time of varying breech force. This approach has been made much easier with the

advent of the computer. Following are calculations for orifice area using this method.

The interior ballistics were not available for the weapon with the parameters used

for this design. A computer printout of the interior ballistics of a similar weapon was

available and is used here for an interim orifice design until the interior ballistics are finalized.

B 1-3

2Q,

--- Página 152 ---

:--

/k_________

-L-

=Mr-0

IU)

N.N

.4-

m~~

1-4

--- Página 153 ---

RECOIL ORIFICE

Let:

= Solution point

= Time - -- sec

m -Recoiling mass - --

jbse

in.

Recoil travel -- -in.

Recoil velocity -

in/sec

FB =Breech force ---

F R = Recoil force -- lb

Mass force o F B FR

Ap Recoil piston area - -- sq in.

=Orifice

area - - -sq in.

=Orifice discharge coefficient

Orifice width -

in.

--- Página 154 ---

i i

L2V

V 9

A p

oil

KAo

2 Ap

(2 cylinders)

VgAp

Vg Ap

2 Ape

A 3 e

=16.739 sq in.

= .0313 lb/cu in.

- 386 in/sec2

.61

//(16 739)3 (.0313)

.61

386

=1.011

B1-6

--- Página 155 ---

1~b

Using 3 slots per sleeve

2 2r

.2424 Ao

jj(6)

(4.320)

(.2424) (1.011)

=.245

=(5.75 +5.25

SinO

5.5 Sin 0

=5.5 Sin .245 V9

HI-

13I

--- Página 156 ---

-7jz

0 D00If

0 .K 1 [

oLL-mm(- r -YJ~

0r IA

CO-

cjI

- -

-MZI

O i0-H

H ON m~ 0 L

mr~i cy') M

o ,1

11.1O

\L )

~ H t-

COC H

MY' %0 Lr\

LA Ln LAIU

CIO~I

O'~-. m iy m M

00 ,

l 0.(I00

0OCO

N H Clrtl--r

c0wc

c c

- -- t

cLco

L-C

r- 1:-

t-O -

mCM-c

* 1. c*C .

.I .

c0000000

00000

00000010000

cNC oca

AC\ L"

CAAL

LLc L

(-L'\LALA~

00000

LLU\U

L.I-

c\LO

C o

\L\nLxU

U-\C Ll

0-jV

LN in L\V'N

V\ r L

LACO

,\C,\ C

L'Vt-C 00

C ONI

L-p C

7 04H'

OH ' r

M M '%I H 0'\.

HCJ IN

C~jr

~jc N c\J c\j N jN NNN

C\NIjN NNN

C\;N C4

jINm

0 ,

*1*

*: .

.*I

..i

. I"

CY)r-im

C1CO-

m. 0%N0

- 00LNt

=\ Hz C M

NIMLA

iMCO

(-, C~-

- a , 00 t- n = M

Zc"t

ftcc,

.D=C

L-\

m 0

I'r c

nr 0C

L-~LCs

t-'

LACYT 0Ccm~

LC4I

C\J

NHO

ONi

r- r-.-LHC.

(r-"rl'C

pa~'

__:_

-~ -t-iH

N~jlA

VLn

- - H

H r-iri

HH.3

0O\

%- a

-0_0

01N =~ H0 M~O L

OC )

Cl M

L"\ t>-O Ck-i

N\~

-V\

(;\"00q

OOXlA~

'NJt

NNC\JNO,~N

o w

U"LA

LCO\ m :N

*-.=

=L\COQcD

%0 1 N0);

O%.

-_x=

N -T

O\ O

-w:

nwR

aC)-

N -, a\C7\

0 ~

0000

00\P

co\~NN

H O

~ ~

H CO At-ON

-40

'c-OH

.0I

.. i

--r

N t- Il - (1-3:1..~..

V-')

.\ L~ 0 4\D11Oc" -- c"

Y)c

MN~~_

C:.

()mI

O-jr

0 H

-rL,)

1- 8

t."\-

co(

t-t

--- Página 157 ---

BUFFER

Piston rod area required to pull 100,000 pounds at 50,000 psi stress

Area = 2 sq in.

Rod diameter is 2.5 in.

Maximum inside diameter of rod = d

/it

2.= 4

(2.51 -d)

d -

1.924 use 1-3/4

Buffer spear area

(1.752)

= 2.405 sq in.

Assume the counter recoil force in battery will be 1-1/2 times the recoiling weight

(maximum) and the pressure will double in the 21" stroke.

Apprcximate stored energy = 9600[ 1,5 +.(

)] 21

= 453,600 in-lb

The recoil cylinders will dissipate approximatelh 1/2 of this during counterrecoil.

Energy to be dissipated by 2 buffers is then 226,800 in-lb

Force per buffer with a "S" stroke

F = 201000

18,900 lb

(2) (6)

Pressure a 16750

7,859 psi

2.405

Buffer orifice area -

(See Appendix B2)

Use a round edge orifice, 1%

= 1, because the small clearance between the I.D. of the

buffer cavity and the buffer spear precludes a sharp edge orifice.

Then Ao = 2.405

(2.405)

(2) (.0313) X

1"1

49600

Ao = .00952

4 -

Use 3 orifice grooves .100 wide

Groove depth = .00952

.03173

47-

3) (.100)

Buffer orifice depth

.03173

4'x

.032

.045

.055

.063

.071

.378

81-9

--- Página 158 ---

APPENDIX B2

ORIFICE AREA DERIVATION

Find the orifice area for a constant force recoil system.

Let:

= Recoiling weight - - - lb

= Recoil piston area - - - sq in.

= Number of recoil cylinders

= Recoil oil density -

- - lb/cu in.

= Distance to end of recoil - - - inches

= Total force resisting recoil - - - lb

= Pressure developed by orifice - - - psi

= Ratio of orifice generated force to total force

= Orifice discharge coefficient

= Recoil velocity - - - in./sec

= Velocity of oil through orifice - - - in./sec

= Grifice area- --

sq in.

= Acceleration of gravity -- in/sec2

After the propellent gasses cease to act on the breech, the kinetic energy of the recoiling

weight at any point "S" is equal to the work that will be done by the constant force "F"

acting through the distance "S".

K.E. = FS

= WV'

2FS

Oil velocity, Vo

= Vg

Vo also equals

= V

GF S

KA0

1KA

=6~

2G F§

;2 e

FS e

Since C

PNAp

p=F

NAP C

NAeS

/WC

B12-1

--- Página 159 ---

APPENDIX 63

VEHICLE MOTION RESULTING FROM

FIRING LARGE WEAPONS

Chase I suspension is active. This is analogous to a load suddenly applied to a mass spring system

where the product of the magnitude of the load, firing reaction, and its duration, time of recoil,

is a constant which is equal to the impulse of the round fired.

Let

= Moment of inertia about the point of rotation

- Torsional spring rate of suspension about point of rotation

= Impulseof round

- Trunnion reaction

= Time of recoil

= Effective lever arm of force F

= Total rotation resulting from firing

= Static rotation under load F

Assume No Dampening

= Rotation when reaction ceases or at time t

'I!

oo Cos w t

0 = 00-o

coswt = Oo(1-coswt)

00 = F9

0 = f_

cos wt)

Energy input

F R 0

Fn R2

En =

2 R2 (1-cos wt)

B3-1

--- Página 160 ---

At turn around, e rotation, all input will be in strain energy of the suspension.

En = 1/2 K 0 2

F2 R2

1/2 K

(1- cos w t)

e = 2 -/cosw

Imlo

t.-F

-FR

2(1

K m

Case II Suspension is locked out

Let

- Rotational acceleration

= Vehicle weight

L _.

= Rotation when reaction ceases

Since the angle of rotation will be relatively small,"h" and "a" can be considered as remaining

constant without appreciable error.

Then

= Fh- Wa

Fh- Wa

= 1/2 at 2

t Im

Fh- Wa

2i °

Energy input = Fh 0

At tum around P.E. 'I

W a 9

Let Fh 0= Wa G

o = Ph-0

Wa (Fh-Wa)

h(Fh

2I o

I2 mh

Fh -Wa,

210

FWa -

i 2mh

210

,II

133-2

____

-,.,

--- Página 161 ---

M109 motion caused by firing impulse as a function of recoil length.

Approximate parameters of the N' 09

Impulse of round

15,. .13 lb/sec

Weight-------

53,000 lb

Suspension spring rate

Fore and aft pitch - - - 27 x 106 lb-in /rad

Lateral ----

28 x 106 lb-in /rad

Moment of inertia

Fore and aft

Lateral

About c.g. sprung weight 187 x 106 lb in2

about c.q. sprung wt 36 x 106 lb

06 2

About rear corner

1204 x 106 lb in

about edge of track 365 x 106

Distance

Trunnions to ground 90 in.

c.g. to spade

102 in.

Trunnion to c.g.

36 in.

1/2width

62 in.

Case I active suspension

Firing forward

I! ~

(I _ Cos

T_.I

Im = 15483 lb sec

F =3.864 x 106

L = Recoil length

in.

R =36"

SK = 27x106 lb-in

o = 187x 106 Ibin2

/187x10

=7.84

2x 106 (386)

=7.46

(3.864 x 106) (36).

(7.46)(15483)(L)

e27

x 106 L

cos~ 3.813A x 106

5.152

2 ( 1-cos .03L)

rad

9 =

2 (1- cos .03L)

degrees

B3-3

--- Página 162 ---

Case I Active Suspension

Firing

Firing over the side

Recoil

Firing

Over

Length

Forward

The Side

-12 (1 - cos

G degrees

K 28 x 106 lb-in./rad

8.72

18.23

lo = 36 x 106 Ib in2

8.64

17.39

= /(28) (386)

1" 33

8.55

16.40

(3.864 x 106)(36) /2

(1 - cos (17.33) (15483) L

8.45

15.26

28x 10L

3.864 x 106

4968

'em4_

2 (1 -cos.0694L

rad

8.33

14.01

285

;i t

= L /2 (1 - cos .0694L

degrees

Case 1I Suspension Locked Out

Firing forward

Im'

210

Im = 15483 lb sec

w = 53000 lb

h =90 in.

lo = 1204 x1C)6

W = 53000 lb

a = 102 in,

F = 3.864 x 106

L - recoil lei,,th

e = (154832) (90) (386)

(2) (1204 x 106)

(53000) (102)

3.864 x 106

e = 3458 (1.66 x 105 - 2.59 x 107 L)

= .03458 (1.66 - .0259 L) rad

e = 1.98 (1.66 -. 0259 L) degrees

B3-4

--- Página 163 ---

Case 11 Firing over the side

Im2h

lo = 365 x 10l lb in2

a =62 in.

(15483)2 (90) (386)

2,59x 10-2 L)

(2) (365 x 106)

(53000) (62)

, = 11408 (2.74 x 10"5- 2.59 x 10- 7 L)

e = .11408 (2.74- .0259 L) rad

e - 6.54 (2.74 - .0259 L) degrees

Case II Suspension Locked out

Firing

Recoil

Firing

Over

Length

Forward

The Side

2.26

14.53

2.00

13.68

1.75

12.84

1.49

11.99

1.24

11.14

M109 Rotation from Firing a 15483 Lb/Sec Round

101

Firing Overt e

Suspension Active

V 2

"'Suspension Locked

2 --

Suspension Active

Firing Forward

Suspension Locked

Recoil Length Inches

134-S5

--- Página 164 ---

APPENDIXB84

[PACIFIC

CAR AND FOUNDRY COMPANY

NAME

_?ENGINEERING DEPARTMENT

NAME_

REFERENCE

DATE

Q'PAGE

OF_____

... .2- .1 74

5414-D

284B4-

-,.....

17Tc1174

PC-R-18 /B4

--- Página 165 ---

PACIFIC CAR AND FOUNDRY COMPANY

ENGINEERING DEPARTMENT

NAME

REFERENCE_

________

79______

PAGE ________OF_______

,U$-

2124,43 Pi

r~z~ ~C

144cs,

lucTc(4

Fc<77

\,J'r.t.d

.,, .

I Li t -A '?\

/67,//

/701457

PCF-RN-1284

134-2

(.~ 'r

--- Página 166 ---

PACIFIC CAR AND FOUNDRY COMPANY

ENGINEERING DEPARTMENT

NAME __________________REFERENCE

_______________

DATE

-79

PAGE_

.+rs

=U&2C"7

T'4 42,';

74LC

~(T-o74Wl4S)

I 4-- 2. 1

G )

III gen~t-I,

it t e

.uid

thatL (ir

kI,%h-~g of miliih -,~vm ii : y

ri t

ufj

ais' a

i*rv.

I (~\

,it

i.,

lII-: ved Il tha t

il betteri 11r

atiii l

-o me ava(J~

llQ

v;Ih

Its( of ,IwvII vur~ e' as inl Fig. 10 %%

ill jpimifi

rea.otiabdc

140TCH RADIUS. r. 14CHIrS

02 0

04i

14 iu

t o

I ,.

QUECHE

RAIS

284-3

fN-E

",-,R

MO N

NOTCH RAIA0US. t.tICHE

I ~~~

FG 10

-t",,o

illil

AEAE

NOTCH

IIVI

CURVES

PCF-RN-128A

--- Página 167 ---

PACIFIC CAR AND FOUNDRY COMPANY

ENGINEERING DEPARTMENT

NAME

REFERENCE

DATE_________

PAGE

OF_

___

Fa' 1&QF '5777. OF L1)QOOCHfEro5t

,f~crc

.......

-fig. 3 Comparison of constant-Iifotimo fatigue behavior of notchod and unnotchod spocimans

n G

0 2'

I IN

C--

. \

,--

....

I "

'. , .; ../

4,]

,,~. ,,(

C o. I'Ot

, flaei

igue

for AISI.SAE 4340 alloy %leel (bar), hardened and erl ,erent o ln

.te'tQ

f ) 035 MPQ (150 k

n.s iepcent dlua oblanod

reom wrnrolthed %p.tsmnen, dathed lone, represent dlu

train

ec- m n% Kha,,, 9  nalchet w-th K.

PCF N-28

134-,---4

--- Página 168 ---

:1 ~PACIFIC

CAR AND FOUNDRY COMPANY

ENGINEERING DEPARTMENT

NAME

______________________________________

REFERENCE

aDATE

PAGE

OF ___________

fJ(/7IV

(57.d('

+4J

oI)

li.

. .ft-

wI*I

g/. (2I12.443>

643,I

p5/I

4!)410 5Tt~-j

/5D/l-

&.t'

PA6E 2 (-.v

OSH zA~

' i Eli,

PCF-RN-1284

B4-5

--- Página 169 ---

PACIFIC CAR AND FOUNDRY COMPANY

ENGINEERING DEPARTMENT

NAMEI

REFEREC

__________

DATE

__PAGE

__OF

42.

2ol- Q7ce

4?2Yi

FaCE C-6-rJc ARE4-(

lK"Z6o--j-0l3

lIT ~

VIIL 7-(7t-( /tO G 77f/(J 01U(G

72e

Is r- Y011)G -Vie Lo-lD 7HE12 e /~ A-

14(-

ITP4r ML

O~ELP '5PPe;Af, 77te 164 L CYL)U T(4

PCF-RN-1284

834-6

--- Página 170 ---

I -

PACIFIC CAR AND FOUNDRY COMPANY

NAEL4

ENINEERING DEPARTMENT

|tt

DTE

/"-/-P-AE

(a)

(b)

(c)

FIG. 97

NUT DESIGNS FATIGUE TESTED (WIEGAND)

(FLOW LINES-HELE SHAW METHOD)

In the arrangement shown in Fig. 97c the transmitted load is not rersed. Fatgu tets showed

fatigue

trength more than double that of the standard bolt-and-nut combination (Fig. 97a).

Uidt

face of nut

TL)7~A1OO~ 6A

Conventional nut:

S__-

....-------

7700 /wIj (3t47r ?OT

/)CL)

....

___.._

_________

-.......

UTTYA)

L,0 i

T-,.)eot cu, .

Loaded face of nut

4 1,.....

...

Stiess concentrtion factor

STo bolt htd

/,r Ar

( .

The highest loaded threads are those closest to bolt head in

normal design Nexi drawing shows how load can be evened

Pfshiur

Product Engineering, December

1977

PCF-RN-1284

--- Página 171 ---

PACIFIC CAR AND FOUNDRY COMPANY

ENGINEERING DEPARTMENT

NAME

REFERENCE

DATE____________

PAGE_

z"--

/ATxC4

R1//o& g CW.I. t 1 Fo-O i?at/

D8r& <r)U5,

oo )

I9)r(O~~~)-PI

..e'//T/9-&_

1777 7'

',,

PCF-RN-128

84-8

84-8

--- Página 172 ---

I~ ~

b:-

CDC>~~~\-~

~-''

U~p

4u I

--- Página 173 ---

TAxLz XIV.4.-Tolkrances on Buttress threads, class I Uree)

Threads per inch

Tot on

majo dia

of tit

MaJor diameter

Prctcrred diameters

2throa08d

413

Totranca on pitch diameter, extenal and Intenzi threads

,b.

in.

in.

in.

inb.

W is.

In.hr

to 1 ....... K 4

10.51L

IN&-......-

....

D50

'He~ ~

~ ~~~I

toI.....................ai':::::::::

::::::

"°°*:°''°° ....

*,"

'**-I'

....

°*1-0-

-204

2,34.........

09 .010

.........

..........

I to 0 ,4

......

IK M.041M...

. .... ....... ......

0107o

.01

.012 0

018

...... .......

....

.. .... ....... .. . .

...

- ----

1 o2;6.....

4MA4.8.1M6......... ..........

013 .014

.013 .016 .011 0.001

* 08

2%to 4........

32.3,3 4 ......

... .......

.011

.012

6 0130

.0140

.0150

.0174

.............

.......

.......

........

.060

41tot ....

141,4

........

0133

.0143

.0137

.016"/

.0181 10.0'201 ....... !....... ....... . ..... .......

.011

.to.

7...

...

0142

.0152

.0106 .0176

.0100

.0310 0.02=4 0.0243 .....................

0100

10to1 .......

11.12.14,10

0163

.0176

.018"

.0200

.0220

.0235

.0254 0.0282 0.0303

At to

16 t1o24. ........

0173

.0187

.0197

.0211

.021 .

0246

.0 5 .0293

.0314 0.0341

.0LIO

for measurement of thread angles and pitch they

INTERNAL

THREAD

(NUT)

should be held to close limits; see tables XIV.2,

XIV.3, and XIV.4.

(c) Tolerances on minor diameter of external

thread and major diameter of internal thread.-It%

will be sufficient in most instances to state only

MIN,"

the maximum minor diameter of the external

s MA/

thread and the minimum major diameter of the

internal thread without any tolerance. However,

fl".

the root truncation from a sharp V should not be

greater than 0.0826p or less than 0.0413p.

7. MI

mUM CLEARMNCES FOR EASY AssEM-

BLY.-An allowance (clearance) should be pro-

secure easy assembly of parts. The amount of

the allowance should be deducted from the nomi-

nal major, pitch, and minor diameters of the

.M,+

external member in order to determine the ma:zi-

mum metal condition.

The minimum internal thread diameters will be

basic.

111

IoII

The recommended allowance is the same for all

' "

three classes of thread and is equal to the class 3

(close) pitch diameter tolerance as calculated

EXT6RN4L

THREAD

(SCR1EW)

under par. 6(a), p. 29.

The allowances for various

Fiouaz

iV.2-Illusiradon o tolerances, allowances, and

combinations of pitch and diameter are given in

Fool

trations, Buttress threads.

table XIV.5.

The disposition of ailowances and tolerances is

2-pit

dizetor allowance on exterm thrad

indicated m figure XIV.2.

a-toot tunstioa

TAnLE XIV.5.-Allowances on external Buttreu threads, at cluaes

Tbrads per Ich

USja*o

diameter

Prefrd diamneters 20

f[-[2

4 1 3 12M

21 17 ,1 1

Allowsancn majo, minor, and pitch diameters

in.

Iaia

n. inL. In.

in.

In.

in I

n I

in.

n. I

inaL.

4to'H ...........

id. +,'14 .....

~ m t~oe ..................

003

400.044I

;4 tol ...............

.000

.............

......

0460.0040.....................

..... .......

.......

.......

".....

to 1 ...............

-I,114..............

0043 1.0048

.0051 0.0055 0.00O1 .......

.......

.............. ..................

141t21

4............i

...

2,4...................

1.0 05 0050

.0053

.0058

04 0.0066 0074..........................

2M to4 ................. 34.&39,4 .....................

.0053

.005 6

.0001

.0067

.0071 .0077 ..................... .....

............

4o6 ...................

4,5,, ..............

. ... .

006 .009

.0064

.0070

.0074

.0050 0.00

.................................

6to .............

7..

10. .................

003

.006 .0074

0078

.0093

0.0100 0.0108................

10to 16 ..............

1.. ,

...........

...

0066 1.0072

.0078

.00 .00"098 .0104

.01

0.0126 0.0135.

16o 24.............

A8 2Z24.............. ............

77.

....

0063 .0088

0 4

0103

0109

018 .

:0130

.013

0.01,

Screw. Thread Standards for Federal Services,

U. S. Department of Commerce. National

Bureau of Standards, 1966, Handbook H28

S(1957) - Part IlI

B4-10

--- Página 174 ---

678/Service Characteristics

chenges produced in the ultimate ten.

Fig. 24 Sfer

of fatigue limit deft

sile strength and the hardness. if the

ductility change is also measured and if

Tons." nsquo, W

the qualitative effects of various pro.

24 ,cesses

on different types of metal are

known, more refined estimates of the

- 110

change in fatigue behavior can be made

without resorting to extersive fatigue

:,1,

lotesting.

Fatigue life may be estimated by in.

-gay

sorting a calculated strain amplitude

and the appropriate materials parame.

.ters

from Table 3 into Eq 4, solving for

soo

Nf. Where deformation is purely elas-

tic, a calculated stress amplitude and

----------

Eq 2 may be used. The calculated fa.

Approzxhu-ty ION

m.I hes

tigue life must be adjusted to compen.

sate for stress concentra. ;ons, surface

Ifinish

and the presence of aggressive

800 ~l

stllth We010620

environments, as described in Fig. 7

Tenl4e I

eniro

nd Ref 2. Alternatively, the calculated

Survival after 10 million cycles of ASI-SA| 4340 steel

with tensile strengths of "S, 1320,

stress may be adjusted by using stress

and 1840 MPa (144,191, and 267 ksi).

Rotating-beam fatigue spciens teted at 1O000to

concentration factors such as those in

1 6000

rpm. Coffic1nts of variation range frm 0.f17

to 0.20.

Ref 9 and 10. Any of these calculations

0neinclude

the assumption that the loading

is fully reversed (R -

- 1).

value of b maybe -0.1. If the steel has tigue parameters may be found in Ref8.

Potter (Ref 11) has described a

been severely cold worked, the value of

Estimating Fatigue Life. Design-

method for approximating a constant,

b may be - 0.05.

ers of machine components that will be

lifetime fatigue diagram for unnotched

For a fatigue life of more than a mil-

subjected to cyclic loading would like to

specimens. Using this method, a series

lion cycles, the use of these parameters

be able to predict the fatigue life from

of points corresponding to different life.

in Eq 2 provides a slightly lower esti- basic materials parameters and antici-

times are calculated and plotted aloug

mate of fatigue limit than the fre-

pated loading patterns. However, the

the diagonal line on the left side (R =

quently used rule of thumb that the fa-

scatter of fatigue data is so great that

- 1). Each of these points is connected

tLigue limit is half of the ultimate tensile

the likelihood of accurate predictions is

by a straight line to the point of the

strength.

extremely low. The methods and ap- other diagonal (R -

1.0) that corres

The fatigue ductility coefficient, e, is

proximations in this article and Ref4,7,

ponds to the ultimate tensile strength.

approximated by the true fracture duc-

8 and 12 can provide some indication of A comparison between the estimated

tility, ef, which can be calculated from

fatigue life.

constant-lifetime diagram and the ex.

the reduction in area in a tension test

In a particular situation, assessment

perimentally determined diagram is

of the seriousness of fatigue is aided by

given in Fig. 26. The calculated lines

- af =In

100

(Eq 6) knowledge of the cyclic strains involved

correspond well with the experimental

in fatigue at various lives. These gener-

hines. Generally, the predicted lines

(TO-0alizations

are useful guidelines for duc-

represent lower stresses than the actual

Typical values ofe ican be approximated

t'1e steels:

data. Estimating fatigue parameters

from the Brinell hardness number as

from the Brinell hardness number pro-

follows: ,is 1.0 for HB less than 200;

1 If the peak localized strains are con-

vides more conservative estimates.

is 0.5 for HB between 200 and 400; , is

pletely reversed and the total range

These results are only approximations,

0.1 for HB greater than 400. e'should be

of strain is less than

5/E, fatigue

and the methods may not apply for ev-

calculated from %RA rather than using

failures will occur in a large number

ery material.

these approximate values, if possible.

of cycles or not at all.

Cumulative

Fatigue Damage.

The fatigue ductility exponent, c,

has 2 If the total strain range is greater The data presented in this .rticle, and

approximately the same value (- 0.6)

than 2% (amplitude -1%), fatigue

most other published fatigue data, were

for most ductile steels. Severe cold

failure will probably occur in less

obtained from constant-amplitude test-

working may reduce the value of c to

than 1000 cyles,

ix-,g; every load cycle in the test is iden-

- 0.7; annealing or tempering at a high 3 Part configurations that prevent uti-

tical. In actual service, however, the

temperature may raise c to about

lization uf the ductility of the metal

loading can vary widely during the life-

-0.b.

or metals that have limited ductility

time of a part. There have been many

The elastic modulus (Youngs mod-

are highly susceptible to fatigue fail- programs to evaluate the cumulative

ulus), E, is the slope of the elastic por-

ures.

effects of variations in loading on the

tion of the uniaxial stress/strain curve.

In the long-life fatigue region, the

fatigue behavior of steels. References 3

For most steels, it has a value of about relative magnitude of the change in fa- and 11 through 13 describe methods of

200 GPa (29 x 106 psi). Further infor. tigue strength due to processing may be

analyzing cumulative damage. A few

mation

estimating

these

fa- crudely estimated by the relative

overload cycles can reduce the fatigue

Metals Handbook, Ninth Edition,

American Society for Metals, 1978, Vol. 1

B4-11

TIM

-11-'sw

--- Página 175 ---

APPENDIX C

Engineering Drawings

~ I

_____

--- Página 176 ---

-4Z

'F--

_____

'it;-

LL'

_______________________

~~~1~~

1~EkL

/ -

IF K

''%

aE1~&-

-*1

- - -

,// /

--- Página 177 ---

(.-.

14-7

2~~

r$6-D

I.-.{

411

ToP

'Ie&.2J

4'~L

pap

Ji~t

I~IAhm

LaI

-01'

VAWI

&AM PWOWCINA

--- Página 178 ---

--- Página 179 ---

IVI

-t-

24- ..

±-lK

IOUI

liin

I4.-&

Samat~s

CU&L-IA1

'-147w

CIM&M

T9.e4I

OruC-1.

Sa js

eMSsho

apof

e~tUAT114- bTMQ

/IJZ-hE

EO~SA U

--- Página 180 ---

I ~

M£WOFJ4iE

L---

JL------4

--- Página 181 ---

&QN

(ftF)

I"f47

T--j

1444

Pegsv C

PRtOPOSAL

AUTO LOADER

LAVQ T, AILS.

v-AGWIC

CAM AND=.ga

C064&

--- Página 182 ---

Latam

DWV

LD7

PAXRlm~~Gm~R@I. fa

msIrP

Q~~~

Lli&2p

A 22f

LPFT

--- Página 183 ---

7brou7

KEA~r

--- Página 184 ---

0 I

I I

E30E3

(Shoot 4 of Q!'

Page C,4

___

___

___

___

__I

A07-0O LOADMR

[ ~~

... W6..3-.".+T:

..2 smr...

:41

--- Página 185 ---

~~1.Z

L.L

ILI-

'2:---L2

____

:75i

k3,N

--- Página 186 ---

-46

........

.,-t o 0-.

.25

a2AYL

.d47

--- Página 187 ---

p-1l

Dra

-7-z1

--- Página 188 ---

1 ss'C

.4d

f.41

7~~T~jT

"wk

1-~~3-

4--1

--- Página 189 ---

~~-T

- .5 0

6kxa~:

tmttl

4%-' CO

TMW

*WU 1-

T"MV.C1

P&aO

Mi4%

_A0

Fc"

LIZ

~.-F~C-/

Pop C-

PAS0C

O PU-WPN

--- Página 190 ---

IAr-.000

,-0

,Z I

zu/o

?ON

CAI26

TIlI

-~~~

00R Z~M

M1PL

I.p

1*s

5ilm

qAz%%.q

\1.2S

w &S fR Ms"54

1 1-.32114-

Io'

S"04

fti

%3"-

VALVER~

-~bq

ms"14

6"I

ft_

_____

/S$t-4

--- Página 191 ---

S r

400

DCTAIL ORIIVICE .

I~12

IL4

.I2

'141

234.10

*- a

4.U

'Ll

--- Página 192 ---

Opt!

I s

fs'I

WO__

-lAt

I-'-

'4.1

____

___

____

2-WM4WA

.4 V

oj~

--- Página 193 ---

(-7

____

'4-

~-.

__________

-4---

,<~'

-.---

w ~

p*.-~ ~

________________

-4.

COJJ~

4-.

4'~ '"7

~*44.,

4.--

-i-

-~__

~4u

--- Página 194 ---

~21

4' ________________________

7/.

A I

.~rn~

'wac Caft -

i~5MM

MOOtJLAR

~WCL~L. ~~VIIW

K ~

--- Página 195 ---

6"0

KtU

% S

V ZS46

-A~~

42C

j3L-

ss*

-4~~~

1; 0

~ * 4 * *

M--I q

400

wAM.

L2Lao

4 a

4~ ~ ~

is#i

YCA

#.t

--- Página 196 ---

LED

L4P

X ACW-5Z-.1 47

'N~c-WMs7,044s-q

RAf aV

12E

biU4

)00a

;izr

{rs~

4.IO

/brewin

C-3u

CACAII

OCA)Qpjja

As 34-Q

ICOO

PL~I

ee K

of2)

p aa, pt.

--- Página 197 ---

OAA

I Au

t ~A

WIE

1)lKIc PON 01

nIIIA

HItlItr

vlAwJI

M~l ~iAL

MU'...

'WKINGI~i

Hi4Ai;T,

A'Am Aabe.

'roLIHAN(0

ON~ Alt

IVA 1A(U

LALII1,

IOL1 1RAWLE

ALL

THlk

MLSt

I k

'.4li-'l

--- Página 198 ---

1IFT

I(Aluill

THIS L tNUi

18,l

DrswklgC4

WiVO114I

SSWSCP

opc-

040.A 0-1-1

PACIFIC CAR AND FOUNDRMYCO

tL 5U

-uM

w~b.9O

SUi NOU

so*.me~

NSA?7

80.1

1[fli ~%,of

5(V"

--- Página 199 ---

K44IN

-CML

-----

'"--

u~L~elomnrnwia

FINAL PRIMERV

FINISH

--- Página 200 ---

BILL OF MATERIAL

tow

..o -kH

&egoI fcAyDNI

wo.

N.4

Dr&Aq C-6

polp

Ducito-rio

.4~d4

LC.REVISIONS.4~

cmas/ OP

01.,.

AIFCCR N OUDYCOPN

W"_

ENO.WAHNO

A2MI" O

___VR

Pilo=

.0.J PXTIG

m m

0 .A --'DL

SIZI

- 4

(5tELPa

MoQIQP

MILLWASIED ScAI-

D SRI

UTION

--- Página 201 ---

dof

w -w

BLEKJ D

&15R-

D .0_

UN~LSOTNIRWISspecaao

HEAT TREATMiENT

FINAL PNOThLCTIY FINISH

PA l~cfl,

--- Página 202 ---

BILL OF MATKIAL

A'I

sL.ig

ORIN

lNRY

COPAN

A OF

4& I

~-1

-aK$V

NTW

Drawin Of

--- Página 203 ---

,--,

_I--2

.... i

- -

.. .

--- Página 204 ---

L W

-;-~

-------------

......

--- Página 205 ---

____________________________

.a~.

~*~?M~44e,

I~1

LtT85

k~XIoL SCtSsj$

I'II

-'- A

_____

CtYM p'

- -

---

5 ti .~kshB

~JJ

V~L't.

--- Página 206 ---

--- Página 207 ---

MOW

Laou

D-.RtrIotPie

Fee

rehCoe

''K~KK\SCALE&

Kno

rw"

... ,,o

--- Página 208 ---

\\\\T

\\\CPP

SUMVtUMW.-

--- Página 209 ---

\ X

Layout D-2. Rotary Bolt Primer Feeder -

Breech Open

00,~

--- Página 210 ---

~II~ If

--- Página 211 ---

OCR;

Layouw D-3. 60-Round Primer Drum j