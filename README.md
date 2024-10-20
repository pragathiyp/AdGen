## ADGen: A Multimodal Advertisement Generation Dataset and Video Captioning Framework

We have introduced ADGen, a Text-Image-Video dataset, that comprises 720 variable-length videos totaling 24 hours, along with corresponding images, and text captions across 15 categories, including Entertainment, Education, and Sports. 

## Download

You can download the dataset from the below link:

https://drive.google.com/drive/folders/1-5DFlWAtRaZAwFY6aHcVmIuf7YX0OOGh?usp=drive_link

## Directory Structure

The dataset is organized as follows:

    dataset/
    ├── Text_Captions.json
    ├── videos/
    │   ├── 00000001.mp4
    │   ├── 00000002.mp4
    │   ├── 00000003.mp4
    │   └── ...
    └── images/
        ├── 00000001.png
        ├── 00000002.png
        ├── 00000003.png
        └── ...

**Text_Captions.json:** This file contains the text captions corresponding to each video in the dataset. The captions are stored in a JSON object, where the keys are video IDs and the values are the corresponding captions. The structure of the JSON is as follows:

    {
        "00000001": "<corresponding caption for the video>",
        "00000002": "<corresponding caption for the video>",
        ...
    }

**videos/:** This directory contains the video files, where each file is named with a unique 8-digit identifier corresponding to the video ID in the Text_Captions.json file.

**images/:** This directory contains the image files, where each file is named with the same 8-digit identifier as the corresponding video.

## Prerequisites

Clone the repository:

    git clone https://github.com/S-Sanjith/AdGen.git

Install the required dependencies using the 'requirements.txt' file provided:

    pip install -r requirements.txt

## Usage Instructions

### Download Videos from YouTube

Use the following command to download specific videos from YouTube based on a CSV file:

    video2dataset --url_list="videos.csv" --url_col="url" --output_folder="test_data"

(Make sure you have a CSV file with the links of all the videos to be downloaded using video2dataset)

### Reorganize the Folder Structure

Run the script to reorganize the folder structure after downloading the videos:

    python ./reorganize_folder.py

### Extract and Save Audio

Download and save the audio of each video using the following script:

    python ./extract_and_save_audio.py

### Extract Relevant Images

Get the 10 relevant images towards the end of each video:

    python ./get_10_images.py

### Process Images, Generate Transcripts, and Get Metadata

Use the following script to select the best image among the 10 images, obtain LLava outputs, generate Whisper transcripts, get video metadata and save all of these data:

    python ./llava_whisper.py

### Generate GPT Summaries:

Generate and save GPT summaries for each video using the video metadata and the outputs from LLava and Whisper:

    python ./generate_gpt_summaries.py

### Structure the Final Dataset

Finally, restructure the folder to organize the final dataset:

    python ./structure_final_dataset.py


## Samples

(To be updated later)

## Curators

AdGen is created by Pragathi Y P, S Swaroop Bharadwaj, Preetham Kolli and S Sanjith.

## Citation

(To be updated later)

## Contact

If you have any questions, feel free to contact Pragathi Y P - pragathiy.cs20@bmsce.ac.in
