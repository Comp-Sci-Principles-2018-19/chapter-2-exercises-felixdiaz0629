time=int(input('what time is it'))
long=int(input('how long do you want your alarm'))
longmodelo=long%14
alarmt=time+longmodulo
alarmt=alarmt%24 #dont go past 24
print('I will set off at',alarmt,', Doctor Luigi')