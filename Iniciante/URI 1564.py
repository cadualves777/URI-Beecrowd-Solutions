while True:
    try:
        x = int(input())
        print('vai ter copa!' if x == 0 else 'vai ter duas!')
    except EOFError:
        break
