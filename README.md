# <p style="text-align: center;">**C**ollaborative **A**gentic **T**est Generation (CATGen)</p>

## Summary
Unit test generation using large language models (LLMs) have shown promising results, yet existing methods still face difficulty in terms of scalability, multi-step reasoning, and handling large codebases.  After surveying the achievements and limitations of modern implementations, we decided to research how we can improve them without the expensive costs of fine-tuning, while taking steps towards a fully automated unit test generation process. As a result, we examined the capabilities of multi-agent LLMs that distribute unit test generation workflow. We present CATGen (Collaborative Agentic Test Generation), an automated unit test generation system that leverages multiple LLM agents. Given limited computational resources we used LLaMA 3.1 (8B parameters) and LLaMA Groq for tool usage. Due to these constraints we observed significant challenges, including frequent hallucinations, loss of memory, and ignoring of instructions by the LLMs, which lead to substantial human intervention. Despite these difficulties, CAT-Gen was able to successfully generated executable unit test suites for small code bases that test all functions at least once. While our results were not always desirable, they serve as a proof of concept, demonstrating the feasibility of automated unit test generation using multi-agent LLMs and highlighting areas for future improvement.

## Documentation
Below are the steps on how to deploy CATGen on a local machine. (Note that this project was built in Windows and some commands will differ for Linux or Mac).
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
* Pip
* Autogen 
* Ollama
* OpenAI
* Python (>= 3.8 perferably)

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
![catgen1](https://github.com/user-attachments/assets/344b9fae-7aff-4f1c-9302-deb4de0f683b)
![catgen2](https://github.com/user-attachments/assets/00772653-71ee-4e50-9994-47ac117e9cc9)
![catgen3](https://github.com/user-attachments/assets/569223ba-3089-4bb4-8804-704f25231957)
![catgen4](https://github.com/user-attachments/assets/8b1714c5-f935-4207-afc8-0342e8cc5f93)
![catgen5](https://github.com/user-attachments/assets/d320aada-76b5-41c9-a010-600eeb1102ca)
![catgen6](https://github.com/user-attachments/assets/079a51b4-9a10-485e-acdb-137dd930e19c)
![catgen7](https://github.com/user-attachments/assets/717726cd-05cd-42a3-8a12-8eb9ae58803d)
![catgen8](https://github.com/user-attachments/assets/61d7c8a2-314a-4fb0-9072-9eba04888b08)
![catgen9](https://github.com/user-attachments/assets/e29d534f-781b-42ef-bc2a-933ede75acfe)
![catgen10](https://github.com/user-attachments/assets/883b4615-447e-4bb3-bb82-d8244a7f1a8b)
![catgen11](https://github.com/user-attachments/assets/f54b9d0e-9096-41fc-a607-d1493d1bb608)
![catgen12](https://github.com/user-attachments/assets/fba605de-309c-4b56-a425-4ced58e2c173)

## Resources
* [NumPy submodule](https://numpy.org/doc/2.2/dev/index.html)
* [PyTest API Reference](https://docs.pytest.org/en/7.1.x/reference/reference.html)
* [Coverage.py API Reference](https://coverage.readthedocs.io/en/latest/api.html)

### Contributors: Angelika Bermudez & Yuchen Zhu



