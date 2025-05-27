# Define maximum number of candidates
MAX_C = 11
# Define available symbols
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '~', '+']
# Global array of candidate details
allCandidates = []
# Array to keep track of taken symbols
symbolTaken = [0] * 11

# Function to populate the allCandidates list with candidate details
def fillCandidate(cNum):
    print("Available Symbols: ")
    for j in range(10):
        if symbolTaken[j] == 0:
            print(f"{j + 1} {symbols[j]}")
    num = 0
    while True:
        try:
            num = int(input(f"Enter the symbol number of candidate {cNum + 1}: "))
            if num <= 0 or num > 10 or symbolTaken[num - 1] == 1:
                print("This Symbol is not available. Please choose from the available symbols")
            else:
                symbolTaken[num - 1] = 1
                allCandidates.append({
                    'symbol': symbols[num - 1],
                    'name': input(f"Enter the name of candidate {cNum + 1}: "),
                    'votes': 0
                })
                break
        except ValueError:
            print("Invalid input. Please enter a valid symbol number.")

# Function to display all candidates and their symbols
def displayAllCandidates():
    if not allCandidates or len(allCandidates) == 0:
        print("Invalid Candidate Array")
        return

    for candidate in allCandidates:
        print(f"{candidate['name']}\t\t", end='')
    print("")
    for candidate in allCandidates:
        print(f"{candidate['symbol']}\t\t\t", end='')
    print("")

# Function to get votes from voters
def getVotes(voterCount):
    displayAllCandidates()
    while True:
        try:
            choice = int(input(f"Voter {voterCount + 1}, please enter your choice (1-{len(allCandidates)}): "))
            if choice >= 1 and choice <= len(allCandidates):
                allCandidates[choice - 1]['votes'] += 1
                break
            else:
                print("Invalid choice! Please vote again.")
        except ValueError:
            print("Invalid input. Please enter a valid choice.")

# Function to get voting results
def getResults():
    maxVotes = 0
    winnerIndex = -1
    winnerFrequency = 0
    for i, candidate in enumerate(allCandidates):
        if candidate['votes'] > maxVotes:
            maxVotes = candidate['votes']
            winnerIndex = i
    for candidate in allCandidates:
        if candidate['votes'] == maxVotes:
            winnerFrequency += 1
    print("\n-----RESULT-----")
    if winnerFrequency > 1:
        print("No candidate has majority votes")
    elif winnerIndex != -1:
        print(f"The winner is: {allCandidates[winnerIndex]['name']}")
        print(f"Candidate Symbol: {allCandidates[winnerIndex]['symbol']}")
        print(f"With {maxVotes} votes!")
    else:
        print("No winner")

def main():
    global allCandidates
    # Getting the number of candidates
    candidateCount = int(input("Enter the number of candidates: "))
    if candidateCount >= MAX_C:
        print("Number of candidates cannot be greater than 10.\n Terminating the program\n\n")
        return
    # Filling details of the candidates
    for i in range(candidateCount):
        fillCandidate(i)
    # Getting the number of voters
    numVoters = int(input("Enter the number of voters: "))
    # Collecting votes
    for i in range(numVoters):
        getVotes(i)
    # Printing results
    getResults()

if __name__ == "__main__":
    main()
