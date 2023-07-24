
# Polls Application

The "Polls Application" is a web application developed with Django, a Python-based web development framework. This application enables users to create and participate in polls.

## Features
 
Main features of the application :

Poll creation: Users can create new polls by specifying a question and associated choices.

Voting: Users can vote for their favorite choices in existing polls.

Display results: Once a user has voted in a poll, the results are displayed with the number of votes for each choice.

View active polls: The application displays only active polls with a publication date prior to the current date.

## Screenshots
![Home Page w/ Text](/public/index.png)
![Polling Page w/ Text](/public/votes.png)
![Result Page w/ Text](/public/result.png)
![Add sondage w/ Text](/public/add%20sondage.png)

## Requirements
Python [version 3.11.3]
Django [version 4.2]




## Installation

1.Clone the GitHub repository:

```bash
  git clone [URL du repository]
```

2.Perform database migrations :

```bash
  python manage.py migrate

```

3.Start the development server:

```bash
  python manage.py runserver

```

4.Access the application in your browser at :
```bash
  http://localhost:8000/
```
## License

[MIT](https://choosealicense.com/licenses/mit/)


## Acknowledgements

 - [Awesome Readme Templates](https://awesomeopensource.com/project/elangosundar/awesome-README-templates)
 - [Awesome README](https://github.com/matiassingers/awesome-readme)
 - [How to write a Good readme](https://bulldogjob.com/news/449-how-to-write-a-good-readme-for-your-github-project)
 - [Writing your first Django application](https://docs.djangoproject.com/en/4.2/intro/tutorial01/)
