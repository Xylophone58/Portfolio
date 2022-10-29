# @author Zach Mitchell
def main():
    # Create two empty lists named pars and scores
    pars = []
    scores = []
    # Invoke get_golf_data with the two lists and a file named GolfScores.txt
    get_golf_data(pars, scores, "GolfScores.txt")
    # Invoke count_holes_below_par with the two lists to get the number
    # of times the score was less than the par. Display this number with
    # a preceding header that matches the sample output. 
    # (This can be achieved with one or two lines of code.) 
    belowPar = count_holes_below_par(pars, scores)
    print("Number of holes below par: " + str(belowPar))


def get_golf_data(pars, scores, filename):
    """
    get_golf_data reads golf pars and scores from a file into the associated
    lists.
    @param pars An empty list to be filled with pars
    @param scores An empty list to be filled with scores
    @param filename Contains the name of the input file
    """
    f = open(filename)

    for line in f:
        pieces = line.split(',')
        pars.append(pieces[0])
        scores.append(pieces[1])

def count_holes_below_par(pars, scores):
    """
    count_holes_below_par counts the number of golf holes for which the
    golfer's score was less than the par for that hole.
    @param pars A list filled with pars for each hole played
    @param scores A parallel list to pars filled with scores achieved on each
                  hole played
    @return The number of holes for which the score was less than the par
    """
    below = 0
    for i in range(len(pars)):
        if scores[i] < pars[i]:
            below += 1
    return below

main()
