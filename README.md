# EXCEED Prolific Study - Prelaunch Analysis & Checks

This repository contains the data and the Jupyter notebooks used for the prelaunch analysis and checks of the EXCEED
Prolific study. The notebooks are meant to be run and explored prior to the launch of the main study that we will run
on Prolific. More specifically, we have the following notebooks in the `notebooks` directory:

- `01_fantastic_four.ipynb`: Analyzes pilot study data from 8 Python buggy code snippets and their error messages, rated
  by participants on a 1-5 scale for several statements which we will list below. The aim is to select four
  representative snippets (the "Fantastic Four") for the main Prolific study. The questions that participants rated
  were:
    - "_This code snippet is difficult to understand._"
    - "_I would find it challenging to resolve the issue in this code snippet._"
    - "_Reading this error message feels mentally demanding._"
    - "_This error message is useful for identifying the problem._"
- `02_fantastic_four_prolific.ipynb`: It does the same analysis as the previous notebook, but it uses data that was
  collected via Prolific.
- `03_fantastic_four_combined.ipynb`: Combines the data from the previous two notebooks to analyze the
  Fantastic Four snippets. It also provides a comparison of the ratings between the pilot study and Prolific data.
  Within this notebook, we will also actually select the Fantastic Four snippets based on the aggregated ratings.
- `04_validation_checks.ipynb`: Assesses the effectiveness of rephrased Python error messages for the Fantastic Four
  snippets. Authors provided feedback, which was aggregated and analyzed to validate the project's contribution before
  launching the main study.

> **Notes**: 
> * As expected, the data that was used within these notebooks is stored within the `data` directory.
> * The candidate code snippets that were used in the pilot study are stored in the `data/code_snippets`.

---

## 🏃🏻 Running the notebooks

1. **Clone or fork** the repo

   ```bash
   git clone https://github.com/alemoraru/exceed-python-skill-assessment.git
   cd exceed-python-skill-assessment
   ```
2. **Create a fresh Python ≥3.12 environment** (virtualenv or conda)

   ```bash
   python -m venv .venv
   source .venv/bin/activate
   cd notebooks
   ```
3. **Install dependencies (Optional)**

   ```bash
   pip install -r requirements.txt
   ```

   This step is optional, since each notebook will run `pip install -r requirements.txt` as the first step.

4. **Launch Jupyter** and run the notebooks top‑to‑bottom

   ```bash
   jupyter lab 01_fantastic_four_convenience.ipynb
   jupyter lab 02_fantastic_four_prolific.ipynb
   jupyter lab 03_fantastic_four_combined.ipynb
   jupyter lab 04_validation_checks.ipynb
   ```
   Alternatively, you can of course run the notebooks within VS Code or any other Jupyter-compatible IDE
   (e.g., PyCharm).

---

## 🤝 Contributing

This project was developed as part of the EXCEED MSc Thesis project at Technische Universiteit Delft. As such,
contributions of any sort will not be accepted. This repository is provided for replication and educational purposes
ONLY. Since it was used to orchestrate the deployment of our study on Prolific, it is NOT intended for further
development or contributions.

---

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
