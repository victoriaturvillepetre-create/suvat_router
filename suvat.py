import math

def suvat_router4():
    print("SUVAT Solver (with working)")
    print("Variables: s, u, v, a, t")
    print("Enter known variables. Type '/' when finished.\n")

    known = {}

    # -------- INPUT --------
    while True:
        var = input("Enter variable (s/u/v/a/t or /): ").lower()

        if var == "/":
            break

        if var not in ["s", "u", "v", "a", "t"]:
            print("Invalid variable.")
            continue

        try:
            value = float(input(f"Enter value for {var}: "))

            if var == "t" and value < 0:
                print("Time (t) cannot be negative.")
                continue

            known[var] = value

        except ValueError:
            print("Please enter a numeric value.")

    print("\nKnown values:", known)

    # -------- VALIDATION --------
    if "t" in known and known["t"] < 0:
        print("Error: Time cannot be negative.")
        return

    unknowns = [x for x in ["s", "u", "v", "a", "t"] if x not in known]

    if all(k in known for k in ["u", "v", "a", "t"]):
        if abs((known["u"] + known["a"] * known["t"]) - known["v"]) > 1e-6:
            print("Known values are inconsistent (u + at ≠ v).")
            return

    if len(unknowns) != 1:
        print("Exactly ONE unknown is required.")
        return

    unknown = unknowns[0]

    # -------- SOLVING WITH WORKING --------
    try:
        if unknown == "v" and all(k in known for k in ["u", "a", "t"]):
            print("\nUsing equation: v = u + at")
            print(f"Substitute: v = {known['u']} + ({known['a']} × {known['t']})")
            v = known["u"] + known["a"] * known["t"]
            print(f"v = {v}")

        elif unknown == "u" and all(k in known for k in ["v", "a", "t"]):
            print("\nUsing equation: v = u + at")
            print("Rearrange: u = v − at")
            print(f"Substitute: u = {known['v']} − ({known['a']} × {known['t']})")
            u = known["v"] - known["a"] * known["t"]
            print(f"u = {u}")

        elif unknown == "a" and all(k in known for k in ["v", "u", "t"]):
            if known["t"] == 0:
                print("Cannot calculate acceleration when t = 0.")
                return
            print("\nUsing equation: v = u + at")
            print("Rearrange: a = (v − u) / t")
            print(f"Substitute: a = ({known['v']} − {known['u']}) / {known['t']}")
            a = (known["v"] - known["u"]) / known["t"]
            print(f"a = {a}")

        elif unknown == "t" and all(k in known for k in ["v", "u", "a"]):
            if known["a"] == 0:
                print("Cannot calculate time when acceleration is zero.")
                return
            print("\nUsing equation: v = u + at")
            print("Rearrange: t = (v − u) / a")
            print(f"Substitute: t = ({known['v']} − {known['u']}) / {known['a']}")
            t = (known["v"] - known["u"]) / known["a"]
            if t < 0:
                print("Calculated time is negative — no physical solution.")
            else:
                print(f"t = {t}")

        elif unknown == "s" and all(k in known for k in ["u", "a", "t"]):
            print("\nUsing equation: s = ut + ½at²")
            print(f"Substitute: s = ({known['u']} × {known['t']}) + ½ × {known['a']} × {known['t']}²")
            s = known["u"] * known["t"] + 0.5 * known["a"] * known["t"] ** 2
            print(f"s = {s}")

        elif unknown == "v" and all(k in known for k in ["u", "a", "s"]):
            disc = known["u"]**2 + 2 * known["a"] * known["s"]
            if disc < 0:
                print("No real solution (negative square root).")
                return
            print("\nUsing equation: v² = u² + 2as")
            print(f"Substitute: v² = {known['u']}² + 2 × {known['a']} × {known['s']}")
            print(f"v² = {disc}")
            v = disc ** 0.5
            print(f"v = √{disc} = {v}")

        elif unknown == "u" and all(k in known for k in ["v", "a", "s"]):
            disc = known["v"]**2 - 2 * known["a"] * known["s"]
            if disc < 0:
                print("No real solution (negative square root).")
                return
            print("\nUsing equation: v² = u² + 2as")
            print("Rearrange: u² = v² − 2as")
            print(f"Substitute: u² = {known['v']}² − 2 × {known['a']} × {known['s']}")
            print(f"u² = {disc}")
            u = disc ** 0.5
            print(f"u = √{disc} = {u}")

        else:
            print("No suitable SUVAT equation for the given inputs.")

    except ZeroDivisionError:
        print("Error: Division by zero.")


def suvat_router3():
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
