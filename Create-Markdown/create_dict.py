import openai   

openai.api_key = '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'

topic = input("Enter a topic: ")

def gpt_fill_md(topic):

    prompt = f"Generate a nested dictionairy of important concepts on the topic of {topic} for my notebook. Output just the dictionairy." +
    
    completion = openai.ChatCompletion.create(
      model="gpt-4", 
      messages=[{"role": "user", "content": prompt}]
    )
    
    content_dict = completion['choices'][0]['message']['content']
    return content_dict
