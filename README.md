# Chatbot
Creating a chatbot that acts like Socrates & a financial guru.

## Setting up Environment
__Linux__
1. create a virtual environment: `python -m venv venv`
2. activate virtual environment: `source venv/bin/activate`
3. install packages: `pip install -r requirements.txt`
4. run scripts!

Deactivate virtual environment with `deactivate`

## OpenAI API key
Use your own api key and store it in a file called `.apikey`

## Fine-tuning GPT-3
There are a few commands that are used when tuning GPT-3
**data preparation**: `openai tools fine_tunes.prepare_data -f <LOCAL_FILE>`

**create fine-tune job**: `openai api fine_tunes.create -t <TRAIN_FILE_ID_OR_PATH> -m <BASE_MODEL>`
*In our case we use 'davinci' for `<BASE_MODEL>`*

**cancel a fine-tune job**: `openai api fine_tunes.cancel -i <YOUR_FINE_TUNE_JOB_ID>`

**list all fine-tunes**: `openai api fine_tunes.list`

**retrieve status of a fine-tune job**: `openai api fine_tunes.get -i <YOUR_FINE_TUNE_JOB_ID>`



## Resources 
[OpenAI fine-tuning documentation](https://beta.openai.com/docs/guides/fine-tuning)

[openai.Completion.create](https://beta.openai.com/docs/api-reference/completions/create)

[GPT Tutorial](https://github.com/daveshap/PythonGPT3Tutorial)