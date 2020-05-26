# SpeechLogger

The simple application for logging (and translating) all speech from your microphone and speaker.

I think it would be very useful when you communicate with somebody foreign person by Discord or else app. It can help you to have better understanding your interlocutor if you know his language like I do english) 


## First result

Scope:

* Translation messages from any languages supported by [Google](https://cloud.google.com/speech-to-text/docs/languages) into certain choosen languages at once

* Recognition and translation the speech on choosen language from microphone

TODO:

* recognize all speech from microphone automatically (not only on demand)

* recognize speech from speakers (it will be hard to do)

* write program into desktop app

* add text logging in file

![1](https://github.com/PasaOpasen/SpeechLogger/blob/master/gifs/first.gif)

### How to run

**You can download this app as compiled** (see [releases](https://github.com/PasaOpasen/SpeechLogger/releases)). Unpack and run **.exe** file.

### Notes 

* Not correct showing of arabic words (reversed and upper-cased) exists because of [bags with windows terminal](https://github.com/microsoft/terminal/issues/538). But u will copy this text and paste it into text editor / google / messanger, it would be normal. 

## Second result

What's new:

* recognition speech from speakers too (if u have a speaker supported callbacks)

![see](https://github.com/PasaOpasen/SpeechLogger/blob/master/gifs/second.gif)

### How to run

I cannot compile it now because of [problems with soundcard](https://github.com/bastibe/SoundCard/issues/92), but u can run it by Python:

1. Download Python from [official site](https://www.python.org/downloads/) (choose correct operation system)

1. Open **cmd.exe** 

1. Install necessary packages via commands:

```
pip install numpy
pip install scipy
pip install textblob
pip install pyaudio
pip install soundcard==0.3.3
pip install speechrecognition
pip install termcolor
pip install colorama
```

4. download and run [this file](https://github.com/PasaOpasen/SpeechLogger/releases/download/0.2.0/text_logger3.py)

### Notes
* if u have some problems with installing pyaudio, try to get solutions [here](https://stackoverflow.com/questions/52283840/i-cant-install-pyaudio-on-windows-how-to-solve-error-microsoft-visual-c-14)

## Third result

What's new:

* **json** files with basic settings and supported languages
* trancription (grapheme to phoneme) by [epitran](https://github.com/dmort27/epitran)

TODO firstly:

* transcript persian words better

https://github.com/PasaOpasen/SpeechLogger/blob/master/gifs/third.gif

### How to use

1. also install **epitran** by command (**cmd.exe**):
```
pip install epitran
```
2. download [release](https://github.com/PasaOpasen/SpeechLogger/releases/tag/0.2.1)

3. unpuck and run **.py** file

