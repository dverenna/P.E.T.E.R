"""
writeDict: A way to create json files to add them to the blockchain
Drew Verenna 11/3/18
"""
import json

patientRecords = dict()
name = "Jorge Benjamin"
outputFile = "patient.json"
dOB = "01/01/1970"
bdTyp = "O-"
gen = "Male"

def main():
    print("Main Start")
    global patientRecords
    setUpPatient(name,dOB,bdTyp,gen)
    #testAdd()
    with open(outputFile,"w") as fp:
        json.dump(patientRecords, fp, indent = 4)
    patientRecords = dict()
    print("Main End")

def testAdd():
    global patientRecords
    global name
    testName = name
    testDOB = "01/01/1970"
    testBdTyp = "O-"
    testGen = "Male"
    patientRecords = setUpPatient(testName, testDOB, testBdTyp, testGen)
    addMed("Adderal","Drew","10/15/2017", "03/14/2018")
    addAllergy("Computers in Class","Peter","11/03/2018")
    addSurgery("Apendectomy","Emily","Lauren","01/15/2013")
    addAppt("Physical","Stefanie","Jon Henry","07/07/2017")

def setUpPatient(name, dOB, bdTyp, gen):
    print("Setup start")
    global patientRecords
    patientRecords[name] = dict()
    patientRecords[name]["Date of Birth"] = dOB
    patientRecords[name]["Blood Type"] = bdTyp
    patientRecords[name]["Gender"] = gen
    patientRecords[name]["Medication"] = dict()
    patientRecords[name]["Allergies"] = dict()
    patientRecords[name]["Surgical History"] = dict()
    patientRecords[name]["Appointment History"] = dict()
    print("Setup done")
    return patientRecords


def addMed(newMed,editAuth,startDate,endDate):
    global patientRecords
    patientRecords[name]["Medication"][newMed] = dict()
    patientRecords[name]["Medication"][newMed]["Added By"] = editAuth
    patientRecords[name]["Medication"][newMed]["Started using on"] = startDate
    if endDate != -1:
        patientRecords[name]["Medication"][newMed]["Stopped using on"] = endDate

def addAllergy(newAl,editAuth,addDate):
    global patientRecords
    patientRecords[name]["Allergies"][newAl] = dict()
    patientRecords[name]["Allergies"][newAl]["Added By"] = editAuth
    patientRecords[name]["Allergies"][newAl]["Added on"] = addDate

def addSurgery(newSur,editAuth,surg,surDat):
    global patientRecords
    patientRecords[name]["Surgical History"][newSur] = dict()
    patientRecords[name]["Surgical History"][newSur]["Added By"] = editAuth
    patientRecords[name]["Surgical History"][newSur]["Performed By"] = surg
    patientRecords[name]["Surgical History"][newSur]["Performed On"] = surDat

def addAppt(newAppt, editAuth, doctMet, apptDate):
    global patientRecords
    patientRecords[name]["Appointment History"][newAppt] = dict()
    patientRecords[name]["Appointment History"][newAppt]["Added By"] = editAuth
    patientRecords[name]["Appointment History"][newAppt]["Met With"] = doctMet
    patientRecords[name]["Appointment History"][newAppt]["Appointment Date"] = apptDate

#main()
