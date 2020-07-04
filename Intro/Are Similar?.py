def areSimilar(a, b):
    same_items = sorted(a) == sorted(b)
    differences = [i for i in range(len(a)) if a[i] != b[i]]
    return len(differences) <= 2 and same_items