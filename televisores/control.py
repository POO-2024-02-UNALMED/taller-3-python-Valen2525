class Control:
    def __init__(self, TV):
        self._tv = TV

    def enlazar(self, tv):
        self._tv = tv
        tv.setControl(Control)

    def setTv(self, tv):
        self._tv = tv
    def getTv(self):
        return self._tv
    
    def turnOn(self):
        self._tv.turnOn()
    def turnOff(self):
        self._tv.turnOff()

    def canalUp(self):
        self._tv.canalUp()
    def canalDown(self):
        self._tv.canalDown()
    def setCanal(self):
        self._tv.setCanal()

    def volumenUp(self):
        self._tv.volumenUp()
    def volumenDown(self):
        self._tv.volumenDown()
    def setVolumen(self):
        self._tv.setVolumen()
