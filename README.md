# Blackhole Ray Tracing

This blackhole ray tracer is used to demonstrate the distortion of light from warping of spacetime due to the gravity of blackholes.

This is written onto a python notebook, which allows for flexibility and ease of use. The notebook shows the process in which I took in writting up the blackhole ray tracer. First to start a basic ray tracing model is created through tracing light rays backwards from the persepctive of the observer. This greatly decreases the number of rays. Afterwards, three steps were taken. First was simply rendering an opaque sphere with the correct size, then a model using a thin convex lens, and finally bending of light rays due to spacetime distortions. This program simply renders a Schwarzschild Black Hole, which assumes the blackhole has no spin, zero magnetic field, or any charge, and is only characterized by its mass. Finally note that the current convention is that masses of the blackhole are in units of solar masses and the units of distance are solar radii.

## Basic Ray Tracer Model

Most ray tracers are usually written in C/C++ due to their dependence on performance, however unlike traditional ray tracers we will not be worrying about objects which are reflective, diffuse, or refractive. This means that python would suffice as it is fast enough for the given task. Here in our model we will only have 4 objects that we are going to worry about, the location of the observer, the image, the blackhole, and the sky. 

The similar to traditional ray tracers we are going to have the observer look towards the negative z axis, so normally the observer will have a positive z value lookin at the negative z direction. After the observer we have our image. The image is a plane at we will construct ray originating from the observer to the image plane. Each point corresponds to 1 pixel. Currently the pixels are equivalent to 1 unit on the grid but a future iteration will allow for higher resolution, in which one unit would be subdivided into multiple pixels.
![Image showing how rays are generated(courtesy of UC Berkeley CS184)](https://github.com/ryannova/Raytracing_BH/blob/master/docImages/ObserverRays.jpeg)

The main obeject in focus is going to be the blackhole. It will be located after the image plane and before the sky plane. Now note that it is important the blackhole be located here or not the program will not work as it checks to see if there is any intersects with the blackhole first before checking the sky plane.

Finally we simply have the sky plane which is an image provided by the user such we are able to see the distortions from the blackhole. The sky plane has a normal vector pointing in the z direction and is located behind the blackhole. We can make this image larger or smaller by changing its location as long it lies after the blackhole. In addition distorted rays and rays which aren't influenced by the blackhole will check to see if it intersects the sky plane. If it doesn't then it returns a default black. It is important to note that we are simply looking to see if it intersects a plane so to simulate parallel light rays coming to the blackhole, you would actually move the sky plane closer rather than farther. This will be discuss in more detail in a later section.

## Blackhole Render 

