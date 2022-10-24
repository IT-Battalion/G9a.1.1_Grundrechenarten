class Grundrechnung:
    def __init__(self):
        self.z1 = None
        self.z2 = None
        self.op = None
        self.erg = None
        self.error = None

    def reset(self):
        self.z1 = 0
        self.z2 = 0
        self.op = ""
        self.erg = ""
        self.error = None

    def berechnen(self, z1: int, z2: int, op: str) -> str:
        self.z1 = z1
        self.z2 = z2
        self.op = op[0]
        if self.op == '+':
            self.add()
        elif self.op == '-':
            self.sub()
        elif self.op == '*':
            self.mul()
        elif self.op == '/':
            if z2 == 0:
                self.error = "Fehler: Die Division durch " + "0 ist nicht definiert"
            else:
                self.div()
        else:
            self.error = "Fehler: unbekannter Operator '{}'". \
                format(self.op)
            return self.error

    def add(self) -> None:
        self.erg = str(self.z1 + self.z2)

    def sub(self) -> None:
        self.erg = str(self.z1 - self.z2)

    def mul(self) -> None:
        self.erg = str(self.z1 * self.z2)

    def div(self) -> None:
        self.erg = str(self.z1 / self.z2)


if __name__ == '__main__':
    calc = ((4, 5, '+'), (5, 4, '+'),
            (4, 5, '?'), (5, 0, '/'),
            (4, 5, '-'), (5, 4, '-'),
            (4, 5, '/'), (5, 4, '/'),
            (4, 5, '*'), (5, 4, '*'))
    g = Grundrechnung()
    for c in range(len(calc)):
        e = g.berechnen(calc[c][0], calc[c][1], calc[c][2])
        if e is None:
            print("{0} {2} {1} = {3}".format(g.z1, g.z2, g.op, g.erg))
        else:
            print("Die Berechnung {0} {2} {1}" + " war leider nicht möglich\n {3}".format(g.z1, g.z2, g.op, e))
            g.reset()
