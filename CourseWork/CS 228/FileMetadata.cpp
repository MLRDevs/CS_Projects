// Alex Miller
// take hostname and file from command line, print metadata and read the bytes of the file to a new one

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
    char buf[1000];
    int sock = MakeSocket(argv[1], 80);
    ErrorCheck(sock == -1, "Bad Connection");
    string url = argv[2];

    string cmd = "GET " + url + " HTTP/1.0\r\n\r\n";
    int len = write(sock, cmd.c_str(), cmd.length()); // write command
    ErrorCheck(len == -1, "Bad Write");

    char big[100000]; // big array to hold everything
    int bspot = 0; // index to keep track of where inside of big
    int len2 = 1;
    int alen = 0; // amount of bytes read total so to not read null bytes later on if read is less than the big array size
    while (len2 > 0) {
        len2 = read(sock, buf, 999);
        ErrorCheck(len2 == -1, "Bad Read");
        buf[len2] = 0;
        for (int i=0; i < len2; i++) { // add everything from buf into the big array
            big[bspot] = buf[i];
            bspot++;
        }
        alen += len2; // increase amount of bytes read
    }

    // error check for HTTP/1.1 200
    string num = "";
    num += big[9];
    num += big[10];
    num += big[11];
    ErrorCheck(num != "200", "Error, not 200");

    // looking for border
    string check = "";
    int border = 0;
    for (int i=0; i < alen; i++) { // go through each byte
        for(int j=i; j < i+4; j++) { // get a group of bytes and compare
            check += big[j];
        }
        if (check == "\r\n\r\n") { // break if border is found
            border = i; // save where the border starts
            break;
        }
        else {
            cout << big[i]; // print everything before the border is found
            check = "";
        }
    }

    cout << endl;

    // adding the data to the file
    int start = border+4; // start of data
    ofstream out("output.jpg"); // output file
    ErrorCheck(out.fail(), "File will not open");
    for (int i=start; i < alen; i++) { // put all the bytes into a new file
        out << big[i];
    }
}

