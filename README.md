# Pod
Pod is a complex Python code that integrates several APIs to analyze images or videos and extract information about what's happening in the scene. The code uses the Azure Cognitive Services Computer Vision API, the Google Cloud Storage API, the Google Cloud Speech-to-Text API, and the OpenAI API.

## Getting Started

So before we get started, Let's see how this script works.The script first uploads the media file to Google Cloud Storage, then calls the Azure Computer Vision API to analyze the media file and extracts relevant information such as categories, tags, description, and objects. The script then uses OpenAI to generate a spoken response based on the analysis results. The spoken response is then transcribed to text using the Google Cloud Speech-to-Text API and printed to the console.

To use this code, you will need to replace the placeholders for the API keys and other parameters with your own values. You will also need to install the required Python packages listed in the [requirements.txt](https://github.com/clintonimaroo/Pod/blob/main/requirements.txt) file.


## Prerequisites to run the website locally:

- [conda](https://www.anaconda.com/)
- [pip](https://www.geeksforgeeks.org/how-to-install-pip-on-windows/)

## API keys to add to your placeholders:

- [conda](https://beta.openai.com/examples/default-openai-api/)
- [azure computer version](https://azure.microsoft.com/en-us/products/cognitive-services/vision-services)
- [Text to speech](https://azure.microsoft.com/en-us/products/cognitive-services/text-to-speech/)

