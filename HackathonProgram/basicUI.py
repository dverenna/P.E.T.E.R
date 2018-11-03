#Drew Verenna
#basicUI: A basic user interface
#11/03/2018
from traits.api import *    #Just using star for the traits.api and traitsui.api for now since I don't
from traitsui.api import *  #entirely know which parts will be used yet
import json
import writeDict

class basicUI(HasTraits):
    Create_New_Person = Button()
    Add_New_Medication = Button()
    Add_New_Allergy = Button()
    Add_New_Surgery = Button()
    Add_New_Appointment = Button()

    patient_Name_trait = Str("Patient Name")
    patient_DOB_trait = Str("MM/DD/YYYY")
