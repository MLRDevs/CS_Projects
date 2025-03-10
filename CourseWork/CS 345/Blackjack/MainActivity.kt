// Alex Miller
// game of blackjack

package com.example.pg2_blackjack

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.text.method.ScrollingMovementMethod
import android.widget.Button
import android.widget.TextView

class MainActivity : AppCompatActivity() { // main
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        // Buttons and displays for cards, game ending, and value of the hand
        var HitButt: Button? = null
        var StandButt: Button? = null
        var CardDisplay: TextView? = null
        var ValueDisplay: TextView? = null
        var EndDisplay: TextView? = null

        HitButt = findViewById(R.id.HitButt)
        StandButt = findViewById(R.id.StandButt)
        CardDisplay = findViewById(R.id.CardDisplay)
        ValueDisplay = findViewById(R.id.ValueDisplay)
        EndDisplay = findViewById(R.id.EndDisplay)

        CardDisplay!!.movementMethod = ScrollingMovementMethod()

        // stand button
        StandButt!!.setOnClickListener {
            StandButt.isEnabled = false
            HitButt.isEnabled = false
            GetOutcome(ValueDisplay.text.toString().toInt(), EndDisplay)
        }

        var cards = MakeCards() // make the cards
        var ACES = arrayOf(
            "ACE OF CLUBS",
            "ACE OF SPADES",
            "ACE OF DIAMONDS",
            "ACE OF HEARTS"
        ) // keep track of what ACE are 1 and what ACE are 11
        var decksz = 52
        var Hand = Array<String>(11) { "" }
        var ct = 0 // how many cards are in the hand
        while (ct != 2) {
            var newcard = GetNewCard(decksz, cards, CardDisplay)
            decksz--
            Hand[ct] = newcard // put it in the hand
            ct++
        }

        // get the values of the first two cards and add them together
        var handnum = 0 // hand value
        var num = CardToNum(Hand[0]) // value of current card
        if (num == 0) handnum += 11 // if an ACE add 11
        else handnum += num
        num = CardToNum(Hand[1])
        var temp = handnum + 11
        if (num == 0 && temp <= 21) handnum += 11 // if one ACE add 11
        else if (num == 0) { // if two ACEs, make the second ACE a 1
            handnum += 1
            AceCheck(
                ACES,
                Hand[1]
            ) // update the ACES array so to not repeat changing an ACE I already have
        } else handnum += num

        ValueDisplay!!.text = handnum.toString() // display the hand value
        if (handnum == 21) { // in case the two cards off the start are 21
            HitButt.isEnabled = false
            StandButt.isEnabled = false
            GetOutcome(handnum, EndDisplay)
        }

        // hit button
        HitButt!!.setOnClickListener {
            ValueDisplay.text = handnum.toString() // display the hand value
            var pickedcard = GetNewCard(decksz, cards, CardDisplay)
            decksz--
            ct++
            Hand[ct] = pickedcard // put the new card in the hand
            var num = CardToNum(Hand[ct])
            if (num == 0) { // account for ACE
                var temp = handnum + 11
                if (temp <= 21) handnum += 11
                else {
                    handnum += 1
                    AceCheck(
                        ACES,
                        pickedcard
                    ) // update the ACES array so to not repeat changing an ACE I already have
                }
            } else handnum += num
            handnum = CheckForDrop(
                handnum,
                Hand,
                ACES,
                ct
            ) // check to see if a previous 11 can be changed to a 1
            ValueDisplay.text = handnum.toString() // update the hand value
            if (handnum >= 21) { // check if the game is over
                HitButt.isEnabled = false
                StandButt.isEnabled = false
                GetOutcome(handnum, EndDisplay)
            }
        }

    }
    fun GetOutcome(
        handnum: Int,
        EndDisplay:TextView
    ) { // get the outcome of the game
        if (handnum <= 21) EndDisplay.text = "You Win"
        else EndDisplay.text = "You Bust"
    }
    fun CheckForDrop(
        handnum: Int,
        Hand: Array<String>,
        ACES: Array<String>,
        ct: Int
    ): Int { // check if an ace can go from an 11 to a 1
        var num = handnum
        for (i in 0..ct - 1) { // loop through hand
            if (Hand[i].substringBeforeLast(" OF") == "ACE" && num > 21) { // if there is an ACE
                for (j in 0..3) {
                    if (Hand[i] == ACES[j]) { // check if I have already made this ACE a 1
                        num -= 10
                        ACES[j] = ""
                    }
                }
            }
        }
        return num
    }

    fun GetNewCard(
        decksz:Int,
        cards: Array<String>,
        CardDisplay: TextView
    ): String { // get a new card from the deck
        var pickedcard = (Math.random() * decksz).toInt()
        CardDisplay.text = CardDisplay.text.toString() + "${cards[pickedcard]}\n"
        var newcard = cards[pickedcard]
        var decksize = decksz - 1 // changing the decksize to take the last card and put where the new card was picked
        cards[pickedcard] = cards[decksize]
        return newcard
    }

    fun AceCheck(
        ACES: Array<String>,
        card: String
    ) { // Update ACES array for ACE I have already made a 1
        for (i in 0..3) {
            if (card == ACES[i]) ACES[i] = ""
        }
    }

    fun CardToNum(card: String): Int { // get the value of the card
        var s = card.substringBeforeLast(" OF")
        if (s == "TWO") return 2
        else if (s == "THREE") return 3
        else if (s == "FOUR") return 4
        else if (s == "FIVE") return 5
        else if (s == "SIX") return 6
        else if (s == "SEVEN") return 7
        else if (s == "EIGHT") return 8
        else if (s == "NINE") return 9
        else if (s == "TEN" || s == "JACK" || s == "QUEEN" || s == "KING") return 10
        else return 0 // ACE
    }
        fun MakeCards(): Array<String> { // Make the deck of cards
            var cards = Array<String>(52) { "" }
            var s = ""
            var ct = 0
            for (i in 0..12) { // every ranks
                for (j in 0..3) { // every suit
                    if (i == 0) s += "ACE"
                    else if (i == 1) s += "TWO"
                    else if (i == 2) s += "THREE"
                    else if (i == 3) s += "FOUR"
                    else if (i == 4) s += "FIVE"
                    else if (i == 5) s += "SIX"
                    else if (i == 6) s += "SEVEN"
                    else if (i == 7) s += "EIGHT"
                    else if (i == 8) s += "NINE"
                    else if (i == 9) s += "TEN"
                    else if (i == 10) s += "JACK"
                    else if (i == 11) s += "QUEEN"
                    else s += "KING"

                    s += " OF "
                    if (j == 0) s += "CLUBS"
                    else if (j == 1) s += "SPADES"
                    else if (j == 2) s += "DIAMONDS"
                    else s += "HEARTS"

                    cards[ct] = s
                    s = ""
                    ct++
                }
            }
            return cards
        }
}