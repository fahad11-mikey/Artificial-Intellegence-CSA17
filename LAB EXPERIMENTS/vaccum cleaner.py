def vacuum_cleaner():
    room = {
        'A': 'Dirty',
        'B': 'Dirty'
    }

    location = 'A'

    print("Initial State:")
    print(room)

    while 'Dirty' in room.values():

        if room[location] == 'Dirty':
            print("Cleaning Room", location)
            room[location] = 'Clean'

        else:
            if location == 'A':
                location = 'B'
                print("Moving to Room B")
            else:
                location = 'A'
                print("Moving to Room A")

    print("\nFinal State:")
    print(room)
    print("All rooms are clean!")

vacuum_cleaner()
