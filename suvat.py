
import math

def suvat_router():
    print("SUVAT Equation Router")
    print("Variables:")
    print("s = displacement")
    print("u = initial velocity")
    print("v = final velocity")
    print("a = acceleration")
    print("t = time\n")

    # Ask what variable to find
    find = input("Which variable do you want to find? (s, u, v, a, t): ").lower()

    # Ask which variables are known
    known = input("Enter the known variables (e.g. u v a): ").lower().split()

    values = {}

    # Get values for known variables
    for var in known:
        values[var] = float(input(f"Enter value for {var}: "))

    # ROUTING LOGIC
    if find == "v" and {"u", "a", "t"}.issubset(known):
        v = values["u"] + values["a"] * values["t"]
        print("Using: v = u + at")
        print("v =", v)

    elif find == "s" and {"u", "t", "a"}.issubset(known):
        s = values["u"] * values["t"] + 0.5 * values["a"] * values["t"]**2
        print("Using: s = ut + ½at²")
        print("s =", s)

    elif find == "v" and {"u", "a", "s"}.issubset(known):
        v = math.sqrt(values["u"]**2 + 2 * values["a"] * values["s"])
        print("Using: v² = u² + 2as")
        print("v =", v)

    elif find == "s" and {"u", "v", "t"}.issubset(known):
        s = ((values["u"] + values["v"]) / 2) * values["t"]
        print("Using: s = (u + v)t / 2")
        print("s =", s)

    elif find == "t" and {"u", "v", "a"}.issubset(known):
        t = (values["v"] - values["u"]) / values["a"]
        print("Using: v = u + at")
        print("t =", t)

    else:
        print("No suitable SUVAT equation found for those variables.")
