# Adventure Story

## Introduction 

Adventure story was created to bring back childhood memories. As a child I hated to read books but loved books that gave me options on how the story went. I liked how I could read it over and over again and get to a different ending everytime.

The main aim of this project was to give an adult their memories back, to play a fun but potenitally scary game, through reading and just answering a few questions.

Most games have no meaning behind them, like battleships for example, you just have to guess where they are. However with this game you are reading which is great for your mind and having fun in the proccess.

## Table of contents
* [How To Play](#How_To_Play)
* [Features](#Features)
* [Testing](#Testing)
* [Deployment](#Deployment)
* [Credits](#Credits)
* [After Thoughts](#After_Thoughts)

# How To Play

- The Player first has to confirm their age as they have to be 18+ to play this game.
- The story then loads up, they get given two possible answers and get's to choose which one to take, each way will give them a different ending.


[Back to Table of contents](#table-of-contents)

# Features
- The Welcome Message
    - When a new game starts the welcome message is displayed.
    - You are also met with a question asking how old you are. Because as stated in the rules you have to be 18+ to play the game.

- The Story
    - At the moment there is only one story, however there are different ways to get to the ending.
    - You get given a sentence/paragraph then get asked to choose which way you would like to go, this will effect the outcome of your story.

[Back to Table of contents](#table-of-contents)

# Testing
- Due to the nature of the project, testing has been implemented throughout the entire project mainly debugging through running the program in the terminal as well as debugging using the python debugger.

## Validator Testing

- HTML
    - Not within project scope.

- CSS
    - Not within project scope.

- JS
    - Not within project scope.

- Python
    - No errors were found when passing through the [PEP8 Validator tool](http://pep8online.com/)

- **Lighthouse**

    - Not within project scope.

## Bugs


[Back to Table of contents](#table-of-contents)

## Deployment
The site was deployed via Heroku, and the live link can be found here - 

### Project Deployment
To deploy the project through Heroku I followed these steps:
- Sign up / Log in to [Heroku](https://www.heroku.com/)
- From the main Heroku Dashboard page select 'New' and then 'Create New App'
- Give the project a name - I entered AdventureStory and select a suitable region, then select create app. The name for the app must be unique.
- This will create the app within Heroku and bring you to the deploy tab. From the submenu at the top, navigate to the settings tab.
- This next step is required for creating the app when using the CI Python Deployment Template. If you created your own program without using the CI Template, you might not need to add a config var.
- In the config vars section select the reveal config vars button. This will display the current config vars for the app, there should be nothing already there.
- In the KEY input field input PORT all in capitals, then in the VALUE field input 8000 and select the Add button to the right.
- Next select the add buildpack button below the config vars section.
- In the pop-up window select Python as your first build pack and select save changes.
- Then repeat the steps to add a node.js buildpack.
- The order of the buildpacks is important, in the list Python should be first with Node.js second. If they are not in this order, you can click and drag them to rearrange.
- Next navigate back to the deploy tab using the submenu at the top of the page.
- In the deployment method section select the GitHub - Connect to GitHub button and follow the steps prompted if any to connect your GitHub account
- In the Connect to GitHub section that appears, select the correct account, and enter the name of the repository and select search.
- Once Heroku has located the repo select connect.
- This will connect the repo to the app within Heroku. Below the Apps Connected to Heroku section will be the Automatic Deploys section.
- In this section, confirm the correct branch of the repo is selected in the drop-down box, and then click the Enable Automatic Deploys button
- This will ensure whenever you change something in the repo and push the changes to GitHub, Heroku will rebuild the app. If you prefer to do this manually you can utilise the manual deployment options further down. For this project I utilised the Automatic Deployment to enable me to check changes I made to the app as I developed it.
- Heroku will now build the app for you. Once it has completed the build process you will see a 'Your App Was Successfully Deployed' message and a link to the app to visit the live site.

[Back to Table of contents](#table-of-contents)

# Credits

[Back to Table of contents](#table-of-contents)

# After Thoughts

I am disapointed with how this project turned out. I planned to do a big version of love sandwiches which would be used to manage my bars stock, so our bar manager could use the system to plan her orders for the week. Half way through my project I broke 2 of my fingers, I tried to carry on with my project but realised yesterday theres no way I can finish it. I have made adventure story in hope to get the pass but I couldnt have forseen how difficult It would have been to complete a small project in a day. 

With reflect I should have started this smaller project a while ago, then I could have atleast had some confidence that I have fixed all the bugs. I had a bad start, with just a month to learn python and create the project I should have chosen a project that I could confidently complete within the time-scale.

[Back to Table of contents](#table-of-contents)