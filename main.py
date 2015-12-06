from flask import Flask
from flask.views import View
from flask.templating import render_template
from album_creator import create_album, get_album_image


app = Flask(__name__)


class MainView(View):
    methods = ('GET', )
    template_name = 'index.html'

    def dispatch_request(self):
        return render_template(self.template_name, album_name=create_album().decode('utf-8'), album_img=get_album_image())


class GetAlbumView(MainView):
    template_name = 'index_content.html'


app.add_url_rule('/', view_func=MainView.as_view('main_view'))
app.add_url_rule('/get_album', view_func=GetAlbumView.as_view('get_album'))

if __name__ == '__main__':
    app.run()
