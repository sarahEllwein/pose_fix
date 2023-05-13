# Fix Your Gains
## SLO Hacks 2023 Project

### Summary and Goals

A mobile app project that assist users to correct 
their form when exercising using Google Mediapipe. 

Here's how it works:
1. Users upload a video to the app.
2. The app uses Google Mediapipe to create joint estimates.
3. Scan through the video using these joint estimates for poor form.
4. Create a tip sheet with all form corrections

### Installation

1. Clone this repository on your local machine
2. Open this repository on your IDE and enter these command:\
`virtualenv fix_your_gains`\
`pip install -r requirements.txt`
3. After all necessary libraries are installed, activate the virtual environment:\
`source fix_your_gains/bin/activate`
    * To deactive the virtual environment, enter `deactivate`
4. Start coding!