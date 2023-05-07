# OpenAI-Checker

## Introduction
`OpenAI-Checker` is a Python script that checks the billing and usage of an OpenAI API key and determines whether it can access the GPT-4 model.

## Dependencies
- Python 3.6+
- requests module (can be installed via `pip install requests`)
- Can access `api.openai.com`

## Usage
1. Clone or download this repository to your local machine.
2. Install the required dependencies.
3. Add your OpenAI API keys to a file named `apikey.txt`, with each key on a separate line.
4. Run the script by typing `python main.py` in your terminal.

## Output
The script will output the total amount, total usage, remaining amount, and whether the API key can access the GPT-4 model for each key in the `apikey.txt` file.

## Example

```shell
$ python main.py
[*]Total amount: 5.00 USD
[*]Total usage: 0.00 USD
[*]Remaining amount: 5.00 USD
[-]API Key:  sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx cannot access GPT-4
```



## License
This project is licensed under the MIT License - see the LICENSE file for details.




## References

This project includes code that was developed with the assistance of ChatGPT, a language model developed by OpenAI based on the GPT-3.5 architecture. 



The following projects were referenced during the development of this project:

- [openai-billing](https://github.com/ClarenceDan/openai-billing) - [Reference was made to this project for the balance inquiry code]
