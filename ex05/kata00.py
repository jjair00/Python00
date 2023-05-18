
kata = (19,42,21)  

m = map(str, kata)

if len(kata) == 0:
    print(f"The are not numbers.")
else:
    print(f"The {len(kata)} numbers are: ", ", ".join(m))

