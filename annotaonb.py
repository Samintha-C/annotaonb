from openai import OpenAI

def recipient_groups(gratitude_note):
    client = OpenAI(api_key='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')

    prompt_message_system = "The following is a message written by someone for something they are grateful for. Provide a natural sentences, in a non listed manner describing a few unsung heroes/groups that contribute to what they were grateful for, and how they do so. (JSON object)"
    prompt_message_user = f"I'm grateful for {gratitude_note}. Identify the unsung heroes or groups behind this"

    response = client.chat.completions.create(
        model="gpt-3.5-turbo-1106",
        response_format={"type": "json_object"},
        messages=[
            {"role": "system", "content": prompt_message_system},
            {"role": "user", "content": prompt_message_user}
        ]
    )

    return response.choices[0].message.content
#replace text for needed graditude text
gratitude_text = "The environment in Santa Cruz is wonderful. The tourist attractions are clean, and the facilities in Santa Cruz are easily accessible. I used to release by stress by walking along the sea-side and walking in University of California, Santa Cruz."
print(recipient_groups(gratitude_text))