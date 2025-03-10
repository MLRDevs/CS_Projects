// Alex Miller
// get info from the user and send an email over smtp

#include <iostream>		
#include <stdio.h>	
#include <string.h>
#include <netinet/in.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netdb.h>
#include <stdlib.h>
#include <fstream>
#include<time.h>

using namespace std;

const int BUFSIZE=1024;

void ErrorCheck(bool error, string msg) { // error check
    if (error) { // if error, print msg and exit
      cout << msg << endl;
      exit(1);
    }
}

int MakeSocket(const char *host, int port) {
	int s; 			
	int len;	
	struct sockaddr_in sa; 
	struct hostent *hp;
	struct servent *sp;
	int portnum;	
	int ret;

	hp = gethostbyname(host);
	if (hp == 0) {
		perror("Bad hostname lookup");
		exit(1);
	}
	bcopy((char *)hp->h_addr, (char *)&sa.sin_addr, hp->h_length);
	sa.sin_family = hp->h_addrtype;
	sa.sin_port = htons(port);
	s = socket(hp->h_addrtype, SOCK_STREAM, 0);
	if (s == -1) {
		perror("Could not make socket");
		exit(1);
	}
	ret = connect(s, (struct sockaddr *)&sa, sizeof(sa));
	if (ret == -1) {
    perror("Could not connect");
		exit(1);
  }
	return s;
}

void ReadNCheck(char* buf, int sock) { // check to make sure getting a 200 or 300 number 
    int len = read(sock, buf, 999);
    buf[len] = 0;
    ErrorCheck(len == -1, "Bad Read");

    if (buf[0] != '2' && buf[0] != '3') {
        cout << "ERROR, NOT 2 OR 3" << endl;
        cout << buf;
        exit(1);
    }
    cout << buf;
}
void Write(char* buf, int sock, string ans) {
    int len = write(sock, ans.c_str(), ans.length());
    ErrorCheck(len == -1, "Bad Write");
}
string GetMetaData(int index, string s) { // switch case to get the metadata so not to repeat code
    
    switch(index) {
        case 0:
            return s + "\r\n";
        case 1:
            return "Message-ID:<CAEb5kgpPWSWWqL0Kj=Nui2NbTcF+_tB6CKXfAQzdZBpK6wzp=w@mail.gmail.com>\r\n";
        case 2:
            return "";
        case 3:
            return "";
        case 4:
            return "";
        case 5:
            return "\r\n";
    }
    return "ERROR METADATA";
}
string GetPrompt(int index) { // switch case to get prompt so not to repeat code

    switch(index) {
        case 0:
            return "Who are you? ";
        case 1:
            return "Where is the mail coming from? ";
        case 2:
            return "Who is the recipient? ";
        case 3:
            return "What is the subject? ";
    }

    return "ERROR PROMPT";
}
string GetMsg(int index, string ans) { // switch case to get message to send so not to repeat code

    switch(index) {
        case 0:
            return "HELO " + ans + "\r\n";
        case 1:
            return "MAIL FROM:<" + ans + ">\r\n";
        case 2:
            return "RCPT TO:<" + ans + ">\r\n";
    }
    return "ERROR MSG";
}
string GetTime(string s) { // gets the time in the right format
    string year;
    for (int i=s.length()-5; i < s.length()-1; i++) { // get the year
        year += s[i];
    }
    string day = "";
    char temp = 'a';
    int index = 0;

    // get the other data
    while(temp != ' ') { // gets the day of the week
        temp = s[index];
        day += temp;
        index++;
    }
    string actualday  = "";
    for (int i=0; i < day.length()-1; i++) {
        actualday += day[i];
    }
    temp = 'a';
    string month = "";
    while(temp != ' ') { // gets the month
        temp = s[index];
        month += temp;
        index++;
    }
    temp = 'a';
    string date = "";
    while(temp != ' ') { // get the date of the month
        temp = s[index];
        date += temp;
        index++;
    }
    temp = 'a';
    string t = "";
    while(temp != ' ') { // gets the time
        temp = s[index];
        t += temp;
        index++;
    }
    string dateNtime = actualday + ", " + date + month + year + " " + t;
    return dateNtime;
}

int main() { // get info from the user and send an email over smtp

    // getting the time
    time_t ltime;
    time(&ltime); 
    string s = ctime(&ltime);
    string time = GetTime(s); // print -> Fri Feb 23 15:00:00 2024 type of format

    char buf[1000];
    int sock = MakeSocket("gmail-smtp-in.l.google.com", 25); // making the connection
    ErrorCheck(sock == -1, "Bad Connection");

    ReadNCheck(buf,sock);

    // strings used for later for sending the to and from addresses
    string to;
    string from;
    string subject;

    for (int i=0; i < 4; i++) { // for loop to get all of the info from the user
        string ans;
        cout << GetPrompt(i); // print the right prompt to the user
        getline(cin, ans);
        if (i == 1) from = ans; // special case for to 
        else if (i == 2) to = ans; // special case for from
        else if (i == 3) subject = ans; // special case for subject

        if (i != 3) { // as long as its not the subject line, send the command
            ans = GetMsg(i, ans); // add whatever the user put to make the command
            cout << ans << endl;
            Write(buf, sock, ans);

            ReadNCheck(buf,sock); // make sure everything is good
        }
    }

    // send data
    string send = "DATA\r\n";
    Write(buf, sock, send);
    cout << send << endl;

    // make sure everything is good
    ReadNCheck(buf,sock);

    // sending the metadata the same way as the other info
    for (int i=0; i < 6; i++) { 
        string send = GetMetaData(i,time);
        if (i == 2) send = "Subject: " + subject + "\r\n";
        else if (i == 3) send = "To:" + to + "\r\n";
        else if (i == 4) send = "From:" + from + "\r\n";

        Write(buf, sock, send);
        cout << send << endl;
    }


    // send message
    string ans;
    cout << "Enter the message, end the message with a \'.\' on a blank line " << endl;

    // loop to get the whole message
    while(true) {
        getline(cin,ans);
        ans += "\r\n";
        Write(buf, sock, ans);
        if (ans[0] == '.') break;
    }

    // make sure everything is good
    ReadNCheck(buf,sock);

    // send the quit message
    ans = "QUIT\r\n";
    Write(buf, sock, ans);
    cout << ans << endl;

    // make sure everything is good
    ReadNCheck(buf,sock);

    // end the program with a message
    cout << "Email has been sent!" << endl;
}