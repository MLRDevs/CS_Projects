// Alex Miller
// easy way to describe file compression algorithms

// file compression takes redundent data and replaces it with a key that is then used in a dictionary

// EX: "one thousand ants, two thousand ants, three thousand ants, four thousand ants"
// replace "thousand" and "ants" with  1 and 2 respectively
// "one 1 2, two 1 2, three 1 2"
// then add the dictionary to the file to decompress it

// this is a program that mocks this scenario with any sentence

#include <iostream>
#include <cstdlib>
#include <string>
using namespace std;

int wordcount = 1000;

bool search(string back[], string s) { // return true if string is already inside array
    for (int i=0; i < wordcount; i++) {
        if (back[i] == s) return true;
    }
    return false;
}
int getvalue(string rep[], string s) { // return the place where the string is in the array
    for(int i=0; i < wordcount; i++) {
        if (rep[i] == s) return i;
    }
    return -1;
}
void run(string sent) { // method that does everything

    cout << endl;

    // this is our dictionary
    string *words = new string[wordcount]; // array of all the words

    // count all the spaces in the sentence and get the words and put them in the array
    int i = 0;
    int j = 0;
    string word;
    while (i < sent.length()) { // go through whole sentence
        if (sent[i] != ' ' && i != sent.length()-1) { // if not a space add to the current word
            word += sent[i];
            i++;
        }
        else { // if space or last char
            if (i == sent.length()-1) word += sent[i]; // if last char then add it

            // add the word to the array and reset
            words[j] = word;
            word = "";
            j++;
            i++;
        }
    }

    string *repeats = new string[wordcount]; // array for checking repeats
    string *backup = new string[wordcount]; // backup array to compare

    // go through words array, add word to backup, if not first time, add to repeats
    // this way we get only repeated words inside the repeat array

    j = 0;
    for (int i=0; i < wordcount; i++) { // go through whole words array
        if (search(backup, words[i]) && !search(repeats, words[i])) { // if word is in backup and not in repeats, add it to repeats
            repeats[j] = words[i];
            j++;
        }
        else { // otherwise add to backup
            backup[i] = words[i];
        }
    }
    
    // assign ints to the repeated words and put it all together
    string ans; // answer string
    for (int i=0; i < wordcount; i++) { // go through whole array of words
        if (words[i] == "") break; // this line is here for array sake, doesn't print a bunch of nothing if a lot of the array is empty
        if (search(repeats,words[i])) ans += to_string(getvalue(repeats, words[i])); // if its repeated, use the number where it is in the repeat array
        else {
            ans += words[i]; // else use the word
        }
        ans += " "; // add spaces between words
    }

    // give results from original sentence to new sentence
    cout << endl;
    cout << "Original Sentence: " << sent << endl;
    cout << "Character Count: " << sent.length() << endl;
    cout << endl;
    cout << "New Sentence: " << ans << endl;
    cout << "Characer Count: " << ans.length()-1 << endl; // length()-1 to not count last space when adding the words to the ans string
    cout << endl;

    cout << "Dictionary keys:" << endl;
    // print the dictionary keys
    for (int i=0; i < 1000; i++) {
        if (repeats[i] != "") cout << i << "-" << repeats[i] << endl;
    }
    cout << endl;

    // deallocation
    delete[] words;
    delete[] backup;
    delete[] repeats;
}
int main(int argc, char** argv) { // main method

    // get the original sentence
    string sentence = "";

    while (sentence != "EXIT") { // until user exits
        cout << "Enter sentence (EXIT to exit): ";
        getline(cin, sentence);
        if (sentence == "EXIT") exit(1);
        else run(sentence);
    }

    return 0;
}
