import py_11_module

py_11_module.print_helloworld()
print(py_11_module.PI)

from py_11_module import print_helloworld
from py_11_module import PI

print_helloworld()
print(PI)

import py_11_module as test
test.print_helloworld()
print(test.PI)

import py_11_pkg.package_ex as c
c.print_helloworld(5)

from py_11_pkg.package_ex import print_helloworld
print_helloworld(5)
# 오류 print_helloworld()  오버라이딩 되었음

from py_11_pkg import package_ex as pe
pe.print_helloworld(5)
c.print_helloworld(5)