import math

def suvat_router():
    print("SUVAT Equation Router")
    print("Variables:")
    print("s = displacement")
    print("u = initial velocity")
    print("v = final velocity")
    print("a = acceleration")
    print("t = time\n")

    valid_vars = {"s", "u", "v", "a", "t"}
    # Validate the variable to find
    while True:
        find = input("Which variable do you want to find? (s, u, v, a, t): ").lower().strip()
        if find in valid_vars:
            break
        print("Invalid choice. Please enter one of: s, u, v, a, t.")
    
    # Validate known variables
    while True:
        known = input("Enter the known variables (e.g. u v a): ").lower().split()
    
        # Check for invalid variables
        if not all(var in valid_vars for var in known):
            print("One or more invalid variables entered. Use only: s, u, v, a, t.")
            continue
    
        # Check for duplicates
        if len(set(known)) != len(known):
            print("Duplicate variables detected. Please enter each variable only once.")
            continue
    
        # Check that the unknown variable is not included
        if find in known:
            print(f"You are trying to find '{find}', so it cannot be a known variable.")
            continue
    
        # Optional: ensure at least two known variables
        if len(known) < 2:
            print("Please enter at least two known variables.")
            continue
    
        break

    values = {}

    # Get values for known variables
    for var in known:
        values[var] = float(input(f"Enter value for {var}: "))

    # ===== FINDING s (displacement) =====
    if find == "s" and {"u", "a", "t"}.issubset(known):
        s = values["u"] * values["t"] + 0.5 * values["a"] * values["t"]**2
        print("Using: s = ut + ½at²")
        print("s =", s)

    elif find == "s" and {"u", "v", "t"}.issubset(known):
        s = ((values["u"] + values["v"]) / 2) * values["t"]
        print("Using: s = (u + v)t / 2")
        print("s =", s)

    elif find == "s" and {"u", "v", "a"}.issubset(known):
        s = (values["v"]**2 - values["u"]**2) / (2 * values["a"])
        print("Using: v² = u² + 2as → s = (v² - u²)/(2a)")
        print("s =", s)

    elif find == "s" and {"v", "a", "t"}.issubset(known):
        u = values["v"] - values["a"] * values["t"]
        s = u * values["t"] + 0.5 * values["a"] * values["t"]**2
        print("Using: v = u + at → u = v - at, then s = ut + ½at²")
        print(f"First found u = {u}")
        print("s =", s)

    # ===== FINDING u (initial velocity) =====
    elif find == "u" and {"v", "a", "t"}.issubset(known):
        u = values["v"] - values["a"] * values["t"]
        print("Using: v = u + at → u = v - at")
        print("u =", u)

    elif find == "u" and {"v", "a", "s"}.issubset(known):
        u_squared = values["v"]**2 - 2 * values["a"] * values["s"]
        if u_squared < 0:
            print("Error: No real solution (u² is negative)")
            return
        u = math.sqrt(u_squared)
        print("Using: v² = u² + 2as → u = ±√(v² - 2as)")
        print("u =", u, "(positive root)")

    elif find == "u" and {"s", "a", "t"}.issubset(known):
        u = (values["s"] - 0.5 * values["a"] * values["t"]**2) / values["t"]
        print("Using: s = ut + ½at² → u = (s - ½at²)/t")
        print("u =", u)

    elif find == "u" and {"s", "v", "t"}.issubset(known):
        u = (2 * values["s"]) / values["t"] - values["v"]
        print("Using: s = (u + v)t/2 → u = (2s/t) - v")
        print("u =", u)

    elif find == "u" and {"s", "v", "a"}.issubset(known):
        u_squared = values["v"]**2 - 2 * values["a"] * values["s"]
        if u_squared < 0:
            print("Error: No real solution (u² is negative)")
            return
        u = math.sqrt(u_squared)
        print("Using: v² = u² + 2as → u = ±√(v² - 2as)")
        print("u =", u, "(positive root)")

    # ===== FINDING v (final velocity) =====
    elif find == "v" and {"u", "a", "t"}.issubset(known):
        v = values["u"] + values["a"] * values["t"]
        print("Using: v = u + at")
        print("v =", v)

    elif find == "v" and {"u", "a", "s"}.issubset(known):
        v_squared = values["u"]**2 + 2 * values["a"] * values["s"]
        if v_squared < 0:
            print("Error: No real solution (v² is negative)")
            return
        v = math.sqrt(v_squared)
        print("Using: v² = u² + 2as")
        print("v =", v)

    elif find == "v" and {"s", "a", "t"}.issubset(known):
        v = (values["s"] + 0.5 * values["a"] * values["t"]**2) / values["t"]
        print("Using: s = vt - ½at² → v = (s + ½at²)/t")
        print("v =", v)

    elif find == "v" and {"s", "u", "t"}.issubset(known):
        v = (2 * values["s"]) / values["t"] - values["u"]
        print("Using: s = (u + v)t/2 → v = 2s/t - u")
        print("v =", v)

    # ===== FINDING a (acceleration) =====
    elif find == "a" and {"u", "v", "t"}.issubset(known):
        a = (values["v"] - values["u"]) / values["t"]
        print("Using: v = u + at → a = (v - u)/t")
        print("a =", a)

    elif find == "a" and {"u", "v", "s"}.issubset(known):
        a = (values["v"]**2 - values["u"]**2) / (2 * values["s"])
        print("Using: v² = u² + 2as → a = (v² - u²)/(2s)")
        print("a =", a)

    elif find == "a" and {"u", "s", "t"}.issubset(known):
        a = 2 * (values["s"] - values["u"] * values["t"]) / (values["t"]**2)
        print("Using: s = ut + ½at² → a = 2(s - ut)/t²")
        print("a =", a)

    elif find == "a" and {"v", "s", "t"}.issubset(known):
        a = 2 * (values["v"] * values["t"] - values["s"]) / (values["t"]**2)
        print("Using: s = vt - ½at² → a = 2(vt - s)/t²")
        print("a =", a)

    # ===== FINDING t (time) =====
    elif find == "t" and {"u", "v", "a"}.issubset(known):
        if values["a"] == 0:
            print("Error: Acceleration is zero, time cannot be determined from u, v, a")
            return
        t = (values["v"] - values["u"]) / values["a"]
        print("Using: v = u + at → t = (v - u)/a")
        print("t =", t)

    elif find == "t" and {"u", "v", "s"}.issubset(known):
        if values["u"] + values["v"] == 0:
            print("Error: u + v = 0, time cannot be determined")
            return
        t = (2 * values["s"]) / (values["u"] + values["v"])
        print("Using: s = (u + v)t/2 → t = 2s/(u + v)")
        print("t =", t)

    elif find == "t" and {"v", "a", "s"}.issubset(known):
        # Using v = u + at and v² = u² + 2as
        u_squared = values["v"]**2 - 2 * values["a"] * values["s"]
        if u_squared < 0:
            print("Error: No real solution (u² is negative)")
            return
        u = math.sqrt(u_squared)
        if values["a"] == 0:
            print("Error: Acceleration is zero")
            return
        t = (values["v"] - u) / values["a"]
        print("Using: v² = u² + 2as and v = u + at")
        print(f"First found u = {u}")
        print("t =", t)

    elif find == "t" and {"u", "a", "s"}.issubset(known):
        # From s = ut + ½at² → quadratic: ½at² + ut - s = 0
        a = values["a"]
        u = values["u"]
        s = values["s"]
        
        if a == 0:
            if u == 0:
                print("Error: a=0 and u=0, no motion")
                return
            t = s / u
            print("Using: s = ut (a=0) → t = s/u")
            print("t =", t)
        else:
            discriminant = u**2 + 2 * a * s
            if discriminant < 0:
                print("Error: No real solution (discriminant < 0)")
                return
            t1 = (-u + math.sqrt(discriminant)) / a
            t2 = (-u - math.sqrt(discriminant)) / a
            
            # Choose the physically meaningful solution
            positive_times = [t for t in [t1, t2] if t > 0]
            
            if positive_times:
                t = min(positive_times)  # Usually the smaller positive time
                print(f"Using: s = ut + ½at² → solving quadratic")
                print(f"Two possible times: t = {t1:.4f} or t = {t2:.4f}")
                print(f"Taking the positive solution: t = {t:.4f}")
            else:
                # If both are negative, take the one closer to zero
                t = max(t1, t2)
                print(f"Warning: Both times are negative: {t1:.4f}, {t2:.4f}")
                print(f"Taking: t = {t:.4f}")

    else:
        print("No suitable SUVAT equation found for those variables.")

# Main program loop
while True:
    print("=" * 50)
    suvat_router()
    
    again = input("\nSolve another? (y/n): ").lower().strip()
    if again != 'y':
        print("Goodbye!")
        break
    print("\n" * 3)
