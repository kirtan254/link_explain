Docs »

OpenCV-Python Tutorials »

Introduction to OpenCV »

Introduction to OpenCV-Python Tutorials

Edit on GitHub

Introduction to OpenCV-Python Tutorials¶

OpenCV¶

OpenCV was started at Intel in 1999 by Gary Bradsky and the first release came out in 2000. Vadim Pisarevsky joined Gary Bradsky to manage Intel’s Russian software OpenCV team. In 2005, OpenCV was used on Stanley, the vehicle who won the 2005 DARPA Grand Challenge. This was a big competition for autonomous vehicles. Later its active development continued under the support of Willow Garage, with Gary Bradsky and Vadim Pisarevsky leading the project. Right now, OpenCV supports a lot of algorithms related to Computer Vision and Machine Learning and it is expanding day-by-day. Computer Vision is about teaching computers to see and understand images, and Machine Learning is about teaching computers to learn from data.

Currently, OpenCV supports a wide variety of programming languages like C++, Python, Java, etc., and is available on different platforms including Windows, Linux, OS X, Android, iOS, etc. Also, interfaces based on CUDA and OpenCL are also under active development for high-speed GPU operations. CUDA and OpenCL are technologies that help run tasks faster on graphics cards.

OpenCV-Python is the Python API of OpenCV. It combines the best qualities of OpenCV C++ API and Python language.

OpenCV-Python

Python is a general-purpose programming language started by Guido van Rossum, which became very popular in a short time mainly because of its simplicity and code readability. It enables the programmer to express their ideas in fewer lines of code without reducing any readability. This means you can write less code and still make it easy to understand.

Compared to other languages like C/C++, Python is slower. But another important feature of Python is that it can be easily extended with C/C++. This feature helps us to write computationally intensive codes in C/C++ and create a Python wrapper for it so that we can use these wrappers as Python modules. This means you can write the heavy, complex parts in C/C++ and then use them in Python as if they were regular Python code. This gives us two advantages: first, our code is as fast as the original C/C++ code (since it is the actual C++ code working in the background) and second, it is very easy to code in Python. This is how OpenCV-Python works, it is a Python wrapper around the original C++ implementation. So, you get the speed of C++ with the ease of Python.

And the support of Numpy makes the task more easier. Numpy is a highly optimized library for numerical operations. It gives a MATLAB-style syntax. MATLAB is a programming platform used for numerical computing. All the OpenCV array structures are converted to-and-from Numpy arrays. So whatever operations you can do in Numpy, you can combine it with OpenCV, which increases number of weapons in your arsenal. This means you can use Numpy's powerful tools alongside OpenCV's features. Besides that, several other libraries like SciPy, Matplotlib which supports Numpy can be used with this. SciPy is used for advanced mathematical functions, and Matplotlib is used for creating static, animated, and interactive visualizations.

So OpenCV-Python is an appropriate tool for fast prototyping of computer vision problems. Prototyping means quickly creating a working model of your idea.

OpenCV-Python Tutorials¶

OpenCV introduces a new set of tutorials which will guide you through various functions available in OpenCV-Python. This guide is mainly focused on OpenCV 3.x version (although most of the tutorials will work with OpenCV 2.x also). OpenCV 3.x and 2.x are different versions of the OpenCV library.

A prior knowledge on Python and Numpy is required before starting because they won’t be covered in this guide. Especially, a good knowledge on Numpy is must to write optimized codes in OpenCV-Python. Numpy is a library in Python that helps with numerical operations, like working with arrays and matrices, which are essential for image processing in OpenCV.

This tutorial has been started by Abid Rahman K. as part of Google Summer of Code 2013 program, under the guidance of Alexander Mordvintsev. Google Summer of Code is a program where students work on open-source projects during the summer.

OpenCV Needs You !!!

Since OpenCV is an open source initiative, all are welcome to make contributions to this library. Open source means anyone can use, modify, and share the software freely. And it is same for this tutorial also.

So, if you find any mistake in this tutorial (whether it be a small spelling mistake or a big error in code or concepts, whatever), feel free to correct it. This means you can help improve the tutorial by fixing errors you come across.

And that will be a good task for freshers who begin to contribute to open source projects. Just fork the OpenCV in GitHub, make necessary corrections and send a pull request to OpenCV. Forking means creating your own copy of the project to work on. A pull request is a way to submit your changes for review. OpenCV developers will check your pull request, give you important feedback and once it passes the approval of the reviewer, it will be merged to OpenCV. Then you become an open source contributor. Similar is the case with other tutorials, documentation, etc.

As new modules are added to OpenCV-Python, this tutorial will have to be expanded. So those who know about a particular algorithm can write up a tutorial which includes a basic theory of the algorithm and a code showing basic usage of the algorithm and submit it to OpenCV. This means if you understand how a specific algorithm works, you can help by writing a guide and example code for others to learn from.

Remember, we together can make this project a great success!

Contributors¶

Below is the list of contributors who submitted tutorials to OpenCV-Python.

Alexander Mordvintsev (GSoC-2013 mentor). GSoC stands for Google Summer of Code, a program that encourages students to work on open source projects.

Abid Rahman K. (GSoC-2013 intern)

Additional Resources¶

Alexander Mordvintsev (GSoC-2013 mentor)

Abid Rahman K. (GSoC-2013 intern)

Additional Resources¶

A Quick guide to Python - A Byte of Python. This is a beginner-friendly book that introduces you to Python programming.

Basic Numpy Tutorials. These tutorials will help you understand Numpy, which is a library for numerical operations in Python.

Numpy Examples List. This is a list of practical examples showing how to use Numpy in different scenarios.

OpenCV Documentation. This is the official documentation for OpenCV, a library used for computer vision tasks.

OpenCV Forum. This is an online community where you can ask questions and share knowledge about OpenCV.

Next Previous

© Copyright 2016, eastWillow. Revision c69bb2a6.

Built with Sphinx using a theme provided by Read the Docs. Sphinx is a tool that generates documentation from reStructuredText files, and Read the Docs is a platform that hosts documentation.