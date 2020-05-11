# Blackhole Ray Tracing

This blackhole ray tracer is used to demonstrate the distortion of light from warping of spacetime due to the gravity of blackholes.

This is written onto a python notebook, which allows for flexibility and ease of use. The notebook shows the process in which I took in writting up the blackhole ray tracer. First to start a basic ray tracing model is created through tracing light rays backwards from the persepctive of the observer. This greatly decreases the number of rays. Afterwards, three steps were taken. First was simply rendering an opaque sphere with the correct size, then a model using a thin convex lens, and finally bending of light rays due to spacetime distortions. This program simply renders a Schwarzschild Black Hole, which assumes the blackhole has no spin, zero magnetic field, or any charge, and is only characterized by its mass.

## Basic Ray Tracer Model

Most ray tracers are usually written in C/C++ due to their dependence on performance, however unlike traditional ray tracers we will not be worrying about objects which are reflective, diffuse, or refractive. This means that python would suffice as it is fast enough for the given task. Here in our model we will only have 4 objects that we are going to worry about, the location of the observer, the image, the blackhole, and the sky. 

The similar to traditional ray tracers we are going to have the observer look towards the negative z axis, so normally the observer will have a positive z value lookin at the negative z direction. After the observer we have our image. The image is a plane at which 

![image](https://github.com/ryannova/Raytracing_BH/blob/master/Output/1001x1001.png?raw=true)
