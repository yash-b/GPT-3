# Content generation for Trumpia's product research

### Technologies used
#### Open AI API, Python, Flask

- Flask uses `app_blueprint.py` to use `index.html` to receive prompt, content type, and content mood to display generated content.
- Utilizes generate_content() in `contentgeneration.py` function to touch OpenAI and receive AI content based on prompt.
- Utilizes get_cost() in `contentgeneration.py` to calculate cost per AI generation for the current run.

#### Screencap
<img src="https://cdn.discordapp.com/attachments/693920868220403742/1080653106167173130/image.png"
     alt="Markdown Monster icon"
     style="float: left;" />