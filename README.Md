## Fine Tuning and Inferencing

This repo contains all the python notebooks that were created in order to learn about Fine Tuning, LoRA and vLLM inferencing when you don't have any compute and Google Colab is your only friend, except for the notebook where I demonstrate OpenAI Fine Tuning for which the company I interned at gave access to me (Thank you Greatify!)

This repo explores LoRA fine-tuning using freely available tools and libraries, excluding OpenAI. All notebooks are designed for easy execution in Google Colab(T4 instance), and Python scripts require dependency installation.

All of this was done as a part of my internship at Greatify.

The following libraries and frameworks are demonstrated:

- **Huggingface Transformers:** For model loading and training.
- **TRL:** Reinforcement Learning utilities for language models.
- **PEFT:** Efficient parameter fine-tuning.
- **LLaMAFactory:** Streamlined LLaMA model fine-tuning.
- **Unsloth FastLanguageModel:** Fast and memory-efficient training.

Additionally, the project covers:

- Using **vLLM** to infer with saved LoRA adapters and respective models.
- Hosting a server in Google Colab and accessing the model via API, utilizing cloudflared for tunneling.

Hands-on examples are provided in notebooks for experimentation.

## Resources 
I am also adding the resources that I used in order to learn it so that it can be beneficial for everyone!

- [HuggingFace Docs (Especially PEFT)](https://huggingface.co/docs/peft)
- Huggingface API reference (Since some guides had outdated object args)
- [LoRA paper](https://arxiv.org/abs/2106.09685)
- [Explanation by the creator of LoRA](https://www.youtube.com/watch?v=DhRoTONcyZE)
- [vLLM Docs](https://docs.vllm.ai/en/latest/features/lora.html)
- [Straightforward guide for multi LoRA inferencing with vLLM](https://boardor.com/blog/deploying-multiple-lora-adapters-on-a-base-model-with-vllm)

If you guys need any help or you got stuck do reach out to me!

Finally I want to thank my mentor at Greatify [Santhosh](https://github.com/santhosh00023) for mentoring me and my pookie senior [Kashiful Haque](https://github.com/kashifulhaque) for helping me out by guiding me to right sources and also the Google Overlords to have given me access to the T4 GPU in 4 accounts 😉

