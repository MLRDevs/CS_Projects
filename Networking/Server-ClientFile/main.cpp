// Alex Miller
// Server programming, accepting client and sending whatever they want

#include <iostream>		// cout, cerr, etc
#include <stdio.h>		// perror
#include <string.h>		// bcopy
#include <netinet/in.h>		// struct sockaddr_in
#include <unistd.h>		// read, write, etc
#include <sys/types.h>
#include <sys/socket.h>
#include <netdb.h>
#include <assert.h>
#include <fstream>

using namespace std;

const int BUFSIZE=10240;

int MakeServerSocket(const char *port) {
	const int MAXNAMELEN = 255;
	const int BACKLOG = 3;
	char localhostname[MAXNAMELEN]; // local host name
	int s;
	int len;
	struct sockaddr_in sa;
	struct hostent *hp;
	struct servent *sp;
	int portnum;
	int ret;


	hp = gethostbyname("localhost");

	sscanf(port, "%d", &portnum);
	if (portnum ==  0) {
		sp=getservbyname(port, "tcp");
		portnum = ntohs(sp->s_port);
	}
	sa.sin_port = htons(portnum);

	bcopy((char *)hp->h_addr, (char *)&sa.sin_addr, hp->h_length);
	sa.sin_addr.s_addr = INADDR_ANY;
	sa.sin_family = AF_INET;

	s = socket(AF_INET, SOCK_STREAM, 0);

	ret = bind(s, (struct sockaddr *)&sa, sizeof(sa));
	if (ret < 0)
		perror("Bad");
	listen(s, BACKLOG);
	cout << "Waiting for connection on port " << port << endl;
	return s;
}
bool ErrorCheck(bool b, string s) { // error check, returns true if error, false if not
	if (b) {
		cout << s << endl;
		return true;
	}
	return false;
}
string getType(string s) { // get the content type
	if (s == "txt" ) return "text/plain";
	else if (s == "jpg") return "image/jpeg";
	else if (s == "html") return "text/html";
	else if (s == "gif") return "image/gif";
	return "ERROR";
}
bool RefuseChrome(char* buf, int bufsz) { // refuse any connection made from chrome
	string check = "";
	int spot = 0;
	for (int i=0; i < bufsz/2; i++) { // go through whole buf
		for (int j = i; j < i+13; j++) { // add chars from buf to string
			check += buf[j];
			spot = j;
		}
		if (check == "Google Chrome") { // return true if it is chrome
			return true;
		}
		else check = ""; // reset string if not
	}
	return false;
}
void Connection(int fd, char* buf) { // method that does everything, instead of using "goto" can just return

	// read in the data and print what the user wants
    int len = read(fd, buf, BUFSIZE);
	if (ErrorCheck(len == -1, "Bad Read")) return;
    buf[len] = 0;
    string req;
    for (int i=5; i < BUFSIZE; i++) { // get just the thing the user wants
        if (buf[i] == ' ') break;
        req += buf[i];
    }
	if (RefuseChrome(buf,len)) { // refuse any connection from chrome browser
		string header = "HTTP/1.1 401 Unauthorized. cannot use Chrome\r\n";
		len = write(fd, header.c_str(), header.length());
		if (ErrorCheck(len == -1,"Bad write")) return;
		return;
	}

	// getting the file type
	string type = "";
	bool after = false; // bool for after '.' in file type
	for (int i=0; i < req.length(); i++) {
		if (after) type += req[i]; // get the chars for the file type
		else if (req[i] == '.') after = true;
	}
	type = getType(type); // change it so that it can be used in metadata

	// open file
	fstream in(req, ios::in | ios::binary); // open in binary so images can be used as well
	if (in.fail()) { // file does not exist
		string header = "HTTP/1.1 404 NOT FOUND\r\n";
		len = write(fd,header.c_str(),header.length());
		if (ErrorCheck(len == -1,"Bad Write")) return;
		return; // return if the file does not exist
	}

	int filesz = 0; // size of the file
	in.seekg(0, ios::end);
	filesz = in.tellg(); // get the size of the file
	in.seekg(0, ios::beg);

	string filesize = to_string(filesz); // change to string so can print to console

	// Write to the web client
	string header = "HTTP/1.0 200 OK\r\nContent-Type: " + type + "\r\nContent-Size: " + filesize + "\r\n";
	if (header.length() != write(fd, header.c_str(), header.length())) return;
	write(fd, "\r\n", 2);
	if (ErrorCheck(len == -1, "Bad write")) return;

	char* filebuffer = new char[filesz]; // buf to put the file contents into

	// get the file to the browser
	string get;
	in.read(filebuffer, filesz);
	in.close(); // done with file so close it
	len = write(fd, filebuffer, filesz);
	if (ErrorCheck(len == -1, "Bad write")) return;
}
int main(int argc, char *argv[]) { // main method


	int s; 			// socket descriptor
	int len;		// length of reveived data
	char buf[BUFSIZE];	// buffer in which to read
	int ret;		// return code from various system calls


	s = MakeServerSocket(argv[1]); // make socket

	while (1) { // while program is running
		struct sockaddr_in sa;
		int sa_len = sizeof(sa);
		int fd = accept(s, (struct sockaddr *)&sa, (unsigned int *)&sa_len); // accept the request
		assert(fd != -1);

		Connection(fd, buf); // used to do just about everything, used instead of doing "goto"
		close(fd);
	}
}