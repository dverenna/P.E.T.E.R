"""
personWriter()-program that writes one json per person for multiple people
Drew-11/03/18
"""
import writeDict

def main():
    writeNewPerson("Jorge Silveyra","05/08/1985","A-","Male","JorgeSilveyra.json")
    writeNewPerson("George Benjamin","12/24/1969","AB+","Male","GeorgeBenjamin.json")

def writeNewPerson(name,dOB,bdTyp,gen,outFile):
    writeDict.name = name
    writeDict.dOB = dOB
    writeDict.bdTyp = bdTyp
    writeDict.gen = gen
    writeDict.outputFile = outFile
    writeDict.main()

main()
