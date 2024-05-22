// Alex Miller
// Telnet Client

#include <sys/poll.h>
#include <sys/time.h>
#include <iostream>		// cout, cerr, etc
#include <stdio.h>		// perror
#include <string.h>		// bcopy
#include <netinet/in.h>		// struct sockaddr_in
#include <unistd.h>		// read, write, etc
#include <sys/types.h>
#include <sys/socket.h>
#include <netdb.h>
using namespace std;

const int BUFSIZE=1024;

bool ErrorCheck(bool b, string s) { // error checking, if b print error and return true, false otherwise
    if (b) {
        cout << s << endl;
        return true;
    }
    return false;
}

int MakeSocket(const char *host, const char *port) {
	int s;
	int len;
	struct sockaddr_in sa;
	struct hostent *hp;
	struct servent *sp;
	int portnum;
	int ret;

	hp = gethostbyname(host);
	ErrorCheck(hp==0, "Gethostbyname");
	bcopy((char *)hp->h_addr, (char *)&sa.sin_addr, hp->h_length);
	sa.sin_family = hp->h_addrtype;
	sscanf(port, "%d", &portnum);
	if (portnum > 0) {
		sa.sin_port = htons(portnum);
	}
	else {
		sp=getservbyname(port, "tcp");
		portnum = sp->s_port;
		sa.sin_port = sp->s_port;
	}
	s = socket(hp->h_addrtype, SOCK_STREAM, 0);
	ErrorCheck(s == -1, "Could not make socket");
	ret = connect(s, (struct sockaddr *)&sa, sizeof(sa));
	ErrorCheck(ret == -1, "Could not connect");
	return s;
}

int main(int argc, char *argv[]) { // main method

    int server = MakeSocket(argv[1], argv[2]);
    if (ErrorCheck(server == -1, "Bad connection")) exit(0);

    // poll struct
    struct pollfd questions[2];
    questions[0].fd = 0;
    questions[0].events = POLLIN;
    questions[1].fd = server;
    questions[1].events = POLLIN;
    string quit; // string for checking for "quit\n"
    while(1)
    {
        char c;
        int p = poll(questions,2,-1); // create poll
        if (ErrorCheck(p == -1, "Poll error")) exit(0);

        if (questions[0].revents & POLLIN) { // if data from keyboard
            int len = read(0,&c,1); // read in from the keyboard
            if (ErrorCheck(len == -1, "Bad read from keyboard")) exit(0);

            if (c == '\n' && quit != "quit") { // if end of command and command is not going to be quit
                c = '\r';
                int len = write(questions[1].fd,&c,1);
                if (ErrorCheck(len == -1, "Bad read from keyboard")) exit(0);
                c = '\n';
                len = write(questions[1].fd,&c,1);
                if (ErrorCheck(len == -1, "Bad read from keyboard")) exit(0);

                quit = ""; // reset the quit string
            }
            else { // if not end of command then just send the char
                len = write(questions[1].fd,&c,1); // write to server
                if (ErrorCheck(len == -1, "Bad write to server")) exit(0);
            }

            // deal with exit
            if (quit.length() < 5) quit += c;
            if (quit.length() == 5) { // if the string has the same length as "quit\n"
                if (quit == "quit\n") exit(0); // quit if s is "quit\n"
                else quit = ""; // reset s if not
            }
        }
        if (questions[1].revents & POLLIN) { // if data from server
            int len = read(questions[1].fd,&c,1); // read from server
            if (ErrorCheck(len == -1, "Bad read from server")) exit(0);
            if (len < 1) continue; // stop continuous screen sends of nothing
            len = write(1,&c,1); // write to screen
            if (ErrorCheck(len == -1, "Bad write to screen")) exit(0);

            quit = ""; // if writing back to screen, command was sent so reset s
        }
    }
}