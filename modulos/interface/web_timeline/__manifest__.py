{
    'name': "Web timeline",
    "version": "0.1",
    "application": False,
    "installable": True,
    "website": "http://acsone.eu",
    'depends': [
        'web',
    ],
    'qweb': [
        'static/src/xml/web_timeline.xml',
    ],
    'data': [
        'views/web_timeline.xml',
    ],
}
