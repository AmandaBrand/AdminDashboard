from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.http import require_http_methods
from django.http import JsonResponse, HttpResponse
from django.conf import settings

import json, time

from slugify import slugify

from dashboard.models import *


# Global Variables
# ------------------
CYCLE = Cycle.objects.get(is_current=True)
DEBUG = settings.DEBUG
V = '2016-06-04-1350'
DATA = {
    'page': 'write',
    'version': V,
    'hasPageJS': False,
    'hasPageCSS': False,
    'debug': DEBUG,
    'cycle': CYCLE,
    'loggedIn': False
}
CATEGORIES = Topic.objects.all()



@csrf_protect
@require_http_methods(["GET"])
def write(request):
    if 'username' in request.session:
        DATA['page'] = 'write'
        
        return render(request, 'pages/editor.html', {
            'username': request.session['username'], 
            'data': DATA,
            'categories': CATEGORIES
        })
    else:
        return redirect('dashboard.views.index')


@csrf_protect
@require_http_methods(["GET"])
def edit(request, article_id):
    if 'username' in request.session:
        a = Article.objects.get(id=article_id)
        DATA['page'] = 'edit'

        return render(request, 'pages/editor.html', {
            'username': request.session['username'], 
            'data': DATA,
            'article': a,
            'categories': CATEGORIES
        })
    else:
        return redirect('dashboard.views.index')


# def reread(id):
#     # reading articles in the queue

#     PAGEDATA = {}

#     PAGEDATA.update(DATA)
#     PAGEDATA['page'] = 'proof'
#     PAGEDATA['hasPageCSS'] = False

#     connection.connect()
#     connection.request('GET', '/1/classes/Queue/'+id, '', {
#         "X-Parse-Application-Id": PARSEappID,
#         "X-Parse-REST-API-Key": RESTapiKEY
#     })

#     result = json.loads(connection.getresponse().read().decode('utf-8'))

#     if 'error' not in result.keys():
#         return render_template('editor_proof.html', article=result, data=PAGEDATA)

#     else:
#         print ("error, couldn't find article")
#         # make a notification
#         return redirect(url_for('dashboard.admin'))


# def proof(id):
#     # reading published articles
    
#     PAGEDATA = {}

#     PAGEDATA.update(DATA)
#     PAGEDATA['page'] = 'proof'
#     PAGEDATA['hasPageCSS'] = False

#     connection.connect()
#     connection.request('GET', '/1/classes/Articles/'+id, '', {
#         "X-Parse-Application-Id": PARSEappID,
#         "X-Parse-REST-API-Key": RESTapiKEY
#     })

#     result = json.loads(connection.getresponse().read().decode('utf-8'))

#     if 'error' not in result.keys():
#         return render_template('editor_proof.html', article=result, data=PAGEDATA)

#     else:
#         print ("error, couldn't find article")
#         # make a notification
#         return redirect(url_for('dashboard.admin'))





# --------------------------------------------------------------------
# POST METHODS
# --------------------------------------------------------------------

# @require_POST()
# def submit(request):
#     title = request.form.get('title', None)
#     author = request.form.get('author', None)
#     description = request.form.get('description', None)
#     content = request.form.get('content', None)
#     featureIMG = request.form.get('featureIMG', None)
#     status = request.form.get('status', None)
#     releaseDate = request.form.get('releaseDate', None)
#     doctype = request.form.get('doctype', None)
#     docstyle = request.form.get('docstyle', None)
#     cycle = request.form.get('cycle', None)
#     headerIMG = request.form.get('headerIMG', None)
#     coAuthor = request.form.get('coAuthor', None)
#     tags = request.form.get('tags', None)
#     category = request.form.get('category', None)
#     photoCred = request.form.get('photoCred', None)

#     slug = slugify(title)

#     currCycle = 0
    
#     if cycle == 'True':
#         cycle = True
#         currCycle = CURRCYCLE
#     else:
#         cycle = False

#     connection.connect()
#     connection.request('POST', '/1/classes/InProgress', json.dumps({
#         "title": title,
#         "author": author,
#         "description": description,
#         "content": content,
#         "featureIMG": featureIMG,
#         "status": status,
#         "releaseDate": releaseDate,
#         "doctype": doctype,
#         "docstyle": docstyle,
#         "cycleArticle": cycle,
#         "cycle": currCycle,
#         "category":[x.strip() for x in category.split(',')],
#         "tags": [y.strip() for y in tags.split(',')],
#         "authorFull": {
#             "__type": "Pointer",
#             "className": "_User",
#             "objectId": escape(session['uID'])
#         },
#         "headerIMG": headerIMG,
#         "coAuthor": coAuthor,
#         "photoCred": photoCred,
#         "slug": slug
#     }), {
#         "X-Parse-Application-Id": PARSEappID,
#         "X-Parse-REST-API-Key": RESTapiKEY,
#         "Content-Type": "application/json"
#     })

#     result = json.loads(connection.getresponse().read().decode('utf-8'))

#     if 'error' in result.keys():
#         print ('error when saving')
#         print (result)
#         return jsonify({ 'error': '<strong>Error:</strong> Your article could not be saved. Please make sure the fields are filled out correctly.' })

#     else:
#         print ('success')
#         session['newArticle'] = result['objectId']
#         return jsonify({ 'success': 'The article has been successfully saved. You will now be redirected to the dashboard.' })

# @require_POST()
# def update(request):
#     articleID = request.form.get('id', None)
#     title = request.form.get('title', None)
#     author = request.form.get('author', None)
#     description = request.form.get('description', None)
#     content = request.form.get('content', None)
#     featureIMG = request.form.get('featureIMG', None)
#     status = request.form.get('status', None)
#     releaseDate = request.form.get('releaseDate', None)
#     doctype = request.form.get('doctype', None)
#     docstyle = request.form.get('docstyle', None)
#     cycle = request.form.get('cycle', None)
#     headerIMG = request.form.get('headerIMG', None)
#     coAuthor = request.form.get('coAuthor', None)
#     tags = request.form.get('tags', None)
#     category = request.form.get('category', None)
#     photoCred = request.form.get('photoCred', None)
#     table = request.form.get('table', None)
    
#     cat = [x.strip() for x in category.split(',')]
#     tagslist = [y.strip() for y in tags.split(',')]
    
#     connection.connect()
#     connection.request('GET', '/1/classes/'+ table +'/'+articleID, '', {
#         "X-Parse-Application-Id": PARSEappID,
#         "X-Parse-REST-API-Key": RESTapiKEY
#     })

#     updates = {}

#     result = json.loads(connection.getresponse().read().decode('utf-8'))
    
#     currCycle = 0
    
#     if cycle == 'True':
#         cycle = True
#         currCycle = CURRCYCLE
#     if cycle == 'False':
#         cycle = False

#     if result['title'] != title:
#         updates['title'] = title
#         updates['slug'] = slugify(title)

#     if result['author'] != author:
#         updates['author'] = author

#     if result['description'] != description:
#         updates['description'] = description

#     if result['tags'] != tagslist:
#        updates['tags'] = tagslist

#     if result['content'] != content:
#         updates['content'] = content

#     if result['featureIMG'] != featureIMG:
#         updates['featureIMG'] = featureIMG

#     if result['status'] != status:
#         updates['status'] = status

#     if result['releaseDate'] != releaseDate:
#         updates['releaseDate'] = releaseDate

#     if result['doctype'] != doctype:
#         updates['doctype'] = doctype

#     if result['docstyle'] != docstyle:
#         updates['docstyle'] = docstyle

#     if result['cycle'] != cycle:
#         updates['cycleArticle'] = cycle
#         updates['cycle'] = currCycle

#     if result['category'] != cat:
#         updates['category'] = cat

#     if result['headerIMG'] != headerIMG:
#         updates['headerIMG'] = headerIMG

#     if result['coAuthor'] != coAuthor:
#         updates['coAuthor'] = coAuthor

#     if result['photoCred'] != photoCred:
#         updates['photoCred'] = photoCred

#     connection.request('PUT', '/1/classes/'+ table +'/'+articleID, json.dumps(updates), {
#         "X-Parse-Application-Id": PARSEappID,
#         "X-Parse-REST-API-Key": RESTapiKEY,
#         "Content-Type": "application/json"
#     })

#     result2 = json.loads(connection.getresponse().read().decode('utf-8'))

#     if 'error' in result2.keys():
#         print ('\n', result2, '\n')
#         return jsonify({ 'error': '<strong>Error:</strong> Your article could not be saved. Please make sure the fields are filled out correctly.' })

#     else:
#         return jsonify({ 'success': 'The article has been successfully saved. You will now be redirected to the dashboard.' })

# @require_POST()
# def queue(request):
#     if request.method == 'POST':
#         articleID = request.form.get('id', None)
#         title = request.form.get('title', None)
#         author = request.form.get('author', None)
#         description = request.form.get('description', None)
#         content = request.form.get('content', None)
#         featureIMG = request.form.get('featureIMG', None)
#         status = request.form.get('status', None)
#         releaseDate = request.form.get('releaseDate', None)
#         doctype = request.form.get('doctype', None)
#         docstyle = request.form.get('docstyle', None)
#         cycle = request.form.get('cycle', None)
#         headerIMG = request.form.get('headerIMG', None)
#         coAuthor = request.form.get('coAuthor', None)
#         tags = request.form.get('tags', None)
#         category = request.form.get('category', None)
#         photoCred = request.form.get('photoCred', None)

#         cat = [x.strip() for x in category.split(',')]
#         tagslist = [y.strip() for y in tags.split(',')]

#         currCycle = 0
        
#         if cycle == 'True':
#             cycle = True
#             currCycle = CURRCYCLE
#         else:
#             cycle = False

#         connection.connect()
#         connection.request('GET', '/1/classes/InProgress/'+articleID, '', {
#             "X-Parse-Application-Id": PARSEappID,
#             "X-Parse-REST-API-Key": RESTapiKEY
#         })
#         result = json.loads(connection.getresponse().read().decode('utf-8'))

#         updates = {}

#         updates['authorFull'] = result['authorFull']
#         updates['title'] = title
#         updates['slug'] = slugify(title)
#         updates['author'] = author
#         updates['description'] = description
#         updates['content'] = content
#         updates['featureIMG'] = featureIMG
#         updates['status'] = status
#         updates['releaseDate'] = releaseDate
#         updates['doctype'] = doctype
#         updates['docstyle'] = docstyle
#         updates['cycleArticle'] = cycle
#         updates['cycle'] = currCycle
#         updates['headerIMG'] = headerIMG
#         updates['coAuthor'] = coAuthor
#         updates['tags'] = tagslist
#         updates['category'] = cat
#         updates['photoCred'] = photoCred

#         connection.request('POST', '/1/classes/Queue/', json.dumps(updates), {
#             "X-Parse-Application-Id": PARSEappID,
#             "X-Parse-REST-API-Key": RESTapiKEY,
#             "Content-Type": "application/json"
#         })

#         result2 = json.loads(connection.getresponse().read().decode('utf-8'))

#         if 'error' in result2.keys():
#             print ('\n', result2, '\n')
#             return jsonify({ 'error': '<strong>Error:</strong> Your article could not be saved. Please make sure the fields are filled out correctly.' })

#         else:
#             connection.request('DELETE', '/1/classes/InProgress/'+articleID, '', {
#                 "X-Parse-Application-Id": PARSEappID,
#                 "X-Parse-REST-API-Key": RESTapiKEY
#             })
           
#             result3 = json.loads(connection.getresponse().read().decode('utf-8'))

#             if 'error' not in result3.keys():
#                 return jsonify({ 'success': 'The article has been successfully saved. You will now be redirected to the dashboard.' })

#             else:
#                 return jsonify({ 'error': "Could not delete article" })

#     return render_template("editor_write.html")

# @require_POST()
# def publish(request):
#     articleID = request.form.get('id', None)

#     # get the article from Queue
#     connection.connect()
#     connection.request('GET', '/1/classes/Queue/'+articleID, '', {
#         "X-Parse-Application-Id": PARSEappID,
#         "X-Parse-REST-API-Key": RESTapiKEY
#     })
#     result = json.loads(connection.getresponse().read().decode('utf-8'))

#     # change it's status
#     result['status'] = 'published'
#     del result['objectId']
#     del result['createdAt']
#     del result['updatedAt']

#     sluglist = result['slug'].split('-')

#     searchlist = result['tags'] + result['category'] + sluglist
#     result['search'] = [x.lower() for x in searchlist]

#     print ('\n', result, '\n')

#     # put it in the Articles table
#     connection.request('POST', '/1/classes/Articles/', json.dumps(result), {
#         "X-Parse-Application-Id": PARSEappID,
#         "X-Parse-REST-API-Key": RESTapiKEY,
#         "Content-Type": "application/json"
#     })
#     result2 = json.loads(connection.getresponse().read().decode('utf-8'))

#     # make sure everything went smoothly
#     if 'error' in result2.keys():
#         print (result2)
#         return jsonify({ 'error': 'error' })

#     else:
#         connection.request('DELETE', '/1/classes/Queue/'+articleID, '', {
#             "X-Parse-Application-Id": PARSEappID,
#             "X-Parse-REST-API-Key": RESTapiKEY
#         })
       
#         result3 = json.loads(connection.getresponse().read().decode('utf-8'))

#         if 'error' not in result3.keys():
#             print ('success')
#             return jsonify({ 'success': 'successful' })

#         else:
#             print (result3)
#             return jsonify({ 'error': "Could not delete article" })

# @require_POST()
# def delete(request):
#     articleID = request.form.get('id', None)
#     table = request.form.get('table', None)

#     print ('\n', articleID, '\n')

#     connection.connect()
#     connection.request('DELETE', '/1/classes/'+ table +'/'+articleID, '', {
#         "X-Parse-Application-Id": PARSEappID,
#         "X-Parse-REST-API-Key": RESTapiKEY
#     })
   
#     result = json.loads(connection.getresponse().read().decode('utf-8'))

#     if 'error' in result.keys():
#         return jsonify({ 'error': "Could not delete article" })

#     else:
#         return jsonify({ 'success': "This article has been deleted. You will now be redirected to the dashboard." })




