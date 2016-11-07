__author__ = 'ohodegaa'

from wrappers.motors import Motors


class BeltsController:
    _sharp_turn_dur = 0.6
    _default_speed = 0.6

    def __init__(self):
        self.belts = Motors()
        self.value = None  # [(function, *args)...]

    def update(self, recommendation):
        self.value = recommendation
        self.operationalize()

    def sharp_left(self):
        self.belts.set_value([-self._default_speed, self._default_speed], self._sharp_turn_dur)

    def sharp_right(self):
        self.belts.set_value([self._default_speed, -self._default_speed], self._sharp_turn_dur)

    def backwards(self, dur=None):
        self.belts.set_value([-self._default_speed, -self._default_speed], dur)

    def forward(self, dur=None):
        self.belts.set_value([self._default_speed, self._default_speed], dur)

    def turn_left(self, degree):
        self.belts.set_value([self._default_speed * (1 - degree), self._default_speed])

    def turn_right(self, degree):
        self.belts.set_value([self._default_speed, self._default_speed * (1 - degree)])

    def operationalize(self):
        for (func, args) in self.value:
            func(*args)
            self.belts.forward(speed=1.0, dur=3)

def main():
    belts = BeltsController()
    belts.update([(belts.turn_left, [0.5])])

main()