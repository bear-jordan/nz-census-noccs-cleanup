# NOCC Estimate Tool

The NOCC Estimate Tool is a command-line tool for estimating changes in the number of occupants in residential dwellings based on survey responses. It uses natural language processing, machine learning, and regular expressions to classify survey responses as high, medium, or low confidence, and rank them based on their estimated level of confidence.

## Usage
To use the NOCC Estimate Tool, you will need to have Python 3 installed on your system. You can install the necessary Python libraries by running the following command:

```
pip install -r requirements.txt
```

Once you have installed the necessary dependencies, you can run the tool by executing the main.py script with the path to the input CSV file as an argument:

```
python main.py <path_to_input_csv_file>
```

The tool will process the input file, classify each survey response as high, medium, or low confidence, and produce a sorted list of responses ranked by their estimated level of confidence. The results will be printed to the console, and can also be saved to a CSV file by uncommenting the last line of the main() function in main.py.


## Configuration
The NOCC Estimate Tool is configured using a set of regular expressions defined in the modules/config.py file. These regular expressions are used to match against the contents of the Notes and Notes2 columns in the input CSV file, and identify high confidence labels that are indicative of changes in the number of occupants.

The regular expressions can be modified or expanded as needed to suit different use cases. Additional configuration options can also be added to the modules/config.py file as needed.

## Limitations
The NOCC Estimate Tool is designed to work with survey responses that contain text data in the Notes and Notes2 columns. It may not be effective for other types of data, or for surveys that do not contain relevant text data.

The tool is also limited by the accuracy and completeness of the regular expressions used to identify high confidence labels. While these regular expressions are designed to capture common phrases and patterns that are indicative of changes in the number of occupants, they may not be effective for all use cases.

## Conclusion
The NOCC Estimate Tool is a powerful and efficient tool for estimating changes in the number of occupants in residential dwellings based on survey responses. Its use of natural language processing, machine learning, and regular expressions makes it highly accurate and reliable, while its command-line interface and support for standard CSV file formats make it easy to use and integrate into existing workflows.
