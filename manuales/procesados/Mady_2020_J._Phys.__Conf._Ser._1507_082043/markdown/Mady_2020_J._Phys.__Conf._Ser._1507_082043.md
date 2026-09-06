# Mady 2020 J. Phys.  Conf. Ser. 1507 082043

*Documento procesado el 2026-05-18 18:28:30*

---

--- Página 1 ---

Journal of Physics:

Conference Series

PAPER • OPEN ACCESS

Modelling and Production of artillery firing-tables:

case-study

To cite this article: Mohamed Mady et al 2020 J. Phys.: Conf. Ser. 1507 082043

View the article online for updates and enhancements.

You may also like

Research on Ammunition Simulation

Method

Sun Yong, Li Jun and Fan Kaijun

Stochastic evolution of projectile motion

during artillery exterior ballistic

Wang Mingming, Yang Rongjun, Chen

Hongbin et al.

Research on Evaluation Methods of Firing

Precision of Trajectory Correction

Projectile

Xieen Song, Min Gao, Yi Wang et al.

This content was downloaded from IP address 181.210.24.4 on 29/04/2026 at 07:24

--- Página 2 ---

Content from this work may be used under the terms of the Creative Commons Attribution 3.0 licence. Any further distribution

of this work must maintain attribution to the author(s) and the title of the work, journal citation and DOI.

Published under licence by IOP Publishing Ltd

The 2020 Spring International Conference on Defence Technology

Journal of Physics: Conference Series

1507 (2020) 082043

IOP Publishing

doi:10.1088/1742-6596/1507/8/082043

Mohamed Mady, Mostafa Khalil, Mahmoud Yehia

1.  Introduction

During the preparation of firing table, it must be specified that there is a representative firing

conditions, which is known as the standard firing conditions. There are many factors affect the flight

trajectory, including artillery, projectile, meteorological data and other factors. During real firing, these

factors are varying, where it is impossible to specify the actual firing conditions for each shoot, which

cannot meet the operational requirements of the firing table. Therefore, the actual firing conditions and

standards are not consistent. Therefore, standard firing conditions including standard meteorological,

ballistic, and Earth conditions are specified, and hence, the effects of these deviations are corrected. In

order to precisely construct firing tables, more than 200 thousands flight trajectory simulation are needed

through final phase only [1]. In case of medium range projectiles, the average flight time is

Abstract. Projectile firing accuracy is an important artillery issue to increase killing probability

with minimum number of rounds per target.  This can be achieved through constructing a firing-

table (FT) with both standard and non-standard conditions. Therefore, lot of rounds need to be

shoot for different target ranges as well as meteorological conditions to increase such firing

accuracy. Developing an accurate computational FT prior to shoots has the advantages of

minimizing the cost and providing preliminary prediction of dispersion. In this study, a

computational FT algorithm has been proposed based on the modified-point-mass projectile

trajectory model for solving the ballistics problem. A flow-chart is proposed to illustrate the FT

production levels and the corresponding procedures. A case study for 155mm-M107-HE

projectile is utilized. In order to validate the proposed algorithm, a comparison has been

implemented with results obtained from the well-known commercial package PRODAS. Finally,

based on real firing data available including the corresponding meteorological conditions, a

provisional firing table has been developed.

Firing tables are the basic document necessary for military combat training and shooting

specifications. Without firing table, the effective shooting cannot be performed. Firing table provides

the basic data, the shooting deviation correction data, and related data required to command the shooting

and obtain effective artillery accuracy. Historically, firing tables were developed continuously over a

number of decades. Due to its simplicity, Siacci method were used for computing trajectory problems.

In 1917, the French Short Arc methods were implemented to compute such trajectories by Sandy Hook

and Aberdeen. Numerical integration methods had been introduced by Aberdeen during 1918 to

accurately solve the trajectory problem and hence, firing table calculations.

Email: mostafa.samir@mtc.edu.eg

Aerospace Engineering Department, Military Technical College, Cairo, 11766, Egypt

Modelling and Production of artillery firing-tables:

case-study

--- Página 3 ---

The 2020 Spring International Conference on Defence Technology

Journal of Physics: Conference Series

1507 (2020) 082043

IOP Publishing

doi:10.1088/1742-6596/1507/8/082043

approximately 50 s and hence, approximately two days processing time for normal computer are needed.

In 1943, U.S. army developed an electronic device called Electronic Numerical Integrator and Computer

(ENIAC) that capable of computing new artillery firing tables up to 1000 times faster than any

previously known computer [2]. Different researchers [1, 3-6], proposed the procedure for the

processing of measured data available from real fires to produce a provisional table as well as final firing

table. Drag and lift factors can reduced by comparing the ballistics parameters computed with the

measured ones through fitting process. A graphical firing table mathematical description has been

illustrated [7, 8], where the firing parameters as azimuth and elevation angles  are obtained based on

standard and non-standard conditions. Developing a firing table software can be presented in various

configurations based on model complexity starting from point-mass model [1, 3] to six-degree-of-

freedom model [9], projectile platform as ground-launched [1, 9-11] or air-launched [12], and nature of

meteorological data available [1].

However, with the modernization of the war, the direct use of the firing tables is gradually reduced.

Instead, the fire control system is used to automatically, fast and accurate solution of a set of shooting

conditions to obtain the needed deviation correction. Therefore, an accurate and fast trajectory model

could be developed [12] instead of the well-known six-degree-of-freedom.

In this study, a procedure for developing firing table of high-explosive spinning projectile is

illustrated. This research paper is organized as follows, section 2, illustrates the development procedure

for ground artillery firing table including trajectory model, standard firing conditions, and the definition

of every column through basic and correction tables. The implemented case-study is presented, and

finally, results and discussion are illustrated in section 3.   In section 4, our conclusion are listed.

2.  Methodology

Initially, firing table accuracy is based on the utilized flight model complexity and the number of rounds

to be shoot. Construction of FT can be divided into three main phases as, construction of the preliminary

FT using a suitable flight model and projectile data available through research and development R&D

phase. After achieving the technical and operational requirements of the developed artillery system, a

number of field experiments are done to construct the provisional FT which helps to good estimate the

projectile impact parameters during the production of final FT, which needs large number of shoots

through different elevation angles.

Trajectory Bundle Gen

of elevation angle QE

instead

fixed step value

with

set FT key to Range

Linearly interpolate to

key

muzzle QE

trajectories for range of

Generating

different

DATA INPUT

elevation angle QE

and Max

Min

Standard conditions

Muzzle velocity

Aerodynamic coefficient

Mass properties

Differential Effects

Perturbation Model

model

MPM Trajectory

1962

Standard Atmosphere

Atmospheric Model

Figure 1 . Projectile Coordinate System

and Ballistic Directions.

Figure 2 . Flow chart for the

development procedure of computation FT.

--- Página 4 ---

The 2020 Spring International Conference on Defence Technology

Journal of Physics: Conference Series

1507 (2020) 082043

IOP Publishing

doi:10.1088/1742-6596/1507/8/082043

 V V V

(1)

ρva C

ρa C v

ρa C

R 

(2)

Where,

ref 2

ref

; V is the projectile velocity vector in earth fixed coordinate;

Vt = (V −W) is the projectile total velocity vector with respect to air speed W; v is the projectile total

aerodynamic speed;  is the air density; m, d, and Sref are the projectile mass, reference diameter and

reference area respectively; and the coefficients CD  ,

CL  , and

p  are the aerodynamic drag,  lift,

and Magnus force coefficients respectively.

For symmetrical spinning projectiles, the projectile spinning rate can be obtained using

d v

ref

(3)

Where, Ix is the projectile axial moments of inertia, Cl

p is the aerodynamic spin damping moment

coefficients and the projectile initial spin rate can be computed by

po = 2π. vo

η. d

(4)

Where,  is the rifling twist rate at gun muzzle and vo is the muzzle velocity.

The projectile repose angle aR is defined by,

d v C

I p

ref

(5)

And, the gravitational acceleration g is given by

. 0

(6)

Where, g = 9.80665; and Re is the average radius of the earth (= 6370 km).

2.2.1.  Standard Meteorological Conditions. To determine the atmospheric conditions at zero altitude

(sea-level) as air temperature 𝑇𝑜= 15°𝐶, pressure 𝑝𝑜= 760 𝑚𝑚𝐻𝐺, and density 𝜌𝑜= 1.225 𝑘𝑔/𝑚3.

Standard atmospheric conditions as function of altitude are based on U.S. standard atmosphere 1962

[14]. It has been concluded in [15] that using standard atmosphere is acceptable but sometimes a more

realistic model defining a particular area of the globe is needed specially those areas have very low/high

altitudes compared to sea-level. Finally, the wind speed during whole trajectory is assumed zero.

2.1.  Flight Trajectory Model [13]

Due to the complexity of rigid body 6-DOF trajectory model, a modified point mass (4-DOF) model has

been utilized referred to earth fixed coordinate (X1, X2, X3) as shown in figure. The point mass motion

of the projectile was modified to include projectile Magnus effect, axial spin and an estimation for the

yaw of repose, where the projectile epicyclical motion was neglected. The projectile center of gravity

equations of motion based on the modified point mass model are

2.2.  Standard Firing Conditions

During the preparation of firing table, it must be specified that there is a representative firing conditions,

including:

--- Página 5 ---

The 2020 Spring International Conference on Defence Technology

Journal of Physics: Conference Series

1507 (2020) 082043

IOP Publishing

doi:10.1088/1742-6596/1507/8/082043

2.2.2.  Standard Ballistic Conditions. Include table standard projectile weigh value. Although due to

production errors, the projectiles weight is not the same, where they values obey a normal distribution

with a mean value named as standard weight value. The projectiles weight greater/lower than the

standard value are divided into squares with the sign +/, where firing data are corrected according to

the number of signs on projectile. The standard charge/propellant temperature is set to +15C. For

standard projectile weight and charge temperature, the projectile muzzle velocity will change with

howitzer shooting number, namely for a certain gun, as the shooting number increases, the velocity will

slowly change [16]. Therefore, a standard muzzle velocity value has to be measured from a standard

gun.

2.2.3.  Standard Earth Condition. In the Earth’s inertial (non-rotating) coordinate system, the Coriolis

acceleration and the centrifugal acceleration are zero as illustrated in equation (2).

As illustrated in Fig. 2, for known case study design parameters and nominal flight conditions

(including standard atmosphere) , number of flight trajectories parameters can be generated for given

range of minimum and maximum elevating angles QE (namely, trajectory bundle generation) with step

value  ∆QE. It’s required to set FT-key-value to be the resulted ground range instead of QE, therefore, a

linear interpolation will be utilized to obtain the equi-spaced range values and other flight parameters as

Basic data table. Finally, based on perturbation model, the correction parameters needed to compensate

the impact of non-standard firing conditions is reduced as illustrated in 2.3.2.

Table 1 Firing Table “Basic Data” Columns Definition

No.

Unit

Definition

Range, the resultant ground range (sea-level) as Rstd = √X1

2 + X3

mils

Elevation angle QE, the gun QE corresponds to required ground range.

Fuse setting FS for graze burst, time to be adjusted to have burst earlier to ground impact

as in case of air burst.

Change in fuse setting time ∆FS for 10 m decrease in fuse height burst.

Change in projectile range for 1 mils change in elevation angle, ∆R(1mils).

mils

Fork, the change in the elevation angle necessary to produce a change in ground range

equivalent to four times the range probable error, 4.

Time of flight, TOF.

mils

Azimuth correction due to drift AZstd, the change in the traverse angle needed to discard

the effect of drift in case of spin stabilized projectiles (drift must be compensated to left

in case of right hand twist barrel).

mils

Azimuth correction due to cross-wind AZCW, the change in azimuth angle needed to

compensate for 1 knot cross wind either from right or left, where the correction azimuth

angle is opposite to wind direction.

2.3.1.  Basic data, it consist of 9 columns as illustrated in Table 1. All trajectory parameters are

calculated at standard conditions.

2.3.  Artillery Computational (Preliminary) Firing Table Model

Preliminary firing table are consist of different columns in this section we are going to speak about each

column characteristics, definition and the equations that enables us to have this column. This preliminary

firing tables consists of basic data and correction data.

--- Página 6 ---

The 2020 Spring International Conference on Defence Technology

Journal of Physics: Conference Series

1507 (2020) 082043

IOP Publishing

doi:10.1088/1742-6596/1507/8/082043

2.3.2.  Correction data, introduces correction factors which are needed to account for nonstandard firing

conditions as a unit increase or decrease to some flight parameters through columns 10 to 19 as follows,

- Column 10 and 11, represent range correction ∆R∆vo in [m] due to decrease/increase in projectile

muzzle velocity as ∆vo = ±1 m/s  resulting new range Rc = √X1c

2 + X3c

2 . It will be added to

compensate the deviation in muzzle velocity from the standard value, where

∆R∆vo  = |Rstd −Rc|

(7)

- Column 12 and 13, represent range correction ∆R∆W in [m] due to head/tail range wind as

∆W = ±[1

0] knot resulting Rc.

- Columns 14 and 15, represent range correction ∆R∆To in [m] due to increase/decrease air temperature

(at sea-level) by ∆To = ±(0.01 To) which will affect the sonic speed and resulting Rc.

- Columns 16 and 17, represent range correction ∆R∆ρo in [m] due to increase/decrease air density (at

sea-level) by ∆ρo = ±(0.01 ρo) which will affect air drag and resulting new range Rc.

- Columns 18 and 19, as projectile weight deviated from its standard value by ∆m resulting Rc, where

one square represents ∆m⊡=

0.02

3 mo.

3.  Results and Discussion

∆P = PFT −Pest

(8)

Again, as seen in Fig. 6, both results obtained have the same mannar with tabulated data.  The range

error resulted due to 1knot head/tail wind are illustrated in Fig. 7 and Fig. 8. But in case of the change

2.4.  Provisional Firing Table Model

Through the second phase of the FT production procedure, real shoots will be utilized to improve the

computational-FT accuracy as a provisional FT. Therefore, data for three elevation angles QE are

collected corresponding to minimum, medium, and maximum ground range which can be implemented

through the R&D phase. These data includes, projectile, range, drift, maximum altitude/flight time, and

the corresponding meteorological data. This type of data is mandatory for the development of this and

next step through construction of FT. Hence, the provisional FT is a good estimation for the weapon’s

range-elevation relationship to carry-out firing tests through the final-FT production phase. A

meteorological data has to be measured before firings and to be updated every hour. At the end of

experiments final meteorological observation has to be obtained [1]. In this paper, a computer program

has been developed to assess the relationship between range and elevation with both standard and non-

standard conditions. In order to fit the simulated and real shoot under same meteorological data, three

main factors have to be iteratively estimated namely ballistic coefficient BC, lift factor fL, and Magnus

force fitting factor QM as defined in [6].

3.1.  Case Study and Model Validation

Through this study, a case study has been selected to be 155mm-M107 HE projectile. The corresponding

mass properties and aerodynamic coefficients, which are calculated using the commercial package

PRODAS, are listed in [17]. In order to validate the proposed model, a comparison between the produced

FT using the proposed model and the one produced by PRODAS has been implemented. All results Pest

are based on the deviation from the approved published 155-M107 firing-table parameters PFT as

As illustrated in f i g u r e  3, the estimated elevating angles QE using the proposed model is

outperform PRODAS results.  In case of flight time error ∆TOF, it has been noticed much close

between the two curves to have maximum error at maximum range as 2 s less than the tabulated value.

Fig. 5 shows the the estimated drift error due to projectile spinning, where the proposed model has

better accuracy than  PRODAS with maximum error less than 1 mils through all tabulated data.

--- Página 7 ---

The 2020 Spring International Conference on Defence Technology

Journal of Physics: Conference Series

1507 (2020) 082043

IOP Publishing

doi:10.1088/1742-6596/1507/8/082043

Fig. 5 Drift error due to spinning motion

Fig. 6 Drift error due to cross-wind

MODEL

PRODAS

[mils]

column

QE error

18000

15000

12000

9000

6000

3000

-10

-15

-20

-25

-30

-35

-40

MODEL

PRODAS

[s]

column

Flight time error

18000

15000

12000

9000

6000

3000

0.5

-0.5

-1.5

-2.5

MODEL

PRODAS

Range[m]

[mils]

column

Drift error

18000

15000

12000

9000

6000

3000

0.5

-0.5

-1.5

MODEL

PRODAS

Range[m]

[mils]

column

Drift error dut to CW

18000

15000

12000

9000

6000

3000

0.02

0.01

-0.01

-0.02

-0.03

-0.04

-0.05

-0.06

in air temperature by 1%, the estimated range deviated from the tabulted ones as shown in Fig 9 and

Fig 10.

Range[m]

Fig. 3 Elevation angle QE error.\

Range[m]

Fig. 4 Time of flight error .

3.2.  Problem description

As illustrated in section 3.1.  the accuracy of the developed computational FT is well enough compared

to the approved and published 155-M107-HE firing tables. Therefore, to have a realistic engineering

problem through the development of provisional FT, different aerodynamic coefficients (i.e. baseline

projectile) have been used in order to simulate the status of new projectiles development. In this study

we choose the 105-M1-HE as baseline, where its corresponding aerodynamic coefficients are listed in

[13]. A comparison has been illustrated between the aerodynamic coefficients for both 105 and 155mm

projectiles as shown in Fig. 11-13. According to lift force slope and Magnum force coefficient, a big

difference has bene observed. Only two shoots groups from past experiments have been collected as

--- Página 8 ---

The 2020 Spring International Conference on Defence Technology

Journal of Physics: Conference Series

1507 (2020) 082043

IOP Publishing

doi:10.1088/1742-6596/1507/8/082043

QE = 141.4 and 743.2 mils. Every group consists of seven projectiles. Average projectile mass for each

group has been collected. A meteorological data had been measured once before firing including air

temperature, pressure, humidity and density, and wind speed and direction. The projectile muzzle

velocity had been measured for each shoot, and hence the average velocity for each group were obtained.

As shown in Table 2, other measured data including down range and drift are illustrated.

Fig. 7 Range error due to 1 knot Head-wind

Fig. 8 Range error due to 1 knot Tail-wind

Fig. 9 Range error due to ∆To = +0.01 To

Fig. 10 Range error due to ∆To = −0.01 To

Table 2 Firing data collected for the two groups

Group no

𝑣o [m/s]

𝑚avg [kg]

𝑋1 avg [m]

𝑋3 avg [m]

141.4

690.3

42.664

7943.2

27.2

743.2

692.7

18075.5

11.9

3000

6000

9000

12000

15000

18000

Range error due to Head-wind [m]

Range[m]

PRODAS

MODEL

-3.5

-2.5

-1.5

-0.5

0.5

3000

6000

9000

12000

15000

18000

Range error due to Tail-wind [m]

Range[m]

PRODAS

MODEL

3000

6000

9000

12000

15000

18000

Range error due to +1% in air temp. [m]

Range[m]

PRODAS

MODEL

3000

6000

9000

12000

15000

18000

Range error due to -1% in air temp. [m]

Range[m]

PRODAS

MODEL

--- Página 9 ---

The 2020 Spring International Conference on Defence Technology

Journal of Physics: Conference Series

1507 (2020) 082043

IOP Publishing

doi:10.1088/1742-6596/1507/8/082043

Fig. 11 Zero drag force coefficient

Fig. 12 Lift force coefficient slope

155 mm

105 mm

Mach number

Zero Drag force Coeff.

2.5

1.5

0.5

0.45

0.4

0.35

0.3

0.25

0.2

0.15

0.1

155 mm

105 mm

Mach number

Lift force Coeff.

2.5

1.5

0.5

2.5

1.5

155 mm

105 mm

Mach number

Zero Magnus force Coeff.

2.5

1.5

0.5

-0.2

-0.4

-0.6

-0.8

-1.2

corrected

simulated

[mils]

column

QE error

18000

15000

12000

9000

6000

3000

-20

-40

-60

-80

-100

-120

-140

Fig. 13 Magnus force coefficient.

Range[m]

Fig. 14 Corrected elevation angle QE error.

3.3.  Results

An iterative process has been implemented in order to fit the measured data for two shoot groups as

illustrated before. Only two factors can be estimated as both the total flight time and summit point were

not measured. Therefore, the Magnus force fitting factor is neglected 𝑄𝑀= 1. Other estimated fitting

coefficient namely ballistic coefficient and lift factor are listed on Table 3. By implanting these factors

into our model for computational FT as illustrated before, we will obtain a first draft for provisional FT

with improved accuracy as shown in Fig. 14-16. Although, the error still noticeable as we only have one

meteorological observation and its only valid for one hour.

--- Página 10 ---

The 2020 Spring International Conference on Defence Technology

Journal of Physics: Conference Series

1507 (2020) 082043

IOP Publishing

doi:10.1088/1742-6596/1507/8/082043

There for the results consists of error from the standard table before fitting and after fitting shows in

figures below

Table 3 Fitted coefficients obtained

Group no

141.4

1.012186

0.955145

743.2

1.012186

0.964955

4.  Conclusion

As artillery firing table FT is a primary and essential tool for artillery systems developments, this paper

illustrates the problem of constructing FT starting from computational FT and hence obtain the

provisional one.  A flow-chart for computational (preliminary) FT has been proposed including both

standard and non-standard firing conditions. A flat Earth approximation has been utilized neglecting

Earth’s rotation as well as Coriolis acceleration. In order to validate the proposed model, a case-study

for 155mm-M107-HE projectile is used. Results obtained using the proposed model (computational FT)

is compared with the well-known commercial package PRODAS and the approved published 155-M107

firing-table. It can concluded that the proposed model has good accuracy as well as PRODAS. Finally,

in order to demonstrate the effectiveness of including real fires through provisional FT production, a

different aerodynamic model (105mm-HE) has been implemented for 155mm-M107 firing test. Hence,

the ballistic coefficient and lift factor have been iteratively estimated. It has been observed that the

provisional FT accuracy is improved by implementing available firing tests. This study only includes

two shooting groups for two ground range with one meteorological observation. No measurements for

the total flight time was not observed. The accuracy of the obtained provisional table still need more

improvements using more data for firing angles including the total flight time.

corrected

simulated

Range[m]

[mils]

column

Drift error

18000

15000

12000

9000

6000

3000

corrected

simulated

Range[m]

[s]

column

Flight time error

18000

15000

12000

9000

6000

3000

Fig 15. Corrected drift error.

Fig 16. Corrected time of flight error.

--- Página 11 ---

The 2020 Spring International Conference on Defence Technology

Journal of Physics: Conference Series

1507 (2020) 082043

IOP Publishing

doi:10.1088/1742-6596/1507/8/082043

References

[1]

[2]

[3]

[4]

[5]

[6]

[7]

[8]

[9]

[10]

[11]

[12]

[13]

[14]

[15]

[16]

[17]

E. R. Dickinson, The production of firing tables for cannon artillery, ARMY BALLISTIC

RESEARCH LAB ABERDEEN PROVING GROUND MD 1967.

J. W. Mauchly, "The Eniac," in A History of Computing in the Twentieth Century, ed: Elsevier,

1980 pp. 541-50

S. Gorn and N. Juncosa, On the Computational Procedures for Firing and Bombing Tables

ARMY BALLISTIC RESEARCH LAB ABERDEEN PROVING GROUND MD 1954

C. Xinjun, "Research on coincidence method in the preparation of grenade table," Journal of

Ballistics  9  72-5 1997

W. Yingbin, THE APPLICATION OF BALLISTIC FILTERING THEORY IN THE PRODUCTION OF

FIRING TABLES Journal of Ballistics 5  6, 1995.

N. S. AGENCY, STANAG-4355: The Modified Point Mass and five Degrees of Freedom

Trajectory Models STANAG 3 2009.

H. L. Reed Jr, "Firing table computations on the ENIAC," in Proceedings of the 1952 ACM

national meeting (Pittsburgh) 1952 pp. 103-6

J. A. Matts and D. H. McCoy, A graphical firing table model and a comparison of the accuracy

of three utilization schemes ARMY BALLISTIC RESEARCH LAB ABERDEEN PROVING

GROUND MD 1970

P. Chusilp, W. Charubhun, and A. Ridluan, "Developing firing table software for artillery

projectile using iterative search and 6-DOF trajectory model," in the Second TSME

International Conference on Mechanical Engineering, Krabi, 2011, pp. 19-21.

Y. Sherif, E. Liou, T. Chang, and S. Yao, Modelling the firing tables of field artillery (cannon 105

mm howitzer) Microelectronics Reliability 25 41-53 1985.

Z. H. W. Z. D. F. M. Q. W. Pengxin, Method for compiling ground gun armor ejection table

whose ammunition cannot be modified Journal of Armored Force Engineering Institute pp

49-51 2014

H. J. Breaux, A methodology for the development of fire control equations for guns and

rockets fired from aircraft ARMY BALLISTIC RESEARCH LAB ABERDEEN PROVING

GROUND MD 1985.

R. McCoy, Modern exterior ballistics: The launch and flight dynamics of symmetric projectiles:

Schiffer Pub. 1999.

U. S. C. o. E. t. t. S. Atmosphere, U. S. A. Force, U. S. W. Bureau, U. S. N. Oceanic, and A.

Administration, US Standard Atmosphere: National Oceanic and Amospheric

[sic] Administration, National Aeronautics …, 1962.

D. H. McCoy, Standard Conditions for Cannon Artillery Firing Tables ARMY BALLISTIC

RESEARCH LAB ABERDEEN PROVING GROUND MD 1969

J. R. Ward and I. W. May, Muzzle Velocity Drop in Wear-Limited Army Guns ARMY BALLISTIC

RESEARCH LAB ABERDEEN PROVING GROUND MD 1979

M. Khalil, K. Osama, and H. Abdalla Dispersion analysis for spinning artillery projectile in

International Conference on Aerospace Sciences and Aviation Technology 2009 pp. 1-12.