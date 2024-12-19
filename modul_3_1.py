calls = 0
def count_calls():
    global calls
    calls += 1
def string_info(string):
    count_calls()
    return (len(string), string.upper(), string.lower())
def is_contains(string, list_to_search):
    count_calls()
    return string.lower() in map(str.lower, string)
print(string_info('Cool'))
print(string_info('Collection'))
print(is_contains('Spring', ['cat', 'BiNGO', 'snoWLAke']))  # Urban ~ urBAN
print(is_contains('winter', ['CEnter', 'crystal']))  # No matches
print(calls)

