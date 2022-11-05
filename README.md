# 5541HW6
The goal is to improve your knowledge of signal processing and Fourier Transforms by working with sound files directly.

 
Requirements

This homework must be written in either Python or Java, whichever you want.

You may work with a partner of your choice (or alone) on this homework.

On the course site, you will find links to NLTK's sample of TIMIT data.

 
Your Task

Your task will be to write a program named spectro.py, (or its Java equvalent) that when given a .wav file name, will display the spectrogram of that file.

 
WAV File Format

As we will be working with files from the TIMIT corpus, we can tailor our programs to work with that data particularly.

The first step is simply understanding how to get raw data out of a WAV file.

This is often the most difficult part of the process. You will need to look at file formats and determine how to read bytes from these particular TIMIT files.

This is actually a very difficult process to do by hand (trust me on this one...) that involves knowledge of bytereaders, endianness and an extremely careful attention to sound file specifications. Instead, I strongly recommend that you use a library for reading the sound file. In python, we have the wave library available to us. In Java, there are a few possibilities, I recommend reading this pageLinks to an external site..

TIMIT's audio files are in .wav format, with 1 channel, 16-bit samples, and a 16,000 Hz sample rate.

To make sure that you are reading the data in properly, there are a few sanity checks that I recommend:

    Try printing out the sample value at every 1000th frame or so, then use an audio analysis program (like Audacity) to see if those values match.
    Write a visual output that will plot the sample value at each frame and create a graph of the sound over time. (This second thing is tricky, but very useful to do, since you'll be expected to do visualization later in the project.)

Data Windows

To be able to perform our data visualization and Fourier transform, we need to set an appropriate window size. Begin with a rectangular window with size s = 25 ms (the book refers to this as frame size). Generate a window x[n], ..., x[n+s] based on this window size by taking a slice of the array of samples.

 

Q: You give a window size in milliseconds, but how many samples is that?

A: Good question. Using your sample rate, you should be able to do a little math and convert this properly.

 

You will create a new data window each 10 ms. Again, you'll need to think about conversion from milliseconds to samples. Note that the windows are larger than the step. This is on purpose! See the illustration in section 9.3.2 in the book for a clear example of what is happening.

Once you have created the data windows, you should end up with a list of windows of data, that is, a list of slices of the sound file. In my code, this is a list of lists of samples.
Fourier Transform

So, (again referring to the book,) for each 10 ms time step, you will have a window x[n], ..., x[n+s]. This will be passed to a Fourier Transform function that converts to the frequency domain.

Use libraries for an effective Fourier Transform function. While I'd love to go into the details of the Fast Fourier Transforms, we just don't have the time. Therefore, I once again refer you to some libraries.

In python3, numpy has multiple DFT (Discrete Fourier Transform) and FFT (Fast Fourier Transform) functions that you can apply. For Java, feel free to look up an FFT Java implementation and copy it, make sure to credit where you got it.

The output from a Fourier Transform is an array of complex numbers, denoted as X[k] in the book. To convert each of X[k] to a magnitude, square the real and imaginary components of the complex number, add them, then take the square root to get what is known as the square magnitude. Then, convert from that to log scale with the formula 10 * log10 (square magnitude). (This has the effect of making the visualization nicer.)

Each window should have been translated via the FFT to a list of frequency magnitudes. Therefore, you should now have a list of lists of frequency magnitudes at each timestep.
Visualization

Find your own simple image manipulation package, or use pyplot. All you need is the ability to create an image and set pixel color values.

The traditional visualization for a spectrogram is as the pictures shown in the book: A black-and-white image, with time along the x-axis, (where each 10ms window is 1 pixel of width), frequency along the y-axis and intensity indicated by the darkness of the pixel, with white meaning 0 intensity and black meaning maximum intensity.
Restrictions

    You may not use libraries other than the ones mentioned here: numpy's fft functions, wave, pyplot or maybe a different one for simple visualization

Rubric
HW6 Rubric
HW6 Rubric
Criteria 	Ratings 	Pts
This criterion is linked to a Learning Outcome Wave file reading
	
3 pts
Full Marks
Reads .wav file properly, using library and properly translating data to int
	
0 pts
No Marks
No attempt
	
3 pts
This criterion is linked to a Learning Outcome Windowing
	
5 pts
Full Marks
Input properly divided into multiple overlapping windows and use a hamming (or hanning) window function
	
3 pts
Some errors
Missing window function or windows non-overlapping
	
0 pts
No Marks
No attempt
	
5 pts
This criterion is linked to a Learning Outcome Fourier Transform
	
4 pts
Full Marks
Pass all windows of samples into a Fourier Transform (either from a library or in code). Output from each window converted to log of square magnitude.
	
2 pts
Some errors
square magnitude conversion missing, maybe other small errors in this process
	
0 pts
No Marks
No attempt
	
4 pts
This criterion is linked to a Learning Outcome Visualization
	
3 pts
Full Marks
Convert magnitudes to grayscale values and create an image.
	
0 pts
No Marks
No attempt
	
3 pts
Total Points: 15
