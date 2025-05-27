from math import pi

class Calc:
    def __init__(self, *args, **kwargs):
        self.stairs_types: tuple = (
            'прямой марш', 
            'два прямых маршей', 
            'угловая', 
            'винтовая', 
            'поворотная'
        )
        self._step_height: float = .17

        self._current_stair_type: str = '' 
        self._stair_height: float = 0
        self._stair_width: float = 0
        self._area: float = 0

        self._angle: int = 90
        self._r: int = 0

        self._number_of_steps: int = 0
        self._step_pitch: float = 0
        self._step: float = 0
        self.check: float = 0

    # calc -->
    def _determining_number_of_steps(self):
        # Определение количества ступеней
        self._number_of_steps = int(round((self._stair_height / self._step_height), 0))

    def _determining_step_pitch(self):
        # Определение шага ступени
        self._step_pitch = round((self._area / self._stair_width), 2)

    def _determining_step(self):
        # Расчет шага t ступени
        self._step = round((self._step_pitch / self._number_of_steps), 2)

    def _check_ergonomic_ratio(self) -> bool:
        # Проверка эргономичного соотношения (допустимые отклонения +- 0.03 м)
        self.check = 2 * self._step_height + self._step
        return True if .60 <= self.check <= .66 else False

    # Set vars -->
    def set_step_height(self, step_heigh):
        self._step_height = step_heigh

    def set_stair_type(self, stair_type: str):
        self._current_stair_type = stair_type

    def set_stair_height(self, height: float):
        self._stair_height = height
    
    def set_stair_width(self, width: float):
        self._stair_width = width

    def set_area(self, area: float):
        self._area = area

    def set_r(self, r: float):
        self._r = r

    def set_angle(self, angle: float):
        self._angle = angle

    # stairs calc
    def _direct_march(self) -> bool:
        self._determining_number_of_steps()
        self._determining_step_pitch()
        self._determining_step()
        check_result = self._check_ergonomic_ratio()
        return check_result

    def _two_straight_march(self) -> bool:
        self._determining_number_of_steps()
        self._number_of_steps /= 2        # TODO: что если дробное?
        self._determining_step_pitch()
        self._determining_step()
        check_result = self._check_ergonomic_ratio()
        # TODO: Высота маршей?
        return check_result

    def _corner(self):
        self._determining_number_of_steps()
        self._determining_step_pitch()
        self._determining_step()
        self._step -= self._angle
        check_result = self._check_ergonomic_ratio()
        return check_result

    def _screw(self):
        self._determining_number_of_steps()
        self._determining_step_pitch()
        print(self._r)
        self._step = 2 * pi * self._r
        check_result = self._check_ergonomic_ratio()
        return check_result

    def _turning(self):
        self._determining_number_of_steps()
        self._determining_step_pitch()
        self._step = self._area / (self._stair_width + self._angle)
        check_result = self._check_ergonomic_ratio()
        return check_result

    # Main calc
    def calc(self) -> dict:
        type_stair = self._current_stair_type
        if type_stair in self.stairs_types:
            if type_stair == self.stairs_types[0]: 
                check = self._direct_march()
                return {
                    'numOfSteps': self._number_of_steps,
                    'stepHeight': self._step_height,
                    'stepPitch': self._step_pitch,
                    'checkValue': self.check,
                    'checkStatus': check
                }
            elif type_stair == self.stairs_types[1]: 
                check = self._two_straight_march()
                return {
                    'numOfSteps': self._number_of_steps,
                    'stepHeight': self._step_height,
                    'stepPitch': self._step_pitch,
                    'checkValue': self.check,
                    'checkStatus': check
                }
            elif type_stair == self.stairs_types[2]:
                check = self._corner()
                return {
                    'numOfSteps': self._number_of_steps,
                    'stepHeight': self._step_height,
                    'stepPitch': self._step_pitch,
                    'checkValue': self.check,
                    'checkStatus': check
                }
            elif type_stair == self.stairs_types[3]:
                check = self._screw()
                return {
                    'numOfSteps': self._number_of_steps,
                    'stepHeight': self._step_height,
                    'stepPitch': self._step_pitch,
                    'checkValue': self.check,
                    'checkStatus': check
                }
            elif type_stair == self.stairs_types[4]:
                check = self._turning()
                return {
                    'numOfSteps': self._number_of_steps,
                    'stepHeight': self._step_height,
                    'stepPitch': self._step_pitch,
                    'checkValue': self.check,
                    'checkStatus': check
                }

