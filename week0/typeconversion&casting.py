


# PART 1 — IMPLICIT CONVERSION (Python does it automatically)


# int + float → float
x = 5
y = 2.5
z = x + y
print(f"int + float : {x} + {y} = {z}  → type: {type(z).__name__}")

# int + bool → int
r1 = 10 + True
print(f"int + bool  : 10 + True = {r1}  → type: {type(r1).__name__}")

# bool + float → float
r2 = True + 2.5
print(f"bool + float: True + 2.5 = {r2}  → type: {type(r2).__name__}")

# bool + bool → int
r3 = True + True
print(f"bool + bool : True + True = {r3}  → type: {type(r3).__name__}")

# float stays float (no auto-downcast)
r4 = 5.9 + 1
print(f"float + int : 5.9 + 1 = {r4}  → type: {type(r4).__name__}")
print()


# PART 2 — EXPLICIT CONVERSION (casting — YOU do it)



# ---------- 2.1  int() ----------
print("--- int() : to integer ---")
print(f'int("42")        = {int("42")}')
print(f'int(3.99)        = {int(3.99)}        (truncates, not rounds!)')
print(f'int(True)        = {int(True)}')
print(f'int(False)       = {int(False)}')
print(f'int("  42  ")    = {int("  42  ")}    (strips whitespace)')
print(f'int("0x1A", 16)  = {int("0x1A", 16)}  (hex → decimal)')
print(f'int("101", 2)    = {int("101", 2)}    (binary → decimal)')
print(f'int(float("3.99")) = {int(float("3.99"))}  (2-step for float strings)')
print()


# ---------- 2.2  float() ----------
print("--- float() : to float ---")
print(f'float("3.14")    = {float("3.14")}')
print(f'float(42)        = {float(42)}')
print(f'float("1e3")     = {float("1e3")}')
print(f'float(True)      = {float(True)}')
print(f'float("inf")     = {float("inf")}')
print(f'float("nan")     = {float("nan")}')
print()


# ---------- 2.3  str() ----------
print("--- str() : to string ---")
print(f'str(42)          = {str(42)!r}')
print(f'str(3.14)        = {str(3.14)!r}')
print(f'str(True)        = {str(True)!r}')
print(f'str(None)        = {str(None)!r}')
print(f'str([1,2,3])     = {str([1,2,3])!r}')
print(f'str((1,2))       = {str((1,2))!r}')
print(f'str({{"a":1}})      = {str({"a":1})!r}')
print()


# ---------- 2.4  bool() ----------
print("--- bool() : to boolean ---")
print("FALSY values:")
print(f'  bool(0)        = {bool(0)}')
print(f'  bool(0.0)      = {bool(0.0)}')
print(f'  bool("")       = {bool("")}')
print(f'  bool([])       = {bool([])}')
print(f'  bool(())       = {bool(())}')
print(f'  bool({{}})       = {bool({})}')
print(f'  bool(set())    = {bool(set())}')
print(f'  bool(None)     = {bool(None)}')
print(f'  bool(False)    = {bool(False)}')
print("TRUTHY values:")
print(f'  bool(1)        = {bool(1)}')
print(f'  bool(-1)       = {bool(-1)}')
print(f'  bool(3.14)     = {bool(3.14)}')
print(f'  bool("0")      = {bool("0")}     ⚠️ non-empty string!')
print(f'  bool("False")  = {bool("False")} ⚠️ non-empty string!')
print(f'  bool([0])      = {bool([0])}     non-empty list')
print(f'  bool({{"a":0}})   = {bool({"a":0})}   non-empty dict')
print()


# ---------- 2.5  list() ----------
print("--- list() : to list ---")
print(f'list("abc")          = {list("abc")}')
print(f'list((1, 2, 3))      = {list((1, 2, 3))}')
print(f'list({{1, 2, 3}})        = {list({1, 2, 3})}  (order may vary)')
print(f'list(range(5))       = {list(range(5))}')
print(f'list({{"a":1,"b":2}})    = {list({"a":1,"b":2})}  ← keys only!')
print(f'list(b"hi")          = {list(b"hi")}  ← byte values')
print()


# ---------- 2.6  tuple() ----------
print("--- tuple() : to tuple ---")
print(f'tuple([1, 2, 3])     = {tuple([1, 2, 3])}')
print(f'tuple("abc")         = {tuple("abc")}')
print(f'tuple(range(3))      = {tuple(range(3))}')
print(f'tuple({{1, 2}})         = {tuple({1, 2})}')
print()


# ---------- 2.7  set() ----------
print("--- set() : to set (removes duplicates) ---")
print(f'set([1, 2, 2, 3])    = {set([1, 2, 2, 3])}')
print(f'set("hello")         = {set("hello")}')
print(f'set(range(5))        = {set(range(5))}')
nums = [1, 2, 2, 3, 3, 3, 4]
print(f'dedupe {nums} → {list(set(nums))}')
print()


# ---------- 2.8  dict() ----------
print("--- dict() : to dictionary ---")
print(f'dict([("a",1),("b",2)])      = {dict([("a",1),("b",2)])}')
print(f'dict(a=1, b=2)               = {dict(a=1, b=2)}')
print(f'dict(zip(["a","b"],[1,2]))  = {dict(zip(["a","b"], [1,2]))}')
print()


# ---------- 2.9  complex() ----------
print("--- complex() : to complex ---")
print(f'complex(3)        = {complex(3)}')
print(f'complex(3, 4)     = {complex(3, 4)}')
print(f'complex("3+4j")   = {complex("3+4j")}')
print(f'complex("5")      = {complex("5")}')
print()


# PART 3 — CHAIN CONVERSIONS


# str → float → int
print(f'int(float("3.99"))      = {int(float("3.99"))}')

# list → set → list (dedupe)
lst = [1, 2, 2, 3, 3, 3]
print(f'list(set({lst}))  = {list(set(lst))}')

# tuple → list → string
t = (1, 2, 3)
print(f'str(list({t}))          = {str(list(t))!r}')

# str → list → str (join)
s = "hello"
print(f'"-".join(list("{s}"))    = {"-".join(list(s))!r}')

# dict → items → list → dict
d = {"a": 1, "b": 2}
print(f'dict(list(d.items()))   = {dict(list(d.items()))}')

# int → bool → int
print(f'int(bool(42))           = {int(bool(42))}')

# str → bytes → str
b = "hi".encode()
print(f'"hi".encode()           = {b}')
print(f'b.decode()              = {b.decode()!r}')
print()


# PART 4 — COMMON GOTCHAS (things that FAIL)

# int truncates (not rounds)
print(f'int(3.99)      = {int(3.99)}  ( truncates, round() gives {round(3.99)})')

# int("3.14") fails → 2-step
try:
    int("3.14")
except ValueError as e:
    print(f'int("3.14")      ValueError → use int(float("3.14")) = {int(float("3.14"))}')

# int("abc") fails
try:
    int("abc")
except ValueError as e:
    print(f'int("abc")       ValueError')

# int(None) fails
try:
    int(None)
except TypeError as e:
    print(f'int(None)        TypeError')

# float("abc") fails
try:
    float("abc")
except ValueError:
    print(f'float("abc")    ValueError')

# list(42) fails (int not iterable)
try:
    list(42)
except TypeError:
    print(f'list(42)         TypeError (int not iterable)')

# dict([1,2,3]) fails (needs pairs)
try:
    dict([1, 2, 3])
except (TypeError, ValueError):
    print(f'dict([1,2,3])    TypeError (needs key-value pairs)')

# "0" and "False" are truthy
print(f'bool("0")       = {bool("0")}  non-empty string!')

# list(dict) gives keys only
print(f'list({{"a":1,"b":2}}) = {list({"a":1,"b":2})}  (keys only)')
print()


# PART 5 — SAFE CONVERSION WITH try/except


def safe_int(value, default=None):
    """Convert to int safely; return default on failure."""
    try:
        return int(value)
    except (ValueError, TypeError):
        return default

print(f'safe_int("42")     = {safe_int("42")}')
print(f'safe_int("abc")    = {safe_int("abc")}')
print(f'safe_int("abc", 0) = {safe_int("abc", 0)}')
print(f'safe_int(3.99)     = {safe_int(3.99)}')
print(f'safe_int(None, -1) = {safe_int(None, -1)}')
print()


def safe_float(value, default=0.0):
    try:
        return float(value)
    except (ValueError, TypeError):
        return default

print(f'safe_float("3.14") = {safe_float("3.14")}')
print(f'safe_float("abc")  = {safe_float("abc")}')
print()


# PART 6 — USER INPUT CONVERSION (real-world pattern)

# Simulating input (since we can't type during a script run)
# In a real program, replace raw_* with input(...)
raw_age    = "22"
raw_cgpa   = "7.14"
raw_marks  = "10 20 30 40"
raw_tags   = "python,code,learn"

age    = int(raw_age)                       # str → int
cgpa   = float(raw_cgpa)                    # str → float
marks  = list(map(int, raw_marks.split()))  # str → list[int]
tags   = raw_tags.split(",")                # str → list[str]

print(f'raw_age    = {raw_age!r}  → int   = {age}')
print(f'raw_cgpa   = {raw_cgpa!r} → float = {cgpa}')
print(f'raw_marks  = {raw_marks!r} → list  = {marks}  (sum={sum(marks)})')
print(f'raw_tags   = {raw_tags!r} → list  = {tags}')
print()


# PART 7 — CONVERSION SUMMARY TABLE


conversions = [
    ("str  → int",    'int("42")',           int("42")),
    ("float → int",   'int(3.99)',           int(3.99)),
    ("str  → float",  'float("3.14")',       float("3.14")),
    ("int  → float",  'float(5)',            float(5)),
    ("num  → str",    'str(42)',             str(42)),
    ("any  → bool",   'bool(0)',             bool(0)),
    ("str  → list",   'list("abc")',         list("abc")),
    ("list → tuple",  'tuple([1,2])',        tuple([1, 2])),
    ("list → set",    'set([1,2,2])',        set([1, 2, 2])),
    ("pairs→ dict",   'dict([("a",1)])',     dict([("a", 1)])),
    ("str  → bytes",  '"hi".encode()',       "hi".encode()),
    ("bytes→ str",    'b"hi".decode()',      b"hi".decode()),
]

for label, code, result in conversions:
    print(f'{label:<12}  {code:<22} = {result!r}')

