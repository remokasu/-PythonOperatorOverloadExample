import numpy as np


class UnsupportedTypeError(TypeError):
    def __init__(self, operand_type):
        self.message = f"Unsupported operand type: {operand_type}"
        super().__init__(self.message)


class CastError(TypeError):
    def __init__(self, from_type, to_type):
        self.message = f"Cannot cast `{from_type}` to `{to_type}`"
        super().__init__(self.message)


def get_np_type(value: np.ndarray) -> str:
    if value.dtype == np.bool_:
        return "bool"
    elif value.dtype == np.int8:
        return "int8"
    elif value.dtype == np.int16:
        return "int16"
    elif value.dtype == np.int32:
        return "int32"
    elif value.dtype == np.int64:
        return "int64"
    elif value.dtype == np.uint8:
        return "uint8"
    elif value.dtype == np.uint16:
        return "uint16"
    elif value.dtype == np.uint32:
        return "uint32"
    elif value.dtype == np.uint64:
        return "uint64"
    elif value.dtype == np.float16:
        return "float16"
    elif value.dtype == np.float32:
        return "float32"
    elif value.dtype == np.float64:
        return "float64"
    elif value.dtype == np.complex64:
        return "complex64"
    elif value.dtype == np.complex128:
        return "complex128"
    else:
        raise TypeError(f"Unsupported type: {value.dtype}")


def is_np_bool(value: np.ndarray) -> bool:
    if not isinstance(value, np.ndarray):
        return False
    if value.shape != ():
        return False
    return get_np_type(value) == "bool"


def is_np_int(value: np.ndarray) -> bool:
    if not isinstance(value, np.ndarray):
        return False
    if value.shape != ():
        return False
    return get_np_type(value) in ["int8", "int16", "int32", "int64", "uint8", "uint16", "uint32", "uint64"]


def is_np_float(value: np.ndarray) -> bool:
    if not isinstance(value, np.ndarray):
        return False
    if value.shape != ():
        return False
    return get_np_type(value) in ["float16", "float32", "float64"]


def is_np_complex(value: np.ndarray) -> bool:
    if not isinstance(value, np.ndarray):
        return False
    if value.shape != ():
        return False
    return get_np_type(value) in ["complex64", "complex128"]


class Generic:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        raise TypeError(f"Unsupported operand type(s) for +: '{type(self)}' and '{type(other)}')")

    def __radd__(self, other):
        raise TypeError(f"Unsupported operand type(s) for +: '{type(other)}' and '{type(self)}')")

    def __sub__(self, other):
        raise TypeError(f"Unsupported operand type(s) for -: '{type(self)}' and '{type(other)}')")

    def __rsub__(self, other):
        raise TypeError(f"Unsupported operand type(s) for -: '{type(other)}' and '{type(self)}')")

    def __mul__(self, other):
        raise TypeError(f"Unsupported operand type(s) for *: '{type(self)}' and '{type(other)}')")

    def __rmul__(self, other):
        raise TypeError(f"Unsupported operand type(s) for *: '{type(other)}' and '{type(self)}')")

    def __truediv__(self, other):
        raise TypeError(f"Unsupported operand type(s) for /: '{type(self)}' and '{type(other)}')")

    def __rtruediv__(self, other):
        raise TypeError(f"Unsupported operand type(s) for /: '{type(other)}' and '{type(self)}')")

    def __floordiv__(self, other):
        raise TypeError(f"Unsupported operand type(s) for //: '{type(self)}' and '{type(other)}')")

    def __rfloordiv__(self, other):
        raise TypeError(f"Unsupported operand type(s) for //: '{type(other)}' and '{type(self)}')")

    def __mod__(self, other):
        raise TypeError(f"Unsupported operand type(s) for %: '{type(self)}' and '{type(other)}')")

    def __rmod__(self, other):
        raise TypeError(f"Unsupported operand type(s) for %: '{type(other)}' and '{type(self)}')")

    def __pow__(self, other):
        raise TypeError(f"Unsupported operand type(s) for **: '{type(self)}' and '{type(other)}')")

    def __rpow__(self, other):
        raise TypeError(f"Unsupported operand type(s) for **: '{type(other)}' and '{type(self)}')")

    def __neg__(self):
        raise TypeError(f"Bad operand type for unary -: '{type(self)}'")

    def __pos__(self):
        raise TypeError(f"Bad operand type for unary +: '{type(self)}'")

    def __abs__(self):
        raise TypeError(f"Bad operand type for abs(): '{type(self)}'")

    def __invert__(self):
        raise TypeError(f"Bad operand type for unary ~: '{type(self)}'")

    def __iadd__(self, other):
        raise TypeError(f"Unsupported operand type(s) for +=: '{type(self)}' and '{type(other)}')")

    def __isub__(self, other):
        raise TypeError(f"Unsupported operand type(s) for -=: '{type(self)}' and '{type(other)}')")

    def __imul__(self, other):
        raise TypeError(f"Unsupported operand type(s) for *=: '{type(self)}' and '{type(other)}')")

    def __itruediv__(self, other):
        raise TypeError(f"Unsupported operand type(s) for /=: '{type(self)}' and '{type(other)}')")

    def __ifloordiv__(self, other):
        raise TypeError(f"Unsupported operand type(s) for //=: '{type(self)}' and '{type(other)}')")

    def __imod__(self, other):
        raise TypeError(f"Unsupported operand type(s) for %=: '{type(self)}' and '{type(other)}')")

    def __ipow__(self, other):
        raise TypeError(f"Unsupported operand type(s) for **=: '{type(self)}' and '{type(other)}')")

    def __ilshift__(self, other):
        raise TypeError(f"Unsupported operand type(s) for <<=: '{type(self)}' and '{type(other)}')")

    def __irshift__(self, other):
        raise TypeError(f"Unsupported operand type(s) for >>=: '{type(self)}' and '{type(other)}')")

    def __iand__(self, other):
        raise TypeError(f"Unsupported operand type(s) for &=: '{type(self)}' and '{type(other)}')")

    def __ixor__(self, other):
        raise TypeError(f"Unsupported operand type(s) for ^=: '{type(self)}' and '{type(other)}')")

    def __ior__(self, other):
        raise TypeError(f"Unsupported operand type(s) for |=: '{type(self)}' and '{type(other)}')")

    def __eq__(self, other):
        raise TypeError(f"Unsupported operand type(s) for ==: '{type(self)}' and '{type(other)}')")

    def __ne__(self, other):
        raise TypeError(f"Unsupported operand type(s) for !=: '{type(self)}' and '{type(other)}')")

    def __lt__(self, other):
        raise TypeError(f"Unsupported operand type(s) for <: '{type(self)}' and '{type(other)}')")

    def __gt__(self, other):
        raise TypeError(f"Unsupported operand type(s) for >: '{type(self)}' and '{type(other)}')")

    def __le__(self, other):
        raise TypeError(f"Unsupported operand type(s) for <=: '{type(self)}' and '{type(other)}')")

    def __ge__(self, other):
        raise TypeError(f"Unsupported operand type(s) for >=: '{type(self)}' and '{type(other)}')")

    def __and__(self, other):
        raise TypeError(f"Unsupported operand type(s) for &: '{type(self)}' and '{type(other)}')")

    def __or__(self, other):
        raise TypeError(f"Unsupported operand type(s) for |: '{type(self)}' and '{type(other)}')")

    def __xor__(self, other):
        raise TypeError(f"Unsupported operand type(s) for ^: '{type(self)}' and '{type(other)}')")

    def __lshift__(self, other):
        raise TypeError(f"Unsupported operand type(s) for <<: '{type(self)}' and '{type(other)}')")

    def __rshift__(self, other):
        raise TypeError(f"Unsupported operand type(s) for >>: '{type(self)}' and '{type(other)}')")

    def __int__(self):
        return int(self.value)

    def __float__(self):
        return float(self.value)

    def __complex__(self):
        return complex(self.value)

    def __str__(self):
        return str(self.value)

    def __bool__(self):
        return bool(self.value)

    # repr() function =====
    def __repr__(self):
        return f"Generic({self.value})"

    # hash() function =====
    def __hash__(self):
        return hash(self.value)

    def __bytes__(self):
        return bytes(self.value) 


class String(Generic):
    def __init__(self, value):
        self.value = str(value)

    def __add__(self, other):
        if isinstance(other, (String, str)):
            return type(self)(self.value + other)
        else:
            super().__add__(other)

    def __radd__(self, other):
        if isinstance(other, (String, str)):
            return type(self)(other + self.value)
        else:
            super().__radd__(other)

def string(value):
    return String(value)


class Number(Generic):
    priority = 0  # Default priority

    def __init__(self, value):
        self.raw_value = value
        self.value = np.array(value)
        if self.value.shape != ():  # If value is not a scalar
            raise ValueError("Value must be a scalar")

    def cast(self, other):
        if isinstance(other, int) or is_np_int(other):
            return self, Integer(other)
        elif isinstance(other, float) or is_np_float(other):
            return self, Real(other)
        elif isinstance(other, complex) or is_np_complex(other):
            return self, Complex(other)
        elif isinstance(other, bool) or is_np_bool(other):
            return self, Boolean(other)
        elif isinstance(other, list):
            return self, Vector(other)
        elif isinstance(other, Vector):
            return self, other
        elif isinstance(other, Number):
            if other.priority > self.priority:
                return other.cast(self)
            return self, type(self)(other.value)
        else:
            raise UnsupportedTypeError(type(other))

    # ==============================
    # arithmetic operations
    # ==============================
    # + operator =====
    def __add__(self, other):
        self, other = self.cast(other)
        if isinstance(self, Boolean) and isinstance(other, (Integer, Real, Complex)):
            self = Integer(self.value)
        return type(self)(self.value + other.value)

    def __radd__(self, other):
        return self.__add__(other)

    # - operator =====
    def __sub__(self, other):
        self, other = self.cast(other)
        if isinstance(self, Boolean) and isinstance(other, (Integer, Real, Complex)):
            self = Integer(self.value)
        return type(self)(self.value - other.value)

    def __rsub__(self, other):
        self, other = self.cast(other)
        if isinstance(self, Boolean) and isinstance(other, (Integer, Real, Complex)):
            self = Integer(self.value)
        return type(self)(other.value - self.value)

    # * operator =====
    def __mul__(self, other):
        self, other = self.cast(other)
        if isinstance(self, Boolean) and isinstance(other, (Integer, Real, Complex)):
            self = Integer(self.value)
        return type(self)(self.value * other.value)

    def __rmul__(self, other):
        return self.__mul__(other)

    # / operator =====
    def __truediv__(self, other):
        self, other = self.cast(other)
        if isinstance(self, Boolean) and isinstance(other, (Integer, Real, Complex)):
            self = Integer(self.value)
        if other.value == 0:
            raise ZeroDivisionError("Division by zero")
        if isinstance(self, Complex) or isinstance(other, Complex) :
            return Complex(self.value / other.value)
        elif isinstance(self, (Boolean, Integer, Real)) and isinstance(other, (Boolean, Integer, Real)):
            return Real(self.value / other.value)
        else:
            raise TypeError(f"Unsupported operand type(s) for /: '{type(self)}' and '{type(other)}')")

    def __rtruediv__(self, other):
        self, other = self.cast(other)
        if isinstance(self, Boolean) and isinstance(other, (Integer, Real, Complex)):
            self = Integer(self.value)
        if self.value == 0:
            raise ZeroDivisionError("Division by zero")
        if isinstance(self, Complex) or isinstance(other, Complex):
            return Complex(other.value / self.value)
        elif isinstance(self, (Boolean, Integer, Real)) and isinstance(other, (Boolean, Integer, Real)):
            return Real(other.value / self.value)
        else:
            raise TypeError(f"Unsupported operand type(s) for /: '{type(self)}' and '{type(other)}')")

    # // operator =====
    def __floordiv__(self, other):
        self, other = self.cast(other)
        if isinstance(self, Boolean) and isinstance(other, (Integer, Real, Complex)):
            self = Integer(self.value)
        if self.value == 0:
            raise ZeroDivisionError("Division by zero")
        if isinstance(self, Complex) or isinstance(other, Complex):
            return Complex(self.value // other.value)
        elif isinstance(self, (Boolean, Integer, Real)) and isinstance(other, (Boolean, Integer, Real)):
            return Real(self.value // other.value)
        else:
            raise TypeError(f"Unsupported operand type(s) for //: '{type(self)}' and '{type(other)}')")

    def __rfloordiv__(self, other):
        self, other = self.cast(other)
        if isinstance(self, Boolean) and isinstance(other, (Integer, Real, Complex)):
            self = Integer(self.value)
        if self.value == 0:
            raise ZeroDivisionError("Division by zero")
        if isinstance(self, Complex) or isinstance(other, Complex):
            return Complex(other.value // self.value)
        elif isinstance(self, (Boolean, Integer, Real)) and isinstance(other, (Boolean, Integer, Real)):
            return Real(other.value // self.value)
        else:
            raise TypeError(f"Unsupported operand type(s) for //: '{type(self)}' and '{type(other)}')")

    # % operator =====
    def __mod__(self, other):
        self, other = self.cast(other)
        if isinstance(self, Boolean) and isinstance(other, (Integer, Real, Complex)):
            self = Integer(self.value)
        if other.value == 0:
            raise ZeroDivisionError("Division by zero")
        if isinstance(self, Complex) or isinstance(other, Complex):
            return Complex(self.value % other.value)
        elif isinstance(self, (Boolean, Integer, Real)) and isinstance(other, (Boolean, Integer, Real)):
            return Real(self.value % other.value)
        else:
            raise TypeError(f"Unsupported operand type(s) for %: '{type(self)}' and '{type(other)}')")

    def __rmod__(self, other):
        self, other = self.cast(other)
        if isinstance(self, Boolean) and isinstance(other, (Integer, Real, Complex)):
            self = Integer(self.value)
        if self.value == 0:
            raise ZeroDivisionError("Division by zero")
        if isinstance(self, Complex) or isinstance(other, Complex):
            return Complex(other.value % self.value)
        elif isinstance(self, (Boolean, Integer, Real)) and isinstance(other, (Boolean, Integer, Real)):
            return Real(other.value % self.value)
        else:
            raise TypeError(f"Unsupported operand type(s) for %: '{type(self)}' and '{type(other)}')")

    # ** operator =====
    def __pow__(self, other):
        self, other = self.cast(other)
        if isinstance(self, Boolean) and isinstance(other, (Integer, Real, Complex)):
            self = Integer(self.value)
        if isinstance(self, Complex) or isinstance(other, Complex):
            return Complex(self.value ** other.value)
        elif isinstance(self, (Boolean, Integer, Real)) and isinstance(other, (Boolean, Integer, Real)):
            return Real(self.value ** other.value)
        else:
            raise TypeError(f"Unsupported operand type(s) for **: '{type(self)}' and '{type(other)}')")

    def __rpow__(self, other):
        self, other = self.cast(other)
        if isinstance(self, Boolean) and isinstance(other, (Integer, Real, Complex)):
            self = Integer(self.value)
        return type(self)(other.value ** self.value)

    # ==============================
    # unary operator
    # ==============================
    # - operator =====
    def __neg__(self):
        return type(self)(-self.value)

    # + operator =====
    def __pos__(self):
        return type(self)(self.value)

    # abs() function =====
    def __abs__(self):
        return type(self)(abs(self.value))

    # ~ operator =====
    def __invert__(self):
        return type(self)(~self.value)

    # ==============================
    # inplace
    # ==============================
    # += operator =====
    def __iadd__(self, other):
        self, other = self.cast(other)
        if isinstance(self, Boolean) and isinstance(other, (Integer, Real, Complex)):
            self = Integer(self.value)
        if isinstance(other, (Integer, Real, Complex)):
            self.value += other.value
            return self
        else:
            raise TypeError(f"Unsupported operand type(s) for +=: '{type(self)}' and '{type(other)}')")

    # -= operator =====
    def __isub__(self, other):
        self, other = self.cast(other)
        if isinstance(self, Boolean) and isinstance(other, (Integer, Real, Complex)):
            self = Integer(self.value)
        if isinstance(other, (Integer, Real, Complex)):
            self.value -= other.value
            return self
        else:
            raise TypeError(f"Unsupported operand type(s) for -=: '{type(self)}' and '{type(other)}')")

    # *= operator =====
    def __imul__(self, other):
        self, other = self.cast(other)
        if isinstance(self, Boolean) and isinstance(other, (Integer, Real, Complex)):
            self = Integer(self.value)
        if isinstance(other, (Integer, Real, Complex)):
            self.value *= other.value
            return self
        else:
            raise TypeError(f"Unsupported operand type(s) for *=: '{type(self)}' and '{type(other)}')")

    # /= operator =====
    def __itruediv__(self, other):
        self, other = self.cast(other)
        if isinstance(self, Boolean) and isinstance(other, (Integer, Real, Complex)):
            self = Integer(self.value)
        if other.value == 0:
            raise ZeroDivisionError("Division by zero")
        if isinstance(self, Integer):
            self = Real(self.value)
        self.value /= other.value
        return self

    # //= operator =====
    def __ifloordiv__(self, other):
        self, other = self.cast(other)
        if isinstance(self, Boolean) and isinstance(other, (Integer, Real, Complex)):
            self = Integer(self.value)
        if other.value == 0:
            raise ZeroDivisionError("Division by zero")
        self.value //= other.value
        return self

    # %= operator =====
    def __imod__(self, other):
        self, other = self.cast(other)
        if isinstance(self, Boolean) and isinstance(other, (Integer, Real, Complex)):
            self = Integer(self.value)
        if other.value == 0:
            raise ZeroDivisionError("Division by zero")
        self.value %= other.value
        return self

    # **= operator =====
    def __ipow__(self, other):
        self, other = self.cast(other)
        if isinstance(self, Boolean) and isinstance(other, (Integer, Real, Complex)):
            self = Integer(self.value)
        self.value **= other.value
        return self

    # <<= operator =====
    def __ilshift__(self, other):
        self, other = self.cast(other)
        if isinstance(self, Boolean) and isinstance(other, (Integer, Real, Complex)):
            self = Integer(self.value)
        if isinstance(self, Integer) and isinstance(other, (Boolean, Integer)):
            self.value <<= other.value
            return self
        else:
            raise TypeError(f"Unsupported operand type(s) for <<=: '{type(self)}' and '{type(other)}')")

    # >>= operator =====
    def __irshift__(self, other):
        self, other = self.cast(other)
        if isinstance(self, Boolean) and isinstance(other, (Integer, Real, Complex)):
            self = Integer(self.value)
        if isinstance(self, Integer) and isinstance(other, (Boolean, Integer)):
            self.value >>= other.value
            return self
        else:
            raise TypeError(f"Unsupported operand type(s) for >>=: '{type(self)}' and '{type(other)}')")

    # &= operator =====
    def __iand__(self, other):
        self, other = self.cast(other)
        if isinstance(self, Boolean) and isinstance(other, (Integer, Real, Complex)):
            self = Integer(self.value)
        if isinstance(self, Integer) and isinstance(other, (Boolean, Integer)):
            self.value &= other.value
            return self
        else:
            raise TypeError(f"Unsupported operand type(s) for &=: '{type(self)}' and '{type(other)}')")

    # ^= operator =====
    def __ixor__(self, other):
        self, other = self.cast(other)
        if isinstance(self, Boolean) and isinstance(other, (Integer, Real, Complex)):
            self = Integer(self.value)
        if isinstance(self, Integer) and isinstance(other, (Boolean, Integer)):
            self.value ^= other.value
            return self
        else:
            raise TypeError(f"Unsupported operand type(s) for ^=: '{type(self)}' and '{type(other)}')")

    # |= operator =====
    def __ior__(self, other):
        self, other = self.cast(other)
        if isinstance(self, Boolean) and isinstance(other, (Integer, Real, Complex)):
            self = Integer(self.value)
        if isinstance(self, Integer) and isinstance(other, (Boolean, Integer)):
            self.value |= other.value
            return self
        else:
            raise TypeError(f"Unsupported operand type(s) for |=: '{type(self)}' and '{type(other)}')")

    # ==============================
    # comparison operations
    # ==============================
    def __eq__(self, other):
        self, other = self.cast(other)
        if isinstance(other, Vector):
            return Vector(self.value == other.value)
        return Boolean(self.value == other.value)

    def __ne__(self, other):
        self, other = self.cast(other)
        if isinstance(other, Vector):
            return Vector(self.value != other.value)
        return Boolean(self.value != other.value)

    def __lt__(self, other):
        self, other = self.cast(other)
        if isinstance(other, Vector):
            return Vector(self.value < other.value)
        return Boolean(self.value < other.value)

    def __gt__(self, other):
        self, other = self.cast(other)
        if isinstance(other, Vector):
            return Vector(self.value > other.value)
        return Boolean(self.value > other.value)

    def __le__(self, other):
        self, other = self.cast(other)
        if isinstance(other, Vector):
            return Vector(self.value <= other.value)
        return Boolean(self.value <= other.value)

    def __ge__(self, other):
        self, other = self.cast(other)
        if isinstance(other, Vector):
            return Vector(self.value >= other.value)
        return Boolean(self.value >= other.value)

    # ==============================
    # bitwise operations
    # ==============================
    # & operator =====
    def __and__(self, other):
        self, other = self.cast(other)
        if isinstance(self, (Boolean, Integer)) or isinstance(other, (Boolean, Integer)):
            return Integer(self.value & other.value)
        else:
            raise TypeError(f"Unsupported operand type(s) for &: '{type(self)}' and '{type(other)}')")

    def __rand__(self, other):
        return self.__and__(other)

    # | operator =====
    def __or__(self, other):
        self, other = self.cast(other)
        if isinstance(self, (Boolean, Integer)) or isinstance(other, (Boolean, Integer)):
            return Integer(self.value | other.value)
        else:
            raise TypeError(f"Unsupported operand type(s) for |: '{type(self)}' and '{type(other)}')")

    def __ror__(self, other):
        return self.__or__(other)

    # ^ operator =====
    def __xor__(self, other):
        self, other = self.cast(other)
        if isinstance(self, (Boolean, Integer)) or isinstance(other, (Boolean, Integer)):
            return Integer(self.value ^ other.value)
        else:
            raise TypeError(f"Unsupported operand type(s) for ^: '{type(self)}' and '{type(other)}')")

    def __rxor__(self, other):
        return self.__xor__(other)

    # << operator =====
    def __lshift__(self, other):
        self, other = self.cast(other)
        if isinstance(self, (Boolean, Integer)) or isinstance(other, (Boolean, Integer)):
            return Integer(self.value << other.value)
        else:
            raise TypeError(f"Unsupported operand type(s) for <<: '{type(self)}' and '{type(other)}')")

    def __rlshift__(self, other):
        self, other = self.cast(other)
        if isinstance(self, (Boolean, Integer)) or isinstance(other, (Boolean, Integer)):
            return Integer(other << self.value)
        else:
            raise TypeError(f"Unsupported operand type(s) for <<: '{type(self)}' and '{type(other)}')")

    # >> operator =====
    def __rshift__(self, other):
        self, other = self.cast(other)
        if isinstance(self, (Boolean, Integer)) or isinstance(other, (Boolean, Integer)):
            return Integer(self.value >> other.value)
        else:
            raise TypeError(f"Unsupported operand type(s) for >>: '{type(self)}' and '{type(other)}')")

    def __rrshift__(self, other):
        self, other = self.cast(other)
        if isinstance(self, (Boolean, Integer)) or isinstance(other, (Boolean, Integer)):
            return Integer(other.value >> self.value)
        else:
            raise TypeError(f"Unsupported operand type(s) for >>: '{type(self)}' and '{type(other)}')")

    # ==============================
    # other
    # ==============================
    # repr() function =====
    def __repr__(self):
        return f"Number({self.value})"


    def __int__(self):
        return int(self.value)

    def __float__(self):
        return float(self.value)

    def __complex__(self):
        return complex(self.value)

    def __str__(self):
        return str(self.value)

    def __bool__(self):
        return bool(self.value)


class Boolean(Number):
    priority = 0

    def __init__(self, value):
        if isinstance(value, str):
            try:
                value = int(float(value))
                super().__init__(value)
                return
            except ValueError:
                pass
            value = int(not value.lower() in ["false", "0"])
        elif isinstance(value, Number):
            if isinstance(value, Boolean):
                value = value.value
            elif isinstance(value, (Integer, Real, Complex)):
                value = int(bool(value.value))
            elif isinstance(value, Vector):
                value = int(np.all(value.value))
            else:
                raise CastError(type(value), type(self))
        else:
            try:
                value = int(bool(value))
            except ValueError:
                raise ValueError("Value must be convertible to a boolean")
        super().__init__(value)

    def __repr__(self):
        return f"Boolean({self.value})"

def boolean(value):
    return Boolean(value)


class Integer(Number):
    priority = 1

    def __init__(self, value):
        self.base = 10
        if isinstance(value, str):
            try:
                # value = int(value)
                value = np.array(int(value))
            except ValueError:
                raise ValueError("Value must be an integer")
        elif isinstance(value, Number):
            if isinstance(value, Integer):
                value = value.value
            elif isinstance(value, Complex) or isinstance(value, complex) or is_np_complex(value):
                raise CastError(type(value).__name__, type(self).__name__)
            elif isinstance(value, Vector):
                raise CastError(type(value).__name__, type(self).__name__)
            else:
                # value = int(value.value)
                value = np.array(int(value.value))
        else:
            try:
                # value = int(value)
                value = np.array(int(value))
            except ValueError:
                raise ValueError("Value must be an integer")
        super().__init__(value)

    def to_int8(self):
        return Integer(np.int8(self.value))

    def to_int16(self):
        return Integer(np.int16(self.value))

    def to_int32(self):
        return Integer(np.int32(self.value))

    def to_int64(self):
        return Integer(np.int64(self.value))

    def to_uint8(self):
        return Integer(np.uint8(self.value))

    def to_uint16(self):
        return Integer(np.uint16(self.value))

    def to_uint32(self):
        return Integer(np.uint32(self.value))

    def to_uint64(self):
        return Integer(np.uint64(self.value))

    def __iter__(self):
        return iter(range(self.value))

    def __repr__(self):
        return f"Integer({self.value})"

class Integer8(Integer):
    def __init__(self, value):
        super().__init__(np.int8(value))

class Integer16(Integer):
    def __init__(self, value):
        super().__init__(np.int16(value))

class Integer32(Integer):
    def __init__(self, value):
        super().__init__(np.int32(value))

class Integer64(Integer):
    def __init__(self, value):
        super().__init__(np.int64(value))

class UnsignedInteger8(Integer):
    def __init__(self, value):
        super().__init__(np.uint8(value))

class UnsignedInteger16(Integer):
    def __init__(self, value):
        super().__init__(np.uint16(value))

class UnsignedInteger32(Integer):
    def __init__(self, value):
        super().__init__(np.uint32(value))

class UnsignedInteger64(Integer):
    def __init__(self, value):
        super().__init__(np.uint64(value))

def integer(value):
    return Integer(value)

def int8(value):
    return Integer8(np.int8(value))

def int16(value):
    return Integer16(np.int16(value))

def int32(value):
    return Integer32(np.int32(value))

def int64(value):
    return Integer64(np.int64(value))

def uint8(value):
    return UnsignedInteger8(np.uint8(value))

def uint16(value):
    return UnsignedInteger16(np.uint16(value))

def uint32(value):
    return UnsignedInteger32(np.uint32(value))

def uint64(value):
    return UnsignedInteger64(np.uint64(value))


class Real(Number):
    priority = 2

    def __init__(self, value):
        if isinstance(value, str):
            try:
                # value = float(value)
                value = np.array(float(value))
            except ValueError:
                raise ValueError("Value must be a real number")
        elif isinstance(value, Number):
            if isinstance(value, Real):
                value = value.value
            # elif isinstance(value, (Complex, complex)):
            elif isinstance(value, Complex) or isinstance(value, complex) or is_np_complex(value):
                raise CastError(type(value).__name__, type(self).__name__)
            elif isinstance(value, Vector):
                raise CastError(type(value).__name__, type(self).__name__)
            else:
                # value = float(value.value)
                value = np.array(float(value.value))
        else:
            # value = float(value)
            value = np.array(float(value))
        super().__init__(value)

    def __repr__(self):
        return f"Real({self.value})"


class Real32(Real):
    def __init__(self, value):
        super().__init__(np.float32(value))


class Real64(Real):
    def __init__(self, value):
        super().__init__(np.float64(value))


def real(value):
    return Real(value)

def real32(value):
    return Real32(np.float32(value))

def real64(value):
    return Real64(np.float64(value))


class Complex(Number):
    priority = 3

    def __init__(self, value):
        if isinstance(value, str):
            try:
                # value = complex(value)
                value = np.array(complex(value))
            except ValueError:
                raise ValueError("Value must be a complex number")
        elif isinstance(value, Number):
            if isinstance(value, Complex):
                value = value.value
            elif isinstance(value, Vector):
                raise CastError(type(value).__name__, type(self).__name__)
            else:
                # value = complex(value.value)
                value = np.array(complex(value.value))
        else:
            try:
                # value = complex(value)
                value = np.array(complex(value))
            except ValueError:
                raise ValueError("Value must be a complex number")
        self.real = Real(value.real)
        self.imag = Real(value.imag)
        super().__init__(value)

    def __repr__(self):
        return f"Complex({self.value})"


class Complex64(Complex):
    def __init__(self, value):
        super().__init__(np.complex64(value))


class Complex128(Complex):
    def __init__(self, value):
        super().__init__(np.complex128(value))


def imag(value):
    return Complex(value)

def imag64(value):
    return Complex(np.complex64(value))

def imag128(value):
    return Complex(np.complex128(value))


class Vector(Number):
    def __init__(self, value: list | np.ndarray):
        # self.value = value
        self.value = np.array(value)
        if self.value.shape == ():
            raise ValueError("Vector must have at least one dimension")

    def __truediv__(self, other):
        self, other = self.cast(other)
        if isinstance(other, Vector):
            return Vector(self.value / other.value)
        else:
            return Vector(self.value / other)

    def __rtruediv__(self, other):
        self, other = self.cast(other)
        if isinstance(other, Vector):
            return Vector(other.value / self.value)
        else:
            return Vector(other / self.value)

    def __eq__(self, other):
        self, other = self.cast(other)
        if not isinstance(other, Vector):
            return False
        return np.array_equal(self.value, other.value)

    def __ne__(self, other):
        return not self.__eq__(other)

    def __ge__(self, other):
        self, other = self.cast(other)
        if isinstance(other, (Vector, Number)):
            return Vector(self.value >= other.value)
        else:
            return Vector(self.value >= other)

    def __gt__(self, other):
        self, other = self.cast(other)
        if isinstance(other, (Vector, Number)):
            return Vector(self.value > other.value)
        else:
            return Vector(self.value > other)

    def __le__(self, other):
        self, other = self.cast(other)
        if isinstance(other, (Vector, Number)):
            return Vector(self.value <= other.value)
        else:
            return Vector(self.value <= other)

    def __lt__(self, other):
        self, other = self.cast(other)
        if isinstance(other, (Vector, Number)):
            return Vector(self.value < other.value)
        else:
            return Vector(self.value < other)

    def __repr__(self):
        return f"Vector({self.value})"

    def __getitem__(self, item):
        return self.value[item]

    def __setitem__(self, key, value):
        self.value[key] = value

    def __len__(self):
        return len(self.value)

    def __iter__(self):
        return iter(self.value)

    def __next__(self):
        return next(self.value)

    def __contains__(self, item):
        return item in self.value

    def __index__(self):
        return self.value.__index__()

    def __reversed__(self):
        return reversed(self.value)

def vec(value):
    return Vector(value)


class Undefined:
    def __init__(self, symbol):
        self.symbol = symbol

    def __repr__(self):
        return "Undefined symbol: " + self.symbol


class Operator:
    def __init__(self, symbol):
        self.symbol = symbol

    def __repr__(self):
        return f"Operator({self.symbol})"