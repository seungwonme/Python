# Prompt Engineering

- [Principled Instructions Are All You Need for Questioning LLaMA-1/2, GPT-3.5/4](https://arxiv.org/abs/2312.16171)
- [Prompt Engineering Guide](https://www.promptingguide.ai/kr)
- [dair-ai/Prompt-Engineering-Guide: 🐙 Guides, papers, lecture, notebooks and resources for prompt engineering](https://github.com/dair-ai/Prompt-Engineering-Guide)
- [f/awesome-chatgpt-prompts: This repo includes ChatGPT prompt curation to use ChatGPT better.](https://github.com/f/awesome-chatgpt-prompts)
- [linexjlin/GPTs: leaked prompts of GPTs](https://github.com/linexjlin/GPTs)

## Prompt Design

- Main Instructions - a task you want the model to perform
- Data - any input data (if necessary) 
- Output Instructions - what type of output do you want? What format?

```
### Instruction ###
<Main Instructions>:

<Output Instructions>:

<Data>:
```

### Examples
```
Extract a list of place names from the following input text

Desired Format:
Places: <comma_separated_list_of_names>
JSON array of place names

input: Alaska is a non-contiguous U.S. state on the northwest extremity of North America. It borders the Canadian province of British Columbia and the Yukon territory to the east; it shares a western maritime border in the Bering Strait with Russia's Chukotka Autonomous Okrug. The Chukchi and Beaufort Seas of the Arctic Ocean lie to the north and the Pacific Ocean lies to the south. Technically a semi-exclave of the U.S., Alaska is the largest exclave in the world.
```

```
Generate a list of the top 5 most populated countries in the world with their population

Desired Format: JSON object with country name as the key and population as the value
```

```
Summarize the following text in 2-3 sentences

Input: Psychology is the study of mind and behavior.[1] Its subject matter includes the behavior of humans and nonhumans, both conscious and unconscious phenomena, and mental processes such as thoughts, feelings, and motives. Psychology is an academic discipline of immense scope, crossing the boundaries between the natural and social sciences. Biological psychologists seek an understanding of the emergent properties of brains, linking the discipline to neuroscience. As social scientists, psychologists aim to understand the behavior of individuals and groups.[2][3]

A professional practitioner or researcher involved in the discipline is called a psychologist. Some psychologists can also be classified as behavioral or cognitive scientists. Some psychologists attempt to understand the role of mental functions in individual and social behavior. Others explore the physiological and neurobiological processes that underlie cognitive functions and behaviors.

Psychologists are involved in research on perception, cognition, attention, emotion, intelligence, subjective experiences, motivation, brain functioning, and personality. Psychologists' interests extend to interpersonal relationships, psychological resilience, family resilience, and other areas within social psychology. They also consider the unconscious mind.[4] Research psychologists employ empirical methods to infer causal and correlational relationships between psychosocial variables. Some, but not all, clinical and counseling psychologists rely on symbolic interpretation.

While psychological knowledge is often applied to the assessment and treatment of mental health problems, it is also directed towards understanding and solving problems in several spheres of human activity. By many accounts, psychology ultimately aims to benefit society.[5][6][7] Many psychologists are involved in some kind of therapeutic role, practicing psychotherapy in clinical, counseling, or school settings. Other psychologists conduct scientific research on a wide range of topics related to mental processes and behavior. Typically the latter group of psychologists work in academic settings (e.g., universities, medical schools, or hospitals). Another group of psychologists is employed in industrial and organizational settings.[8] Yet others are involved in work on human development, aging, sports, health, forensic science, education, and the media.
```
