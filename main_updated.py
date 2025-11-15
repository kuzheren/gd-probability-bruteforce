A = 214013
C = 2531011
MASK = 0xFFFFFFFF
TH = 16547
SPECIAL_INDICES = (0, 7, 13) # UPDATED INDICES CUS LEVEL IS ASS

def count_safe_passes(seed, steps, special_mask):
    s = seed & 0xFFFFFFFF
    safe = 0
    for i in range(steps):
        s = (s * A + C) & MASK
        R = (s >> 16) & 0x7FFF
        sel = 0 if R <= TH else 1
        is_special = (special_mask >> i) & 1
        wall_sel = 0 if is_special == 1 else 1
        if sel == wall_sel:
            break
        safe += 1
    return safe


def make_special_mask(steps):
    m = 0
    for idx in SPECIAL_INDICES:
        if idx < steps:
            m |= (1 << idx)
    return m


def main():
    start = 0
    end = 4294967296
    steps = 30
    special_mask = make_special_mask(steps)

    print(f"Scanning seeds from {start} to {end}, steps={steps}")

    best_n = -1
    best_seed = None

    for seed in range(start, end):
        n = count_safe_passes(seed, steps, special_mask)
        if n > best_n:
            best_n = n
            best_seed = seed
            print(f"New record: steps={best_n}, seed={best_seed}")

    print(f"Done! Best: steps={best_n}, seed={best_seed}")


if __name__ == "__main__":
    main()
