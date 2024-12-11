# use property for setting and getting


class Color:

    def __init__(self, code, color_name) -> None:
        self.code = code
        self.color_name = color_name

    @property
    def code(self):
        return self._code
    
    @code.setter
    def code(self, code):
        self._code = code


    @property
    def color_name(self):
        return self._color_name
    

    @color_name.setter
    def color_name(self, color_name):
        if color_name:
            self._color_name = color_name
        else:
            raise ValueError("Color name cannot be empty")





green = Color(0X16A34A, "light green")

print(green.code)
print(green.color_name)


green.color_name = "dark green"

print(green.code)
print(green.color_name)
    