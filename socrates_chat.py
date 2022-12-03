import openai
speaker = 'ANDREW TATE'
person = 'TRISTAN'
def open_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as infile:
        return infile.read()

openai.api_key = open_file('.apikey')


def gpt3_completion(prompt, engine='text-davinci-003', temp=0.9, top_p=1.0, tokens=300, freq_pen=0.5, pres_pen=0.5, stop=[f'{speaker}:', f'{person}:']):
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
    conversation = list()
    while True:
        user_input = input(f'{person}: ')
        conversation.append(f'{person}: %s' % user_input)
        text_block = '\n'.join(conversation)
        prompt = open_file('socrates_prompt.txt').replace('<<BLOCK>>', text_block)
        prompt = prompt + f'\n{speaker}:'
        response = gpt3_completion(prompt)
        print(f'{speaker}:', response)
        conversation.append(f'{speaker}: %s' % response)
