// Alex Miller
// reads in cards and prints the poker hand equivalent 

fun main() {
	var cards = Array<String> (5) {""} // array of the cards
	for (i in 0..4) {
		print("Enter Card #${i+1}: ")
		var card = readLine()!!
		cards[i] = card.uppercase() // make all the cards uppercase
	}
	println()
	var ranks = Array<Int> (13) {0} // array of rank numbers
	var Suits = Array<Int> (4) {0} // array of suit numbers
	for (card in cards) {
		var rank = card.substringBeforeLast(" OF") // get the rank
		var rn = CardtoRank(rank)
		ranks[rn-1]++ // adjust the rank counter
		
		var suit = card.substringAfter("OF ") // get the suit
		var sn = CardtoSuit(suit)
		Suits[sn-1]++ // adjust suit counter, here so it's easy to find a flush
	}
	var pairct = Array<Int> (5) {0} // pair counter
	for (rank in ranks) { // adjust pair counter
		if (rank == 4) pairct[0]++
		else if (rank == 3) pairct[1]++
		else if (rank == 2) pairct[2]++
		else if (rank == 1) pairct[3]++
		else if (rank == 0) pairct[4]++
	}
	var flush = false
	if (5 in Suits) { // check if there is a flush
		flush = true
	}
	
	FindHand(pairct, ranks, flush) // find the hand
	
}
fun FindHand(pairct: Array<Int>, ranks: Array<Int>, flush: Boolean) { // print the hand with the given cards
	if (flush) { // if there is any kind of flush then it is one of these
		if (CheckStraight(ranks)) print("You have a Straight Flush")
		else if (CheckRoyal(ranks)) print("You have a Royal Flush")
		else print("You have a Flush")
	}
	else { // not a flush
		if (CheckStraight(ranks)) { // check for normal straight
			print("You have a Straight")
		}
		// check the pairs
		else if (pairct[0] == 1) print("You have a Four of a Kind")
		else if (pairct[1] == 1 && pairct[2] == 1) print("You have a Full House")
		else if (pairct[1] == 1) print("You have a Three of a Kind")
		else if (pairct[2] == 2) print("You have a Two Pair")
		else if (pairct[2] == 1) print("You have a Pair")
		else { // check the highs
			if (ranks[0] == 1) print("You have Ace high") // if Ace high
			else {
				for (i in 12 downTo 6) { // get the highest card that isn't an Ace
					if (ranks[i] == 1) {
						var card = RanktoCard(i)
						print("You have ${card} High")
					}
				}
			}
		}
	}
}
fun RanktoCard(rank: Int): String { // return the string equivalent of the rank
	if (rank == 12) return "King"
	else if (rank == 11) return "Queen"
	else if (rank == 10) return "Jack"
	else if (rank == 9) return "Ten"
	else if (rank == 8) return "Nine"
	else if (rank == 7) return "Eight"
	else if (rank == 6) return "Seven"
	return ""
}
fun CheckStraight(ranks: Array<Int>): Boolean { // check if there is a Straight
	for (i in 0..8) {
		if (ranks[i] == 1 && ranks[i+1] == 1 && ranks[i+2] == 1 && ranks[i+3] == 1 && ranks[i+4] == 1) return true
	}
	return false
}
fun CheckRoyal(ranks: Array<Int>): Boolean { // check if there is a Royal Flush
	if (ranks[0] == 1 && ranks[12] == 1 && ranks[11] == 1 && ranks[10] == 1 && ranks[9] == 1) return true
	return false
}
fun CardtoRank(card:String): Int { // return the integer equivalent of the rank
	if (card == "ACE") return 1
	else if (card == "TWO") return 2
	else if (card == "THREE") return 3
	else if (card == "FOUR") return 4
	else if (card == "FIVE") return 5
	else if (card == "SIX") return 6
	else if (card == "SEVEN") return 7
	else if (card == "EIGHT") return 8
	else if (card == "NINE") return 9
	else if (card == "TEN") return 10
	else if (card == "JACK") return 11
	else if (card == "QUEEN") return 12
	else if (card == "KING") return 13
	return 0
}
fun CardtoSuit(card:String): Int { // return the integer equivalent of the suit
	if (card == "HEARTS") return 1
	else if (card == "SPADES") return 2
	else if (card == "CLUBS") return 3
	else if (card == "DIAMONDS") return 4
	return 0
}