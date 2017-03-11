# OpenMind Backend API

## Generating Test Data
The command to create test data is in the format: 
- `python manage.py loadtestdata app.Model:#`

To generate test data for the Emotion and Journal models run the following command:
- `python manage.py loadtestdata emotion.Emotion:10 journal.Journal:10`