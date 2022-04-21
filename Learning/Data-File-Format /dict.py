import json
test_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
with open('JSON_test.json', mode='w') as f:
    json.dump(test_dict, f)