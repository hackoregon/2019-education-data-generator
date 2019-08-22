# 2019-education-data-generator
Fake data generator to facilitate prototyping of education data collaborative visualizations

## Objective
We want to be able to generate data with some fidelity to intersectionality that obeys
certain assumptions we make.  In that way, we hope to generate several sets of
educational attainment data that developers can use to build visualizations from.

The hope is that when access to real data is granted, we will be able to simply point
the objects built off of our fake data at the real source with as little friction
as possible.

## Process
A Factory is the main driver of the process.  It pulls in the known demographic data
and uses it to generate a set of Student objects of the desired size and with
approximately the correct intersectional demographics.

A Factory is given a Strategy to pass on to each student that helps those students
generate their data.  In general, Students randomly choose for themselves an overall
aptitude bonus as well as a bonus in each of the (so far) four scales the NWEA
measure: English (language usage), Mathematics, Reading, and Science.

The Students are responsible for generating their own Rasch Unit ([RIT]) scores. They
do so by using the Strategy object the Factory points them to. The bonuses "rolled"
are used to modify the base normal score distributions given by the NWEA by grade
for the 2015 student cohort (see [NWEA: 2015 RIT Norms]).  The hope is that this
generates a set of students that seem more like a real cohort, with students of
varying aptitudes and subject preferences.

Once a Factory has generated the appropriate number of Students and each Student
has generated their own aptitude, preferences, and scores, we can then view the student
body demographics to ensure that the randomness has given us something at least close
to what we have counted in the real world Oregon cohorts.

## To Do
There are still several critical tasks that remain.
1. We need to be able to output the Students to a format that could be ingested by a database
(or even to a database itself).  We have a schema to emulate for the students themselves,
but not yet for RIT scores (cf. `Data Elements\Data Model_3.docx` in the `team-education`
shared drive).

In addition, there are several reasonable and interesting stretch goals.
1. These factors should probably be reconsidered, as they are likely increasing score
variation in their current formulation.
1. RIT scales have additive subcategories known as Score Reporting Categories (SRCs).
We know what those are for each of the four scales (in our shared team drive, see
`Data Elements\Assessment Score Reporting Category Descriptions by Subject`).  We could
use the "Pythagorean Theorem of Statistics" to generate SRC sub scores for each category
that add in such a way that they maintain the correct distributions for total scores,
and thus better reflect the schema of the real data.
1. We have some potentially interesting benchmark data in the known schema; we could
therefore attempt to generate benchmark data for each student as well (hopefully tied
to their RIT scores), so that we could prepare for a potential comparison of growth
measurements with achievement measurements.
1. A serious stretch goal would be to generate schools as well as students, but this
would require a significant gathering of complex demographic data as well as a large
refactoring of the Factory object.


## Sources
[RIT]: https://community.nwea.org/docs/DOC-1647
[NWEA: 2015 RIT Norms]: https://www.nwea.org/resource-library/research/2015-normative-data-3
