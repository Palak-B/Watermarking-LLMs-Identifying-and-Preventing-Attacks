# Watermarking-LLMs-Identifying-and-Preventing-Attacks
The project seeks to create defense systems against insertion attacks and contribute to the responsible and secure use of LLMs
Abstract
This project aims to enhance the existing watermarking framework presented by
Kirchenbauer et al. (2023), with a specific focus on mitigating text insertion attacks
against Large Language Models (LLMs). We present a two-part solution. In the
first ‘simple’ solution, we extend the watermarking framework by incorporating
one sublayer: an attack classifier in the text generation pipeline. In the second
‘real-world’ solution, once a prompt is identified as an insertion attack, we create
an attack-free version of the prompt and provide it to the watermarker. This way,
despite attackers removing the inserted tokens, our detector can still accurately
identify watermarks. We test the efficiency of our solutions through comprehensive
testing against text insertion attacks. We have an accuracy of 99.5% with solution I
and 36% with solution II.
Introduction
The advent and development of Large Language Models (LLMs), such as GPT-3, GPT-4, PaLM2,
and LLaMA, have undeniably revolutionized the natural language processing field, demonstrating
unprecedented performance in a wide range of applications, including but not limited to language
translation, questions answering, summarization, and even creating executable
codes. Most notably, these models can understand and generate relevant and logical long-form
texts that are indistinguishable from those written by humans. However, with their escalating
influence and widespread adoption, LLMs are becoming vulnerable to potential misapplications,
spanning a spectrum of domains, from academic cheating, plagiarizing, and generating fake news, to
impersonating human users, engaging in fraudulent activities, and even compromising public services. In light of these concerns, the need to identify LLM-generated text has become paramount.
One compelling approach to address this is through watermarking techniques, which both protect the
intellectual property rights of the models and mitigate the potential harms caused by their misuse.
Watermarking involves injecting imperceptible information or patterns into the generated text to
enable the efficient detection of machine-generated content while maintaining the quality of the
generated text. Nevertheless, watermarking is susceptible to various types of prompt-based attacks,
such as insertion, deletion, paraphrasing, and substitution attacks, in which the watermarked text is
easily altered after generation. In this context, we seek to create defense systems against these attacks
and explore how these approaches can contribute to the responsible use of LLMs.
Kirchenbauer et al. proposed a watermarking framework that generates pseudo-random “red”
and “green” token lists of equal size from a vocabulary that typically contains at least |V | = 50, 000
tokens. During the text generation step, the green tokens are softly promoted, i.e. increasing
probability by δ, before a word is generated. The detector relies on knowing which tokens fall in
the “green” and “red” lists for each generated word. Because the red list is chosen at random, it is
expected that half of the human-generated tokens would be in the red list, while few to none of the
machine-generated tokens are. However, the efficacy of this watermarking model is compromised
when faced with adversarial users who are aware of the watermarking algorithm and employ various
strategies to evade detection. For instance, an attack known as "Emoji Attack" prompts the generator
to insert emoji tokens after every word that can then be removed, which randomizes the red lists
37th Conference on Neural Information Processing Systems (NeurIPS 2023).
(a) Detecting Text as Language Model Generated (b) Detecting Text without Emoji Incorrectly as Human
Figure 1: Example of Kirchenbauer et al. Watermarker Failing with Insertion Attack.
associated with subsequent non-emoji tokens. We aim to make the watermarker robust
to prompt-based attacks.
