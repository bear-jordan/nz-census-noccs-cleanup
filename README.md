# NOCC Estimate Tool

The NOCC Estimate Tool is a command-line tool for estimating whether or not the number of occupants in a residential dwelling needs to be changed. The tool takes as input a CSV file containing responses from a survey and produces as output a sorted list of responses ranked by the estimated level of confidence that they represent a change in the number of occupants.

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

## Configuration
The NOCC Estimate Tool is configured using a set of regular expressions defined in the modules/config.py file. These regular expressions are used to match against the contents of the Notes and Notes2 columns in the input CSV file, and identify high confidence labels that are indicative of changes in the number of occupants.

The regular expressions can be modified or expanded as needed to suit different use cases. Additional configuration options can also be added to the modules/config.py file as needed.

## Limitations
The NOCC Estimate Tool is designed to work with survey responses that contain text data in the Notes and Notes2 columns. It may not be effective for other types of data, or for surveys that do not contain relevant text data.

The tool is also limited by the accuracy and completeness of the regular expressions used to identify high confidence labels. While these regular expressions are designed to capture common phrases and patterns that are indicative of changes in the number of occupants, they may not be effective for all use cases.

## Conclusion
The NOCC Estimate Tool is a powerful and efficient tool for estimating changes in the number of occupants in residential dwellings based on survey responses. Its use of natural language processing, machine learning, and regular expressions makes it highly accurate and reliable, while its command-line interface and support for standard CSV file formats make it easy to use and integrate into existing workflows.
