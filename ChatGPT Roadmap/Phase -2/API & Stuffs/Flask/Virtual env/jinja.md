# About Jinja2

Jinja2 is a templating engine for Python.
It lets you embed Python-like expressions into HTML so your website can show dynamic content.

It's not a compulsory part for our journey, but let's just learn it because it's on the tutorial.

## What does it do?

Jinja takes an HTML file with special syntax (placeholders, loops, if-else), fills in the blanks with data from Python, and sends the final HTML to the browser.

- It mainly has two major syntax rules:
1. {% %} for a logic (like: for, if-else)
2. {{ }} for variables

## Template inheritence with block tags

Jinja uses two special tags for template inheritence with html;
1. {% block *Something* %}
2. {% endblock %}
  
 These are Jinja "block tags" used for template inheritance — a way to avoid repeating the same HTML (like headers, navbars, footers) across multiple pages.

  You can see it working in the base.html and index.html file.

## Connecting stylesheet or js file

Unlike normal `<link rel="stylesheet" href= path_to_css_file>`, you have to use some extra spice to let the renderer understand the file path. In this case, we gotta use something named `url_for()` to allow to perfectly link a file. Here's an example: 


`<link rel="stylesheet" href="{{ url_for("static", filename="css/main.css") }}"> `

You can see it in action in **base.html** file 

