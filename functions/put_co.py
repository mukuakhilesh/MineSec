from firebase import firebase

co = 87879

firebase = firebase.FirebaseApplication('https://ddfgte-8fc94.firebaseio.com/',authentication=None)
firebase.put('mines','co',co)
#print (put)
