# Image Scrambling

This Python project lets you scramble and unscramble images using the logistic map algorithm. The current implementation uses hardcoded values, with plans to introduce interactive features in future updates.



## Features
- **Image Scrambling**: Transforms images into a scrambled state using the logistic map algorithm.
- **Image Unscrambling**: Restores scrambled images to their original form. 

## Dependencies
The project requires the following Python libraries:
- **NumPy**: For efficient numerical computations. 
- **OpenCV (cv2)**: For image processing capabilities. 
- **Random**: For generating random values in the scrambling process. 








## Installation and Usage on Windows 🖥️

1. **Download the Project** 
- Download ZIP
- Extract it

2. **Open Command Prompt in the Project Folder**
Navigate to the project directory:
- Hold `Shift`, right-click an empty space in the folder, and select **Open PowerShell window here** or **Open Command Prompt here**. A terminal window will open, ready for commands.

**Note**: If **Open Command Prompt here** is unavailable, PowerShell is a suitable alternative.

3. **Set Up a Virtual Environment**
Create an isolated environment for the project’s dependencies:
- In the Command Prompt or PowerShell, enter:
  ```bash
  python -m venv lms_env
  ```
  This creates a folder named `lms_env` for the project’s dependencies.
- Activate the environment:
  ```bash
  lms_env\Scripts\activate
  ```
  The prompt will display `(lms_env)`, indicating the environment is active.
- For PowerShell, use:
  ```bash
  .\lms_env\Scripts\Activate.ps1
  ```

**Purpose**: A virtual environment isolates project dependencies, preventing conflicts with other Python projects.

**Note**: Omitting the virtual environment installs libraries globally, which is acceptable unless you manage multiple Python projects.

4. **Install Dependencies**
Install the required libraries:
- In the Command Prompt (with `(lms_env)` displayed), run:
  ```bash
  pip install -r requirements.txt
  ```
  This installs NumPy, OpenCV, and other dependencies listed in `requirements.txt`. The process may take a moment.


5. **Run the Script** 

#### Run the `lms.py` with either 'scram' or 'unscram YOUR_KEY' and the image filename as arguments

```bash
python lms.py scram picture.jpg
```
 ***The key used for unscrambling is saved along with the scrambled image (key.npy)***

 ```bash
python lms.py unscram key.npy scramebled_picture.jpg
```

6. **View Results** 
- Result will be saved in the same directory as `lms.py`.









## Installation and Usage on Linux/Mac 🐧

To set up and run the project on Linux or Mac:

1. **Clone the Repository**
   - Open a terminal and navigate to your preferred directory (e.g., `cd ~/Desktop`).
   - Clone the repository:
     ```bash
     git clone <repo-link>
     ```

 2. **Create a Virtual Environment**
   - Run this command in the project directory:
     ```bash
     python3 -m venv lms_env
     source lms_env/bin/activate
     ```

 3. **Install Dependencies**
   - Execute:
     ```bash
     pip install -r requirements.txt
     ```

4.  **Run the Script**

#### Run the `lms.py` with either 'scram' or 'unscram YOUR_KEY' and the image filename as arguments

```bash
python lms.py scram picture.jpg
```
 ***The key used for unscrambling is saved along with the scrambled image (key.npy)***

 ```bash
python lms.py unscram key.npy scramebled_picture.jpg
```


 5. **View Results**
   - Result will be saved in the same directory as `lms.py`.






Thank you for exploring this project! 🌟