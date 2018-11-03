#Drew Verenna
#basicUI: A basic user interface
#11/03/2018
from traits.api import *    #Just using star for the traits.api and traitsui.api for now since I don't
from traitsui.api import *  #entirely know which parts will be used yet
import json
import ast
import writeDict
import upToChain
import altrpyget

patientRecords = dict()

class basicUI(HasTraits):
    Create_New_Person = Button()
    Add_New_Medication = Button()
    Add_New_Allergy = Button()
    Add_New_Surgery = Button()
    Add_New_Appointment = Button()
    Post_Dictionary = Button()
    Get_Dictionary = Button()

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
    post_output_trait = Str("Output reference token")
    get_input_trait = Str("Input reference token")
    get_output_trait = Str("Get Output")

    #Generics used for multiple things
    edit_Author_trait = Str("Enter the name of the Author")
    buffer_text = Str(" ")

    #View
    view = View(Item('patient_Name_trait',style = 'simple', label = 'Patient Name'),
                 Item('patient_DOB_trait',style = 'simple', label = 'Patient Date of Birth'),
                 Item('patient_BloodType_trait',style = 'simple',label = 'Patient Blood Type'),
                 Item('patient_Gender_trait',style = 'simple', label = 'Patient Gender'),
                 Item('Create_New_Person',show_label = False),
                 #Item('buffer_text',style='readonly', label=' ',show_label = False),
                 Item('allergy_type_trait',style = 'simple',label = 'Allergy Type'),
                 Item('allergy_diagnoseDate_trait',style = 'simple', label = 'Date of Diagonsis'),
                 Item('edit_Author_trait',style = 'simple',label = 'Name of Editor'),
                 Item('Add_New_Allergy',show_label = False),
                 #Item('buffer_text',style='readonly', label=' ',show_label = False),
                 Item('medication_type_trait',style = 'simple', label = "Medication Name"),
                 Item('medication_StartDate_trait',style = 'simple', label = "Medication Start Date"),
                 Item('medication_EndDate_trait',style = 'simple', label = "Medication End Date (Enter '-1' if still taking)"),
                 Item('edit_Author_trait',style = 'simple',label = 'Name of Editor'),
                 Item('Add_New_Medication',show_label = False),
                 #Item('buffer_text',style='readonly', label=' ',show_label = False),
                 Item('surgery_type_trait',style = 'simple', label = "Type of Surgery"),
                 Item('surgery_Surgeon_trait',style = 'simple',label = 'Name of Surgeon'),
                 Item('surgery_date_trait',style = 'simple',label = "Date of Surgery"),
                 Item('edit_Author_trait',style = 'simple',label = 'Name of Editor'),
                 Item('Add_New_Surgery',show_label = False),
                 #Item('buffer_text',style='readonly', label=' ',show_label = False),
                 Item('appointment_type_trait',style = 'simple',label = 'Type of Appointment'),
                 Item('appointment_Doctor_trait',style = 'simple',label = 'Doctor Name'),
                 Item('edit_Author_trait',style = 'simple',label = 'Name of Editor'),
                 Item('appointment_Date_trait',style = 'simple',label = 'Date of Appointment'),
                 Item('Add_New_Appointment',show_label = False),
                 #Item('buffer_text',style='readonly', label=' ',show_label = False),
                 Item('Post_Dictionary',show_label = False),
                 Item('post_output_trait',style='simple',label = 'Response',show_label = True),
                 Item('Get_Dictionary',show_label = False),
                 Item('get_input_trait',style = 'simple',label = 'Input',show_label = True),
                 Item('get_output_trait',style = 'readonly',label = 'Response',show_label = True),

                 style = "custom", resizable = True
    )

    def _Create_New_Person_fired(self):
        global patientRecords
        patientRecords = writeDict.setUpPatient(demo.patient_Name_trait,
                                                demo.patient_DOB_trait,
                                                demo.patient_BloodType_trait,
                                                demo.patient_Gender_trait)
        """
        with open("uiPatient.json","w") as fp:
            json.dump(patientRecords, fp, indent = 4)
        """
        print("New Patient done")

    def _Add_New_Medication_fired(self):
        global patientRecords
        patientRecords = writeDict.addMed(patientRecords,
                                          demo.patient_Name_trait,
                                          demo.medication_type_trait,
                                          demo.edit_Author_trait,
                                          demo.medication_StartDate_trait,
                                          demo.medication_EndDate_trait)
        with open("uiPatient.json","w") as fp:
            json.dump(patientRecords, fp, indent = 4)
        print("New Med done")

    def _Add_New_Allergy_fired(self):
        global patientRecords
        patientRecords = writeDict.addAllergy(patientRecords,
                                              demo.patient_Name_trait,
                                              demo.allergy_type_trait,
                                              demo.edit_Author_trait,
                                              demo.allergy_diagnoseDate_trait)
        with open("uiPatient.json","w") as fp:
            json.dump(patientRecords, fp, indent = 4)
        print("New Al Done")

    def _Add_New_Surgery_fired(self):
        global patientRecords
        patientRecords = writeDict.addSurgery(patientRecords,
                                              demo.patient_Name_trait,
                                              demo.surgery_type_trait,
                                              demo.edit_Author_trait,
                                              demo.surgery_Surgeon_trait,
                                              demo.surgery_date_trait)
        with open("uiPatient.json","w") as fp:
            json.dump(patientRecords, fp, indent = 4)
        print("New Surgery Done")

    def _Add_New_Appointment_fired(self):
        global patientRecords
        patientRecords = writeDict.addAppt(patientRecords,
                                           demo.patient_Name_trait,
                                           demo.appointment_type_trait,
                                           demo.edit_Author_trait,
                                           demo.appointment_Doctor_trait,
                                           demo.appointment_Date_trait)
        with open("uiPatient.json","w") as fp:
            json.dump(patientRecords, fp, indent = 4)
        print("New Appointment Done")

    def _Post_Dictionary_fired(self):
        global patientRecords
        ref = upToChain.post(patientRecords)
        demo.post_output_trait = ref

    def _Get_Dictionary_fired(self):
        print("Get Start")
        ref = demo.get_input_trait
        output = altrpyget.get(ref)
        with open("getOutput.json","w") as fp:
            json.dump(ast.literal_eval(output), fp, indent = 4)
        demo.get_output_trait = "Success"

demo = basicUI()

if __name__ == '__main__':
    demo.configure_traits()
