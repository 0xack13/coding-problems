def _permutation_repeat(text, prefix, n, k):
    if k == 0:
        print(prefix)
        return
    # without reptition e.g. add start index
    for i in range(n):
        new_prefix = prefix + text[i] # a, aa, aaa, aab, aac ab, aba, abb, abc
        print(new_prefix)
        _permutation_repeat(text, new_prefix, n, k-1)
    print('---')

def permutation_repeat(text, k):
    _permutation_repeat(text, "", len(text), k)

permutation_repeat("abc", 3)
