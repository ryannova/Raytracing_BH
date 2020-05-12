# Black Hole Ray Tracing

![equation](https://github.com/ryannova/Raytracing_BH/blob/master/docImages/out_long_repeat.gif?raw=true)

This black hole ray tracer is used to demonstrate the distortion of light from warping of spacetime due to the gravity of black holes.

This is written onto a python notebook, which allows for flexibility and ease of use. The notebook shows the process in which I took in writing up the black hole ray tracer. First to start a basic ray tracing model is created through tracing light rays backwards from the perspective of the observer. This greatly decreases the number of rays. Afterwards, three steps were taken. First was simply rendering an opaque sphere with the correct size, then a model using a thin convex lens, and finally bending of light rays due to spacetime distortions. This program simply renders a Schwarzschild Black Hole, which assumes the black hole has no spin, zero magnetic field, or any charge, and is only characterized by its mass. Finally, note that the current convention is that masses of the black hole are in units of solar masses and the units of distance are solar radii.

## Basic Ray Tracer Model

Most ray tracers are usually written in C/C++ due to their dependence on performance, however unlike traditional ray tracers we will not be worrying about objects which are reflective, diffuse, or refractive. This means that python would suffice as it is fast enough for the given task. Here in our model we will only have 4 objects that we are going to worry about, the location of the observer, the image, the black hole, and the sky. 

The similar to traditional ray tracers we are going to have the observer look towards the negative z axis, so normally the observer will have a positive z value looking at the negative z direction. After the observer, we have our image. The image is a plane where we will construct ray originating from the observer to the image plane. Each point corresponds to 1 pixel. Currently, the pixels are equivalent to 1 unit on the grid but a future iteration will allow for higher resolution, in which one unit would be subdivided into multiple pixels.
![Image showing how rays are generated(courtesy of UC Berkeley CS184)](https://github.com/ryannova/Raytracing_BH/blob/master/docImages/ObserverRays.jpeg?raw=true)
Image showing how rays are generated(courtesy of UC Berkeley CS184)

The main object in focus is going to be the black hole. It will be located after the image plane and before the sky plane. Now note that it is important the black hole be located here or not the program will not work as it checks to see if there is any intersects with the black hole first before checking the sky plane.

Finally, we have the sky plane which is an image provided by the user such we are able to see the distortions from the black hole. The sky plane has a normal vector pointing in the z direction and is located behind the black hole. We can make this image larger or smaller by changing its location as long it lies after the black hole. In addition, distorted rays and rays which aren't influenced by the black hole will check to see if it intersects the sky plane. If it doesn't then it returns a default black. It is important to note that we are simply looking to see if it intersects a plane so to simulate parallel light rays coming to the black hole, you would actually move the sky plane closer rather than farther. This will be discussed in more detail in a later section.

## Black hole Render 
There were three steps taken to render the black hole. First we had to ensure that the ray tracing model works correctly as indented and this a simple opaque sphere was created as a test case. This can be seen in the first cell of the main code section of the notebook. Here we want to demonstrate that the rays are accurrately rendering the black hole. The next render was done using a thin lens model in which light approaching the black hole would be refracted and then refracted again once it leaves the black hole. Now a normal black hole wouldn't allow users to be able to see the center of the black hole but for this test case there are two modes which allows for a ring which is similar to how black hole distort light rays and a true lens where the center can be seen. Finally, the last render is one which creates as accurate of a image as possible using the curvature of spacetime.

## Implementation
Here we are going to describe in greater detail about implementation of each of the components for the ray tracing such that if someone wishes to create their own this can be used as a guidance on how to create such a program.

### Rays and Observer
I won't go into too muny details on certain aspects of basic ray tracing. You can read up more on this in papers and documents regarding how ray tracing works. For our implementation, rays coordinates are described as 3D vectors. A ray can be defined by its origin and a directional vector, such that any point on a ray can be defined as ray = origin + direction * t. Usually t is referred to as time but in a basic calculation we can use t simply to traverse the ray in any direction. As for the sphere, note that most sphere are defined by an equation such as x^2 + y^2 + z^2 = radius but since we are only interested about intersections on the surface we can see that we can define as sphere as (p-c)^2 - R^2 = 0, where p is some surface point, c is the center of the sphere, and R is the radius. To find whether a ray intersects with a sphere we can first assume that we have a ray that intersects with our sphere. With this assumption we are able to substitute our ray equation for p, and solve for t where we get 
![equation](https://github.com/ryannova/Raytracing_BH/blob/master/docImages/sphere_intersect.png?raw=true)
where 
![equation](https://github.com/ryannova/Raytracing_BH/blob/master/docImages/sphere_var.png?raw=true)

Using this equation, all real solutions will represent an intersection of the ray with the sphere. Note that we have three cases where we have 0, 1, or 2 intersection points. In the interest of increasing performance we can see that instead of computing t for all rays we simply need the values under the square root. Note that if b^2 \< 4ac there are 0 intersects, b^2 = 4ac there is 1 intersect, and b^2 \> 4ac there are 2 intersects. We can check this condition before proceeding and if there isn't any intersect we can immediately look at any intersections with the sky plane. To find interactions with the sky plane is relatively straight forward. Here we can see that we only need the plane's normal vector and a point on the plane to define a plane, such that (p^2 - p'^2) dot N = 0, where p is the intersection point from the ray, p' is a separate point on the plane, and N is the normal vector. Once again we can plug in our ray equation and solve for t, and we can see that we have

![equation](https://github.com/ryannova/Raytracing_BH/blob/master/docImages/plane_intersect.png?raw=true)

Finally, since we are only have a fixed size for our sky plane we can simply check to see if the intersection with the plane lies within the coordinates of the sky plane and if it doesn't we set the pixel to be black.

### Black hole Size Determination
Note that a size of a black hole can simply be determined by its mass solely since we are assuming that the object has collapsed past its Schwarzschild radius (Rs = 2GM/c^2). Now it would naive to assume that we are simply going to render the black hole by is Schwarzschild radius as photons that get very close to the black hole is going to be essentially captured by the black hole and these photons will continue in a stable or decaying orbit into the black hole. To save on computation, instead of computing the orbits as we know that they these photons will not escape to reach the observer, we are able to just say that at these distances no photons will escape. Consequently, this is described to be the photon sphere(Rp = 3GM/c^2) which is 3/2 times the Scwarzschild radius for non-rotating black holes, and we use this as the radius for our black hole. This means that the dark circle we see in the simulation is not the Schwarzschild radius but is photon sphere. Something that should be noted is that in many of these calculations the Schwarzschild radius or some factor of it will be within our calcaluation so it is recommended that this values is computed and saved to reduce computations.

### Lensing
Given that we have a bound for the size of the black hole we need to know where it will be distorting the light that we see coming in. Now note that in actuality we would light distortion gradually get weaker and weaker until it is not noticeable, however if we are to apply this effect to all light rays it would create too large of a toll on the computation and thus causing the program to run between 3 to 10x slower. Given that the program already takes about 30mins to render a long animation this would cause it to run between 1.5-5hrs. Now it is important to note that it is okay to give this distortion a hard bound because this distortion is caused by the gravitational pull of the black hole. Since the force of gravity is proportional to 1/R^2 we can see that it drops down very quickly.  As such to decrease the number of computations needed, we can look at how gravitaional lensing is causes an effect which creates a ring around the black hole. This ring is called an Einstein ring which has an angular size of 

![equation](https://github.com/ryannova/Raytracing_BH/blob/master/docImages/angularSize.png?raw=true)

This can be derived by looking at how the light is deflected based on the ratios between the source plane, black hole plane, and observer plane as described in the diagram below

![equation](https://github.com/ryannova/Raytracing_BH/blob/master/docImages/angularSizeDiagram.png?raw=true)

where the deflection angle alpha is defined as 

![equation](https://github.com/ryannova/Raytracing_BH/blob/master/docImages/deflectionAngle.png?raw=true)

Using this we are able to create the size of the ring that we will be seeing and as such we have the size of the ring we will be observing. Finally, to create the lensing effect we are able to simply redirect the ray once it has reach the lensing plane, which is located at where the black hole is. By using the same plane equation we are able to determine where it intersects this plane. There can simply reflect it at the same angle of incident. This is true because assuming that all the light rays we are back tracing converge at the observer then the focal point is the location of the observer for all the light rays that are coming from the black hole and as such we are able to see redirect it at the same angle. To accomplish this a new ray is created with its origin at the lens plane then the direction would be equal to direction of the redirected ray. This will give us a lensing effect as shown in the following image.

![equation](https://github.com/ryannova/Raytracing_BH/blob/master/Output/lensing_true.png?raw=true)

Now we are also able to see what this lensing effect with the black hole there. This would simply be using the same intersection code that we had from the previous part if we see that the ray intersects a portion of the black hole itself, as seen below.

![equation](https://github.com/ryannova/Raytracing_BH/blob/master/Output/lensing.png?raw=true)

### Spacetime Curvature

Finally, we have all the necessary background code to create a realistic image of black hole lensing by looking at how much light bends from the curvature of spacetime due to gravity. As stated before we can see the incident light ray will be deflected by alpha as defined above. Then here we are able to compute the deflection angle for each individual ray. From this we are able to get an accurate representation of how rays are distorted by the black hole. Now note that we are going to be only doing this for the area enclosed by the angular size that is computed, as this is to help with computation. Now unlike previously we are able to create the directional ray of the same angle we have different angles for different rays. Looking at a 2D circle we can see that the incident ray would be coming with some impact parameter b. Then the angle deflected would be alpha given above. Now here what we can do is that we know the angle is going to be deflected along the plane where is it defined by the vector of the incoming ray and the vector pointing from the center of the circle to the point of deflection. The normal vector for this plane is the cross product of these two vectors. However instead of computing the cross product we can simply see that the direction of this new ray is given by cos(alpha) * ray - sin(alpha) * radial\_vector. You can see this in the diagram below

![Diagram](https://github.com/ryannova/Raytracing_BH/blob/master/docImages/impact_diagram.jpg?raw=true)

Note that this equation is only true when both directional ray vector and the radial vector both have unit length, so be sure they are both unit vectors. Also here we make the assumption that the radial vector is defined as the center point to the point of impact, but if you define it the other way around such that the vector is from the point of impact to the center point then we would add sin(alpha) * radial\_vector instead. This is a very important point to note because you will get 2 different results due to this sign error. You can see the difference in the two gif below. The first shows when you use the wrong sign and the second one is the actual result that you should get.

![equation](https://github.com/ryannova/Raytracing_BH/blob/master/docImages/out_long_repeat_sign_error.gif?raw=true)

![equation](https://github.com/ryannova/Raytracing_BH/blob/master/docImages/out_long_repeat.gif?raw=true)

This approach of having different angles at which they are deflected is similar to how spacetime is warped. Some effects that we don't see is the bright ring that we would expect to see around the photon sphere. This is due to the fact that photons close to the photon sphere, though they escape it does take a longer time than photons which are farther apart. This means that it will cause photons to collect and this might this brighter ring around the photon sphere that is not seen in this simulation. These difference will be address in the future goals for this project.

### Creating Animation
Finally to create the nice gif animations we simply need to do the same thing as we have done for one image but along multiple different points. Currently, the program has a parameter called BHrange which causes the black hole to move from -BHrange to BHrange along the x-axis and samples at every integer value. However the black hole can be moved to any location and sampled at any rate. Due to high computation time it is recommended to render all the images and use those sets of images to create the animation so that it is much smoother since 301x301 images take about 15-30 seconds to render. For longer animations such as the one shown at the top has 200 frames which would take approximately 50min to 1hr 40min depending on the speed of your computer. Note that currently all renders are done on the CPU, and on one thread which makes this program CPU heavy.

## Future Goals



