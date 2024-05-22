// Alex Miller
// Send and recieve bytes from server at specific port


#include <iostream>
#include <stdio.h>
#include <string.h>
#include <netinet/in.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netdb.h>
#include <stdlib.h>

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

int main(int argc, char *argv[]) { // take a server and a port number, send and read bytes

    string hostname = argv[1];
    int portnum = stoi(argv[2]);
    char buf[1000];
    int sock = MakeSocket(hostname.c_str(), portnum);
    ErrorCheck(sock == -1, "Bad Connection");

    int len;
    int len2;
    string send;
    cout << "What do you want to send to the server: "; // thing to send to server
    getline(cin,send);
    send += "\r\n\r\n";
    //cout << send << endl;
    while (len2 != 0) { // while there is a connection
        len = write(sock, send.c_str(), send.length()); // write to server
        ErrorCheck(len == -1, "Bad Write");
        len2 = read(sock, buf, 999); // read from server
        ErrorCheck(len2 == -1, "Bad Read");
        buf[len2] = 0; // stop reading
        cout << buf; // print result
    }
    cout << endl;
}

