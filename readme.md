# Test your connection stability

##  <u>Problem:</u>
I came across this problem where my home internet connection was not stable. I was often disconnected and reconnected again, unable to access internet in the meantime.

Let's try to see what the problem is I said. Probably easy right ? **Not so much.** How can I see where the problem come from if I don't know the frequency of the disconnections, and how long they last...

I needed something to track down precisely when the connection was lost and the time between them, without having to check manually my devices.

##  <u>Solution:</u>
A simple python script that you let running in the background. This will create a logs.txt file with a timestamp for each time where the script was unable to receive a ping back from google.com (if any, but then you don't have disconnections...)

By default, the script will send a ping every 60 seconds. To increase or decrease the delay, simply change the last line of *main.py* as follow:

    main(time_in_seconds)

To view the output, simply open *logs.txt* which should be created in the folder of the script.