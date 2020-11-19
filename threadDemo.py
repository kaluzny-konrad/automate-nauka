import threading, time
print('Start of program.')

def takeANap():
    time.sleep(2)
    print('Wake up!')

threadObj = threading.Thread(target=takeANap)
threadObj.start()

threadObj2 = threading.Thread(target=print, args=['Cats', 'Dogs', 'Frogs'],
kwargs={'sep': ' & '})
threadObj2.start()

def printZwierzeta():
    print('Cats2', 'Dogs2', 'Frogs2', sep=' & ')

threadObj3 = threading.Thread(target=printZwierzeta)
threadObj3.start()

print('End of program.')

