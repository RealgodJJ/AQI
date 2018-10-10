"""
    author: RealgodJJ
    function:
    version: 1.0
    date:
"""


class Person:
    name = []


def main():
    p1 = Person()
    p2 = Person()
    p1.name.append("小明")
    print(p1.name)
    print(p2.name)
    print(Person.name)

if __name__ == '__main__':
    main()
