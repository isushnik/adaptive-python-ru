def test(x):
    if not x:
        print('x like false value!')
    else:
        print('not')

# test([None])
# test(float('nan'))
# test(float('inf'))
# test('True')

test([])
test(None)

# test(True)

test(0)

# test(object())
# test([None, None])

test(set())

# test('False')

test('')
