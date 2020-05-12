# Blackhole Ray Tracing

This blackhole ray tracer is used to demonstrate the distortion of light from warping of spacetime due to the gravity of blackholes.

This is written onto a python notebook, which allows for flexibility and ease of use. The notebook shows the process in which I took in writting up the blackhole ray tracer. First to start a basic ray tracing model is created through tracing light rays backwards from the persepctive of the observer. This greatly decreases the number of rays. Afterwards, three steps were taken. First was simply rendering an opaque sphere with the correct size, then a model using a thin convex lens, and finally bending of light rays due to spacetime distortions. This program simply renders a Schwarzschild Black Hole, which assumes the blackhole has no spin, zero magnetic field, or any charge, and is only characterized by its mass. Finally note that the current convention is that masses of the blackhole are in units of solar masses and the units of distance are solar radii.

## Basic Ray Tracer Model

Most ray tracers are usually written in C/C++ due to their dependence on performance, however unlike traditional ray tracers we will not be worrying about objects which are reflective, diffuse, or refractive. This means that python would suffice as it is fast enough for the given task. Here in our model we will only have 4 objects that we are going to worry about, the location of the observer, the image, the blackhole, and the sky. 

The similar to traditional ray tracers we are going to have the observer look towards the negative z axis, so normally the observer will have a positive z value lookin at the negative z direction. After the observer we have our image. The image is a plane at we will construct ray originating from the observer to the image plane. Each point corresponds to 1 pixel. Currently the pixels are equivalent to 1 unit on the grid but a future iteration will allow for higher resolution, in which one unit would be subdivided into multiple pixels.
![Image showing how rays are generated(courtesy of UC Berkeley CS184)](https://github.com/ryannova/Raytracing_BH/blob/master/docImages/ObserverRays.jpeg?raw=true)
Image showing how rays are generated(courtesy of UC Berkeley CS184)

The main obeject in focus is going to be the blackhole. It will be located after the image plane and before the sky plane. Now note that it is important the blackhole be located here or not the program will not work as it checks to see if there is any intersects with the blackhole first before checking the sky plane.

Finally we simply have the sky plane which is an image provided by the user such we are able to see the distortions from the blackhole. The sky plane has a normal vector pointing in the z direction and is located behind the blackhole. We can make this image larger or smaller by changing its location as long it lies after the blackhole. In addition distorted rays and rays which aren't influenced by the blackhole will check to see if it intersects the sky plane. If it doesn't then it returns a default black. It is important to note that we are simply looking to see if it intersects a plane so to simulate parallel light rays coming to the blackhole, you would actually move the sky plane closer rather than farther. This will be discuss in more detail in a later section.

## Blackhole Render 
There were three steps taken to render the blackhole. First we had to ensure that the ray tracing model works correctly as indented and this a simple opaque sphere was created as a test case. This can be seen in the first cell of the main code section of the notebook. Here we want to demonstrate that the rays are acurrately rendering the blackhole. The next render was done using a thin lens model in which light approaching the blackhole would be refracted and then refracted again once it leaves the blackhole. Now a normal blackhole wouldn't allow users to be able to see the center of the blackhole but for this test case there are two modes which allows for a ring which is similar to how blackhole distort light rays and a true lens where the center can be seen. Finally the last render is one which creates as accurate of a image as possible using the curvature of spacetime.

## Implementation
Here we are going to describe in greater detail about implementation of each of the components for the ray tracing such that if someone wishes to create their own this can be used as a guidance on how to create such a program.

### Rays and Observer
I won't go into too much details on certain aspects of basic ray tracing. You can read up more on this in papers and documents regarding how ray tracing works. For our implementation, rays coordinates are descibed as 3D vectors. A ray can be defined by its origin and the a directional vector, such that any point on a ray can be defined as ray = origin + direction * t. Usually t is refered to as time but in a basic calculation we can use t simply to traverse the ray in any direction. As for the sphere, note that most sphere are defined by an equation such as x^2 + y^2 + z^2 = radius but since we are only interested about intersections on the surface we can see that we can define as sphere as (p-c)^2 - R^2 = 0, where p is some surface point, c is the center of the sphere, and R is the radius. To find an whether a ray intersects with a sphere we can first assume that we have a ray that intersects with our sphere. With this assumption we are able to substitute our ray equation for p, and solve for t where we get 
![equation](https://github.com/ryannova/Raytracing_BH/blob/master/docImages/sphere_intersect.png?raw=true)
where 
![equation](https://github.com/ryannova/Raytracing_BH/blob/master/docImages/sphere_var.png?raw=true)

Using this equation, all real solutions will represent an intersection of the ray with the sphere. Note that we have three cases where we have 0, 1, or 2 intersection points. In the interest of increasing performance we can see that instead of computing t for all rays we simply need the values under the square root. Note that if b^2 \< 4ac there are 0 intersects, b^2 = 4ac there is 1 intersect, and b^2 \> 4ac there are 2 intersects. We can check this condition before preceeding and if there isn't any intersect we can immediately look at any intersections with the sky plane. To find interections with the sky plane is realtively straight forward. Here we can see that we only need the plane's normal vector and a point on the plane to define a plane, such that (p^2 - p'^2) dot N = 0, where p is the intersection point from the ray, p' is a separate point on the plane, and N is the normal vector. Once again we can plug in our ray equation and solve for t and we can see that we have

![equation](https://github.com/ryannova/Raytracing_BH/blob/master/docImages/plane_intersect.png?raw=true)

