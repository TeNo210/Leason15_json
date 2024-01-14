import pickle
big_object = {

        'items':[
            '1',
            (2,3),
            ['some','else']
            {'op':'ap'}

        ]
}
result = pickle.dumps(big_object)

print(result)
result = pickle.dumps(big_object)
print(result)
big_object_recovery = pickle.loads(result)
print(big_object_recovery)