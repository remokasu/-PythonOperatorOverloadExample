# Pythonの独自Classに対して算術演算を定義するための例
演算子のオーバーロードはよく使用するので，その方法をまとめておく．

## 概要
ここでは，基本的なデータ型を再定義して，演算子をオーバーロードする方法を示す.<br>
例として, `uint8` と `int8` 等の固定長のデータを扱うクラスを定義して，演算子をオーバーロードする．<br>
データ型は `numpy` のデータ型に準拠する．<br>


## 構成

- Generic (base class)
    - Numeric
        - Integer
        - Bool
        - Real
        - Complex
        - Vector
    - String


## 使い方

### 使用可能なデータ型
- integer
- int8
- int16
- int32
- int64
- uint8
- uint16
- uint32
- uint64
- boolean
- real
- real32
- real64
- imag
- imag32
- imag64
- vec (配列)
- string (文字列)


### 例
``` python
from data_type import *

a = uint8(255)
b = uint8(1)
print(a + b) # 0　uint8の最大値を超えたので0になる

a = int8(127)
b = int8(1)
print(a + b) # -128  int8の最大値を超えたので-128になる
```


## メモ

### 演算子のオーバーロード
- `+` は `__add__` と `__radd__` を定義する．
- `-` は `__sub__` と `__rsub__` を定義する．
- `*` は `__mul__` と `__rmul__` を定義する．
- `/` は `__truediv__` と `__rtruediv__` を定義する．
- `//` は `__floordiv__` と `__rfloordiv__` を定義する．
- `%` は `__mod__` と `__rmod__` を定義する．
- `**` は `__pow__` と `__rpow__` を定義する．
- `+=` は `__iadd__` を定義する
- `-=` は `__isub__` を定義する
- `*=` は `__imul__` を定義する
- `/=` は `__idiv__` を定義する
- `%=` は `__imod__` を定義する
- `**=` は `__ipow__` を定義する
- `==` は `__eq__` を定義する
- `!=` は `__ne__` を定義する
- `<` は `__lt__` を定義する
- `<=` は `__le__` を定義する
- `>` は `__gt__` を定義する
- `>=` は `__ge__` を定義する
- `<<` は `__lshift__` を定義する
- `>>` は `__rshift__` を定義する
- `&` は `__and__` を定義する
- `|` は `__or__` を定義する
- `^` は `__xor__` を定義する
- `&=` は `__iand__` を定義する
- `|=` は `__ior__` を定義する
- `^=` は `__ixor__` を定義する
- `+x` は `__pos__` を定義する
- `-x` は `__neg__` を定義する
- `~x` は `__invert__` を定義する
- `abs(x)` は `__abs__` を定義する
- `int(x)` は `__int__` を定義する
- `long(x)` は `__long__` を定義する
- `float(x)` は `__float__` を定義する
- `complex(x)` は `__complex__` を定義する
- `oct(x)` は `__oct__` を定義する
- `hex(x)` は `__hex__` を定義する


### その他
- `del` は `__del__` を定義する
- `with` は `__enter__` と `__exit__` を定義する
- `[]` は `__getitem__` を定義する
- `[]=` は `__setitem__` を定義する
- `()` は `__call__` を定義する
- `str()` は `__str__` を定義する
- `repr()` は `__repr__` を定義する
- `len()` は `__len__` を定義する
- `iter()` は `__iter__` を定義する
- `in` は `__contains__` を定義する
- `index(x)` は `__index__` を定義する
- `hash(x)` は `__hash__` を定義する
- `bool(x)` は `__nonzero__` を定義する
- `dir(x)` は `__dir__` を定義する
- `format(x)` は `__format__` を定義する
- `await(x)` は `__await__` を定義する
- `next(x)` は `__next__` を定義する
- `iter(x)` は `__iter__` を定義する
- `length_hint(x)` は `__length_hint__` を定義する
- `reversed(x)` は `__reversed__` を定義する
