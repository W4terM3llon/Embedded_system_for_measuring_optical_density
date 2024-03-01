
# Embeded system for measuring optical density
The goal of this project is to measure the optical density of a solution (in this case solution of yeasts). Based on the optical density it is possible to calculate the growth of the yests over time and perform data analysis.

Presentation of the results of this project can be seen here:
1. Online: https://www.youtube.com/watch?v=bZ1Xkovjmjk
2. In this repository: [Project_presentation.mp4](docs%2FProject_presentation.mp4)

Server presentation: [Server_presentarion_1.MOV](docs%2FServer_presentarion_1.MOV) and [Server_presentarion_2.MOV](docs%2FServer_presentarion_2.MOV)




## Running microcontroller, server and web client

Running the project Requires following steps:
1. Make sure that your microcontroller runs Micropython.
2. Upload `microcontroller` folder to your microcontroller. You can use VS Code extansion "Pymakr" to communicate with microcontroller.
3. Remember to updatye `DataSender.py` class to include:
    1. Name of the network
    2. Password to the network
    3. Url of the server on the network
4. Run `run_app.cmd` to create docker containers with backend and frontend applications.
## FAQ

#### How did the yeast grow?

Like this:

![yeat_growth_chart.png](docs%2Fyeat_growth_chart.png)


