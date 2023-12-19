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
        elif isinstance(other, Number):
            if other.priority > self.priority:
                return other.cast(self)
            return self, type(self)(other.value)
        else:
            raise UnsupportedTypeError(type(other))

    # ----------------------------------------------------------------------------------------------
    # arithmetic operations
    # ----------------------------------------------------------------------------------------------
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

    # ----------------------------------------------------------------------------------------------
    # unary operator
    # ----------------------------------------------------------------------------------------------
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

    # ----------------------------------------------------------------------------------------------
    # inplace
    # ----------------------------------------------------------------------------------------------
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

    # ----------------------------------------------------------------------------------------------
    # comparison operations
    # ----------------------------------------------------------------------------------------------
    def __eq__(self, other):
        self, other = self.cast(other)
        return Boolean(self.value == other.value)

    def __ne__(self, other):
        self, other = self.cast(other)
        return Boolean(self.value != other.value)

    def __lt__(self, other):
        self, other = self.cast(other)
        return Boolean(self.value < other.value)

    def __gt__(self, other):
        self, other = self.cast(other)
        return Boolean(self.value > other.value)

    def __le__(self, other):
        self, other = self.cast(other)
        return Boolean(self.value <= other.value)

    def __ge__(self, other):
        self, other = self.cast(other)
        return Boolean(self.value >= other.value)

    # ----------------------------------------------------------------------------------------------
    # bitwise operations
    # ----------------------------------------------------------------------------------------------
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

    # ----------------------------------------------------------------------------------------------
    # type conversion
    # ----------------------------------------------------------------------------------------------
    # int() function =====
    def __int__(self):
        return int(self.value)

    # float() function =====
    def __float__(self):
        return float(self.value)

    # complex() function =====
    def __complex__(self):
        return complex(self.value)

    # str() function =====
    def __str__(self):
        return str(self.value)

    # bool() function =====
    def __bool__(self):
        return bool(self.value)

    # ----------------------------------------------------------------------------------------------
    # other
    # ----------------------------------------------------------------------------------------------
    # repr() function =====
    def __repr__(self):
        return f"Number({self.value})"

    # hash() function =====
    def __hash__(self):
        return hash(self.value)

    def __bytes__(self):
        return bytes(self.value)


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
            else:
                raise CastError(type(value), type(self))
        else:
            try:
                value = int(bool(value))
            except ValueError:
                raise ValueError("Value must be convertible to a boolean")
        super().__init__(value)

    def __repr__(self):
        return str(bool(self.value))

    def __str__(self):
        return str(bool(self.value))


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

    def __repr__(self):
        return str(self.value)


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
            else:
                # value = float(value.value)
                value = np.array(float(value.value))
        else:
            # value = float(value)
            value = np.array(float(value))
        super().__init__(value)

    def __repr__(self):
        return str(self.value)


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
        return str(self.value)


class Vector(Number):
    def __init__(self, value):
        # self.value = value
        self.value = np.array(value)
        if self.value.shape == ():
            raise ValueError("Vector must have at least one dimension")


class Undefined:
    def __init__(self, symbol):
        self.symbol = symbol

    def __repr__(self):
        return "Undefined"


class Operator:
    def __init__(self, symbol):
        self.symbol = symbol

    def __repr__(self):
        return f"Operator({self.symbol})"


def test_Integer():
    assert Integer(1) == 1
    assert Integer(1) == Integer("1")
    assert Integer(2) + Integer(2) == Integer(4)
    assert Integer(2) + Integer(2) == 4
    assert Integer(2) + 2 == Integer(4)
    assert Integer(2) + 2 == 4
    assert 2 + Integer(2) == Integer(4)
    assert 2 + Integer(2) == 4
    assert Integer(2) + 2.0 == Real(4.0)
    assert Integer(2) + 2.0 == 4.0
    assert 2.0 + Integer(2) == Real(4.0)
    assert 2.0 + Integer(2) == 4.0
    assert Integer(2) + 2 + 2.0 == Real(6.0)
    assert Integer(2) + 2 + 2.0 == 6.0
    assert 2.0 + 2 + Integer(2) == Real(6.0)
    assert 2.0 + 2 + Integer(2) == 6.0
    assert Integer(2) * Integer(2) == Integer(4)
    assert Integer(2) * Integer(2) == 4
    assert Integer(2) * 2 == Integer(4)
    assert Integer(2) * 2 == 4
    assert 2 * Integer(2) == Integer(4)
    assert 2 * Integer(2) == 4
    assert Integer(2) * 2.0 == Real(4.0)
    assert Integer(2) * 2.0 == 4.0
    assert 2.0 * Integer(2) == Real(4.0)
    assert 2.0 * Integer(2) == 4.0
    assert Integer(2) * 2 * 2.0 == Real(8.0)
    assert Integer(2) * 2 * 2.0 == 8.0
    assert 2.0 * 2 * Integer(2) == Real(8.0)
    assert 2.0 * 2 * Integer(2) == 8.0
    assert Integer(2) - Integer(2) == Integer(0)
    assert Integer(2) - Integer(2) == 0
    assert Integer(2) - 2 == Integer(0)
    assert Integer(2) - 2 == 0
    assert 2 - Integer(2) == Integer(0)
    assert 2 - Integer(2) == 0
    assert Integer(2) - 2.0 == Real(0.0)
    assert Integer(2) - 2.0 == 0.0
    assert 2.0 - Integer(2) == Real(0.0)
    assert 2.0 - Integer(2) == 0.0
    assert Integer(2) - 2 - 2.0 == Real(-2.0)
    assert Integer(2) - 2 - 2.0 == -2.0
    assert 2.0 - 2 - Integer(2) == Real(-2.0)
    assert 2.0 - 2 - Integer(2) == -2.0
    assert Integer(2) / Integer(2) == Real(1.0)
    assert Integer(2) / Integer(2) == 1.0
    assert Integer(2) / 2 == Real(1.0)
    assert Integer(2) / 2 == 1.0
    assert 2 / Integer(2) == Real(1.0)
    assert 2 / Integer(2) == 1.0
    assert Integer(2) / 2.0 == Real(1.0)
    assert Integer(2) / 2.0 == 1.0
    assert 2.0 / Integer(2) == Real(1.0)
    assert 2.0 / Integer(2) == 1.0
    assert Integer(2) / 2 / 2.0 == Real(0.5)
    assert Integer(2) / 2 / 2.0 == 0.5
    assert 2.0 / 2 / Integer(2) == Real(0.5)
    assert 2.0 / 2 / Integer(2) == 0.5
    assert Integer(2) == Integer(2)
    assert Integer(2) == 2
    assert Integer(2) == 2.0
    assert Integer(2) == Real(2.0)
    assert Integer(2) == Complex(2.0)
    assert Integer(1) == Boolean(True)
    assert Integer(0) == Boolean(False)
    assert Integer(1) == True
    assert Integer(0) == False
    assert Integer(2) != Boolean(True)


def test_Real():
    assert Real(1.0) == 1.0
    assert Real(1.0) == Real("1.0")
    assert Real(2.0) + Real(2.0) == Real(4.0)
    assert Real(2.0) + Real(2.0) == 4.0
    assert Real(2.0) + 2 == Real(4.0)
    assert Real(2.0) + 2 == 4.0
    assert 2 + Real(2.0) == Real(4.0)
    assert 2 + Real(2.0) == 4.0
    assert Real(2.0) + 2.0 == Real(4.0)
    assert Real(2.0) + 2.0 == 4.0
    assert 2.0 + Real(2.0) == Real(4.0)
    assert 2.0 + Real(2.0) == 4.0
    assert Real(2.0) + 2 + 2.0 == Real(6.0)
    assert Real(2.0) + 2 + 2.0 == 6.0
    assert 2.0 + 2 + Real(2.0) == Real(6.0)
    assert 2.0 + 2 + Real(2.0) == 6.0
    assert Real(2.0) * Real(2.0) == Real(4.0)
    assert Real(2.0) * Real(2.0) == 4.0
    assert Real(2.0) * 2 == Real(4.0)
    assert Real(2.0) * 2 == 4.0
    assert 2 * Real(2.0) == Real(4.0)
    assert 2 * Real(2.0) == 4.0
    assert Real(2.0) * 2.0 == Real(4.0)
    assert Real(2.0) * 2.0 == 4.0
    assert 2.0 * Real(2.0) == Real(4.0)
    assert 2.0 * Real(2.0) == 4.0
    assert Real(2.0) * 2 * 2.0 == Real(8.0)
    assert Real(2.0) * 2 * 2.0 == 8.0
    assert 2.0 * 2 * Real(2.0) == Real(8.0)
    assert 2.0 * 2 * Real(2.0) == 8.0
    assert Real(2.0) - Real(2.0) == Real(0.0)
    assert Real(2.0) - Real(2.0) == 0.0
    assert Real(2.0) - 2 == Real(0.0)
    assert Real(2.0) - 2 == 0.0
    assert 2 - Real(2.0) == Real(0.0)
    assert 2 - Real(2.0) == 0.0
    assert Real(2.0) - 2.0 == Real(0.0)
    assert Real(2.0) - 2.0 == 0.0
    assert 2.0 - Real(2.0) == Real(0.0)
    assert 2.0 - Real(2.0) == 0.0
    assert Real(2.0) - 2 - 2.0 == Real(-2.0)
    assert Real(2.0) - 2 - 2.0 == -2.0
    assert 2.0 - 2 - Real(2.0) == Real(-2.0)
    assert 2.0 - 2 - Real(2.0) == -2.0
    assert Real(2.0) / Real(2.0) == Real(1.0)
    assert Real(2.0) / Real(2.0) == 1.0
    assert Real(2.0) / 2 == Real(1.0)
    assert Real(2.0) / 2 == 1.0
    assert 2 / Real(2.0) == Real(1.0)
    assert 2 / Real(2.0) == 1.0
    assert Real(2.0) / 2.0 == Real(1.0)
    assert Real(2.0) / 2.0 == 1.0
    assert 2.0 / Real(2.0) == Real(1.0)
    assert 2.0 / Real(2.0) == 1.0
    assert Real(2.0) / 2 / 2.0 == Real(0.5)
    assert Real(2.0) / 2 / 2.0 == 0.5
    assert 2.0 / 2 / Real(2.0) == Real(0.5)
    assert 2.0 / 2 / Real(2.0) == 0.5
    assert Real(2.0) == Real(2.0)
    assert Real(2.0) == 2
    assert Real(2.0) == 2.0
    assert Real(2.0) == Integer(2)
    assert Real(2.0) == Complex(2.0)
    assert Real(1.0) == Boolean(True)
    assert Real(0.0) == Boolean(False)
    assert Real(1.0) == True
    assert Real(0.0) == False
    assert Real(2.0) != Boolean(True)


def test_Complex():
    assert Complex(1 + 1j) == 1 + 1j
    assert Complex(1 + 1j) == Complex("1+1j")
    assert Complex(2 + 2j) + Complex(2 + 2j) == Complex(4 + 4j)
    assert Complex(2 + 2j) + Complex(2 + 2j) == 4 + 4j
    assert Complex(2 + 2j) + 2 == Complex(4 + 2j)
    assert Complex(2 + 2j) + 2 == 4 + 2j
    assert 2 + Complex(2 + 2j) == Complex(2 + (2 + 2j))
    assert 2 + Complex(2 + 2j) == (2 + (2 + 2j))
    assert Complex(2 + 2j) + 2.0 == Complex((2 + 2j) + 2.0)
    assert Complex(2 + 2j) + 2.0 == (2 + 2j) + 2.0
    assert 2.0 + Complex(2 + 2j) == Complex(2.0 + (2 + 2j))
    assert 2.0 + Complex(2 + 2j) == (2.0 + (2 + 2j))
    assert Complex(2 + 2j) + 2 + 2.0 == Complex((2 + 2j) + 2 + 2.0)
    assert Complex(2 + 2j) + 2 + 2.0 == ((2 + 2j) + 2 + 2.0)
    assert 2.0 + 2 + Complex(2 + 2j) == Complex(2.0 + 2 + (2 + 2j))
    assert 2.0 + 2 + Complex(2 + 2j) == (2.0 + 2 + (2 + 2j))
    assert Complex(2 + 2j) * Complex(2 + 2j) == Complex((2 + 2j) * (2 + 2j))
    assert Complex(2 + 2j) * Complex(2 + 2j) == ((2 + 2j) * (2 + 2j))
    assert Complex(2 + 2j) * 2 == Complex((2 + 2j) * 2)
    assert Complex(2 + 2j) * 2 == ((2 + 2j) * 2)
    assert 2 * Complex(2 + 2j) == Complex(2 * (2 + 2j))
    assert 2 * Complex(2 + 2j) == (2 * (2 + 2j))
    assert Complex(2 + 2j) * 2.0 == Complex((2 + 2j) * 2.0)
    assert Complex(2 + 2j) * 2.0 == ((2 + 2j) * 2.0)
    assert 2.0 * Complex(2 + 2j) == Complex(2.0 * (2 + 2j))
    assert 2.0 * Complex(2 + 2j) == (2.0 * (2 + 2j))
    assert Complex(2 + 2j) * 2 * 2.0 == Complex((2 + 2j) * 2 * 2.0)
    assert Complex(2 + 2j) * 2 * 2.0 == ((2 + 2j) * 2 * 2.0)
    assert 2.0 * 2 * Complex(2 + 2j) == Complex(2.0 * 2 * Complex(2 + 2j))
    assert 2.0 * 2 * Complex(2 + 2j) == (2.0 * 2 * Complex(2 + 2j))
    assert Complex(2 + 2j) - Complex(2 + 2j) == Complex((2 + 2j) - (2 + 2j))
    assert Complex(2 + 2j) - Complex(2 + 2j) == ((2 + 2j) - (2 + 2j))
    assert Complex(2 + 2j) - 2 == Complex((2 + 2j) - 2)
    assert Complex(2 + 2j) - 2 == ((2 + 2j) - 2)
    assert 2 - Complex(2 + 2j) == Complex(2 - (2 + 2j))
    assert 2 - Complex(2 + 2j) == (2 - (2 + 2j))
    assert Complex(2 + 2j) - 2.0 == Complex((2 + 2j) - 2.0)
    assert Complex(2 + 2j) - 2.0 == ((2 + 2j) - 2.0)
    assert 2.0 - Complex(2 + 2j) == Complex(2.0 - (2 + 2j))
    assert 2.0 - Complex(2 + 2j) == (2.0 - (2 + 2j))
    assert Complex(2 + 2j) - 2 - 2.0 == Complex((2 + 2j) - 2 - 2.0)
    assert Complex(2 + 2j) - 2 - 2.0 == (2 + 2j) - 2 - 2.0
    assert 2.0 - 2 - Complex(2 + 2j) == Complex(2.0 - 2 - (2 + 2j))
    assert 2.0 - 2 - Complex(2 + 2j) == (2.0 - 2 - (2 + 2j))
    assert Complex(2 + 2j) / Complex(2 + 2j) == Complex((2 + 2j) / (2 + 2j))
    assert Complex(2 + 2j) / Complex(2 + 2j) == (2 + 2j) / (2 + 2j)
    assert Complex(2 + 2j) / 2 == Complex((2 + 2j) / 2)
    assert Complex(2 + 2j) / 2 == ((2 + 2j) / 2)
    assert 2 / Complex(2 + 2j) == Complex(2 / (2 + 2j))
    assert 2 / Complex(2 + 2j) == (2 / (2 + 2j))
    assert Complex(2 + 2j) / 2.0 == Complex((2 + 2j) / 2.0)
    assert Complex(2 + 2j) / 2.0 == (2 + 2j) / 2.0
    assert 2.0 / Complex(2 + 2j) == Complex(2.0 / (2 + 2j))
    assert 2.0 / Complex(2 + 2j) == (2.0 / (2 + 2j))
    assert Complex(2 + 2j) / 2 / 2.0 == Complex((2 + 2j) / 2 / 2.0)
    assert Complex(2 + 2j) / 2 / 2.0 == (2 + 2j) / 2 / 2.0
    assert 2.0 / 2 / Complex(2 + 2j) == Complex(2.0 / 2 / (2 + 2j))
    assert 2.0 / 2 / Complex(2 + 2j) == (2.0 / 2 / (2 + 2j))
    assert Complex(2 + 2j) == Complex(2 + 2j)
    assert Boolean(Complex(1 + 1j)) == Boolean(True)
    assert Boolean(Complex(0 + 0j)) == Boolean(False)
    assert Boolean(Complex(1 + 1j)) == True
    assert Boolean(Complex(0 + 0j)) == False
    assert Boolean(Complex(2 + 2j)) == Boolean(True)


def test_Boolean():
    assert Boolean(True) == Boolean(True)
    assert Boolean(True) == Boolean(1)
    assert Boolean(True) == Boolean(1.0)
    assert Boolean(True) == Boolean("true")
    assert Boolean(True) == Boolean("1")
    assert Boolean(True) == Boolean("1.0")
    assert Boolean(True) == Boolean("TRUE")
    assert Boolean(True) == Boolean("TRUE")
    assert Boolean(True) == Boolean("TrUe")
    assert Boolean(True) == Boolean("TrUe")
    assert Boolean(True) == Boolean("tRuE")
    assert Boolean(True) == Boolean("tRuE")
    assert Boolean(True) == Boolean("t")
    assert Boolean(True) == Boolean("T")
    assert Boolean(True) == Boolean("y")
    assert Boolean(True) == Boolean("Y")
    assert Boolean(True) == Boolean("yes")
    assert Boolean(True) == Boolean("Yes")
    assert Boolean(True) == Boolean("YES")
    assert Boolean(True) == Boolean("yEs")
    assert Boolean(True) == Boolean("yES")
    assert Boolean(True) == Boolean("YeS")
    assert Boolean(True) == Boolean("YeS")
    assert Boolean(True) == Boolean("YEs")
    assert Boolean(False) == Boolean(False)
    assert Boolean(False) == Boolean(0)
    assert Boolean(False) == Boolean(0.0)
    assert Boolean(False) == Boolean("false")
    assert Boolean(False) == Boolean("0")
    assert Boolean(False) == Boolean("0.0")
    assert Boolean(False) == Boolean("FALSE")
    assert (Integer(1) > Integer(0)) == Boolean(True)
    assert (Integer(1) < Integer(0)) == Boolean(False)
    assert (Integer(1) == Integer(1)) == Boolean(True)
    assert (Integer(1) == Integer(0)) == Boolean(False)
    if Boolean(True) == True:
        assert True
    else:
        assert False
    if Boolean(False) == False:
        assert True
    assert Boolean(0) == bool(0)
    assert Boolean(1) == bool(1)
    assert Boolean(1.1) == bool(1.1)
    assert Boolean(2 + 5j) == bool(2 + 5j)
    assert Boolean("True") == True
    assert Boolean("False") == False
    assert Boolean("1") == True
    assert Boolean("0") == False
    assert Boolean("1.1") == True
    assert Boolean("2+5j") == True
    assert Boolean("2 + 5j") == True


def test_logic():
    def excute(op, a, b, expected):
        try:
            result = op(a, b)
            assert result == expected, f"Expected {expected} but got {result}"
        except TypeError:
            assert expected == TypeError
    assert Boolean(True) & Boolean(True) == Boolean(True)
    assert Boolean(True) & Boolean(False) == Boolean(False)
    assert Boolean(False) & Boolean(True) == Boolean(False)
    assert Boolean(False) & Boolean(False) == Boolean(False)
    assert Boolean(True) | Boolean(True) == Boolean(True)
    assert Boolean(True) | Boolean(False) == Boolean(True)
    assert Boolean(False) | Boolean(True) == Boolean(True)
    assert Boolean(False) | Boolean(False) == Boolean(False)
    assert Boolean(True) & True == Boolean(True)
    assert Boolean(True) & False == Boolean(False)
    assert Boolean(False) & True == Boolean(False)
    assert Boolean(False) & False == Boolean(False)
    assert True & Boolean(True) == Boolean(True)
    assert True & Boolean(False) == Boolean(False)
    assert False & Boolean(True) == Boolean(False)
    assert False & Boolean(False) == Boolean(False)
    assert Boolean(True) | True == Boolean(True)
    assert Boolean(True) | False == Boolean(True)
    assert Boolean(False) | True == Boolean(True)
    assert Boolean(False) | False == Boolean(False)
    assert True | Boolean(True) == Boolean(True)
    assert True | Boolean(False) == Boolean(True)
    assert False | Boolean(True) == Boolean(True)
    assert False | Boolean(False) == Boolean(False)
    assert Boolean(True) & 1 == Boolean(True)
    assert Boolean(True) & 0 == Boolean(False)
    assert Boolean(False) & 1 == Boolean(False)
    assert Boolean(False) & 0 == Boolean(False)
    assert 1 & Boolean(True) == Boolean(True)
    assert 1 & Boolean(False) == Boolean(False)
    assert 0 & Boolean(True) == Boolean(False)
    assert 0 & Boolean(False) == Boolean(False)
    assert Boolean(True) | 1 == Boolean(True)
    assert Boolean(True) | 0 == Boolean(True)
    assert Boolean(False) | 1 == Boolean(True)
    assert Boolean(False) | 0 == Boolean(False)
    assert 1 | Boolean(True) == Boolean(True)
    assert 1 | Boolean(False) == Boolean(True)
    assert 0 | Boolean(True) == Boolean(True)
    assert 0 | Boolean(False) == Boolean(False)
    assert Integer(5) & Integer(3) == Integer(1)
    assert Integer(5) | Integer(3) == Integer(7)
    try:
        assert Integer(5) & Real(3.0) == Integer(1)
        assert False
    except TypeError:
        assert True
    try:
        assert Integer(5) | Real(3.0) == Integer(7)
        assert False
    except TypeError:
        assert True
    try:
        assert Real(5.0) & Integer(3) == Integer(1)
        assert False
    except TypeError:
        assert True
    try:
        assert Real(5.0) | Integer(3) == Integer(7)
        assert False
    except TypeError:
        assert True
    try:
        assert Real(5.0) & Real(3.0) == Integer(1)
        assert False
    except TypeError:
        assert True
    try:
        assert Real(5.0) | Real(3.0) == Integer(7)
        assert False
    except TypeError:
        assert True
    try:
        assert Integer(5) & Complex(3 + 0j) == Integer(1)
        assert False
    except TypeError:
        assert True
    try:
        assert Integer(5) | Complex(3 + 0j) == Integer(7)
        assert False
    except TypeError:
        assert True
    try:
        assert Complex(5 + 0j) & Integer(3) == Integer(1)
        assert False
    except TypeError:
        assert True
    try:
        assert Complex(5 + 0j) | Integer(3) == Integer(7)
        assert False
    except TypeError:
        assert True
    try:
        assert Complex(5 + 0j) & Complex(3 + 0j) == Integer(1)
        assert False
    except TypeError:
        assert True
    try:
        assert Complex(5 + 0j) | Complex(3 + 0j) == Integer(7)
        assert False
    except TypeError:
        assert True


def test_bitwise():
    def excute(op, a, b, expected):
        try:
            result = op(a, b)
            assert result == expected, f"Expected {expected} but got {result}"
        except TypeError:
            assert expected == TypeError

    a = Integer(10)
    b = Integer(2)
    excute(lambda a, b: a & b, a, b, Integer(2))
    excute(lambda a, b: a | b, a, b, Integer(10))
    excute(lambda a, b: a ^ b, a, b, Integer(8))
    excute(lambda a, b: a << b, a, b, Integer(40))
    excute(lambda a, b: a >> b, a, b, Integer(2))
    excute(lambda a, b: ~a, a, None, Integer(-11))

    a = Integer(10)
    b = 2
    excute(lambda a, b: a & b, a, b, Integer(2))
    excute(lambda a, b: a | b, a, b, Integer(10))
    excute(lambda a, b: a ^ b, a, b, Integer(8))
    excute(lambda a, b: a << b, a, b, Integer(40))
    excute(lambda a, b: a >> b, a, b, Integer(2))
    excute(lambda a, b: ~a, a, None, Integer(-11))

    a = 10
    b = Integer(2)
    excute(lambda a, b: a & b, a, b, Integer(2))
    excute(lambda a, b: a | b, a, b, Integer(10))
    excute(lambda a, b: a ^ b, a, b, Integer(8))
    excute(lambda a, b: a << b, a, b, Integer(40))
    excute(lambda a, b: a >> b, a, b, Integer(2))
    excute(lambda a, b: ~a, a, None, Integer(-11))

    a = Integer(10)
    b = Real(2.0)
    excute(lambda a, b: a & b, a, b, TypeError)
    excute(lambda a, b: a | b, a, b, TypeError)
    excute(lambda a, b: a ^ b, a, b, TypeError)
    excute(lambda a, b: a << b, a, b, TypeError)
    excute(lambda a, b: a >> b, a, b, TypeError)
    excute(lambda a, b: ~a, a, None, TypeError)

    a = Real(10.0)
    b = Integer(2)
    excute(lambda a, b: a & b, a, b, TypeError)
    excute(lambda a, b: a | b, a, b, TypeError)
    excute(lambda a, b: a ^ b, a, b, TypeError)
    excute(lambda a, b: a << b, a, b, TypeError)
    excute(lambda a, b: a >> b, a, b, TypeError)
    excute(lambda a, b: ~a, a, None, TypeError)

    a = Integer(10)
    b = Complex(2 + 0j)
    excute(lambda a, b: a & b, a, b, TypeError)
    excute(lambda a, b: a | b, a, b, TypeError)
    excute(lambda a, b: a ^ b, a, b, TypeError)
    excute(lambda a, b: a << b, a, b, TypeError)
    excute(lambda a, b: a >> b, a, b, TypeError)
    excute(lambda a, b: ~a, a, None, TypeError)


def test_cast():
    assert Real(Integer(1)) == Real(1.0)
    assert isinstance(Real(Integer(1.0)), Real)

    assert Integer(Real(1.0)) == Integer(1)
    assert isinstance(Integer(Real(1.0)), Integer)

    assert Complex(Integer(1)) == Complex(1 + 0j)
    assert isinstance(Complex(Integer(1)), Complex)

    try:
        assert Integer(Complex(1 + 0j)) == Integer(1)
        assert False
    except CastError:
        assert True

    try:
        assert Real(Complex(1 + 0j)) == Real(1.0)
        assert False
    except CastError:
        assert True

    assert Complex(Real(1.0)) == Complex(1 + 0j)
    assert isinstance(Complex(Real(1.0)), Complex)

    assert Integer(Real(1.0)) == Integer(1)
    assert isinstance(Integer(Real(1.0)), Integer)

    assert Real(Integer(1)) == Real(1.0)
    assert isinstance(Real(Integer(1)), Real)


def test_inplace():
    a = Integer(10)
    b = Integer(2)
    a += b
    assert a == Integer(12)
    a = Integer(10)
    a -= b
    assert a == Integer(8)
    a = Integer(10)
    a -= 5
    assert a == Integer(5)

    a = Integer(10)
    a *= b
    assert a == Integer(20)
    a = Integer(10)
    a *= 5
    assert a == Integer(50)

    a = Integer(10)
    a /= b
    assert a == Integer(5)
    a = Integer(10)
    a /= 5
    assert a == Integer(2)

    a = Integer(10)
    a //= b
    assert a == Integer(5)
    a = Integer(10)
    a //= 5
    assert a == Integer(2)

    a = Integer(10)
    a %= b
    assert a == Integer(0)
    a = Integer(10)
    a %= 5
    assert a == Integer(0)

    a = Integer(10)
    a **= b
    assert a == Integer(100)
    a = Integer(10)
    a **= 5
    assert a == Integer(100000)

    a = Integer(10)
    a &= b
    assert a == Integer(2)
    a = Integer(10)
    a &= 3
    assert a == Integer(2)

    a = Integer(10)
    a |= b
    assert a == Integer(10)
    a = Integer(10)
    a |= 3
    assert a == Integer(11)

    a = Integer(10)
    a ^= b
    assert a == Integer(8)
    a = Integer(10)
    a ^= 3
    assert a == Integer(9)

    a = Integer(10)
    a <<= b
    assert a == Integer(40)
    a = Integer(10)
    a <<= 3
    assert a == Integer(80)

    a = Integer(10)
    a >>= b
    assert a == Integer(2)
    a = Integer(10)
    a >>= 3
    assert a == Integer(1)

    a = Integer(10)
    a = -a
    assert a == Integer(-10)
    a = Integer(10)
    a = +a
    assert a == Integer(10)
    a = Integer(10)
    a = ~a
    assert a == Integer(-11)

    a = Real(10.0)
    b = Real(2.0)
    a += b
    assert a == Real(12.0)
    a = Real(10.0)
    a -= b
    assert a == Real(8.0)
    a = Real(10.0)
    a -= 5
    assert a == Real(5.0)
    a = Real(10.0)
    a *= b
    assert a == Real(20.0)
    a = Real(10.0)
    a *= 5
    assert a == Real(50.0)
    a = Real(10.0)
    a /= b
    assert a == Real(5.0)
    a = Real(10.0)
    a /= 5
    assert a == Real(2.0)
    a = Real(10.0)
    a //= b
    assert a == Real(5.0)
    a = Real(10.0)
    a //= 5
    assert a == Real(2.0)
    a = Real(10.0)
    a %= b
    assert a == Real(0.0)
    a = Real(10.0)
    a %= 5
    assert a == Real(0.0)
    a = Real(10.0)
    a **= b
    assert a == Real(100.0)
    a = Real(10.0)
    a **= 5
    assert a == Real(100000.0)
    a = Real(10.0)
    a = -a
    assert a == Real(-10.0)
    a = Real(10.0)
    a = +a
    assert a == Real(10.0)
    try:
        a = Real(10.0)
        a = ~a
        assert a == Real(-11.0)
        assert False
    except TypeError:
        assert True
    try:
        a = Real(10.0)
        a &= b
        assert a == Real(2.0)
        assert False
    except TypeError:
        assert True
    try:
        a = Real(10.0)
        a |= b
        assert a == Real(10.0)
        assert False
    except TypeError:
        assert True
    try:
        a = Real(10.0)
        a ^= b
        assert a == Real(8.0)
        assert False
    except TypeError:
        assert True
    try:
        a = Real(10.0)
        a <<= b
        assert a == Real(40.0)
        assert False
    except TypeError:
        assert True
    try:
        a = Real(10.0)
        a >>= b
        assert a == Real(2.0)
        assert False
    except TypeError:
        assert True
    

def test():
    a = Integer(1)
    b = Real(2.0)
    c = Complex(1+1j)
    u = Undefined("x")
    o = Operator("+")
    # Test __add__
    assert a + 1 == Integer(2), "Integer addition failed"
    assert 1 + a == Integer(2), "Integer reverse addition failed"
    assert b + 1 == Real(3.0), "Real addition failed"
    assert 1 + b == Real(3.0), "Real reverse addition failed"
    assert c + 1 == Complex(2 + 1j), "Complex addition failed"
    assert 1 + c == Complex(2 + 1j), "Complex reverse addition failed"
    # Test __sub__
    assert a - 1 == Integer(0), "Integer subtraction failed"
    assert 2 - a == Integer(1), "Integer reverse subtraction failed"
    assert b - 1 == Real(1.0), "Real subtraction failed"
    assert 3.0 - b == Real(1.0), "Real reverse subtraction failed"
    assert c - 1 == Complex(0 + 1j), "Complex subtraction failed"
    assert 2 - c == Complex(1 - 1j), "Complex reverse subtraction failed"
    # Test __mul__
    assert a * 2 == Integer(2), "Integer multiplication failed"
    assert 2 * a == Integer(2), "Integer reverse multiplication failed"
    assert b * 2 == Real(4.0), "Real multiplication failed"
    assert 2 * b == Real(4.0), "Real reverse multiplication failed"
    assert c * 2 == Complex(2 + 2j), "Complex multiplication failed"
    assert 2 * c == Complex(2 + 2j), "Complex reverse multiplication failed"
    # Test __truediv__
    assert b / 2 == Real(1.0), "Real division failed"
    assert 4.0 / b == Real(2.0), "Real reverse division failed"
    assert c / 2 == Complex(0.5 + 0.5j), "Complex division failed"
    assert (1 + 1j) / c == Complex(1 + 0j), "Complex reverse division failed"
    # Test __eq__
    assert a == 1, "Integer equality failed"
    assert b == 2.0, "Real equality failed"
    assert c == (1 + 1j), "Complex equality failed"
    # Test __lt__ and __gt__
    assert a < 2, "Integer less-than failed"
    assert b > 1.0, "Real greater-than failed"


def test_type():
    assert type(Integer(1)) == Integer, "Integer type failed"
    assert type(Real(1.0)) == Real, "Real type failed"
    assert type(Complex(1 + 1j)) == Complex, "Complex type failed"
    assert type(Boolean(True)) == Boolean, "Boolean type failed"

    # + operator
    val = Integer(1) + 1
    assert type(val) == Integer, "Integer type failed"
    val = 1 + Integer(1)
    assert type(val) == Integer, "Integer type failed"

    val = Real(1.0) + 1
    assert type(val) == Real, "Real type failed"
    val = 1 + Real(1.0)
    assert type(val) == Real, "Real type failed"

    val = Complex(1 + 1j) + 1
    assert type(val) == Complex, "Complex type failed"
    val = 1 + Complex(1 + 1j)
    assert type(val) == Complex, "Complex type failed"

    val = Boolean(True) + 1
    assert type(val) == Integer, "Integer type failed"
    val = 1 + Boolean(True)
    assert type(val) == Integer, "Integer type failed"

    b = Boolean(True) == 1
    assert type(b) == Boolean, "Boolean type failed"
    b = 1 == Boolean(True)
    assert type(b) == Boolean, "Boolean type failed"
    b = Boolean(True) == True
    assert type(b) == Boolean, "Boolean type failed"
    b = True == Boolean(True)
    assert type(b) == Boolean, "Boolean type failed"
    b = Boolean(True) == 1.0
    assert type(b) == Boolean, "Boolean type failed"
    b = 1.0 == Boolean(True)
    assert type(b) == Boolean, "Boolean type failed"

    # - operator
    val = Integer(1) - 1
    assert type(val) == Integer, "Integer type failed"
    val = 1 - Integer(1)
    assert type(val) == Integer, "Integer type failed"

    # * operator
    val = Integer(1) * 1
    assert type(val) == Integer, "Integer type failed"
    val = 1 * Integer(1)
    assert type(val) == Integer, "Integer type failed"

    # / operator
    val = Integer(1) / 1
    assert type(val) == Real, "Integer type failed, got: " + str(type(val))
    val = 1 / Integer(1)
    assert type(val) == Real, "Integer type failedgot: " + str(type(val))



if __name__ == "__main__":
    test()
    test_Integer()
    test_Real()
    test_Complex()
    test_Boolean()
    test_type()
    test_logic()
    test_inplace()
    test_bitwise()
    test_cast()
    print("All tests passed.")
    a = Integer(1)
    a += Integer(1)
    a += 1
    print(a)
    a -= 1
    a -= Integer(1)
    a -= Real(1)
    a = 5
    a -= Integer(1)
    print(a)
    a = Integer(1)
    b = Integer(2)
    print(a & b)
    a = Boolean(True)
    b = Boolean(False)
    c = a & b
    print(c, type(c))

    a = Real(np.array(4))
    b = Real(np.array(2))
    print(a + b)
    print(type(a.value))

    a = String("Hello")
    b = String("World")
    print(a + b)
    print(a + "aaaa")
    print("bbb" + a)

    a = Vector([1, 2, 3])
    b = Vector([4, 5, 6])
    print(a + b)
    print(a + 1)
    print(1 + a)
    print(a * b)