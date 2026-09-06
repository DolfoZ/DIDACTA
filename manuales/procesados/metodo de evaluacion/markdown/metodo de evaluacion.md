# metodo de evaluacion

*Documento procesado el 2026-05-18 18:28:31*

---

--- Página 1 ---

doi: 10.21495/5896-3-440

26th International Conference

ENGINEERING MECHANICS 2020

Brno, Czech Republic, November 24 – 25, 2020

DESIGN OF SUITABLE ASYMPTOTIC COURSES OF METEO-

BALLISTIC WEIGHTING FACTOR FUNCTIONS FOR SENSITIVITY

ANALYSIS OF PERTURBED PROJECTILE TRAJECTORIES

Rozehnal O.*, Čech V.**

Abstract: This paper is a free continuation of the paper at Engineering Mechanics 2014 by Čech, Jevický

and Jedlička. In practice, various relationships are used to sensitivity analysis the effect of meteo conditions

on the uncontrolled projectile trajectory, all of which are derived from the corresponding Weighting Factor

Functions - WFFs. One of the ways to analyze the influence of the trend of meteo conditions on the projectile

trajectory is the use of simplified - asymptotic courses of WFFs. Thus, for example, Weighting Factors - WFs

for STANAG 4061 were created in this way. In the article, we deal with the analysis of the properties of one

group of asymptotic WFFs, which is suitable for surface-to-surface fire and the effect of wind

on the projectile trajectory with altitude up to cc. 10 km (range up to cc. 30 km) and virtual temperature up

to altitude cc. 6 km (range up to cc. 20 km). From the given WFFs, the corresponding systems of WFs are

easily calculated. At the same time, we present the relations for the calculation of the Reference Height

of projectile trajectory, which is given in the tabular firing tables according to the Soviet methodology.

Keywords:  Perturbation of the projectile trajectory, Weighting factor function (curve), Weighting

factor, (meteorological) Ballistic elements, Firing tables.

1. Introduction

Calculations of the position of Mean Point of Impact/Burst (MPI) using Tabular Firing Tables (TFT)

assume the use of so-called “ballistic values” of wind wB = (wx,B, 0, wz,B), air density B and virtual

temperature Tv,B according to NATO STANAG 4061 and 4119 methodology or wB = (wx,B, 0, wz,B),

virtual temperature Tv,B and air pressure p(hG), where hG is the altitude of the barrel muzzle

of the weapon/gun (according to Soviet methodology). To calculate ballistic values (wB, B, Tv,B),

the corresponding Weighting Factors - WFs are used, which are simply calculated from the corresponding

Weighting Factor Functions - WFFs. According to the Soviet methodology, WFs are not used, but

the corresponding Reference Heights YR of the projectile trajectory - RHTs are calculated from the given

WFFs (Kovalenko and Shevkunov, 1975) and (Cech et al., 2014a). Current ballistic values are presented

in special artillery meteorological messages, for example METBKQ (according to STANAG 4061).

WFFs and Green’s functions are also special sensitivity functions, without which it is not possible

to perform high-quality sensitivity analysis of the influence of meteo conditions on changes

in the unguided projectile trajectory.

Complications in the calculation of WFFs are caused by the so-called "norm effect". An improved theory

of generalized meteo-ballistic WFFs has been published (Cech and Jevicky, 2016 and 2019), which

successfully overcomes these problems. This theory was supplemented by an improved theory

of generalized RHTs (Cech and Jevicky, 2017).

Another complication (Bliss, 1944), (Molitz and Strobel, 1963) is that the shape of a given WFFs depends

on the specific value of the ballistic coefficient c, initial (muzzle) velocity v0 and angle of departure Θ0.

Instead of the dependence on the angle Θ0, the dependence on the trajectory vertex (summit)

yS = f (c, v0, Θ0) is more often mentioned.

Ing. Ondřej Rozehnal: Department of Weapons and Ammunition, University of Defence; Kounicova 65; 662 10, Brno;

CZ,ondrej.rozehnal@unob.cz

** Assoc. Prof. Ing. Vladimír Čech, CSc.: Research and Consultancy Services, Osvobození 1654, 666 01 Tišnov; CZ and

Department of Weapons and Ammunition, University of  Defence; Kounicova 65; 662 10, Brno; CZ, vlaczekh@gmail.com

440

--- Página 2 ---

Methodologies for generating meteo messages similar to METBKQ assume the dependence of WFs only

on the trajectory vertex yS and ignore the dependence on ballistic coefficient c and initial velocity v0. This

simplifies the whole problem, but at the cost of reducing the accuracy of the calculated ballistic values.

In other words, WFs are "averaged" for usual calibers (cc. 30 to 300 mm) and usual initial velocities v0

(cc. 100 to 1300 m/s). Thus, "averaged" WFFs are used to calculate WFs, which express the trend

or asymptotic component of the course of real WFFs (Cech et al., 2014a, b).

For sensitivity analysis, these "averaged" or asymptotic WFFs can be used in the first approximation.

Their suitably selected subsets can be advantageously approximated by simple analytical functions.

In our paper we present an approximation of WFFs r(, n) - Fig. 1a and r(, n) - Fig. 2b for surface-to-

surface fire, which is suitable for the approximation of real WFFs for windw = (wx, 0, wz,), up to

an altitude vertex yS of 10 km, which corresponds to the range up to cc. 30 km, and for virtual

temperature Tv up to altitude cc. 6 km, which corresponds to the range up to cc. 20 km.

2. Weighting factor functions approximation

The basic definition or approximation of WFFs r(, n) is in the time domain - Fig. 1a. The approximation

parameter is the exponent n  0. From WFF we obtain by deriving the corresponding Green’s (impulse

response) function g(, n) – Fig. 1b (Cech. and Jevicky, 2016 and 2019).

However, for practical calculations, WFFs r(, n) – Fig. 2b and Green’s functions g(, n) – Fig. 3a

in vertical coordinate y domain (y – coordinate domain)with Bliss’notation (Bliss, 1944) are more often

used (Cech and Jevicky, 2016 and 2019).

The conversion of functions from time domain to y - coordinate domain is performed using the function

t = f (y), which is selected in the first approximation as a result of vacuum parabolic trajectory theory.

As an intermediate result we obtain a two-branched effect functionr(2)(, n) - Fig. 2a. From it, WFFs

in y – coordinate domain in Garnier’s and Bliss’notations are calculated (Cech and Jevicky, 2016

and 2019).

In our case we get

𝑟(𝜂, 𝑛) = 1 −

2𝑛+1 {[1 + √1 −𝜂]

𝑛+1 −[1 −√1 −𝜂]

𝑛+1}

(1)

and further

𝛾(𝜂, 𝑛) =

𝑔(𝜂,𝑛)

𝑔(𝜂,0) =

𝑛+1

2𝑛+1 {[1 + √1 −𝜂]

𝑛+ [1 −√1 −𝜂]

𝑛}.

(2)

The relation holds for the calculation of ballistic values ( = wx, wz, Tv, )

Δ𝜇𝐵(𝑛) = ∫Δ𝜇(𝜏) ∙𝑔(𝜏, 𝑛) ∙𝑑𝜏=

∫Δ𝜇(𝜂) ∙𝑔(𝜂, 𝑛) ∙𝑑𝜂

(3)

where:

 =  - STD– absolute deviation of meteo parameter ,

 - measured or model values,

STD – standard values.

A similar relationship applies to relative deviations  = /STD (Cech and Jevicky, 2016 and 2019).

3. Analysis of relations for WFFs and Green's functions

Eq. (3) represent Duhamel’s convolution integrals, which can also be interpreted as formulas

for calculating the weighted average B of a given function  using the “weight” function - Green’s

function g.

For n = 0 the integral in the time domain (Fig. 1b) represents the calculation of the arithmetic average

for g(, 0) = 1, while in the y - coordinate domain it is already a weighted average.

These relations were used by the French mathematician M. E. Borel to calculate ballistic wind as early

as the 1910s (Cranz, 1925). However, the course g(, 0) contradicts physical reality, because

g() = 0 for   1 must hold. The real courses are approximated for n  0.The question arises as to how

441

--- Página 3 ---

these approximations have been used successfully for more than 100 years. The answer is paradoxical:

The courses of both WFFs and Green’s function for n = 0 and 1 are identical in y - coordinate domain -

Fig. 2b, Fig. 3a, although they have completely different courses in the time domain – Fig. 1. As far as we

know, we are the first to publish this revelation here.

a)                                                                                  b)

Fig. 1: a) Weighting factor functions – WFFs r(, n); b) Green’s functions g(, n)

in time domain (tF – time of flight to the point of fall; chosen for simplicity tF = 1 s).

a)                                                                         b)

Fig. 2: a) Two-branched effect functions r(2)(, n); b) Weighting factor functions – WFFs r(, n)

in vertical coordinate y domain (y – coordinate domain).

a)                                                                         b)

Fig. 3: a) Green’s functions g(, n); b) ratio (, n)

in vertical coordinate y domain (y – coordinate domain).

442

--- Página 4 ---

Fig. 4: Moment mWFF,1(n) of the Weighting Factor Functions r(, n).

From Fig. 3a it is clear that Green’s functions g(, n) diverge for  1, closer to Cech V. and Jevicky J.

(2019).

From Fig. 3a, b shows that as n (n  0.414) increases, the weight of a part of the projectile's trajectory

near its vertex (  cc. 0.667) decreases, and then the weight of its part at the ground increases

(  cc. 0.667). As a result, the reference height YR of projectile trajectory also changes – Fig. 4.

4.  Conclusions

In the following period, we will gradually publish other suitable asymptotic approximations of WFFs.

Acknowledgement

This work originated with the support of financing from the Research Project for the Development of the

Department of Weapons and Ammunition, Faculty of Military Technology, University of Defence, Brno,

DZRO VYZBROJ.

References

Bliss, G. A. (1944) Mathematics for Exterior Ballistics. John Wiley and Sons, Inc., London, Printed in USA 1944,

p. 128.

Cech, V., Jedlicka, L. and Jevicky, J. (2014a) Problem of the Reference Height of the Projectile Trajectory

as a Reduced Meteo-ballistic Weighting Factor. Defence Technology 10, no. 2, iss. 2, Special issue of the 28th

International Symposium on Ballistics, ISSN: 2214-9147, pp. 131-140.

Cech, V., Jedlicka, L. and Jevicky, J. (2014b) Some Problems with the Estimation of Projectile Trajectory

Perturbations. Proc. of 20th International Conf. Engineering Mechanics 2014, Ed. Fuis, V., Svratka, pp. 116-119.

Cech, V. and Jevicky, J. (2016) Improved theory of generalized meteo-ballistic weighting factor functions and their

use, Defence Technology 12, iss. 3: Special issue of the 29th International Symposium on Ballistics, ISSN: 2214-

9147, pp. 242-254.

Cech, V. and Jevicky, J. (2017) Improved theory of projectile trajectory reference heights as characteristics of

meteo-ballistic sensitivity functions, Defence Technology 13, iss. 3: Special issue of the 30th International

Symposium on Ballistics, ISSN: 2214-9147, pp. 177-187.

Cech V. and Jevicky J. (2019) Some problems with numerical calculations of the meteo-ballistic sensitivity

functions and their solutions. IOSR Journal of Mechanical and Civil Engineering (IOSR – JMCE), vol. 16, iss. 4,

Ser. I, pp. 1-16.

Cranz C. (1925) Textbook of Ballistics. 1st volume. Exterior Ballistics. 5th edition, Springer Verlag, Berlin 1925,

p. 712, (in German).

Kovalenko, V. V. and Shevkunov, V. I. (1975) Meteorological preparation of artillery fire. Military Artillery

Academy of M. I. Kalinin, Leningrad, p. 84, (in Russian).

Molitz, H. and Strobel, R. (1963) Exterior Ballistics, Berlin, Springer-Verlag, 610 p., (in German).

STANAG 4061 MET, Ed. 4 Adoption of a Standard Ballistic Meteorological Message (METBKQ), 2000.

STANAG 4119, Ed. 2 Adoption of a Standard Cannon Artillery Firing Table Format, 2007.

443