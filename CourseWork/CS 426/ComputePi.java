// Alex Miller
// calculate pi using dart throwing unit circle technique using multiple threads and compute the time it took

import java.io.*;
import java.util.*;
import java.util.concurrent.ThreadLocalRandom;

public class ComputePi {

    public static Scanner in;
    
    public static void main(String args[]) { // main

        // initialize scanner
        in = new Scanner(System.in);

        // ask user for amount of threads
        System.out.print("Enter the amount of threads: ");
        double tcount = in.nextInt(); // make it a double for more accurate pi later

        // timer in milliseconds
        long timer = 0;

        // create array of threads with the amount user requested
        thread[] arr = new thread[(int)tcount];

        // loop for making and placing threads
        for (int i=0; i < tcount; i++) {
            thread t = new thread();
            arr[i] = t;
            t.tcount = (int)tcount; // set the thread count in the thread so not all the threads are doing too much work
        }

        // loop for starting
        for (int i=0; i < tcount; i++) {
            arr[i].start();
        }

        // loop for joining
        for (int i=0; i < tcount; i++) {
            try {
                arr[i].join();
            }
            catch (InterruptedException e) { // error catch
                System.out.println("ERROR IN JOIN");
                System.exit(0);
            }
        }

        // getting pi
        double pi = 0.0;
        for (int i=0; i < tcount; i++) {
            pi += arr[i].pi;
        }

        pi /= tcount; // average of pi between all the threads
        timer = arr[0].timer; // get the timer from first thread since each thread has the same time

        // print results
        System.out.println("pi is: " + pi);
        System.out.println("with " + (int)tcount + " threads");
        System.out.println("in " + timer + " milliseconds");

    }
}
class thread extends Thread { // class of the stuff the thread will do

    double pi;
    long timer;
    int amount =  1000000000; // amount of darts thrown
    int tcount = 0; // amount of threads
    public void run() {

        // x and y coordinates
        double x = 0.0;
        double y = 0.0;

        // hits and tosses onto the unit square
        double hits = 0.0;
        double tosses = 0.0;

        // start time
        long start = System.currentTimeMillis();

        // loop to run to throw darts
        for (int i=0; i < amount/tcount; i++) { // split the total amount of darts between all the threads
            // Random numbers, x and y coordinates
            x = ThreadLocalRandom.current().nextDouble(0,1);
            y = ThreadLocalRandom.current().nextDouble(0,1);

            // get the sides of the triangle to find the distance from the center to the random point
            double distA = Math.abs(y-0.5);
            double distB = Math.abs(x-0.5);
            double distC = Math.sqrt((distA*distA) + (distB*distB));

            // if the point is inside the circle
            if (distC < 0.5) hits++;
            tosses++;

        }

        // compute pi
        pi = (hits/tosses) * 4;

        // end time
        long end = System.currentTimeMillis();
        timer = end-start;
    }
}