class Calc:
    def __init__(self, *args, **kwargs):
        self.stairs_types: dict = (
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

        self._number_of_steps: int = 0
        self._step_pitch: float = 0
        self._step: float = 0

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
        check = 2 * self._step_height + self._step
        return True if .60 <= check <= .66 else False

    # Set vars -->
    def set_stair_type(self, stair_type: str):
        self._current_stair_type = stair_type

    def set_stair_height(self, height: float):
        self._stair_height = height
    
    def set_stair_width(self, width: float):
        self._stair_width = width

    def set_area(self, area: float):
        self._area = area

    # stairs calc
    def _direct_march(self):
        self._determining_number_of_steps()
        self._determining_step_pitch()
        self._determining_step()
        check_result = self._check_ergonomic_ratio()

    def _two_straight_march(self):
        pass

    def _corner(self):
        pass

    def _screw(self):
        pass

    def _turning(self):
        pass

    # Main calc
    def calc(self, stair_type: str, stair_widht: float, stair_height: float, area: float):
        self.set_stair_type(stair_type)
        self.set_stair_width(stair_widht)
        self.set_stair_height(stair_height)
        self.set_area(area)

        type_stair = self._current_stair_type
        if type_stair in self.stairs_types:
            if type_stair == self.stairs_types[0]: 
                check = self._direct_march()
                return (
                    self._number_of_steps,
                    self._step_height,
                    self._step_pitch,
                    check
                )
            elif type_stair == self.stairs_types[1]: pass
            elif type_stair == self.stairs_types[2]: pass
            elif type_stair == self.stairs_types[3]: pass
            elif type_stair == self.stairs_types[4]: pass

