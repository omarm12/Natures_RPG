# file: cstest.py
# author: colin seifer
# description: test suite for RPG type and stats

from ..src import TypeAssign

def test():
    numPassed = 0
    numFailed = 0
    # test that bottom of accuracy curve is always below 100

    # test that top of accuracy curve is always above or at 100

    # test that accuracy randomization always lands within curve

    # test that attack and defense are calculated correctly

    # test that minimum of attack calculation is 1

    # test that attack calculation subtracts properly from health

    # test that faster observation moves first

    # test that in a tie, either observation may move first

    # test that standard range for base stats is 70-130

    # test that type + modifier works correctly

    # test that type - modifier works correctly

    # test that minimum base stat is 70 without modifiers

    # test that maximum base stat is 130 without modifiers

    # test that minimum base stat is 52 with modifiers

    # test that maximum base stat is 162 with modifiers

    # test that quality modifier for base stats does not exceed range 100-130

    # test that quality modifier for base stats does not go below range 70-130

    # test that unassigned observations return an error
    uType = TypeAssign.Type(0)
    if(uType.AssignType == 'Undefined'):
        numPassed += 1
    else:
        numFailed += 1
        print("Error: unassigned observation did not return \'Undefined\'")

    # test that Mammalia is properly assigned
    mType = TypeAssign.Type(40151)
    if(mType.AssignType == 'Mammalia'):
        numPassed += 1
    else:
        numFailed += 1
        print("Error: Mammalia key mismatch")

    # test that Mammalia gets +eva -acc

    # test that Actinopterygii (fish) is properly assigned
    aType = TypeAssign.Type(47178)
    if(aType.AssignType == 'Actinopterygii'):
        numPassed += 1
    else:
        numFailed += 1
        print("Error: Actinopterygii key mismatch")

    # test that Actinopterygii gets +spd -atk

    # test that Fungi is properly assigned
    fType = TypeAssign.Type(47170)
    if(fType.AssignType == 'Fungi'):
        numPassed += 1
    else:
        numFailed += 1
        print("Error: Fungi key mismatch")

    # test that Fungi gets +hp -eva

    # test that Reptilia is properly assigned 
    rType = TypeAssign.Type(26036)
    if(rType.AssignType == 'Reptilia'):
        numPassed += 1
    else:
        numFailed += 1
        print("Error: Reptilia key mismatch")

    # test that Reptilia gets +acc -eva

    # test that Chromista is properly assigned
    cType = TypeAssign.Type(48222)
    if(cType.AssignType == 'Chromista'):
        numPassed += 1
    else:
        numFailed += 1
        print("Error: Chromista key mismatch")

    # test that Chromista gets +hp -spd

    # test that Plantae is properly assigned
    pType = TypeAssign.Type(47126)
    if(pType.AssignType == 'Plantae'):
        numPassed += 1
    else:
        numFailed += 1
        print("Error: Plantae key mismatch")

    # test that Plantae gets +def -atk

    # test that Animalia is properly assigned
    anType = TypeAssign.Type(1)
    if(anType.AssignType == 'Animalia'):
        numPassed += 1
    else:
        numFailed += 1
        print("Error: Animalia key mismatch")

    # test that Anamalia is balanced

    # test that Mollusca is properly assigned
    moType = TypeAssign.Type(47115)
    if(moType.AssignType == 'Mollusca'):
        numPassed += 1
    else:
        numFailed += 1
        print("Error: Mollusca key mismatch")

    # test that Mollusca gets +def -spd

    # test that Insecta is properly assigned
    iType = TypeAssign.Type(47158)
    if(iType.AssignType == 'Insecta'):
        numPassed += 1
    else:
        numFailed += 1
        print("Error: Insecta key mismatch")

    # test that Insecta gets +spd -def

    # test that Aves (birds) is properly assigned
    avType = TypeAssign.Type(3)
    if(avType.AssignType == 'Aves'):
        numPassed += 1
    else:
        numFailed += 1
        print("Error: Aves key mismatch")

    # test that Aves gets +acc -hp

    # test that Amphibia is properly assigned
    amType = TypeAssign.Type(20978)
    if(amType.AssignType == 'Amphibia'):
        numPassed += 1
    else:
        numFailed += 1
        print("Error: Amphibia key mismatch")

    # test that Amphibia gets +atk - acc

    # test that Arachnida is properly assigned
    arType = TypeAssign.Type(47119)
    if(arType.AssignType == 'Arachnida'):
        numPassed += 1
    else:
        numFailed += 1
        print("Error: Arachnida key mismatch")

    # test that Arachnida gets +atk -def

    # test that Protozoa is properly assigned 
    prType = TypeAssign.Type(47686)
    if(prType.AssignType == 'Protozoa'):
        numPassed += 1
    else:
        numFailed += 1
        print("Error: Protozoa key mismatch")

    # test that Protozoa gets +eva -hp

    # test ancestor ids
    ancestorType = TypeAssign.Type(0, {0, 47686})
    if(prType.AssignType == 'Protozoa'):
        numPassed += 1
    else:
        numFailed += 1
        print("Error: ancestor key mismatch")

    # print results
    print(numPassed, "tests passed!", '\n', numFailed, "tests failed.\n")