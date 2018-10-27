from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseNotAllowed
from django.views.decorators.csrf import csrf_exempt
import json
import statistics

@csrf_exempt
def val_payment(request):
	if request.method == "POST":
		d = request.POST
		data = None
		# transaction = data['transaction']
		for key in d.keys():
			data = json.loads(key)
		print(dict(data))
		# call ML pay validation function for transaction validation. Set value to "val"
		val = True
		if val:
			return JsonResponse({'status':'success', 'access':'True'})
		else:
			return JsonResponse({'status':'success', 'access':'False'})
	else:
		return HttpResponseNotAllowed(['POST'])

@csrf_exempt
def login_user(request):
	if request.method == "POST":
		d = request.POST
		data = None
		for key in d.keys():
			data = json.loads(key)
		# print(dict(data))
		usr_name = json.loads(data['user'])
		usr_pass = json.loads(data['pass'])
		print(usr_name)
		user = [(chr(i['character']), i['time']) for i in usr_name]
		password = [(chr(i['character']), i['time']) for i in usr_pass]
		# print(user)
		# print(password)
		# call ML Typing validation function. Set value to "val"
		val = True
		if val:
			return JsonResponse({'status':'success', 'access':'True'})
		else:
			return JsonResponse({'status':'success', 'access':'False'})
	else:
		return HttpResponseNotAllowed(['POST'])


counter = 0
l = []
p = []
train_l = []
train_p = []
@csrf_exempt
def gen_typing_data(request):
	global counter, l, p, train_p, train_l
	if request.method == "POST":
		d = request.POST
		data = None
		for key in d.keys():
			data = json.loads(key)
		# print(dict(data))
		usr_name = json.loads(data['user'])
		usr_pass = json.loads(data['pass'])
		print(usr_name)
		user = [(chr(i['character']), i['time']) for i in usr_name]
		password = [(chr(i['character']), i['time']) for i in usr_pass]
		if counter==0:
			for i in range(len(user)):
				l.append([])
			for i in range(len(password)):
				p.append([])

		for ur in range(len(user)):
			l[ur].append(user[ur][1])
		for pr in range(len(password)):
			p[pr].append(password[pr][1])

		counter+=1
		if counter == 8:
			counter = 0
			mean1 = []
			std1 = []
			for i in l:
				std1.append(statistics.stdev(i))
			for i in l:
				mean1.append(statistics.mean(i))
			train_l.append(std1)
			train_l.append(mean1)
			mean2 = []
			std2 = []
			for i in p:
				std2.append(statistics.stdev(i))
			for i in p:
				mean2.append(statistics.mean(i))
			train_p.append(std2)
			train_p.append(mean2)
			# Call training function ML
			print(l)
			print(p)
			print(train_l)
			print(train_p)
		print(counter)
		return JsonResponse({'status':'success', 'access':'True'})
	else:
		return HttpResponseNotAllowed(['POST'])