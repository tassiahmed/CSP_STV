import prefpy
import io
import math
from .preference import Preference
from .profile import Profile
'''
if __name__ == "__main__":
    

	#profile is not defined?
	p = Profile()


	# need to make filename first
	#the designed file name is pretty confusing based on the read_election_file function

	# Preflib Election Data Format

	p.importPreflibFile("Basic Text Document.txt")
	mP = MechanismPlurality()
	scoreVect = mP.getScoringVector(p)
'''
	
class MechanismSTV(Mechanism):
	"""
	Goal is to return the winner of STV Voting (plurality each round, where loser
	drops out every round until there is a winner).
	Inherits from the general scoring mechanism (can change to positional if that
	works better).
	
	TODO: 
	- STV with no tiebreaker
	- STV with ties broken alphabetically
	- STV with all alternatives returned
	- Ensure voting is valid (no partial orders)
	
	A few questions for the future:
	- Should the final result rank whoever dropped first as the last place?
	- Curious about line 97 in Mechanism.py:
		if elecType != "soc" and elecType != "toc":
            return False
		
		Is this correct? It seems like there should be an 'or'
	"""
	
	#def __init__(self):
		# add something here...
		
	
	
	# override getWinners eventually...
	# def getWinners(self, profile):
	
	# and possibly getRanking...
	# def getRanking(self, profile)
	
	def computeRoundLoser(self, profile, droppedOut):
		""" 
		Computes who should drop out on a round
		
		profile - voting profile given
		droppedOut - list of candidates who have already dropped out
		"""
		
		rankMaps = []
		counts = []
		for preference in profile:
			ranksMaps.append(preference.getReverseRankMap())
			counts.append(preferences.count)
		
		if (len(rankMaps) != len(counts)):
			print("something is wrong")
		
		totals = dict()
		for rank in rankMaps:
			for i in range(1, len(rank)):
				if (rank[i] not in droppedOut):
					if (rank[i] in totals):
						totals[rank[i]] += counts[i]
					else:
						totals[rank[i]] = counts[i]
					break
		
		minVotes = min(totals.values())
		losers = [key for key, value in totals.iteritems() if value == minVotes]
		return losers
	
	# def STVWinner(self, profile):
		"""
		Computes the winner(s) for STV voting
		
		TODO: implement this so it continually calls computeRound loser until a winner
		can be found
		"""	
	

	#Basic main that should get the winner
	# Phil still an't load prefpy....
def main():
	filename = "test.txt"
	candmap, rankmaps, rankmapcounts, numvoters = read_election_file(filename)
	prof = Profile(candmap, rankMaps)
	dropped = []

	while(dropped.len < candmap.len-1)
		dropped = computeRoundLoser(prof, dropped)

	for name in dropped:
		if name not in candmap:
			print name



main()