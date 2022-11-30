import transformers
import openai


def read_key(file):
    with open(file, 'r', encoding='utf-8') as f:
        return f.read()

openai.api_key = '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'
#print(read_key('.apikey'))
def gpt3_completion(prompt, engine='text-davinci-003', temp=0.7, top_p=1.0, tokens=400, freq_pen=0.0, pres_pen=0.0, stop=['<<END>>']):
    prompt = prompt.encode(encoding='ASCII',errors='ignore').decode()
    response = openai.Completion.create(
        engine=engine,
        prompt=prompt,
        temperature=temp,
        max_tokens=tokens,
        top_p=top_p,
        frequency_penalty=freq_pen,
        presence_penalty=pres_pen,
        stop=stop)
    text = response['choices'][0]['text'].strip()
    return text

if __name__ == '__main__':
    file = open('prompt.txt', 'rt')
    contents = file.read()
    prompt = contents
    response = gpt3_completion(prompt)
    print(response)