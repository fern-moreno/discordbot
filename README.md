# discordbot

This bot is designed for college students who create Discord servers to communicate with each other about a college course they are enrolled in.
Depending on a command a user enters, the bot will output different information about the course. For example, if someone types `.office_hours` the bot will 
display the current office hours that the teacher has for the day. Typing in `.current_assignments hw` will display upcoming homework assignments that are 
due. 

Other functionality includes:
- displaying how many remaining assignments there are (homework, exams, quizzes, etc)
- displaying assignment details (due date and how many points it is worth)
- whether and assignment is late, and how many points it is now worth after applying late penalties
- displaying teacher contact information

Each assignment type has its own dictionary, where the values are stored as a list.
