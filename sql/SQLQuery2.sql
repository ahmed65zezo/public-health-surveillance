--The Average of Age (by Gender)
select Gender, avg(age) as 'Average Patient Age'
from Public_health
group by Gender

--Number of Patient (by Location)
select Location, count(Patient_ID) as 'Number of Patient'
from Public_health
group by Location

--Patient Chronic diseases (by Gender)
select Gender,sum(Chronic_Conditions) as 'Have Chronic diseases'
from Public_health
group by Gender

--Immunity level of each patient (by Gender)
select Gender,Immunity_Level, count(patient_id) as 'Number of Patient'
from Public_health
group by Gender,Immunity_Level

--Hospitalization Requirement (by Gender)
select Gender,Hospitalization_Requirement, count(patient_id) as 'Number of Patient'
from Public_health
group by Gender,Hospitalization_Requirement

--Disease outbreaks by location
select Location,Outbreak_Status, count(Patient_ID) as 'Number of Patient'
from Public_health
group by Location, Outbreak_Status