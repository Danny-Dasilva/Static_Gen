from markdown import markdown
from jinja2 import Environment, FileSystemLoader
from json import load

template_env = Environment(loader=FileSystemLoader(searchpath='./'))
template = template_env.get_template('layout.html')

with open('article.md') as markdown_file:
    article = markdown(markdown_file.read(),
    extensions=['extra',])

with open('config.json') as config_file:
    config = load(config_file)

with open('index2.html', 'w') as output_file:
    output_file.write(
        template.render(
            title=config['title'],
            article=article
        )
    )