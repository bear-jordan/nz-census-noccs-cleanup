# NOCC Estimate Tool

The NOCC Estimate Tool is a command-line tool for estimating whether or not the number of occupants in a residential dwelling needs to be changed. The tool takes as input a CSV file containing responses from a survey and produces as output a sorted list of responses ranked by the estimated level of confidence that they represent a change in the number of occupants.

## Requirements

- Python 3.6 or later
- pandas
- scikit-learn

## Installation

- Clone the repository: git clone https://github.com/example/nocc-estimate-tool.git
- Navigate to the repository directory: cd nocc-estimate-tool
- Install the required Python packages: pip install -r requirements.txt


## Usage

To use the NOCC Estimate Tool, follow these steps:

- Copy the CSV file containing the survey responses to the data/external directory.
- Open a terminal window and navigate to the nocc-estimate-tool directory.
- Run the command python main.py data_file.csv, where data_file.csv is the name of the CSV file containing the survey responses.
- The tool will classify the responses as high, medium, or low confidence, based on the contents of the Notes and Notes2 columns. It will then apply a logistic regression model to the cleaned text data to predict the level of confidence for each response.
- The tool will sort the responses by confidence level and print the results to the console. Optionally, it will also save the results to a CSV file in the data/processed directory.


## Example
Suppose we have a CSV file named survey_responses.csv containing the following responses:

Response Number	Notes	Notes2
1	Confirmed with Joe that there are 2 people	
2	Two occupants confirmed	
3	One confirmed	Not sure about this

We can use the NOCC Estimate Tool to estimate the level of confidence that each response represents a change in the number of occupants as follows:

```$ python main.py survey_responses.csv```

   Response Number                                   Notes  \
0                1  Confirmed with Joe that there are 2 people   
1                2                    Two occupants confirmed   
2                3                                One confirmed   

             Notes2 CONFIDENCE  
0                      High  
1                      High  
2  Not sure about this    Medium 
 
In this example, the tool has classified the first two responses as high confidence and the third response as medium confidence, based on the contents of the Notes and Notes2 columns. It has then used a logistic regression model to predict the level of confidence for each response, resulting in the sorted output shown above.