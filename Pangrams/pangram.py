def pangrams (s):
    alphabet_set = set('abcdefghijklmnopqrstuvwxyz')
    test_set = set(s.lower())
    return 'pangram' if test_set.issuperset(alphabet_set) else 'not pangram'