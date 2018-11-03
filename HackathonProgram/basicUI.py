#Drew Verenna
#basicUI: A basic user interface
#11/03/2018
from traits.api import *    #Just using star for the traits.api and traitsui.api for now since I don't
from traitsui.api import *  #entirely know which parts will be used yet
import json
import writeDict
import upToChain
import altrpyget

class basicUI(HasTraits):
    Create_New_Person = Button()
    Add_New_Medication = Button()
    Add_New_Allergy = Button()
    Add_New_Surgery = Button()
    Add_New_Appointment = Button()

    #Stuff for initialization
    patient_Name_trait = Str("Patient Name")
    patient_DOB_trait = Str("MM/DD/YYYY")
    patient_BloodType_trait = Str("Patient Blood Type")
    patient_Gender_trait = Str("Patient Gender")

    #New Medication
    medication_type_trait = Str("Enter Name of Medication")
    medication_StartDate_trait = Str("MM/DD/YYYY")
    medication_EndDate_trait = Str("MM/DD/YYYY")

    #New Appointment
    appointment_type_trait = Str("Enter Type of Appointment")
    appointment_Doctor_trait = Str("Enter Doctor Name")
    appointment_Date_trait = Str("MM/DD/YYYY")

    #New Surgery
    surgery_type_trait = Str("Enter Type of Surgery")
    surgery_Surgeon_trait = Str("Enter Surgeon Name")
    surgery_date_trait = Str("MM/DD/YYYY")

    #New Allergy
    allergy_type_trait = Str("Enter the type of Allergy")
    allergy_diagnoseDate_trait = Str("Enter the Date of Diagnosis")

    #Post and Get
    post_text_trait = Str(" ")
    post_output_trait = Str("Output reference token")
    get_text_trait = Str(" ")
    get_input_trait = Str("Input reference token")

    #Generics used for multiple things
    edit_Author_trait = Str("Enter the name of the Author")
    buffer_text = Str(" ")

    #View
    view = View(Item('patient_Name_trait',style = 'simple', label = 'Patient Name'),
                 Item('patient_DOB_trait',style = 'simple', label = 'Patient Date of Birth'),
                 Item('patient_BloodType_trait',style = 'simple',label = 'Patient Blood Type'),
                 Item('patient_Gender_trait',style = 'simple', label = 'Patient Gender'),
                 Item('edit_Author_trait',style = 'simple',label = 'Name of Editor'),
                 Item('Create_New_Person',show_label = False),
                 Item('buffer_text',style='readonly', label=' ',show_label = False),
                 Item('allergy_type_trait',style = 'simple',label = 'Allergy Type'),
                 Item('allergy_diagnoseDate_trait',style = 'simple', label = 'Date of Diagonsis'),
                 Item('edit_Author_trait',style = 'simple',label = 'Name of Editor'),
                 Item('Add_New_Allergy',show_label = False),
                 Item('buffer_text',style='readonly', label=' ',show_label = False),
                 Item('medication_type_trait',style = 'simple', label = "Medication Name"),
                 Item('medication_StartDate_trait',style = 'simple', label = "Medication Start Date"),
                 Item('medication_EndDate_trait',style = 'simple', label = "Medication End Date (Enter '-1' if still taking)"),
                 Item('edit_Author_trait',style = 'simple',label = 'Name of Editor'),
                 Item('Add_New_Medication',show_label = False),
                 Item('buffer_text',style='readonly', label=' ',show_label = False),
                 Item('surgery_type_trait',style = 'simple', label = "Type of Surgery"),
                 Item('surgery_Surgeon_trait',style = 'simple',label = 'Name of Surgeon'),
                 Item('surgery_date_trait',style = 'simple',label = "Date of Surgery"),
                 Item('edit_Author_trait',style = 'simple',label = 'Name of Editor'),
                 Item('Add_New_Surgery',show_label = False),
                 Item('buffer_text',style='readonly', label=' ',show_label = False),
                 Item('appointment_type_trait',style = 'simple',label = 'Type of Appointment'),
                 Item('appointment_Doctor_trait',style = 'simple',label = 'Doctor Name'),
                 Item('edit_Author_trait',style = 'simple',label = 'Name of Editor'),
                 Item('appointment_Date_trait',style = 'simple',label = 'Date of Appointment'),
                 Item('Add_New_Appointment',show_label = False),
                 Item('buffer_text',style='readonly', label=' ',show_label = False),
                 Item('post_text_trait',style='readonly',label= 'Post',show_label = True),
                 Item('post_output_trait',style='readonly',label = 'Output Reference Token',show_label = True),
                 Item('get_text_trait',style = 'readonly',label = 'Get',show_label = True),
                 Item('get_input_trait',style = 'simple',label = 'Input Reference Token',show_label = True),

                 style = "custom", resizable = True
    )

demo = basicUI()

if __name__ == '__main__':
    demo.configure_traits()
