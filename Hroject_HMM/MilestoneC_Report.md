# HMM on Weather Prediction

## Group Member:

Ziyuan Wang (wangzi@uw.edu)

Ye Jin (yjin2@uw.edu)

## Program Description:

The main purpose for this program is to determine the weather (Rainy, Cloudy or Sunny day) by observing the previous days' temperature, humidity and Pressure.

## Brief Description on  our Technique:

### Data Collection:

Collect weather data of Seattle from the website, <https://www.wunderground.com/>, including the date, temperature, humidity, pressure and weather.

### Data Process:

Firstly,  the transition probability matrix and emission probabilities are defined by our experience. The place we chose is Seattle, so the probability of rainy days should be much greater than the cloudy and sunny days. 

Secondly, since our intuition was not that accurate, we decided to get the  transition probability matrix and emission probabilities by process the data we have. 

For the transition probability matrix, because we had the today's weather and next day's weather, the times of each transition states can be calculated and then divided the times of the condition state. In this way, we can get the Transition probability.

For example, firstly, the 'Rainy|Rainy', 'Cloudy|Rainy' and 'Sunny|Rainy' states appear 3, 4, 3 times each. 'x|y' means today's weather is 'y' and next day's weather is 'x'. The total times of Rainy days is $3+4+3=10$. Therefore, $P(Rainy|Rainy) = 3/10 = 0.3$. By this way, the transition probability matrix can be calculated.

For the emission probability, we firstly set a threshold to determine the three level of the temperature, humidity and pressure. 

For temperature:
$$
1:\begin{bmatrix}
-\infty& 50.0
\end{bmatrix}\ \ \ 
2: \begin{bmatrix}
50.0& 68.0
\end{bmatrix}\ \ \ 
3: \begin{bmatrix}
68.0& +\infty
\end{bmatrix}
$$
For humidity:
$$
1:\begin{bmatrix}
-\infty& 39.0
\end{bmatrix}\ \ \ 
2: \begin{bmatrix}
39.0& 66.0
\end{bmatrix}\ \ \ 
3: \begin{bmatrix}
66.0& +\infty
\end{bmatrix}
$$
For pressure:
$$
1:\begin{bmatrix}
-\infty& 29.3
\end{bmatrix}\ \ \ 
2: \begin{bmatrix}
29.3& 29.9
\end{bmatrix}\ \ \ 
3: \begin{bmatrix}
29.9& +\infty
\end{bmatrix}
$$
By this way, the temperature, humidity and pressure are divided into three level separately. And then, the emission probabilities can be calculated by getting the times of the level 1, 2 or 3 under certain state and then dividing the times of that state.

For example, when the weather is rainy day, for the temperature, there are 4 times on level 1, 3 times on level 2, and 3 times on level 3. The total times of rainy days is 10. Therefore, $P(1|Rainy) = 4/10 = 0.4$. $P(1|Rainy)$ means when the weather is Rainy, the probability of level 1 temperature. Because we only considered one observed state, temperature, humidity or pressure, we did not define a character to represent them.

### MMH Algorithm:

The Forward Algorithm and Viterbi Algorithm are all achieved in this project.

The reference we read provided the pseudo code for these two algorithm.

The Forward Algorithm:

![](C:\Users\PrinceYuan\OneDrive\Courses\SPRING 2019\CSE415\project\Foward.png)

The Viterbi Algorithm:

![](C:\Users\PrinceYuan\OneDrive\Courses\SPRING 2019\CSE415\project\Viterbi.png)

We programed these complex function and equation by matrix, so the code would be simple and be easy to understand.

<div STYLE="page-break-after: always;"></div>

## Screen Shot of Results

For statistical data,

![](C:\Users\PrinceYuan\OneDrive\Courses\SPRING 2019\CSE415\project\pic\s_temp_s.png)

![](C:\Users\PrinceYuan\OneDrive\Courses\SPRING 2019\CSE415\project\pic\s_temp.png)

![](C:\Users\PrinceYuan\OneDrive\Courses\SPRING 2019\CSE415\project\pic\s_hum_s.png)

![](C:\Users\PrinceYuan\OneDrive\Courses\SPRING 2019\CSE415\project\pic\s_hum.png)

![](C:\Users\PrinceYuan\OneDrive\Courses\SPRING 2019\CSE415\project\pic\s_press_s.png)

![](C:\Users\PrinceYuan\OneDrive\Courses\SPRING 2019\CSE415\project\pic\s_press.png)

For customized data,

![](C:\Users\PrinceYuan\OneDrive\Courses\SPRING 2019\CSE415\project\pic\c_temp_s.png)

![](C:\Users\PrinceYuan\OneDrive\Courses\SPRING 2019\CSE415\project\pic\c_temp.png)

![](C:\Users\PrinceYuan\OneDrive\Courses\SPRING 2019\CSE415\project\pic\c_hum_s.png)

![](C:\Users\PrinceYuan\OneDrive\Courses\SPRING 2019\CSE415\project\pic\c_hum.png)

![](C:\Users\PrinceYuan\OneDrive\Courses\SPRING 2019\CSE415\project\pic\c_press_s.png)

![](C:\Users\PrinceYuan\OneDrive\Courses\SPRING 2019\CSE415\project\pic\c_press.png)

## Demo Instruction

Type the command below on the Terminal

For customized data,

```
Python main.py --customized
```

For statistical data,

```
Python main.py
```

## Example Code

```python
parser = argparse.ArgumentParser(description='Customized or Statistical Data')
parser.add_argument('--Customized', action='store_true')
args = parser.parse_args()
```

Using the parameters on the command to switch the mode, Customized or Statistical Data.

```python
    fig = plt.figure()
    plt.title('Temperature')
    plt.plot(timeDomain, Predict_State_Code, label='Predicted weather by Viterbi Algorithm')
    plt.plot(timeDomain, DATA.Code_realweather, label='Real Weather')
    plt.xlabel('Day')
    plt.ylabel('0: Rainy 1: Cloudy 2: Sunny')
    plt.legend()
```

Using the plot to show the result and compare with the real weather.

## Learning in Project

Ziyuan Wang: 

1. Learn how to program as a team.
2. Better understand the HMM.
3. Learn how to design a project and achieve the goal.

Ye Jin:

	1. Learn the application of HMM.
 	2. Learn how to program as a team.

## Future Design

1. Collect more accurate data.
2. Find a way to combine the three observation together to predict the weather.
3. For now, we just showed the result by plot (0: Rainy, 1: Cloudy, 2: Sunny). It is not that straightforward. Therefore, we are wondering if there is a better way to show it.
4. Design a GUI for this program.

## Reference

Weather data: <https://www.wunderground.com/>

Algorithm reference: <https://web.stanford.edu/~jurafsky/slp3/A.pdf>

## Partners' Reflections

Ziyuan Wang:

In this team, I was responsible for most of the coding work including the Forward algorithm, Viterbi Algorithm and Data Processing. During this experience, I found coding together is not simple, because it is hard to read and understand other’s code. What we did was expressing our thought while coding, so it is easier to understand what the code means and follow the progress of developing the program. In this project, I am better understand how to do the project as a team and how to design a complete project.

Ye Jin:

In this team, I was responsible for part of coding work. Including the initial possibility setting and frame of the program, and collecting data from the internet. During this process, I found that, although large amount of data was on the Internet, it still needs to set a standard to collect the useful data. Also, I got more experience in teamwork of coding.