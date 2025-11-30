import requests
import csv
import google.generativeai as genai
import asyncio
import json

ids=[]
async def call_model(model, final_prompt):
    response = await model.generate_content_async(final_prompt)
    return response.text

async def main(prompt,list_of_ids):
    tasks = []
    for item in list_of_ids:
        title, id= item
        final_prompt = prompt + str(title)
        task = asyncio.create_task(call_model(model, final_prompt))
        tasks.append(task)
        ids.append(id)

    # Wait for all tasks to finish
    results = await asyncio.gather(*tasks)
    return list(results)

    # Print the results
    # for i,result in enumerate(results):
    #     print(i+1,result,sep=',')

# api_key_1 = "AIzaSyDg2WVbmsbwgtm0NkVCVHzM5OjrCu4PZNU"
# api_key_2 = 'AIzaSyAc0uSTfoejhGScUzbUb1xxB2DtHyOwi94'
api_key_2 = "AIzaSyDJsAXZNhgIvGFk9P93msy2cl6xGO5sJ6I"
genai.configure(api_key=api_key_2)
model = genai.GenerativeModel('gemini-pro')

# csv_file_path_1 = r"videos_titles.csv"
# list_of_ids = []
# with open(csv_file_path_1, 'r',encoding="utf-8",newline='') as csvfile:
#     csv_reader = list(csv.reader(csvfile))
#     for item in csv_reader:
#         list_of_ids.append([item[0],item[1]])

with open('final_captions.json','r') as f:
    data = json.load(f)

# fin_json= {}

# for item in data:
#     for id in item:
#         fin_json[id]=item[id]

# print(fin_json)
prompt = "Given a list of captions containing actions and potentially unidentified elements, generate a single, grammatically correct caption that combines the information coherently. Here are some guidelines: 1. Replace uppercase letters with 'person'. Eg: 'C walks' should be changed to 'a person walks'. Do not include references or notations in the final prompt at any cost 2. If the caption containins '#unsure', predict the missing information based on context from previous or the next captions. Eg: ['A person has a ball','He plays with '#unsure'']. Here, the person is most likely playing with the 'ball'. Hence, replace it with 'ball'.  But, if '#unsure' comes in the end of a caption, remove it from the caption and dont include in final prompt. 3. Combine the captions while maintaining chronological order and avoiding redundancy and ensure the final caption is grammatically correct and well-structured. 4. In case you notice 2 captions contradicting each other and are causing redundancy, consider the first one out of those 2 captions and ignore the second one from the final prompt. Example input: [ 'Person A scans surroundings, adjusts camera.', 'Person B shakes hands with #unsure in a room while looking around', 'Person walks around the room.' ]. Example output: A person scans their surroundings and adjusts a camera on their head. They then greet another person with a handshake while oking around the room. A third person walks around the room. Explanation: Explanation: 'another person' in caption 2 is likely the person from caption 1 based on context. So, we replaced '#unsure' with 'another person'. I repeat, pay a lot of attention to all the guidelines mentioned above. Your final prompt MUST NOT contain and upper-case alphabet notations or '#unsure'.Here is the list of captions: "

for item in data[10:20]:
    caption=[]
    for id in item:
        caption=item[id]
    
    final_prompt = prompt + str(caption)
    response = model.generate_content(final_prompt)
    print(response.text)






# prompt = "Given a list of captions containing actions and potentially unidentified elements, generate a single, grammatically correct caption that combines the information coherently. Here are some guidelines: 1. Replace uppercase letters with 'person'. Eg: 'C walks' should be changed to 'a person walks'. Do not include references or notations in the final prompt at any cost 2. If the caption containins '#unsure', predict the missing information based on context from previous or the next captions. Eg: ['A person has a ball','He plays with '#unsure'']. Here, the person is most likely playing with the 'ball'. Hence, replace it with 'ball'.  But, if '#unsure' comes in the end of a caption, remove it from the caption and dont include in final prompt. 3. Combine the captions while maintaining chronological order and avoiding redundancy and ensure the final caption is grammatically correct and well-structured. 4. In case you notice 2 captions contradicting each other and are causing redundancy, consider the first one out of those 2 captions and ignore the second one from the final prompt. Example input: [ 'Person A scans surroundings, adjusts camera.', 'Person B shakes hands with #unsure in a room while looking around', 'Person walks around the room.' ]. Example output: A person scans their surroundings and adjusts a camera on their head. They then greet another person with a handshake while oking around the room. A third person walks around the room. Explanation: Explanation: 'another person' in caption 2 is likely the person from caption 1 based on context. So, we replaced '#unsure' with 'another person'. I repeat, pay a lot of attention to all the guidelines mentioned above. Your final prompt MUST NOT contain and upper-case alphabet notations or '#unsure'.Here is the list of captions: "
# res = data["002ad105-bd9a-4858-953e-54e88dc7587e"]
# final_prompt = prompt + str(res)
# response = model.generate_content(final_prompt)
# print(response.text)
# for item in list_of_ids:
#     title,id = item
#     final_prompt = prompt + str(title)
#     response = model.generate_content(final_prompt)
#     print(response.text)
# results = asyncio.run(main(prompt,list_of_ids))
# csv_file_path_2 = r"surely_final_dataset.csv"

# with open(csv_file_path_2, 'w',encoding="utf-8", newline='') as csvfile:
#     csv_writer = csv.writer(csvfile)
#     for id,task in zip(ids,results):
#         if task.upper()=="YES":
#             csv_writer.writerow([id])

# for i,res in enumerate(results):
#     print(i+1,res,sep=',')







