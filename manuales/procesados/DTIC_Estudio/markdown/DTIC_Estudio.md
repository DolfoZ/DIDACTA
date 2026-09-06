# DTIC Estudio

*Documento procesado el 2026-05-18 18:28:21*

---

--- Página 1 ---

AD-A147 500

THE ELECTRONIC TYPESETTING PROGRAM PROGRAMMER'S MANUAL

1/2

(U) ARMY ARMAMENT RESEARCH AND DEVELOPMENT CENTER

ABERDEEN PROVIN..

J H WHITESIDE ET AL. AUG 84

UNCLARSSIFIED ARBRL-MR-93379 SBI-AD-F388 488

F/G 14/5

EhEEEEEmhmhhhI

EEE/hlhE/hhEEE

EhIIIhIhhhEIhE

iiEEllllEEEEEE

llEEllEEEEEEE

EEEllllEEEEEEE

--- Página 2 ---

L3.

L 3

-111111

MICROCOPY RESOLUTION TEST CHART

NATIONAL BUREAU OF STANDARDS IAEF A

.1*

--- Página 3 ---

nag

n.•.

II -

.,.

Lfl

MEMORANDUM REPORT ARBRL-MR-03379

THE ELECTRONIC TYPESETTING PROGRAM

PROGRAMMER'S MANUAL

John H. Whiteside

Carla G. Messina

August 1984

ARMY

ARMAMENT

RESEARCH

AND

DEVE[OPMENT

CENTER

BALLISTIC RESEARCH

LABORATORY

ABERDEEN

PROVING GROUND, MARYLAND

Approved for public release; distribution unlimited.

tov j5§4~

9.-

84 10

31 .040

--- Página 4 ---

Destroy this report when it is no longer needed.

Do not return it to the originator.

Additional copies of this report may be obtained

from the National Technical Information Service,

U. S. Department of Commerce, Springfield, Virginia

22161.

The findings in this report are not to be construed as an official

Department of the Army position, unless so designated by other

authorized documents.

The use of trade names or manufacturers' names in this report

does not constitute indorsement of any commercial product.

S~ ?

" "- 0..

I°-

*%j

"1--*

*.*-*

.o*

--- Página 5 ---

-UNCLASSIFIED

.. "

SECURITY CLASSIFICATION OF THIS PAGE (When Data Entered)

REPORT DOCUMENTATION PAGE

READ INSTRUCTIONS

DBEFORE

COMPLETING FORM

REPORT NUMBER

2. GOVT ACCESSION NO.

RECIPIENT'S CATALOG NUMBER

MEMORANDUM REPORT ARBRL-MR-03379

.... .

4. TITLE (and Subtitle)

5. TYPE OF REPORT & PERIOD COVERED

THE ELECTRONIC TYPESETTING PROGRAM

Final

PROGRAMMER' S MANUAL

6. PERFORMING ORG. REPORT NUMBER

AUTHOR(o)

CONTRACT OR GRANT NUMBER(&)

John H. Whiteside

Carla G. Messina *

PERFORMING ORGANIZATION NAME AND ADDRESS

10.

PROGRAM ELEMENT. PROJECT, TASK

US Army Ballistic Research Laboratory

AREA & WORK UNIT NUMBERS

ATTN: DRXBR-LFD

Aberdeen Proving Ground, Maryland 21005-5066

CONTROLLING OFFICE NAME AND ADDRESS

12. REPORT DATE

US Army Ballistic Research Laboratory

August 1984

ATTN:

DRXBR-OD-ST

13. NUMBER OF PAGES

Aberdeen Proving Ground, Maryland 21005-5066

128

14. MONITORING AGENCY NAME & ADDRESS(If different from Controllind Office)

IS. SECURITY CLASS. (of thle report)

UNCLASSIFIED

ISa. DECLASSIFICATION/DOWNGRADING

SCHEDULE

16.

DISTRIBUTION STATEMENT (of the Repc-t)

Approved for public release, distribution unlimited.

17.

DISTRIBUTION STATEMENT (of the abetract mitered in Block 20, It different from Report)

IS. SUPPLEMENTARY NOTES

This report supersedes IMR-755, dated October 1982.

*National Bureau of Standards

19.

KEY WORDS (Continue on reveree side if neceeaary and Identify by block number)

Artillery Firing Tables

Electronic Typesetting

Photocomposition Machine

20. ASIISTNACr (Conihue -

pevin ad Iffneeeaamy and idenify by block num~ber) (a

A new method of processing the data to make print masters (images from which

printing plates are made) for artillery firing tables has been developed.

The

new system uses electronic typesetting, derived from the National Bureau of

Standards Typographic System, to prepare data for a photocomposition machine.

This is a programmer's manual with information on how the program works, how to

alter it to produce artillery firing tables, and the structure of the Typo-

graphic System from which it is derived.

FOOM

D I

173

EDITION OF I NOV S IS OMOLETE

UNCLASSIFIED

SECURIITY CLASSIFICATION OF THIS PAGE (When Dot* Entered)

I.'.,

.,.

w-.,..-.,,

--- Página 6 ---

TABLE OF CONTENTS

PAGE

LIST OF ILLUSTRATIONS ...... ...

......................

LIST OF TABLES ..... .....

.........................

OUTLINE OF THE ELECTRONIC TYPESETTING PROGRAM

A. Background ..... .....

.........................

B. Flow Outline of the Typesetting Program .....

...........

II.

DETAILED DESCRIPTION OF INPUT PROCESSING

A. Input Processing Objectives .......

.................

B. How the Objectives are Accomplished ................

....

III.

INTERMEDIATE DATA AND CONTROL FORMS

A. Intermediate Data Forms .....

................... ...

B. Processing of Typesetting Commands ...

............. ... 11

IV. DETAILED DESCRIPTION OF OUTPUT PROCESSING

A. Reading the DIC File ..........

...............

....

B. Putting Out Photocomposition Machine Commands .........

...

V. OUTPUT FORMS AND HOW THEY ARE MODIFIED

A. The Data Card in SETHELVTIMES ....

................ ...

B. The Data Cards in WHITETOTAL, WHITEBLACK, WHITERED .......

C. Type Fonts Used in the Videocomp Output ....

...........

D. How to Include Alternate Characters or Fonts ..........

...

E. How to Interpret the Output of VIDWRT ...............

...

F. The Output Tape .......

...................... ...

VI.

FILES NEEDED TO RUN THE TYPESETTING PROGRAM .....

...........

VII.

HOW TO USE TYPESETTING COMMANDS TO CREATE WHAT YOU WANT

A. Line Drawing and the Difficulties Thereof ............

....

B. Shading ......

...........................

...

C. Changing Point Size ......

.....................

D. Changing Cursor Position .....

.................. ...

--- Página 7 ---

TABLE OF CONTENTS (Continued)

PAGE

ADDENDUMS

A. Ink Selection for Safe Light Readable Negative Numbers ..... ...

B. A Brief History of The Typesetting Program ....

...........

ACKNOWLEDGEMENTS ....... ..

............................ ...

REFERENCES ....... ... ....

... ....

... ....

...

109

APPENDIX A ........

... ..

............................ .111

Keyboard Entry of Typesetting Input

DISTRIBUTION LIST .. .. .. .... ... ... ....

.... .....

127

14TIS -GRA&I

DTIC TABA&°

,Unanounced

Justificatio

Distribution/

AvallabilitY CodeS

Avail

and/or

Dist

Special

°d~

'.°

,.g*

~~.' p.

*~~*~.*'*(.*

--- Página 8 ---

LIST OF ILLUSTRATIONS

FIGURE

PAGE

MODERNIZED SYSTEM FOR PRODUCING PRINT MASTERS ............

... 21

OUYLINE OF COMBINED EDITING AND MANUSCRIPT PROGRAM .......

"-."

FLOW CHART FOR ELECTRONIC TYPESETTING PROGRAM ....

.........

" .4

DETAILED ELECTRONIC TYPESETTING FLOW CHART FOR

DIC CODING .....

... ....

... ....

... .....

STRUCTURE AND DEFINITION OF DOCUMENT IMAGE CODE ........... .. 25

THE ASCII CODE ..... ...

......................... ... 26

CONVERSION OF JOB STREAM DATA TO DOCUMENT IMAGE CODE ...

......

DETAILED ELECTRONIC TYPESETTING FLOW CHART FOR

DIC READING ......... ... ....

... ....

....

GPO TIMES ITALIC FONT ......

...................... ... 29

GPO TIMES ITALIC SPECIALS .....

.................... ...

GPO HELVETICA ROMAN FONT

..... ........... .

GPO HELVETICA ROMAN SPECIALS ..... ....... ......

GPO UNIVERSAL DISPLAY ...... ... ....

... ....

ARMY CARDS WITH SAMPLE INPUT DATA TABLE . . . . . . . . . . . .

SAMPLE OF ARMY CARDS OUTPUT .....

................... ... 35

SAMPLE OF VIDWRT OUTPUT .....

...................

....

LINE DRAWING CORRECTIONS FOR LINE WIDTH ................

...

CHARACTER SPACING DIAGRAM ......

................... ...

CHARACTER POSITION MEASUREMENT MASK ......

...............

e-6

MODIFICATIONS IN TIMES ROMAN, BODONI, AND GOTHIC ..........

...

v%.0

A SAMPLE PAGE FROM NBS SPECIAL PUBLICATION 480-3 .......... V

RUN STREAM FORMS USED TO PROCESS AN ASCII FILE WITH

GPSDC FOR TYPESETTING ......

...................... ...

SAMPLE COUNTRY LISTINGS FROM AN INTERNATIONAL PLACE

NAME TABLE ..... ... ..

...........................

--- Página 9 ---

LIST OF ILLUSTRATIONS (Continued)

FIGURE

PAGE

THE INPUT FOR THE VIETNAM SECTION OF THE INTERNATIONAL

PLACE NAME TABLE. ...... ... ....

... ....

....

SAMPLE USES OF THE f80, f83, AND f86 INTERNAL

TYPESETTING COMMANDS ........

.......................

INPUT FOR THE SAMPLE USES OF THE f80, f83, AND f86

INTERNAL TYPESETTING COMMANDS FIGURE ..................

... 50

RULES ON RULES AND POINT SIZES .....

.................. ... 52

EXCERPTS FROM THE JANUARY 1983 GPO STYLE MANUAL ....

.........

INPUT USED TO CREATE EXCERPTS FROM THE JANUARY 1983

GPO STYLE MANUAL .......

......................... ...

30.

TOTAL TABLE EXAMPLE ....... ..

.......................

31.

BLACK TABLE EXAMPLE ....... ..

.......................

32.

RED TABLE EXAMPLE .......

........................ ... 65

--- Página 10 ---

LIST OF TABLES

TABLE NO.

PAGE

FONT CONTROL COMMANDS ....... ...

.............. ... 66

"NEGATIVE" CHARACTERS WHICH ARE NOT ITALICIZED

........

EDITING TRANSFORMATIONS IN CARLA*BATCHRUNS.ASCGPSARMY ..... ...

TABLE OF GPSDC SYSTEM CHARACTERS ....... ....

....

LINE DRAWING AND SHADE COMMANDS ........ ... .....

ACSII AND GPSDC ESCAPE SEQUENCES .. .. ... . ... ......

JOB STREAM COMMAND WORDS AND THEIR MEANING .. .......... ... 81

JOB STREAM COMMAND SEQUENCES USED BY THE

TYPESETTING PROGRAM .......

.................... ... 85

THE STRUCTURE OF PGLN .....

.....................

....

DOCUMENT IMAGE CODE LINE PARAMETER ARRAY (ISTATE). ......

SPECIAL GPSDC CODES FOR TYPESETTING .................

...

THE DSDG*VIDBLOCK.SETHELVTIMES DATA CARD .............

....

LISTING OF CARLA*BATCHRUNS.CUTMARK .....

........... ... 95

THE VIDEOCOMP 500 COMMAND CODE .......

................

TYPESETTING MEASUREMENT UNITS AND VIDEOCOMP

PAGE SPECIFICATIONS ......

....

............... ...

INTERPRETATION OF ARMY CARDS INPUT DATA TABLE ....

.........

100

REQUIRED CHANGES TO ARMY CARDS OUTPUT .....

.............

101

THE DSDG*VIDBLOCK.HELVTIMES DATA TABLE ...

............

... 102

FILES NEEDED TO RUN THE TYPESETTING PROGRAM ....

..........

105

COMMANDS TO CHANGE POINT SIZE AND REPOSITION CURSOR .........

106

r"-i

--- Página 11 ---

I. OUTLINE OF THE ELECTRONIC TYPESETTING PROGRAM

A. Background

Electronic typesetting is an automated method of doing what printers used

to do by hand; selecting the proper type size from a given kind of type (type

font) and putting the proper characters in the right positions to recreate in

print a written manuscript. It was adopted as part of a modernization effort

designed to minimize the amount of manual labor required for firing table

production. The Electronic Typesetting Program is an outgrowth of an effort

started in 1977 to modernize the way artillery firing tables were produced.

The current Typesetting Program is a modification of the National Bureau of

Standards Typographic System.

B. Flow Outline of the Typesetting Program

The basic data flow is illustrated in Figure 1. The Combined Editing and

Manuscript Program and the Typesetting Program work together to produce the

final result: a tape from which print masters can be made.

The print masters,

master copies from which printing plates are made, are made on photocomposi-

tion machines located at the Government Printing Office.

The Combined Editing and Manuscript Program is responsible for putting

final table data into the proper format with the proper page and column

titles (Figure 2).

Commands to draw lines and shade data columns are added

by referencing a "line pack" which contains master line and shade commands.

See the Combined Manuscript Program writeup.for details. The line and shade

commands are directed to the Typesetting Program which acts on them. The

sequence of events is shown in Figure 3.

II. DETAILED DESCRIPTION OF INPUT PROCESSING

A. Input Processing Objectives

The objectives of the input processing are to take the output from the

Combined Editing and Manuscript Program, convert it into a format useable on

c'he particular host computer (in this case, a UnivacR 1100/60 or a VAXR

11/780), search for negative numbers in the data, insert typesetting commands

to deal with them, and finally convert typesetting commands from the Manuscript

Program into the proper form for the Typesetting Program. This processing is

shown in the top half of Figure 4.

Runivac is a trademark of Sperry Rand Corporation

RVAX is a trademark of Digital Equipment Corporation

--- Página 12 ---

B. How the Objectives are Accomplished

(1) The input data is brought in on magnetic tape written at 1600 BPi,

114 characters per line, one line per record in ASCII format.

(2) The information from tape is then passed through a special program,

CARLA*BATCHRUNS.ASCIITOSDF. The program takes the data from tape and converts

it into Univac SDF (Scientific Data Format).

Without this program, the

Univac would attempt to map ASCII input into Field Data format. Since ASCII

has 96 characters (upper and lower case) and Field Data has 64, the need for

conversion is plain. The program was written by Joseph Yancone of the Edge-

wood MISSD.

(3) The input data, now on mass storage, is searched for negative num-

bers by CARLA*BATCHRUNS.CHARED. This program, written by Wayne Bushell of

the Edgewood MISSD, takes the negative numbers it encounters and inserts type-

setting commands to make the negative number italic. These commands are shown

in Table 1. However, certain cases must be excluded from this process. These

are shown in Table 2.

(4) Final processing of the input data is done by calling the Univac

editor to convert commands and symbols put out by the Manuscript Program into

ones recognized by the Electronic Typesetting Program. This is done as part

of CARLA*BATCHRUNS.ASCGPSARMY. The transformations that take place are shown

in Table 3.

III.

INTERMEDIATE DATA AND CONTROL FORMS

A. Intermediate Data Forms

The objective of the first half of the typesetting process, as shown in

Figure 4, is to transform an input data stream into a master code, the

General Purpose Scientific Document Code (GPSDC), which contains all the type-

setting information in compressed form.

The origin and structure of this code

are discussed extensively in Reference 1. The structure is shown in Figure 5.

Basically it is a 16-bit code which contains a character set greatly expanded

over the ASCII character set (Figure 6). A listing of the GPSDC code is shown

in Table 4. A single GPSDC frame can contain almost all the information

needed to typeset a given character, including font, representation (normal,

italic, bold, etc.) and vertical position on a line (superscript, main line,

subscript). An entire line of space characters can be collapsed into a single

frame by putting 250 in LOFRM and the number of spaces in HIFRM, thus saving

considerable storage space. The conversion to GPSDC takes place in two steps

for data.

1. Blanton C. Duncan, "Complete Clear Text Representation of Scientific

Documents in Machine Readable Form," National Bureau of Standards

Technical Note 820, U.S. Department of Commerce, Febr' ar

1974.

, , "7 ".

r~r

_, " -

' ,

-".~

*- 7

' -,'

-.- ,.-.- -

-_-'

• ".-Q ,-.- ---.-- -- • -•-

--- Página 13 ---

....

(1) Input data is coded into GPSDC form by reference to a GPSDC dictio-

nary in GPSDC*DIC8S.ASCIIN. If composite (combinations of characters) or

special characters are involved, the additional dictionaries GPSDC*DICX8S.

ASCOMP and GPSDC*DICX8S.ASDIC may be used. At this point, the character is

represented in PTDICT coding as a GPSDC character number. Spaces are uncom-

pressed. Font and modification information is carried separately - see dis-

cussion in B. below.

(2) After the input information is in GPSDC(PTDICT) code, typesetting in-

formation is gleaned from the input data and put into a GPSDC biframe along

with the character itself. This is done by GPSDC*DICX8S.DECDE. The result

is the character plus typesetting information contained in Document Image

Code (DIC).

Figure 5 shows the final result.

B. Processinq of Typesetting Commands

Typesetting commands come from several sources: explicit commands from

the input data stream, from parameter setting "cards" in the editing program,

and information inferred from the input data.

(1) Explicit commands such as "draw a line" or "change font" begin with

an escape sequence - the ASCII escape character plus one or more symbols.

GPSDC*DICX8S.DECDE passes these sequences to GPSDC*DICX8S.PFMESC for direct

conversion to DIC code. This code is then passed back to DECDE for inclusion

in the DIC file. Tables 1, 5 and 6 plus the listing in Figure 5 show the es-

cape sequences used and their meaning.

(2) Run stream data, that is, data taken from the job stream rather than

input data, is processed by GPSDC*DICX8S.CARDS. The general sequence is

shown in Figure 7. The possible command words are shown in Table 7. The two

sets of job stream commands used by portions of the Typesetting Program are

shown in Table 8.

(3) Parameters that control the way input data is handled comes from

several sources:

initial default values supplied by the program, values re-

sulting from job stream command cards, and values calculated or inferred from

the nature of the input data. Parameters that affect the typesetting of an

entire page, "global parameters," are stored in a one-dimensional array called

PGLN. Its elements are defined in Table 9. Parameters that are specific to

a given line of text are carried in a two-dimensional array called ISTATE.

Its elements are defined in Table 10. Ultimately, all typesetting parameters

are put into DIC coding and stored along with text in the DSDG*GPS-ARMY file.

(4) Typesetting control data extracted from one of the above sources or

inserted via a program change are stored in GPSDC in a special format. Figure

5 shows the GPSDC word is divided into two 8-bit sections, LOFRM and HIFRM.

Control data is stored by placing special values in these two sections. Table

11 shows a number of these combinations.

--- Página 14 ---

IV. DETAILED DESCRIPTION OF OUTPUT PROCESSING

A. Reading the DIC File

The DIC file, DSDG*GPS-ARMY, is read by DSDG*VIDBLOCK.VID500MAIN as shown

in Figure 8. This program also accepts the header information that will be

put at the top of each Videocomp page from the data card in CARLA*BATCHRUNS.

IWHITETOTAL, WHITEBLACK, or WHITERED. The DIC file is read three times, once

by each of the preceding three job streams to produce three Videocomp files:

one with all characters, one with black characters only, and one with red

(negative) characters only. The line drawing and shade conands are processed

by a modification of VID500MAIN contained in CARLA*BATCHRUNS.VIDDRAW. Lines

and shade appear in the TOTAL and BLACK files only.

B. Putting out Photocomposition Machine Commands

After the DIC line is read, the characters are converted to the language

of the photocomposition machine (a Videocomp 500), BIL 500, in several steps.

First, VID50I.AIN sets up the page commands that tell the photocomposition

machine where to start the page, what size it's going to be, and where to put

tab stops.

The point size of the characters is set and the fonts the charac-

ters are to be in are also set. The point size and other page parameters are

set by the data card in DSDG*VIDBLOCK.SETHELVTIMES as shown in Table 12.

Then two large dots (GPSDC 132 - big center dot) are put out near the top and

bottom of the page at the extreme right-hand margin. These act as guides for

the autotitic paper cutter which cuts the output roll into sheets. These

dots are generated by CARLA*BATCHRUNS.CUTMARK, listed in Table 13, for the

WHITERED job stream and by a modification to CARLA*BATCHRUNS.VIDDRAW for the

WHITETOTAL and WHITEBLACK job streams. Once the preliminary work is done,

VID500FLAIN goes about the business of putting out characters and keeping

track of the cursor (printing) position. The codes used by the photocompo-

sition machine are listed in Table 14.

Once the code is generated, it is put

onto tape by VIDPRT as Figure 8 shows.

V. OUTPUT FORMS AN1D HOW THEY ARE MODIFIED

A. The Data Card in SETHELVTI11ES

The information on this data card directs the typesetting process. The

meaning of each data field is given in Table 12. The point size and lead size

parameters determine the size of the printed characters and how much space

surrounds a given character. The characters in the Typesetting Program are

"set solid", that is, the point size and lead size are the same. Eight point

type is used. This provides good readability and reasonable information den-

sity on a page. The other important parameters are CHARACTER WIDTH and

MOJOWIDTH. Both widths are in Videocomp units - a non-dimensional measure.

Units can't be translated into physical size until the nominal point size of

the characters is specified. When MONOWIDTH is specified, CHARACTER WIDTH

(the width of integers) is ignored and all characters are squeezed or ex-

panded as appropriate in the horizontal plane to the specified width in units.

L-I

' ' ' '. , .'

' '- ..

' .- -.-.. ..

"''-.'

.'.'

- '.'-, . ...'.

--- Página 15 ---

•. .

."-

-.-.

"V.IK

The vertical extent of the character is not affected. The actual width of the

characters is determined by the formula shown in Table 15.

Thus, a 112 unit

character normally 8 points wide will actually be 4.48 points wide and 8

points high when set in monowidth.

B. The Data Card in WHITETOTAL, WHITEBLACK, WHITERED

The data card in WHITETOTAL, WHITEBLACK, and WHITERED is read by

DSDG*VIDBLOCK.VID50OMAIN which calls GPSDC*DICX8S.CARDS to do the actual read-

ing of the field data in the data card. This data is converted to GPSDC and

processed with the rest of the data in the DIC file. The data card contains

the label put at the top of each Videocomp page. The label can be easily

changed by changing the data card without affecting the contents of the DIC

file.

Normally the date portion of the label is the only part that is changed.

C. Type Fonts Used in the Videocomp Output

(1) The type fonts which may be used on the Videocomp 500 machine are

listed in the Government Printing Office Font Manual.

This manual is updated

periodically as new fonts are added. The group in charge of the manual is

the Electronic Printing Division of the GPO.

Fonts currently used by the

Typesetting Program are Times Italic, Times Italic Specials, Helvetica Roman,

Helvetica Roman Specials, and Universal Display. These are illustrated in

Figures 9 through 12. When looking through the font book, notice that each

font has a font number and a subset number. Individual characters within the

subsets are described by a two digit hexadecimal number.

(2) The type fonts selected for printing firing tables were chosen after

trying out several for readability, particularly under adverse lighting con-

ditions. Separate fonts were chosen for positive and negative numbers to

minimize the possibility of confusing one with the other. Special plus and

minus signs were designed and put into subset 2 for the respective fonts, as

suitable ones were not available. The dashes found in subset zero of each

font cannot be used as minus signs since they are placed at less than half

the height of the characters.

One extra character was developed. This was the special shade char-

acter in the Universal Display font, subset 1, hex 84. This is shown in

Figure 13.

This character is one dot wide and the height of a character.

Thus, it can be used to shade a column by shading in set fractions of a line

at a time. This is much faster than trying to put out one dot at a time and

computationally much simpler.

D. How to Include Alternate Characters or Fonts

(1) ARMYCARDS

All font and character information used by the Typesetting Program to

actually drive a photocomposition machine is stored in compressed form in

DSDG*VIDBLOCK.HELVTIMES. This set of data makes the connection between the

seven internal fonts and the "real" fonts used by the photocomposition machine.

.5.

, -

-'"

w. .

-,..

.'',"-.

--- Página 16 ---

..............

...

....

.............

............

7.-

Examples of these fonts have already been noted in Figures 9 through 13.

change the "real" font that an internal font is connected to, this data must

be changed. The program that generates HELVTIMES is CARLA*BATCHRUNS.AR1YCARDS.

The input to this program is a data table which contains all the needed infor-

mation in a clear text format. An example of this table is shown in Figure

14.

The interpretation of the numbers is given in eble 16.

(2) The background of ARMYCARDS

""'"The

NBS Typographic System and the Electronic Typesetting Program de-

rived from it use a character reference table in order to be flexible.

The

Videocomp has many styles of type (fonts) available, e.g., Times Roman,

Bodoni, Century, etc. whose character descriptions reside on a disc.

The lo-

cation of characters within a given font is at the discretion of the group

owning the photocomposition machine. The GPO is consistent in character lo-

cation, but private companies may not be.

By altering the HELVTIMES table,

the Typesetting Program can be adapted to any Videocomp 500 character set.

Each character on a Videocomp 500 is accessible by the use of four

decimal numbers or three hexidecimal numbers. Since the computer at the

National Bureau of Standards does not operate in hexadecimal, decimal numbers

are used to identify each character. The four decimal numbers needed to drive

the Videocomp 500 are:

font, sub font, position in font, and width of char-

acter.

The GPSDC 16 bit code can be reduced to three descriptive numbers:

the character number (1 to 511); the level (0 to 3); and the modification

(0 to 7).

The character numbers are listed'in Table 4.

Level refers to ver-

tical position on a line:

mainline, subscript, superscript or subscript under

previous superscript. Modification refers to a given internal Typesetting

Program font. The three GPSDC descriptive numbers must then be matched with

a specific set of four Videocomp 500 numbers in order to do any typesetting.

Therefore, it takes seven input numbers to describe one typeset character.

GPSDC's code allows for 511*4*8 individual characters before the Videocomp

500 adds its four numbers. The use of multiple dimensioned data sets would

have exceeded the available computer memory and then some, so another method

of data storage had to be developed. Carla G. iessina and Robert C. Thompson

of NBS developed the data storage scheme used in the NBS Typographic System

and the Electronic Typesetting Program. The data set design has to pack the

needed information in as small an area as possible and have a quick method of

retrieval.

The data set has to contain a fast way of determining the presence

or absence of a character and the location of the character, if present. The

information matrix is mostly empty and some of the possible character combina-

tions can be made empty. As an example, DSDG*VIDBLOCK.VID5001AIN can create

monowidth, italic, bold, superscript, and subscript characters from existing

characters so these particular characters don't have to be stored.

No empty

entries are to be stored.

ARMYCARDS calls the program DSDG*VIDBLOCK.CARDIN to convert the input

data illustrated in Figure 14 into the required compact data set.

CARDIN

packs the five numbers: modification, font, sub font, position, and character

width into one 36 bit word. There is one word for each modification. The

addresses of the 36 bit words within this table are stored in the interger

--- Página 17 ---

array LOOK (level+1, GPSDC NO.).

Three of the four levels can be set to zero

if superscripts and subscripts are made from the characters stored for level

zero. The addresses of the eight possible modifications (GPSDC internal fonts)

stored in ITAB() words are determined in the following way. If the desired

character is not in the current data set, LOOK(1,GPSDC NO.) is negative or

zero. All modifications of a character in the data set are stored, in order

of increasing modification number, between LOOK (1,GPSDC NO.) and the Absolute

Value [LOOK(1, GPSDC NO. + 1)]-l.

(3) The Output of ARMYCARDS

The table as actually created by ARMYCARDS is illustrated in Figure

15. Note that as output, the table is one-dimensional and a width table is

at the end (MAIN, N, N).

For the Typesetting Program to work, this output

must be altered. The changes that must be made are detailed in Table 17.

Once these changes are made, the table resembles Table 18.

E. How to Interpret the Output of VIDWRT

The printouts of WHITETOTAL, WHITEBLACK, and WHITERED all contain a diag-

nostic table, generated by DSDG*VIDBLOCK.VIDWRT, which analyzes the first and

last records put out by DSDG*VIDBLOCK.VIDPRT. All the records can be analyzed

by setting a new value for the SETHELVTIMES option switch.

See Table 12 for

the details. A sample table is shown in Figure 16. The printout is based on

a standard Videocomp 500 font character grid. Figures 9 and 11 give the hexa-

decimal codes for the standard alphabet and numerals. Note from Table 14 that

Videocomp command codes end at 7616 while the lowest hexadecimal character

code is 80. The characters are directly above the hexadecimal number repre-

senting them. The zone and number lines correspond to 161 and 160, respec-

tively. Trouble arises when a command parameter is 8016 or larger or when a

non-standard font is used. VIDWRT will put out a character whenever it en-

counters a hexadecimal number that corresponds to a standard character, even

if a character is not intended. If a non-standard font is used, VIDWRT will

not put out a non-standard character but will replace it with a standard

character with the same hexadecimal value. Thus, when writing in Times Italic

font 18, Subset 0, a C616 represents an "F" but in Subset 2 of the same font,

C616 is a minus sign. By using the Videocomp 500 command table and the proper

font table, an entire BIL 500 file can be decomposed and analyzed when prob-

*lems

arise.

*'oF.

The Output Tape

The GPO Videocomp 500 requires a standard set of input tape parameters.

The Typesetting Program puts out a tape with these parameters, which are:

9-track, 800 bit/inch, no parity, no tape header label.

The writing of the tape is controlled by DSDG*VIDBLOCK.VIDPRT. The actual

writing is done by GPSDC*DICX8S.NTRAN-28O/16OOPE.

--- Página 18 ---

VI.

FILES NEEDED TO RUN THE TYPESETTING PROGRAM

The files needed to make the Typesetting Program work are listed in Table

19. The program requires a few subroutines from some files and most programs

stored from other files.

VII.

HOW TO USE TYPESETTING INPUT COMMANDS TO CREATE WHAT YOU WANT

A. Line Drawing and the Difficulties Thereof

Table 5 contains the line drawing and shading commands.

To use the line

drawing facility, first lay out the form to be created on a sheet of paper.

Draw it to scale and decide if all lines are to be the same width. The use

of multiple line widths allows attention to be called to the principal parts

of the form. Each line desired should be labeled with its origin coordinates,

width, and length.

Now the line interactions must be checked. Perpendicular

lines that both end in an intersection at the left side of the form, pass

through each other without terminating, or that end in a "T" intersection can

be ignored. Perpendicular lines terminating in an intersection on the right

side of the form will look disjointed unless corrected for the effects of

line thickness. This problem arises because a vertical line is drawn from

its origin coordinates down, with its width going to the right of the origin

"Y" coordinate. A horizontal line drawn to terminate at this coordinate will

form an intersection that appears to have a bite taken out of it. The solu-

tion is to raise the origin of the vertical line by an amount equal to the

thickness of the horizontal line.

Don't forget to increase the length of the

vertical line by a corresponding amount. The horizontal line must then be

lengthened by the thickness of the vertical line.

The thicker the lines,

the more important this correction becomes.

The correction process is illus-

trated in Figure 17.

B. Shading

Shading for artillery firing tables is done using a special shade charac-

ter developed for this application. It is shown in Figure 13 as 8416

This

character is one row of dots (16 units) wide and one line high. In 8-point

type, this is equal to .0064 points wide. The shading command causes the

shade character to be repeated for the width of the column, then the cursor

is reset to the left-hand side of the column, dropped one line, and the

process is repeated until the column is fully shaded. The origin coordinates

used in the shade command are those of the upper left-hand corner of the top

of the shaded area. The width should be the column width plus an extra char-

acter width. This is done because it's unlikely that an integral number of

shade characters will fit into the width of the column. If the shading width

is one or two characters short of the column width, a vertical white line

appears next to the right-hand column separation line. Overrunning the column

width by less than the width of the vertical lines produces no ill effects.

0Alternate

shade characters, shown in Figure 13, may be used but would

require program changes to CARLA*BATCHRUNS.VIDDRAW.

9.,

--- Página 19 ---

C. Changing Point Size

Point size can be changed deliberately, that is for an entire document,

or on the fly, that is for the moment only. When changed on the fly, only

specified characters have their point size changed.

A deliberate point size change is made by changing the point size and lead

size parameters on the data card in DSDG*VIDBLOCK.SETHELVTIfIES. This card is

*shown

in Table 12.

Firing tables are "set solid" so the point and lead sizes

are the same. During the development of the Typesetting Program, 7 point type

on 8 point lead was tried but 8 point "solid" looked better, and so was adop-

-ted.

If the characters are not set solid, be sure to use the lead size, not

the character size, when calculating "character/line" (see Table 15).

The

spacing of characters is illustrated in Figure 18.

Changing point size on the fly is used to put met line numbers in artillery

firing tables' Table B-Complimentary Range Line Number. A series of tests

demonstrated that 18 point type best matched the earlier hand drawn met line

numbers.

Characters whose point size is changed on the fly are "set" the same

way as regular characters on a page. Thus, if the regular characters are "set

solid,,, the characters in the altered point size will also be "set solid."

Table 20 shows the commands used to alter point size on the fly. The sug-

gestions in

the "Strategy" portion of this table should be followed. In par-

ticular, the point size change and cursor movement commands must be the last

items on a page. Attempting to draw lines or print normal characters after

these commands have been used can result in disaster. Once a new page is

started, however, the Typesetting Program resets the cursor and the lead to

their default values.

To avoid the necessity of counting spaces by hand or measuring character

coordinates with a ruler, an overlay mask was made by photographing a pattern

*like

the one shown in Figure 19.

This has been reduced considerably from nor-

mal size. With the mask put over a manuscript page, oversize character loca-

tions and line origins can be quickly determined. The measurements are done

in terms of 8-point lead but can be quickly converted to other point sizes by

using the ratio calculation in the Table 20 Strategy Note. Observe that the

initial location for page characters in Figure 19 is (16,5).

This means the

first table character is 16 8-point spaces from the left hand edge of the

videocomp page and 5 lines below the top of the page. This allows a "binding

margin" on the left for a bound, printed page and space at the top for a label.

D. Changing Cursor Position

The cursor position change commands are listed in Table 20, along with a

strategy for their use. The cursor location is the position on a Videocomp

page where a character will be written if commanded. The Typesetting Program

automatically indexes this position as each character and each line is com-

pleted. The basic unit the Program uses is a half vertical space written

"fhu" for "format half unit." A series of editing commands in CARLA*BATCHRUNS.

ASCGPSARMY convert the plain language vertical movement commands to "fhu's."

C.%IA

--- Página 20 ---

The only place these movement commands are used for firing tables is in

Table B. There the proper sequence of events is to first print all normal

point size characters, then do the table mask lines, then the extra heavy met

line number separation lines and finally, put in the 18-point met line numbers.

ADDENDUM A:

Ink Selection for Safe Light Readable Negative Numbers

Conventional firing tables have their negative numbers printed in a cherry

red ink which is invisible under a red safe light.

The new ink used for nega-

tive numbers, D.O.D. Standard Color Specification #SPC61121, looks reddish but

has high reflectivity in red light. It was developed by the Defense Mapping

Agency for Topographic maps.

In the event the Army switches to a blue safe

light to defeat image intensifying devices, the same ink could be used since

this ink's visual efficiency is higher in blue light than in red.

See Refer-

ence 2 for more complete information.

ADDENDUM B:

A Brief History of This Program

This program is an outgrowth of a requirement started in 1977 to modernize

the way firing tables were produced. The current Typesetting Program is a

modification of the National Bureau of Standards Typographic System.

The

Typographic System was developed over a period of years by Dr. David Garvin,

Dr. Blanton C. Duncan, Mrs. Carla Messina, Mr. Robert Thompson and others at

the National Bureau of Standards (NBS).

It was developed to typeset documents

for the Office of Standard Reference Data.

Documentation of the Typographic

System is contained in References 3 and 4. Mrs. Messina cooperated with the

Ballistic Research Laboratory (BRL) in adopting the system for use in typeset-

ting firing tables.

The modifications involved special programming to create

lines and shade, accept input in certain formats, and to create 3 output files,

the Total, Black, and Red files, described in Section 4.A., and illustrated in

Figures 30, 31, and 32.

A long period of testing was required before the modi-

fications all worked properly. Part of the testing involved finding the best

fonts and point size to use for positive and negative numbers. Modifications

were made to the fonts where necessary by having new characters designed by

".'tazdard Printing Color Catalog'ze for ,,apping, Charting, m; 3 .i

zDat

and Re7ated Produts," Defense Mapping Ageny, Tpoj:'

...

'7,

Washington, DC, July 1972.

Robert C. Thompson, "General Purpose .iceentif ii

Doea,. Wi<. (o,.

so r'

,ianua7 " National Bureau of St.anc2 dd,

npub I .5i? d, Dc.,,?';,eP 9W I

Robert C. Thompson, "

ZTener!

F upoae

7*_-'e

(-.f'

.?yeh:,

lla;nuaZ, " lNat onal Bureau of Stan,.".K,'p~l.U

.,,

--- Página 21 ---

Information International, the photocomposition machine manufacturer. These

characters include the "cut off," "6" and "9" in Helvetica, the "+" and ""

signs in Helvetica and Times Italic, and the new shade character in Universal

Display. Mr. Robert Schwenk in the Electronic Printing Division of the Govern-

ment Printing Office (GPO) had the new characters implemented on the GPO

Videocomp 500 and helped with the extensive testing that followed. At this

point, the actual typesetting process was automated and checked out, but the

line and shade commands and Table B point size and cursor movement commands

were added by hand. Mr. Joseph Hurff and Mrs. Lilly Harrington from Firing

Tables Branch modified the Combined Editing and Manuscript Program so that it

would generate the line and shade commands automatically. As of this date,

the Table B commands have not been included. With this last step, the process

of manuscript (now print master) preparation will be complete. The automation

of the process saves one to four man-months per table, depending on table size.

Thus, the time and money invested in development should be paid back within

several years.

--- Página 22 ---

ACKNOWLEDGEMENTS

The authors appreciate the assistance received from Mr. Robert Thompson

and others at the Office of Standard Reference Data, National Bureau of

Standards.

The assistance Mr. Steve Sandborn of Information International provided

is very much appreciated.

Several of the figures and tables are derived from

information he provided. The authors owe a great deal to Mr. Robert Schwenk

and Mr. Bud Collison of the U.S. Government Printing Office. Their prompt

processing of typesetting test cases and criticism of the initial results

allowed timely program corrections to be made, shortening the program develop-

ment period considerably.

Finally, the authors appreciate the support given

by their supervisors, particularly when things looked bleakest, deadlines

were missed, and hope was in short supply.

!:i~20

0 -.

--- Página 23 ---

MODERNIZED SYSTEM FOR PRODUCING PRINT MASTERS

FINAL TABLE DATA

ARE ASSEMBELED

DATA INPUT INTO

COMBINED EDITING AND

MANUSCRIPT PROGRAM

EDITED DATA WITH

LINE AND SHADE

COMMANDS PRODUCED

EDITED DATA

ENTERED INTO

ELECTRONIC TYPESETTING

PROGRAMI

TYPESET DATA TRANSFERRED

BY TAPE TO GOVERNMENT

PRINTING OFFICE (GPO)

PRINT MASTERS PRODUCED

BY GPO ON PHOTOCOMPOSITION

MACHINE

PITMASTERS PHOTOGRAPHED

PHOTOS USLD TO MAKE PLATES

Figure 1

--- Página 24 ---

'.p.

777

OUTLINE OF COMBINED EDITING AND MANUSCRIPT PROGRAM

TRAJECTORY AND

EFFECTS DATA

FOR TABLES

DATA ORGANIZED INTO

PROPER FORMAT FOR

EACH TABLE - PAGE

BY PAGE

TABLE HEADERS

ADDED

LINE AND SHADE

STANPARD PAGE

COMMANDS ADDED FOR

LINE & SHADE

EACH PAGE - NON-STANDARD

COMMAND DIRJCIORY

PAGES ACCOMMODATED

FINAL PAGE DATA

ASSEMBLED AND PUT

IN FILE

F-':

Figure 2

--- Página 25 ---

FLOW CHART FOR ELECTRONIC TYPESETTING PROGRAM

[."

PAGE DATA FROM

COMBINED EDITING

AND MANUSCRIPT

PROGRAM

ALPHANUMERIC INFORMATION

AND LINE & SHADE COMMANDS

CONVERTED TO GENERAL PURPOSE

SCIENTIFIC DOCUMENT CODE (GPSDC)

DATA AND COMMANDS TPST

COMPRESSED, AND PUT INTO

DOCUMENT IMAGE CODE (DIC)

DIC CODE READ FOR

ALL CHARACTERS PLUS LINE AND

SHADE COMMANDS, TRANSLATED

INTO BIL 500 CODE AND PUT ON TAPE

DIC CODE READ FOR BLACK CHARACTERS

PLUS LINE AND SHADE COMMANDS, TRANSLATED

INTO BIL 500 CODE AND PUT ON TAPE

DIC CODE READ FOR RED CHARACTERS

ONLY, TRANSLATED INTO BIL 500 Ct'n1:

AND PUT ON TAPE

Figure 3

--- Página 26 ---

DETAILED ELECTRONIC TYPESETTING FLOW CHART FOR OIC CODING

INPUT DATA

IN ASCII

CHARACTERS

SOF IEC

EDTE

ORCOET

TESTIGWAND

HARACER

RORM: THCANUSCRPTROGR.AM ITO

NROPERSADER

TYPESETT

INGOJTO

HAATR

PRGACARLA*BATCHRUNS.CARE

READIN

SDFE

FILEE

DICTIOVARY

PROGRAM:~

FRO

DSDGMANARCRITSDFOGNA1

ROGA:PDDC8SAIN

0 ~ ~

POE

CONTROLIN

REPETITOV READINGERESPEILCNRLDT

OF LINS

IN SF FILECi

FROM RUNSTREAM CARDS

PRRAMTR

GSDCDEX TI

PROGRA:I GPSDCC8

READIREA

All SIED

FIONE IN

PROGRAM:I

[SGCRSSFN

PROGRA:

DSDG*DCRDS.SFREA

PROGRAM:

GPSDC*DICX8S.DECDE

PUT LINE AND SHADE COtW4ANDS

INTO DIC

PUT UT IC INEPROGRAM:

GPSDC*D1CX8S. PFMESC

PROGRAM:

DSDG*GOGPO.STRIPLINEOT]

Figure 4

--- Página 27 ---

V'X-

~10

I--

LA-

LL.

cnI-

Lo?)

LaJ

0.c-

LLI

=U!

C=A

~L" U

L-9

co)

uL'O tz

C.)

LaI

oA -c

coLia

%D.

C'V

>-CA)

-. 1

LL.

U-I-

CDO

C-)

CDJ

L-A) CE

Lii

C-~

LL.A-~

ClO'

C.D

co-Irc

a-4 0% 0%o

fl '.

CIA

00-4

C%I M

sUa V)

c ~

tos

c.N %Js 00~

c%' CO LJa

lj '..

LA.0A.

V-4

LI~

LA)

LA.

L".

U.~

UI I

I -

LA-

CLu

%=s

'CD

C:)

A25

%U %a

%L.%.%

--- Página 28 ---

ASCII/TTY CODE CHART

r'i-MSB

HEX

DIGIT___________

36-I

LSB

HEX

HIGHX&Y

CONTROL

HIC INU

LOW X

LOW Y

""DIGIT

g 2 o

GRAPHIC INPUT

NUL

DLE

a) 6

1 20

ISO

916

8001

SOH

DC1

141

0 .

STX

DC2

2'2

40.'

*:."

"i-"ET

#28

1 11

ETX

DC3

3 3

03C

6lie64

0100

EOT

DC4

404

'4444.

3'3

6 9

0 II

ENO

NAK

1064

0-.

lit44

ACK

SYN

6o,

106

446

0iii

BEL

ETB

4.•

'4"6

10"

447

161

4in

1 BS

CAN

5,'

661

454

1 o 0

1010

SUB

112

':44

172

ESC

5-3

*'3

443

4' '

47'3

51Z

1FF

''4

a4 I7

1101

1110

463441

it.4

111

Figure 6

2 E

--- Página 29 ---

CONVERSION OF JOB STREAM DATA TO DOCUMENT IMAGE CODE

CALLING

PROGRAM

RETURN DIC

TO CALLING

PROGRAM

GPSDC*DICX8S.CARDS

READ IN A FIELD DATA

THERE A

CARD IMAGE

COMMAND

SYMBOL?

YES

GPSDC*DICX8S.CONVRT

GPSDC*DICX8S. PARCHK

CONVERT FIELD DATA 1-

DECODE PARAMETER

CARD IMAGE TO DIC

SETTING COMMAND WORD

Figure 7

*1S

--- Página 30 ---

7.'

'0j

co..

wLJ

,,.

-C~~-

028

--- Página 31 ---

I.'I

'13

0-4

E-4~

cnq

o co

TJ7x

_2_

[mob-

--- Página 32 ---

.%J

CC.

cqq

E-4

E--

C44

eqc

--- Página 33 ---

ILT

CD§

E-_

-D7

cq eq

--- Página 34 ---

-p-

C~1

0 o0

Z3_

--- Página 35 ---

* ..-..

.--

7717..7*.

~cv

if--

V-H-

......

u .

N~ ~

--- Página 36 ---

," t-'

ARMY CARDS WITH SAMPLE INPUT DATA TABLE

@ELT,L CARLA*BATCHRUNS.ARMYCARDS

@RUN,/R JHW,801A8/JXWHITESIDE,FTMOD,5,200/500

@ELT,L CARLA*BATCHRUNS.ARMYCARDS

@MSG,W PLEASE INTERPRET PUNCH CARD OUTPUT FROM MESSCD

@ASG,A DSDG*GOGPO.

@ADD DSDG*GOGPO.NBSASG

@USE MAP$PF., MISD*FORLIB.

@MAP,IN V500

LIE DSDG*VIDBLOCK.,DSDG*CARDS.

IN CARDIN, INDATA,HEXOUT

10.

@XQT V500

11.

ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789

12.

1 0 4 18 0 205 66

13.

4 0 4 18 0 246 100

14.

5 0 4 18 0 244 200

15.

6 0 4 18 0 144 150

16.

8 0 4 18 0 244 70

17.

9 0 4 18 0 242 70

18.

10 0 4 18 0 243 100

19.

11 0 4 18 2 197 100

20.

12 0 4 18 0 139 52

21.

13 0 4 18 2 198 100

22.

14 0 4 18 0 138 52

23.

15 0 4 18 0 225 100

24.

16 0 4 18 0 176 100

25.

17 0 4 18 0 177 100

26.

18 0 4 18 0 178 100

27.

19 0 4 18 0 179 100

28.

20 0 4 18 0 180 100

29.

21 0 4 18 0 181 100

30.

22 0 4 18 0 182 100

31.

23 0 4 18 0 183 100

32.

24 0 4 18 0 184 100

33.

25 0 4 18 0 185 100

34.

26 0 4 18 0 204 52

35.

27 0 4 18 0 140 52

36.

31 0 4 18 0 141 82

37.

33 0 4 18 0 193 136

38.

34 0 4 18 0 194 134

39.

35 0 4 18 0 195 146

40.

36 0 4 18 0 196 158

41.

37 0 4 18 0 197 142

42.

38 0 4 18 0 198 128

43.

39 0 4 18 0 199 156

44.

40 0 4 18 0 200 162

45.

41 0 4 18 0 201 82

46.

42 0 4 18 0 209 94

47.

43 0 4 18 0 210 148

48.

44 0 4 18 0 211 138

49.

45 0 4 18 0 212 188

50.

46 0 4 18 0 213 164

51.

47 0 4 18 0 214 150

52.

48 0 4 18 0 215 118

53.

49 0 4 18 0 216 150

54.

50 0 4 18 0 217 154

55.

51 0 4 18 0 226 112

Figure 14

--- Página 37 ---

SAMPLE OF ARMY CARDS OUTPUT

DATA(LOOKII(I),I-

1, 180)/

1 1,5,6,7,11,15,19,20,24,28,

2 32,34,38,40,44,48,52,56,60,64,

3 68,72,76,80,84,88,92,96,97,98,

4 99,-103,103,107,111,115,119,123,127,131,

5 135,139,143,147,151,155,159,163,167,171,

6 175,179,183,187,191,195,199,203,207,-208,

7 208,209,-210,210,211,215,219,223,227,231,

8 235,239,243,247,251,255,259.263,267,271,

10.

9 275,279,283,287,291,295,299,303,307,311,

11.

A 315,316,317,-318,3*0,318,319,320,

12.

B 323,324,325,326,327,328,331,332,333,334,

13.

C 335,336,-337,2*0,337,338,339,340,341,

14.

D 342,343,344,345,346,347,348,349,350,-351,

15.

E 0,351,352,353,354,355,356,357,358,359,

16.

F 360,361,362,363,364,365,366,367,368,369,

17.

G 370,371,372,373,374,375,376,377,378,379,

18.

H 380,381,382,383,384,385,386,387,-388,0,

19.

1 388,389,390,391,392,-393,4*0,

20.

DATA(LOOKI1(I),If 181, 410)/

21.

1 393,394,-395,2*0,395,396,397,398,-399,

22.

2 3*0,399,400,-401,4*0,

23.

3 56*0,401,402,403,404,

24.

4 405,406,407,408,409,410,411,412,413,414,

25.

5 415,416,417,418,419,420,421,422,423,424,

26.

6 425,426,427,428,429,430,431,432,433,434,

27.

7 435,436,437,438,439,-440,441,442,443,

28.

8 444,-445,8*0,

29.

9 445,446,447,448,449,450,451,452,453,545,

30.

A 455,456,457,460,461,462,463,464,

31.

B 465,466,467,468,469,470,471,472,473,474,

32.

C -475,475,-476,0,476,477,478,479,480,481,

33.

D -482,0,482,483,484,485,486,487,488,489,

34.

E 490,491,492,493,494,495,496,497,498,499,

.35.

F 500,501,502,503,504,505,506,507,-508,508,

36.

G 509,510,511,512,513,514,515,516,517,518,

37.

H 519,520,521,524,525,526,527,-528,2*0,

38.

I 528,529,530,531,-533,2*0,533,534/

39.

DATA(LOOKII(I),I- 411, 512)/

40.

1 535,536,537,-538,0,538,539,-540,2*0,

41.

2 6*0,540,541,-542,0,

42.

3 10*0,

43.

4 542,-543,7*0,543,

44.

5 546,-549,549,550,551,552,553,554,555,556,

45.

6 557,558,559,-560,-561,3*0,

46.

7 2*0,561,-562,2*0,562,-563,2*0,

47.

8 32*0/

48.

DATA(ITAB (I),I-

1, 80)/

49.

1 6986039920, 7288029840, 8932196640, 7355138720,13429933040,

50.

2 21038067314,15040447088,15074001552,13496942880,15141110432,

51.

3 26851541616,26885096080,26918650144,26952204960,18258330224,

52.

4 19097191056,20204486944,19164299936, 6719013872, 8597832304,

53.

5 8899822224, 9470247200, 8966931104, 8597865072, 9168290448,

54.

6 9470279968, 9235399328,13427541362,13463290512,13496844576,

55.

7 13530399392,15038841458,13495337250, 6983877232, 7017431696,

Figure 15

"..................'....'..

--- Página 38 ---

o .

* -

SAMPLE OF ARMY CARDS OUTPUT

56.

8 7050985760, 7084540576,15038874226,13495370018, 6983844464,

57.

9 7017398928, 7050952992, 7084507808,13429146224,13462700688,

58.

A 13496254752,13529809568,15038153328,15071707792,13494649120,

59.

B 15138816672,15038186096,15071740560,13494681888,15138849440,

60.

C 15038218864,15071773328,13494714656,15138882208,15038251632,

61.

D 15071806096,13494747424,15138914976,15038284400,15071838864,

62.

E 13494780192,15138947744,15038317168,15071871632,13494812960,

63.

F 15138980512,15038906994,15071904400,13494845728,15139013280,

64.

G 15038382704,15071937168,13494878496,15139046048,15038415472/

65.

DATA(ITAB

(1),I-

81,160)/

66.

1 15071969936,13494911264,15139078816,15038939762,15072002704,

67.

2 13494944032,15139111584, 6986007152, 7019561616, 7053115680,

68.

3 7086670496, 6983910000, 7017464464, 7051018528, 7084573344,

69.

4 26849444848,26849313776,26849412080,13694829168,15338996368,

70.

5 11077583136,15406105284,17991500400,19367232144,18327044384,

71.

6 19434341024,17991533168,18830394000,18058641696,18897502880,

72.

7 18528436848,19098862224,19669287200,19165971104,19065340528,

73.

8 19367330448,21279932704,19434439328,17454760560,17488315024,

74.

9 19132481824,17555423904,16381051504,16146170512,17253466400,

75.

A 16213279392,20676051568,20441170576,21011595552,20508279456,

76.

B 19333907056,19367461520,21861934688,19434570400, 7254344304,

77.

C 8361640592,11079549216, 8428749472,13428621936,14804353680,

78.

D 12690424096,14871462560,17992057456,19367789200,19938214176,

79.

E 19434898080,15039300208,16415031952,18596069644,16482140832,

80.

F 22555525744,22320644752,25306988832,22387753632,19602768496,

81.

G 19367887504,22058796128,19434996384,20676543088,20710097552/

82.

DATA(ITAB

(I),I= 161, 240)/

83.

1 20206780704,20777206432,16918479472,17220469392,15911846176,

84.

2 17287578272,20676608624,20710163088,20206846240,20777271968,

85.

3 19334464112,19368081576,20743749920,19435127456,17455710832,

86.

4 17220829840,15106900256,17287938720,16392001776,16952427152,

87.

5 17791287584,17019536032,19066389104,19099943568,20744110368,

88.

6 19167052448,17455809136,18294669968,18596659488,18361778848,

89.

7 24972934672,25810895504i25844449582,25878004384,17187439216,

90.

8 18831606416,18328289568,18898715296,17724342896,18026332186,

91.

9 18328322336,18093441696,16919069296,16415752848,18865226061,

92.

A 16482861728, 7520977458, 7521010226,13428458864,26848331088,

93.

B 14768177776,15070167696,13491309024,15137276576,15036646000,

94.

C 16412377744,13493141792,16479486624,13962936944,15070233232,

95.

D 11345690912,15135342112,15036711536,16680878736,14566949152,

96.

E 16747987616,15036744304,15607169680,11345756148,15674278560,

97.

F 8057455216, 9970057872, 8929870112,10037166752,14768374384,

98.

G 16412541584,12687999264,16479650464,15036842608,16144138896,

99.

DATA(ITAB

(I),I- 241, 320)/

100.

1 14298644768,16211247776, 5641634416, 7017366160, 7319355680,

101.

2 7084475040, 5910332016, 7286063760, 6782746912, 7353172640,

102.

3 13694993008,15070724752,14835843360,15137833632, 6178833008,

103.

4 7017693840, 7856554272, 7084802720,22284993136,23660724880,

104.

5 22352101664,23727833760,15037268592,16144564880,14567506208,

105.

6 16211673760,15305736816,16949904016,12420055328,17017012896,

106.

7 15037334128,16413065872,12956959008,16480174752,15037366896,

107.

8 16413098640,12956991776,16480207520, 8863384176,10775986832,

108.

9 10272669984,10843095712, 13427081840,14534378128, 9467658528,

109.

110.

THIS DATA CONTINUES FOR A WHILE

Figure 15 (Continued)

--- Página 39 ---

SAMPLE OF ARMY CARDS OUTPUT

169.

DATA CITAB(I),I-

567,

569)/

170.

DATA (COMPOS(I),Im

3)/

171.

1 2,64096,28768/

172.

DATA ICMPRS,NEND / 567,

569/

173.

DATA (MAINo (1),1-

330)/

174.

1 52,100,150,112,200,136,50,2*64,100,112,52,112,52,100,

175.

2 10*112,2*52,3*200,

176.

3 102,0,2*134,138,142,130,122,154,144,54,100,134,112,168,

177.

4 146,154,126,154,144,130,122,142,130,186,128,132,126,56,0,

178.

5 56,100,0,200,110,112,104,2*112,60,110,112,42,44,102,

179.

6 46,166,112,114,2*112,66,100,60,108,100,144,98,2*96,

180.

7 3*100,3*0,112,50,7*200,

181.

8 64,2*200,2*100,2*200,3*0,160,140,150,200,100,

182.

9 200,76,2*100,5*200,2*0,2*150,100,200,

183.

A 142,140,154,148,140,160,140,2*158,152,156,128,134,122,108,

184.

B 90,94,122,112,2*116,132,112,100,142,110,156,104,138,120,

185.

C 132,142,150,2*0,150,2*200,100,50,5*0,

186.

D 72,108,3*0,3*200,100,4*0,112,200,60*0,

187.

E 0,4*164,4*94,4*146,2*94,

188.

F 2*94,2*80,2*54,2*158,2*110,3*156,2*108,

189.

G 108,148,100,162,108,200,158,2*110,200,0,200,2*150,200,

190.

R 150,9*0,2*150,200,164,94,

191.

1 158,110,164,94,148,10*104/

192.

DATA (MAINO (1),1-

331,512)/

193.

1 80,54,80,54,158,110,156,108,0,106,2*0,145,

194.

2 56,100,110,162,108,2*0,76,2*92,100,2*110,2*108,

195.

3 2*78,76,66,92,4*94,54,110,2*108,111,94,

196.

4 54,108,94,0,110,54,200,86,80,78,76,130,138,96,118,

197.

5 124,98,200,146,84,2*108,3*0,150,4*200,

198.

6 3*0,5*200,2*0,200,150,3*0,

199.

7 6*0,2*200,7*0,

200.

8 5*0,118,8*0,52,

201.

9 52,0,11*100,2*0,

202.

A 148,6*0,118,3*0,146,3*0,

203.

B 32*0/

204.

DATA (MAIN2 (I),I=

1,512)/

205.

1 54,2*0,112,200,142,0,66,68,100,0,52,0,52,100,

4206.

2 10*112,2*52,3*0,

207.

3 114,0,144,140,142,144,130,120,152,144,62,110,144,122,166,

208.

4 144,154,128,154,144,128,126,142,136,192,140,134,122,2*0,

209.

5 4*0,112,122,112,124,116,74,122,120,52,54,112,

210.

6 52,176,120,126,2*122,80,108,72,118,112,160,112,114,102,

211.

7 9*0,200,5*0,

4212.

8 68,14*0,

213.

9 272*0,200,12*0,

214.

A 44*0,52,

215.

B 52,14*0,

216.

C 47*0/

217.

DATA (t4AIN4 (1),1-

1,512)/

218.

1 66,2*0,100,200,150,0,2*70,2*100,52,100,52,100,

219.

2 10*100,2*52,3*0,

220.

3 82,0,136,134,146,158,142,128,156,162,82,94,148,138,188,

*221.

4 164,150,118,150,154,112,132,154,138,192,2*136,140,2*0,

Figure 15 (Continued)

--- Página 40 ---

SAMPLE OF ARMY CARDS OUTPUT

222.

5 4*0,2*100,84,108,84,66,94,106,54,50,110,

223.

6 58,166,108,92,2*96,76,70,62,110,82,128,106,90,80,

-,224.

7 422*0/

225.

DATA(NAIH6

(I),-

1,512)/

*226.

1 54,2*0,112,200,142,0,66,68,100,0,52,0,52,100,

227.

2 10*112,2*52,3*0,

228.

3 114,0,144,140,142,144,130,120,152,144,62,110,144,122,166,

229.

4 144,154,128,154,144,128,126,142,136,192,140,134,122,2*0,

230.

5 4*0,112,122,112,124,116,74,122,120,52,54,112,

231.

6 52,176,120,126,2*122,80,108,72,118,112,160,112,114,102,

232.

7 9*0,200,5*6,

233.

8 68,14*0,

234.

9 272*0,200,12*0,

235.

A 44*0,52,

236.

B 52,14*0,

237.

C 47*0/

Figure 15 (Continued)

--- Página 41 ---

Nft, b

Al 0

N &

0V on

4#4

-A 0

0 0

444L19

'84

cc 0,

4 4

4bd

"1,

V4~I "10'"

ccVmw

0044

MnV

VIt0

0000

NVIlo-wwi

ftwzum

cc cc cc

480

%IWIDG

cc,

.8 %p

001L dbpw

owft

D cc

0.w

NV..On

oft

aiV

2P a

AV w0

AVI

Nt-

000

94Ww

a ft,

DCo-

00ft&

m@%

O44

Merl

00 4p.

toO

ObMP

AMat

aV a

sm i

ft~

40wo

0VI

Lon

noI

00v~

00w

410

009

fm ^

f4t i

090

a*%

IV in

c c

tv W

P0 #4

0 0

0 0

0 0

s o

1 0

08 0

wiLa'a

0~@

00wbt

0 0-

NVI

.0,0

of-

4V an

00009

ftanP

.00

404

0 0 WI

00004do

b00

.ff 0

0V% aV

4.0f4

f,0

44 a

049

004=';

a00

%O 1

ftini 0

ft, W%

0cI0

00C,

z A

on ftiLI a

wP Im at 000aCA

co00

00.6rdo

003

002

0 0

0bft

CJC

~~3

004

4.0

44 an

4wV

0 0

00 a

cc4

CC)

DO0

ft4n

oo-

DOCII"0

ftmwi

.00JU

COa

CC.

a00

4LI-

04LI.w~

44 a

00j

00*

00-

Wi4

cca

D 0

CAO

1^en

t 0

0 0

w -f

orbLV

CJmm

a4 w

0t6t

cCI

t-Wwi

44M0N

Q00

C:v

CA~

00 rb

6vi

00V~

0t. 0

fy ~

4 0

0=0

0 0

00 n

00 '

o0O4'Ja

NVI

ow0

C C

) -

0%520

4 0

0V ft

000j0

C C

0 C

&,a

NVI

DOt

IV0t.

P-N

*'.

Ij"

02Qe4%

DC.

DC.

2M 44%

o~ =b

ft,13

.IO f

goI

0.-

DCsU.

C..

CC g-

LLJ

0 W.~

"If

a001

-1)C.

DC "

L-1 L.

C. C.

A.LL

04ft

oo 00

14~ m

ft 0.

C-8 .6f%

1&10

I C.*

L.L.j

.,p

4.0

%& W.4

00W

Plo

011

002

-1, :

Cra

C.L,

o s

jr4

C.4 CD

C- L-1

C-C.

-Z W%

031

JIr

N-,j

0jQ0

CA.,

C.04

CA -

CI C-.

V, vL

0r.-

-)I ;N

CLL nY u CA,

NV4

3'!v A

I* f

.W,

Wig..

VOt

C C:

3VI

EN 1K

30A

0. C3

0 C2

r-,

EN C

GO4 NV%

P.,W

e 414

44A

CAC

C*U

002

,30

On%#-

OOC3

,.in4Y

EN-

C-. C

NP.

C1Q C Q

LCaO

meIW

03C30

0i D

a 0

.N CA

WLV

vL CA' a

Pi0

0 CCA0

-00

~A" 00

flC

.20

!130

DC)

ft b%"

C.a~

a Q

C 0

CAD

-,aL

W1%

0 D

twi

P-a

03,0

L 0

04O

Q40

LDfE

C Ci

tN C.C

0 C

rC.

00f

W.6 V

C0 a

OUINLD OILJ4P.

mc%

C...

ClC.

.410

2 40

-S.

00,'m 0

00Q

Z jO

NW 4

%. CC

.00

" I--

C.LIN

C,.C

14.0

P4 bN

00oI

0n C

C22

C .yCi a a

C, V,

ftbr

CC.

(C' C-C C C

00 04

4@"

oo3$

3Z0

0. a

C 0--

W.V LC

ft0%4

P C

.8 LaO

NP.-

C.C

DC.

C) QD

LiE

CWIC.C

N4k

C's 6n

10C

C-C

E-C a

&"C' PIC..aj-ft

C, .

Co C

C C. a&

I* 4p4

4 0

plan

0 0

NP..,

C3 L)

CA 0

CL-

C 0

DC,

ft W,

r-.

D C.

CL..

CC r

0 .

C. C.

! I.C-..

5% 5%

--- Página 42 ---

F9 v "

" ._

* ..

"-4

LINE DRAWING CORRECTIONS FOR LINE WIDTH

LINE A

W.-"

Y(X

2,YI) VERTICAL LINE ORIGIN

(LINE

LENGTH (X)

(:.XIY

1 HORIZONTAL LINE ORIGIN

LINE LENGTH

(Y)

STEP 1. RAISE VERTICAL LINE ORIGIN BY HORIZONTAL LINE'S WIDTH, THEN

INCREASE ITS LENGTH BY THAT AMOUNT.

2 YI + AY) NEW VERTICAL LINE

21ORIGIN

W-..-

LINE LENGTH (X)

(X1,Y1 HORIZONTAL LINE ORIGIN

LINE LENGTH (Y + AY)

-AX

j- LINE WIDTH

STEP 2. INCREASE HORIZONTAL LINE LENGTH BY THE VERTICAL LINE'S WIDTH.

-.,-

WT YLNELNTXL

VERTICAL LINE ORIGIN (X2 ,Y +

! ',.LINE

LENGTH (X + AX)

(XI,YI) HORIZONTAL LINE ORIGIN

LINE LENGTH (Y + -Y)

SAX

LINE WIDTH

*'."

Figure 17

.1*

--- Página 43 ---

CHARACTER SPACING DIAGRAM

.5z

,.'-

uiI

'"n

%Ln

LLn

Figure 18

.... _

-,J

i"tI*

". .','-..o .

I. _

i.l....

......

'S..,,.,.

- ..

.,.

.•,

,'%

,",-..

,,,,,,,".'..r,'-

--- Página 44 ---

4.0 '5

t .

79,

10x

101

zc2C

2.,

3535

4.0

'.SKOXXKOXKKKOKKKKOKKKOKKKOKKKOKKOKKXOXKKKOKKKKXXCXXCXXKKOKKKKCXXXKCK

4.0 4.5 5c

5 C

*70

7575

K 20

'.5

65,

ABSOLUTE PAGE COORDINATES IN SPACES

Figure 19

--- Página 45 ---

MODIFICATIONS I9 TIMES ROMAN, BODONI, AND GOTHIC

BODONI

Typesetting Flags

Type

To get

in red

hold face

Fi,Fd

italic face

bold italic face

smaller size characters (use in place of small capitals font)

Fonts Fc, Fe and Fg are to be used only after

consultation

fontse

monowidti face

return to normal face

TIMES ROMAN

Type

T getypesetting

Flags

in red

*Fb

bold face

Fi,Fd

italic face

bold italic face

smaller size characters (use in place of small capitals font)

Fonts Fc, Fe and Fg are to be used only after

consultation

font.9

monowidth face

return to normal face

GOTHIC

typesetting f lags

Type

To get

in red

bold face

Fi,Fd

italic face

bold italic face

smaller size characters (use in place of small capitals font)

Fonts Fc, Fe and Fg are to be used only after

consultation

font

return to normal face

Figure 20

--- Página 46 ---

A SA-PLE PAGE FROM NBS SPECIAL PUBLICATION 480-3

Sntltifil ailon

a alt eacrie$

Department types

LEAA geographic region

State police

, = Conn.. Maine. Mass.. N.H.. RI.. Vt.

County police and sheriffs

2 = N.J., N.Y.

City with 1.9 officers

3 = Del.. Md., Pa., Va., .

Va., D.C.

City with 10-49 officers

4 = Ala., Fla.. Ga., K).. Mi.s.. N.C.. S.C., Tenn

City with 50 or more officers'

5 = III., Ind., Mich., Ohio. Wis., Minn.

The 50 largest U.S. cities"

6 = Ark.. La., N. Mex.. Okla.. Tex.

Township departments

7 = Iowa, Kans., Mo.. Nebr.

8 = Colo., Mont., N. Dak.. S. Dak., Utah. Wyo.

9 = Ariz., Calif.. Nev., Hawaii

10 = Alaska. Idaho, Oreg., Wash.

I FcIuding the Wo lartt,

R, popslation. I S

1970 cen...

T4Bt.F 1.2.2. Number of police departments b.N region and type

LEAA region

Department type

Total

State

50'

County

257

764

536

.506

413

288

103

120

3.137

City (1-9 officers)

348

713

979

1:470

703

611

283

135

217

5.486

City (10-49 officers)

237

166

344

508

230

142

168

1.985

City (SO- officers)

119

554

50 largest cities

Township

629

349

362

234

1.574

Total

829

1,088

1,544

2.186

2.883

1.498

1,196

668 505

439

12.836

*" ---

~ue

w.........ere

ac.tt, sent to 56 stote potece departmenss ince

w.ere 6 .t.e

department .

h,h

lited 2 patte agnc

o. h-...

reference to ia common central agency

However. onl) one set of queitonnairen wa% accepted fro-

each of these nit stale- a% descrobed in vol I.

app B. p 8-2

T Bt.E 1.2-3. Number of departments selected t) receive the

Detailed Questionnaire: Sirens and lights-b. region and department t.pe

LEAA geographic region

Department type

Total

State'

County

100

City 11.9 officers)

City (10-49 officers)

100

- e

City (50+ officers)

50 largest cities

Township 2

ass

Total

528

ioesiinnaireo were actusil

sent to 56 stiae police departments % ince there .ee IS st

department

wh, h litrd 2 police agenies

nilthos

ieleresce to a common central aftenr) However. onls

et ot quentionnaire% -a

accepted from each of thene it% stales

T-wsshtp departments esist onlo in retsns I. 2..3. and 5

Figure 21

,V.

eas

--- Página 47 ---

RUN STREAM FORMS USED TO PROCESS AN ASCII FILE

WITH GPSDC FOR TYPESETTING

@RUN,M/R AAAAYY, 10000-CHARMS,AAAAXXXYY,5O. 10000,D1850

@MSG,N YY XXX AAAA DATE FONT ASC*FILE.ELEMENT

@ELT, L AAAA*RUNS. ASCGPSXXX

@ASO,T 8.

@DELETE ,C AAAA*GPS-XXX.

@ED,UNQ ASC*FILE .ELEMENT, 8.

EXIT

@FREE ASC*FILE.

@ASG,UP AAAA*GPS-XXX.

@USE I., AAAA*GPS-~XXX.

@NBS*FOR .FOR. W DSDXJVIDBLOCK. WVFONT,WVTABLE

@ADD DSDG*GOGPO. SDFGpsDC

*PAL4)4 2=1

*MISC 1 82054 2

*TAB 3 10 1520 3040 100

FILE I NEW

AAAA*GPS-XXX. DATE FONT ASC*FILE.ELEMENT

*RUN

@START AAAA*RUNS .GPSGPOXXX

@RUN,N/R

AAAAYY,10000-CHARMS,AAAAGPOYY,45,1000,D1840

.Gps

To GpO

@MSG,N YY,XXX,VVV,FONT,DATE AAAA

@ELT,L AAAA*RUNS.GPSGPOXXX

@ASG,A

AAAA*GPS-XXX.

.NAME

THE GPSDC FILE

@USE

,AAAA*GPS-XXX.

@ASG,A

DSDG*GOGPO.

@ADD, P

DSDG*GOGPO. NBSASG

@MSG,W

10000-CHARMS

PLS WRITE ENABLE VVV

@ASG,TJ

2.,U9H,VVVW

.TAPE

FOR GPO

@REWIND

@ADD, P DSDG*VIDBLOCK. SETFONT

VIDEOCOMP 500

AAAA*GPS-XXX.

FONT

DATE

@EOF

AAAA

is operators qualifier

is current run flag

XXX

current job flag

VVV

is direct driver tape for typesetting device

DATE

current date

FONT

desired font name

ASC*FILE. ELEMENT

address for the file to be processed

Figure 22

--- Página 48 ---

. .,

.. ,

.... .. .

, .

SAMPLE COUNTRY LISTINGS FROM AN INTERNATIONAL PLACE NAME TABLE

TURKEY

VIETNAM

SAUDI ARABIA

province/ili

province

emirate/min~aqat

TU0I

Adana

VMO1

An Giang

SAW

'Afif

TU02

Adnyaman

VM02

Bac Thii

SA02

Al Bil/ah

TU03

Afyon

VM03

Be'n Tre

SA03

AI Jawf

TU04

Agri

VM04

Binh Tri Thi~n

SA04

Al Khi$irah

TU05

Amasya

VM05

Cao Bang

SA05

Al Madinah

TU06

Ankara

VM06

Cuu Long

SA08

Al Qa~im

TU07

Antalya

VM07

Dac Lc

SA09

Al Qurayyit

TU08

Artvin

VM08

Dong Nai

SAW0

Ar Riyfi

TU09

Aydin

VM09

D'ng Thfp

SA06

Ash Sharqiyah

TUIO

Balikesir

VMIO

Gia Lai-Cng Turn

SAlI

'Asir

TUI1

Bilecik

VM11

Hi B~ac

SA15

Al lJudfid ash Shamdlivah

TU12

Bing6l

VM12

Hai Hung

SA07

Al Muqita'ah ash Shamiliyah

TU13

Bitlis

VM13

Hii Phbng

SA12

Bishah

TUI4

Bolu

VMI4

Hi Nam Ninh

SAI3

I-i'il

TU15

Burdur

VM15

Ha N6i

SAI4

Makkah

TU16

Bursa

VMI6

Ha Son Binh

SA16

Najrin.

TU17

Canakkale

VM 17

Ha Tuy~n

SA17

Qizin

" -

TUI8

Cankin

VM18

Hhu Giang

SA18

Ranyah

TUI9

(Corum

VM19

Hoing Li~n Son

TU20

Denizli

VM20

Hb Chi Minh

TU21

Diyarbakir

VM21

Kie'n Giahg

iTU22

Edirne

VM22

Lai Chitu

TU23

Elazig

VM23

Lrm Dong

TU24

Erzincan

VM24

Long An

TU25

Erzurum

VM25

Minh Hai

TU26

Eski~ehir

VM26

Nghe Tinh

TU27

Gaziantep

VM27

Nghia Binh

TU28

Giresun

VM28

Phi Khinh

TU29

Gimiihane

VM29

Quang Nam-Di Nang

TU30

Hakkiri

VM30

Qu~ng Ninh

TU31

Hatay

VM31

S6ng B6

TU32

igel

VM32

Son La

TU33

isparta

VM33

Tiy Ninh

VM34

Thanh H6a

VM35

Thii Binh

VM36

Thuin Hai

VM37

Tien Giang

VM38

Vinh Phi6

Figure 23

--- Página 49 ---

A ~ ~

~ ~ ~ ~ ~ ~ ~ ~

-* -~ -. -

SAMPLE COUNTRY LISTINGS FROM AN INTERNATIONAL PLACE NAME TABLE

ICELAND

HUNGARY

county/sysla

county/megye

independent town/* kaupstabir

urban division/* fbviros

urban division/* megyei viros

ICOI

Akranes

1C02

Akureyri

*HU01

Bacs-Kiskun

IC03

Arnessysla

HU02

Baranya

IC04

Austur-Barbastrandarsysla

HU03

Bekes

IC05

Austur-Hunavatnssysla

HU04

Borsod-Abafij-Zemp]6n

IC06

Austur-Skaftafelissysla

HU05

Budapest

IC07

Borgarfjarbarsysla

HU06

Csongrid

IC08

Dalasysla

HU07

Debrecen

IC09

Eyjafjartarsysla

.HU08

Fej~r

ICIO

Gullbringusysla

HU25

Gybr

Ic 11

Hafnarfjbrbur *HU09

Gybr-Sopron

IC12

Hiisavik

HUIO

Hajdii-Bibar

IC13

1safjorbur

*HUll

Heves

IC14

Keflavik

*HU12

Komirom

1C15

Kjosarsysla

HU13

Miskolc

IC 16

Kopavogur *HU

N6grid

IC17

Myras~sla

HU15

Pecs

IC18

Neskaupstabur

*HU16

Pest

IC19

Norbur-fsafjarbarsysla

HU17

Somogy

IC20

Norbur-Mfilasysla

HU 18

Szabolcs-Szatmir

IC21

Norbur-I'ingeyjarsysla

HU19

Szeged

IC22

61afsfjdrbur *

HU20

Szolnok

IC23

Rangirvallas~sla

HU2 1

Tolna

IC24

Reykjavik

*HU22

Vas

IC25

Saubirkr6kur aHU23

Veszprem

IC26

Sey~isfjdrbur

aHU24

Zala

IC27

Siglufjbr'6ur

IC28

Skagafjartarssla

IC29

SnamfelIsnes- og Hanppadalsssla

IC30

Strandasysla

IC31I

Subur-Mulasysla

IC32

Subur-ingeyjars'sla

IC33

Vestmannaeyjar

IC34

Vestur-Babhastrandars~sla

IC35

Vestur-Hu1navatnssysla

IC36

Vest ur- Isafjarbarsysla

IC37

Vestur-Skaftafelissysla

Fiue23.otiud

--- Página 50 ---

-~~

77-

AV4

LL.

Cco

LsJ

0cc

I.-.

L..0

=~ VV.

0fr

&4 (U

ci-

CZC-)

O4 a.

t-~

00 X4 t

...

U~ AC

444

0'.

(V-

4)OJ

%0'.ff-,

ANC

-24A

000.0

00-4

A C

.'~.

c A

J5.

C..

O'r

4 0

.ACr

AV4

0 ~-

c a4

=A a

N4C

4CV.

U.. IN

A- (D

C 0

w4.

ONA

V4-1t

( A-AZ

oo t-

'40

CC m

C00

4A c4

-44

Cz. co

LLJa

06cl

AVAA 4L

00'

-I)&C

VA~

4 e

GoA

aAff

(U4

m A( ~C.

La.

-V;

IN~ Go

'4 4

*r .

'4)

LL.

r4. W

'4'

U.C

c. A0.

ccd 44 A

*.4

C(VA

Nov

=.4 V4...

(UC

0-1cca

A 00

air cu ='

fkc

C)a

r4'4

ODC

(w)

0AC,

c .

CPIL.

co&0

-D %

Cca

cC~

.Q.

C.00

C- ffl

V AL~

f)U

f*41' c

U. L

(UvwC

ff.0L.

VIff

Uy)

W [L.

A4 c)

AM,

;MV

CtOnCOU A4 LL.

4L..0

ev'

AC,

v -

'o0'

CIOa.

M* m

4 0

Arv

AC COC

LL 0. 4

Go co 0 A .0

A. 4

''4

X4 0e ,

C-.4

'LL.

z..-Lz..

a.0

-V)4 Cr U

co.

e~e.

-LA.

0 (30

.0 C..

to Ar9'.('.

=rv

ULz

(30

(A 'oZ

X is Am

0AA0

A00

0'O

AAif

C4Am-

CVC~200

4 -0

(.AA

%0 G

%0 L*

5'.-

0.0

4-- A'4

2--

A1.

Eu 4 ,A4

-Q A Ak0

.AMA

A u -* %-4(

mA&

AA1

%0AI-

Ll c

Cua

4' -'4i'

CLA 0)

0o-

M MA W4 W 0L

C- ff. m

A'AM,.0%AA0

(w- 00 A0*. AC LL.

...

AD% 4j

AACU.

4-A4~

0 4

OL AA-

41 C

Cri.>

Lad

m*4

44sI-dCM. .

.OV o&4 X.0

MA W =

AL 4 A4 0 X. JZAM

rAMA

AfXAACM

(V A CV.*C'C

M-MZ..-O

.4A C) CA-

Mj M, M~

0 0

(U ~

0 Cm WU

A (U

-'4-

Li..~

-3.

(U'

zU~

'lv

Z'IY.

H4' E'

C0 A

Nv N

mV N'~ N

.8j AIr Ar

m (V, (W

mU-

6'0

+U(

I-I48

--- Página 51 ---

SAMPLE USES OF THE f80, f81, f83, AND f86 INTERNAL TYPESETTING COMMANDS

03100 Benjamin Fraklin .................................. 00

District of Columbia. B 20044

50000 ................. 9

Part B. Diacritics

extended macron

C04/12

extended macron below

D07/06

Test of under line

Test of over score

C.f

C(0)

C2(o)

Test of under line and over score

Teat of mder lir, over score ad sade

At any given times during the execution of an executable program, the

deffiitiostatna of each variable, array element, or substring is either

defrmedor unldefi nd (Section 7).

Scope of Symbolic Names an

Statements Labels

FIPS 55

Codes for Named Populated Places,

,,%

Primary County Divisions, and Other Locational Entities

District of Columbia

Page

Code: 11 Postal Abbrev: K

ZIP

Part Other

Place

County

Class ZIP Code

Name GSA MIRF

SMSA

Code

Entry

Code County Equivalent Code Code Range Code CodL Code Code Code CD CD CD

00100 Anacostia .............................

.........

001 District of Columbia. U4 20020 .. 50000 ......

00600 Anacostia Junction ... ............................. 001 District ofC olubia. S ..... .. 50000 ..... ... .

01100 Arcade ............................................. 001 District of Columbia. X ..... .. 50000 ..... .

01600 Barnaby Terrace .................................... 001 District of Colmlbia. U4 ..... .. 50000 ...

02100 Barnaby Woods ...................................... 001 District of Columbia. 14 ..... .. 50000 ..... .... ....

02600 Bellevue ........................................... 001 District of Columbia. U4 ..... .. 50000 ... . ..

03100 Benjamin Franklin .................................. 001 District of Colmbia. B 20044

50000 .

03600 Benning ............................................ 001 District of Colmbia. U4 20019

50000

04100 Benning Heights ............................... 0

001 District of Colmbia. U4 ...... 50000 ..............

The mystery numbers are

valid

input

from the

terminal.

They are

created by a digit

(1-9) backspace question mark. They look as follows

1, 2. 3, etc.

The mystery numbers can be used only after

agreement

with the

publication

section.

Other characters can be made by the

use

of a red

f6 as follows V, m., 0. M.

Figure 25

--- Página 52 ---

4.4-.

4..o4.I

.7o4

'NJ

-'Z)

: -0

Q " I

. ,

* "

-4+..

. ,

Le)

L;'.3

40'

lo 04(

30 )'

-74

AD4

4DAVA

RJAl

5004

--- Página 53 ---

'4)

w 0

cco

C .,

0 10 .0

m 2

061

000

to'

a0 0

L'i~

1 -

.1 -

CL~

C. m

(1 02'

so 0))S~~C

01.

'30

.4A

L-4 0000-D

003000z03

z L.

f..

-34.-

C.~

C. AD)

06 W.

XUUCJC3VI

6 V) 2C,

*0C.

124

4o-Cos~

:.,

*fl-44.4C44.4y

CC.~~j

C'14."

~ .

'0*

AD.

2.C

*0&0

5..

130

-Z V

V (

' 0

-0.C.

01r

C". 4)')

6CaL

4) AD IN 'o0

--- Página 54 ---

...

...

-'------;- -- ;--

" •

" .,o

RULES ON RULES AND POINT SIZES

Point Sizes

Type

To get

.-..

in red

M5ed

Fe Pont Type

16Si

Point type

f07

Seven Point Type

ful

Eight Point Type

)f09

Nine Point Type

fl0

Ten Point Type

f12

Twelve Point Type

f14

Fourteen Point Type

f18

Eighteen Point Type

f24

Twentyfour Point Type

RULES

Rules are never to be centered or justified. Rules are made by a series of

minuses in a row. Rules appear in the center of the line and not on the bottom of the

line as in underscoring.

Normal rule

Light rule (Red Fa)

Heavy Rule (Red Fb)

Extra Heavy Rule (Red Ff)

Double Rule (Red Fi)

Normal

Light

Heavy

Extra Heavy

Double

Figure 27

.s.

--- Página 55 ---

EXCERPTS FROM THE JANUARY 1973 STYLE MANUAL

Excerpts from the January 1973 GPO Style Manual

Scientific and technical terms

6. COMPOUND WORDS

6.42. Do not print a hyphen in scientific terms (names of chemicals,

diseases, animals, insects, plants) used a unit modifiers if no hyphen appears

in their original form. (See list of plant names, p. 277, and insect names, p.

284.)

carbon monoxide poisoning

equivalent uranium content

guinea pig raising

whooping cough remedy

hog cholera serum

but

screw-worm raising

methyl bromide solution

Russian-olive plantings

stem rust control

white-pine weevil

Douglas-fir tree

6.43. Chemical elements used in combination with figures use a hyphen,

except with superior figures.

polonium-210

uranium-235; but U2'5; Srw; 2U2U.

Freon-12

6.44. Note use of hyphens and closeup punctuation in chemical formulas.

9-nit roanthra( 1,9,4,10)bis( I )oxathiazone-2,7-bisdioxide

Cr-Ni-Mo

2,4-D

6.45. Print a hyphen between the elements of technical compound units of

measurement.

candle-hour

light-year

horsepower-hour

passenger-mile

kilowaitt-hour

10. SIGNS AND SYMBOLS

10.1. The increased use of signs and symbols and their importance in

technical

and

scientific

work

have

emphasized

the

necessity

standardization on a national basis and of the consistent use of the standard

forms.

Figure 28

--- Página 56 ---

EXCERPTS FROM THE JANUARY 1973 STYLE MANUAL

10.2. Certain symbols are well standardized-number symbols (the digits,

0, 1, 2, 3, 4, 5, 6, 7, 8, 9); letter symbols (the letters of the alphabet, a, b, c,

d, etc.); and graphic symbols (the mathematical signs +, -,

, x,

10.3. The Government Printing Office will furnish at cost new special

symbols for technical matter when necessary.

10.4. The signs

-, -, ×, and -,

etc., are closed against accom-

panying figures and symbols. When the X is used to indicate "crossed

with" (in plant or animal breeding) or magnification, it will be separated

from the accompanying words by a space.

i-viii+ 1-288 pages

20.000±5,000

The equation A+ B

Early June X Bright (crossed with)

The result is 4x4

X 4 (magnification)

Symbols with figures

10.5. The degree mark is always used in lieu of the word degree following

a figure denoting measurement.

Ij.6. Any symbol that is set close up to figures such as the degree mark,

Greek mu, dollar mark, or commercial c (*,

p, $, v), is used before or after

each figure in a group or series.

45* to 65' F., not 45 to 65' F.

3g to 5o (no spaces)

30.k and 50p

±2 to ±7; 2 ±1"; 3 ohms ±1

$5 to $8 price range

but

§ 12 (thin space)

5-7' long. not 5-7' long

from 15 to 25 percent

Letter symbols

10.7. Letter symbols are set in italic without periods and are capitalized

only if so shown in copy, since the capitalized form may have an entirely

different meaning. However, a few symbols are set in roman if so indicated

in copy.

Equations

10.8. In mathematical equations, use italic for all letter symbols-capitals,

lowercase, small capitals, and superiors and inferiors (exponents and

subscripts); use roman for figures, including superiors and inferiors.

10.9. If an equation or a mathematical expression needs to be divided,

break before +, -, =, etc. However, the equal sign is to clear on the left of

other beginning mathematical signs. (See example (6), p. 170.)

Figure 28 (Continued)

.'J-

S... . . .

--- Página 57 ---

EXCERPTS FROM THE JANUARY 1973 STYLE MANUAL

10.10. A short equation in text should not be broken at the end of a line.

Space out the line so that the equation will begin on the next line; or better,

center the equation on a line by itself.

10.11. An equation too long for one line is set flush on the left, the second

half of the equation is set flush on the right, and the two parts are balanced

, "as

nearly as possible.

10.12. Two or more equations in series are alined on the equal signs and

centered on the longest equation in the group.

10.13, Connecting words of explanation, such as hence, therefore, and

similarly, are set flush either on the same line with the equation or on a

separate line.

10.14. If a built-up fraction occurs in one part of an equation, all other

fractions in that line must be built up.

10.15. Parentheses, braces, brackets, integral signs, and summation signs

should be of the same height as the mathematical expressions they include.

10.16. Inferiors precede superiors if they appear together; but if either

inferior or superior is too long, the two are alined on left.

Chemical symbols

10.17. The chemical elements are designated by the initial letter or a

shortened form of the English or Latin name. They are set in roman,

without periods. (For treatment of symbols, see rule 6.44.)

2(KHCH 4O6)+ CaC0 3 = CaC4H4O+ K2C 4H4O+ H,O+CO.,

Standardized symbols

10.18. Symbols duly standardized by any scientific, professional, or

technical group are accepted as preferred forms within the field of the

group. The issuing office desiring or requiring the use of such standardized

symbols should see that copy is prepared accordingly.

Scientific names

11.9. The scientific names of genera, subgenera, species, and subspecies

-" ..

(varieties) are italicized, but are set in roman in italic matter; the names of

groups of higher rank than genera (phyla, classes, orders, families, tribes,

etc.) are printed in roman.

A.s. perpallidus

Dorothia? sp. (roman "?')

Tsuga canadensis

Cypripedium parviflorum var. pubescens

the genera Quercus and Liriodendron

the family Leguminosae

Measurements of specimens of Cyanoderma erythroptera neocara

Figure 28 (Continued)

--- Página 58 ---

EXCERPTS FROM THE JANUARY 1973 STYLE MANUAL

11.10. Quotation marks should be used in place of italic for scientific

names appearing in lines set in caps, caps and small caps, or boldface, even

if there is italic type available in the series.

11.12. All letters (caps, small caps, lowercase, superiors, and inferiors)

used as symbols are italicized (excepted as provided by rule 8.122), but in

italic matter roman letters are used. Chemical symbols (even in italic

matter) and certain other standardized symbols are set in roman. (See also

rules 6.44 and 10.8.)

nth degree; x dollars

D- 0.025V,'.

0.042

G-1

5Cu:S.2(Cu,Fe,Zn)S2Sb2S0

11.13. Letter designations in mathematical and scientific matter, except

chemical symbols, are italicized.

.'p

Figure 28 (Continued)

-..-

''IN

--- Página 59 ---

LLII

-5-q

1en

.5..

fb 1

'-4

~-I0.

Ai.

LA4

L))

0.V

a.C

060

.9-

'.0

..-4

-'-

.8 4

M..0

M JO W Ad A M

..0 A

Ad0. M4*

044AD A

--- Página 60 ---

06.0

-r44

It)

r-44

0 0

4:3.

-4 -

:.. C..4

m4 c4*~

44~'

v S.0

I 14

'''

*\Ic

M- 44--I

02- 4j

L.41

4Cml

t~ o

Ch oA

AdA.LV1

0Adv

VXA

580

--- Página 61 ---

A'-,

0.At

C Al

w44

U'%

48"

LA.

0;4

.~ >1.

v) 0

)44

'A4

U)J 0

+4AL)-

1.0

:3 m)

.an~ AN

ALI CI

%0A

C CI

=~~~

4)-4

in C.

0oc

c00

1.-

C).-

LU*0

*m).

.JCi

4).).8

-4~~~-

--- Página 62 ---

.*t~

~*b ~ *.

.5-V

~A H8

0e P-4

I'.9)

4-..

0).

L..

-(0

,0e4

(D q

4.4

La.

9.n-a

"44

'-.4

"-'(

)4-4

C4C

2~ 8'

'Z0

Wr4

H ~

.94i0c

=)-4

4),

wo)

+ l

4 3

0~ A N

' D..

C~w

41-4

%~~~~~~~

14c

0~ )0

-- 0S

Aff

4)a4)

Q).

*4)

f'U

S.4,

o'-

O*4)

C;O

.i0f(

0qL

N.aM

--- Página 63 ---

6*Z

In4

enr

c.,0

~4m~A

f-zV

~~i

0).

LAJaa

0.4

4.)4

.41 "

41~

0 ,4.

0.'

LAJr

01"1

a-I

)ff

UAl

04H

.0 a

d i

A 4.)IJ

040

: -

~a~

VS .9

V4-

44.P

pp..AJ.ArA.Ap.A.A-.A..

--- Página 64 ---

777.

00)

P.-

I-VI

01-4

4 -H

n-..

.JJ

LLJ

La)4

il %.0-4

La)

jMMm4)

a0I L &I t V

A V

- y

o--A

--- Página 65 ---

TOTAL TABLE EXAIPLE

CHARGE

TABLE A

FT 8 ADD-G 1

QUADRANT ELEVATION

PROJ, HE, M509A1

FUZE, MTSO, M577

CORRECTIONS TO

CORR

CORR TO

QUADRANT

CORR TO

QUAD ELEV

FOR LOW

DEFL

ELEVATION QUAD ELEV FOR AN INC OF

LEVEL

TIME

RANGE I

FOR

FOR PROJ.

FOR PROJ.

50 M

100 M WIND OF

PROJ,

M509A1

M509A1

IN HGT

IN RG I KNOT

FLIGHT

MPACT

509A1

MILS,

MILS

MILS

MILS METERS

SEC

METERS

MILS

1025

36.4 -126.9

11.1

25.7

4627

LO.5

947

45.0 -136.6

10.7

24.7

4979

LO.4

863

55.8 -146.5

10.3

23.6

5243

LO.3

774

69.2 -154.0

9.7

22.3

5394

LO.2

680

85.1 -153.5

9.0

20.9

5403

LO.1

585

101.5 -139.8

8.3

19.4

5253

LO.1

494

114.1

-115.4

7.5

18.0

4966

0.0

417

118.4

-89.0

6.9

16.8

4617

0.0

355

114.9

-66.8

6.4

16.0

4279

0.0

308

107.0

-50.3

5.9

15.4

3989

0.0

271

97.9

-38.3

5.6

15.0

3752

0.0

100

242

89.2

-29.6

5.3

14.8

3563

0.0

105

219

81.4

-23.0

5.1

14.6

3411

0.0

110

200

74.7

-18.0

5.0

14.5

3291

0.0

115

184

68.9

-14.)

4.8

14.5

3195

0.0

120

170

64.0

-11.0

4.7

14.5

3119

0.0

125

159

59.7

-8.5

4.6

14.6

3058

0.0

130

148

56.0

-6.4

4.5

14.6

3012

0.0

135

140

52.7

-4.7

4.4

14.7

2976

0.0

140

132

49.8

-3.2

4.3

14.8

2949

0.0

145

125

47.3

-1.8

4.2

14.9

2930

0.0

150

120

45.0

-0.6

4.1

15.0

2917

0.0

155

115

42.9

0.4

4.0

15.2

2909

0.0

160

110

40.9

1.2

4.0

15.3

2907

0.0

165

105

39.1

1.9

3.9

15.5

2911

0.0

170

37.5

2.4

3.9

15.7

2921

0.0

175

36.1

2.9

3.9

15.8

2931

0.0

180

34.9

3.5

3.8

16.0

2944

0 0

185

33.9

4.0

3.8

16.2

2959

0.0

190

33.0

4.4

3.7

16.4

2977

0.0

195

32.0

4.8

3.7

16.5

2997

LO.1

200

31.1

5.2

3.7

16.7

3019

LO.1

205

30.2

5.6

3.6

16.9

3042

LO 1

210

29.4

5.9

3.6

17.1

3066

LO.1

215

28.7

6.2

3.6

17.3

3092

t.0.1

220

28.0

6.5

3.5

17.5

3119

LO 1

225

27.3

6.8

3.5

17.7

3147

LO.1

Figure 30

J6.

63X

--- Página 66 ---

BLACK TABLE EXAMPLE

CHARGE

TABLE A

FT 8 ADD-G-1

QUADRANT ELEVATION

PROJ, HE, M509A1

FUZE, MTSQ, M577

CORRECTIONS TO

CORR

CORR TO

QUADRANT

CORR TO

QUAD ELEV

FOR LOW

DEFL

ELEVATION QUAD ELEV FOR AN INC OF

LEVEL

TIME

RANGE

FOR

FOR PROJ, FOR PROJ,

50 M

100 M WIND OF

PROJ,

M509A1

M509A1

IN HGT

IN RG 1 KNOT

FLIGHT

IMPACT

M509A1l

MILS

MILS

MILS

MILS METERS

SEC

METERS

MILS

1025

36.4

11.1

25.7

4627

LO.5

947

45.0

10.7

24.7

4979

LO.4

863

55.8

10.3

23.6

5243

LO.3

774

69.2

9.7

22.3

5394

L0.2

680

85.1

9.0

20.9

5403

LO.1

585

101.5

8.3

19,4

5253

LO.1

494

114.1

7.5

18.0

4966

0.0

417

118.4

6.9

16.8

4617

0.0

355

114.9

6.4

16.0

4279

0.0

308

107.0

5.9

15.4

3989

0.0

271

97.9

5.6

15.0

3752

0.0

100

242

89.2

5.3

14.8

3563

0.0

105

219

81.4

5.1

14.6

3411

0.0

110

200

74.7

5.0

14.5

3291

0.0

115

184

68.9

4.8

14.5

3195

0.0

120

170

64.0

4.7

14.5

3119

0.0

125

159

59.7

4.6

14.6

3058

0.0

130

148

56.0

4.5

14.6

3012

0.0

135

140

52.7

4.4

14.7

2976

0.0

140

132

49.8

4.3

14.8

2949

0.0

145

125

47.3

4.2

14.9

2930

0.0

150

120

45.0

4.1

15.0

2917

0.0

155

115

42.94

15.2

2909

0.0

160

110

40.9

1.21

4.0

15.3

2907

0.0

165

105

39.1

1.9

3.9

15.5

2911

0.0

170

1 37.5

2.4

3.9

15.7

2921

0.0

170

15.

2921

175

36.13.9

15.8

_2931

0.0

180

34.9

3.5

3.8

16.0

2944

0.0

185

33.9

4.0

3.8

16.2 I 2959

0.0

190

33.0 ,

4.4

3.7

16.4

2977

0.0

195

32.0

4.8

3.1

16.5

2997

LO.1

200

31.1

5.2

3.7

16.7

3019

LO.1

205

30.2 r

5.6

3.6

16.9

3042

LO.1

210

29.4

5.9

3.6

17.1

3066

LO.1

215

28.7

6.2

3.6

17.3

3092

LO.1

220

28.0

6.5 I

3.5

17.5

3119

LO.1

225

27.3

6.8

3.5

17.7

3147

LO.1

Figure 31

--- Página 67 ---

TOTAL TABLE EXAIPLE

CHARGE

TABLE A

FT 8 ADD G 1

QUADRANT ELEVATION

PROJ, HE, M509A1

_FUZE,

MTSQ, M577

URCORRECTIONS

CORR

CORR TO

QUADRANT

CORR TO

QUAD ELEV

FOR LOW

DEFL

ELEVATION QUAD ELEV FOR AN INC OF

LEVEL

TIME

RANGE

FOR

FOR PROJ.

FOR PROJ,

50 M

100 M WIND OF

PROJ.

-M509A1

M509A1

IN HGT

IN RG 1 KNOT

FLIGHT

IMPACT

M509A1

MILS

MILS

MILS

MILS METERS

SEC

METERS

MILS

1025

36.4 -126.9

11.1

25.7

4627

LO.5

947

45.0 -136.6

10.7

24.7

4979

LO.4

863

55.8 -146.5

10.3

23.6

5243

LO.3

774

69.2 -154.0

9.7

22.3

5394

LO.2

680

85.1

-153.5

9.0

20.9

5403

LO.1

585

101.5 -139.8

8.3

19.4

5253

LO.1

494

114.1

-115.4

7.5

18.0

4966

0.0

417

118.4

-89.0

6.9

16.8

4617

0.0

.7"

355

114.9

-66.8

6.4

16.0

4279

0.0

308

107.0

-50.3

5.9

15.4

3989

0.0

271

97.9

-38.3

5.6

15.0

3752

0.0

100

242

89.2

-29.6

5.3

14.8

3563

0.0

105

219

81.4

-23.0

5.1

14.6

3411

0.0

110

200

74.7

-18.0

5.0

14.5

3291

0.0

115

184

68.9

-14.1

4.8

14.5

3195

0.0

120

170

64.0

-11.0

4.7

14.5

3119

0.0

125

159

59.7

--8.5

4.6

14.6

3058

0.0

130

148

56.0

-6.4

4.5

14.6

3012

0.0

135

140

52.7

-4.7

4.4

14.7

2976

0.0

140

132

49.8

-3.2

4.3

14.8

2949

0.0

145

125

47.3

-1.8

4.2

14.9

2930

0.0

150

120

45.0

-0.6

4.1

15.0

2917

0.0

155

115

42.9

0.4

4.0

15.2

2909

0.0

160

110

40.9

1.2

4.0

15.3

2907

0.0

165

105

39.1

1.9

3.9

15.5

2911

0.0

170

37.5

2.4

3.9

15.7

2921

0.0

175

36.1

2.9

3.9

15.8

2931

0.0

180

3.5

3.8

16.0

2944

0.0

185

33.9

4.0

3.8

16.2

2959

0.0

190

33.0

4.4

3.7

16.4

2977

0.0

195

32.0

4.8

3.7

16.5 I 2997

1LO.1

200

31.1

5.2

3.7

16.7

3019

LO.1

205

30.2

5.6

3.6

16.9

3042

LO 1

210

29.4

5.9

3.6

17.1

3066

LO.1

215

28.7

6.2

3.6

17.3

3092

L0.1

220

28.0

6.5

3.5

17.5

3119

LO 1

225

-69

27.3

6.8

3.5

17.7

3147

LO.1

Figure 30

-..-.

--- Página 68 ---

RED TABLE EXAMPLE

-126.9

-136.6

-146.5

-154.0

-153.5

-139.8

-115.4

-89. 0

-66.8

-50.3

-38.3

-29. 6

-23.0

-18.0

-14.)

-11.0

-8.5

-6.4

-4. 7

-3.2

-1.8

-0.6

|''

1 -.

.'.

Figure 32

--- Página 69 ---

TABLE 1

FONT CONTROL COMMANDS

As put out by Combined Editing and Manuscript Program:

Enter normal font:

Enter neutral font: _G

(characters following this command are

neither black nor red)

As input to Typesetting Program:

Enter normal font:

Esn

Enter italic font:

Esi

Enter neutral font:

Esg

NOTE:

The letter used in the command must be lower case

ES is the ASCII "ESCAPE" character

--- Página 70 ---

x x

RED TABLE EXAMPLE

-126. 9

-136.6

-146.5

-154. 0

-153.5

-139.8

-115.4

-89.0

-66.8

4. ~

-50.3

-38.3

-29.6

-23.0

-18.0

-8.5

-6.4

-4. 7

-3.2

-1.8

-0. 6

Figure 32

--- Página 71 ---

TABLE 2

NEGATIVE CHARACTERS WHICH ARE NOT ITALICIZED

1. DOUBLE ENTRY NUMBER

EXAMPLE: -12+

These are found in Tables D and H

2. MINUS SIGN USED AS A DASH

EXAMPLE:

FT 8-J-4

These are found in Tables A, H, and I plus the

identification header for all tables.

3. MINUS SIGN FOLLOWED BY MORE THAN 5 CHARACTERS

EXAMPLE:

See last line of Table A QE column.

4. SPECIAL CASE: -1 MIL from Table G column header.

~ S.

'...

:: .:4,

4 .

V ~ ~ ~

* .

~ .

--- Página 72 ---

TABLE 3

EDITING TRANSFORMATIONS IN CARLA*BATCHRUNS.ASCGPSARMY

CHARACTER(S) FROM

TRANSFORMED CHARACTERS FOR

MANUSCRIPT PROGRAM

TYPESETTING PROGRAM

PURPOSE

1 (in column 1)

Form Feed (ASCII ADE 12)

To insure the type-

(line 1)

setting program

starts a new page

ESCAPE (ASCII ADE 27)

To insure the "Escape"

character is in

proper machine format

Esn (ESCAPE lower case n)

Enter normal font

UPHALFLINE

Es3fhuE s4

Raise printing base

up half a line in the

current point size

UP5LINES

Es3fhufhufhufhufhufhufhufhufhufhuEs4

Raise printing base

up 5 lines in the

current point size

UP2LINES

E53fhufhufhufhuEs4

Raise printing base

up 2 lines in the

current point size

UPILINE

Es3fhufhuEs4

Raise printing base

up 1 line ii the

current point size

lb S

fps

Lower case letters

are required for

typesetting command

FP lb V

Fpv

Lower case letters

are required

4- ',

_''.>

%%%%

--- Página 73 ---

P. °•.

TABLE 3 (Continued)

CHARACTER(S) FROM

TRANSFORMED CHARACTERS FOR

MANUSCRIPT PROGRAM

TYPESETTING PROGRAM

PURPOSE

FP lb H

fph

Lower case letters

are required

- GX

ESgXESn

Put fiducial "X" in

neutral font and

return to normal

font

F05

f05

Lower case letters

required-point size

change

F08

f08

Lower case letters

required-point size

change

F18

f18

Lower case letters

required-point size

change

where:

lb means one blank space

NOTE:

The lower case typesetting commands when

preceded by "ESCAPE 3" are coded in

GPSDC as "Red" fps, fpv, or fph

".6

,-i

--- Página 74 ---

7717.%,

TABLE 4

Table of GPSDC SYSTEM Characters

Using an Extended ASCII Terminal 1/77

GPSDC Symbol

Parts

Name

No.

exclamation

double prime

3 .

number or scratch

dollar sign

percent sign

ampersand

apostrophe or prime

left parenthesis

right parenthesis

asterisk

plus

comma

minus

period

slant/slash

numeral zero

numeral one

numeral two

numeral three

numeral four

numeral five

numeral six

numeral seven

numeral eight

numeral nine

colon

semicolon

less than sign

equal sign

Igreater than sign

question mark

grave ccent

uppercase a

uppercase b

uppercase c

uppercase d

uppercase e

uppercase f

uppercase g

uppercase h

uppercase i

uppercase j

uppercase k

uppercase 1

uppercase m

uopercase n

uppercase o

uppercase p

uppercase q

PL -L.

--- Página 75 ---

TABLE 4 (Continued)

Table of GPSDC SYSTEM Characters

Using an Extended ASCII Terminal 1/77

GPSDC Symbol

Parts

Name

No.

uppercase r

uppercase a

uppercase t

uppercase u

uppercase v

uppercase w

uppercase x

uppercase y

uppercase z

left bracket

reverse slant

right bracket

circumflex

underline

641

commercial at

lowercase a

lowercase b

lowercase 0

lowercase d

lowercase e

lowercase f

9 lowercase g

lowercase h

lowercase i

lowercase J

lowercase k

lowercase 1

lowercase m

lowercase n

lowercase o

lowercase p

lowercase q

lowercase r

lowercase s

841

lowercase t

lowercase u

lowercase v

lowercase w

lowercase x

lowercase y

lowercase z

left brace

vertical bar

right brace

tilda

red!

single bar left

red

half bar left

redl

sinale bar riaht

|-o-

9,,,

,-":""-,"..

"7..,,

'?"

"''

--- Página 76 ---

TABLE 4 (Continued)

Table of GPSDC SYSTEM Characters

Using an Extended ASCII Terminal 1/77

GPSDC Symbol

Parts

Name

No.

100

red $

thick dash

101

red%

full bar left

103

red &

double bond left

104

red '

double bond right

106

red -

hyphen

107

red(

r) intersection

108

red)

U union of two sets

109

< left corner/average brace left

109

red [

110

> right corner/average brace right

110

red J

111

red..

D implies

112

red

C implied by

113

red E

3 there exists

114

red F

control for font

115

red f

control for typsetting

116

red B

product symbol

117

red C

summation symbol

118

red N

del/nabla

119

red X

X multiplied by

120

red Z

section mark

121

red e

infinity

122

red *

degree

123

red V

dagger

123

par S

red M

124

par 4

red=

t double dagger

125

red R

varies directly as

126

red 8

upward arrow

127

red 7

-- rightward arrow

128

red 9

downward arrow

129

red 6

leftward arrow

130

red H

a lozenge

131

red

logical not

132

red ?

big center dot

133

red I

integral

134

red C

diferential

135

red 0

square root

136

red G

uppercase gamma

137

red D

uppercase delta

138

uopercase theta

139

red L

uppercase lambda

140

red J

uppercase xi

141

red P

n uppercase pi

142

red S

uppercase sigma

143

red U

uppercase uosilon

1144

uppercase phi

V',

145

red Y

uppercase psi

.....

...............

--- Página 77 ---

TABLE 4 (Continued)

Table of GPSDC SYSTEM Characters

Using an Extended ASCII Terminal 1/77

GPSDC Symbol

Parts

Name

No.

146

red V

uppercase omega

147

red a

lowercase alpha

148

red b

lowercase beta

149

red g

lowercase gamma

150

red d

lowercase delta

151

red e

lowercase epsilon

152

red z

C lowercase zeta

153

red h

lowercase eta

154

red q

theta

155

red k

lowercase kappa

156

red 1

lowercase lambda

157

red m

lowercase mu

158

red n

lowercase nu

159

red J

lowercase xi

160

redp

lowercase pi

161

red r

lowercase rho

162

red 3

lowercase sigma

163

red t ,

lowercase tau

164

lowercase phi

165

red x

lowercase chi

166

red y

lowercase psi

167

red w

lowercase omega

168

red _

open box/meta space

170

red M

do not use

171

red A

diamond

172

red 1

vertical double bond

173

red =

approximately equal

174

red T

breve

175

red 2

center dot

176

red 3

northwest dot

177

red 4

nort,,east dot

178

red .

southwest dot

179

red 5

. southeast dot

180

red +

diereses/two dot leader

181

red I

lowercase iota

182

red u

lowercase upsilon

183

red 0

right horizonal bar

184

red :

left horizonal bar

185

red ;

right high vertical bar

186

top corner

186

red <

187

bottom corner

187

red >

188

red K

at reversible reaction

189

red Q

paragraph mark

190

red -

macron

191

red 0

do not use

--- Página 78 ---

TABLE 4 (Continued)

Table of GPSDC SYSTEM Characters

Using an Extended ASCII Terminal 1/77

GPSDC Symbol

Parts

Name

No.

193

red

box with round corners

194

red o

o ellipse

195

red v

equivalent/similar to

257

par A

red

A- angstrom

258

uppercase a circumflex

259

uppercase a grave

260

uppercase a umlaut

261

par i

red

lowercase angstrom

262

lowercase a circumflex

263

lowercase a grave

264

lowercase a umlaut

265

uppercase e acute

266

uppercase e circumflex

267

uppercase e grave

268

uppercase e umlaut

269

lowercase e acute

270

lowercase e circumflex

271

lowercase e grave

272

lowercase e umlaut

273

uppercase i circumflex

274

[ uppercase 1 umlaut

275

i lowercase i circumflex

276

lowercase i umlaut

277

uppercase o circumflex

278

uppercase o umlaut

279

lowercase o circumflex

280

lowercase o umlaut

281

uppercase u circumflex

282

uppercase u grave

283

uppercase u umlaut

284

lowercase u circumflex

285

U lowercase u grave

286

1 lowercase u umlaut

287

uppercase c cedilla

288

lowercase c cedilla

--:.

289

R uppercase n tilda

290

lowercase n tilda

291

plus or minus

292

uppercase Danish o

293

o lowercase Danish o

294

cent

295

not equal

297

divided by

298

less than or equal

299

greater than or equal

300

is identical

301

is congruent

--- Página 79 ---

TABLE 4 (Continued)

Table of GPSDC SYSTEM Characters

Using an Extended ASCII Terminal 1/77

GPSDC Symbol

Parts

Name

No.

307

three bonds left

308

three bonds right

311

not less than

312

not greater than

313

" not equal

314

j uppercase a tilda

315

lowercase a tilda

316

0 uppercase o tilda

317

.9 lowercase o tilda

318

A uppercase a acute

319

lowercase a acute

320

par e

red

uppercase c breve

321

par 7

red -

one macron

322

par 2

red

two macron

323

par 3

red -

three macron

324

par 4

red

four macron

325

par 5

red

five macron

326

par

. six macron

327

par 7

red -

seven macron

328

par 8

red -

eight macron

329

par 9

red -

nine macron

330

par 0

red -

zero macron

331

uppercase i acute

332

i lowercase i acute

333

uppercase i grave

334

lowercase i grave

335

0 uppercase o acute

336

6 lowercase o acute

337

uppercase o grave

338

6 lowercase o grave

339

uppercase u acute

340

u lowercase u acute

341

uppercase k cedilla

342

lowercase k cedilla

343

1 lowercase 1 acute

3411

par 1

red *

| lowercase 1 breve

345

L uppercase polish I

346

I lowercase polish 1

347

6 lowercase c acute

348

lowercase g tilda

349

uppercase N acute

350

lowercase n acute

353

. lowercase 3 cedilla

par i

red "

lowercase z dot/z degree

-.-

355

j lowercase z acute

356

par e

red

Z lowercase c breve

357

par 1

red'

lowercase q breve

--- Página 80 ---

TABLE 4 (Continued)

Table of GPSDC SYSTEM Characters

Using an Extended ASCII Terminal 1/77

GPSDC Symbol

Parts

Name

.4"

No.

358

lowercase g grave

359

lowercase n cedilla

360

par A

red '

I lowercase n breve

361

r lowercase r cedilla

362

par t

red

f lowercase r breve

363

par A

red '

lowercase a breve

364

lowercase t cedilla

365

par I

red '

lowercase z breve

366

par A

red '

£ lowercase a breve

367

par 6

red

. lowercase e breve

368

par I

red -

.1 lowercase a macron

369

par 8

red

I lowercase e macron

370

par I

red-

I lowercase £ macron

371

par 6

red '

6 lowercase o breve

372

par 0

red

a lowercase u macron

373

par z

red "

lowercase u degree

374

y lowercase y acute

375

4 lowercase a hook

"376

.A lowercase i hook

377

m1 lowercase u hook

376

t lowercase e hook

379

lowercase m tilda

380

par 5

red -

6 lowercase o macron

381

.red

I i lowercase i breve

382

par X

red -

P minus or plus

383

par 6

red e

epsilon acute/epsilon prime

384

par I

red

.uppercase i degree

385

lowercase r acute

386

d lowercase s acute

387

par G

red "

uppercase g macron

388

par H

red

uppercase h macron

389

par S

red -

uppercase s macron

390

par C

red -

uppercase c macron

391

par X

red -

uppercase x macron

392

par ft

red

lowercase n macron

393

red 5

red

red 5

...

dieresis/three dot leader

394

par E

red -

uppercase e macron

395

par I

red -

lowercase x macron

396

par C

red

uppercase 1 macron

397

par F

red -

uppercase f macron

401

red i

red I

red o

contour integral

402

par I

red

is not a subset of

403

par I

red }

is not contained as a Subset of

4104

par 4

red (

E is an element of

405

par i

red

a such that

106

par V

red -

V logical for all

109

red 3

red 3

red \

northwest arrow

.e.e,

-""

' ' .

". ,"

-','

"'""""" ,"

. "'

--- Página 81 ---

TABLE 4 (Continued)

Table of GPSDC SYSTEM Characters

Using an Extended ASCII Terminal 1/77

GPSDC Symbol

Parts

Name

No.

410

red 5

red 5

red \

southeast arrow

411

red N

red 4

red /

? northeast arrow

412

red I

red .

red /

e southwest arrow

413

red S

red 8

red 9

t up-down arrow

416

red S

red 6

red 7

' left-right arrow

417

par |

red 1

fU vertical triple bond

427

registered

428

copyright

441

pound

442

currency

443

par i

red

not identically equal

450

'open

quote

451

close quote

452

par 2

red -

I bar one half

453

one half

454

V one fourth

455

% three fourths

456

% one third

457

% two thirds

458

% one eighth

459

three eighths

460

% five eighths

461

?A seven eighths

462

one sixth

463

five sixths

465

uppercase a cedillaAC

466

uppercase C acute

467

£ uppercase e tilda

468

uppercase e cedilla

4 69

f 6 lowercase e tilda

470

par 6

red'

0 uppercase g breve

471

uppercase i tilda

472

lowercase i tilda

173

uppercase s acoute

474

uppercase s cedilla

475

uppercase u tilda

476

- lowercase u tilda

477

uppercase z acute

478

uppercase z grave

481

mystery number one

mystery number two

483

mystery number three

484

mystery number four

S..7

.5' ..

. .....

--- Página 82 ---

L°77"

TABLE 4 (Continued)

r \-,

Table of GPSDC SYSTEM Characters

Using an Extended ASCII Terminal 1/77

GPSDC Symbol

Parts

Name

No.

485

mystery number five

486

mystery number six

487

?mystery

number seven

488

mystery number eight

489

mystery number nine

ASCII characters with the word red are preceded by an escape three and

followed by an escape four on an extended ASCII terminal.

Symbols preceded

by the word par are made up of a red and a black character.

Use the following overprint characters only with GPSDC.

501

502

par 2

red

,;.

.*.

°-b.

-WM

--- Página 83 ---

I$ ..

...

.'.

TABLE 5

LINE DRAWING AND SHADE COMMANDS

As put out by Combined Editing and Manuscript Program:

Horizontal Line:

Es3FP (Ib) H (Ib) ES4 (IB) X,Y; (ib) Thickness; (Ib) Length

Vertical Line:

Es3FP (ib) V (1b) ES4 (Ib) X,Y; (1b) Thickness; (lb) Length

Shade:

Es3FP (Ib) S (Ib) FS4 (Ib) X,Y; (1b) Width; (ib) Vertical Extent

where:

ES is the ASCII "ESCAPE" character

X is the horizontal]

Coordinate of the line origin

Y is the vertical

measured in 1/10's of a point

"THICKNESS" is line thickness in 1/10's of a point

"LENGTH"

is line length in 1/10's of a point

"WIDTH"

is the width of a column to be shaded in

1/10's of a point

"VERTICAL EXTENT" is the height of a column to be shaded

in 1/1O's of a point

As edited commands input to the Typesetting Program:

Horizontal Line:

ES3 (Ib) fph (Ib) ES4

Plus above parameters

Vertical Line:

ES3 (1b) fpv (1b) ES4

Shade:

ES3 (1b) fps (Ib) ES4

NOTE:

Lower case letters must be used at this point.

**'qo

--- Página 84 ---

TABLE 6

5,-:

ASCII ESCAPE SEQUENCES

CHARACTER FOLLOWING

'-"

ACTION TAKEN

ASCII "ESCAPE"

Set horizontal tab stop

Clear horizontal tab stop

Enter extended graphic (red) character

set

Leave extended graphic (red) character

set

Clear vertical tab

Set vertical tab

7Reverse

line feed (back up one line)

Reverse half-line feed (back up one

half line)

Half-line feed (advance one half line)

Enter modification 1 - small case

Enter modification 2 - bold face

Enter modification 3 - fancy characters

d or i

Enter modification 4 - italic face

Enter modification 5 - header font

Enter modification 6 - bold italic face

Enter modification 7 - monowidth

Return to modification zero

Enter normal (modification 0) face

-'.

--- Página 85 ---

TABLE 7

JOB STREAM COMMAND WORDS AND THEIR MEANING

COMMAND WORD

MEANING

STOP

This is the last card in a free form editing command deck

for EDBOSS - a GPSDC file editor. "STOP" means stop read-

ing free form data. A RUN or EOF is also recognized.

FILE

This is used to label a file with an identifying number

as in "FILE " and to indicate whether it's a "NEW" file

(one into which GPSDC data will be written), an "OLD"

file (one from which GPSDC data will be read), or "ADDON"

(one to which GPSDC data may be added piece by piece over

a period of time).

Data is put on the card as follows:

FILE # NEW

Columns 1-12

Identification number -

Columns 13-16 not required

Blanks

Columns 19-24

Remarks

Columns 25-76

SvMBOL

This changes the command symbol

in EDCARD, EDCHK, or in

CARDS.

PGOPT

Program Option - Use depends on the programmer and the

program being run.

Check program writeups for par-

ticular program.

DMPOPT

Dump Option - Used by GPSDC*DICX8.BCDUMP. When the card

is read BCDUMP reads the GPSDC file being processed,

converts each line to field data, and prints it out.

Character modifications, i.e., bold or italic, are

not indicated.

Superscripts and subscripts are noted

if the 3-line option is used.

The options are:

0 = No dump

I = One line dump on printer

2 = FORTRAN formated dump on

magnetic tape unit 9

4 = Punched cards

8 = Three line dump (superscripts

and subscripts indicated)

The option numbers are additive so option 9 would mean

do both option 1 and option 8.

'Z<

--- Página 86 ---

.--.-

TABLE 7 (Continued)

JOB STREAM COMMAND WORDS AND THEIR MEANING

COMMAND WORD

MEANING

.. J-.

CMPDIC

Allows a change to the composite character dictionary on

the fly. The dictionary name is given followed by three

numbers. The first two numbers specify GPSDC primitive

characters which will be combined to make the new character.

The last number gives the composite dictionary location of

the character to be replaced.

DMPDIC

This allows one GPSDC character to be substituted for

another for a 3-line dump.

Change the Left Margin value set by value in PGLN to a

new value.

TAB

Set tab stops at the positions given. Up to 15 separate

tab stops may be specified. The ones not set are placed

at the Right Margin. Example: TAB

LNFEED

Gives the number of 1/2 line feeds per Line Feed character.

This sets the number of 1/2 lines/printed "line". If not

specified, the default number is 3. This leaves room for

subscripts and superscripts.

PGLENG

Sets page length in 1/2 lines. A maximum of 239 half-lines

can be used for one page. The format is:

PGLENG 1 = 239

or the page length for pages from FILE 1 is 239 half lines.

RTMARG

Changes the Right Margin as set by PGLN to a new value.

*Example:

RM 150- the right margin of the current file is

150 character spaces to the right of the Left Margin.

UNIT

Not currently used.

Same meaning as "RTMARG".

Set line feed in 1/2 lines for each individual file.

Can

be used when copying from one GPSDC file to another.

Example:

LF 1-2 -the

line feed for FILE 1 is equal to

two half lines.

-4--p -.

--- Página 87 ---

[p.

-o-

....

TABLE 7 (Continued)

JOB STREAM COMMAND WORDS AND THEIR MEANING

COMMAND WORD

MEANING

PGWDTH

Page width specified by number of horizontal character

spaces. Maximum width is 230. Example:

PGWDTH 1=150 -

the page width for FILE 1 is 150 spaces.

The physical

size of the page will be set by the point size of the

characters.

NEW

Used with FILE card to designate an empty file into which

GPSDC information will be written.

OLD

Used with FILE card to designate an existing GPSDC file -

causes the file title on the card to be checked against

the actual file title.

ADDON

Used with FILE card to designate an existing GPSDC file to

which new GPSDC data may be added - the program actually

copies it to a new file and then adds the new GPSDC data.

INPUT

Designates the input file which is active. Up to 4 input

files may be designated but only one can be active at a

given time. Used to change an existing (default) active

file designation.

OUT

Not used.

INFILE

Same meaning as INPUT.

OTFILE

Designates the output file number -

the file from which

GPSDC data is read

RUN

This card marks the end of the free form data deck. On

Univac an @EOF card has the same effect.

DOMFIL

This designates the dominant file, that is, the one whose

parameters will be used. It is used when there is more

than one GPSDC file and allows one file's parameters to

be applied to a different file. Thus, FILE 1 might be

active but if DOMFIL 2, then file 2's parameters would

be used for FILE 1.

'.=

- "

. *

=N,%I

--- Página 88 ---

TABLE 7 (Continued)

JOB STREAM COMMAND WORDS AND THEIR MEANING

COMMAND WORD

MEANING

PGNUM

Sets the number of the first page in the GPSDC file.

BBNUM

Sets the default book block number.

(Note:

This cannot

exceed 244 books.)

MSG

This prints out a message.

MISC

A "programmer's choice" card for typesetting. The use in

CARLA*BATCHRUNS. STRIPLINEOT is:

1. Number of input files

2. Point size

3. Width in characters or picas

4. Depth in characters or picas

5. Interline spacing (delta lead).

Must be

present when 4. is not zero.

PARAM

Parameter setting card whose meaning varies with the pro-

gram it's used with. As used in the Typesetting Program:

PARAM 2=1.

The ASCII input record must have a carriage

return, line feed inserted at the end of each

record.

PARAM 2=0

EDTEXT file

Co.o

.--.-

.--

--- Página 89 ---

.. -

.oV

TABLE 8

JOB STREAM COMMAND SEQUENCES USED BY THE TYPESETTING PROGRAM

SEQUENCE 1

LOCATION: CARLA*BATCHRUNS.ASCGPSARMY

*MISC

0 8

*OTFILE 1

*PARAM 2=0

*FILE 1 NEW

UNIVAC ASCII FILE TRANSFORMED INTO GPSDC

*TABS

100

FILE 1 NEW

MESSIN ARMY 12-30-81

CARLA*BTEXT.

*PARAM 2=1

*RUN

EXPLANATION:

The miscellaneous (MISC) card numbers are read by

DSDG*GOGPO.STRIPLINEOT. The first number is the number

of input files

the second is the point size of the print

the third is the page width in PICAS

the fourth is page depth in PICAS

the fifth is interline spacing

..-

SEQUENCE 2

LOCATION:

DSDG*VIDBLOCK.SETHELVTIMES

*INFILE 1

*DMPOPT 0

*RUN

8 8

200

112

1 1

8000

112

EXPLANATION:

*INFILE 1 - DATA READ FROM GPSDC FILE1

*DMPOPT 0 - DON'T DO A BCD DUMP (PROGRAM: GPSDC*DICX8S.BCDUMP)

*RUN

- THIS ENDS THE FREE FORM DATA DECK

--- Página 90 ---

TABLE 8 (Continued)

JOB STREAM COMMAND SEQUENCES USED BY THE TYPESETTING PROGRAM

DATA CARD:

DATA READ BY GPSDC*DICX8S.CARDS AND PASSED TO

DSDG*VIDBLOCK.VID500MAIN IN 1615 FORMAT

DATA POSITION

USE

Character point size

Lead size in points (size of box the character fits in)

Minimum spacing between characters (in units)

Maximum spacing (units). If a character is called

which isn't in the dictionaries, a space this width

replaces the character.

Number of consecutive spaces which set a tab

Character width (units)

Option switch for DSDG*VIDBLOCK.VIDPRT

Meaning: 1 - Print first and last records in GPSDC

file plus make a tape

0 - Print all records and make a tape

-1 - Print all records and make no tape

Number of the first printed page

Number of last possible page (make larger than last

real page number anticipated)

May be used for job ID. Not normally used.

Monowidth (units).

If present, this causes all

characters to be monowidth with the specified width.

--- Página 91 ---

TABLE 9

THE STRUCTURE OF PGLN

The use of almost all of the 120 cells in PGLN is defined. They are used

for those items that PARCHK and EDCHEK cannot set directly. One important

restriction is that file parameters may not be loaded into ISTATE until after

a file has been opened. The opening routines wash out ISTATE.

LOCATION

USE

1-40

Edit program page and line numbers

41-55

Miscellaneous numbers - for any use

56-59

Starting bookblock numbers files 1-4 (for output files).

Normally set at 1. The output file opening program also

supplies 1, in ISTATE (3,FILE).

Edit program, EDKTRL. Stores number corresponding to a

specific edit command:

subs, write, etc.

Edit program, MULT. The number of page-line number pairs

for this command. 50 = "THRU"

Edit program, command switch.

Command = 0, Text = 1

66-69

Starting page numbers, files 1-4 (for output files).

Normally set at zero here and also by the file opening

program. Corresponds to ISTATE (2,FILE).

Edit program. User exit switch.

71-74

Line feed, files 1-4.

Default values should be supplied.

Transfer to ISTATE (19,FILE).

Edit program - pagination control.

FOLLOW = 1,

IGNORE = 0. Needed only during Random Order Data Deck phase.

76-79

Parameters 1 to 4. Any use allowed.

Typewriter input:

left margin (Normally = 1)

81-95

Typewriter input:

Tab stops

Typewriter input, right margin (supply override value

here!)

--- Página 92 ---

TABLE 9 (Continued)

THE STRUCTURE OF PGLN

LOCATION

USE

Typewriter input:

switch = 1 if any word 80-96 is

changed.

100

Message switch = 1 if BCD message constructed

101

Input file:

current value

102

Output file:

current value

103

Program option

104

END switch = 1 if "RUN" or "STOP" recognized by PARCHK

105

Command switch = 1 if a value has been loaded in PGLN

other than an Edit program (1-40, 61-63) command, a

typewriter input (80-97) or a message (100).

106-9

"Dominant File".

Set = 1 for an input file that is to

control the output pagb width. Used by PREPLN.

Normally set = 0.

111-114

Page widths files 1-4 (output files).

Supply default

val ue.

116-119

Page lengths files 1-4 (output files). Supply default

value.

l88

--- Página 93 ---

TABLE 10

DOCUMENT IMAGE CODE LINE PARAMETER ARRAY (ISTATE)

The array ISTATE (24, 5) is a master array in which the parameters of a

DIC line are stored. The second variable is FILE, thus 5 columns are pro-

vided. The first four are normally associated with input-output units.

The

fifth column is a temporary storage column - its contents may be changed by

any subroutine. A programmer must not expect them to be the same after he

transfers control to some routine he has not written.

The use ,'or various words in each column-are prescribed

1. File Status (Set by input/output routines. Must be examined by

routines that call the I/O routines.)

2. Page Number

3. Book Blocl Number

4. Page Width (maximum X coordinate)

5. Page Length (maximum Y coordinate, in half lines)

6. Line Type (presence of superscripts, subscripts, modification and

leading summarized here for line text. Diagrammatic text mode

indicated if it applied.

7. Length of Text in biframes (16 bit bytes).

This is the current

length.

It changes if blanks are compressed by a routine.

8. Line Number

9. "Old" Y coordinate

-output. Next available half line interval

-input. Value associated with previous line read

10.

"New" Y coordinate

-output. That value assigned to this line

-input. That value found assigned to this line

11.

Line Suffix Signal

Records the number of biframes on the line in addition to the text,

according to these rules:

0 no additional material

2 if either (or both) the edit biframe (12) or the diagnostic

biframe (13) are not null, and no other bytes are present

--- Página 94 ---

TABLE 10 (Continued)

DOCUMENT IMAGE CODE LINE PARAMETER ARRAY (ISTATE)

>2 If a non-standard suffix, i.e. material other than the

edit and diagnostic byte, is present, then the value is

the length of the non-standard suffix plus 2.

12.

EDIT BYTE

Null value 255/255

This biframe is used by editing programs to indicate that the

particular line was edited. Two primitive DIC symbols may be

stored. Upper ,-ase letters preferred.

13. Diagnostic BYTE

Null value 127/127

This is a bit storage word, each bit conveying some information

about input/output troubles. Bits are knocked down to indicate use.

No use of this byte should be made by the casual programmer.

14.

Right Bracket

15.

String Length

This word has various meanings at different points in a program. It

may record the total line length including all brackets, text and

suffix, as at output. It may total the text and the non-standard

suffix, as for a line returned by the input program. Its value

after a call to CMPRS is the length of text that will fit the de-

sired page width (4, above).

16.

Operation Check Indicator

This is an input/output error word, each bit of which stores error

information of a particular type. It is set by the routines that

read and write DIC records.

17.

General Purpose Switch

This is a bit by bit switch. Change only the bit in question.

Bit 1. Zero if no compressed blanks on line. 1 if compressed

blanks are present. Set by input/output. Should be

set if lines are generated by a program.

Bit 2. Zero if the line is within a page. 1 if the line

should be written as the last line on a page.

(Forces

pagination by output program.)

w -

go--

---

---

-.-

...

--- Página 95 ---

TABLE 10 (Continued)

DOCUMENT IMAGE CODE LINE PARAMETER ARRAY (ISTATE)

Description of ISTATE (1, File)

A. Position on a page. Tells what the previous I/O action did.

0 undefined

1 in a gap between pages

2 starting page bracket recognized

3 undefined

4 in a gap between lines on a page (but not after the first line)

5 after the last line on a page

6 in the gap after the first line on a page

7 only one line on the page (combination of 1, 2 and 4)

B. Output Files

0 closed or non-existent

1 end of reel trailer sensed (write head positioned after it)

" .2

after a end of file trailer label

3 after an end of medium mark

4 open and processing

'I..

"-'"

C. Input Files

0 closed or non-existent

1 end of reel trailer sensed (need head positioned past it)

2 end of file read (need head positioned past it)

3 at (after) tape mark

4 open and processing

.4 .

-""

%..

'A..

V2.

4a*

I.*

k'~%~

''a.h..

--- Página 96 ---

TABLE 10 (Continued)

DOCUMENT IMAGE CODE LINE PARAMETER ARRAY (ISTATE)

18.

Not Used

19.

Line Feed

Stores the current normal line spacing for a file, measured in 1/2

lines from main line to main line.

"Double spacing" = 4, etc.

20. Reserved for use by CMPRS

Records the page width required to handle the line of text supplied

to CMPRS. Compare 15.

21.

Logical Unit used for this file.

22. Previous Line Type Switch, formerly known as KSBSW.

It is =1 if there was a subscript or leading on previous line and

=0 if not.

(This switch influences location of next line.

See

discussion of Y-coordinates.)

rw..

' :"

--- Página 97 ---

-q,

...

~.*~~.

W -

TABLE 11

SPECIAL GPSDC CODES FOR TYPESETTING

Special (;PSDC Codes for Typesetting

The GPSDC word is divided into an upper and lower eight bits called LOFRNI and HIFRM. When the

LOFRM is

either. 96. 250, or 253, the HIFRM contains specific typesetting commands.

HIFRM

LOFRM

space of no width on typesetter.

n>2

space of size n in typesetting units.

250

space of DSPACE

in typesetting units.

X>2

250

causes following information to be tabbed

to position COUNTL+X. Position

is CHARID*PTSIZE* (COL'NTL+X)

from left margin.

I to 36

253

set point size to this numb.-'.

253

set a tab at this position on typesetter

253

tab curser to position set by (83-253)

253

move curser up the page half the current

leading toward the top of the page.

253

center the character following over the

preceeding character.

253

decrease the counter COUNTL

by one.

Used in creating COMPOSITE characters.

253

move the curser down the page a

distance of one fourth the point size.

253

move the curser up the page a

distance of one fourth the point size.

253

rotate the page so the page is wider

than it is long.

253

restore page to proper rotation. i.e.

the page is longer than it is wide.

92 to 99

253

the number of points of space

(0-7)

to be placed between lines. 8 point line on

10 point space lead has 2 points of

space between lines.

151 to 199

253

temporary change in number of points of

space (0-48) to be placed between lines.

In order to insert a GPSDC 253 into an ASCII file to be processed. the operator kevboard, iESC3)fxx(ESC4)

where xx is a two digit integer. So the 0-86-253 of the COMPOSITE table becomes 1ESC3)f86(ESC4. on an ASCII

terminal. The ESC is the ASCII Escape code.

,93

piK ..

%5.-.%55**..,

*.~****

--- Página 98 ---

0 01

di*'-

4-)

.4-

o4.

o 0

I-4-

OWQ

'S4.)

0 o-

4.-

LuI

U)~(

.CU

LUI

4-)

4.)

tV4J 4-)

cmer

LUI

S -

0) 4J 0

cat

_ r

tio

~ D4..S2-0

-r-

V)I

11 C)

.4-3

4-3U

4.)

4.)

C.D

P)4)

4-)3Wd

S.-

-0u

r o

-~ I.-

*.-

UiC.

4C)

4-1

S..

-d4-

4-3

r o

03-

Li..

1=04--

4.)

LC)

-(di

+.3

4-)

0C-

C..

4LUJ

CC) w..

F-I-

4-'

todia)

'S-144.)

*-dto

CAU)

OC V)

_r_

-CD

S..

4.)

S..

4-)

LUJ

(1)

1 4

4-)

4.)

4-3

o-F

*LU

CA(

U)'

S..

..J

LU-

LUJ

I-S.

S..

4-)-0

-e-

'4.)

.1-

.1-

uC F

4-'

4-)

CC.")

0L S-

(A-

C) U

4-'

w '

di(

.. J

m~C

4-'

r5di

~--

0D.

co-

C--

-4)I

C~~

LAUU)

4.)

0CL~

-.-

4 .3

4-) LLJ

toC

d U)

C.-d

0S-.

4'~(2

-ea

C- o

LUC./)

4-)

-03

4-)

01).

C/LUJ

34-)

(1)

Cd)

4-)

C..)

14-'

to '

4-'

U)3

di)

CL0

c- di

4-) c:

4 4-4)0

LUI

-C)U

Uro

~4-3

t--

di)

--.

4-'

4-'

U)to

to-

tA 4- to

S. -

:-:p

Udi)

tod

1 -

0..C4-)

4-J

4.3

L.-

0~~*.

LUC/

W4- 3

r_~

04-'

to u

C r_

CrN_

4-'

~ .-

4-)

S- aA

C0>-o~

.'JCA.cr

U) LU0

ciu

4tuo

CLU

LUJ

<-CCP

4.)

m-C.

.. j V)

LUJ

C-)

a0-

LU J

r-4

LUJ

L.A

C.D-

LI..

r14

I-0-

~LUL

LUJ

I- 0-

...

L.)

LU-

>< C

to0-

--- Página 99 ---

RD-A147 588

THE ELECTRONiC TYPESETTING PROGRAM PROGRAMMER'S MANUAL

2/ 2 .

~(U)

ARMY ARMAMENT RESEARCH AND DEVELOPMENT CENTER

RBERDEEN PROVIN.-

J H WHITESIDE ET AL. AUG 84

UNCLASSIFIED ARBRL-R-

79 SBI-D-F388 488

F/G 14/5

zaammmaaaa/z

--- Página 100 ---

L-0

Lm0

111l202

11111.!2

1111J

Ill1.

MICROCOPY

RESOLUTION

TEST

CHART

NATIONAL

BUREAU OF STANDARDS-

1963-A

.,.

.1*.

--- Página 101 ---

TABLE 13

LISTING OF CARLA*BATCHRUNS.CUTMARK

CARLA*BATCHRUNS(L)I.CUTMARK( 1)

@FOR, S DSDG*VIDBLOCK. VID500MAIN, VIDSOOMAIN

DATA (RED(I),I-1,17)/183,172,175,176,177,179,129,127,126,128,150,

1 115,153,156,169,161,182/

C PATCH TO ADD BULLETS TO MAKE EASY AUTOMATIC PAPER CUTTING AT GPO

CARLA MESSINA MAY 1978

-105,111

C MOVE EDGE OF TURN PAGE 24 POINTS AWAY FROM TOP OF FILM TO MAKE PAPER CUT EASY

IF (ITURN .EQ. 0) GO TO 157

IC(M-4)-52

TEMP-0

IC(M-2)-24

157

CALL HEXBYT(TEMPIC(M-1) ,IC(M))

-123

C PUT OUT TWO BIG BULLETS BETWEEN PAGES TO HELP THE AUTOMATIC PAPER CUTTER

C TURN PAGE WILL HAVE NO BULLETS

IF (ITURN .EQ.

1) GO TO 156

C NORMAL OUTPUT PAGE

PT-PTSIZE

PTSIZE-18

MODFI -;7

SYNFRN-132

TEMPlI

10*PWIDTH-160

TEMP- 50*PLENG -800

M=M+3

C SPACE FORWARD TO END OF PAGE

IC(M-2)-70

CALL HEXBYT(TEMPIC(M-1),IC(M))

CALL CARCAL

C ADVANCE DOWN TO END OF PAGE

M-M+3

IC(M-2)-76

CALL HEXBYT(TEMP1 ,IC(M-1) ,IC(M))

M-M+3

IC(M-2)-70

CALL HEXBYT(TEMPIC(M-1),IC(M))

CALL CARCAL

C TAB BACK TO TOP LEFT CORNER

M-M+2

- " -

IC(M-1)-81

IC(M)-O

• •

M=M+ 2

IC(M-1)-85

IC(M)-O

PTSIZE-PT

156

CONTINUE

"-'

-129

C TAB TO TOP OF PAGE

M-M+2

IC(M-1)-85

IC(M)-O

C ADVANCE 10 POINTS

MM+3

IC(M-2)-76

o.A

J.~h

--- Página 102 ---

TABLE 14

Videocomp 500 Command Codes

Hex

Decimal

Name

Bytes

Unites

Remarks

Job ID

End of Record

none

Ignore

Consider

Select Font Directory

Select String Directory 3

RADRU

Font Fetch

Font ID (0-999) Subset (0-5)

1/10 point point size

Font Set Width

1/10 point

Roman

none

Oblique

degrees

angles of 617.

Monofont

none

all spaces = 1 em

Microfont

none

all spaces =

size

Save String

string no = 0-3

string to be saved, end with

string end

Execute String

End String

none

Define Page

points

Width diagonal <81 picas

full face

points

Length diagonal< 81 picas

Define Page

points

Width< 70 picas

line-by-line

points

Length <124 picas

End Page

none

Required

Define area Location

points

Define area Location

points

and rotate 900

points

Define area Location

poi nts

and rotate 1800

poirts

Define area Location

points

a., rotate 2700

points

"J'

, ,""" , ";.

,-""

"""""

.*'

~ .

S." "; -. .','.

". .-- ',','-2,

--- Página 103 ---

TABLE 14 (Continued)

Videocomp 500 Command Codes

Hex

Decimal

Name

Bytes

Unites

Remarks

Basic Space

none

36/100 of current em

Em space

none

Function of current font set wdt

En space

none

of an Em

Thin space

none

h of an Em

Execute user space

none

Space forward

1/50 point

Space backward

1/50 point

Define User Space

1/50 point

Letterspace

1/50 point set to zero after end of every

line

Advance

1/10 point

Reverse

1/10 point use only in full face mode

1/10 point < 72 points

Down

1/10 point < 72 points

Define horizontal

Tab no.

0-256

tab N

1/50 point with respect to left boundary

Move to horizontal

'Tab no.

tab N

Save horizontal Tab N

Tab no.

current horizontal position

Define Vertical Tab N

Tab no.

0-256

1/10 point with respect to top of page

Move to vertical Tab N

Tab no.

Save

vertical Tab N

Tab no.

•56

Save vertical Tab N

Tab no.

Define horizontal

rule N

1/10 point

height of rule

1/10 point

length of rule

•••

--- Página 104 ---

TABLE 14 (Continued)

Videocomp 500 Command Codes

Hex

Decimal

Name

Units

Remarks

Set horizontal rule N

Define Vertical

rule N

1/10 point height of rule

1/10 point width of rule

Set vertical rule N

100

Set rule

1/10 point height of rule

1/10 point width of rule

112

Fill one Character

to horizontal Tab N

Char.

114

Fill one Character

1/50 point

to intermediate position +1

Char

116

Fill two Characters

to horizontal Tab N

Chars.

118

Fill two Characters

1/50 point

to Intermediate position +2

Chars.

--- Página 105 ---

TABLE 15

TYPESETTING MEASUREMENT UNITS AND VIDEOCOMP

PAGE SPECIFICATIONS

MEASUREMENT UNITS:

a. VIDEOCOMP (PHOTO TYPESETTER) UNITS -

Non-dimensional units used

to express the relative sizes of characters

b. POINTS

72 points = 1 inch

c. PICAS

1 PICA

= 12 points

VIDEOCOMP PAGE SIZES:

Standard page size (42 PICAS wide x 62 PICAS high

or 504 points x 744 points)

Maximum page size

550 points wide x 790 points high

FORMULAS FOR CHARACTER SIZE:

2400 x (PICAS/LINE)

NUMBER OF CHARACTERS/LINE = (POINT SIZE) X (INTEGER SET WIDTH)(UNITS)

CHARACTER WIDTH (UNITS)

POINTS/CHARACTER

= LEAD (IN POINTS) X

200

'99

--- Página 106 ---

4-)

0-4

(AZI

=Z0

LU 3LI0

ECL

4-)

LU0

coDI

>.C..

Loco

03.

LL.

CDL.)

4-JF

....3

LA-

-JO

41.

4-)

cou(

Q4.. =

G0O

4..

4J COL.

cmW u

CDL

LL.L

r_. cu

C -

zZf

4- 0

X0J-

u U

CLC

I..

to-

.CL

*u(

S -

0 tv

LLJ

r_()

.03 0)

3:C

o 0.1-

S.-

r-~

C4-

I-J

S-U

U-3

00-

4-)

a)- r_0

r-0

.r'

.,-.a

4-)C.

2c'4

(a-

.0t

4..)

LA.

0r4-

4-)

.QL)

0JC1)

L) CO

=4 ror

0 '0

LIC

A..

0~r

4)- 4.-)

LI-

O4-

~~L4

)I'-

-z r*

La.J

L")I

41X

Z~4

C)~L

LII

P-4

%~~

EUU

m- Z:

U0.

0-CL

LIJ

LA-

LU)

LODCD 0

100

--- Página 107 ---

TABLE 17

REQUIRED CHANGES TO ARMYCARDS OUTPUT

1. Remove the line:

DATA (COMPOS(I), I = 1, 3)/ and its continuation on

the following line. This is found below the bottom of the last ITAB

table.

2. Remove all lines below: DATA ICMPRS, NEND / 567, 569/.

3. Convert the LOOK1 tables into two dimensional tables. Do not alter the

LOOK(2,1) or LOOK(3,I) DATA statements. The LOOKI tables are converted

by finding each DATA (LOOK11(I) statement and changing it to DATA

(LOOK(1,I). The balance of these DATA lines remains unaltered.

4. The modified ARMYCARDS output is put into a file named DSDG*VIDBLOCK.

HELVTIMES.

5. An END statement is put at the end of HELVTIMES.

6. Compile HELVTIMES and store it as DSDG*VIDBLOCK.HELVTIMES.

101

--- Página 108 ---

TABLE 18

THE DSDG*VIDBLOCK.HELVTIMES DATA TABLE

JOHN WHITESIDE

1:C

BALLISTIC RESEARCH LAB ABERDEEN PROVING GROUND

2:CARLA MESSINA NOV 1979 HELVETICA WITH TINES ROMAN ITALICS ROMA(NINE)

3:C

NO WV TABLE IS NEEDED AS ALL ARMY WORK IS MONOWIDTH

BLOCK DATA

COMMON /VID500/ ICfPRS,NEND,LOOK(3,512),ITAB(1500)

DATA (LOOK(2,I),I-I,512)/512*O/

DATA (LOOK(3,I),I-1,512)/512*0/

DATA (LOOK(1,I),I-1,180)

1 1,5,6,7,11,15,19,20,24,28,

10:

2 32,34,38,40,44,48,52,56,60,64,

11:

3 68,72,76,80,84,88,92,96,97,98,

12:

4 99,-103,103,107,111,115,119,123,127,131,

13:

5 135,139,143,147,151,155,159,163,167,171,

14:

6 175,179,183,187,191,195,199,203,207,-208,

15:

7 208,209,-210,210,211,215,219,223,227,231,

16:

8 235,239,243,247,251,255,259,263,267,271,

17:

9 275,279,283,287,291,295,299,303,307,311,

18:

A 315,316,317,-318,3*0,318,319,320,

19:

B 323,324,325,326,327,328,331,332,333,334,

20:

C 335,336,-337,2*0,337,338,339,340,341,

21:

D 342,343,344,345,346,347,348,349,350,-351,

22:

E 0,351,352,353,354,355,356,357,358,359,

23:

F 360,361,362,363,364,365,366,367,368,369,

24:

G 370,371,372,373,374,375,376,377,378,379,

25:

H 380,381,382,383,384,385,386,387,-388,0,

26:

1 388,389,390,391,392,-393,4*0,

27:

DATA(LOOK(1,I),I- 181, 410)/

28:

1 393,394,-395,2*0,395,396,397,398",-399,

29:

2 3*0,399,400,-401,4*0,

30:

3 56*0,401,402,403,404,

31:

4 405,406,407,408,409,410,411,412,413,414,

32:

5 415,416,417,418,419,420,421,422,423,424,

33:

6 425,426,427,428,429,430,431,432,433,434,

34:

7 435,436,437,438,439,-440,441,442,443,

35:

8 444,-445,8*0,

36:

9 445,446,447,448,449,450,451,452,453,545,

37:

A 455,456,457,460,461,462,463,464,

38:

B 465,466,467,468,469,470,471,472,473,474,

39:

C -475,475,-476,0,476,477,478,479,480,481,

40:

D -482,0,482,483,484,485,486,487,488,489,

41:

E 490,491,492,493,494,495,496,497,498,499,

42:

F 500,501,502,503,504,505,506,507,-508,508,

43:

G 509,510,511,512,513,514,515,516,517,518,

44:

H 519,520,521,524,525,526,527,-528,2*0,

45:

I 528,529,530,531,-533,2*0,533,534/

46:

DATA(LOOK(1,I),I- 411, 512)/

47:

1 535,536,537,-538,0,538,539,-540,2*0,

48:

2 6*0,540,541,-542,0,

49:

3 10*0,

50:

4 542,-543,7*0,543,

51:

5 546,-549,549,550,551,552,553,554,555,556,

52:

6 557,558,559,-560,-561,3*0,

53:

7 2*0,561,-562,2*0,562,-563,2*0,

54:

8 32*0/

102

--- Página 109 ---

TABLE 18 (Continued)

THE DSDG*VICBLOCK.HELVTIMES DATA TABLE

55:

DATA(ITAB (1),1-

1, 80)/

56:

1 6986039920, 7288029840, 8932196640, 7355138720,13429933040,

57:

2 21038067314,15040447088,15074001552,13496942880,15141110432,

58:

3 26851541616,26885096080,26918650144,26952204960,18258330224,

59:

4 19097191056,20204486944,19164299936, 6719013872, 8597832304,

60:

5 8899822224, 9470247200, 8966931104, 8597865072, 9168290448,

61:

6 9470279968, 9235399328,13427541362,13463290512,13496844576,

62:

7 13530399392,15038841458,13495337250, 6983877232, 7017431696,

63:

8 7017398928, 7050952992, 7084507808,13429146224,13462700688,

64:

9 7017398928, 7050952992, 7084507808,13429146224,13462700688,

65:

A 13496254752,13529809568,15038153328,15071707792,13494649120,

66:

B 15138816672,15038186096,15071740560,13494681888,15138849440,

67:

C 15038218864,15071773328,13494714656,15138882208,15038251632,

68:

D 15071806096,13494747424,15138914976,15038284400,15071838864,

69:

E 13494780192,15138947744,15038317168,15071871632,13494812960,

70:

F 15138980512,15038906994,15071904400,13494845728,15139013280,

71:

G 15038382704,15071937168,13494878496,15139046048,15038415472/

72:

DATA(ITAB

(I),-

81,160)/

73:

1 15071969936,13494911264,15139078816,15038939762,15072002704,

74:

2 13494944032,15139111584, 6986007152, 7019561616, 7053115680,

75:

3 7086670496, 6983910000, 7017464464, 7051018528, 7084573344,

76:

4 26849444848,26849313776,26849412080,13694829168,15338996368,

77:

5 11077583136,15406105284,17991500400,19367232144,18327044384,

78:

6 19434341024,17991533168,18830394000,18058641696,18897502880,

79:

7 18528436848,19098862224,19669287200,19165971104,19065340528,

80:

8 19367330448,21279932704,19434439328,17454760560,17488315024,

81:

9 19132481824,17555423904,16381051504,16146170512,17253466400,

82:

A 16213279392,20676051568,20441170576,21011595552,20508279456,

83:

B 19333907056,19367461520,21861934688,19434570400, 7254344304,

84:

C 8361640592,11079549216, 8428749472,13428621936,14804353680,

85:

D 12690424096,14871462560,17992057456,19367789200,19938214176,

86:

E 19434898080,15039300208,16415031952,18596069644,16482140832,

87:

F 22555525744,22320644752,25306988832,22387753632,19602768496,

88:

G 19367887504,22058796128,19434996384,20676543088,20710097552/

89:

DATA(ITAB

(1),1- 161, 240)/

90:

1 20206780704,20777206432,16918479472,17220469392,15911846176,

91:

2 17287578272,20676608624,20710163088,20206846240,20777271968,

92:

3 19334464112,19368081576,20743749920,19435127456,17455710832,

93:

4 17220829840,15106900256,17287938720,16392001776,16952427152,

94:

5 17791287584,17019536032,19066389104,19099943568,20744110368,

95:

6 19167052448,17455809136,18294669968,18596659488,18361778848,

96:

7 24972934672,25810895504,25844449582,25878004384,17187439216,

97:

8 18831606416,18328289568,18898715296,17724342896,18026332186,

98:

9 18328322336,18093441696,16919069296,16415752848,18865226061,

99:

A 16482861728, 7520977458, 7521010226,13428458864,26848331088,

100:

B 14768177776,15070167696,13491309024,15137276576,15036646000,

101:

C 16412377744,13493141792,16479486624,13962936944,15070233232,

102:

D 11345690912,15135342112,15036711536,16680878736,14566949152,

103:

E 16747987616,15036744304,15607169680,11345756448,15674278560,

104:

F 8057455216, 9970057872, 8929870112,10037166752,14768374384,

105:

G 16412541584,12687999264,16479650464,15036842608,16144138896,

106:

DATA(ITAB

(I),1- 241, 320)/

107:

1 14298644768,16211247776, 5641634416, 7017366160, 7319355680,

108:

2 7084475040, 5910332016, 7286063760, 6782746912, 7353172640,

109:

3 13694993008,15070724752,14835843360,15137833632, 6178833008,

103

.'..'.',.

,**

.%-

V.....%.%

*-%

_-%,

,*'

. "

--- Página 110 ---

TABLE 18 (Continued)

THE DSDG*VIDBLOCK.HELVTIMES DATA TABLE

110:

4 701769384j, 7856554272, 7084802720,22284993136,23660724880,

111:

5 22352101664,23727833760,15037268592,16144564880,14567506208,

U112:

6 16211673760,15305736816,16949904016,12420055328,17017012896,

113:

7 15037334128,16413065872,12956959008,16480174752,15037366896,

114:

8 16413098640,12956991776,16480207520, 8863384176,10775986832,

115:

9 10272669984,10843095712,13427081840,14534378128, 9467658528,

116:

117:

THIS DATA CONTINUES FOR A WHILE

118:

171:

DATA (ITAB(I),1-

567,

569)/

'V172:

DATA ICNP&S,NEND /567,

569/

174:

END

DSDG*VIDBLOCK(1) .HELVTIMES( 1)

.10

--- Página 111 ---

TABLE 19

FILES NEEDED TO RUN THE TYPESETTING PROGRAM

CARLA*BATCHRUNS.

GPSDC*DICX8.

GPSDC*DICX8S.

DSDG*GOGPO.

DSDGkCARDS.

DSDG*V IDBLOCK.

EXP*RLIB$.

TEXTPROCESS*L IB.

5105

--- Página 112 ---

TABLE 20

COMMANDS TO CHANGE POINT SIZE AND REPOSITION CURSOR

Point Size Change:

A. Leave HOME point size for NEW point size command as put out by

Combined Editing and Manuscript Program.

Es3FNNEs4

where:

ES is the ASCII "ESCAPE" CHARACTER

NN is the point size to change to.

Both N's must be filled

in. Eight point type would be "08".

Command as input to the Typesetting Program

Es3fNNEs4 -

The transformation of "Es3F" to "Es3f" takes

place in CARLA*BATCHRUNS.ASCGPSARMY

Example:

Es3F18E 4 - Shift into 18 point type

B. Return to HOME point size

E 3FXXE 4 - where "XX" is HOME point size

NOTE:

When returning to HOME point size from the NEW point size, the

cursor moves down one line in the NEW poirnt size. This must

be compensated for.

C. Horizontal Cursor Movement:

Where NEW point size characters are to be placed on a line, move up

from the bottom fiducial marks (or bottom line in HOME point size)

using the Vertical Movement Commands.

Shift into the NEW point size

and then space over horizontally to the 1st character's location; put

that character out and move on.

When all characters on the line have

been put out, shift back into HOME point size. Don't forget to con-

pensate for the vertical one line cursor drop after shifting back to

HOME. Also remember that the spaces are measured in the new lead

size (if point size and lead size are different).

.]'.106

-"_

-. -. "-

* .'"A~m

,V,

'V2"' , - ;''

,' ' .-

' '

.'C .

... .

' .... ""'-

"""""""€"""' "

, - :'

--- Página 113 ---

TABLE 20 (Continued)

COMMANDS TO CHANGE POINT SIZE AND REPOSITION CURSOR

Example:

Es3F18Es4 lOb 0 13b 1UP1LINEEs3FO8Es4

where:

b stands for physical blanks left on the card image

of the line.

Explanation:

The HOME point size in the example is 08. At the begin-

ning of the line, shift into 18 point type. Space over

10 18-point blanks from the left margin and put out one

18-point zero.

Move over 13 more 18-point blanks and

put out a "one".

Compensate for vertical cursor move-

ment then return to HOME point size.

D. Vertical Cursor Movement:

UPHALFLINE -

Move cursor up half a line as measured in the current

lead size.

UPILINE

-Move cursor up one full line in current lead size.

UP2LINES

- Move cursor up two full lines in current lead size.

UP5LINES

- Move cursor up five full lines in current lead size.

Example:

Move the cursor up 81 lines in the current lead size

UP5LINESUP2LINESUP1LINEUPHALFLINE

NOTE:

NO spaces are allowed between the commands or inside

them.

E. Strategy:

When two point sizes are to be used on a page, write the entire page

in the HOME lead size. Move up from the page bottom in HOME size,

shift into NEW point size for the line in question, put out the char-

acters required, correct for vertical cursor movement, shift into

HOME size, and move vertically again.

NOTE:

Point size change commands and cursor movement commands should

be the last data on a page - after even the line and shade

commands.

Also in planning the locations of oversize characters, note that

the width in monowidth of an 18 point character is 10.08 points

horizontally. To locate the horizontal position of an oversize

107

--- Página 114 ---

TABLE 20 (Continued)

COMMANDS TO CHANGE POINT SIZE AND REPOSITION CURSOR

character, find the number of 8 point spaces from the left

hand edge it is to be, then multiply by 4.48/10.08 = .4444 to

obtain the number of monowidth 18 point spaces to space over.

Drop fractions of a point - don't round up.

Remember also

that the left hand edge of the table is 16 8-point spaces from

left hand edge of the page.

FORMULA:

To calculate the number of characters (blanks) to space over,

the following formula may also be used:

-O-F HRCTR:[PAGE DISTANCE (INCHES)][200]

.- '*,iNO.

OF CHARACTERS:

[LEAD (POINTS)][CHARACTER WIDTH (UNITS)]

108

4'-

.'.

--- Página 115 ---

REFERENCES

1. Blanton C. Duncan, "Complete Clear Text Representation of Scientific

Documents in Machine Readable Form," National Bureau of Standards Techni-

cal Note 820, U.S. Department of Commerce, February 1974.

2. "Standard Printing Color Catalogue for Mapping, Charting, and Geodetic

Data and Related Products," Defense Mapping Agency, Topographic Center,

Washington, DC, July 1972.

3. Robert C. Thompson, "General Purpose Scientific Document Code User's

Manual,." National Bureau of Standards, unpublished, December 1981.

4. Robert C. Thompson, "General Purpose Scientific Document Code Programmer's

Manual," National Bureau of Standards, unpublished, April 1982.

109

Maul"Ntoa ueuo0tnadupbihd

--- Página 116 ---

5'.

.4'

..-

* .4--

.4-..

5'.'

APPENDIX A

KEYBOARD ENTRY OF TYPESETTING INPUT

55.4.4*

*~.1

-. 5

5'.

.4.

111

.4,

.5.

-'.

.....................

--- Página 117 ---

CONTENTS OF APPENDIX:

A. Introduction

B. Character Entry

1. Input

2. Character Set

3. Character Display

C. Test Formatting

1. Introduction

2. Center Text

3. Flush Right

4. Paragraph

5. Spacing

6. Paging

D. Table Formatting

1. Table Setup

2. Tabbing

E. Typesetting Controls

1. Background

2. Format Parameters

3. Internal Typesetting Commands

F. Complex Text Example

S1',

--- Página 118 ---

KEYBOARD

APPENDIX A

KEYBOARD ENTRY OF TYPESETTING INPUT

A. INTRODUCTION

Although the Electronic Typesetting Program is specially set up to process fixed format

input for firing tables, it retains the ability to process free format input inherited from the NBS

Typographic System. The methods for doing this are detailed in the following sections.

B. CHARACTER ENTRY

1. Input

The Typesetting ASCII input file can be either in fixed format or free format. A fixed

format file, like that created by the Combined Editing and Manuscript Program, only

requires the Electronic Typesetting Program to translate the input data into typesetting

commands. Free format input requires the Program to put the input into a final, edited state

before translating it into typesetting commands.

The most flexible way to create a free format input file is with an ASCII printing

terminal having red and black ribbon shift, half space forward, and reverse platten rotation.

However, any ASCII terminal which allows a non-deleting backspace and the input of

escape sequences can be used.

2. Character Set

aa.

Basic Characters

The ASCII escape character will be represented as 9. Ninety five characters are

added by printing the original set with red ribbon. The 03 sequence indicates a shift to

red ribbon, and 04 a shift to black ribbon. The normal red characters are GPSDC

numbers 97-195 with the exceptions noted in Table 4. There does not have to be a visible

ribbon shift, but it helps make input checking easier.

Example: a Greek alpha (a) is 03aO4.

b. Synthetic Characters

Additional typesetting characters can be created by putting one ASCII character (red

or black) on top of another by using a backspace (1).

Example: a division (-) sign is :b- or -14: The order is not important.

Characters not used when GPSDC was designed have been added with the use of a

"fancy" character set. This character set is entered with ic. An On returns to normal font.

Combining these character extention methods leads to still more characters.

Example: Greater than or equal ( ) is > = but oc> b=On gives .

115

--- Página 119 ---

,'0

3. Character Display

All characters can be changed in three basic ways: modification, line level, and

substitution.

a. Modification

V..

Any GPSDC character can be modified for display in one of eight ways. A character

may not be modified in two ways simultaneously, i.e., the bold and monowidth

modifications can't be used for the same character at the same time. The modifications

available are:

Modification

Example

Normal (Roman)

Small Characters

Bold

Fancy

Italic

Header Bold

Bold Italic

Monowidth

Examples of these modifications in three different type fonts (Times Roman, Bodoni,

and Gothic) are shown in Figure 20. These modifications should not be confused with a

typesetting font. Once a particular font is chosen, all eight modifications of it are

available for use. The two ways of causing a change in modification are shown below:

Modification

Command

Alternate Command

Normal (Roman)

13Fn04

Small Characters

03Fa4

Bold

f3Fb4

Fancy

63Fc04

Italic

63FiW4

63FdL4

Header Bold

03Fe&4

Monowidth

03Fg,4

The Italic modification can also be invoked by underlining the text, and the Bold Face

modification by overprinting the text with red circumflexes. These last two methods

work only when the basic text is in normal modification.

116

--- Página 120 ---

b. Line Level

.A-

The line level is literally the level on a line where a character is displayed. This is

carried as one of the three parts of a GPSDC character: the character itself, the

modification, and the level. The four levels available are:

Code

Description

main line (full size character)

superscript (2/3 size of main line character)

subscript (2/3 size of main line character)

subscript under superscript

Note: the point size is never allowed to be smaller than 5

The code assumes that the first printable character is a main line character.

Subsequent characters may be main line, superscript or subscript. The commands for

altering line level are:

Command

Action

Move next character up 1/2 line from current position

Move next character down 1/2 line from current position

Examples:

Create C9 type commands: C69908

Create C.' type commands:- CO9a8081+ 0

or: C08 +16099a08

Note: all modifications can be present on any level

c. Character Substitution

The fancy character set may be used to introduce characters not found in the normal

character set. This is done by redefining GPSDC characters in terms of Videocomp font

characters. This process is covered in section V.D. of this report. A GPSDC "L" for

instance could be defined as the symbol for lightning in the Fancy font. Then, each time

this symbol was needed, a shift into Fancy modification, an "L." and a return to Normal

modification would put it out.

-11

- .'

117

.5,

--- Página 121 ---

C. TEXT FORMATTING

1. Introduction

Most text editing systems use a simple set of commands to shape text into the desired

form. The Typesetting System subroutines have been designed to accept text formatting

commands from three NBS editing systems: RUNOFF, EDTEXT, and ATS. Only

EDTEXT style commands will be described here.

EDTEXT formatting commands start in column one of a line with "Control a" (if), the

ASCII Start of Heading control character. The text affected by the command begins on the

next line down.

2. Center Text (Atuc)

The instruction ituc is used to center each of the following text lines. It remains in force

until turned off by one of the following commands: Atu, itur, or %tf. These commands are

described later on.

Before the computation of line length is made for centering, leading and trailing blanks

are removed from the line and internal spaces made uniform (expect a single, integer-width

space between words no matter how many were originally there).

The line is centered in the page width set by format parameter three on the *MISC card.

*See

Table 7 and the Appendix section on format parameters for further information on this

parameter.

3. Flush Right (itur)

The command itur sets subsequent lines flush to the right margin using the width set by

format parameter three. Leading and trailing blanks are removed and internal spaces

processed before the computation is done. The command is turned off by Atuc, itf, or Atu.

4. Paragraph (dtf)

The command

tf begins the formation of paragraphs. Paragraphs can be described by

how many spaces the first line is indented, and how far the rest of the lines of the paragraph

are indented. Paragraphs are ended by Att, ittu, Xtuc, itur, or At+n, or a change in line

-indentation.

Block paragraphs must be separated by "(' commands as there is no change in

line indentation.

5. Spacing (it + n)

*'O"

The spacing command has the form t+n where "n" is an integer. #t+0 is used to

separate paragraphs. At + I inserts a space between lines. The size of the space is computed

by adding format parameter two (point size) to format parmeter 5 (number of points to insert

between lines) and multiplying the result by "n". Spacing is independent of all other "i"

commands.

6. Paging (it+ 99)

The command to start a new page is (t +99). The page will either be as long as format

parameter four (page depth) or cut short by the t+ 99 command, whichever comes first.

r.11

U . ""

1 1 8

U. ."

.%-

--- Página 122 ---

D. TABLE FORMATTING

1. Table Set Up

The command to make tables is Xtu. Tables are entered line by line. Adjacent entries in

columns should be separated by at least two spaces. When the table format command is

given, each line is read from left to right. When two or more consequetive spaces are

encountered in a line, the program computes where the next character would be if the line

were typed in monowidth. The cursor is then moved to that point before the next character

is put out. The width of the monowidth character (CHARWD) used to determine the cursor

position is the width of an integer from the chosen font. In general, lower case letters are

smaller than CHARWD and upper case letters are larger. Mathematical symbols are about

twice the size of CHARWD, and punctuation is about half CHARWD's size. The characters in the

escape sequences, and the modification and typesetting commands are not counted when

calculating cursor position.

The table format command is terminated by one of the following commands: Etuc, Etf, or

Atur.

Example (with commands displayed):

CHARWD

FONT

100

Times Roman

104

Bodoni

112

Helvetica

Gothic

2. Tabbing

Tables can be set up by spacing column entries on a line, or entries can be tabbed to the

proper position by using the ASCII tab character. The 0l command sets a tab at the column

the "i" character is in. Any previous 01 commands on the line are ignored when calculating

the tab position. For example, to set tabs after positons 5 and 10 the line would be set as: 5

spaces, 6l, 5 spaces, 0l. Up to 15 tabs may be set on a line. The command 2 clears all tab

settings to the right of the command. To use. the tab settings with table material, simply key

in a tab character at the end of each column entry. When typeset, the cursor will

automatically advance to the next tab setting before putting out succeeding characters. Lines

containing tab sets and and tab clears can be used as desired through out the ASCII file.

Tables are entered as a typist would. The columns are spaced to make the table look good.

Comment entries can run across several columns with no change of format. The only rule of

thumb is to make very sure that each entry in a line is separated by at least two spaces from

the next entry and that no single column entry contains two adjacent spaces. Figure 21 is an

example of a table set up with different sets of tab positions on a single page.

In a file with ASCII tab characters but no tabs set, the *TAB card (see Figure 22) can be

used to set tab positions before the file is processed. The tab settings on this card are altered

when tab clear and tab set lines are encountered in the file.

119

--- Página 123 ---

E. TYPESETTING CONTROLS

1. Background

All commands dealing directly with the typesetting device are done in "red" character

strings, i.e. the commands begin with 03 and end with 04. These commands are printed in

red on an ASCII terminal to avoid any confusion with regular text in a line. When

converted to GPSDC (see Table 4), the commands are represented by the "red" characters

listed in the table.

The typesetting controls are divided into general and specific (one time) orders. The

general typesetting controls are found in the format parameter commands numbered two

through six.

2. Format Parameters

There are seven format parameters:

Parameter

Description

number of files to be processed on an input tape

point size

page width in picas or typesetting units

i.e

page depth in picas or typesetting units

number of points to insert betNween lines (interline leading) Values from 0 to

7 points

Value=0, normal mode printing (long axis of page coincides with long axis

of photocomposition machine paper). Maximum page size 45 picas wide and

65 picas deep.

Value=90, turn page mode (long axis of page perpendicular to long axis of

photocomposition machine paper). maximum page size 45 picas wide and 45

picas deep.

Temporarily change the interline spacing from the value set by format

parameter 5 to a new value between 0 and 48 points. This value is used only

for the spacing with the line following the line with this command.

A format parameter command starts in the first position of a line and is alone on that line.

Six of the seven format parameters (2-7) can be stored as lines within an ASCII file.

Format parameter one, the number of files to be processed from an input tape, cannot be

stored in a line. This command has meaning only before a file is read and therefore is not

valid inside the file.

.1',

%.,

120

C.~

%~.%.

JiJdI

6JI>

--- Página 124 ---

Inside a file, the format parameter commands have the form:

'63fpn=m64

where n = 2,3,4,5,6,7 is the parameter number and 'i' is a positive integer or zero.

Format parameters one through five can be preset before the file is procesed by using the

*MISC card in the computer runstream as shown in Figure 22. The first number on the *MISC

card is format parameter one, the second number is format parameter two, etc. as shown in

Table 7. The numbers set by the *MISC card are changed when a format command is

encountered in the file. The *MISC card is used to set default parameters and to process files

not containing any format parameter commands.

2. Format Parameter Descriptions

a. Format Parameter Two (fp2)

This is the point size used in any formatting done by tf, Atuc, and itur commands.

The point size for a specific bit of formatted text may be altered without changing the

value of fp2 by the use of an internal point size change command. At the end of a

centered line (ituc), flush right line (tur),

or paragraph (Atf), the point size is

automatically returned to the fp2 value. This point size alteration is useful for example,

for setting a table heading in a different point size than the body of the table. It's also

useful for putting footnotes in smaller type than the main text.

b. Format Parameter Three (fp3)

This is the width of the formatted text in picas or typesetting units. Since the

maximum width a page can have is 65 picas, the program interprets any width value over

65 as being typesetting units. There are 2400 Videocomp500 typesetting units to one pica.

Typesetting units would be used for width if, for example, a non-integer width (in picas)

was desired. Since format parameter values must be unsigned integers, the width would

have to be expressed in typesetting units.

Example: set the page width at 20.5 picas

Since this calls for a non-integral width, convert the width to units: 20.5 picas=

49200 units. The width would then be set by: 3fp3 -4920064

c. Format Parameter Four (fp4)

This is the page depth in picas or typesetting units. Caution: make sure the depth

specified is smaller than the value described in fp6.

.1'2

121

,.,

--- Página 125 ---

d. Format Parameter Five (fp5)

This is the space inserted between lines in points. The fp5 command can have values

from 0 to 7 points. When 3fp5=004, the text is "set solid".

Example:

1) If 3fp5 -204 and 3fp2 = 84 the leading will be 10 points.

2) If O3fp5=2E4 and a formatted line starts with an internal points size of 14

(3f144), the line leading will be 16 points.

Note: If the point size is increased within a formatted line, it is possible to overprint

the previous line as the lead is only compu,.d at the start of a formatted line.

e. Format Parameter Six (fp6)

This is used to rotate the page 90 degrees. That is, the long axis of the page is placed

perpendicular to the long axis of the Videocomp 500 page. The Videocomp 500 has a

window of 45 picas by 65 picas. With L3fp6=9004, the page is wider than it is long: 65

picas by 45 picas. If used, fp6 must be 0 or 90. All fp6 commands force a new page.

f. Format Parameter Seven (fp7)

When used, fp7 causes a temporary change in the interline spacing set by fp5. The

interline spacing reverts to the nominal fp5 value after the next line of text is

encountered. The fp7 command can have a value from 0 to 48 points. This gives the fp7

command a finer control of interline spacing than the t + n command.

122

,°-

--- Página 126 ---

3. Internal Typesetting Commands

a. Background

The internal typesetting commands generally allow a finer control of the typesetting

device than the format parameters allow, although some of the commands duplicate

format parameter functions. These special typesetting codes can be inserted anywhere in

the text.

The form of the code is: 3fnnj4 where "nn" is a two digit integer.

b. Typesetting Command Table

Command

Description

f5 to f36

set point size to this number.

fSO

shade from position set by (O3f8364) to this position.

f8.

underline from position set by (O3f8304) to this position.

f82

overscore from position set by (3f8304) to this position.

f83

set a tab at this position on the typesetting device.

f84

tab cursor to position set by (03f8304).

f85

move cursor up toward the top of the page by half the current leading.

fhu

this is an alternate form of f85-format half space up.

f86

center the character following over the preceeding character.

f87

decrease the character position counter, COUNTL, by one. When using f83 with

f84 to create special characters, f87 must be used to decrease COUNTL by one for

each extra character to be overprinted. This adjustment is needed to make the

table formatting work properly.

-. 0.

f88

move the cursor down the page a distance of one-fourth the point size.

f89

move the cursor up the page a distance of one-fourth the point size.

*'."

rotate the page 90 degrees so that it is wider than it is long.

f91

restore page to proper rotation, i.e., the page is longer than it is wide.

f92 to f99

the number of points of space (0-7) to be placed between lines.

An 8 point line on 10 point lead has 2 points of pace between the lines.

123

,%,

--- Página 127 ---

c. Sample Uses of Typesetting Commands

The foreign place names shown in Figure 23 contain special marks not found in

normal type fonts. They can be created from normal type fonts with the use of the

typesetting and formatting commands described. Figure 24 shows how this was done. As

illustrated here, the most useful command for character creation is f86. Figure 25

illustrates several of the special effects that can be created by using combinations of

internal typesetting commands. Figure 26 shows the commands used to make Figure 25.

d. Rules on Rules and Point Sizes

The commands to change point size and their effect are shown in the top of Figure

27.

The following section on rules is shown typeset on the lower half of Figure 27 to

illustrate how the rules described look.

Rules are never to be centered or justified. Rules are made by a series of minuses in a

row. Rules appear in the center of the line and not on the bottom of the line as in

underscoring.

Normal Rule

3Fn4.........................

Light Rule (red Fa)

13Fa4 ...............

3Fn&4

Heavy Rule (Red Fb) 63Fb4 ................

OFn&4

Extra Heavy Rule (red F)

03FfH4 ...........

3Fn4

Double Rule (red Fi)

3Fi4-.............

3Fn4

Normal ... Light 3Fa4 .... 3Fn4 Heavy ,3Fb4 ...... 3Fn4

Extra Heavy 03Ff4 ..... 3Fn4 Double

3Fi£4 .... 3FnO4

e. Spaces and Dashes

Spaces and dashes of fixed width are sometimes needed. The following table shows

how to create them.

Table of Dashes and Spaces

Command

Space and Dash Description

03V4

a very small space suitable for placing between a number and its unit (i.e.

273.15t3!O4K which gives: 273.15 K)

3f4

a space the width of an integer

a very large fixed space the width of a "W" (an ASCII underscore)

.3-44

a small dash (nut dash)

minus size dash

-354

a dash the size of an "M

124

EI%

=;.

. .,.................,..,.,xp.,...:..,,,',y rw',,

,,'P

p;,

W,'p

(."".2p

'p.

"""P",??S

--- Página 128 ---

G. COMPLEX TEXT EXAMPLE

The commands in this report can be combined to do sophisticated typesetting. Figures 28

and 29 contain most of the commands described in this Appendix. Figure 28 shows the typeset

example and Figure 29 shows the commands used to produce it. Some tables in the example are

set in eight point type using 03fp2=804 and others are set in eight point type using fD8.

Modifications are achieved by the 3Fb4 command and by underlining. Interline spacing is

done both by f3fp7=nnj4 and with ot+n commands. The text and tables in Figure 29 are put in

exactly the order given in Figure 28.

p.4.

'125

V .

R,.q

--- Página 129 ---

*0*

,.J.

-. 4

---

I..,

.pJ

~4j

--- Página 130 ---

DISTRIBUTION LIST

No, of

No. of

Copies

Organization

Copies

Organization

Administrator

1 Director

Defense Technical Info Center

US Army Air Mobility Research and

ATTN:

DTIC-DDA

Development Laboratory

Cameron Station

Ames Research Center

Alexandria, VA

22314

Moffett Field, CA

94035

Commander

1 Commander

US Army Materiel Development

US Army Communications Rsch and

and Readiness Command

Development Command

ATTN: DRCDRA-ST.

ATTN: DRSEL-ATDD

5001 Eisenhower Avenue

Fort Monmouth, NJ

07703

Alexandria, VA

22333

1 Commander

Commander

US Army Electronics Research and

Armament R&D Center

Development Command

US Army AMCCOM

Technical Support Activity

ATTN:

DRSMC-TDC(D)

ATTN:

DELSD-L

Dover, NJ

07801

Fort Monmouth, NJ

07703

Commander

1 Commander

Armament R&D Center

US Army Missile Command

US Army AMCCOM

ATTN: DRSMI-R

ATTN:

DRSKC-TSS(D)

Redstone Arsenal, AL

35898

Dover, NJ

07801

1 Commander

1- Commander

US Army Missile Command

US Army Armament, Munitions

ATTN:

DRSMI-YDL

and Chemical Command

Redstone Arsenal, AL

35898

ATTN:

DRSAR-LEP-L(R)

Rock Island, IL

61299

1 Commander

US Army Tank Automotive Command

Director

ATTN:

DRSTA-TSL

Benet Weapons Laboratory

Warren, MI

48090

Armament R&D Center

US Army AMCCOM

1 Director

ATTN:

DRSMC-LCB-TL(D)

US Army TRADOC Systems Analysis

Watervliet, NY

12189

Activity

dATTN:

ATAA-SL

1" Commander

White Sands Missile Range,

US Army Aviation Research

88002

* @and

Development Command

ATTN:

DRDAV-E

1 Commandant

4300 Goodfellow Blvd

US Army Infantry School

St. Louis, MO

63120

ATTN: ATSH-CD-CSO-OR

Commander

Fort Benning, GA

31905

US Army Development

Employment Agency

i AFWL/SUL

ATTN: MODE-TED-SAB

Kirtland AFB, NM

87117

Fort Lewis, WA 98433

1 IIQDA(DAMA-ART-M)

127

Washington, DC 20310

--- Página 131 ---

DISTRIBUTION LIST (Continued

No. of

No. of

Copies

Organization

Copies

Organization

AFATL/BLDG

Information International

ATTN:

Jack Robbins

ATTN:

Mr. Steve Sandborn

Eglin Air Force Base, FL

32542

1747 Old Meadow Road

CmMcLean.

22101

Commander

US Naval Surface Weapons Center Aberdeen Proving Ground

ATTN:

Code G12, Harold Jones

Code K11, Don Daniels

Dir, USAMSAA

Dahlgren, VA

22448

ATTN:

DRXSY-D

DRXSY-MP, H. Cohen

Federal Communications Commission Cdr, USATECOM

Mobile Services Division

ATTN:

DRSTE-TO-F

Common Carrier Bureau

Cdr, CRDC, AMCCOM

ATTN:

Mr. Gaspar Messina, PHYS/EE

ATTN:

DRSMC-CLB-PA

1919 M Street, N.W.

DRSMC-CLN

Washington, DC

20554

DRSMC-CLJ-L

AMCCOM/MISSD Techniques Branch

National Bureau of Standards

ATTN:

DRSMC-MSE-TL

Office of Standard Reference Data

Mr. W. Wallace

A323 Physics Building

ATTN:

Dr. David R. Lide

Washington, DC

20234

National Bureau of Standards

Electronic Typesetting

A813 Administration Building

ATTN:

Ms. R. J. Morehouse

Washington, DC

20234

National Bureau of Standards

Technical Information and

Publications Division

A540 Administration Building

ATTN:

Mr. R. C. MacCullough

Washington, DC

20234

Mr. John Seybold, Editor-In-Chief

The Seybold Report on Publishing

Systems

28936 Cliffside Drive

Malibu, CA

90265

Mrs. P. A. Johnson, Editor

The P.E.O. Record

P.E.O. Authors Book Collection

3700 Grand Avenue

Des Moines, IA 50312

128

--- Página 132 ---

-....

USER EVALUATION SHEET/CHANGE OF ADDRESS

This Laboratory undertakes a continuing effort to improve the quality of the

reports it publishes. Your comments/answers to the items/questions below will

aid us in our efforts.

1. BRL Report Number

Date of Report

2. Date Report Received

3. Does this report satisfy a need?

(Comment on purpose, related project, or

other area of interest for which the report will be used.)

4. flow specifically, is the report being used?

(Information source, design

data, procedure, source of ideas, etc.)

S. Has the information in this report led to any quantitative savings as far

as man-hours or dollars saved, operating costs avoided or efficiencies achieved,

etc?

If so, please elaborate.

6. General Comments.

What do you think should be changed to improve future

reports?

(Indicate changes to organization, technical content, format, etc.)

.-.

Name

ETOrganization

CURRENT

~ADDRESS

ARSAddress

City, State, Zip

7. If indicating a Change of Address or Address Correction, please provide the

New or Correct Address in Block 6 above and the Old or Incorrect address below.

Name

OLD

Organization

ADDRESS

Address

*City,

State, Zip

(Remove this sheet along the perforation, fold as indicated, staple or tape

closed, and mail.)

";,* ,' .. .-.,'. ., •.."."-.-> ; . ."

-.-

.-"'-.-;-4 .;';.%'4'"-.-- ,

.,;- -.

,,* -.

' X:'.

--- Página 133 ---

FOLD HERE

3irector

111

JS Army Ballistic Research Laboratory

NO POSTAGE

_ TTN:

DRXBR-OD-ST

NECESSARY

berdeen Proving Ground, MD 21005-5066

IN THE

UNITED STATES

OFFICIAL BUSINESS

PENALTY FOR PRIVATE USE.

BUSINESS REPLY MAIL

FIRST CLASS

PERMIT NO 12062

WA44INGTONOC

POSTAGE WILL BE PAID BY DEPARTMENT OF THE ARMY

Director

US Army Ballistic Research Laboratory

ATTN: DRXBR-OD-ST

Aberdeen Proving Ground, MD 21005-9989

---

FOLD HERE--

S.*

S %

% , ' * .

' '

°.b

J~~

--- Página 134 ---

*4.

4n4

i, A

161