str = input().lower()
vowels = ['a', 'o', 'y', 'e', 'u', 'i']
new_str = list(filter(lambda x : x not in vowels, str))
new_str.insert(0, '')
print('.'.join(new_str))