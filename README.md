This project summarizes the research work done on the topic of Diffusion of Innovation that contributes to understanding new product adoption. The background of diffusion research and it's effect on social structure and communication. The diffusion model has aided our understandings of the consumption of new products.

We built a model of a population of individuals exposed to a new concept Individuals decide to adopt, then later discard, the innovation. We can use a 3-cell compartment model: potential, adopters, disposers
* Set parameters for total population size N
* parameter for adoption rate beta
*  parameter for disposal rate gamma
* set parameter for maximum time range max\_time
*  data recording the population dynamics over time


The foundational classes
for our model are
  * Population to model a group of Persons
  * Person to model the individuals

We'll iterate from 0 to N-1 create a new Person with a pid. Then we'll initialize with approximately beta*N adopters and the rest will be considered potentials. We keep track of the individual Persons by putting
them in the person\_list

We'll iterate from 0 to N-1,if the i-th Person is a Potential.Then we simulate via chance that they switch to become an adopter or disposer. We can take the Person and
Population class and put it into a Python "package" file called 'Diffusion.py'.
We imported the library  matplotlib for plots and our Diffusion package for Population class. We create a DOI\_Model class to manage the model,\_\_init\_\_ sets up our history lists, model, parameters, and initial Population object. The model iterates over the time span at each time step, it counts and saves the number of potentials, adopters, and disposers to be modeled.



We will be using iPad sales data in order to back our research. The diffusion of iPad is used to study the trend of how new innovations are adopted and later disposed and there sustainability in the society.


![p43](https://user-images.githubusercontent.com/98371832/176995186-d8dafe43-cd67-430d-b5f4-6d015f50653c.png)



![P44](https://user-images.githubusercontent.com/98371832/176995196-9e137f98-b003-43c4-8736-7e0bb1ba0ea2.png)




