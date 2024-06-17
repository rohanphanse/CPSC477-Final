## CPSC 477 Final: Knowledge Distillation From Gemini to Mistral for Earnings Call Transcript Summarization
By: Rohan Phanse and Joonhee Park

### Setup Guide

First, install Jupyter Lab by running `pip install jupyterlab` in the terminal and start the server with the `jupyter-lab` command. Next, run the cells in `data.ipynb` in order to generate the augmented dataset. Then, run the `train.ipynb` notebook on a GPU - we used the A100 through Google Colab. Load the CSV files for each split of the augmented dataset into the environment: `train.csv`, `val.csv`, `test.csv` in the `dataset` directory. The train notebook will finetune the Mistral model, perform inference on the test dataset, and store the generated summaries in a directory. Finally, add that directory of summaries to the `inference` directory and run `eval.ipynb` to obtain the ROUGE scores and evaluation metrics of those summaries.

### Report

See [`report.pdf`](https://github.com/rohanphanse/CPSC477-Final/blob/main/report.pdf) for details about project motivations, related work, approach, and results.
