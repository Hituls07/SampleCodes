class Calculator:

    def __init__(self):
        self

    def power(self, base, pwr):

        try:
            if base >= 0 and pwr >= 0:
                return base ** pwr
            else:
                raise RuntimeError()

        except Exception:
            return 'n and p should be non-negative'



print(Calculator().power(3,-5))

