from flask import request, redirect, render_template, url_for, flash
from app import app
from services import ShortUrlService


@app.route('/', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        url = request.form['url']
        short_url = request.form['short_url']

        if short_url and ShortUrlService.short(short_url) is not None:
            flash('Please enter different short url! '
                  'This url already exists', 'danger')
            return redirect(url_for('create'))

        if url and ShortUrlService.long(url) is not None:
            flash('Please enter different url! '
                  'This url already exists', 'danger')
            return redirect(url_for('create'))

        if not url:
            flash('The URL is required!')
            return redirect(url_for('create'))

        if not short_url:
            ShortUrlService.gen()

        ShortUrlService.new(url, short_url)
        return render_template('index.html')

    return render_template('index.html')


@app.route('/urls')
def all_urls():
    urls = ShortUrlService.all_urls()
    return render_template('all.html', urls=urls)


@app.route('/<short_url>')
def redirect_url(short_url):
    link = ShortUrlService.short(short_url)
    ShortUrlService.count_click(link)
    return redirect(link.long_url)


if __name__ == '__main__':
    app.run(debug=True)
