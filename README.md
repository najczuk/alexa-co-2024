# Writing Your First Custom Alexa Skill

This guide will walk you through the steps to create your first custom Alexa skill using Python programming language and the Alexa web-based console.

## 1. Create an Alexa Developer Account

1. Go to the [Amazon Developer Portal](https://developer.amazon.com/) and sign in with your Amazon account credentials.
2. Click on the "Alexa" tab and then click on "Get Started" under the "Alexa Skills Kit" section.
3. Follow the instructions to create a new developer account or sign in if you already have one.

## 2. Create Your First Alexa Hosted Custom Skill

1. In the Alexa Developer Console, click on the "Create Skill" button.
2. Choose the "Custom" model for the skill and click "Create skill."
3. On the "Skill Information" page, provide a name for your skill (e.g., "My First Skill").
4. Select "Python" as the language for your skill.
5. Choose the "Start from scratch" option and click "Create skill."

## 3. Define the Invocation Name

1. In the "Interaction Model" section, click on the "Invocation" tab.
2. Enter "teach me" as the Skill Invocation Name.
3. Click "Save Model" and then "Build Model."

## 4. Create the StartIntent

1. In the "Interaction Model" section, click on the "JSON Editor" tab.
2. Locate the "intents" section and add the following code:

```json
{
  "name": "StartIntent",
  "samples": [
    "start quiz",
    "a quiz",
    "start a quiz"
  ]
}
```

3. Click "Save Model" and then "Build Model."

## 5. Create the AnswerIntent with Slots

1. In the "Interaction Model" section, click on the "JSON Editor" tab.
2. Locate the "intents" section and add the following code:

```json
{
  "name": "AnswerIntent",
  "slots": [
    {
      "name": "answer",
      "type": "AMAZON.SearchQuery"
    },
    {
      "name": "city",
      "type": "AMAZON.City"
    }
  ],
  "samples": [
    "it is {answer}",
    "it's {answer}",
    "the answer is {answer}",
    "{city}"
  ]
}
```

3. Click "Save Model" and then "Build Model."

After completing these steps, you will have created your first custom Alexa skill with the specified intents and utterances. You can now proceed to write the code for your skill's logic and deploy it to the Alexa platform.

Note: This README file provides a basic guide to creating a custom Alexa skill using the web-based console. For more advanced features and customizations, you may need to refer to the official Alexa Skills Kit documentation.

## 6. Copy Code and Data Files

1. Switch to the "Code" view in the Alexa Skills Console.
2. Replace the contents of `lambda_function.py` and `utils.py` with the files available in the `lambda` directory of the workshop repository.
3. Copy the `flashcards.json` file from the workshop repository to your skill's project.

## 7. Save and Deploy the Code

1. After making the necessary changes, click on the "Save" button to save your code.
2. Click on the "Deploy" button to deploy your code to the Alexa platform.

## 8. Test the Skill

1. In the Alexa Skills Console, switch to the "Test" view.
2. Enable the "Developer Mode" by toggling the switch in the top-right corner.
3. To trigger your skill, use the invocation name "teach me" followed by the intent utterance. For example, say or type "teach me start a quiz" to trigger the `StartIntent`.
4. Interact with your skill by providing the required responses based on the prompts.

## 9. Access CloudWatch Logs

If you encounter any issues while testing your skill, you can access the CloudWatch logs for debugging purposes.

1. In the Alexa Skills Console, navigate to the "Code" view.
2. Click on the "Logs" button to open the CloudWatch logs for your skill.
3. Here, you can view the logs and identify any errors or issues that may have occurred during the execution of your skill.

By following these steps, you will have successfully created, deployed, and tested your first custom Alexa skill using Python programming language and the Alexa web-based console. Remember to refer to the official Alexa Skills Kit documentation for more advanced features and customizations.

## 10. Possible Improvements

After successfully creating and testing your first custom Alexa skill, you may want to consider adding some improvements to enhance the user experience. Here are a few suggestions:

### 1. Display Current Score

Modify the code to make Alexa respond with the current score before reading the next question. This will help users keep track of their progress during the quiz.

To implement this feature, you can update the `AnswerIntentHandler` class in `lambda_function.py` to include the current score in the response before asking the next question. You can store the current score and number of already asked questions int `attr` variable.

### 2. Enable Hint Functionality

Enhance the skill by allowing users to request a hint for the current question. This can be particularly useful for challenging questions or when users are stuck.

To implement this feature, you can create a new intent (e.g., `HintIntent`) in the Interaction Model and handle it in your code. Within the `HintIntentHandler` class in `lambda_function.py`, you can provide a relevant hint based on the current question or flashcard.


These are just a few examples of possible improvements you could consider. Feel free to explore other enhancements, such as adding more flashcard categories, implementing a leaderboard system, or integrating with external APIs to fetch additional information.

Remember to thoroughly test your changes and ensure that the skill functions as expected before deploying it to the Alexa platform.