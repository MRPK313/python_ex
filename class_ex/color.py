# use property for setting and getting


class Color:

    def __init__(self, code, color_name) -> None:
        self.code = code
        self.color_name = color_name


    def _set_code(self, code):
        self._code = code


    def _get_code(self):
        return self._code


    def _set_color_name(self, color_name):
        if color_name:
            self._color_name = color_name
        else:
            raise ValueError("Color name cannot be empty")


    def _get_color_name(self):
        return self._color_name


    

    code = property(_get_code, _set_code)
    color_name = property(_get_color_name, _set_color_name)




green = Color(0X16A34A, "light green")

print(green.code)
print(green.color_name)


green.color_name = "dark green"

print(green.code)
print(green.color_name)
    