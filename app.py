#import mymodule.mypackage.hello; print mymodule.mypackage.hello.test('Igor')
#from mymodule.mypackage import hello; print hello.test('Igor')

from mymodule.mypackage import hello

print hello.test('Igor')