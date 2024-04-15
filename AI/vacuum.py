def vacuum(RoomA, RoomB, Cost):
    if RoomA == 1:
        Cost += 1
        print("The cost of cleaning room A: 1")
    if RoomB == 1:
        Cost += 1
        print("Cost to move from A -> B: 1")
        Cost += 1
        print("The cost of cleaning room B: 1")
    print("Total cost for the vacuum: ", Cost)

def main():
    RoomA = int(input("Enter the condition of room A (1 for dirty, 0 for clean): "))
    RoomB = int(input("Enter the condition of room B (1 for dirty, 0 for clean): "))
    print("Vacuum is in room A")
    vacuum(RoomA, RoomB, 0)

if __name__ == "__main__":
    main()
