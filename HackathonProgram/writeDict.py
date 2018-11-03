"""
writeDict: A way to create json files to add them to the blockchain
Drew Verenna 11/3/18
"""
import json

#patientRecords = dict()
#name = "Jorge Benjamin"
#outputFile = "patient.json"
#dOB = "01/01/1970"
#bdTyp = "O-"
#gen = "Male"

def main():
    #print("Main Start")
    global patientRecords
    setUpPatient(name,dOB,bdTyp,gen)
    #testAdd()
    """
    with open(outputFile,"w") as fp:
        json.dump(patientRecords, fp, indent = 4)
    """
    #patientRecords = dict()
    #print("Main End")

"""
def testAdd():
    global patientRecords
    global name
    testName = name
    testDOB = "01/01/1970"
    testBdTyp = "O-"
    testGen = "Male"
    patientRecords = setUpPatient(testName, testDOB, testBdTyp, testGen)
    #addMed("Adderal","Drew","10/15/2017", "03/14/2018")
    #addAllergy("Computers in Class","Peter","11/03/2018")
    #addSurgery("Apendectomy","Emily","Lauren","01/15/2013")
    #addAppt("Physical","Stefanie","Jon Henry","07/07/2017")
"""

def setUpPatient(name, dOB, bdTyp, gen):
    print("Setup start")
    patientRecords = dict()
    patientRecords[name] = dict()
    patientRecords[name]["Date of Birth"] = dOB
    patientRecords[name]["Blood Type"] = bdTyp
    patientRecords[name]["Gender"] = gen
    patientRecords[name]["Medication"] = dict()
    patientRecords[name]["Allergies"] = dict()
    patientRecords[name]["Surgical History"] = dict()
    patientRecords[name]["Appointment History"] = dict()
    return patientRecords
    print("Setup done")

def addMed(patientRecords,name,newMed,editAuth,startDate,endDate):
    print("Med Start")
    #print(patientRecords)
    patientRecords[name]["Medication"][newMed] = dict()
    patientRecords[name]["Medication"][newMed]["Added By"] = editAuth
    patientRecords[name]["Medication"][newMed]["Started using on"] = startDate
    if endDate != -1:
        patientRecords[name]["Medication"][newMed]["Stopped using on"] = endDate
    print("Med End")
    return patientRecords

def addAllergy(patientRecords,name,newAl,editAuth,addDate):
    patientRecords[name]["Allergies"][newAl] = dict()
    patientRecords[name]["Allergies"][newAl]["Added By"] = editAuth
    patientRecords[name]["Allergies"][newAl]["Added on"] = addDate
    return patientRecords

def addSurgery(patientRecords,name,newSur,editAuth,surg,surDat):
    patientRecords[name]["Surgical History"][newSur] = dict()
    patientRecords[name]["Surgical History"][newSur]["Added By"] = editAuth
    patientRecords[name]["Surgical History"][newSur]["Performed By"] = surg
    patientRecords[name]["Surgical History"][newSur]["Performed On"] = surDat
    return patientRecords

def addAppt(patientRecords,name,newAppt, editAuth, doctMet, apptDate):
    patientRecords[name]["Appointment History"][newAppt] = dict()
    patientRecords[name]["Appointment History"][newAppt]["Added By"] = editAuth
    patientRecords[name]["Appointment History"][newAppt]["Met With"] = doctMet
    patientRecords[name]["Appointment History"][newAppt]["Appointment Date"] = apptDate
    return patientRecords

#main()
