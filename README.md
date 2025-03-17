# <p style="text-align: center;">**C**ollaborative **A**gentic **T**est Generation (CATGen)</p>

## Summary
Unit test generation using large language models (LLMs) have shown promising results, yet existing methods still face difficulty in terms of scalability, multi-step reasoning, and handling large codebases.  After surveying the achievements and limitations of modern implementations, we decided to research how we can improve them without the expensive costs of fine-tuning, while taking steps towards a fully automated unit test generation process. As a result, we examined the capabilities of multi-agent LLMs that distribute unit test generation workflow. We present CATGen (Collaborative Agentic Test Generation), an automated unit test generation system that leverages multiple LLM agents. Given limited computational resources we used LLaMA 3.1 (8B parameters) and LLaMA Groq for tool usage. Due to these constraints we observed significant challenges, including frequent hallucinations, loss of memory, and ignoring of instructions by the LLMs, which lead to substantial human intervention. Despite these difficulties, CAT-Gen was able to successfully generated executable unit test suites for small code bases that test all functions at least once. While our results were not always desirable, they serve as a proof of concept, demonstrating the feasibility of automated unit test generation using multi-agent LLMs and highlighting areas for future improvement.

## Documentation
Below are the steps on how to deploy CATGen on a local machine. (Note that this project was built in Windows and some commands will differ for Linux or Mac). We will also assume that pip is installed and python version 3.8 or above is installed.
### Setting up Environment (optional):
Create a clean virtual environment (Mac and Windows):
```
python -m venv catgen-env
```
Activate new environment (Windows):
```
catgen-env/Scripts/Activate
```
Activate new environment (Mac):
```
source autogen-env/bin/activate
```
### Installing Dependencies:
To run this project these are necessary dependencies we will install:
* Ollama
* Autogen 
* OpenAI
* Pytest

To install Ollama please visit https://ollama.com/download and download for the platform you are currently on.

Once installed verify successful instally by opening the command prompt or terminal and running the command 
```
ollama
```
Once successful download is verified we need to download our LLM models. In this prototype we will be using "llama3.1:latest" and "llama3-groq-tool-use:latest"
```
ollama pull llama3.1:latest
ollama pull llama3-groq-tool-use:latest
```
Once Ollama and the models are successfully downloaded, we need to install:
* Autogen 
* OpenAI
* Pytest
To do so, install via pip:
```
pip install autogen
pip install openai
pip install ollama
pip install pytest
```
Now the enviornment should be set up.
### Running CATGen:
In this current submission, the source code that we will generate unit test code for is located in the directory "CATgen/testings/mainTest.py".

To run the main chat of our prototype, navigate first to "CATgen/groupchat/". Run "mainChat.py"
```
python mainChat.py
```
You will be prompted to select an agent as the next speaker. To reproduce an example run see the Example Execution section of this README.

To run and test individual agents navigate to "CATgen/agents/" and there should be multiple files. All the first except "configs.py" are actively working agents and to run any of them individually replace file with the file continaing the agent to test:
```
python <file>.py
```



## Evaluation and Results
To test and evaluate the generated unit tests, we passed in a [simple
calculator python file](https://github.com/yzhu133/CATGen/blob/main/groupchat/testings/mainTest.py) that had basic functions such as add, subtract,
multiple, and divide. Then as the User we manually selected the
speakers in their intended order to generate a full PyTest unit test
suite. We then empirically evaluated the generated unit test verifying if it did indeed generate unit tests for all existing functions
within the source code. We then ran the code using PyTest and observed that the generate code executed without fail although it had
some tests that did not pass. We attempted to feed the failing test
cases back into the GroupChat to fix them. The results of this varied
depending from iteration to iteration but in at least one iteration
the agents fixed the code and generated a PyTest unit test suite that
passed all the tests and tested all the functions. Ultimately however,
the results of our experiement and testing demonstrated that our
current prototype was unable to process and generate unit tests
for large complex code bases. However, for smaller code bases it
was able to successfully generate unit tests given enough attempts
and prompting. This prototype serves as a proof of concept to a
multi-agent approach but requires further work.
\
\
For future implementations, we would like to evaluate on comparison with NumPy's unit test library. For now, we do have a comprehensive list of NumPy's code coverage in [our repo](https://github.com/yzhu133/CATGen/blob/main/coverage_report.txt).
## Example Execution
Below are screenshots and exact inputs of an example execution of "CATGen/groupchat/mainChat.py". Please note that results will vary from system to system due to the nature of these LLMs.


When you first run "mainChat.py" you will see you (User) have sent a default message to begin the workflow and will be prompted to select the next speaker from a list. Type "2" and click enter.
![catgen](https://github.com/user-attachments/assets/d5eef11e-35fe-40cb-8199-74a3293b88c7)
You will now see tools_agent attempt to make a function call. Click enter.
![catgenn](https://github.com/user-attachments/assets/17f602a4-771e-4ba8-b8ec-b5ca8e34dfa0)
The results of the function call are displayed and you are prompted to select the next speaker. Type "2" and click enter. Then type "1" to select yourself as the next speaker and click enter.
![catgen1](https://github.com/user-attachments/assets/344b9fae-7aff-4f1c-9302-deb4de0f683b)
![catgen2](https://github.com/user-attachments/assets/00772653-71ee-4e50-9994-47ac117e9cc9)
![catgen3](https://github.com/user-attachments/assets/569223ba-3089-4bb4-8804-704f25231957)

As the next speaker type "Write a pytest unit test suite for the code in testings/mainTest.py sent by tools_agent." and click enter. Type "3" to select the test_engineer as the next speaker then click enter. Once the test_engineer is done generating their response type "6" to select the critic_agent and click enter.
![catgen4](https://github.com/user-attachments/assets/8b1714c5-f935-4207-afc8-0342e8cc5f93)
![catgen5](https://github.com/user-attachments/assets/d320aada-76b5-41c9-a010-600eeb1102ca)
![catgen6](https://github.com/user-attachments/assets/079a51b4-9a10-485e-acdb-137dd930e19c)
Once the critic is dont generting their response type "3" to select the test_engineer as the next speaker then click enter.
![catgen7](https://github.com/user-attachments/assets/717726cd-05cd-42a3-8a12-8eb9ae58803d)
![catgen8](https://github.com/user-attachments/assets/61d7c8a2-314a-4fb0-9072-9eba04888b08)
![catgen9](https://github.com/user-attachments/assets/e29d534f-781b-42ef-bc2a-933ede75acfe)
Once the test_engineer is done generating code, copy and paste this code into "CATGen/groupchat/testings/test_mainTest.py". There should be an example already loaded.
![catgen10](https://github.com/user-attachments/assets/883b4615-447e-4bb3-bb82-d8244a7f1a8b)
![catgen11](https://github.com/user-attachments/assets/f54b9d0e-9096-41fc-a607-d1493d1bb608)
![catgen12](https://github.com/user-attachments/assets/fba605de-309c-4b56-a425-4ced58e2c173)
You can now run the generated unit tests by navigating to "CATGen/groupchat/testings/" and running the command 
```
pytest test_mainTest.py
```
## Resources
* [NumPy submodule](https://numpy.org/doc/2.2/dev/index.html)
* [PyTest API Reference](https://docs.pytest.org/en/7.1.x/reference/reference.html)
* [Coverage.py API Reference](https://coverage.readthedocs.io/en/latest/api.html)
* [Tool Useage "CATGen/groupchat/agents/tools.py"](https://github.com/microsoft/autogen/blob/9bc013b82d9379924369d802108eb859605a4e3f/notebook/agentchat_function_call_code_writing.ipynb)
* [Autogen Documentation](https://microsoft.github.io/autogen/0.2/docs/Getting-Started/)
* [Pytest Documentation](https://docs.pytest.org/en/stable/)
* [Ollama](https://ollama.com/)
* [Ollama and Autogen Set Up Tutorial 1](https://www.youtube.com/watch?v=DMYCJe1vBVA)
* [Ollama and Autogen Set Up Tutorial 2](https://www.youtube.com/watch?v=UQw04VW60U0)
* [Calcualtor Code](https://github.com/nevinmathew/Simple-Calculator/blob/main/Simple%20Calculator.py)




### Contributors: Angelika Bermudez & Yuchen Zhu



